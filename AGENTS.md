# AGENTS.md

This file is for coding agents and contributors working inside this repository.

## Purpose Of This File

Use this file to understand how to modify the SDK without drifting from the design decisions already
made in this codebase.

- It records repository context, implementation rules, endpoint inventory, and SDK methodology for
  future development work.
- Generated endpoint coverage is kept here so agents can compare the documented PlexTrac surface
  against the polished public Python modules.

## Repository Context

This package is an unofficial Python API for PlexTrac. The public SDK surface is intentionally made
of grouped function modules plus explicit dataclasses and enums. It should not become a single giant
client object.

Important package areas:

- `src/plextrac_api/functions/`: public grouped API functions and shared request helpers.
- `src/plextrac_api/types/`: public dataclasses, enums, and parsing/serialization helpers.
- `src/plextrac_api/generated/endpoints.py`: generated endpoint metadata from the PlexTrac Postman
  collection snapshot.
- `scripts/generate_endpoints.py`: regenerates endpoint metadata and the endpoint coverage section
  in this file.
- `tests/unit/`: focused request-shape, response parsing, enum, webhook, and registry tests.
- `demos/`: git-ignored local demo scripts and credentials/session cache.

## Working Rules For Agents

- Preserve the grouped-function API shape. Do not introduce a monolithic `PlexTrac` client object.
- Pass `AuthSession` explicitly as the first argument to functions that call PlexTrac.
- Keep public polished functions explicit: no public `**kwargs`, `Any`, or `JsonDict` returns.
- Add or reuse dataclasses/enums instead of exposing ambiguous dictionaries or strings when the
  value set or structure is documented.
- Prefer semantic public dataclass field names over raw PlexTrac keys. Map raw keys explicitly in
  `from_api()` and `to_api()`; for example, parse analytics `clientName`, `reportName`, and
  context-specific `id` values into `client_name`, `report_name`, `finding_id`, or `asset_id`.
- Keep shared types in `types.common` only when they are truly cross-cutting; otherwise use the
  matching `types.<group>` module.
- Add generator overrides for intentional endpoint/function naming fixes.
- Use `execute_graphql` as the raw GraphQL escape hatch; do not recreate standalone generated
  GraphQL query/mutation modules unless a unique workflow is intentionally polished.
- Keep webhook support framework-neutral: raw bytes/strings/header mappings in, typed events out.
- Do not commit or expose local demo credentials, `.env` files, session caches, or cache artifacts.

## Verification

Before considering a change complete, run:

```bash
.venv/bin/python -m pytest tests/unit
.venv/bin/python -m ruff check .
```

When generator behavior changes, also run:

```bash
.venv/bin/python scripts/generate_endpoints.py
```

That script must update `src/plextrac_api/generated/endpoints.py` and the generated endpoint
coverage block in this file.

## Documentation Responsibilities

- Keep `README.md` user-facing, concise, and suitable for GitHub.
- Keep `AGENTS.md` focused on contributor/agent context, methodology, and generated endpoint
  inventory.
- Keep detailed implementation rules here, not in `README.md`.
- Keep user-facing usage examples in `README.md`, not here.
- Keep repository documentation split between `README.md` and `AGENTS.md`.
- If public examples change in `README.md`, make sure they still match the actual function/type
  names.

<!-- BEGIN GENERATED ENDPOINT COVERAGE -->
## Endpoint Coverage Snapshot

This generated section inventories the currently known PlexTrac API groups and endpoint wrappers. It is useful for SDK development and gap tracking, but it is not intended to be the primary user guide.

The `clients`, `reports`, `findings`, `assets`, `affected_assets`, `files`, `mailer`, `substatus`, `analytics`, `tenant`, `templates`, `integrations`, `parser_actions`, `scheduler`, `users`, `admin`, `assessments`, `content_library`, and `runbooks` groups are hand-polished and show the intended long-term SDK shape.

The inventory is based on the public PlexTrac Postman collection snapshot.

When multiple documented versions expose the same operation, this SDK keeps only the latest supported version.

Total documented endpoint operations in snapshot: **356**

| API group | Function module | Endpoint functions |
|---|---|---:|
| Authentication | `plextrac_api.functions.auth` | manual auth helpers |
| Admin | `plextrac_api.functions.admin` | 29 explicit functions |
| Affected Assets | `plextrac_api.functions.affected_assets` | 6 explicit functions |
| Analytics | `plextrac_api.functions.analytics` | 10 explicit functions; 1 documented operation not exposed |
| Assessments | `plextrac_api.functions.assessments` | 31 explicit functions; 1 documented operation not exposed |
| Assets | `plextrac_api.functions.assets` | 9 explicit functions; 1 documented operation not exposed |
| Content Library | `plextrac_api.functions.content_library` | 38 explicit functions; 1 documented operation not exposed |
| Clients | `plextrac_api.functions.clients` | 14 explicit functions |
| Files | `plextrac_api.functions.files` | 6 explicit functions |
| Findings | `plextrac_api.functions.findings` | 13 explicit functions |
| Integrations | `plextrac_api.functions.integrations` | 21 explicit functions |
| Mailer | `plextrac_api.functions.mailer` | 3 explicit functions |
| Parser Actions | `plextrac_api.functions.parser_actions` | 8 explicit functions |
| QA Workflow | _not generated_ | 0 |
| Reports | `plextrac_api.functions.reports` | 17 explicit functions |
| Runbooks | `plextrac_api.functions.runbooks` | 62 explicit functions |
| Scheduler | `plextrac_api.functions.scheduler` | 10 explicit functions |
| Substatus | `plextrac_api.functions.substatus` | 4 explicit functions |
| Templates | `plextrac_api.functions.templates` | 14 explicit functions |
| Tenant | `plextrac_api.functions.tenant` | 13 explicit functions |
| Users | `plextrac_api.functions.users` | 16 explicit functions |
| Graph QL Queries | `plextrac_api.functions.common.execute_graphql` | raw GraphQL helper only |
| Graph QL Mutations | `plextrac_api.functions.common.execute_graphql` | raw GraphQL helper only |
| Webhooks | `plextrac_api.functions.webhooks` | typed receiver helpers |

## Method Inventory

### `authentication`

