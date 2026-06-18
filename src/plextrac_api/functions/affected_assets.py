from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.assets import (
    AffectedAssetImportSource,
    AffectedAssetStatusMap,
    AffectedAssetStatusUpdate,
)
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.findings import FindingInput


def import_finding_affected_assets(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    source: AffectedAssetImportSource,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> OperationResult:
    """Import affected assets for one finding from a CSV or XML file."""
    close_after = None
    if isinstance(file, (str, Path)):
        path = Path(file)
        close_after = path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "affected-assets")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        data = rest_request(
            session,
            "POST",
            f"/api/v2/clients/{client_id}/reports/{report_id}/flaws/{finding_id}/affected-assets/import/{source.value}",
            files=files,
        )
    finally:
        if close_after is not None:
            close_after.close()
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def remove_affected_asset(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    asset_id: int | str,
) -> OperationResult:
    """Remove one affected asset from a finding."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}/asset/{asset_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_get_affected_asset_statuses(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    asset_ids: list[int | str],
) -> AffectedAssetStatusMap:
    """Get the latest status tracker update for multiple affected assets."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/client/{client_id}/report/{report_id}/flaw/{finding_id}/assets/status",
        json={"assetIds": asset_ids},
    )
    return AffectedAssetStatusMap.from_api(data)


def list_affected_asset_status_updates(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    asset_id: int | str,
) -> list[AffectedAssetStatusUpdate]:
    """List status tracker updates for one affected asset."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}/asset/{asset_id}/status",
    )
    return (
        [AffectedAssetStatusUpdate.from_api(item) for item in data if isinstance(item, dict)]
        if isinstance(data, list)
        else []
    )


def create_affected_asset_status_update(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    asset_id: int | str,
    finding: FindingInput,
) -> OperationResult:
    """Add an affected-asset status update using PlexTrac's finding payload endpoint."""
    data = rest_request(
        session,
        "POST",
        f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}/asset/{asset_id}/status/update",
        json=finding.to_api(),
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_create_affected_asset_status_updates(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    updates: list[AffectedAssetStatusUpdate],
) -> OperationResult:
    """Create affected-asset status tracker updates in bulk."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/client/{client_id}/report/{report_id}/finding/{finding_id}/asset/status",
        json=[update.to_api(include_asset_id=True) for update in updates],
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})
