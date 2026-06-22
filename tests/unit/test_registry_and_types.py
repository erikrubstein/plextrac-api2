from plextrac_api.functions import __all__ as function_groups
from plextrac_api.generated.endpoints import GROUPS
from plextrac_api.types import (
    AffectedAsset,
    AffectedAssetBulkStatusUpdate,
    AffectedAssetStatus,
    AffectedAssetStatusMap,
    AffectedAssetStatusUpdate,
    AnalyticsFilter,
    AnalyticsRecord,
    AnalyticsResult,
    AnalyticsTags,
    AnalyticsTrendFilter,
    AnswerOption,
    Artifact,
    ArtifactRelation,
    ArtifactRelationModel,
    ArtifactUploadResult,
    Assessment,
    AssessmentAnswer,
    AssessmentAnswerField,
    AssessmentCreateResult,
    AssessmentSortOrder,
    Asset,
    AssetAnalyticsFilter,
    AssetCreateResult,
    AssetCriticality,
    AssetInput,
    AssetType,
    AuditLogEntry,
    AuditLogEventType,
    AuthenticationProvider,
    AuthenticationProviderConfiguration,
    AuthenticationProviderName,
    Client,
    ClientAssessmentInput,
    ClientAssetFilter,
    ClientAssetFilterField,
    ClientAssetSort,
    ClientAssetSortField,
    ClientCreateResult,
    ClientFilter,
    ClientFilterField,
    ClientFindingFilter,
    ClientFindingFilterField,
    ClientFindingPageLimit,
    ClientFindingPagination,
    ClientPageLimit,
    ClientPagination,
    ClientSort,
    ClientSortField,
    CodeSample,
    ContentLibraryUser,
    ContentLibraryUserInput,
    CurrentUserUpdate,
    DefaultUserRole,
    EmailTemplate,
    EmailTemplateKind,
    EngagementScheduleEventSearch,
    ExportTemplateType,
    Filter,
    Finding,
    FindingAnalyticsAssetPagination,
    FindingAnalyticsBootstrapFilter,
    FindingAnalyticsBootstrapOrderField,
    FindingCreateResult,
    FindingEvidenceUpdate,
    FindingField,
    FindingFilter,
    FindingFilterField,
    FindingImportStatus,
    FindingPageLimit,
    FindingPagination,
    FindingSeverity,
    FindingSort,
    FindingSortField,
    FindingStatus,
    FindingTemplate,
    FindingTemplateInput,
    FindingVisibility,
    IntegrationConfigurationInput,
    IntegrationConfigurationType,
    JiraConnectionInput,
    JiraSyncFrequency,
    NarrativeRepository,
    NarrativeRepositoryInput,
    NarrativeSectionInput,
    OperationResult,
    Pagination,
    ParserActionInput,
    ParserActionType,
    ParserPluginSource,
    QuestionAnswerType,
    QuestionInput,
    Questionnaire,
    QuestionnaireInput,
    Report,
    ReportCreateResult,
    ReportFilter,
    ReportFilterField,
    ReportPageLimit,
    ReportPagination,
    ReportSort,
    ReportSortField,
    ReportStatus,
    RoleNameAvailability,
    RunbookListArgs,
    RunbookMutationResult,
    RunbookProcedureLog,
    RunbookProcedureLogInput,
    RunbookRecordInput,
    RunbookRepository,
    RunbookTag,
    RunbookTeam,
    RunbookUploadResult,
    SamlConfiguration,
    SlaAnalyticsFilter,
    SlaAssetCriticality,
    SLABenchmark,
    SLABenchmarkNotificationSettings,
    SLABenchmarkResult,
    Sort,
    SortOrder,
    Substatus,
    SubstatusInput,
    SubstatusStatus,
    TemplateField,
    Tenant,
    TenantAssessmentSort,
    TenantAssetFilter,
    TenantAssetFilterField,
    TenantAssetSort,
    TenantAssetSortField,
    TenantImageUploadResult,
    TenantUserInput,
    UserFindingSearch,
    Writeup,
    WriteupDeleteResult,
    WriteupImportSource,
    WriteupRepository,
    WriteupRepositoryInput,
    WriteupTransfer,
)


def test_generated_registry_covers_public_snapshot():
    total = sum(len(group["endpoints"]) for group in GROUPS.values())

    assert total == 356
    assert "clients" in GROUPS
    assert "assets" in GROUPS
    assert "reports" in GROUPS
    assert "findings" in GROUPS
    assert "runbooks" in GROUPS


def test_graphql_transport_groups_are_not_public_function_modules():
    assert "graph_ql_queries" in GROUPS
    assert "graph_ql_mutations" in GROUPS
    assert "graph_ql_queries" not in function_groups
    assert "graph_ql_mutations" not in function_groups


