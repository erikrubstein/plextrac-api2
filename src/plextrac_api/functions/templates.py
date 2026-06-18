from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.templates import (
    ExportTemplate,
    ExportTemplateType,
    FindingTemplate,
    FindingTemplateInput,
    ReportTemplate,
    ReportTemplateInput,
    TemplateOperationResult,
)


def list_report_templates(
    session: AuthSession,
    tenant_id: int | str,
) -> list[ReportTemplate]:
    """List report templates for a tenant."""
    data = rest_request(session, "GET", f"/api/v1/tenant/{tenant_id}/report-templates")
    return [ReportTemplate.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def get_report_template(
    session: AuthSession,
    tenant_id: int | str,
    report_template_id: int | str,
) -> ReportTemplate:
    """Get one report template."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/report-template/{report_template_id}",
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac report template response was not a JSON object.")
    return ReportTemplate.from_api(data)


def create_report_template(
    session: AuthSession,
    tenant_id: int | str,
    template: ReportTemplateInput,
) -> TemplateOperationResult:
    """Create a report template."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/report-template",
        json=template.to_api(),
    )
    return TemplateOperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_report_template(
    session: AuthSession,
    tenant_id: int | str,
    report_template_id: int | str,
    template: ReportTemplateInput,
) -> TemplateOperationResult:
    """Update a report template."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/report-template/{report_template_id}",
        json=template.to_api(),
    )
    return TemplateOperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_report_template(
    session: AuthSession,
    tenant_id: int | str,
    report_template_id: int | str,
) -> OperationResult:
    """Delete a report template."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v1/tenant/{tenant_id}/report-template/{report_template_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_finding_templates(
    session: AuthSession,
) -> list[FindingTemplate]:
    """List finding field templates."""
    data = rest_request(session, "GET", "/api/v1/field-templates")
    return [FindingTemplate.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def get_finding_template(
    session: AuthSession,
    finding_template_id: int | str,
) -> FindingTemplate:
    """Get one finding field template."""
    data = rest_request(session, "GET", f"/api/v1/field-template/{finding_template_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac finding template response was not a JSON object.")
    return FindingTemplate.from_api(data)


def create_finding_template(
    session: AuthSession,
    tenant_id: int | str,
    template: FindingTemplateInput,
) -> TemplateOperationResult:
    """Create a finding field template."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/field-template",
        json=template.to_api(),
    )
    return TemplateOperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def update_finding_template(
    session: AuthSession,
    tenant_id: int | str,
    finding_template_id: int | str,
    template: FindingTemplateInput,
) -> TemplateOperationResult:
    """Update a finding field template."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v1/tenant/{tenant_id}/field-template/{finding_template_id}",
        json=template.to_api(),
    )
    return TemplateOperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_finding_template(
    session: AuthSession,
    tenant_id: int | str,
    finding_template_id: int | str,
) -> OperationResult:
    """Delete a finding field template."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v1/tenant/{tenant_id}/field-template/{finding_template_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_export_templates(
    session: AuthSession,
    tenant_id: int | str,
) -> list[ExportTemplate]:
    """List export templates for a tenant."""
    data = rest_request(session, "GET", f"/api/v2/tenant/{tenant_id}/export-templates")
    if not isinstance(data, dict):
        return []
    return [
        ExportTemplate.from_api(template_id, item)
        for template_id, item in data.items()
        if isinstance(item, dict)
    ]


def download_export_template(
    session: AuthSession,
    tenant_id: int | str,
    export_template_id: int | str,
) -> bytes:
    """Download an export template file."""
    data = rest_request(
        session,
        "GET",
        f"/api/v1/tenant/{tenant_id}/export-template/{export_template_id}",
    )
    if isinstance(data, bytes):
        return data
    raise ValueError("PlexTrac export template download response was not bytes.")


def import_export_template(
    session: AuthSession,
    tenant_id: int | str,
    file: str | Path | BinaryIO,
    *,
    name: str,
    template_type: ExportTemplateType = ExportTemplateType.CUSTOM,
    filename: str | None = None,
    content_type: str | None = None,
) -> TemplateOperationResult:
    """Import a Word or Jinja export template file."""
    data = _upload_template(
        session,
        f"/api/v1/tenant/{tenant_id}/template/import",
        file,
        params={"name": name, "type": template_type.value},
        filename=filename,
        content_type=content_type,
    )
    return TemplateOperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_export_template(
    session: AuthSession,
    tenant_id: int | str,
    export_template_id: int | str,
) -> OperationResult:
    """Delete an export template."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v1/tenant/{tenant_id}/template/{export_template_id}",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def _upload_template(
    session: AuthSession,
    path: str,
    file: str | Path | BinaryIO,
    *,
    params: dict[str, str],
    filename: str | None,
    content_type: str | None,
) -> object:
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "export-template")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        return rest_request(session, "POST", path, params=params, files=files)
    finally:
        if close_after is not None:
            close_after.close()
