from __future__ import annotations

import re
import time
from collections.abc import Mapping
from typing import Any

import httpx

from plextrac_api.generated.endpoints import GROUPS
from plextrac_api.types.auth import REFRESH_WITHIN_SECONDS, AuthSession, _jwt_expiration
from plextrac_api.types.common import JsonDict


class PlexTracError(Exception):
    pass


class PlexTracAuthError(PlexTracError):
    pass


class PlexTracGraphQLError(PlexTracError):
    pass


class PlexTracNotFoundError(PlexTracError):
    pass


class PlexTracPermissionError(PlexTracError):
    pass


class PlexTracRateLimitError(PlexTracError):
    pass


PLACEHOLDER_RE = re.compile(r"(\{\{?)([A-Za-z0-9_]+)(\}?\})")

def build_auth_headers(session: AuthSession | None = None) -> dict[str, str]:
    headers = {"Accept": "application/json", "User-Agent": "plextrac-api2/0.1.0"}
    if session is not None:
        headers["Authorization"] = f"Bearer {session.token}"
    return headers


def rest_request(
    session: AuthSession,
    method: str,
    path: str,
    *,
    params: Mapping[str, Any] | None = None,
    json: Any | None = None,
    data: Any | None = None,
    files: Any | None = None,
    headers: Mapping[str, str] | None = None,
    content: Any | None = None,
    stream: bool = False,
    authenticated: bool = True,
) -> Any:
    request_headers = dict(headers or {})
    if authenticated:
        if _is_expired(session):
            raise PlexTracAuthError("PlexTrac token has expired; create a new session.")
        if session.is_expiring(within_seconds=REFRESH_WITHIN_SECONDS):
            refresh_session(session)
        request_headers = {**build_auth_headers(session), **request_headers}

    response = _send(
        session,
        method,
        path,
        params=params,
        json=json,
        data=data,
        files=files,
        headers=request_headers,
        content=content,
    )
    if response.status_code == 401 and authenticated and _can_retry_refresh_after_401(session):
        refresh_session(session)
        request_headers = {**build_auth_headers(session), **dict(headers or {})}
        response = _send(
            session,
            method,
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=request_headers,
            content=content,
        )
    return _parse_response(response, stream=stream)


def endpoint_request(
    session: AuthSession,
    group: str,
    endpoint_name: str,
    **kwargs: Any,
) -> Any:
    endpoint = _endpoint(group, endpoint_name)
    path_params = dict(kwargs.pop("path_params", {}) or {})
    params = dict(endpoint.get("default_params") or [])
    params.update(kwargs.pop("params", {}) or {})

    json_body = kwargs.pop("json", None)
    data = kwargs.pop("data", None)
    files = kwargs.pop("files", None)
    headers = kwargs.pop("headers", None)
    content = kwargs.pop("content", None)
    stream = bool(kwargs.pop("stream", False))
    authenticated = bool(kwargs.pop("authenticated", True))

    path = endpoint["path"]
    for key in _placeholders(path):
        if key in kwargs:
            path_params[key] = kwargs.pop(key)
    path = _interpolate(path, path_params)

    for key, value in list(params.items()):
        if isinstance(value, str):
            params[key] = _interpolate(value, {**path_params, **kwargs}, strict=False)

    body_mode = endpoint.get("body_mode")
    graphql_query = endpoint.get("graphql_query")
    if json_body is None and graphql_query:
        variables = kwargs.pop("variables", None) or kwargs
        kwargs = {}
        json_body = {"query": graphql_query, "variables": variables}
    elif json_body is None and kwargs:
        if endpoint["method"] in {"GET", "DELETE"} or body_mode == "none":
            params.update(kwargs)
        elif body_mode == "formdata":
            data = data or kwargs
        else:
            json_body = kwargs

    return rest_request(
        session,
        endpoint["method"],
        path,
        params={key: value for key, value in params.items() if value is not None},
        json=json_body,
        data=data,
        files=files,
        headers=headers,
        content=content,
        stream=stream,
        authenticated=authenticated,
    )


def graphql_request(
    session: AuthSession,
    operation_name: str | None,
    query: str,
    variables: JsonDict | None = None,
) -> JsonDict:
    payload: JsonDict = {"query": query, "variables": variables or {}}
    if operation_name:
        payload["operationName"] = operation_name
    response_data = rest_request(session, "POST", "/graphql", json=payload)
    if not isinstance(response_data, dict):
        raise PlexTracGraphQLError("PlexTrac GraphQL response was not a JSON object.")
    errors = response_data.get("errors")
    if errors:
        raise PlexTracGraphQLError(str(errors))
    data = response_data.get("data")
    if not isinstance(data, dict):
        raise PlexTracGraphQLError("PlexTrac GraphQL response did not include data.")
    return data


