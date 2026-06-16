"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def search_replace_in_report_occurrences(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/search-replace/occurrences\n\nPlexTrac endpoint: Search & Replace in Report (Occurrences)"""
    return endpoint_request(session, "reports", "search_replace_in_report_occurrences", **kwargs)


def search_replace_in_report_replace(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/search-replace\n\nPlexTrac endpoint: Search & Replace in Report (Replace)"""
    return endpoint_request(session, "reports", "search_replace_in_report_replace", **kwargs)


def list_client_reports(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/reports\n\nPlexTrac endpoint: List Client Reports"""
    return endpoint_request(session, "reports", "list_client_reports", **kwargs)


def get_report_list(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/reports\n\nPlexTrac endpoint: Get Report List"""
    return endpoint_request(session, "reports", "get_report_list", **kwargs)


def get_report(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}\n\nPlexTrac endpoint: Get Report"""
    return endpoint_request(session, "reports", "get_report", **kwargs)


def get(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `get_report`."""
    return get_report(session, **kwargs)


def create_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/create\n\nPlexTrac endpoint: Create Report"""
    return endpoint_request(session, "reports", "create_report", **kwargs)


def create(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `create_report`."""
    return create_report(session, **kwargs)


def update_report(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/client/{clientId}/report/{reportId}\n\nPlexTrac endpoint: Update Report"""
    return endpoint_request(session, "reports", "update_report", **kwargs)


def update(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `update_report`."""
    return update_report(session, **kwargs)


def delete_report(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/client/{clientId}/report/{reportId}\n\nPlexTrac endpoint: Delete Report"""
    return endpoint_request(session, "reports", "delete_report", **kwargs)


def delete(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `delete_report`."""
    return delete_report(session, **kwargs)


def bulk_delete_reports(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/reports/bulk/delete\n\nPlexTrac endpoint: Bulk Delete Reports"""
    return endpoint_request(session, "reports", "bulk_delete_reports", **kwargs)


def get_exhibit(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/{exhibitId}\n\nPlexTrac endpoint: Get Exhibit"""
    return endpoint_request(session, "reports", "get_exhibit", **kwargs)


def bulk_add_tags_to_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/reports/bulk/tags\n\nPlexTrac endpoint: Bulk Add Tags to Report"""
    return endpoint_request(session, "reports", "bulk_add_tags_to_report", **kwargs)


def bulk_assign_reviewers_to_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/reports/bulk/reviewers\n\nPlexTrac endpoint: Bulk Assign Reviewers to Report"""
    return endpoint_request(session, "reports", "bulk_assign_reviewers_to_report", **kwargs)


def bulk_adjust_status_of_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/reports/bulk/status\n\nPlexTrac endpoint: Bulk Adjust Status of Report"""
    return endpoint_request(session, "reports", "bulk_adjust_status_of_report", **kwargs)


def export_report_to_ptrac(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/export/ptrac\n\nPlexTrac endpoint: Export Report to Ptrac"""
    return endpoint_request(session, "reports", "export_report_to_ptrac", **kwargs)


def export_report_to_word(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/export/doc\n\nPlexTrac endpoint: Export Report to Word"""
    return endpoint_request(session, "reports", "export_report_to_word", **kwargs)


def export_report_to_pdf(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/client/{clientId}/report/{reportId}/export/pdf\n\nPlexTrac endpoint: Export Report to PDF"""
    return endpoint_request(session, "reports", "export_report_to_pdf", **kwargs)


def import_ptrac_report(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/import\n\nPlexTrac endpoint: Import Ptrac Report"""
    return endpoint_request(session, "reports", "import_ptrac_report", **kwargs)

