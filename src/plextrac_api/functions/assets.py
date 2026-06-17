from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.assets import (
    Asset,
    AssetCreateResult,
    AssetImportSource,
    AssetInput,
    AssetPage,
    ClientAssetFilter,
    ClientAssetPageLimit,
    ClientAssetSort,
    TenantAssetFilter,
    TenantAssetPageLimit,
    TenantAssetSort,
)
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict, OperationResult


def list_tenant_assets(
    session: AuthSession,
    *,
    offset: int = 0,
    limit: TenantAssetPageLimit = TenantAssetPageLimit.TWENTY_FIVE,
    sort: list[TenantAssetSort] | None = None,
    filters: list[TenantAssetFilter] | None = None,
) -> AssetPage:
    """List tenant assets with documented pagination, sorting, and filters."""
    payload: JsonDict = {
        "pagination": {"offset": offset, "limit": int(limit)},
        "sort": [item.to_api() for item in sort] if sort is not None else None,
        "filters": [item.to_api() for item in filters] if filters is not None else None,
    }
    data = rest_request(
        session,
        "POST",
        "/api/v2/tenant/assets",
        json={key: value for key, value in payload.items() if value is not None},
    )
    return AssetPage.from_api(data if isinstance(data, (dict, list)) else {"data": data})


def list_client_assets(
    session: AuthSession,
    client_id: int | str,
    *,
    offset: int = 0,
    limit: ClientAssetPageLimit = ClientAssetPageLimit.TWENTY_FIVE,
    sort: list[ClientAssetSort] | None = None,
    filters: list[ClientAssetFilter] | None = None,
) -> AssetPage:
    """List assets for one client with documented pagination, sorting, and filters."""
    payload: JsonDict = {
        "pagination": {"offset": offset, "limit": int(limit)},
        "sort": [item.to_api() for item in sort] if sort is not None else None,
        "filters": [item.to_api() for item in filters] if filters is not None else None,
    }
    data = rest_request(
        session,
        "POST",
        f"/api/v2/clients/{client_id}/assets",
        json={key: value for key, value in payload.items() if value is not None},
    )
    return AssetPage.from_api(data if isinstance(data, (dict, list)) else {"data": data})


def list_report_assets(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
) -> list[Asset]:
    """List assets that are associated with one report."""
    data = rest_request(session, "GET", f"/api/v2/clients/{client_id}/reports/{report_id}/assets")
    return [Asset.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def get_asset(
    session: AuthSession,
    client_id: int | str,
    asset_id: int | str,
) -> Asset:
    """Get one asset for a client."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/asset/{asset_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac get asset response was not a JSON object.")
    return Asset.from_api(data)


def create_asset(
    session: AuthSession,
    client_id: int | str,
    asset: AssetInput,
) -> AssetCreateResult:
    """Create an asset for a client from a reusable AssetInput payload."""
    if asset.name is None:
        raise TypeError("create_asset requires asset.name.")
    data = rest_request(session, "PUT", f"/api/v1/client/{client_id}/asset/0", json=asset.to_api())
    return AssetCreateResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_asset(
    session: AuthSession,
    client_id: int | str,
    asset_id: int | str,
    asset: AssetInput,
) -> OperationResult:
    """Update an asset for a client from a reusable AssetInput payload."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/client/{client_id}/asset/{asset_id}",
        json=asset.to_api(),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_asset(
    session: AuthSession,
    client_id: int | str,
    asset_id: int | str,
) -> OperationResult:
    """Delete one asset from a client."""
    data = rest_request(session, "DELETE", f"/api/v1/client/{client_id}/asset/{asset_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def import_client_assets(
    session: AuthSession,
    client_id: int | str,
    source: AssetImportSource,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> OperationResult:
    """Import client assets from a supported parser source."""
    close_after = None
    if isinstance(file, (str, Path)):
        path = Path(file)
        close_after = path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "assets")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        data = rest_request(
            session,
            "POST",
            f"/api/v2/client/{client_id}/assets/import/{source.value}",
            files=files,
        )
    finally:
        if close_after is not None:
            close_after.close()
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_delete_client_assets(
    session: AuthSession,
    client_id: int | str,
    asset_ids: list[int | str],
) -> OperationResult:
    """Delete multiple client assets."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/client/{client_id}/bulk/assets/delete",
        json={"assetIds": asset_ids},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})