def test_generated_registry_exposes_canonical_latest_names():
    method_names = [
        endpoint["method_name"]
        for group in GROUPS.values()
        for endpoint in group["endpoints"]
    ]

    assert "get_authenticated_user" in method_names
    assert "get_authenticated_user_v1" not in method_names
    assert "get_authenticated_user_v2" not in method_names
    assert "list_authentication_providers" in method_names
    assert "get_available_authentication_providers" not in method_names
    assert "get_tenant_authentication_provider_configuration" in method_names
    assert "get_tenant_provider_authentication_configuration" not in method_names
    assert "get_saml_configuration" in method_names
    assert "get_saml_provider" not in method_names
    assert "list_security_role_users" in method_names
    assert "get_role_users" not in method_names
    assert "add_security_role_user" in method_names
    assert "add_role_user" not in method_names
    assert "remove_security_role_user" in method_names
    assert "remove_role_user" not in method_names
    assert "list_available_security_roles" in method_names
    assert "get_available_security_roles" not in method_names
    assert "list_security_roles" in method_names
    assert "get_security_roles" not in method_names
    assert "check_security_role_name_availability" in method_names
    assert "get_role_name_availability" not in method_names
    assert "update_security_role_permissions" in method_names
    assert "update_security_role_permission" not in method_names
    assert "list_sla_benchmarks" in method_names
    assert "get_sla_benchmarks" not in method_names
    assert "list_audit_log_entries" in method_names
    assert "get_audit_log" not in method_names
    assert "list_tenant_assets" in method_names
    assert "get_tenant_assets" not in method_names
    assert "list_client_assets" in method_names
    assert "get_assets_by_client" not in method_names
    from plextrac_api.functions import assets

    assert not hasattr(assets, "get_scanner_output")
    assert "list_client_assessments" in method_names
    assert "list_client_assessments_filtered" not in method_names
    assert "list_client_assessments_legacy" in method_names
    from plextrac_api.functions import assessments

    assert not hasattr(assessments, "list_client_assessments_legacy")
    assert "get_client_assessment_details" in method_names
    assert "get_client_assessment_with_questions_and_answers" not in method_names
    assert "list_assessment_questions" in method_names
    assert "get_assessment_questions" not in method_names
    assert "list_assessment_answers" in method_names
    assert "get_assessment_answers" not in method_names
    assert "list_assessment_reviewers" in method_names
    assert "get_assessment_reviewers" not in method_names
    assert "copy_assessment_questionnaire" in method_names
    assert "copy_asessment_questionnaire" not in method_names
    assert "update_question_order" in method_names
    assert "change_question_order" not in method_names
    assert "retrieve_analytics_trends_opened_closed" in method_names
    assert "analytics_trends_opened_closed" not in method_names
    assert "retrieve_analytics_trends_from_creation_to_close" in method_names
    assert "analytics_trends_from_creation_to_close" not in method_names
    assert "analytics_trends_age_of_open_findings" not in method_names
    assert "retrieve_analytics_trends_slas" in method_names
    assert "analytics_trends_slas" not in method_names
    assert "retrieve_analytics_trends_sla_findings" in method_names
    assert "analytics_trends_sla_findings" not in method_names
    assert "upsert_integration" in method_names
    assert "save_integration" not in method_names
    assert "get_tenant_tag_by_name" in method_names
    assert "find_tenant_tag" not in method_names
    assert "list_runbook_engagements" in method_names
    assert "runbook_engagement_list" not in method_names
    assert "get_runbook_engagement" in method_names
    assert "runbook_engagement_detail" not in method_names
    assert "create_runbook_repository" in method_names
    assert "runbook_repository_create" not in method_names
    assert "list_available_runbook_repository_users" in method_names
    assert "list_available_list_runbook_repository_users" not in method_names
    assert "add_runbook_repository_users" in method_names
    assert "list_add_runbook_repository_users" not in method_names
    assert "list_available_tenant_users" in method_names
    assert "available_tenant_users" not in method_names
    assert "assign_users_to_client" in method_names
    assert "assign_user_to_client" not in method_names
    assert "remove_users_from_client" in method_names
    assert "remove_user_from_client" not in method_names
    assert "list_reports" in method_names
    assert "get_report_list" not in method_names
    assert "count_report_search_occurrences" in method_names
    assert "search_replace_in_report_occurrences" not in method_names
    assert "bulk_update_report_statuses" in method_names
    assert "bulk_adjust_status_of_report" not in method_names
    assert "remove_affected_asset" in method_names
    assert "remove_affected_asset_from_flaw" not in method_names
    assert "bulk_get_affected_asset_statuses" in method_names
    assert "bulk_get_affected_assets_status" not in method_names
    assert "list_artifacts" in method_names
    assert "get_artifacts" not in method_names
    assert "download_artifact" in method_names
    assert "download_an_artifact" not in method_names
    assert "upload_artifact" in method_names
    assert "upload_an_artifact_file" not in method_names
    assert "delete_artifact" in method_names
    assert "delete_an_artifact" not in method_names
    assert "upload_tenant_image" in method_names
    assert "upload_image_to_tenant" not in method_names
    assert "list_mailer_templates" in method_names
    assert "get_mailer_templates" not in method_names
    assert "list_substatuses" in method_names
    assert "list_substatus" not in method_names
    assert "retrieve_analytics_findings_aging" in method_names
    assert "retreive_analytics_findings_aging" not in method_names
    assert "get_tenant_analytics" in method_names
    assert "tenant_analytics" not in method_names
    assert "upload_tenant_logo" in method_names
    assert "add_tenant_logo" not in method_names
    assert "delete_tenant_dark_icon" in method_names
    assert "delete_tenant_icon_dark" not in method_names
    assert "get_root_info" in method_names
    assert "root_request" not in method_names
    assert "list_finding_templates" in method_names
    assert "list_findings_templates" not in method_names
    assert "get_finding_template" in method_names
    assert "get_findings_template" not in method_names
    assert "download_export_template" in method_names
    assert "get_export_template" not in method_names
    assert "list_configurations" in method_names
    assert "get_configurations" not in method_names
    assert "create_configuration" in method_names
    assert "create_configurations" not in method_names
    assert "list_tenable_io_tags" in method_names
    assert "tenable_io_get_tags" not in method_names
    assert "sync_tenable_io_tags" in method_names
    assert "tenable_io_sync_tags" not in method_names
    assert "list_jira_issue_mappings" in method_names
    assert "get_issue_mapping_types" not in method_names
    assert "reset_jira_issue_mappings" in method_names
    assert "reset_issue_mapping_types" not in method_names
    assert "bulk_update_jira_issue_type_mappings" in method_names
    assert "bulk_update_issue_type_mappings" not in method_names
    assert "create_jira_tickets_from_findings" in method_names
    assert "create_jira_ticket_from_findings" not in method_names
    assert "list_tenant_parser_actions" in method_names
    assert "get_tenant_parser_actions" not in method_names
    assert "set_parser_plugin_actions_enabled" in method_names
    assert "enable_disable_parser_plugin_actions" not in method_names
    assert "upload_engagement_schedule_event_artifact" in method_names
    assert "create_engagement_schedule_event_artifact" not in method_names
    assert "search_engagement_schedule_events" in method_names
    assert "find_many_engagement_schedule_events" not in method_names
    assert "get_engagement_schedule_event" in method_names
    assert "get_engagement_schedule_event_by_id" not in method_names
    assert "list_tenant_users_paginated" in method_names
    assert "get_tenants_users" not in method_names
    assert "bulk_create_users" in method_names
    assert "bulk_create_user" not in method_names
    assert "disable_tenant_user_mfa_token" in method_names
    assert "disable_other_user_mfa_token" not in method_names
    assert "set_user_disabled" in method_names
    assert "enable_disable_user" not in method_names
    assert "list_user_notifications" in method_names
    assert "get_user_notifications" not in method_names
    assert "mark_user_notifications_read" in method_names
    assert "set_user_notifications_read" not in method_names
    assert "search_user_findings" in method_names
    assert "get_user_findings" not in method_names
    assert "create_narrative_repository" in method_names
    assert "create_narratives_db_repository" not in method_names
    assert "copy_section_to_narrative_repository" in method_names
    assert "copy_section_to_narative_repository" not in method_names
    assert "create_writeup" in method_names
    assert "create_writeups" not in method_names
    assert "list_writeup_repositories" in method_names
    assert "list_all_writeup_repositories" not in method_names
    assert "search_writeup_repository_users" in method_names
    assert "get_all_writeups_repository_users" not in method_names
    assert all(not name.endswith(("_v1", "_v2", "_v3")) for name in method_names)


