# plextrac-api2

Unofficial Python API for PlexTrac. It provides a typed, function-oriented API for clients,
reports, findings, assets, assessments, content libraries, integrations, runbooks, users, tenant
administration, files, analytics, webhooks, and raw REST or GraphQL access when needed.

The public API is intentionally not one enormous object with hundreds of methods. It keeps PlexTrac
operations organized by product area, uses explicit function signatures, and models documented
request and response structures with dataclasses and enums where the API provides stable structure.

It is not affiliated with or endorsed by PlexTrac.

## Design Approach

The API is built by PlexTrac product area, not by a single catch-all client object:

- Functions live in `src/plextrac_api/functions/`.
- Structured request and response types live in `src/plextrac_api/types/`.
- Shared session helpers and errors are available from `plextrac_api`.
- Grouped API modules are available from `plextrac_api.functions`.

Each group owns a focused part of the PlexTrac workflow. Clients own client records and client-user
assignment. Reports own report records, report search/replace, imports, exports, and report-level
bulk actions. Findings own finding records, finding imports, evidence, status updates, and finding
bulk actions. Runbooks own runbook repositories, methodologies, tactics, techniques, procedures,
engagements, and engagement procedure data.

Some documented PlexTrac surface area is intentionally handled carefully:

- Duplicate endpoint versions are collapsed to the preferred documented version.
- Function names are normalized when the documented names are inconsistent or awkward.
- Raw REST and GraphQL helpers remain available for edge cases and unsupported payload fields.
- Webhooks are modeled as receiver-side helpers, not outbound API calls.
- Generated endpoint inventory and implementation methodology live in `AGENTS.md`.

## Installation

This project targets Python 3.11+.

From a local checkout:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

For development dependencies:

```bash
pip install -e ".[dev]"
```

From GitHub:

```bash
pip install "git+https://github.com/erikrubstein/plextrac-api2.git"
```

## Getting Started

Create an authenticated session:

```python
from plextrac_api import create_session

session = create_session(
    base_url="https://example.plextrac.com",
    username="you@example.com",
    password="your-password",
)
```

If you already have a PlexTrac bearer token:

```python
from plextrac_api import session_from_token

session = session_from_token(
    base_url="https://example.plextrac.com",
    token="jwt-token",
)
```

Call grouped API functions:

```python
from plextrac_api.functions import clients
from plextrac_api.types import ClientPageLimit, ClientPagination

page = clients.list_clients(
    session,
    pagination=ClientPagination(limit=ClientPageLimit.FIFTY, offset=0),
)

for client in page.clients:
    print(client.client_id, client.name)
```

Create related records through their product groups:

```python
from plextrac_api.functions import findings, reports
from plextrac_api.types import FindingInput, FindingSeverity, FindingStatus, ReportInput

report = reports.create_report(
    session,
    client_id="client-id",
    report=ReportInput(name="Example Report"),
)

finding = findings.create_finding(
    session,
    client_id="client-id",
    report_id=report.report_id,
    finding=FindingInput(
        title="Example Finding",
        severity=FindingSeverity.HIGH,
        status=FindingStatus.OPEN,
        description="Example description",
    ),
)
```

Save and load sessions for local scripts:

```python
from plextrac_api import load_session, refresh_session, save_session

save_session(session, "session.json")
session = load_session("session.json")
refresh_session(session, session_path="session.json")
```

## Function Overview

This is a curated overview of commonly used functions, not an exhaustive list of every implemented
wrapper. All authenticated API functions take `session` as their first argument.

### Auth

- `create_session`
- `session_from_token`
- `refresh_session`
- `save_session`
- `load_session`

### Clients

- `list_clients`
- `get_client`
- `create_client`
- `update_client`
- `delete_client`
- `list_client_users`
- `list_available_tenant_users`
- `assign_users_to_client`
- `remove_users_from_client`
- `add_client_logo`

### Reports

- `list_reports`
- `list_client_reports`
- `get_report`
- `create_report`
- `update_report`
- `delete_report`
- `bulk_delete_reports`
- `bulk_add_tags_to_reports`
- `bulk_assign_reviewers_to_reports`
- `bulk_update_report_statuses`
- `export_report_to_ptrac`
- `export_report_to_word`
- `export_report_to_pdf`
- `import_report_from_ptrac`

### Findings

- `list_report_findings`
- `get_finding`
- `create_finding`
- `update_finding`
- `delete_finding`
- `bulk_delete_findings`
- `bulk_upsert_finding_evidence`
- `get_scanner_output`
- `list_finding_status_updates`
- `create_finding_status_update`
- `request_presigned_upload_url`
- `import_preuploaded_findings`
- `list_import_statuses`

### Assets And Affected Assets

- `list_tenant_assets`
- `list_client_assets`
- `list_report_assets`
- `get_asset`
- `create_asset`
- `update_asset`
- `delete_asset`
- `import_client_assets`
- `bulk_delete_client_assets`
- `import_finding_affected_assets`
- `remove_affected_asset`
- `bulk_get_affected_asset_statuses`
- `list_affected_asset_status_updates`
- `create_affected_asset_status_update`
- `bulk_create_affected_asset_status_updates`

### Files

- `list_artifacts`
- `download_artifact`
- `upload_artifact`
- `delete_artifact`
- `get_upload_by_name`
- `upload_tenant_image`

### Users, Tenant, And Admin

- `get_authenticated_user`
- `list_tenant_users`
- `bulk_create_users`
- `update_user`
- `delete_user`
- `change_password`
- `list_user_notifications`
- `get_tenant`
- `update_tenant`
- `get_root_info`
- `list_authentication_providers`
- `list_security_roles`
- `create_security_role`
- `list_tenant_tags`
- `list_audit_log_entries`

