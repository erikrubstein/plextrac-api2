from __future__ import annotations

import json
from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.clients import (
    Client,
    ClientFilter,
    ClientFindingFilter,
    ClientFindingPage,
    ClientFindingSort,
    ClientInput,
    ClientPage,
    ClientPagination,
    ClientSort,
    ClientUser,
    ClientUserAssignment,
)
from plextrac_api.types.common import (
    JsonDict,
    OperationResult,
)


def list_client_users(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
) -> list[ClientUser]:
    """List users who already have access to a client."""
    data = rest_request(session, "GET", f"/api/v2/tenants/{tenant_id}/clients/{client_id}/users")
    return [ClientUser.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def list_available_tenant_users(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
) -> list[ClientUser]:
    """List tenant users who can be assigned to a client."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/client/{client_id}/users/available")
    return [ClientUser.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def assign_users_to_client(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    users: list[ClientUserAssignment],
) -> OperationResult:
    """Assign existing tenant users to a client by username."""
    data = rest_request(session, "POST", f"/api/v2/tenant/{tenant_id}/client/{client_id}/user/assign", json={"users": [user.to_assign_api() for user in users]})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_assign_users_to_client(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    users: list[ClientUserAssignment],
) -> OperationResult:
    """Bulk assign client users with email/name/classification payloads."""
    data = rest_request(session, "POST", f"/api/v2/tenant/{tenant_id}/client/{client_id}/bulk/users/assign", json=[user.to_bulk_api() for user in users])
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def remove_users_from_client(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    usernames: list[str],
) -> OperationResult:
    """Remove users from a client by username."""
    data = rest_request(session, "POST", f"/api/v1/tenant/{tenant_id}/client/{client_id}/user/remove", data={"users": json.dumps([{"username": username} for username in usernames])})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_tenant_clients(
    session: AuthSession,
    tenant_id: int | str,
) -> list[Client]:
    """List clients for a specific tenant using the tenant-scoped endpoint."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/client/list")
    if isinstance(data, list):
        return [Client.from_api(item) for item in data if isinstance(item, dict)]
    return ClientPage.from_api(data if isinstance(data, dict) else {"data": data}).clients


def list_clients(
    session: AuthSession,
    *,
    pagination: ClientPagination | None = None,
    sort: list[ClientSort] | None = None,
    filters: list[ClientFilter] | None = None,
) -> ClientPage:
    """List clients with the latest paginated, sortable, filterable endpoint."""
    payload: JsonDict = {
        "pagination": (pagination or ClientPagination()).to_api(),
        "sort": [item.to_api() for item in sort] if sort is not None else None,
        "filters": [item.to_api() for item in filters] if filters is not None else None,
    }
    payload = {key: value for key, value in payload.items() if value is not None}
    data = rest_request(session, "POST", "/api/v2/clients", json=payload)
    return ClientPage.from_api(data if isinstance(data, dict) else {"data": data})


def get_client(
    session: AuthSession,
    client_id: int | str,
) -> Client:
    """Get one client by client ID."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac get client response was not a JSON object.")
    return Client.from_api(data)


def create_client(
    session: AuthSession,
    client: ClientInput,
) -> OperationResult:
    """Create a client from a reusable ClientInput payload."""
    if client.name is None:
        raise TypeError("create_client requires client.name.")
    data = rest_request(session, "POST", "/api/v1/client/create", json=client.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_client(
    session: AuthSession,
    client_id: int | str,
    client: ClientInput,
) -> OperationResult:
    """Update a client from a reusable ClientInput payload."""
    data = rest_request(session, "PUT", f"/api/v1/client/{client_id}", json=client.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_client(
    session: AuthSession,
    client_id: int | str,
) -> OperationResult:
    """Delete a client by client ID."""
    data = rest_request(session, "DELETE", f"/api/v1/client/{client_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def add_client_logo(
    session: AuthSession,
    client_id: int | str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> OperationResult:
    """Upload a logo file for a client."""
    close_after = None
    if isinstance(file, (str, Path)):
        path = Path(file)
        close_after = path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "logo")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        data = rest_request(session, "POST", f"/api/v1/client/{client_id}/logo", files=files)
    finally:
        if close_after is not None:
            close_after.close()
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_client_logo(
    session: AuthSession,
    client_id: int | str,
) -> OperationResult:
    """Delete a client's logo."""
    data = rest_request(session, "DELETE", f"/api/v1/client/{client_id}/logo")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_client_findings(
    session: AuthSession,
    client_id: int | str,
    *,
    pagination: ClientPagination | None = None,
    sort: list[ClientFindingSort] | None = None,
    filters: list[ClientFindingFilter] | None = None,
) -> ClientFindingPage:
    """List findings for a client with pagination, sorting, and filters."""
    payload: JsonDict = {
        "pagination": (pagination or ClientPagination()).to_api(),
        "sort": [item.to_api() for item in sort] if sort is not None else None,
        "filters": [item.to_api() for item in filters] if filters is not None else None,
    }
    data = rest_request(session, "POST", f"/api/v2/client/{client_id}/findings", json={key: value for key, value in payload.items() if value is not None})
    return ClientFindingPage.from_api(data if isinstance(data, (dict, list)) else {"data": data})