def test_client_type_parses_documented_fields():
    client = Client.from_api(
        {
            "client_id": 1,
            "cuid": "client-cuid",
            "tenant_id": 2,
            "name": "Example",
            "poc": "Alice",
            "poc_email": "alice@example.com",
            "custom_field": [{"label": "Region", "value": "North"}],
            "users": {"user@example.com": {"role": "ADMIN", "classificationId": "abc"}},
        }
    )

    assert client.client_id == 1
    assert client.cuid == "client-cuid"
    assert client.name == "Example"
    assert client.poc == "Alice"
    assert client.poc_email == "alice@example.com"
    assert client.custom_fields[0].label == "Region"
    assert client.users["user@example.com"].role == "ADMIN"

    camel_client = Client.from_api(
        {
            "id": 2,
            "clientId": 3,
            "tenantId": 4,
            "classification_id": "classification-1",
            "docType": "client",
        }
    )

    assert camel_client.client_id == 3
    assert camel_client.tenant_id == 4
    assert camel_client.classification_id == "classification-1"
    assert camel_client.doc_type == "client"

    nested_client = Client.from_api(
        {
            "data": {
                "client_id": 5,
                "tenant_id": 0,
                "name": "Nested Client",
                "poc": "Nested POC",
            }
        }
    )

    assert nested_client.client_id == 5
    assert nested_client.tenant_id == 0
    assert nested_client.name == "Nested Client"
    assert nested_client.poc == "Nested POC"
    assert nested_client.raw == {
        "data": {
            "client_id": 5,
            "tenant_id": 0,
            "name": "Nested Client",
            "poc": "Nested POC",
        }
    }


def test_asset_type_parses_documented_fields():
    asset = Asset.from_api(
        {
            "id": "asset-1",
            "asset": "host1",
            "clientId": 1,
            "assetCriticality": "High",
            "type": "Server",
            "knownIps": ["192.0.2.1"],
            "dnsName": "host1.example.com",
            "macAddress": "00:11:22:33:44:55",
            "ports": {"443": {"number": "443", "service": "https", "protocol": "tcp"}},
        }
    )

    assert asset.asset_id == "asset-1"
    assert asset.name == "host1"
    assert asset.client_id == 1
    assert asset.criticality is AssetCriticality.HIGH
    assert asset.asset_type is AssetType.SERVER
    assert asset.dns_name == "host1.example.com"
    assert asset.mac_address == "00:11:22:33:44:55"
    assert asset.ports["443"].protocol == "tcp"


def test_client_request_shape_types_serialize_with_verified_fields():
    assert Pagination(limit=50, offset=25).to_api() == {"offset": 25, "limit": 50}
    assert Sort(by="name", order=SortOrder.DESCENDING).to_api() == {"by": "name", "order": "DESC"}
    assert Filter(by="tags", value=["external"]).to_api() == {"by": "tags", "value": ["external"]}
    assert ClientPagination(limit=ClientPageLimit.FIFTY, offset=25).to_api() == {
        "offset": 25,
        "limit": 50,
    }
    assert ClientPagination().to_api() == {
        "offset": 0,
        "limit": 25,
    }
    assert ClientFindingPagination(limit=ClientFindingPageLimit.ALL).to_api() == {
        "offset": 0,
        "limit": 99999,
    }
    assert ClientFindingPagination().to_api() == {
        "offset": 0,
        "limit": 10,
    }
    assert ClientSort(by=ClientSortField.NAME, order=SortOrder.DESCENDING).to_api() == {
        "by": "name",
        "order": "DESC",
    }
    assert ClientFilter(by=ClientFilterField.TAGS, value=["external"]).to_api() == {
        "by": "tags",
        "value": ["external"],
    }
    assert ClientFindingFilter(
        by=ClientFindingFilterField.VISIBILITY,
        value=FindingVisibility.PUBLISHED,
    ).to_api() == {
        "by": "visibility",
        "value": "published",
    }


def test_operation_result_does_not_flatten_specific_ids():
    result = OperationResult.from_api({"status": "success", "report_id": 42})

    assert result.ok
    assert not hasattr(result, "id")
    assert result.raw == {"status": "success", "report_id": 42}


def test_operation_result_treats_non_object_success_response_as_ok():
    result = OperationResult.from_api([])

    assert result.ok
    assert result.raw == {"ok": True, "data": []}


def test_operation_result_treats_boolean_success_flags_as_ok():
    assert OperationResult.from_api({"deleted": True}).ok
    assert OperationResult.from_api({"created": True}).ok
    assert OperationResult.from_api({"updated": True}).ok


def test_operation_result_treats_punctuated_success_text_as_ok():
    assert OperationResult.from_api({"status": "success!"}).ok


def test_create_result_types_preserve_specific_identifiers():
    assert ClientCreateResult.from_api({"client_id": 1, "created": True}).client_id == 1
    assert (
        ClientCreateResult.from_api({"data": {"clientId": 2}, "status": "success"}).client_id
        == 2
    )
    assert ClientCreateResult.from_api({"data": {"id": 0}, "status": "success"}).client_id == 0
    assert AssetCreateResult.from_api({"id": "asset-1", "status": "success"}).asset_id == "asset-1"
    assert (
        AssetCreateResult.from_api({"data": {"assetId": "asset-2"}, "status": "success"}).asset_id
        == "asset-2"
    )
    assert ReportCreateResult.from_api({"report_id": 42, "message": "success"}).report_id == 42
    assert FindingCreateResult.from_api({"flaw_id": 99, "status": "success"}).finding_id == 99


