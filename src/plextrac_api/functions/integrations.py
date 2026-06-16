"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def get_integration(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/tenant/{tenantId}/integrations/{product}\n\nPlexTrac endpoint: Get Integration"""
    return endpoint_request(session, "integrations", "get_integration", **kwargs)


def get(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `get_integration`."""
    return get_integration(session, **kwargs)


def save_integration(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/tenant/{tenantId}/integrations/{product}\n\nPlexTrac endpoint: Save Integration"""
    return endpoint_request(session, "integrations", "save_integration", **kwargs)


def delete_integration(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/tenant/{tenantId}/integrations/{product}\n\nPlexTrac endpoint: Delete Integration"""
    return endpoint_request(session, "integrations", "delete_integration", **kwargs)


def delete(session: AuthSession, **kwargs: Any) -> Any:
    """Alias for `delete_integration`."""
    return delete_integration(session, **kwargs)


def tenable_io_get_tags(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/integrations/tenable-io/tags\n\nPlexTrac endpoint: TenableIO Get Tags"""
    return endpoint_request(session, "integrations", "tenable_io_get_tags", **kwargs)


def tenable_io_sync_tags(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/integrations/tenable-io/tags/sync\n\nPlexTrac endpoint: TenableIO Sync Tags"""
    return endpoint_request(session, "integrations", "tenable_io_sync_tags", **kwargs)


def list_jira_projects(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/jira/projects\n\nPlexTrac endpoint: List Jira Projects"""
    return endpoint_request(session, "integrations", "list_jira_projects", **kwargs)


def create_and_link_jira_ticket_to_finding(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/createAndLinkJiraTicket\n\nPlexTrac endpoint: Create and Link Jira Ticket to Finding"""
    return endpoint_request(session, "integrations", "create_and_link_jira_ticket_to_finding", **kwargs)


def bulk_create_and_link_jira_tickets_to_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets\n\nPlexTrac endpoint: Bulk Create and Link Jira Tickets to Findings"""
    return endpoint_request(session, "integrations", "bulk_create_and_link_jira_tickets_to_findings", **kwargs)


def create_jira_connection(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/jira/connect\n\nPlexTrac endpoint: Create Jira Connection"""
    return endpoint_request(session, "integrations", "create_jira_connection", **kwargs)


def update_jira_connection(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/jira/connect/{integrationId}\n\nPlexTrac endpoint: Update Jira Connection"""
    return endpoint_request(session, "integrations", "update_jira_connection", **kwargs)


def delete_jira_connection(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/jira/connect/{integrationId}\n\nPlexTrac endpoint: Delete Jira Connection"""
    return endpoint_request(session, "integrations", "delete_jira_connection", **kwargs)


def set_jira_projects(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/jira/projects/{integrationId}\n\nPlexTrac endpoint: Set Jira Projects"""
    return endpoint_request(session, "integrations", "set_jira_projects", **kwargs)


def get_jira_projects(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/jira/integration/projects/{integrationId}\n\nPlexTrac endpoint: Get Jira Projects"""
    return endpoint_request(session, "integrations", "get_jira_projects", **kwargs)


def get_issue_mapping_types(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings\n\nPlexTrac endpoint: Get Issue Mapping Types"""
    return endpoint_request(session, "integrations", "get_issue_mapping_types", **kwargs)


def reset_issue_mapping_types(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings/reset\n\nPlexTrac endpoint: Reset Issue Mapping Types"""
    return endpoint_request(session, "integrations", "reset_issue_mapping_types", **kwargs)


def bulk_update_issue_type_mappings(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/jira/integration/{integrationId}/issues/bulk/mappings\n\nPlexTrac endpoint: Bulk Update Issue Type Mappings"""
    return endpoint_request(session, "integrations", "bulk_update_issue_type_mappings", **kwargs)


def create_jira_ticket_from_findings(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/jira/integration/{integrationId}/issues/create\n\nPlexTrac endpoint: Create Jira Ticket From Findings"""
    return endpoint_request(session, "integrations", "create_jira_ticket_from_findings", **kwargs)


def unlink_jira_ticket_from_findings(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/jira/integration/unlink/client/{clientId}/report/{reportId}/finding/{findingId}\n\nPlexTrac endpoint: Unlink Jira Ticket From Findings"""
    return endpoint_request(session, "integrations", "unlink_jira_ticket_from_findings", **kwargs)


def get_configurations(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/integrations/configurations\n\nPlexTrac endpoint: Get Configurations"""
    return endpoint_request(session, "integrations", "get_configurations", **kwargs)


def create_configurations(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/integrations/configurations\n\nPlexTrac endpoint: Create Configurations"""
    return endpoint_request(session, "integrations", "create_configurations", **kwargs)


def get_configuration(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/integrations/configurations/{configId}\n\nPlexTrac endpoint: Get Configuration"""
    return endpoint_request(session, "integrations", "get_configuration", **kwargs)


def update_configuration(session: AuthSession, **kwargs: Any) -> Any:
    """PUT /api/v2/integrations/configurations/{configId}\n\nPlexTrac endpoint: Update Configuration"""
    return endpoint_request(session, "integrations", "update_configuration", **kwargs)


def delete_configuration(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/integrations/configurations/{configId}\n\nPlexTrac endpoint: Delete Configuration"""
    return endpoint_request(session, "integrations", "delete_configuration", **kwargs)