### Assessments

- `list_questions`
- `get_question`
- `create_question`
- `update_question`
- `update_question_order`
- `delete_question`
- `list_answer_types`
- `get_answer_type`
- `create_answer_type`
- `update_answer_type`
- `delete_answer_type`
- `list_questionnaires`
- `get_questionnaire`
- `create_questionnaire`
- `update_questionnaire`
- `delete_questionnaire`
- `export_questionnaire`
- `import_questionnaire`
- `list_tenant_assessments`
- `list_client_assessments`
- `get_client_assessment_details`
- `get_client_assessment`
- `get_assessment_by_cuid`
- `list_assessment_questions`
- `list_assessment_answers`
- `update_assessment_answers`
- `list_assessment_reviewers`
- `create_client_assessment`
- `update_client_assessment`
- `delete_client_assessment`
- `create_report_from_assessment_questionnaire`
- `copy_assessment_questionnaire`

### Content Library And Templates

- `list_narrative_repositories`
- `create_narrative_repository`
- `list_narrative_repository_sections`
- `create_narrative_repository_section`
- `list_writeups`
- `create_writeup`
- `bulk_add_writeups_to_report`
- `list_writeup_repositories`
- `list_report_templates`
- `list_finding_templates`
- `list_export_templates`
- `import_export_template`

Writeup list endpoints return `WriteupSummary` records for the fields PlexTrac includes in list
payloads. Single-writeup create/get/update calls return full `Writeup` records.

### Integrations

- `get_integration`
- `upsert_integration`
- `delete_integration`
- `list_tenable_io_tags`
- `sync_tenable_io_tags`
- `list_jira_projects`
- `create_jira_connection`
- `update_jira_connection`
- `delete_jira_connection`
- `set_jira_projects`
- `get_jira_projects`
- `list_jira_issue_mappings`
- `reset_jira_issue_mappings`
- `bulk_update_jira_issue_type_mappings`
- `create_jira_tickets_from_findings`
- `unlink_jira_ticket_from_findings`
- `list_configurations`
- `create_configuration`
- `get_configuration`
- `update_configuration`
- `delete_configuration`

### Analytics

Analytics filters use semantic Python field names such as `client_ids`, `report_ids`, and
`asset_ids`, while response rows are exposed through `AnalyticsResult.records`. Endpoint-specific
records such as `AnalyticsFindingRecord`, `AnalyticsAssetRecord`, `AnalyticsReportRecord`, and
`AnalyticsClientRecord`, plus trend rows as `AnalyticsTrendRecord`, avoid unrelated nullable fields;
the original PlexTrac response remains available on each record's `raw` field and on
`AnalyticsResult.data` / `AnalyticsResult.raw`.

- `retrieve_analytics`
- `retrieve_analytics_findings`
- `retrieve_analytics_findings_aging`
- `get_finding_analytics_bootstrap`
- `retrieve_analytics_assets`
- `retrieve_analytics_assets_with_filter`
- `retrieve_analytics_trends_opened_closed`
- `retrieve_analytics_trends_from_creation_to_close`
- `retrieve_analytics_trends_slas`
- `retrieve_analytics_trends_sla_findings`

### Runbooks

- `list_runbook_repositories`
- `create_runbook_repository`
- `list_runbook_methodologies`
- `create_runbook_methodology`
- `list_runbook_tactics`
- `list_runbook_techniques`
- `list_runbook_procedures`
- `list_runbook_engagements`
- `create_runbook_engagement`
- `list_runbook_engagement_procedures`
- `upload_runbook_engagement_procedure_attachment`
- `export_runbook`
- `import_runbook`

### Scheduling, Mailer, Parser Actions, And Substatus

- `search_engagement_schedule_events`
- `create_engagement_schedule_event`
- `approve_engagement_schedule_event`
- `list_mailer_templates`
- `get_email_template`
- `upsert_email_template`
- `get_tenant_parsers`
- `list_tenant_parser_actions`
- `get_tenant_parser_action`
- `create_tenant_parser_action`
- `update_parser_action`
- `bulk_update_tenant_parser_actions`
- `set_parser_plugin_actions_enabled`
- `import_parser_plugins`
- `list_substatuses`
- `create_substatus`

### Raw Helpers

- `rest_request`
- `execute_graphql`
- `graphql_request`

Use `rest_request` when PlexTrac supports a workflow that has not been modeled yet:

```python
from plextrac_api import rest_request

data = rest_request(session, "GET", "/api/v1/")
```

Use `execute_graphql` when you need direct GraphQL access:

```python
from plextrac_api import execute_graphql

data = execute_graphql(
    session,
    "query Example($tenantId: String!) { tenant(id: $tenantId) { id } }",
    variables={"tenantId": "tenant-cuid"},
)
```

### Webhooks

- `verify_signature`
- `signature_from_headers`
- `parse_webhook_event`
- `parse_verified_webhook_event`

Webhook helpers are framework-neutral:

```python
from plextrac_api.functions.webhooks import parse_verified_webhook_event, signature_from_headers

signature = signature_from_headers(request.headers)
if signature is None:
    raise ValueError("Missing PlexTrac webhook signature.")

event = parse_verified_webhook_event(
    payload=request.body,
    signature=signature,
    secret="configured-webhook-secret",
)
```

## Development

Run tests and linting:

```bash
python -m pytest tests/unit
python -m ruff check .
```

Regenerate endpoint metadata and the endpoint inventory in `AGENTS.md`:

```bash
python scripts/generate_endpoints.py
```

## Safety Notes

This is an unofficial API for PlexTrac. PlexTrac may change endpoints, fields, authentication
behavior, webhook payloads, or validation rules without notice.

## License

MIT