Display name: Authentication

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `authentication` | POST | `/api/v1/authenticate` |  |
| `multi_factor_authentication` | POST | `/api/v1/authenticate/mfa` |  |
| `refresh_token` | PUT | `/api/v1/token/refresh` |  |
| `generate_qr_code` | GET | `/api/v2/user/mfa/qr` |  |
| `activate_mfa` | POST | `/api/v2/user/mfa/qr/activate` |  |

### `admin`

Display name: Admin

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_authentication_providers` | GET | `/api/v2/authenticate/providers` |  |
| `get_tenant_authentication_provider_configuration` | GET | `/api/v2/tenants/{tenantId}/providers/plextrac` |  |
| `update_tenant_authentication_provider_configuration` | POST | `/api/v2/tenants/{tenantId}/providers/plextrac` |  |
| `update_tenant_user_authentication_method` | PUT | `/api/v2/authenticate/tenants/{tenantId}/users/{userId}/configuration` |  |
| `get_saml_configuration` | GET | `/api/v2/tenants/{tenantId}/saml/plextrac` |  |
| `upsert_saml_configuration` | POST | `/api/v2/tenants/{tenantId}/saml/plextrac` |  |
| `get_user_permissions` | GET | `/api/v2/tenants/{tenantId}/user/{userId}/permissions` |  |
| `list_security_role_users` | GET | `/api/v2/tenants/{tenantId}/security/role/{roleKey}/users` |  |
| `add_security_role_user` | PUT | `/api/v2/tenants/{tenantId}/security/role/{roleId}/users` |  |
| `remove_security_role_user` | DELETE | `/api/v2/tenants/{tenantId}/security/role/{roleId}/users/{userId}` |  |
| `list_available_security_roles` | GET | `/api/v2/tenants/{tenantId}/security/role/available` |  |
| `list_security_roles` | GET | `/api/v2/tenants/{tenantId}/security/role` |  |
| `get_security_role` | GET | `/api/v2/tenants/{tenantId}/security/role/{roleId}` |  |
| `check_security_role_name_availability` | POST | `/api/v2/tenants/{tenantId}/security/role/availability` |  |
| `create_security_role` | POST | `/api/v2/tenants/{tenantId}/security/role` |  |
| `update_security_role_info` | PUT | `/api/v2/tenants/{tenantId}/security/role/{roleId}/info` |  |
| `update_security_role_permissions` | PUT | `/api/v2/tenants/{tenantId}/security/role/{roleId}/permissions` |  |
| `delete_security_role` | DELETE | `/api/v2/tenants/{tenantId}/security/role/{roleId}` |  |
| `list_tenant_tags` | GET | `/api/v1/tenant/{tenantId}/tag` |  |
| `create_tenant_tag` | POST | `/api/v1/tenant/{tenantId}/tag` |  |
| `delete_tenant_tag` | DELETE | `/api/v1/tenant/{tenantId}/tag/{tagId}` |  |
| `search_tenant_tags` | GET | `/api/v1/tenant/{tenantId}/tag/search` |  |
| `get_tenant_tag_by_name` | POST | `/api/v1/tenant/{tenantId}/tag/find` |  |
| `list_sla_benchmarks` | GET | `/api/v2/sla/benchmarks` |  |
| `create_sla_benchmark` | POST | `/api/v2/sla/benchmarks` |  |
| `get_sla_benchmark` | GET | `/api/v2/sla/benchmarks/{slaBenchmarkId}` |  |
| `update_sla_benchmark` | PUT | `/api/v2/sla/benchmarks/{slaBenchmarkId}` |  |
| `delete_sla_benchmark` | DELETE | `/api/v2/sla/benchmarks/{slaBenchmarkId}` |  |
| `list_audit_log_entries` | GET | `/api/v2/auditlog` |  |

### `affected_assets`

Display name: Affected Assets

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `import_finding_affected_assets` | POST | `/api/v2/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected-assets/import/{source}` |  |
| `remove_affected_asset` | DELETE | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}` |  |
| `bulk_get_affected_asset_statuses` | POST | `/api/v2/client/{clientId}/report/{reportId}/flaw/{findingId}/assets/status` |  |
| `list_affected_asset_status_updates` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status` |  |
| `create_affected_asset_status_update` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status/update` |  |
| `bulk_create_affected_asset_status_updates` | POST | `/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/status` |  |

### `analytics`

Display name: Analytics

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `retrieve_analytics` | POST | `/api/v1/clients/analytics` |  |
| `retrieve_analytics_findings` | POST | `/api/v1/clients/analytics/findings` |  |
| `retrieve_analytics_findings_aging` | POST | `/api/v1/clients/analytics/findings/aging` |  |
| `get_finding_analytics_bootstrap` | POST | `/api/v2/findingAnalytics/bootstrap` |  |
| `retrieve_analytics_assets` | POST | `/api/v2/clients/analytics/assets/overview` |  |
| `retrieve_analytics_assets_with_filter` | POST | `/api/v2/clients/analytics/assets` |  |
| `retrieve_analytics_trends_opened_closed` | POST | `/api/v2/clients/analytics/trends/opened-closed` |  |
| `retrieve_analytics_trends_from_creation_to_close` | POST | `/api/v2/clients/analytics/trends/from-creation-to-close` |  |
| `retrieve_analytics_trends_age_of_open_findings` | POST | `/api/v2/clients/analytics/trends/age-of-open-findings` | live-unavailable; not exposed in polished module |
| `retrieve_analytics_trends_slas` | POST | `/api/v2/sla/analytics/mean-time` |  |
| `retrieve_analytics_trends_sla_findings` | POST | `/api/v2/sla/analytics/findings` |  |

### `assessments`

