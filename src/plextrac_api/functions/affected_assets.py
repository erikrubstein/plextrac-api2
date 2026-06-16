"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def import_finding_affected_assets(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected-assets/import/{source}\n\nPlexTrac endpoint: Import Finding Affected Assets"""
    return endpoint_request(session, "affected_assets", "import_finding_affected_assets", **kwargs)


def remove_affected_asset_from_flaw(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}\n\nPlexTrac endpoint: Remove Affected Asset from Flaw"""
    return endpoint_request(session, "affected_assets", "remove_affected_asset_from_flaw", **kwargs)


def bulk_get_affected_assets_status(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/client/{clientId}/report/{reportId}/flaw/{findingId}/assets/status\n\nPlexTrac endpoint: Bulk Get Affected Assets Status"""
    return endpoint_request(session, "affected_assets", "bulk_get_affected_assets_status", **kwargs)


def get_affected_asset_status_list(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status\n\nPlexTrac endpoint: Get Affected Asset Status List"""
    return endpoint_request(session, "affected_assets", "get_affected_asset_status_list", **kwargs)


def create_affected_asset_status(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status/update\n\nPlexTrac endpoint: Create Affected Asset Status"""
    return endpoint_request(session, "affected_assets", "create_affected_asset_status", **kwargs)


def bulk_create_affected_asset_status(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/status\n\nPlexTrac endpoint: Bulk Create Affected Asset Status"""
    return endpoint_request(session, "affected_assets", "bulk_create_affected_asset_status", **kwargs)

