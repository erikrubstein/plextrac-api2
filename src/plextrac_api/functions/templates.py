"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def list_report_templates(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/report-templates\n\nPlexTrac endpoint: List Report Templates"""
    return endpoint_request(session, "templates", "list_report_templates", **kwargs)


def get_report_template(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/report-template/{reportTemplateId}\n\nPlexTrac endpoint: Get Report Template"""
    return endpoint_request(session, "templates", "get_report_template", **kwargs)


def create_report_template(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/report-template\n\nPlexTrac endpoint: Create Report Template"""
    return endpoint_request(session, "templates", "create_report_template", **kwargs)


def update_report_template(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/report-template/{reportTemplateId}\n\nPlexTrac endpoint: Update Report Template"""
    return endpoint_request(session, "templates", "update_report_template", **kwargs)


def delete_report_template(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/report-template/{reportTemplateId}\n\nPlexTrac endpoint: Delete Report Template"""
    return endpoint_request(session, "templates", "delete_report_template", **kwargs)


def list_findings_templates(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/field-templates\n\nPlexTrac endpoint: List Findings Templates"""
    return endpoint_request(session, "templates", "list_findings_templates", **kwargs)


def get_findings_template(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/field-template/{findingTemplateId}\n\nPlexTrac endpoint: Get Findings Template"""
    return endpoint_request(session, "templates", "get_findings_template", **kwargs)


def create_finding_template(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/field-template\n\nPlexTrac endpoint: Create Finding Template"""
    return endpoint_request(session, "templates", "create_finding_template", **kwargs)


def update_finding_template(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v1/tenant/{tenantId}/field-template/{findingTemplateId}\n\nPlexTrac endpoint: Update Finding Template"""
    return endpoint_request(session, "templates", "update_finding_template", **kwargs)


def delete_finding_template(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/field-template/{findingTemplateId}\n\nPlexTrac endpoint: Delete Finding Template"""
    return endpoint_request(session, "templates", "delete_finding_template", **kwargs)


def list_export_templates(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenant/{tenantId}/export-templates\n\nPlexTrac endpoint: List Export Templates"""
    return endpoint_request(session, "templates", "list_export_templates", **kwargs)


def get_export_template(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/tenant/{tenantId}/export-template/{exportTemplateId}\n\nPlexTrac endpoint: Get Export Template"""
    return endpoint_request(session, "templates", "get_export_template", **kwargs)


def import_export_template(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/tenant/{tenantId}/template/import\n\nPlexTrac endpoint: Import Export Template"""
    return endpoint_request(session, "templates", "import_export_template", **kwargs)


def delete_export_template(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/tenant/{tenantId}/template/{exportTemplateId}\n\nPlexTrac endpoint: Delete Export Template"""
    return endpoint_request(session, "templates", "delete_export_template", **kwargs)

