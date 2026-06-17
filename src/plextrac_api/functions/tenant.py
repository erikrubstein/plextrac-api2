from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.findings import FindingVisibility
from plextrac_api.types.tenant import (
    NotificationSettings,
    RootInfo,
    Tenant,
    TenantAnalytics,
)


def update_settings(
    session: AuthSession,
    tenant_id: int | str,
    *,
    visibility: FindingVisibility | None = None,
    sender_email_address: str | None = None,
) -> OperationResult:
    """Update tenant-level settings."""
    payload = {
        "visibility": visibility.value if visibility is not None else None,
        "senderEmailAddress": sender_email_address,
    }
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/tenants/{tenant_id}/settings",
        json={key: value for key, value in payload.items() if value is not None},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_tenant(
    session: AuthSession,
    tenant_id: int | str,
) -> Tenant:
    """Get tenant profile and settings."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac tenant response was not a JSON object.")
    return Tenant.from_api(data)


def update_tenant(
    session: AuthSession,
    tenant_id: int | str,
    *,
    name: str | None = None,
    address: str | None = None,
) -> OperationResult:
    """Update tenant profile fields."""
    params = {
        "name": name,
        "address": address,
    }
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}",
        params={key: value for key, value in params.items() if value is not None},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_notification_settings(
    session: AuthSession,
    tenant_id: int | str,
) -> NotificationSettings:
    """Get tenant finding-status reminder settings."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/notificationsettings")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac notification settings response was not a JSON object.")
    return NotificationSettings.from_api(data)


def update_notification_settings(
    session: AuthSession,
    tenant_id: int | str,
    *,
    reminder_days: int,
) -> OperationResult:
    """Update tenant finding-status reminder settings."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/notificationsettings",
        params={"reminderDays": reminder_days},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_tenant_analytics(
    session: AuthSession,
    tenant_id: int | str,
) -> TenantAnalytics:
    """Get tenant risk analytics."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/analytics")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac tenant analytics response was not a JSON object.")
    return TenantAnalytics.from_api(data)


def upload_tenant_logo(
    session: AuthSession,
    tenant_id: int | str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> OperationResult:
    """Upload the tenant light-mode logo."""
    data = _upload_tenant_image(
        session,
        f"/api/v1/tenant/{tenant_id}/logo",
        file,
        filename=filename,
        content_type=content_type,
        fallback_name="tenant-logo",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def upload_tenant_dark_logo(
    session: AuthSession,
    tenant_id: int | str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> OperationResult:
    """Upload the tenant dark-mode logo."""
    data = _upload_tenant_image(
        session,
        f"/api/v1/tenant/{tenant_id}/logo/dark",
        file,
        filename=filename,
        content_type=content_type,
        fallback_name="tenant-dark-logo",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_tenant_logo(
    session: AuthSession,
    tenant_id: int | str,
) -> OperationResult:
    """Delete the tenant light-mode logo."""
    data = rest_request(session, "DELETE", f"/api/v1/tenant/{tenant_id}/logo")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_tenant_dark_logo(
    session: AuthSession,
    tenant_id: int | str,
) -> OperationResult:
    """Delete the tenant dark-mode logo."""
    data = rest_request(session, "DELETE", f"/api/v1/tenant/{tenant_id}/logo/dark")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_tenant_icon(
    session: AuthSession,
    tenant_id: int | str,
) -> OperationResult:
    """Delete the tenant light-mode icon."""
    data = rest_request(session, "DELETE", f"/api/v1/tenant/{tenant_id}/icon")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_tenant_dark_icon(
    session: AuthSession,
    tenant_id: int | str,
) -> OperationResult:
    """Delete the tenant dark-mode icon."""
    data = rest_request(session, "DELETE", f"/api/v1/tenant/{tenant_id}/icon/dark")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_root_info(
    session: AuthSession,
) -> RootInfo:
    """Check the instance root API response."""
    data = rest_request(session, "GET", "/api/v1/")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac root response was not a JSON object.")
    return RootInfo.from_api(data)


def _upload_tenant_image(
    session: AuthSession,
    path: str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None,
    content_type: str | None,
    fallback_name: str,
) -> object:
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", fallback_name)).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        return rest_request(session, "POST", path, files=files)
    finally:
        if close_after is not None:
            close_after.close()
