from __future__ import annotations

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict, OperationResult, clean
from plextrac_api.types.findings import (
    Finding,
    FindingEvidenceUpdate,
    FindingFilter,
    FindingImportSource,
    FindingImportStatus,
    FindingImportUpload,
    FindingInput,
    FindingPage,
    FindingPagination,
    FindingSort,
    FindingStatus,
    FindingStatusUpdate,
    FindingVisibility,
    PresignedUpload,
)


def request_presigned_upload_url(
    session: AuthSession,
    upload: FindingImportUpload,
) -> PresignedUpload:
    """Request a pre-signed upload URL for a finding import file."""
    if upload.filename is None:
        raise TypeError("request_presigned_upload_url requires upload.filename.")
    data = rest_request(session, "POST", "/api/v2/presigned-url", json=upload.to_presigned_api())
    if not isinstance(data, dict):
        raise ValueError("PlexTrac presigned upload response was not a JSON object.")
    return PresignedUpload.from_api(data)


def import_preuploaded_findings(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    source: FindingImportSource,
    upload: FindingImportUpload,
) -> OperationResult:
    """Import findings from a file that was already uploaded with a pre-signed URL."""
    data = rest_request(session, "POST", f"/api/v2/client/{client_id}/report/{report_id}/preuploaded-import/{source.value}", json=upload.to_preuploaded_import_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_import_statuses(
    session: AuthSession,
) -> list[FindingImportStatus]:
    """List recent finding import status events."""
    data = rest_request(session, "GET", "/api/v2/my-imports")
    return [FindingImportStatus.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def get_scanner_output(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    asset_id: int | str,
) -> bytes:
    """Get scanner output for one affected asset on a finding."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}/asset/{asset_id}/scanoutput")
    if isinstance(data, bytes):
        return data
    if isinstance(data, str):
        return data.encode()
    raise ValueError("PlexTrac scanner output response was not bytes or text.")


def update_finding_evidence(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    asset_id: int | str,
    evidence_id: int | str,
    evidence: FindingEvidenceUpdate,
) -> OperationResult:
    """Update one evidence item for an affected asset on a finding."""
    data = rest_request(session, "PUT", f"/api/v2/client/{client_id}/report/{report_id}/finding/{finding_id}/asset/{asset_id}/evidence/{evidence_id}", json=evidence.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_upsert_finding_evidence(
    session: AuthSession,
    tenant_id: int | str,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    evidence: list[FindingEvidenceUpdate],
) -> OperationResult:
    """Create or update evidence items for affected assets on a finding."""
    data = rest_request(session, "PUT", f"/api/v2/tenant/{tenant_id}/client/{client_id}/report/{report_id}/finding/{finding_id}/asset/evidence", json=[item.to_api() for item in evidence])
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_report_findings(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    *,
    pagination: FindingPagination | None = None,
    sort: list[FindingSort] | None = None,
    filters: list[FindingFilter] | None = None,
) -> FindingPage:
    """List report findings with pagination, sorting, and filters."""
    payload: JsonDict = {
        "pagination": (pagination or FindingPagination()).to_api(),
        "sort": [item.to_api() for item in sort] if sort is not None else None,
        "filters": [item.to_api() for item in filters] if filters is not None else None,
    }
    data = rest_request(session, "POST", f"/api/v2/clients/{client_id}/reports/{report_id}/findings", json={key: value for key, value in payload.items() if value is not None})
    return FindingPage.from_api(data if isinstance(data, (dict, list)) else {"data": data})


def get_finding(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
) -> Finding:
    """Get one finding from a report."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac get finding response was not a JSON object.")
    return Finding.from_api(data)


def create_finding(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding: FindingInput,
) -> OperationResult:
    """Create a finding for a report from a reusable FindingInput payload."""
    missing = [
        name
        for name, value in {
            "title": finding.title,
            "severity": finding.severity,
            "status": finding.status,
            "description": finding.description,
        }.items()
        if value is None
    ]
    if missing:
        raise TypeError(f"create_finding missing required fields: {', '.join(missing)}.")
    data = rest_request(session, "POST", f"/api/v1/client/{client_id}/report/{report_id}/flaw/create", json=finding.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_finding(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    finding: FindingInput,
) -> OperationResult:
    """Update a finding for a report from a reusable FindingInput payload."""
    data = rest_request(session, "PUT", f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}", json=finding.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_update_findings_metadata(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_ids: list[int | str],
    *,
    tags: list[str] | None = None,
    created_at: int | None = None,
    visibility: FindingVisibility | None = None,
) -> OperationResult:
    """Apply bulk metadata changes such as tags, creation date, or visibility."""
    payload = clean({"findingIds": finding_ids, "tags": tags, "createdAt": created_at, "visibility": visibility.value if visibility is not None else None})
    data = rest_request(session, "PUT", f"/api/v2/clients/{client_id}/reports/{report_id}/findings", json=payload)
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_update_finding_statuses(
    session: AuthSession,
    client_id: int | str,
    finding_ids: list[int | str],
    *,
    status: FindingStatus | None = None,
    substatus: str | None = None,
    substatus_cuid: str | None = None,
    assigned_to: str | None = None,
    comments: str | None = None,
) -> OperationResult:
    """Bulk update finding status, substatus, and assignment."""
    payload = clean(
        {
            "findingIds": finding_ids,
            "status": status.value if status is not None else None,
            "subStatus": substatus,
            "substatusCuid": substatus_cuid,
            "assignedTo": assigned_to,
            "comments": comments,
        }
    )
    data = rest_request(session, "PUT", f"/api/v2/client/{client_id}/findings", json=payload)
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_finding(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
) -> OperationResult:
    """Delete one finding from a report."""
    data = rest_request(session, "DELETE", f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_delete_findings(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_ids: list[int | str],
) -> OperationResult:
    """Delete multiple findings from a report."""
    data = rest_request(session, "POST", f"/api/v1/client/{client_id}/report/{report_id}/flaws/delete", json={"findingIds": finding_ids})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_finding_status_updates(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
) -> list[FindingStatusUpdate]:
    """List status tracker updates for a finding."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}/status")
    return [FindingStatusUpdate.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def create_finding_status_update(
    session: AuthSession,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
    update: FindingStatusUpdate,
) -> OperationResult:
    """Add a status tracker update to a finding."""
    data = rest_request(session, "POST", f"/api/v1/client/{client_id}/report/{report_id}/flaw/{finding_id}/status/update", json=update.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})
