# Endpoint Coverage Snapshot

This file is an inventory of the currently known PlexTrac API groups and endpoint wrappers. It is useful for SDK development and gap tracking, but it is not intended to be the primary user guide.

Most groups are still generated wrappers. The `clients`, `reports`, `findings`, `assets`, `affected_assets`, `files`, `mailer`, `substatus`, `analytics`, `tenant`, `templates`, `integrations`, `parser_actions`, `scheduler`, `users`, `admin`, `assessments`, and `content_library` groups are hand-polished and show the intended long-term SDK shape.

The inventory is based on the public PlexTrac Postman collection snapshot.

When multiple documented versions expose the same operation, this SDK keeps only the latest supported version.

Total supported endpoint functions in snapshot: **357**

| API group | Function module | Endpoint functions |
|---|---|---:|
| Authentication | `plextrac_api.functions.auth` | manual auth helpers |
| Admin | `plextrac_api.functions.admin` | 29 explicit functions |
| Affected Assets | `plextrac_api.functions.affected_assets` | 6 explicit functions |
| Analytics | `plextrac_api.functions.analytics` | 11 explicit functions |
| Assessments | `plextrac_api.functions.assessments` | 32 explicit functions |
| Assets | `plextrac_api.functions.assets` | 9 explicit functions |
| Content Library | `plextrac_api.functions.content_library` | 39 explicit functions |
| Clients | `plextrac_api.functions.clients` | 14 explicit functions |
| Files | `plextrac_api.functions.files` | 6 explicit functions |
| Findings | `plextrac_api.functions.findings` | 16 explicit functions |
| Integrations | `plextrac_api.functions.integrations` | 21 explicit functions |
| Mailer | `plextrac_api.functions.mailer` | 3 explicit functions |
| Parser Actions | `plextrac_api.functions.parser_actions` | 8 explicit functions |
| QA Workflow | _not generated_ | 0 |
| Reports | `plextrac_api.functions.reports` | 17 explicit functions |
| Runbooks | `plextrac_api.functions.runbooks` | 63 |
| Scheduler | `plextrac_api.functions.scheduler` | 10 explicit functions |
| Substatus | `plextrac_api.functions.substatus` | 4 explicit functions |
| Templates | `plextrac_api.functions.templates` | 14 explicit functions |
| Tenant | `plextrac_api.functions.tenant` | 13 explicit functions |
| Users | `plextrac_api.functions.users` | 16 explicit functions |
| Graph QL Queries | `plextrac_api.functions.graph_ql_queries` | 1 |
| Graph QL Mutations | `plextrac_api.functions.graph_ql_mutations` | 2 |
| Webhooks | `plextrac_api.functions.webhooks` | manual receiver helper |

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
| `find_tenant_tag` | POST | `/api/v1/tenant/{tenantId}/tag/find` |  |
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
| `analytics_trends_opened_closed` | POST | `/api/v2/clients/analytics/trends/opened-closed` |  |
| `analytics_trends_from_creation_to_close` | POST | `/api/v2/clients/analytics/trends/from-creation-to-close` |  |
| `analytics_trends_age_of_open_findings` | POST | `/api/v2/clients/analytics/trends/age-of-open-findings` |  |
| `analytics_trends_slas` | POST | `/api/v2/sla/analytics/mean-time` |  |
| `analytics_trends_sla_findings` | POST | `/api/v2/sla/analytics/findings` |  |

### `assessments`