Display name: Assessments

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_questions` | GET | `/api/v2/assessments/questionnaires/{questionnaireId}/questions` |  |
| `get_question` | GET | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` |  |
| `create_question` | POST | `/api/v2/assessments/questionnaires/{questionnaireId}/questions` |  |
| `update_question` | PUT | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` |  |
| `update_question_order` | PUT | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}/order` |  |
| `delete_question` | DELETE | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` |  |
| `list_answer_types` | POST | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes` |  |
| `get_answer_type` | GET | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}` |  |
| `update_answer_type` | PUT | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}` |  |
| `create_answer_type` | POST | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/create` |  |
| `delete_answer_type` | DELETE | `/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}` |  |
| `list_questionnaires` | GET | `/api/v1/tenant/{tenantId}/assessments` |  |
| `get_questionnaire` | GET | `/api/v2/assessments/questionnaires/{questionnaireId}` |  |
| `create_questionnaire` | POST | `/api/v2/assessments/questionnaires` |  |
| `update_questionnaire` | PUT | `/api/v2/assessments/questionnaires/{questionnaireId}` |  |
| `delete_questionnaire` | DELETE | `/api/v1/tenant/{tenantId}/assessment/{questionnaireId}` |  |
| `export_questionnaire` | GET | `/api/v2/assessments/questionnaires/{questionnaireId}/export` |  |
| `import_questionnaire` | POST | `/api/v2/import/questionnaire` |  |
| `list_tenant_assessments` | GET | `/api/v2/tenants/{tenantId}/assessments` |  |
| `list_client_assessments_legacy` | GET | `/api/v1/tenant/{tenantId}/client/{clientId}/assessments` | redundant legacy v1 operation; use `list_client_assessments` |
| `list_client_assessments` | GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments` |  |
| `get_client_assessment_details` | GET | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}` |  |
| `get_client_assessment` | GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}` |  |
| `get_assessment_by_cuid` | GET | `/api/v2/assessments/{assessmentCuid}` |  |
| `list_assessment_questions` | GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/questions` |  |
| `list_assessment_answers` | GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers` |  |
| `update_assessment_answers` | PUT | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers` |  |
| `list_assessment_reviewers` | GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/reviewers` |  |
| `create_client_assessment` | POST | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment` |  |
| `update_client_assessment` | PUT | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}` |  |
| `delete_client_assessment` | DELETE | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}` |  |
| `create_report_from_assessment_questionnaire` | POST | `/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}/report` |  |
| `copy_assessment_questionnaire` | POST | `/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy` |  |

### `assets`

Display name: Assets

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_tenant_assets` | POST | `/api/v2/tenant/assets` |  |
| `list_client_assets` | POST | `/api/v2/clients/{clientId}/assets` |  |
| `list_report_assets` | GET | `/api/v2/clients/{clientId}/reports/{reportId}/assets` |  |
| `get_asset` | GET | `/api/v1/client/{clientId}/asset/{assetId}` | `get` |
| `create_asset` | PUT | `/api/v1/client/{clientId}/asset/0` | `create` |
| `update_asset` | PUT | `/api/v1/client/{clientId}/asset/{assetId}` | `update` |
| `delete_asset` | DELETE | `/api/v1/client/{clientId}/asset/{assetId}` | `delete` |
| `import_client_assets` | POST | `/api/v2/client/{clientId}/assets/import/{source}` |  |
| `bulk_delete_client_assets` | POST | `/api/v1/client/{clientId}/bulk/assets/delete` |  |
| `get_scanner_output` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput` | cross-group duplicate; use `findings.get_scanner_output` |

### `content_library`

Display name: Content Library

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_all_sections` | POST | `/api/v2/narratives/sections/all` |  |
| `list_narrative_repository_sections` | POST | `/api/v2/narratives/{repositoryId}/sections` |  |
| `get_narrative_repository_section` | GET | `/api/v2/narratives/sections/{sectionId}` |  |
| `create_narrative_repository` | POST | `/api/v2/narratives/createNarrativesRepository` |  |
| `create_narrative_repository_section` | POST | `/api/v2/narratives/sections` |  |
| `update_narrative_repository_section` | PUT | `/api/v2/narratives/sections/{sectionId}` |  |
| `delete_narrative_repository_section` | DELETE | `/api/v2/narratives/{repositoryId}/sections/{sectionId}` |  |
| `list_narrative_repositories` | POST | `/api/v2/narratives/getAllNarrativesRepositories` |  |
| `copy_section_to_narrative_repository` | POST | `/api/v2/narratives/sections/copy` | live-unavailable; not exposed in polished module |
| `list_all_narrative_repository_users` | POST | `/api/v2/narratives/users/all` |  |
| `list_narrative_repository_users` | POST | `/api/v2/narratives/{narrativeRepositoryId}/users` |  |
| `update_narrative_repository_users` | PUT | `/api/v2/narratives/{narrativeRepositoryId}/users` |  |
| `get_narrative_repository` | GET | `/api/v2/narratives/{narrativeRepositoryId}/getNarrativesRepository` |  |
| `update_narrative_repository` | PUT | `/api/v2/narratives/{narrativeRepositoryId}/updateNarrativesRepository` |  |
| `delete_narrative_repository` | DELETE | `/api/v2/narratives/{narrativeRepositoryId}/deleteNarrativesRepository` |  |
| `list_writeups` | GET | `/api/v1/template/list` |  |
| `get_writeup` | GET | `/api/v1/template/{writeupId}` |  |
| `create_writeup` | POST | `/api/v1/template/create` |  |
| `update_writeup` | PUT | `/api/v1/template/{writeupId}` |  |
| `delete_writeup` | DELETE | `/api/v1/template/{writeupId}` |  |
| `add_writeup_to_report` | PUT | `/api/v1/copy/{writeupId}` | deprecated; not exposed in polished module |
| `bulk_add_writeups_to_report` | POST | `/api/v2/writeups/bulk/addToReport` |  |
| `list_writeups_from_repository` | POST | `/api/v2/repositories/{repositoryId}/getWriteups` |  |
| `add_writeups_to_repository` | POST | `/api/v2/repositories/{repositoryId}/addWriteups` |  |
| `copy_finding_to_writeups_repository` | POST | `/api/v2/repositories/copyFlawToWriteupsRepository` | deprecated; use `create_writeup` instead |
| `import_writeups_to_repository` | POST | `/api/v2/writeups/import/{source}` |  |
| `remove_writeups_from_repository` | POST | `/api/v2/repositories/{repositoryId}/removeWriteup` |  |
| `bulk_copy_writeups` | POST | `/api/v2/writeups/bulk/copy` |  |
| `bulk_move_writeups` | POST | `/api/v2/writeups/bulk/move` |  |
| `bulk_add_tags_to_writeups` | POST | `/api/v2/writeups/bulk/tags` |  |
| `bulk_delete_writeups` | POST | `/api/v2/writeups/bulk/delete` |  |
| `list_writeup_repositories` | POST | `/api/v2/repositories/getAllWriteupsRepositories` |  |
| `list_editable_writeup_repositories` | GET | `/api/v2/repositories/listUserCanEdit` |  |
| `get_writeup_repository` | POST | `/api/v2/repositories/{repositoryId}` |  |
| `create_writeup_repository` | POST | `/api/v2/repositories/add` |  |
| `update_writeup_repository` | POST | `/api/v2/repositories/{repositoryId}/update` |  |
| `delete_writeup_repository` | POST | `/api/v2/repositories/delete` |  |
| `list_writeup_repository_users` | GET | `/api/v2/repositories/{repositoryId}/users` |  |
| `add_writeup_repository_users` | POST | `/api/v2/repositories/{repositoryId}/users` |  |
| `update_writeup_repository_users` | PUT | `/api/v2/repositories/{repositoryId}/users` |  |
| `search_writeup_repository_users` | POST | `/api/v2/repositories/users` |  |

