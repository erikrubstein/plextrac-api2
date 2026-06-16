"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def add_findings_from_file_imports(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/client/{clientId}/report/{reportId}/importAsync/{source}\n\nPlexTrac endpoint: Add Findings from File Imports V2"""
    return endpoint_request(session, "findings", "add_findings_from_file_imports", **kwargs)


def request_presigned_url(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/presigned-url \n\nPlexTrac endpoint: Request Presigned URL"""
    return endpoint_request(session, "findings", "request_presigned_url", **kwargs)


def add_findings_async_from_preuploaded_file_imports(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}\n\nPlexTrac endpoint: Add Findings Async from Preuploaded File Imports"""
    return endpoint_request(session, "findings", "add_findings_async_from_preuploaded_file_imports", **kwargs)


def get_import_status(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/my-imports\n\nPlexTrac endpoint: Get Import Status"""
    return endpoint_request(session, "findings", "get_import_status", **kwargs)


def get_scanner_output(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput\n\nPlexTrac endpoint: Get Scanner Output"""
    return endpoint_request(session, "findings", "get_scanner_output", **kwargs)


def bulk_get_evidence(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence\n\nPlexTrac endpoint: Bulk Get Evidence"""
    return endpoint_request(session, "findings", "bulk_get_evidence", **kwargs)


def update_evidence(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}\n\nPlexTrac endpoint: Update Evidence"""
    return endpoint_request(session, "findings", "update_evidence", **kwargs)


def bulk_upsert_evidence(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence\n\nPlexTrac endpoint: Bulk Upsert Evidence"""
    return endpoint_request(session, "findings", "bulk_upsert_evidence", **kwargs)


def list_report_findings(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/flaws\n\nPlexTrac endpoint: List Report Findings"""
    return endpoint_request(session, "findings", "list_report_findings", **kwargs)


def get_findings_by_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/clients/{clientId}/reports/{reportId}/findings\n\nPlexTrac endpoint: Get Findings by Report"""
    return endpoint_request(session, "findings", "get_findings_by_report", **kwargs)


def get_finding(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}\n\nPlexTrac endpoint: Get Finding"""
    return endpoint_request(session, "findings", "get_finding", **kwargs)


def get(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `get_finding`."""
    return get_finding(session, **kwargs)


def create_finding(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/{reportId}/flaw/create\n\nPlexTrac endpoint: Create Finding"""
    return endpoint_request(session, "findings", "create_finding", **kwargs)


def create(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `create_finding`."""
    return create_finding(session, **kwargs)


def update_finding(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}\n\nPlexTrac endpoint: Update Finding"""
    return endpoint_request(session, "findings", "update_finding", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_finding`."""
    return update_finding(session, **kwargs)


def bulk_update_findings(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/clients/{clientId}/reports/{reportId}/findings\n\nPlexTrac endpoint: Bulk Update Findings"""
    return endpoint_request(session, "findings", "bulk_update_findings", **kwargs)


def bulk_update_findings_assign_update_status(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/client/{clientId}/findings\n\nPlexTrac endpoint: Bulk Update Findings - Assign / Update Status"""
    return endpoint_request(session, "findings", "bulk_update_findings_assign_update_status", **kwargs)


def delete_finding(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}\n\nPlexTrac endpoint: Delete Finding"""
    return endpoint_request(session, "findings", "delete_finding", **kwargs)


def delete(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `delete_finding`."""
    return delete_finding(session, **kwargs)


def bulk_delete_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/{reportId}/flaws/delete\n\nPlexTrac endpoint: Bulk Delete Findings"""
    return endpoint_request(session, "findings", "bulk_delete_findings", **kwargs)


def get_finding_status_list(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status\n\nPlexTrac endpoint: Get Finding Status List"""
    return endpoint_request(session, "findings", "get_finding_status_list", **kwargs)


def create_status_update(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status/update\n\nPlexTrac endpoint: Create Status Update"""
    return endpoint_request(session, "findings", "create_status_update", **kwargs)

