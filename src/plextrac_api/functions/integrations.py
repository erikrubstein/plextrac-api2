from __future__ import annotations

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import JsonDict, OperationResult
from plextrac_api.types.integrations import (
    IntegrationConfiguration,
    IntegrationConfigurationInput,
    IntegrationSettings,
    JiraConnection,
    JiraConnectionInput,
    JiraIssueMapping,
    JiraIssueMappingInput,
    JiraIssueTypeMappingInput,
    JiraProject,
    JiraProjectMappingType,
    JiraTicketCreateResult,
    TenableTag,
)


def get_integration(
    session: AuthSession,
    tenant_id: int | str,
    product: str,
) -> IntegrationSettings:
    """Get one tenant integration configuration."""
    data = rest_request(session, "GET", f"/api/v2/tenant/{tenant_id}/integrations/{product}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac integration response was not a JSON object.")
    return IntegrationSettings.from_api(product, data)


def upsert_integration(
    session: AuthSession,
    tenant_id: int | str,
    product: str,
    settings: JsonDict,
) -> IntegrationSettings:
    """Create or update one tenant integration configuration."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/tenant/{tenant_id}/integrations/{product}",
        json=dict(settings),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac integration response was not a JSON object.")
    return IntegrationSettings.from_api(product, data)


def delete_integration(
    session: AuthSession,
    tenant_id: int | str,
    product: str,
) -> OperationResult:
    """Delete one tenant integration configuration."""
    data = rest_request(session, "DELETE", f"/api/v2/tenant/{tenant_id}/integrations/{product}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_tenable_io_tags(
    session: AuthSession,
) -> list[TenableTag]:
    """List Tenable.io tags."""
    data = rest_request(session, "GET", "/api/v2/integrations/tenable-io/tags")
    return [TenableTag.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def sync_tenable_io_tags(
    session: AuthSession,
) -> OperationResult:
    """Trigger a Tenable.io tag sync."""
    data = rest_request(session, "GET", "/api/v2/integrations/tenable-io/tags/sync")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_jira_projects(
    session: AuthSession,
) -> list[JiraProject]:
    """List Jira projects available to the legacy Jira integration."""
    data = rest_request(session, "GET", "/api/v1/jira/projects")
    return [JiraProject.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def create_jira_connection(
    session: AuthSession,
    connection: JiraConnectionInput,
) -> JiraConnection:
    """Create a Jira connection."""
    data = rest_request(session, "POST", "/api/v2/jira/connect", json=connection.to_api())
    if not isinstance(data, dict):
        raise ValueError("PlexTrac Jira connection response was not a JSON object.")
    return JiraConnection.from_api(data)


def update_jira_connection(
    session: AuthSession,
    integration_id: int | str,
    connection: JiraConnectionInput,
) -> JiraConnection:
    """Update a Jira connection."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/jira/connect/{integration_id}",
        json=connection.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac Jira connection response was not a JSON object.")
    return JiraConnection.from_api(data)


