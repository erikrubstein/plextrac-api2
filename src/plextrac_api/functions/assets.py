"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def get_tenant_assets(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenant/assets\n\nPlexTrac endpoint: Get Tenant Assets"""
    return endpoint_request(session, "assets", "get_tenant_assets", **kwargs)


def get_assets_by_client(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/{clientId}/assets\n\nPlexTrac endpoint: Get Assets by Client"""
    return endpoint_request(session, "assets", "get_assets_by_client", **kwargs)


def list_client_assets(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/assets\n\nPlexTrac endpoint: List Client Assets"""
    return endpoint_request(session, "assets", "list_client_assets", **kwargs)


def list_report_assets(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/clients/{clientId}/reports/{reportId}/assets\n\nPlexTrac endpoint: List Report Assets"""
    return endpoint_request(session, "assets", "list_report_assets", **kwargs)


def get_asset(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/asset/{assetId}\n\nPlexTrac endpoint: Get Asset"""
    return endpoint_request(session, "assets", "get_asset", **kwargs)


def get(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `get_asset`."""
    return get_asset(session, **kwargs)


def create_asset(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/client/{clientId}/asset/0\n\nPlexTrac endpoint: Create Asset"""
    return endpoint_request(session, "assets", "create_asset", **kwargs)


def create(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `create_asset`."""
    return create_asset(session, **kwargs)


def update_asset(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/client/{clientId}/asset/{assetId}\n\nPlexTrac endpoint: Update Asset"""
    return endpoint_request(session, "assets", "update_asset", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_asset`."""
    return update_asset(session, **kwargs)


def delete_asset(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/client/{clientId}/asset/{assetId}\n\nPlexTrac endpoint: Delete Asset"""
    return endpoint_request(session, "assets", "delete_asset", **kwargs)


def delete(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `delete_asset`."""
    return delete_asset(session, **kwargs)


def import_client_assets(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/client/{clientId}/assets/import/{source}\n\nPlexTrac endpoint: Import Client Assets v2"""
    return endpoint_request(session, "assets", "import_client_assets", **kwargs)


def bulk_delete_client_assets(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/bulk/assets/delete\n\nPlexTrac endpoint: Bulk Delete Client Assets"""
    return endpoint_request(session, "assets", "bulk_delete_client_assets", **kwargs)


def get_scanner_output(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput\n\nPlexTrac endpoint: Get Scanner Output"""
    return endpoint_request(session, "assets", "get_scanner_output", **kwargs)