def test_asset_request_shape_types_serialize_with_verified_fields():
    assert TenantAssetSort(
        by=TenantAssetSortField.ASSET_CRITICALITY,
        order=SortOrder.DESCENDING,
    ).to_api() == {
        "by": "assetCriticality",
        "order": "DESC",
    }
    assert TenantAssetFilter(by=TenantAssetFilterField.TAGS, value=["external"]).to_api() == {
        "by": "tags",
        "value": ["external"],
    }
    assert ClientAssetSort(by=ClientAssetSortField.ASSET, order=SortOrder.ASCENDING).to_api() == {
        "by": "asset",
        "order": "ASC",
    }
    assert ClientAssetFilter(by=ClientAssetFilterField.TAGS, value=["none"]).to_api() == {
        "by": "tags",
        "value": ["none"],
    }
    assert AssetInput(
        name="host1",
        asset_type=AssetType.SERVER,
        criticality=AssetCriticality.HIGH,
    ).to_api() == {
        "asset": "host1",
        "type": "Server",
        "assetCriticality": "High",
    }


def test_file_type_parses_artifacts_and_upload_results():
    artifact = Artifact.from_api(
        {
            "id": "artifact-1",
            "filename": "proof.png",
            "content_type": "image/png",
            "description": "proof",
            "createdAt": 1682615928019,
            "components": ["report_artifacts"],
            "relations": [{"model": "report", "id": 500824}],
            "size": 757,
        }
    )

    assert artifact.artifact_id == "artifact-1"
    assert artifact.content_type == "image/png"
    assert artifact.relations[0].model is ArtifactRelationModel.REPORT
    assert artifact.relations[0].object_id == 500824
    assert ArtifactRelation(model=ArtifactRelationModel.CLIENT, object_id=1045).to_api() == {
        "model": "client",
        "id": "1045",
    }
    upload_result = ArtifactUploadResult.from_api(
        {"status": "ok", "data": {"id": "artifact-2"}}
    )
    assert upload_result.artifact_id == "artifact-2"
    assert TenantImageUploadResult.from_api(
        {"fileUrl": "uploads/image.png"}
    ).file_url == "uploads/image.png"
    assert TenantImageUploadResult.from_api(
        {"data": {"url": "uploads/nested.png"}}
    ).file_url == "uploads/nested.png"


def test_mailer_type_parses_documented_template_fields():
    template = EmailTemplate.from_api(
        {
            "template": "FORGOTTEN_PASSWORD",
            "subject": "Reset your password",
            "body": "<html>Reset</html>",
        }
    )

    assert template.template is EmailTemplateKind.FORGOTTEN_PASSWORD
    assert template.subject == "Reset your password"
    assert template.body == "<html>Reset</html>"


def test_substatus_type_parses_and_serializes_documented_fields():
    parsed = Substatus.from_api(
        {
            "cuid": "substatus-1",
            "tenantCuid": "tenant-1",
            "status": "In Process",
            "value": "In Development",
        }
    )

    assert parsed.cuid == "substatus-1"
    assert parsed.tenant_cuid == "tenant-1"
    assert parsed.status is SubstatusStatus.IN_PROCESS
    assert parsed.value == "In Development"
    assert SubstatusInput(status=SubstatusStatus.CLOSED, value="Accepted").to_api() == {
        "status": "Closed",
        "value": "Accepted",
    }


def test_analytics_filter_serializes_documented_fields():
    payload = AnalyticsFilter(
        client_ids=[1045],
        tags=AnalyticsTags(findings=["pci"], finding_tags_is_union=True),
        statuses=[FindingStatus.OPEN],
        limit=10,
        offset=0,
    ).to_api()

    assert payload == {
        "clients": [1045],
        "tags": {"findings": ["pci"], "findingTagsIsUnion": True},
        "statuses": ["Open"],
        "limit": 10,
        "offset": 0,
    }
    assert FindingAnalyticsBootstrapFilter(
        client_ids=[1045],
        report_ids=[22],
        finding_tags=["pci"],
        order=[FindingAnalyticsBootstrapOrderField.CLIENTS],
        asset_pagination=FindingAnalyticsAssetPagination(
            limit=10,
            offset=0,
            total=25,
            search="host",
        ),
        runbook_ids=["runbook-1"],
        methodology_ids=["methodology-1"],
        engagement_ids=["engagement-1"],
        engagement_tags=["external"],
        tactic_ids=["tactic-1"],
        assignees=["analyst@example.com"],
        asset_ports=["443"],
        operating_systems=["Linux"],
        data_owners=["data-owner"],
        system_owners=["system-owner"],
        physical_locations=["datacenter"],
        cve_ids=["CVE-2026-0001"],
        cwe_ids=["CWE-79"],
    ).to_api() == {
        "clients": [1045],
        "clientTags": [],
        "assetTags": [],
        "reports": [22],
        "reportTags": [],
        "findingTags": ["pci"],
        "order": ["clients"],
        "assetPagination": {
            "limit": 10,
            "offset": 0,
            "total": 25,
            "search": "host",
        },
        "runbooks": ["runbook-1"],
        "methodologies": ["methodology-1"],
        "engagements": ["engagement-1"],
        "engagementTags": ["external"],
        "tactics": ["tactic-1"],
        "assignees": ["analyst@example.com"],
        "assetPorts": ["443"],
        "operatingSystem": ["Linux"],
        "dataOwner": ["data-owner"],
        "systemOwner": ["system-owner"],
        "physicalLocation": ["datacenter"],
        "cveIDs": ["CVE-2026-0001"],
        "cweIDs": ["CWE-79"],
    }
    assert FindingAnalyticsBootstrapFilter().to_api() == {
        "clients": [],
        "clientTags": [],
        "assetTags": [],
        "reports": [],
        "reportTags": [],
        "findingTags": [],
        "order": [
            "reportTags",
            "clients",
            "findingTags",
            "reports",
            "assetTags",
            "assignees",
            "assetPorts",
            "operatingSystem",
            "dataOwner",
            "systemOwner",
            "physicalLocation",
            "cveIDs",
            "cweIDs",
        ],
    }
    assert AssetAnalyticsFilter(
        client_ids=[1045],
        asset_types=["Server"],
        criticality=[AssetCriticality.HIGH],
        data_owner="data-owner",
        physical_location="datacenter",
        system_owner="system-owner",
    ).to_api() == {
        "clients": [1045],
        "criticality": ["High"],
        "type": ["Server"],
        "data_owner": "data-owner",
        "physical_location": "datacenter",
        "system_owner": "system-owner",
    }
    assert AnalyticsTrendFilter(
        client_ids=[1045],
        report_ids=[22],
        finding_severities=[FindingSeverity.HIGH],
    ).to_api() == {
        "clients": [1045],
        "reports": [22],
        "severity": ["High"],
    }
    assert SlaAnalyticsFilter(
        client_ids=[1045],
        report_ids=[22],
        finding_severities=[FindingSeverity.HIGH],
        asset_criticality=[SlaAssetCriticality.UNSPECIFIED],
    ).to_api() == {
        "clients": [1045],
        "reports": [22],
        "findingSeverities": ["High"],
        "clientTags": [],
        "reportTags": [],
        "findingTags": [],
        "assetCriticality": ["Unspecified"],
        "assetTags": [],
        "findingTagsIsUnion": True,
        "assetTagsIsUnion": True,
    }
    assert SlaAnalyticsFilter().to_api() == {
        "clients": [],
        "reports": [],
        "findingSeverities": ["Informational", "Low", "Medium", "High", "Critical"],
        "clientTags": [],
        "reportTags": [],
        "findingTags": [],
        "assetCriticality": [
            "Critical",
            "High",
            "Medium",
            "Low",
            "Informational",
            "Unspecified",
        ],
        "assetTags": [],
        "findingTagsIsUnion": True,
        "assetTagsIsUnion": True,
    }
    assert AnalyticsResult.from_api({"status": "success", "data": {"total": 1}}).data == {
        "total": 1
    }