def execute_graphql(
    session: AuthSession,
    query: str,
    *,
    variables: JsonDict | None = None,
    operation_name: str | None = None,
) -> JsonDict:
    return graphql_request(session, operation_name, query, variables)


def refresh_session(session: AuthSession) -> AuthSession:
    response = _send(
        session,
        "PUT",
        "/api/v1/token/refresh",
        json=None,
        headers=build_auth_headers(session),
    )
    data = _parse_response(response)
    if not isinstance(data, dict):
        raise PlexTracAuthError("Refresh response was not a JSON object.")
    token = _first_string(data, ("token", "jwt", "jwtToken", "accessToken", "access_token"))
    cookie = _first_string(data, ("cookie",))
    refresh_token = _first_string(data, ("refreshToken", "refresh_token"))
    tenant_id = _first_value(data, ("tenant_id", "tenantId"))
    if not token:
        raise PlexTracAuthError("Refresh response did not include a token.")
    session.token = token
    if cookie:
        session.cookie = cookie
    session.expires_at = _jwt_expiration(token)
    if refresh_token:
        session.refresh_token = refresh_token
    if isinstance(tenant_id, (int, str)):
        session.tenant_id = tenant_id
    return session


def _send(session: AuthSession, method: str, path: str, **kwargs: Any) -> httpx.Response:
    url = path if path.startswith(("http://", "https://")) else f"{session.base_url}{path}"
    with httpx.Client(timeout=30.0) as client:
        return client.request(method, url, **kwargs)


def _parse_response(response: httpx.Response, *, stream: bool = False) -> Any:
    if response.status_code >= 400:
        error_cls = PlexTracError
        if response.status_code == 401:
            error_cls = PlexTracAuthError
        elif response.status_code == 403:
            error_cls = PlexTracPermissionError
        elif response.status_code == 404:
            error_cls = PlexTracNotFoundError
        elif response.status_code == 429:
            error_cls = PlexTracRateLimitError
        raise error_cls(_response_error(response))
    if stream:
        return response
    if response.status_code == 204 or not response.content:
        return None
    content_type = response.headers.get("content-type", "")
    if "application/json" in content_type or response.text[:1] in {"{", "["}:
        return response.json()
    return response.content


def _response_error(response: httpx.Response) -> str:
    try:
        data = response.json()
    except Exception:
        return response.text or f"PlexTrac request failed with HTTP {response.status_code}."
    if isinstance(data, dict):
        return str(
            data.get("message")
            or data.get("error")
            or data.get("detail")
            or f"PlexTrac request failed with HTTP {response.status_code}."
        )
    return str(data)


def _endpoint(group: str, endpoint_name: str) -> JsonDict:
    for endpoint in GROUPS[group]["endpoints"]:
        if endpoint["method_name"] == endpoint_name:
            return endpoint
    raise KeyError(f"Unknown endpoint {group}.{endpoint_name}")


def _placeholders(value: str) -> set[str]:
    return {match.group(2) for match in PLACEHOLDER_RE.finditer(value)}


def _interpolate(value: str, replacements: Mapping[str, Any], *, strict: bool = True) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(2)
        if key in replacements:
            return str(replacements[key])
        if strict:
            raise TypeError(f"Missing required path parameter: {key}")
        return match.group(0)

    return PLACEHOLDER_RE.sub(replace, value)


def _is_expired(session: AuthSession) -> bool:
    return session.expires_at is not None and time.time() >= session.expires_at


def _can_retry_refresh_after_401(session: AuthSession) -> bool:
    return session.expires_at is None


def _first_string(data: JsonDict, keys: tuple[str, ...]) -> str | None:
    nested = data.get("data")
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    if isinstance(nested, dict):
        for key in keys:
            value = nested.get(key)
            if isinstance(value, str) and value:
                return value
    return None


def _first_value(data: JsonDict, keys: tuple[str, ...]) -> object:
    nested = data.get("data")
    for key in keys:
        if key in data:
            return data[key]
    if isinstance(nested, dict):
        for key in keys:
            if key in nested:
                return nested[key]
    return None