### `clients`

Display name: Clients

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_client_users` | GET | `/api/v2/tenants/{tenantId}/clients/{clientId}/users` |  |
| `list_available_tenant_users` | GET | `/api/v1/tenant/{tenantId}/client/{clientId}/users/available` |  |
| `assign_users_to_client` | POST | `/api/v2/tenant/{tenantId}/client/{clientId}/user/assign` |  |
| `bulk_assign_users_to_client` | POST | `/api/v2/tenant/{tenantId}/client/{clientId}/bulk/users/assign` |  |
| `remove_users_from_client` | POST | `/api/v1/tenant/{tenantId}/client/{clientId}/user/remove` |  |
| `list_tenant_clients` | GET | `/api/v1/tenant/{tenantId}/client/list` |  |
| `list_clients` | POST | `/api/v2/clients` | `list` |
| `get_client` | GET | `/api/v1/client/{clientId}` | `get` |
| `create_client` | POST | `/api/v1/client/create` | `create` |
| `update_client` | PUT | `/api/v1/client/{clientId}` | `update` |
| `delete_client` | DELETE | `/api/v1/client/{clientId}` | `delete` |
| `add_client_logo` | POST | `/api/v1/client/{clientId}/logo` |  |
| `delete_client_logo` | DELETE | `/api/v1/client/{clientId}/logo` |  |
| `list_client_findings` | POST | `/api/v2/client/{clientId}/findings` |  |
| `list_client_assets` | POST | `/api/v2/clients/{clientId}/assets` |  |

### `files`

Display name: Files

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_artifacts` | POST | `/api/v1/file-manager/artifacts` |  |
| `download_artifact` | GET | `/api/v1/file-manager/artifacts/{artifactId}` |  |
| `upload_artifact` | POST | `/api/v1/file-manager/upload` |  |
| `delete_artifact` | DELETE | `/api/v1/file-manager/artifacts/{artifactId}` |  |
| `get_upload_by_name` | GET | `/api/v1/uploads/9bee9f28-7e25-4b4f-8b64-b520fc3c0b7c.png` |  |
| `upload_tenant_image` | POST | `/api/v1/uploads` |  |

### `findings`

Display name: Findings

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `add_findings_from_file_imports` | POST | `/api/v2/client/{clientId}/report/{reportId}/importAsync/{source}` |  |
| `request_presigned_url` | POST | `/api/v2/presigned-url ` |  |
| `add_findings_async_from_preuploaded_file_imports` | POST | `/api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}` |  |
| `get_import_status` | GET | `/api/v2/my-imports` |  |
| `get_scanner_output` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput` |  |
| `bulk_get_evidence` | POST | `/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence` |  |
| `update_evidence` | PUT | `/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}` | live GUID/CUID mismatch; not exposed in polished module |
| `bulk_upsert_evidence` | PUT | `/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence` |  |
| `list_report_findings` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaws` |  |
| `get_findings_by_report` | POST | `/api/v2/clients/{clientId}/reports/{reportId}/findings` |  |
| `get_finding` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `get` |
| `create_finding` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/create` | `create` |
| `update_finding` | PUT | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `update` |
| `bulk_update_findings` | PUT | `/api/v2/clients/{clientId}/reports/{reportId}/findings` | live-unavailable; not exposed in polished module |
| `bulk_update_findings_assign_update_status` | PUT | `/api/v2/client/{clientId}/findings` | live-unavailable; not exposed in polished module |
| `delete_finding` | DELETE | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `delete` |
| `bulk_delete_findings` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaws/delete` |  |
| `get_finding_status_list` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status` |  |
| `create_status_update` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status/update` |  |

### `integrations`

Display name: Integrations

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `get_integration` | GET | `/api/v2/tenant/{tenantId}/integrations/{product}` | `get` |
| `upsert_integration` | POST | `/api/v2/tenant/{tenantId}/integrations/{product}` |  |
| `delete_integration` | DELETE | `/api/v2/tenant/{tenantId}/integrations/{product}` | `delete` |
| `list_tenable_io_tags` | GET | `/api/v2/integrations/tenable-io/tags` |  |
| `sync_tenable_io_tags` | GET | `/api/v2/integrations/tenable-io/tags/sync` |  |
| `list_jira_projects` | GET | `/api/v1/jira/projects` |  |
| `create_and_link_jira_ticket_to_finding` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/createAndLinkJiraTicket` |  |
| `bulk_create_and_link_jira_tickets_to_findings` | POST | `/api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets` |  |
| `create_jira_connection` | POST | `/api/v2/jira/connect` |  |
| `update_jira_connection` | PUT | `/api/v2/jira/connect/{integrationId}` |  |
| `delete_jira_connection` | DELETE | `/api/v2/jira/connect/{integrationId}` |  |
| `set_jira_projects` | POST | `/api/v2/jira/projects/{integrationId}` |  |
| `get_jira_projects` | GET | `/api/v2/jira/integration/projects/{integrationId}` |  |
| `list_jira_issue_mappings` | GET | `/api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings` |  |
| `reset_jira_issue_mappings` | POST | `/api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings/reset` |  |
| `bulk_update_jira_issue_type_mappings` | PUT | `/api/v2/jira/integration/{integrationId}/issues/bulk/mappings` |  |
| `create_jira_tickets_from_findings` | POST | `/api/v2/jira/integration/{integrationId}/issues/create` |  |
| `unlink_jira_ticket_from_findings` | DELETE | `/api/v2/jira/integration/unlink/client/{clientId}/report/{reportId}/finding/{findingId}` |  |
| `list_configurations` | GET | `/api/v2/integrations/configurations` |  |
| `create_configuration` | POST | `/api/v2/integrations/configurations` |  |
| `get_configuration` | GET | `/api/v2/integrations/configurations/{configId}` |  |
| `update_configuration` | PUT | `/api/v2/integrations/configurations/{configId}` |  |
| `delete_configuration` | DELETE | `/api/v2/integrations/configurations/{configId}` |  |

### `mailer`

Display name: Mailer

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_mailer_templates` | GET | `/api/v2/tenants/{tenantId}/mailer/templates` |  |
| `get_email_template` | GET | `/api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD` |  |
| `upsert_email_template` | PUT | `/api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD` |  |