def delete_jira_connection(
    session: AuthSession,
    integration_id: int | str,
) -> OperationResult:
    """Delete a Jira connection."""
    data = rest_request(session, "DELETE", f"/api/v2/jira/connect/{integration_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def set_jira_projects(
    session: AuthSession,
    integration_id: int | str,
    *,
    mapping_type: JiraProjectMappingType,
    projects: list[JiraProject],
) -> OperationResult:
    """Set Jira projects available to a Jira connection."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/jira/projects/{integration_id}",
        json={"mappingType": mapping_type.value, "projects": [project.to_api() for project in projects]},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_jira_projects(
    session: AuthSession,
    integration_id: int | str,
) -> list[JiraProject]:
    """List Jira projects for a Jira connection."""
    data = rest_request(session, "GET", f"/api/v2/jira/integration/projects/{integration_id}")
    return [JiraProject.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def list_jira_issue_mappings(
    session: AuthSession,
    integration_id: int | str,
    jira_project_id: int | str,
    jira_issue_type_id: int | str,
) -> list[JiraIssueMapping]:
    """List Jira issue mapping fields for a project issue type."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/jira/integration/{integration_id}/projects/{jira_project_id}/issues/{jira_issue_type_id}/mappings",
    )
    return [JiraIssueMapping.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def reset_jira_issue_mappings(
    session: AuthSession,
    integration_id: int | str,
    jira_project_id: int | str,
    jira_issue_type_id: int | str,
) -> OperationResult:
    """Reset Jira issue mapping fields for a project issue type."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/jira/integration/{integration_id}/projects/{jira_project_id}/issues/{jira_issue_type_id}/mappings/reset",
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def bulk_update_jira_issue_type_mappings(
    session: AuthSession,
    integration_id: int | str,
    mappings: list[JiraIssueTypeMappingInput],
) -> OperationResult:
    """Bulk update Jira issue type mappings."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/jira/integration/{integration_id}/issues/bulk/mappings",
        json=[mapping.to_api() for mapping in mappings],
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def create_jira_tickets_from_findings(
    session: AuthSession,
    integration_id: int | str,
    finding_ids: list[int | str],
    *,
    client_id: int | str | None = None,
    report_id: int | str | None = None,
    project_id: int | str | None = None,
    issue_type_id: int | str | None = None,
    mappings: list[JiraIssueMappingInput] | None = None,
) -> JiraTicketCreateResult:
    """Create Jira tickets from PlexTrac findings."""
    payload = {
        "findingIds": finding_ids,
        "clientId": client_id,
        "reportId": report_id,
        "projectId": project_id,
        "issueTypeId": issue_type_id,
        "mappings": [mapping.to_api() for mapping in mappings] if mappings is not None else None,
    }
    data = rest_request(
        session,
        "POST",
        f"/api/v2/jira/integration/{integration_id}/issues/create",
        json={key: value for key, value in payload.items() if value is not None},
    )
    return JiraTicketCreateResult.from_api(data if isinstance(data, dict) else {"data": data})


def unlink_jira_ticket_from_findings(
    session: AuthSession,
    integration_id: int | str,
    client_id: int | str,
    report_id: int | str,
    finding_id: int | str,
) -> OperationResult:
    """Unlink a Jira ticket from a finding."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/jira/integration/unlink/client/{client_id}/report/{report_id}/finding/{finding_id}",
        params={"integrationId": integration_id},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_configurations(
    session: AuthSession,
) -> list[IntegrationConfiguration]:
    """List integration configurations."""
    data = rest_request(session, "GET", "/api/v2/integrations/configurations")
    return [IntegrationConfiguration.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def create_configuration(
    session: AuthSession,
    configuration: IntegrationConfigurationInput,
) -> IntegrationConfiguration:
    """Create an integration configuration."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/integrations/configurations",
        json=configuration.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac integration configuration response was not a JSON object.")
    return IntegrationConfiguration.from_api(data)


def get_configuration(
    session: AuthSession,
    configuration_id: int | str,
) -> IntegrationConfiguration:
    """Get one integration configuration."""
    data = rest_request(session, "GET", f"/api/v2/integrations/configurations/{configuration_id}")
    if not isinstance(data, dict):
        raise ValueError("PlexTrac integration configuration response was not a JSON object.")
    return IntegrationConfiguration.from_api(data)


def update_configuration(
    session: AuthSession,
    configuration_id: int | str,
    configuration: IntegrationConfigurationInput,
) -> IntegrationConfiguration:
    """Update an integration configuration."""
    data = rest_request(
        session,
        "PUT",
        f"/api/v2/integrations/configurations/{configuration_id}",
        json=configuration.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac integration configuration response was not a JSON object.")
    return IntegrationConfiguration.from_api(data)


def delete_configuration(
    session: AuthSession,
    configuration_id: int | str,
) -> OperationResult:
    """Delete an integration configuration."""
    data = rest_request(session, "DELETE", f"/api/v2/integrations/configurations/{configuration_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})
