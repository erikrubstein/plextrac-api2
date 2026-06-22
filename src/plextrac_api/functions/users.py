from __future__ import annotations

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.users import (
    AuthenticatedUser,
    CurrentUserUpdate,
    TenantUser,
    TenantUserInput,
    TenantUserPage,
    UserFindingSearch,
    UserFindingSearchResult,
    UserNotification,
    UserNotificationReadFilter,
    UserSortField,
    UserSortOrder,
)


def get_authenticated_user(
    session: AuthSession,
) -> AuthenticatedUser:
    """Get the currently authenticated user."""
    data = rest_request(session, "GET", "/api/v2/whoami")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac authenticated user response was not a JSON object.")
    return AuthenticatedUser.from_api(data)


def list_tenant_users(
    session: AuthSession,
    tenant_id: int | str,
) -> list[TenantUser]:
    """List tenant users using the legacy unpaginated endpoint."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/user/list")
    return _user_list(data)


def list_tenant_users_paginated(
    session: AuthSession,
    tenant_id: int | str,
    *,
    offset: int = 0,
    limit: int = 10,
    sort_by: UserSortField = UserSortField.FIRST_NAME,
    order: UserSortOrder = UserSortOrder.DESCENDING,
    search: str | None = None,
) -> TenantUserPage:
    """List tenant users using the paginated endpoint."""
    params = {
        "offset": offset,
        "limit": limit,
        "sortBy": sort_by.value,
        "order": order.value,
        "filter": search,
    }
    data = rest_request(
        session,
        "GET",
        f"/api/v2/tenants/{tenant_id}/users",
        params={key: value for key, value in params.items() if value is not None},
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac tenant users response was not a JSON object.")
    return TenantUserPage.from_api(data)


def bulk_create_users(
    session: AuthSession,
    tenant_id: int | str,
    users: list[TenantUserInput],
) -> list[TenantUser]:
    """Bulk create tenant users."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/user/create/bulk",
        json=[user.to_api() for user in users],
    )
    return _user_list(data)


def update_user(
    session: AuthSession,
    update: CurrentUserUpdate,
) -> AuthenticatedUser:
    """Update the current user's profile information."""
    data = rest_request(session, "PUT", "/api/v1/user/update", json=update.to_api())
    if not isinstance(data, dict):
        raise ValueError("PlexTrac user update response was not a JSON object.")
    return AuthenticatedUser.from_api(data)


def delete_user(
    session: AuthSession,
    *,
    email: str,
) -> OperationResult:
    """Delete a user by email."""
    data = rest_request(session, "DELETE", "/api/v2/user/delete", json={"email": email})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def change_password(
    session: AuthSession,
    *,
    current_password: str,
    new_password: str,
) -> OperationResult:
    """Change the current user's password."""
    data = rest_request(
        session,
        "PUT",
        "/api/v1/user/changepass",
        json={"currentPassword": current_password, "newPassword": new_password},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def forgot_password(
    session: AuthSession,
    *,
    email: str,
) -> OperationResult:
    """Send a password recovery email."""
    data = rest_request(
        session,
        "POST",
        "/api/v1/user/forgotpass",
        json={"email": email},
        authenticated=False,
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def reset_user_password(
    session: AuthSession,
    tenant_id: int | str,
    *,
    email: str,
) -> OperationResult:
    """Send a tenant user a password reset email."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/user/resetpass",
        json={"email": email},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def set_mfa_token(
    session: AuthSession,
) -> OperationResult:
    """Set the current user's MFA token."""
    data = rest_request(session, "PUT", "/api/v1/user/mfa/token")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def disable_user_mfa_token(
    session: AuthSession,
) -> OperationResult:
    """Disable the current user's MFA token."""
    data = rest_request(session, "PUT", "/api/v1/user/mfa/token/disable")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def disable_tenant_user_mfa_token(
    session: AuthSession,
    tenant_id: int | str,
    *,
    email: str,
) -> OperationResult:
    """Disable MFA for another tenant user."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/user/mfa/disable",
        json={"email": email},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def set_user_disabled(
    session: AuthSession,
    tenant_id: int | str,
    *,
    email: str,
    disabled: bool,
) -> OperationResult:
    """Enable or disable a tenant user."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/tenant/{tenant_id}/user/toggledisabled",
        json={"email": email, "disabled": disabled},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_user_notifications(
    session: AuthSession,
    *,
    limit: int = 10,
    skip: int = 0,
    read: UserNotificationReadFilter = UserNotificationReadFilter.UNREAD,
) -> list[UserNotification]:
    """List notifications for the current user."""
    data = rest_request(
        session,
        "GET",
        "/api/v1/user/notifications",
        params={"limit": limit, "skip": skip, "read": read.value},
    )
    payload = _data_payload(data)
    return [
        UserNotification.from_api(item) for item in payload if isinstance(item, dict)
    ] if isinstance(payload, list) else []


def mark_user_notifications_read(
    session: AuthSession,
    notification_ids: list[int | str],
) -> OperationResult:
    """Mark user notifications as read."""
    data = rest_request(
        session,
        "PUT",
        "/api/v1/user/notifications",
        json={"notificationIds": notification_ids},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def search_user_findings(
    session: AuthSession,
    search: UserFindingSearch,
) -> UserFindingSearchResult:
    """List findings assigned to the current user."""
    data = rest_request(session, "POST", "/api/v2/user/findings", json=search.to_api())
    if not isinstance(data, dict):
        raise ValueError("PlexTrac user findings response was not a JSON object.")
    return UserFindingSearchResult.from_api(data)


def _user_list(data: object) -> list[TenantUser]:
    payload = _data_payload(data)
    return [TenantUser.from_api(item) for item in payload if isinstance(item, dict)] if isinstance(payload, list) else []


def _data_payload(data: object) -> object:
    if isinstance(data, dict) and "data" in data:
        return data["data"]
    return data
