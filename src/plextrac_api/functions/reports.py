from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import (
    CustomField,
    JsonDict,
    OperationResult,
    Pagination,
)
from plextrac_api.types.reports import (
    Narrative,
    Report,
    ReportDraft,
    ReportExhibit,
    ReportFilter,
    ReportPage,
    ReportPatch,
    ReportReplaceResult,
    ReportSearchOccurrenceResult,
    ReportSort,
    ReportStatus,
    ReportSummary,
)


def count_report_search_occurrences(session: AuthSession, report_id: int | str, search: str) -> ReportSearchOccurrenceResult:
    """Count occurrences of a search value within a report."""
    data = rest_request(session, "POST", "/api/v1/search-replace/occurrences", json={"search": search, "report_id": report_id})
    if not isinstance(data, dict):
        raise ValueError("PlexTrac report search occurrence response was not a JSON object.")
    return ReportSearchOccurrenceResult.from_api(data)


def replace_report_text(session: AuthSession, report_id: int | str, search: str, replace: str) -> ReportReplaceResult:
    """Find and replace a text value within a report."""
    data = rest_request(session, "POST", "/api/v1/search-replace", json={"search": search, "replace": replace, "report_id": report_id})
    if not isinstance(data, dict):
        raise ValueError("PlexTrac report replace response was not a JSON object.")
    return ReportReplaceResult.from_api(data)


def list_client_reports(session: AuthSession, client_id: int | str) -> list[ReportSummary]:
    """List summarized reports for a specific client."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/reports")
    return [ReportSummary.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def list_reports(session: AuthSession, *, pagination: Pagination | None = None, sort: list[ReportSort] | None = None, filters: list[ReportFilter] | None = None) -> ReportPage:
    """List tenant reports with pagination, sorting, and filters."""
    payload: JsonDict = {
        "pagination": (pagination or Pagination()).to_api(),
        "sort": [item.to_api() for item in sort] if sort is not None else None,
        "filters": [item.to_api() for item in filters] if filters is not None else None,
    }
    data = rest_request(session, "POST", "/api/v2/reports", json={key: value for key, value in payload.items() if value is not None})
    return ReportPage.from_api(data if isinstance(data, (dict, list)) else {"data": data})


def get_report(session: AuthSession, client_id: int | str, report_id: int | str) -> Report:
    """Get one report for a client."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac get report response was not a JSON object.")
    return Report.from_api(data)