Display name: Assessments

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `list_questions` | GET | `/api/v2/assessments/questionnaires/{questionnaireId}/questions` |  |
| `get_question` | GET | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` |  |
| `create_question` | POST | `/api/v2/assessments/questionnaires/{questionnaireId}/questions` |  |
| `update_question` | PUT | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}` |  |
| `change_question_order` | PUT | `/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}/order` |  |
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
| `list_client_assessments_legacy` | GET | `/api/v1/tenant/{tenantId}/client/{clientId}/assessments` |  |
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
| `get_tenant_assets` | POST | `/api/v2/tenant/assets` |  |
| `get_assets_by_client` | POST | `/api/v2/clients/{clientId}/assets` |  |
| `list_client_assets` | GET | `/api/v1/client/{clientId}/assets` |  |
| `list_report_assets` | GET | `/api/v2/clients/{clientId}/reports/{reportId}/assets` |  |
| `get_asset` | GET | `/api/v1/client/{clientId}/asset/{assetId}` | `get` |
| `create_asset` | PUT | `/api/v1/client/{clientId}/asset/0` | `create` |
| `update_asset` | PUT | `/api/v1/client/{clientId}/asset/{assetId}` | `update` |
| `delete_asset` | DELETE | `/api/v1/client/{clientId}/asset/{assetId}` | `delete` |
| `import_client_assets` | POST | `/api/v2/client/{clientId}/assets/import/{source}` |  |
| `bulk_delete_client_assets` | POST | `/api/v1/client/{clientId}/bulk/assets/delete` |  |
| `get_scanner_output` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput` |  |

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
| `copy_section_to_narrative_repository` | POST | `/api/v2/narratives/sections/copy` |  |
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
| `add_writeup_to_report` | PUT | `/api/v1/copy/{writeupId}` | `deprecated; not exposed in polished module` |
| `bulk_add_writeups_to_report` | POST | `/api/v2/writeups/bulk/addToReport` |  |
| `list_writeups_from_repository` | POST | `/api/v2/repositories/{repositoryId}/getWriteups` |  |
| `add_writeups_to_repository` | POST | `/api/v2/repositories/{repositoryId}/addWriteups` |  |
| `copy_finding_to_writeups_repository` | POST | `/api/v2/repositories/copyFlawToWriteupsRepository` | `deprecated; use create_writeup instead` |
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
| `update_evidence` | PUT | `/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}` |  |
| `bulk_upsert_evidence` | PUT | `/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence` |  |
| `list_report_findings` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaws` |  |
| `get_findings_by_report` | POST | `/api/v2/clients/{clientId}/reports/{reportId}/findings` |  |
| `get_finding` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `get` |
| `create_finding` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/create` | `create` |
| `update_finding` | PUT | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `update` |
| `bulk_update_findings` | PUT | `/api/v2/clients/{clientId}/reports/{reportId}/findings` |  |
| `bulk_update_findings_assign_update_status` | PUT | `/api/v2/client/{clientId}/findings` |  |
| `delete_finding` | DELETE | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}` | `delete` |
| `bulk_delete_findings` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaws/delete` |  |
| `get_finding_status_list` | GET | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status` |  |
| `create_status_update` | POST | `/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status/update` |  |

### `integrations`