def test_analytics_records_parse_raw_keys_to_semantic_fields():
    finding_result = AnalyticsResult.from_api(
        {
            "status": "success",
            "data": {
                "total": 1,
                "rows": [
                    {
                        "id": 99,
                        "clientName": "Example Client",
                        "reportName": "External Pentest",
                        "title": "SQL Injection",
                        "severity": {"name": "High", "value": 4},
                        "status": "Open",
                        "lastUpdateAt": "2026-06-20T12:00:00Z",
                        "severities": {"High": 1},
                    }
                ],
            },
        },
        record_kind="finding",
    )

    assert finding_result.total_count == 1
    assert finding_result.records[0].finding_id == 99
    assert finding_result.records[0].client_name == "Example Client"
    assert finding_result.records[0].report_name == "External Pentest"
    assert finding_result.records[0].finding_title == "SQL Injection"
    assert finding_result.records[0].severity is FindingSeverity.HIGH
    assert finding_result.records[0].status is FindingStatus.OPEN
    assert finding_result.records[0].last_update_at == "2026-06-20T12:00:00Z"
    assert finding_result.records[0].severity_counts == {"High": 1}

    asset_record = AnalyticsRecord.from_api(
        {
            "id": "asset-1",
            "name": "host1",
            "clientName": "Example Client",
            "type": "Server",
            "findings": 4,
            "percentage": "25%",
        },
        record_kind="asset",
    )

    assert asset_record.asset_id == "asset-1"
    assert asset_record.asset_name == "host1"
    assert asset_record.finding_title is None
    assert asset_record.client_name == "Example Client"
    assert asset_record.asset_type == "Server"
    assert asset_record.finding_count == 4
    assert asset_record.percentage == "25%"

    report_record = AnalyticsRecord.from_api(
        {"id": 22, "name": "External Pentest", "clientName": "Example Client"},
        record_kind="report",
    )

    assert report_record.report_id == 22
    assert report_record.report_name == "External Pentest"
    assert report_record.finding_title is None


def test_tenant_type_parses_documented_fields():
    parsed = Tenant.from_api(
        {
            "tenant_id": 1,
            "cuid": "tenant-cuid",
            "name": "Example",
            "poc": {"first": "Ada", "last": "Lovelace", "email": "ada@example.com"},
            "settings": {"visibility": "draft", "rapidTemplating": False},
        }
    )

    assert parsed.tenant_id == 1
    assert parsed.point_of_contact.email == "ada@example.com"
    assert parsed.settings.visibility is FindingVisibility.DRAFT
    assert parsed.settings.rapid_templating is False


def test_template_type_parses_and_serializes_documented_fields():
    assert ExportTemplateType.CUSTOM.value == "custom"

    parsed = FindingTemplate.from_api(
        {
            "doc_id": "template-1",
            "template_name": "Finding Template",
            "fields": {"synopsis": {"label": "Synopsis", "value": "<p>Example</p>"}},
        }
    )

    assert parsed.template_id == "template-1"
    assert parsed.fields["synopsis"].label == "Synopsis"
    assert FindingTemplateInput(
        template_name="Finding Template",
        fields={"synopsis": TemplateField(label="Synopsis", value="<p>Example</p>")},
    ).to_api() == {
        "template_name": "Finding Template",
        "fields": {"synopsis": {"label": "Synopsis", "value": "<p>Example</p>"}},
    }


