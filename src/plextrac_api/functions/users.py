"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def get_authenticated_user(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/whoami\n\nPlexTrac endpoint: Get Authenticated User v2"""
    return endpoint_request(session, "users", "get_authenticated_user", **kwargs)


def list_tenant_users(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/user/list\n\nPlexTrac endpoint: List Tenant Users"""
    return endpoint_request(session, "users", "list_tenant_users", **kwargs)


def get_tenants_users(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenants/{tenantId}/users\n\nPlexTrac endpoint: Get Tenants Users"""
    return endpoint_request(session, "users", "get_tenants_users", **kwargs)


def create_user_deprecated(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/user/create\n\nPlexTrac endpoint: Create User (DEPRECATED)"""
    return endpoint_request(session, "users", "create_user_deprecated", **kwargs)


def bulk_create_user(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/user/create/bulk\n\nPlexTrac endpoint: Bulk Create User"""
    return endpoint_request(session, "users", "bulk_create_user", **kwargs)


def update_user(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/user/update\n\nPlexTrac endpoint: Update User"""
    return endpoint_request(session, "users", "update_user", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_user`."""
    return update_user(session, **kwargs)


def delete_user(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/user/delete\n\nPlexTrac endpoint: Delete User"""
    return endpoint_request(session, "users", "delete_user", **kwargs)


def delete(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `delete_user`."""
    return delete_user(session, **kwargs)


def change_password(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/user/changepass\n\nPlexTrac endpoint: Change Password"""
    return endpoint_request(session, "users", "change_password", **kwargs)


def forgot_password(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/user/forgotpass\n\nPlexTrac endpoint: Forgot Password"""
    return endpoint_request(session, "users", "forgot_password", **kwargs)


def reset_user_password(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/user/resetpass\n\nPlexTrac endpoint: Reset User Password"""
    return endpoint_request(session, "users", "reset_user_password", **kwargs)


def set_mfa_token(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/user/mfa/token\n\nPlexTrac endpoint: Set MFA Token"""
    return endpoint_request(session, "users", "set_mfa_token", **kwargs)


def disable_user_mfa_token(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/user/mfa/token/disable\n\nPlexTrac endpoint: Disable User MFA Token"""
    return endpoint_request(session, "users", "disable_user_mfa_token", **kwargs)


def disable_other_user_mfa_token(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/user/mfa/disable\n\nPlexTrac endpoint: Disable Other User MFA Token"""
    return endpoint_request(session, "users", "disable_other_user_mfa_token", **kwargs)


def enable_disable_user(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/user/toggledisabled\n\nPlexTrac endpoint: Enable/Disable User"""
    return endpoint_request(session, "users", "enable_disable_user", **kwargs)


def get_user_notifications(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/user/notifications\n\nPlexTrac endpoint: Get User Notifications"""
    return endpoint_request(session, "users", "get_user_notifications", **kwargs)


def set_user_notifications_read(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/user/notifications\n\nPlexTrac endpoint: Set User Notifications Read"""
    return endpoint_request(session, "users", "set_user_notifications_read", **kwargs)


def get_user_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/user/findings\n\nPlexTrac endpoint: Get User Findings"""
    return endpoint_request(session, "users", "get_user_findings", **kwargs)