Display name: Integrations

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `get_integration` | GET | `/api/v2/tenant/{tenantId}/integrations/{product}` | `get` |
| `save_integration` | POST | `/api/v2/tenant/{tenantId}/integrations/{product}` |  |
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
| `runbook_engagement_procedure_operator_list` | POST | `/graphql` |  |
| `runbook_engagement_procedure_operators_update` | POST | `/graphql` |  |
| `runbook_engagement_procedure_asset_list` | POST | `/graphql` |  |
| `runbook_engagement_procedure_assets_add` | POST | `/graphql` |  |
| `runbook_engagement_procedure_asset_create` | POST | `/graphql` |  |
| `runbook_engagement_procedure_asset_delete` | POST | `/graphql` |  |
| `runbook_engagement_procedure_asset_update` | POST | `/graphql` |  |
| `runbook_engagement_procedure_logs` | POST | `/graphql` |  |
| `runbook_engagement_procedure_log_create` | POST | `/graphql` |  |
| `runbook_engagement_procedure_log_update` | POST | `/graphql` |  |
| `runbook_engagement_procedure_log_delete` | POST | `/graphql` |  |
| `runbook_engagement_procedure_attachment_list` | POST | `/graphql` |  |
| `upload_attachment_to_engagement_procedure` | POST | `/api/v2/runbooks/engagement-procedures/{engagementProcedureId}/attachments/upload` |  |
| `runbook_engagement_procedure_attachments_update` | POST | `/graphql` |  |
| `runbook_engagement_procedure_attachment_delete` | POST | `/graphql` |  |
| `runbook_engagement_procedure_ids` | POST | `/graphql` |  |
| `runbook_engagement_procedure_list` | POST | `/graphql` |  |
| `runbook_engagement_procedure_detail` | POST | `/graphql` |  |
| `runbook_engagement_procedure_update` | POST | `/graphql` |  |
| `runbook_engagement_procedure_delete` | POST | `/graphql` |  |
| `runbook_engagement_list` | POST | `/graphql` |  |
| `runbook_engagement_detail` | POST | `/graphql` |  |
| `runbook_engagement_create` | POST | `/graphql` |  |
| `runbook_engagement_update` | POST | `/graphql` |  |
| `runbook_engagement_delete` | POST | `/graphql` |  |
| `runbook_engagement_finish` | POST | `/graphql` |  |
| `runbook_test_plan_list` | POST | `/graphql` |  |
| `runbook_test_plan_detail` | POST | `/graphql` |  |
| `runbook_test_plan_create` | POST | `/graphql` |  |
| `runbook_test_plan_update` | POST | `/graphql` |  |
| `runbook_test_plan_delete` | POST | `/graphql` |  |
| `runbook_repository_available_user_list` | POST | `/graphql` |  |
| `runbook_repository_users` | POST | `/graphql` |  |
| `runbook_repository_users_add` | POST | `/graphql` |  |
| `runbook_repository_user_update` | POST | `/graphql` |  |
| `runbook_repository_user_remove` | POST | `/graphql` |  |
| `runbook_repository_list` | POST | `/graphql` |  |
| `runbook_repository_detail` | POST | `/graphql` |  |
| `runbook_repository_create` | POST | `/graphql` |  |
| `runbook_repository_update` | POST | `/graphql` |  |
| `runbook_repository_delete` | POST | `/graphql` |  |
| `runbook_methodology_list` | POST | `/graphql` |  |
| `runbook_methodology_detail` | POST | `/graphql` |  |
| `runbook_methodology_create` | POST | `/graphql` |  |
| `runbook_methodology_update` | POST | `/graphql` |  |
| `runbook_methodology_delete` | POST | `/graphql` |  |
| `runbook_tactic_list` | POST | `/graphql` |  |
| `runbook_tactic_detail` | POST | `/graphql` |  |
| `runbook_tactic_create` | POST | `/graphql` |  |
| `runbook_tactic_update` | POST | `/graphql` |  |
| `runbook_tactic_delete` | POST | `/graphql` |  |
| `runbook_technique_list` | POST | `/graphql` |  |
| `runbook_technique_detail` | POST | `/graphql` |  |
| `runbook_technique_create` | POST | `/graphql` |  |
| `runbook_technique_update` | POST | `/graphql` |  |
| `runbook_technique_delete` | POST | `/graphql` |  |
| `runbook_procedure_list` | POST | `/graphql` |  |
| `runbook_procedure_detail` | POST | `/graphql` |  |
| `runbook_procedure_create` | POST | `/graphql` |  |
| `runbook_procedure_update` | POST | `/graphql` |  |
| `runbook_procedure_delete` | POST | `/graphql` |  |
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
| `client_asset` | POST | `/graphql` |  |

### `graph_ql_mutations`

Display name: Graph QL Mutations

| Method | HTTP | Path | Aliases |
|---|---|---|---|
| `finding_update` | POST | `/graphql` |  |
| `narrative_update` | POST | `/graphql` |  |

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