def test_content_library_types_parse_and_serialize_documented_fields():
    assert WriteupImportSource.CSV.value == "csv"
    assert ContentLibraryUserInput(user_id=12, permission_level="EDITOR").to_api() == {
        "userId": 12,
        "permissionLevel": "EDITOR",
    }
    assert NarrativeSectionInput(
        title="Executive Summary",
        repository_id="repo-1",
        section_id="section-1",
        text="<p>Summary</p>",
    ).to_api() == {
        "label": "Executive Summary",
        "id": "section-1",
        "repositoryId": "repo-1",
        "text": "<p>Summary</p>",
    }
    assert NarrativeRepositoryInput(name="Narratives", description="Shared").to_api() == {
        "name": "Narratives",
        "description": "Shared",
    }
    assert WriteupRepositoryInput(name="Default", description="Shared").to_api() == {
        "name": "Default",
        "description": "Shared",
    }
    assert WriteupTransfer(
        writeup_ids=["template_1"],
        source_repository_id="repo-1",
        destination_repository_id="repo-2",
    ).to_api() == {
        "writeups": ["template_1"],
        "destinationRepositoryId": "repo-2",
        "sourceRepositoryId": "repo-1",
    }

    writeup = Writeup.from_api(
        {
            "id": "template_104560",
            "doc_id": 104560,
            "repositoryId": "repo-1",
            "severity": "Critical",
            "title": "Password returned in URL query string",
            "tags": ["web"],
        }
    )
    repository = WriteupRepository.from_api(
        {"id": "repo-1", "name": "Default", "writeups": [writeup.raw]}
    )
    wrapped_repository = WriteupRepository.from_api(
        {
            "data": {
                "repositoryID": "repo-2",
                "title": "Wrapped Repository",
                "writeups": [
                    {
                        "data": {
                            "template_id": "template_2",
                            "docId": 2,
                            "repository_id": "repo-2",
                            "severity": "High",
                            "title": "Wrapped Writeup",
                        }
                    }
                ],
            }
        }
    )
    narrative = NarrativeRepository.from_api(
        {
            "id": "narrative-repo-1",
            "name": "Narratives",
            "sections": [{"id": "section-1", "title": "Executive Summary"}],
        }
    )
    wrapped_narrative = NarrativeRepository.from_api(
        {
            "data": {
                "repositoryID": "narrative-repo-2",
                "title": "Wrapped Narratives",
                "permission_level": "EDITOR",
                "sections": [
                    {
                        "data": {
                            "section_id": "section-2",
                            "repositoryID": "narrative-repo-2",
                            "name": "Wrapped Section",
                        }
                    }
                ],
            }
        }
    )
    user = ContentLibraryUser.from_api({"data": {"id": 12, "email": "ada@example.com"}})

    assert writeup.severity is FindingSeverity.CRITICAL
    assert repository.writeups[0].writeup_id == "template_104560"
    assert wrapped_repository.repository_id == "repo-2"
    assert wrapped_repository.writeups[0].writeup_id == "template_2"
    assert wrapped_repository.writeups[0].doc_id == 2
    assert wrapped_repository.writeups[0].repository_id == "repo-2"
    assert narrative.sections[0].section_id == "section-1"
    assert wrapped_narrative.repository_id == "narrative-repo-2"
    assert wrapped_narrative.permission_level == "EDITOR"
    assert wrapped_narrative.sections[0].section_id == "section-2"
    assert user.email == "ada@example.com"
    assert WriteupDeleteResult.from_api({"message": "success", "doc_id": "template_1"}).ok
    assert WriteupDeleteResult.from_api({"data": {"docId": 0}}).doc_id == 0


def test_runbook_types_parse_and_serialize_graphql_shapes():
    assert RunbookTeam.RED.value == "RED"
    assert RunbookListArgs(limit=10, offset=5, search="repo").to_api() == {
        "limit": 10,
        "offset": 5,
        "search": "repo",
    }
    assert RunbookRecordInput(
        name="Purple Team",
        short_name="PT",
        description="Shared procedures",
        repository_id="repo-1",
    ).to_api() == {
        "name": "Purple Team",
        "shortName": "PT",
        "description": "Shared procedures",
        "repositoryId": "repo-1",
    }
    assert RunbookProcedureLogInput(
        text="Started",
        start_date="2026-06-18T10:00:00Z",
        team=RunbookTeam.RED,
    ).to_api() == {
        "text": "Started",
        "startDate": "2026-06-18T10:00:00Z",
        "team": "RED",
    }

    repository = RunbookRepository.from_api(
        {
            "id": "repo-1",
            "name": "Purple Team",
            "shortName": "PT",
            "tags": [{"id": "tag-1", "tag": "attack"}],
        }
    )
    log = RunbookProcedureLog.from_api(
        {"id": "log-1", "engagementProcedureId": "procedure-1", "text": "Started"}
    )

    assert repository.record_id == "repo-1"
    assert isinstance(repository.tags[0], RunbookTag)
    assert repository.tags[0].tag == "attack"
    assert log.engagement_procedure_id == "procedure-1"
    assert RunbookMutationResult.from_api({"id": "repo-1"}).ok
    assert RunbookUploadResult.from_api({"id": "attachment-1"}).ok


def test_integration_type_serializes_documented_enums():
    assert JiraConnectionInput(
        url="https://jira.example.com",
        username="api@example.com",
        api_token="secret",
        sync_frequency=JiraSyncFrequency.DAILY,
    ).to_api() == {
        "url": "https://jira.example.com",
        "username": "api@example.com",
        "apiToken": "secret",
        "syncFrequency": "Daily",
    }
    assert IntegrationConfigurationInput(
        integration_type=IntegrationConfigurationType.SNYK,
        api_key="secret",
        api_username="api-user",
        org_id="org-1",
    ).to_api() == {
        "integrationType": "Snyk",
        "apiKey": "secret",
        "apiUserName": "api-user",
        "orgId": "org-1",
    }


def test_parser_action_type_serializes_documented_enums():
    assert ParserActionInput(
        id="sql-1",
        severity=FindingSeverity.HIGH,
        title="SQL Injection",
        action=ParserActionType.IGNORE,
    ).to_api() == {
        "id": "sql-1",
        "severity": "High",
        "title": "SQL Injection",
        "action": "IGNORE",
    }
    assert ParserPluginSource.OWASP_ZAP.value == "owaspzap"


def test_scheduler_type_serializes_search_payload():
    assert EngagementScheduleEventSearch(
        filters={"status": "APPROVED"},
        pagination={"offset": 0, "limit": 10},
    ).to_api() == {
        "filters": {"status": "APPROVED"},
        "pagination": {"offset": 0, "limit": 10},
    }


def test_user_type_serializes_documented_fields():
    assert TenantUserInput(
        email="ada@example.com",
        role=DefaultUserRole.ANALYST,
        first_name="Ada",
        last_name="Lovelace",
        default_group=True,
    ).to_api() == {
        "email": "ada@example.com",
        "role": "ANALYST",
        "name": {"first": "Ada", "last": "Lovelace"},
        "default_group": True,
    }
    assert UserFindingSearch(
        filters=[FindingFilter(by=FindingFilterField.STATUS, value=[FindingStatus.OPEN])],
        pagination=FindingPagination(limit=FindingPageLimit.TEN),
        sort=[FindingSort(by=FindingSortField.SEVERITY, order=SortOrder.DESCENDING)],
    ).to_api() == {
        "filters": [{"by": "status", "value": ["Open"]}],
        "pagination": {"offset": 0, "limit": 10},
        "sort": [{"by": "severity", "order": "DESC"}],
    }
    assert CurrentUserUpdate(
        first_name="Ada",
        authentication_provider=AuthenticationProviderName.PLEXTRAC,
    ).to_api() == {
        "name": {"first": "Ada"},
        "authenticationProvider": "plextrac",
    }