### `parser_actions`

Display name: Parser Actions

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `set_parser_plugin_actions_enabled` | POST | `/api/v1/tenant/{tenantId}/integrationconfig/parserConfig` |  |
| `get_tenant_parsers` | GET | `/api/v1/tenant/{tenantId}/actions` |  |
| `list_tenant_parser_actions` | GET | `/api/v1/tenant/{tenantId}/actions/{parserName}` |  |
| `get_tenant_parser_action` | GET | `/api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}` |  |
| `create_tenant_parser_action` | POST | `/api/v1/tenant/{tenantId}/actions/{parserName}/action` |  |
| `update_parser_action` | PUT | `/api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}` | `update` |
| `bulk_update_tenant_parser_actions` | PUT | `/api/v1/tenant/{tenantId}/actions/{parserName}/bulk` |  |
| `import_parser_plugins` | POST | `/api/v1/tenant/{tenantId}/actions/upload/{source}` |  |

### `qa_workflow`

Display name: QA Workflow

| Method | HTTP | Path | Aliases |
|---|---|---|---|

### `reports`

Display name: Reports

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `count_report_search_occurrences` | POST | `/api/v1/search-replace/occurrences` |  |
| `replace_report_text` | POST | `/api/v1/search-replace` |  |
| `list_client_reports` | GET | `/api/v1/client/{clientId}/reports` |  |
| `list_reports` | POST | `/api/v2/reports` | `list` |
| `get_report` | GET | `/api/v1/client/{clientId}/report/{reportId}` | `get` |
| `create_report` | POST | `/api/v1/client/{clientId}/report/create` | `create` |
| `update_report` | PUT | `/api/v1/client/{clientId}/report/{reportId}` | `update` |
| `delete_report` | DELETE | `/api/v1/client/{clientId}/report/{reportId}` | `delete` |
| `bulk_delete_reports` | POST | `/api/v2/reports/bulk/delete` |  |
| `get_report_exhibit` | GET | `/api/v1/client/{clientId}/report/{reportId}/{exhibitId}` |  |
| `bulk_add_tags_to_reports` | POST | `/api/v2/reports/bulk/tags` |  |
| `bulk_assign_reviewers_to_reports` | POST | `/api/v2/reports/bulk/reviewers` |  |
| `bulk_update_report_statuses` | POST | `/api/v2/reports/bulk/status` |  |
| `export_report_to_ptrac` | GET | `/api/v1/client/{clientId}/report/{reportId}/export/ptrac` |  |
| `export_report_to_word` | GET | `/api/v1/client/{clientId}/report/{reportId}/export/doc` |  |
| `export_report_to_pdf` | GET | `/api/v1/client/{clientId}/report/{reportId}/export/pdf` |  |
| `import_report_from_ptrac` | POST | `/api/v1/client/{clientId}/report/import` |  |

### `runbooks`

