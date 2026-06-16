"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def update_settings(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenants/{tenantId}/settings\n\nPlexTrac endpoint: Update settings"""
    return endpoint_request(session, "tenant", "update_settings", **kwargs)


def get_tenant(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}\n\nPlexTrac endpoint: Get Tenant"""
    return endpoint_request(session, "tenant", "get_tenant", **kwargs)


def get(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `get_tenant`."""
    return get_tenant(session, **kwargs)


def update_tenant(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}\n\nPlexTrac endpoint: Update Tenant"""
    return endpoint_request(session, "tenant", "update_tenant", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_tenant`."""
    return update_tenant(session, **kwargs)


def get_notification_settings(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/notificationsettings\n\nPlexTrac endpoint: Get Notification Settings"""
    return endpoint_request(session, "tenant", "get_notification_settings", **kwargs)


def update_notification_settings(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/notificationsettings\n\nPlexTrac endpoint: Update Notification Settings"""
    return endpoint_request(session, "tenant", "update_notification_settings", **kwargs)


def tenant_analytics(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/analytics\n\nPlexTrac endpoint: Tenant Analytics"""
    return endpoint_request(session, "tenant", "tenant_analytics", **kwargs)


def add_tenant_logo(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/logo\n\nPlexTrac endpoint: Add Tenant Logo"""
    return endpoint_request(session, "tenant", "add_tenant_logo", **kwargs)


def add_tenant_logo_dark(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/logo/dark\n\nPlexTrac endpoint: Add Tenant Logo Dark"""
    return endpoint_request(session, "tenant", "add_tenant_logo_dark", **kwargs)


def delete_tenant_logo(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/logo\n\nPlexTrac endpoint: Delete Tenant Logo"""
    return endpoint_request(session, "tenant", "delete_tenant_logo", **kwargs)


def delete_tenant_logo_dark(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/logo/dark\n\nPlexTrac endpoint: Delete Tenant Logo Dark"""
    return endpoint_request(session, "tenant", "delete_tenant_logo_dark", **kwargs)


def delete_tenant_icon(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/icon\n\nPlexTrac endpoint: Delete Tenant Icon"""
    return endpoint_request(session, "tenant", "delete_tenant_icon", **kwargs)


def delete_tenant_icon_dark(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/icon/dark\n\nPlexTrac endpoint: Delete Tenant Icon Dark"""
    return endpoint_request(session, "tenant", "delete_tenant_icon_dark", **kwargs)


def root_request(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/\n\nPlexTrac endpoint: Root Request"""
    return endpoint_request(session, "tenant", "root_request", **kwargs)