def test_admin_type_serializes_documented_sla_and_audit_fields():
    providers = [
        AuthenticationProvider.from_api(value)
        for value in ["plextrac", "okta", "google", "azure", "openid_connect"]
    ]
    configuration = AuthenticationProviderConfiguration.from_api(
        {"enabled": True, "provider": "okta"}
    )

    assert [provider.provider for provider in providers] == [
        AuthenticationProviderName.PLEXTRAC,
        AuthenticationProviderName.OKTA,
        AuthenticationProviderName.GOOGLE,
        AuthenticationProviderName.AZURE,
        AuthenticationProviderName.OPENID_CONNECT,
    ]
    assert configuration.provider is AuthenticationProviderName.OKTA
    saml_configuration = SamlConfiguration.from_api(
        {
            "enabled": True,
            "providerName": "plextrac",
            "issuer": "https://idp.example.com",
            "cert": "certificate-body",
            "idpSSOUrl": "https://idp.example.com/sso",
        }
    )

    assert saml_configuration.certificate == "certificate-body"
    assert saml_configuration.to_api() == {
        "enabled": True,
        "providerName": "plextrac",
        "issuer": "https://idp.example.com",
        "cert": "certificate-body",
        "idpSSOUrl": "https://idp.example.com/sso",
    }
    assert RoleNameAvailability.from_api({"available": True}).available is True

    benchmark = SLABenchmark(
        name="Critical SLA",
        days_to_close=5,
        finding_severity=[FindingSeverity.CRITICAL],
        finding_tags=["nessus_findings"],
        asset_criticality=[AssetCriticality.CRITICAL],
        asset_tags=["internet-facing"],
        enabled=True,
        notification_settings=SLABenchmarkNotificationSettings(
            hours_before_expiration_notify=12,
            recipients=["ada@example.com"],
            send_daily_notification_to_assigned_user=True,
        ),
    )

    assert benchmark.to_api() == {
        "name": "Critical SLA",
        "daysToClose": 5,
        "findingSeverity": ["Critical"],
        "findingTags": ["nessus_findings"],
        "assetCriticality": ["Critical"],
        "assetTags": ["internet-facing"],
        "enabled": True,
        "notificationSettings": {
            "hoursBeforeExpirationNotify": 12,
            "recipients": ["ada@example.com"],
            "sendDailyNotificationToAssignedUser": True,
        },
    }
    assert SLABenchmarkResult.from_api({"id": "sla-1"}).benchmark_id == "sla-1"

    entry = AuditLogEntry.from_api(
        {
            "cuid": "audit-1",
            "user_info": "Ada Test (ada@example.com)",
            "message": "Successful login",
            "event_type": "LoginSuccess",
            "timestamp": "2024-08-08T20:45:24.286Z",
        }
    )

    assert entry.event_type is AuditLogEventType.LOGIN_SUCCESS


def test_assessment_type_serializes_question_and_answer_payloads():
    questionnaire = Questionnaire.from_api(
        {
            "questionnaire_id": 123,
            "assessment_title": "CIS Control 12",
            "questions_count": 5,
        }
    )

    assert questionnaire.questionnaire_id == 123
    assert questionnaire.title == "CIS Control 12"
    assert QuestionnaireInput(title="CIS Control 12", framework_id="cis20").to_api() == {
        "assessment_title": "CIS Control 12",
        "framework_id": "cis20",
    }

    question = QuestionInput(
        title="New Question",
        text="Description of new question.",
        severity=FindingSeverity.HIGH,
        answer_type=[
            QuestionAnswerType(
                key="answer_type_1",
                label="Response",
                value="freeForm",
                required=False,
                multi_choice_answers=[AnswerOption(label="Yes", value="Yes")],
            )
        ],
    )

    assert question.to_api() == {
        "answer_type": [
            {
                "key": "answer_type_1",
                "label": "Response",
                "value": "freeForm",
                "required": False,
                "multi_choice_answers": [{"label": "Yes", "value": "Yes"}],
            }
        ],
        "severity": "High",
        "text": "Description of new question.",
        "title": "New Question",
    }

    answer = AssessmentAnswer(
        question_id="12.6",
        answer=[
            AssessmentAnswerField(
                key="answer_type_1",
                label="Response",
                value=["Operational"],
                required=False,
            )
        ],
        status="completed",
    )

    assert answer.to_api() == {
        "qid": "12.6",
        "answer": [
            {
                "key": "answer_type_1",
                "label": "Response",
                "value": ["Operational"],
                "required": False,
            }
        ],
        "status": "completed",
    }
    parsed_answer = AssessmentAnswer.from_api(
        {"qid": "12.6", "completionRequired": False}
    )

    assert parsed_answer.completion_required is False
    assessment = Assessment.from_api(
        {
            "assess_id": 3151,
            "assessment_title": "CIS Control 12",
            "hasReviewers": False,
            "allApproved": False,
        }
    )

    assert assessment.assessment_id == 3151
    assert assessment.title == "CIS Control 12"
    assert assessment.has_reviewers is False
    assert assessment.all_approved is False


def test_client_assessment_input_serializes_backend_required_defaults():
    assert ClientAssessmentInput(questionnaire_id=7).to_api() == {
        "questionnaire_id": 7,
        "answers": [],
        "saveOnly": True,
    }


def test_assessment_create_result_parses_nested_ids():
    result = AssessmentCreateResult.from_api(
        {
            "status": "success",
            "data": {
                "doc_id": "assessment_3151_tenant_0_client_2",
                "assessment_id": 3151,
            },
        }
    )

    assert result.ok is True
    assert result.document_id == "assessment_3151_tenant_0_client_2"
    assert result.assessment_id == 3151
    live_shape = AssessmentCreateResult.from_api(
        {
            "status": "success",
            "message": "success",
            "doc_id": "assessment_4072_tenant_0_client_66602",
        }
    )

    assert live_shape.assessment_id == "4072"