Display name: Runbooks

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_runbook_engagement_procedure_operators` | POST | `/graphql` |  |
| `update_runbook_engagement_procedure_operators` | POST | `/graphql` |  |
| `list_runbook_engagement_procedure_assets` | POST | `/graphql` |  |
| `add_runbook_engagement_procedure_assets` | POST | `/graphql` |  |
| `create_runbook_engagement_procedure_asset` | POST | `/graphql` |  |
| `delete_runbook_engagement_procedure_asset` | POST | `/graphql` |  |
| `update_runbook_engagement_procedure_asset` | POST | `/graphql` |  |
| `list_runbook_engagement_procedure_logs` | POST | `/graphql` |  |
| `create_runbook_engagement_procedure_log` | POST | `/graphql` |  |
| `update_runbook_engagement_procedure_log` | POST | `/graphql` |  |
| `delete_runbook_engagement_procedure_log` | POST | `/graphql` |  |
| `list_runbook_engagement_procedure_attachments` | POST | `/graphql` |  |
| `upload_runbook_engagement_procedure_attachment` | POST | `/api/v2/runbooks/engagement-procedures/{engagementProcedureId}/attachments/upload` |  |
| `update_runbook_engagement_procedure_attachments` | POST | `/graphql` | live backend error; not exposed in polished module |
| `delete_runbook_engagement_procedure_attachment` | POST | `/graphql` |  |
| `list_runbook_engagement_procedure_ids` | POST | `/graphql` |  |
| `list_runbook_engagement_procedures` | POST | `/graphql` |  |
| `get_runbook_engagement_procedure` | POST | `/graphql` |  |
| `update_runbook_engagement_procedure` | POST | `/graphql` |  |
| `delete_runbook_engagement_procedure` | POST | `/graphql` |  |
| `list_runbook_engagements` | POST | `/graphql` |  |
| `get_runbook_engagement` | POST | `/graphql` |  |
| `create_runbook_engagement` | POST | `/graphql` |  |
| `update_runbook_engagement` | POST | `/graphql` |  |
| `delete_runbook_engagement` | POST | `/graphql` |  |
| `finish_runbook_engagement` | POST | `/graphql` |  |
| `list_runbook_test_plans` | POST | `/graphql` |  |
| `get_runbook_test_plan` | POST | `/graphql` |  |
| `create_runbook_test_plan` | POST | `/graphql` |  |
| `update_runbook_test_plan` | POST | `/graphql` |  |
| `delete_runbook_test_plan` | POST | `/graphql` |  |
| `list_available_runbook_repository_users` | POST | `/graphql` |  |
| `list_runbook_repository_users` | POST | `/graphql` |  |
| `add_runbook_repository_users` | POST | `/graphql` |  |
| `update_runbook_repository_user` | POST | `/graphql` |  |
| `remove_runbook_repository_user` | POST | `/graphql` |  |
| `list_runbook_repositories` | POST | `/graphql` |  |
| `get_runbook_repository` | POST | `/graphql` |  |
| `create_runbook_repository` | POST | `/graphql` |  |
| `update_runbook_repository` | POST | `/graphql` |  |
| `delete_runbook_repository` | POST | `/graphql` |  |
| `list_runbook_methodologies` | POST | `/graphql` |  |
| `get_runbook_methodology` | POST | `/graphql` |  |
| `create_runbook_methodology` | POST | `/graphql` |  |
| `update_runbook_methodology` | POST | `/graphql` |  |
| `delete_runbook_methodology` | POST | `/graphql` |  |
| `list_runbook_tactics` | POST | `/graphql` |  |
| `get_runbook_tactic` | POST | `/graphql` |  |
| `create_runbook_tactic` | POST | `/graphql` |  |
| `update_runbook_tactic` | POST | `/graphql` |  |
| `delete_runbook_tactic` | POST | `/graphql` |  |
| `list_runbook_techniques` | POST | `/graphql` |  |
| `get_runbook_technique` | POST | `/graphql` |  |
| `create_runbook_technique` | POST | `/graphql` |  |
| `update_runbook_technique` | POST | `/graphql` |  |
| `delete_runbook_technique` | POST | `/graphql` |  |
| `list_runbook_procedures` | POST | `/graphql` |  |
| `get_runbook_procedure` | POST | `/graphql` |  |
| `create_runbook_procedure` | POST | `/graphql` |  |
| `update_runbook_procedure` | POST | `/graphql` |  |
| `delete_runbook_procedure` | POST | `/graphql` |  |
| `export_runbook` | GET | `/api/v1/export/runbook/{runbookId}` | `export` |
| `import_runbook` | POST | `/api/v1/import/runbook` |  |

### `scheduler`

Display name: Scheduler

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `upload_engagement_schedule_event_artifact` | POST | `/api/v2/engagement-schedule-artifacts` |  |
| `list_engagement_schedule_event_artifacts` | GET | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts` |  |
| `update_engagement_schedule_event_artifact` | PATCH | `/api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}` |  |
| `delete_engagement_schedule_event_artifact` | DELETE | `/api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}` |  |
| `download_engagement_schedule_event_artifact` | GET | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}` |  |
| `search_engagement_schedule_events` | POST | `/api/v2/engagement-schedule-events/search` |  |
| `get_engagement_schedule_event` | GET | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}` |  |
| `create_engagement_schedule_event` | POST | `/api/v2/engagement-schedule-events` |  |
| `approve_engagement_schedule_event` | POST | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/approve` |  |
| `update_engagement_schedule_event` | PATCH | `/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}` |  |

### `substatus`

Display name: Substatus

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_substatuses` | GET | `/api/v3/substatus` |  |
| `create_substatus` | POST | `/api/v3/substatus` | `create` |
| `update_substatus` | PATCH | `/api/v3/substatus/{substatusCuid}` | `update` |
| `delete_substatus` | DELETE | `/api/v3/substatus/{substatusCuid}` | `delete` |

### `templates`

Display name: Templates

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_report_templates` | GET | `/api/v1/tenant/{tenantId}/report-templates` |  |
| `get_report_template` | GET | `/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}` |  |
| `create_report_template` | PUT | `/api/v1/tenant/{tenantId}/report-template` |  |
| `update_report_template` | PUT | `/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}` |  |
| `delete_report_template` | DELETE | `/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}` |  |
| `list_finding_templates` | GET | `/api/v1/field-templates` |  |
| `get_finding_template` | GET | `/api/v1/field-template/{findingTemplateId}` |  |
| `create_finding_template` | PUT | `/api/v1/tenant/{tenantId}/field-template` |  |
| `update_finding_template` | PUT | `/api/v1/tenant/{tenantId}/field-template/{findingTemplateId}` |  |
| `delete_finding_template` | DELETE | `/api/v1/tenant/{tenantId}/field-template/{findingTemplateId}` |  |
| `list_export_templates` | GET | `/api/v2/tenant/{tenantId}/export-templates` |  |
| `download_export_template` | GET | `/api/v1/tenant/{tenantId}/export-template/{exportTemplateId}` |  |
| `import_export_template` | POST | `/api/v1/tenant/{tenantId}/template/import` |  |
| `delete_export_template` | DELETE | `/api/v1/tenant/{tenantId}/template/{exportTemplateId}` |  |

### `tenant`

Display name: Tenant

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `update_settings` | PUT | `/api/v2/tenants/{tenantId}/settings` |  |
| `get_tenant` | GET | `/api/v1/tenant/{tenantId}` | `get` |
| `update_tenant` | PUT | `/api/v1/tenant/{tenantId}` | `update` |
| `get_notification_settings` | GET | `/api/v1/tenant/{tenantId}/notificationsettings` |  |
| `update_notification_settings` | PUT | `/api/v1/tenant/{tenantId}/notificationsettings` |  |
| `get_tenant_analytics` | GET | `/api/v1/tenant/{tenantId}/analytics` |  |
| `upload_tenant_logo` | POST | `/api/v1/tenant/{tenantId}/logo` |  |
| `upload_tenant_dark_logo` | POST | `/api/v1/tenant/{tenantId}/logo/dark` |  |
| `delete_tenant_logo` | DELETE | `/api/v1/tenant/{tenantId}/logo` |  |
| `delete_tenant_dark_logo` | DELETE | `/api/v1/tenant/{tenantId}/logo/dark` |  |
| `delete_tenant_icon` | DELETE | `/api/v1/tenant/{tenantId}/icon` |  |
| `delete_tenant_dark_icon` | DELETE | `/api/v1/tenant/{tenantId}/icon/dark` |  |
| `get_root_info` | GET | `/api/v1/` |  |

### `users`

Display name: Users

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `get_authenticated_user` | GET | `/api/v2/whoami` |  |
| `list_tenant_users` | GET | `/api/v1/tenant/{tenantId}/user/list` |  |
| `list_tenant_users_paginated` | GET | `/api/v2/tenants/{tenantId}/users` |  |
| `create_user_deprecated` | POST | `/api/v1/tenant/{tenantId}/user/create` |  |
| `bulk_create_users` | POST | `/api/v1/tenant/{tenantId}/user/create/bulk` |  |
| `update_user` | PUT | `/api/v1/user/update` | `update` |
| `delete_user` | DELETE | `/api/v2/user/delete` | `delete` |
| `change_password` | PUT | `/api/v1/user/changepass` |  |
| `forgot_password` | POST | `/api/v1/user/forgotpass` |  |
| `reset_user_password` | PUT | `/api/v1/tenant/{tenantId}/user/resetpass` |  |
| `set_mfa_token` | PUT | `/api/v1/user/mfa/token` |  |
| `disable_user_mfa_token` | PUT | `/api/v1/user/mfa/token/disable` |  |
| `disable_tenant_user_mfa_token` | PUT | `/api/v1/tenant/{tenantId}/user/mfa/disable` |  |
| `set_user_disabled` | POST | `/api/v1/tenant/{tenantId}/user/toggledisabled` |  |
| `list_user_notifications` | GET | `/api/v1/user/notifications` |  |
| `mark_user_notifications_read` | PUT | `/api/v1/user/notifications` |  |
| `search_user_findings` | POST | `/api/v2/user/findings` |  |

### `graph_ql_queries`

Display name: Graph QL Queries

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `client_asset` | POST | `/graphql` | transport-only; use `assets.get_asset` or raw `execute_graphql` |

### `graph_ql_mutations`

Display name: Graph QL Mutations

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `finding_update` | POST | `/graphql` | transport-only; use `findings.update_finding` or raw `execute_graphql` |
| `narrative_update` | POST | `/graphql` | transport-only; use `reports.update_report` or raw `execute_graphql` |

### `webhooks`

Display name: Webhooks

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `wfa_on_report_finding_creation_edit` | POST | `https://[YOUR_WEBHOOK_LISTENER_URL]` |  |
| `wfa_on_report_creation_edit` | POST | `https://[YOUR_WEBHOOK_LISTENER_URL]` |  |
| `on_report_published` | POST | `https://[YOUR_WEBHOOK_LISTENER_URL]` |  |
| `on_report_finding_published` | POST | `https://[YOUR_WEBHOOK_LISTENER_URL]` |  |
| `on_assessment_submission` | POST | `https://[YOUR_WEBHOOK_LISTENER_URL]` |  |
| `on_scheduler_engagement_submission` | POST | `https://[YOUR_WEBHOOK_LISTENER_URL]` |  |

