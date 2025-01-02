import json
from datetime import datetime
from functools import wraps
from io import BytesIO
import traceback
from urllib.parse import quote

import urllib3
from urllib import parse

from sharepoint_wrapper._constants import SCOPE


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper


http = urllib3.PoolManager()


def get_graph_token(
    tenant_domain: str, client_id: str, client_secret: str
) -> tuple[str, datetime]:
    url = f"https://login.microsoftonline.com/{tenant_domain}/oauth2/v2.0/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": SCOPE,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    try:
        response = http.request(
            "POST",
            url,
            headers=headers,
            body=parse.urlencode(data),
            retries=False,  # Disable automatic retries
        )
        response_data = json.loads(response.data.decode("utf-8"))

        if response.status != 200:
            error_description = response_data.get("error_description", "Unknown error")
            raise Exception(error_description)

        token = response_data.get("access_token", None)
        expires_in = response_data.get("expires_in", None)  # in seconds
        if expires_in is not None:
            expires_in = datetime.fromtimestamp(datetime.now().timestamp() + expires_in)

        return token, expires_in

    except Exception as e:
        raise Exception(f"Error during token retrieval: {str(e)}")


def get_site(tenant: str, site: str, token: str) -> str:
    url = (
        f"https://graph.microsoft.com/v1.0/sites/{tenant}.sharepoint.com:/sites/{site}"
    )
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = http.request(
            "GET",
            url,
            headers=headers,
            retries=False,  # Disable automatic retries
        )
        response_data = json.loads(response.data.decode("utf-8"))

        if response.status != 200:
            error_description = response_data["error"]["message"]
            raise Exception(error_description)

        site_id = response_data.get("id", None)
        return site_id

    except Exception as e:
        raise Exception(f"Invalid Site: {str(e)}")


def get_drives(site_id: str, token: str) -> list[str]:
    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = http.request(
            "GET",
            url,
            headers=headers,
            retries=False,  # Disable automatic retries
        )
        response_data = json.loads(response.data.decode("utf-8"))

        if response.status != 200:
            error_description = response_data["error"]["message"]
            raise Exception(error_description)

        raw_drives = response_data.get("value", None)
        drives = []
        if raw_drives is not None:
            drives = [(d.get("id"), d.get("name")) for d in raw_drives]

        return drives

    except Exception as e:
        raise Exception(f"Invalid Site: {str(e)}")


def build_query_string(
    filter_params: dict | None = None,
    sort_params: list | None = None,
) -> str:
    """
    Build OData query string for filtering and sorting.
    """
    query_parts = []

    if filter_params:
        filter_conditions = " and ".join(filter_params)
        query_parts.append(f"$filter={quote(filter_conditions)}")

    if sort_params:
        sort_string = ",".join(sort_params)
        query_parts.append(f"$orderby={quote(sort_string)}")

    return "&".join(query_parts)


def get_children(
    drive_id,
    token,
    base_path: str | None = None,
    category: str | None = None,
    filter_params: list | None = None,
    sort_params: list | None = None,
    detailed_response: bool | None = False,
):
    """
    Get Children.
    None : All | folder : Folders only | file : Files only
    """
    if base_path is not None and not base_path.startswith("/"):
        raise Exception("Base path must always begin with a slash /")
    base_path = "" if base_path is None else f":{base_path}:"
    base_url = (
        f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root{base_path}/children"
    )
    query_string = build_query_string(filter_params, sort_params)
    url = f"{base_url}?{query_string}" if query_string else base_url

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "ConsistencyLevel": "eventual",
    }

    try:
        response = http.request(
            "GET",
            url,
            headers=headers,
            retries=False,  # Disable automatic retries
        )
        response_data = json.loads(response.data.decode("utf-8"))

        if response.status != 200:
            error_description = response_data["error"]["message"]
            raise Exception(error_description)

        raw_drives = response_data.get("value", None)
        if raw_drives is None:
            return []

        if not detailed_response:
            return [
                {
                    "name": d.get("name"),
                    "webUrl": d.get("webUrl"),
                    "type": (
                        "folder"
                        if "folder" in d
                        else "file" if "file" in d else "unknown"
                    ),
                }
                for d in raw_drives
                if (category is None) or (category is not None and category in d)
            ]

        return [
            {
                "name": d.get("name"),
                "webUrl": d.get("webUrl"),
                "type": (
                    "folder" if "folder" in d else "file" if "file" in d else "unknown"
                ),
                "createdDateTime": d.get("createdDateTime"),
                "lastModifiedDateTime": d.get("lastModifiedDateTime"),
                "createdBy": {
                    "email": keys_exists(d, "createdBy", "user", "email"),
                    "displayName": keys_exists(d, "createdBy", "user", "displayName"),
                },
                "lastModifiedBy": {
                    "email": keys_exists(d, "lastModifiedBy", "user", "email"),
                    "displayName": keys_exists(
                        d, "lastModifiedBy", "user", "displayName"
                    ),
                },
            }
            for d in raw_drives
            if (category is None) or (category is not None and category in d)
        ]

    except Exception as e:
        raise Exception(f"Invalid Site: {str(e)}")


def keys_exists(element, *keys):
    """
    Check if *keys (nested) exists in `element` (dict).
    """
    if not isinstance(element, dict):
        raise AttributeError("keys_exists() expects dict as first argument.")
    if len(keys) == 0:
        raise AttributeError("keys_exists() expects at least two arguments, one given.")

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return None
    return _element


def get_file(
    drive_id: str,
    token: str,
    file_name: str,
    base_path: str | None = None,
) -> BytesIO:
    """
    Get File.
    """
    if base_path is not None and not base_path.startswith("/"):
        raise Exception("Base path must always begin with a slash /")

    path = (base_path or "") + "/" + file_name

    path = f":{path}:"
    url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root{path}/content"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = http.request(
            "GET",
            url,
            headers=headers,
            # retries=False,  # Disable automatic retries
        )

        if response.status != 200:
            response_data = json.loads(response.data.decode("utf-8"))
            error_description = response_data["error"]["message"]
            raise Exception(error_description)

        return BytesIO(response.data)

    except Exception as e:
        raise Exception(f"Invalid Site: {str(e)}")


def write_file(
    drive_id: str, token: str, file_content: BytesIO, file_name: str, base_path: str
) -> dict:
    """
    Write file to a location.
    """
    if base_path is not None and not base_path.startswith("/"):
        raise Exception("Base path must always begin with a slash /")

    path = (base_path or "") + "/" + file_name

    path = f":{path}:"
    url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root{path}/content"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = http.request(
            "PUT",
            url,
            headers=headers,
            body=file_content,
            # retries=False,  # Disable automatic retries
        )

        response_data = json.loads(response.data.decode("utf-8"))

        if response.status not in (201, 200):
            error_description = response_data["error"]["message"]
            raise Exception(error_description)

        return response_data

    except Exception as e:
        print(traceback.format_exc())
        raise Exception(f"Error uploading file: {str(e)}")