def test_report_request_shape_types_serialize_with_verified_fields():
    assert ReportPagination(limit=ReportPageLimit.ONE_THOUSAND).to_api() == {
        "offset": 0,
        "limit": 1000,
    }
    assert ReportSort(
        by=ReportSortField.STATUS,
        order=SortOrder.DESCENDING,
    ).to_api() == {"by": "status", "order": "DESC"}
    assert ReportFilter(
        by=ReportFilterField.STATUS,
        value=[ReportStatus.PUBLISHED.value],
    ).to_api() == {
        "by": "status",
        "value": ["Published"],
    }


def test_assessment_sort_order_uses_assessment_wire_values():
    assert AssessmentSortOrder.ASCENDING.value == "ascend"
    assert AssessmentSortOrder.DESCENDING.value == "descend"
    assert TenantAssessmentSort.ALL_DESCENDING.value == "ALL_DESCEND"


def test_finding_request_shape_types_serialize_with_verified_fields():
    assert FindingPagination(limit=FindingPageLimit.FIFTY, offset=10).to_api() == {
        "offset": 10,
        "limit": 50,
    }
    assert FindingSort(
        by=FindingSortField.SEVERITY,
        order=SortOrder.DESCENDING,
    ).to_api() == {"by": "severity", "order": "DESC"}
    assert FindingFilter(
        by=FindingFilterField.STATUS,
        value=[FindingStatus.OPEN],
    ).to_api() == {
        "by": "status",
        "value": ["Open"],
    }
    assert FindingField(
        field_id="field-1",
        key="synopsis",
        label="Synopsis",
        value="Example",
        sort_order=0,
    ).to_api() == {
        "id": "field-1",
        "key": "synopsis",
        "label": "Synopsis",
        "value": "Example",
        "sort_order": 0,
    }
    assert FindingSort(by=FindingSortField.FINDING_ID).to_api() == {
        "by": "flawId",
        "order": "ASC",
    }
    assert FindingFilter(by=FindingFilterField.FINDING_ID, value=99).to_api() == {
        "by": "flaw_id",
        "value": 99,
    }
    assert CodeSample(code_sample_id="cs1", caption="example", code="print(1)").to_api() == {
        "id": "cs1",
        "caption": "example",
        "code": "print(1)",
    }
    assert FindingEvidenceUpdate(
        evidence_id="ev1",
        caption="Evidence",
        code="proof",
        assets=["asset-1"],
    ).to_api() == {
        "id": "ev1",
        "caption": "Evidence",
        "code": "proof",
        "assets": ["asset-1"],
    }


def test_report_type_parses_narratives():
    report = Report.from_api(
        {
            "report_id": 10,
            "cuid": "report-cuid",
            "client_id": 1,
            "name": "Assessment",
            "status": "Draft",
            "exec_summary": {
                "custom_fields": [{"id": "n1", "label": "Executive Summary", "text": "Text"}]
            },
        }
    )

    assert report.report_id == 10
    assert report.cuid == "report-cuid"
    assert report.status is ReportStatus.DRAFT
    assert report.narratives[0].label == "Executive Summary"


def test_finding_type_parses_affected_assets_and_identifiers():
    finding = Finding.from_api(
        {
            "flaw_id": 99,
            "id": "finding-cuid",
            "title": "Example finding",
            "severity": "High",
            "status": "Open",
            "visibility": "published",
            "common_identifiers": {
                "CVE": [{"name": "CVE-2024-0001", "year": 2024, "id": 1}],
                "CWE": [{"name": "CWE-79", "id": 79}],
                "code_samples": [{"id": "cs1", "caption": "example", "code": "print(1)"}],
            },
            "fields": {
                "Synopsis": {"key": "synopsis", "label": "Synopsis", "value": "Example"}
            },
            "affected_assets": {
                "asset-1": {
                    "id": "asset-1",
                    "asset": "host1",
                    "status": "Open",
                    "assignedTo": "analyst@example.com",
                    "comment": "triage note",
                    "vulnerableParameters": [{"id": "p1", "text": "q"}],
                }
            },
        }
    )

    assert finding.finding_id == 99
    assert finding.cuid == "finding-cuid"
    assert finding.severity is FindingSeverity.HIGH
    assert finding.status is FindingStatus.OPEN
    assert finding.visibility is FindingVisibility.PUBLISHED
    assert finding.cves[0].name == "CVE-2024-0001"
    assert finding.code_samples[0].code_sample_id == "cs1"
    assert finding.fields["Synopsis"].key == "synopsis"
    assert isinstance(finding.affected_assets["asset-1"], AffectedAsset)
    assert finding.affected_assets["asset-1"].status is AffectedAssetStatus.OPEN
    assert finding.affected_assets["asset-1"].assigned_to == "analyst@example.com"
    assert finding.affected_assets["asset-1"].comment == "triage note"
    assert finding.affected_assets["asset-1"].vulnerable_parameters[0].text == "q"


def test_finding_import_status_uses_semantic_import_id():
    parsed = FindingImportStatus.from_api(
        {"id": "import-1", "status": "completed", "message": "done"}
    )

    assert parsed.import_id == "import-1"
    assert parsed.status == "completed"


def test_affected_asset_status_update_serializes_documented_fields():
    update = AffectedAssetStatusUpdate(
        asset_id="asset-1",
        status=AffectedAssetStatus.IN_PROCESS,
        substatus="Investigating",
        assigned_to="analyst@example.com",
        comment="triage started",
    )

    assert update.to_api(include_asset_id=True) == {
        "assetId": "asset-1",
        "status": "In Process",
        "subStatus": "Investigating",
        "assignedTo": "analyst@example.com",
        "comment": "triage started",
    }
    bulk_update = AffectedAssetBulkStatusUpdate(
        asset_ids=["asset-1", "asset-2"],
        status=AffectedAssetStatus.IN_PROCESS,
        assigned_to="analyst@example.com",
        substatus="Investigating",
        comment="triage started",
    )

    assert bulk_update.to_api() == {
        "assetIds": ["asset-1", "asset-2"],
        "status": "In Process",
        "assignedTo": "analyst@example.com",
        "subStatus": "Investigating",
        "comment": "triage started",
    }

    status_map = AffectedAssetStatusMap.from_api(
        {"asset-1": {"status": "In Process", "comment": "triage started"}}
    )

    assert status_map["asset-1"].status is AffectedAssetStatus.IN_PROCESS
    assert status_map.get("asset-1") is status_map["asset-1"]
    assert list(status_map.keys()) == ["asset-1"]