<!-- END GENERATED ENDPOINT COVERAGE -->

## SDK Methodology

This document defines how this SDK should translate the documented PlexTrac API into a Python
package. When PlexTrac's documentation, generated names, or endpoint versions are awkward, these
rules describe the SDK shape we prefer.

## Goals

The SDK should feel organized, typed, and approachable. It should expose PlexTrac functionality
without becoming one enormous client object full of unrelated methods.

Primary goals:

- Keep the package close to PlexTrac's documented API groups.
- Prefer explicit functions and dataclasses over dynamic catch-all objects.
- Make common workflows pleasant without hiding the underlying HTTP API.
- Keep generated coverage useful, but treat hand-polished wrappers as the final SDK surface.

## Package Shape

Public API calls live in grouped function modules:

```text
plextrac_api.functions.clients
plextrac_api.functions.reports
plextrac_api.functions.findings
```

Types live beside those groups:

```text
plextrac_api.types.common
plextrac_api.types.clients
plextrac_api.types.reports
plextrac_api.types.findings
```

Rules:

- Do not create a single `PlexTrac` object with hundreds of methods.
- Pass `AuthSession` explicitly as the first argument to functions that call PlexTrac.
- Keep shared HTTP behavior, GraphQL behavior, and errors in `functions.common`.
- Keep cross-cutting dataclasses in `types.common`.
- Keep group-specific dataclasses in the matching `types.<group>` module.
- Keep reusable request-shaping types such as `Pagination`, `Sort`, and `Filter` in
  `types.common`.

## Endpoint Version Policy

The SDK should expose one preferred function per operation.

Rules:

- If PlexTrac documents multiple versions of the same operation, expose only the latest supported
  documented version.
- If an operation only exists as `v1`, keep it, but do not include `_v1` in the public function name.
- If an operation only exists as `v2`, keep it, but do not include `_v2` in the public function name.
- Version details belong in docstrings, endpoint coverage docs, and generated metadata, not in the
  normal function name.

Examples:

- `get_authenticated_user_v2` becomes `get_authenticated_user`.
- `import_client_assets_v2` becomes `import_client_assets`.
- `runbook_engagement_list_v2` becomes `runbook_engagement_list`.

## Naming Policy

Function names should be Pythonic and consistent, even when the source documentation is not.

Rules:

- Prefer action-oriented verbs: `list_`, `get_`, `create_`, `update_`, `delete_`, `import_`,
  `export_`, `count_`, `request_`, `upsert_`, and other clear workflow verbs when they describe
  the operation more precisely than the core CRUD verbs.
- Preserve PlexTrac terminology when it is clear.
- Fix names when the documented name is misleading, inconsistent, misspelled, or too awkward for
  normal use.
- Prefer consistency inside a group over strict title-to-function mechanical conversion.
- Add generator overrides for intentional naming fixes so regenerated files stay stable.
- Avoid Python built-in names for public parameters when a clear SDK name exists. Keep the
  documented PlexTrac field name at the wire boundary.

Example:

- PlexTrac's `Available Tenant Users` operation is exposed as `list_available_tenant_users` because
  it returns a list and sits beside `list_client_users`.

## Types Policy

Typed wrappers should be explicit. A polished function should not rely on ambiguous `**kwargs`
inputs or `Any`/`JsonDict` outputs.

Rules:

- Default to explicit structures, schemas, and expected values. Treat looseness as something that
  must be justified by the PlexTrac docs or observed API behavior, not as a convenience.
- Define request dataclasses for structured request bodies when the shape is documented and reused.
- Name reusable request dataclasses with an `Input` suffix when they represent create/update-style
  object payloads, such as `ClientInput`, `ReportInput`, and `FindingInput`.
- Define response dataclasses for documented response objects.
- Do not define request/input dataclasses that are used by only one public function. Use explicit
  function parameters for single-use request bodies.
- When a request/input dataclass is reused by multiple public functions, require that dataclass in
  those functions and do not also offer explicit keyword arguments as an alternative.
- Use concrete return types such as `Client`, `ClientPage`, `list[ClientUser]`, or
  `OperationResult`.