def create_report(session: AuthSession, client_id: int | str, report: ReportDraft | None = None, *, name: str | None = None, status: ReportStatus | None = None, include_evidence: bool | None = None, tags: list[str] | None = None, custom_fields: list[CustomField] | None = None, template: str | None = None, start_date: str | None = None, end_date: str | None = None, fields_template: str | None = None, is_track_changes: bool | None = None) -> OperationResult:
    """Create a report for a client from a ReportDraft or explicit keyword fields."""
    if report is None:
        if name is None:
            raise TypeError("create_report requires either report or name.")
        report = ReportDraft(
            name=name,
            status=status,
            include_evidence=include_evidence,
            tags=tags,
            custom_fields=custom_fields,
            template=template,
            start_date=start_date,
            end_date=end_date,
            fields_template=fields_template,
            is_track_changes=is_track_changes,
        )
    data = rest_request(session, "POST", f"/api/v1/client/{client_id}/report/create", json=report.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_report(session: AuthSession, client_id: int | str, report_id: int | str, report: ReportPatch | None = None, *, name: str | None = None, status: ReportStatus | None = None, include_evidence: bool | None = None, tags: list[str] | None = None, custom_fields: list[CustomField] | None = None, narratives: list[Narrative] | None = None, template: str | None = None, start_date: str | None = None, end_date: str | None = None, fields_template: str | None = None, is_track_changes: bool | None = None) -> OperationResult:
    """Update report metadata and narratives for a client report."""
    patch = report or ReportPatch(
        name=name,
        status=status,
        include_evidence=include_evidence,
        tags=tags,
        custom_fields=custom_fields,
        narratives=narratives,
        template=template,
        start_date=start_date,
        end_date=end_date,
        fields_template=fields_template,
        is_track_changes=is_track_changes,
    )
    data = rest_request(session, "PUT", f"/api/v1/client/{client_id}/report/{report_id}", json=patch.to_api())
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_report(session: AuthSession, client_id: int | str, report_id: int | str) -> OperationResult:
    """Delete one report for a client."""
    data = rest_request(session, "DELETE", f"/api/v1/client/{client_id}/report/{report_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_delete_reports(session: AuthSession, client_id: int | str, report_ids: list[int | str]) -> OperationResult:
    """Delete multiple reports for a client."""
    data = rest_request(session, "POST", "/api/v2/reports/bulk/delete", json={"clientId": client_id, "reportIDs": report_ids})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_report_exhibit(session: AuthSession, client_id: int | str, report_id: int | str, exhibit_id: int | str) -> ReportExhibit:
    """Get an exhibit filename/reference from a report."""
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/{exhibit_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac get report exhibit response was not a JSON object.")
    return ReportExhibit.from_api(data)


def bulk_add_tags_to_reports(session: AuthSession, client_id: int | str, report_ids: list[int | str], tags: list[str]) -> OperationResult:
    """Add tags to multiple reports for a client."""
    data = rest_request(session, "POST", "/api/v2/reports/bulk/tags", json={"clientId": client_id, "reportIDs": report_ids, "tags": tags})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_assign_reviewers_to_reports(session: AuthSession, client_id: int | str, report_ids: list[int | str], reviewers: list[str]) -> OperationResult:
    """Assign reviewers to multiple reports by email address."""
    data = rest_request(session, "POST", "/api/v2/reports/bulk/reviewers", json={"clientId": client_id, "reportIDs": report_ids, "reviewers": reviewers})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_update_report_statuses(session: AuthSession, client_id: int | str, report_ids: list[int | str], status: ReportStatus) -> OperationResult:
    """Set the same status on multiple reports."""
    data = rest_request(session, "POST", "/api/v2/reports/bulk/status", json={"clientId": client_id, "reportIDs": report_ids, "status": status.value})
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def export_report_to_ptrac(session: AuthSession, client_id: int | str, report_id: int | str) -> bytes:
    """Export a report in .ptrac format."""
    return _bytes_response(rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/export/ptrac"))


def export_report_to_word(session: AuthSession, client_id: int | str, report_id: int | str, *, include_evidence: bool = False, template_id: int | str | None = None) -> bytes:
    """Export a report as a Word document."""
    params: JsonDict = {"includeEvidence": include_evidence, "templateID": template_id}
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/export/doc", params={key: value for key, value in params.items() if value is not None})
    return _bytes_response(data)


def export_report_to_pdf(session: AuthSession, client_id: int | str, report_id: int | str, *, include_evidence: bool = False, template_id: int | str | None = None) -> bytes:
    """Export a report as a PDF."""
    params: JsonDict = {"includeEvidence": include_evidence, "templateID": template_id}
    data = rest_request(session, "GET", f"/api/v1/client/{client_id}/report/{report_id}/export/pdf", params={key: value for key, value in params.items() if value is not None})
    return _bytes_response(data)


def import_report_from_ptrac(session: AuthSession, client_id: int | str, file: str | Path | BinaryIO, *, filename: str | None = None, content_type: str | None = None) -> OperationResult:
    """Import a .ptrac file as a report for a client."""
    close_after = None
    if isinstance(file, (str, Path)):
        path = Path(file)
        close_after = path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "report.ptrac")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        data = rest_request(session, "POST", f"/api/v1/client/{client_id}/report/import", files=files)
    finally:
        if close_after is not None:
            close_after.close()
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def _bytes_response(data: object) -> bytes:
    if isinstance(data, bytes):
        return data
    raise ValueError("PlexTrac export response was not bytes.")