- Use `OperationResult` only for generic operation responses. If an endpoint returns unique
  information, define a dedicated result type that preserves it.
- Do not collapse explicit response fields into vague generic fields. For example, a response
  field named `report_id` should become `ReportCreateResult.report_id`, not
  `OperationResult.id`.
- Use explicit identifier names on domain models when PlexTrac documents them. For example,
  prefer `Client.client_id`, `Report.report_id`, and `Finding.finding_id` over a generic `id`
  property. Keep separate CUID-style document identifiers in a `cuid` field when present.
- Keep raw API payloads available on response dataclasses when useful for debugging or forward
  compatibility, but never use `raw` to construct polished request payloads.
- Do not add public `extra` escape-hatch fields to polished request types or functions. Use the raw
  REST helper for unsupported payload keys instead.
- Do not expose generic `Sort` or `Filter` on polished functions when the endpoint documents field
  names. Define group-specific sort/filter field enums.
- If an endpoint accepts an object or list whose item shape is documented, model that item shape
  with a dataclass instead of `dict`.
- If an endpoint field is truly open-ended, keep the narrowest accurate type and document why in
  the type or function review notes. Examples include service-defined upload form fields or tenant
  custom role codes.
- Use `Enum` for documented finite value sets instead of `Literal` or plain `str`.
- Give enum members readable, unabbreviated names even when the API value is abbreviated.
- Serialize enums back to PlexTrac's documented wire values at the API boundary.
- Use `JsonDict` internally for payload assembly when needed, but do not treat it as the desired
  public return type for polished wrappers.

Examples:

- `SortOrder.ASCENDING` serializes to `"ASC"`.
- `ReportStatus.READY_FOR_REVIEW` serializes to `"Ready For Review"`.
- `ReportReplaceResult` is preferred over `OperationResult` for report text replacement because the
  response includes a meaningful `data` boolean.
- `ReportPtracExport` is preferred over bytes for `.ptrac` export because live PlexTrac returns a
  structured JSON object with report, finding, evidence, client, and procedure sections.

Generated endpoint metadata may include unpolished operation names and raw request shapes. Public
function modules should still expose explicit signatures and typed returns.

## Formatting Policy

Polished public function signatures should be easy to scan as typed API declarations.

Rules:

- Use multiline function signatures for polished public functions, even when the signature would
  fit on one line.
- Put one parameter per line, including `session`.
- Put `*` on its own line when keyword-only arguments are used.
- Put the closing parenthesis and return annotation on their own line.
- Private helpers may stay compact when their signatures are short and obvious.

## Docstring Policy

Polished functions should include concise docstrings that describe the operation from the SDK
user's point of view.

Rules:

- Put docstrings inside the function body, immediately after the function definition.
- Keep docstrings short and practical.
- Do not use docstrings to restate every parameter when type hints already make the signature clear.
- Mention version or transport details only when they are important to the user's decision.

## Generated Metadata vs Polished Functions

The SDK keeps generated metadata and hand-written public wrappers separate:

- Generated endpoint metadata preserves coverage from the PlexTrac Postman collection.
- Hand-written function modules provide the public Python interface.

Generated metadata should be considered inventory, not the final SDK surface. When endpoint names
are intentionally polished, add generator overrides so regeneration does not drift from the public
function names.

The `clients`, `reports`, `findings`, `assets`, `affected_assets`, `files`, `mailer`, `substatus`,
`analytics`, `tenant`, `templates`, `integrations`, `parser_actions`, `scheduler`, `users`,
`admin`, `assessments`, `content_library`, and `runbooks` groups are the current models for
polished groups:

- explicit function arguments
- reusable input dataclasses only when shared across functions
- concrete return types
- group-specific dataclasses
- documented finite value sets represented as enums
- documented sort/filter fields represented as enums
- canonical endpoint version only
- naming fixes where needed
- multiline public function signatures
- concise docstrings

## REST, GraphQL, And Webhooks

REST is the primary SDK surface.

GraphQL policy:

- Keep `execute_graphql` as the raw helper for callers who need direct GraphQL access.
- Do not expose standalone GraphQL query/mutation modules when documented operations overlap
  existing REST-backed domain functions.
- Move a GraphQL operation into the relevant domain group only when it represents a unique workflow
  or response shape that REST does not cover.
- Do not assume GraphQL is a complete replacement for REST.

Webhook policy:

- Webhooks are inbound events, not SDK calls to PlexTrac.
- Keep receiver-side helpers such as signature verification, signature-header lookup, and payload
  parsing.
- Do not depend on a web framework; helpers should accept raw request bytes/strings and header
  mappings.
- Model documented webhook payload identifiers with explicit event dataclasses.
- Preserve raw webhook payloads on parsed events because PlexTrac may include fields beyond the
  documented identifiers.

## Compatibility Policy

This SDK prioritizes a clean Python interface over mirroring every historical PlexTrac API variant.

Rules:

- Do not expose deprecated or superseded versions solely for completeness.
- Keep raw request helpers available for edge cases.
- When the SDK intentionally renames or collapses an operation, document that decision in the
  generator, endpoint coverage, or this methodology.

## Implementation Checklist For A Group

When polishing an API group:

1. Review the documented endpoints and response examples.
2. Identify duplicate versions and select the latest supported endpoint per operation.
3. Choose consistent Python function names.
4. Add any required generator naming overrides.
5. Define shared dataclasses in `types.common` only when they are cross-cutting.
6. Define group-specific dataclasses in `types.<group>`.
7. Use explicit function parameters for single-use request bodies.
8. Use request dataclasses only when the same input type is reused across multiple public functions.
9. Do not provide both a request dataclass and explicit keyword alternatives for the same function.
10. Replace ambiguous `**kwargs` wrappers with explicit function arguments.
11. Replace `Any`/`JsonDict` public returns with concrete return types.
12. Replace documented finite string sets with enums that use readable member names.
13. Replace documented sort/filter field strings with group-specific enums.
14. Replace documented nested dictionaries with dataclasses.
15. Use dedicated result types instead of `OperationResult` when endpoint responses contain unique
    information.
16. Format public function signatures across multiple lines.
17. Add concise docstrings to polished functions.
18. Update endpoint coverage and docs.
19. Add tests for request shape, response parsing, enum serialization, and naming regressions.
