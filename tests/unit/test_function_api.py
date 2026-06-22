import base64
import json
import time

import httpx
import pytest

from plextrac_api.functions import (
    admin,
    affected_assets,
    analytics,
    assessments,
    assets,
    clients,
    content_library,
    files,
    findings,
    integrations,
    mailer,
    parser_actions,
    reports,
    runbooks,
    scheduler,
    substatus,
    templates,
    tenant,
    users,
)
from plextrac_api.functions.auth import session_from_token
from plextrac_api.functions.common import PlexTracAuthError, PlexTracNotFoundError
from plextrac_api.types import (
    AffectedAsset,
    AffectedAssetBulkStatusUpdate,
    AffectedAssetStatus,
    AffectedAssetStatusMap,
    AnalyticsFilter,
    AnalyticsTags,
    ArtifactRelation,
    ArtifactRelationModel,
    AssessmentAnswer,
    AssessmentAnswerField,
    AssessmentSortOrder,
    AssetAnalyticsFilter,
    AssetCriticality,
    AssetInput,
    AssetType,
    AuditLogEventType,
    AuthenticationProviderName,
    AuthSession,
    ClientAssetPageLimit,
    ClientAssetSort,
    ClientAssetSortField,
    ClientFindingPageLimit,
    ClientFindingPagination,
    ClientInput,
    ContentLibraryUserInput,
    EmailTemplateKind,
    EngagementScheduleEventSearch,
    ExportTemplateType,
    FindingField,
    FindingInput,
    FindingSeverity,
    FindingStatus,
    FindingTemplateInput,
    FindingVisibility,
    JiraConnectionInput,
    JiraSyncFrequency,
    NarrativeSectionInput,
    ParserActionSearchType,
    QuestionAnswerType,
    QuestionInput,
    ReportInput,
    ReportPageLimit,
    ReportPagination,
    ReportStatus,
    RunbookAssetInput,
    RunbookListArgs,
    RunbookRecordInput,
    RunbookUserInput,
    SLABenchmark,
    SLABenchmarkNotificationSettings,
    SortOrder,
    SubstatusInput,
    SubstatusStatus,
    TemplateField,
    UserSortField,
    UserSortOrder,
    WriteupImportSource,
    WriteupInput,
)


def test_explicit_client_function_interpolates_path_params(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["base_url"] = session.base_url
        seen["method"] = method
        seen["path"] = path
        seen["headers"] = kwargs["headers"]
        return httpx.Response(200, json={"client_id": 123, "name": "Example"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = clients.get_client(session, client_id="123")

    assert result.client_id == 123
    assert result.name == "Example"
    assert seen["base_url"] == "https://example.plextrac.com"
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v1/client/123"
    assert seen["headers"]["Authorization"] == "Bearer test-token"


def test_list_clients_and_client_findings_use_distinct_default_pagination(monkeypatch):
    seen = []

    def fake_send(session, method, path, **kwargs):
        seen.append({"method": method, "path": path, "json": kwargs["json"]})
        return httpx.Response(200, json={"data": []})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    clients.list_clients(session)
    clients.list_client_findings(session, client_id="123")

    assert seen == [
        {
            "method": "POST",
            "path": "/api/v2/clients",
            "json": {"pagination": {"offset": 0, "limit": 25}},
        },
        {
            "method": "POST",
            "path": "/api/v2/client/123/findings",
            "json": {"pagination": {"offset": 0, "limit": 10}},
        },
    ]


def test_list_client_findings_accepts_all_client_finding_page_limit(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"data": []})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    clients.list_client_findings(
        session,
        client_id="123",
        pagination=ClientFindingPagination(limit=ClientFindingPageLimit.ALL),
    )

    assert seen["json"] == {"pagination": {"offset": 0, "limit": 99999}}


def test_explicit_content_library_create_section_serializes_input(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "id": "section-1",
                "repositoryId": "repo-1",
                "title": "Executive Summary",
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = content_library.create_narrative_repository_section(
        session,
        NarrativeSectionInput(
            title="Executive Summary",
            repository_id="repo-1",
            text="<p>Summary</p>",
        ),
    )

    assert result.section_id == "section-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/narratives/sections"
    assert seen["json"] == {
        "title": "Executive Summary",
        "repositoryId": "repo-1",
        "text": "<p>Summary</p>",
    }


def test_explicit_content_library_create_writeup_serializes_documented_fields(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "id": "template_104560",
                "doc_id": 104560,
                "repositoryId": "repo-1",
                "severity": "High",
                "title": "Password returned in URL query string",
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = content_library.create_writeup(
        session,
        WriteupInput(
            title="Password returned in URL query string",
            repository_id="repo-1",
            severity=FindingSeverity.HIGH,
            description="Description",
            recommendations="Recommendation",
            tags=["web"],
        ),
    )

    assert result.writeup_id == "template_104560"
    assert result.severity is FindingSeverity.HIGH
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/template/create"
    assert seen["json"] == {
        "title": "Password returned in URL query string",
        "repositoryID": "repo-1",
        "severity": "High",
        "description": "Description",
        "recommendations": "Recommendation",
        "tags": ["web"],
    }


def test_explicit_content_library_repository_users_and_import_use_typed_shapes(
    monkeypatch,
    tmp_path,
):
    seen = {}
    upload_path = tmp_path / "writeups.csv"
    upload_path.write_text("title,severity\nExample,High\n")

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs.get("json")
        seen["files"] = kwargs.get("files")
        if path.endswith("/users"):
            return httpx.Response(200, json={"users": [{"userId": 12, "email": "ada@example.com"}]})
        return httpx.Response(200, json={"status": "success", "importId": "import-1"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    users = content_library.add_writeup_repository_users(
        session,
        repository_id="repo-1",
        users=[ContentLibraryUserInput(user_id=12, permission_level="EDITOR")],
    )

    assert users[0].user_id == 12
    assert seen["json"] == {"users": [{"userId": 12, "permissionLevel": "EDITOR"}]}

    result = content_library.import_writeups_to_repository(
        session,
        upload_path,
        source=WriteupImportSource.CSV,
    )

    assert result.import_id == "import-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/writeups/import/csv"
    assert seen["files"]["file"][0] == "writeups.csv"


def test_explicit_create_runbook_repository_uses_graphql_variables(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "runbookRepositoryCreateV2": {
                        "id": "repo-1",
                        "name": "Purple Team",
                        "shortName": "PT",
                    }
                }
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = runbooks.create_runbook_repository(
        session,
        RunbookRecordInput(
            name="Purple Team",
            short_name="PT",
            description="Shared procedures",
        ),
    )

    assert result.record_id == "repo-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/graphql"
    assert seen["json"]["operationName"] == "RunbookRepositoryCreateV2"
    assert seen["json"]["variables"] == {
        "data": {
            "name": "Purple Team",
            "shortName": "PT",
            "description": "Shared procedures",
        }
    }


def test_explicit_list_runbook_repositories_parses_graphql_items(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "runbookRepositoryListV2": {
                        "items": [{"id": "repo-1", "name": "Default"}]
                    }
                }
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    results = runbooks.list_runbook_repositories(
        session,
        RunbookListArgs(limit=10, offset=5, search="default"),
    )

    assert results[0].record_id == "repo-1"
    assert seen["json"]["operationName"] == "RunbookRepositoryListV2"
    assert seen["json"]["variables"] == {"args": {"limit": 10, "offset": 5, "search": "default"}}


def test_explicit_runbook_update_asset_uses_single_asset_payload(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "runbookEngagementProcedureAssetUpdateV2": {
                        "id": "asset-1",
                        "name": "host1",
                        "hostname": "host1.example.com",
                    }
                }
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = runbooks.update_runbook_engagement_procedure_asset(
        session,
        asset_id="asset-1",
        procedure_id="procedure-1",
        asset=RunbookAssetInput(name="host1", hostname="host1.example.com"),
        evidence_ids=["evidence-1"],
    )

    assert result.asset_id == "asset-1"
    assert seen["json"]["operationName"] == "RunbookEngagementProcedureAssetUpdateV2"
    assert seen["json"]["variables"] == {
        "id": "asset-1",
        "procedureId": "procedure-1",
        "clientAsset": {"name": "host1", "hostname": "host1.example.com"},
        "evidences": [{"id": "evidence-1"}],
    }
    assert "input" not in seen["json"]["variables"]


def test_explicit_runbook_update_repository_user_serializes_user_input(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "runbookRepositoryUserUpdateV2": {
                        "id": "user-1",
                        "userId": "user-1",
                        "role": "operator",
                    }
                }
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = runbooks.update_runbook_repository_user(
        session,
        repository_id="repo-1",
        user_id="user-1",
        user=RunbookUserInput(user_id="user-1", role="operator"),
    )

    assert result.user_id == "user-1"
    assert seen["json"]["operationName"] == "RunbookRepositoryUserUpdateV2"
    assert seen["json"]["variables"] == {
        "repositoryId": "repo-1",
        "userId": "user-1",
        "data": {"userId": "user-1", "role": "operator"},
    }


def test_explicit_runbook_attachment_upload_uses_rest_endpoint(monkeypatch, tmp_path):
    seen = {}
    upload_path = tmp_path / "evidence.txt"
    upload_path.write_text("proof")

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["files"] = kwargs["files"]
        return httpx.Response(
            200,
            json={"id": "attachment-1", "filename": "evidence.txt", "status": "success"},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = runbooks.upload_runbook_engagement_procedure_attachment(
        session,
        engagement_procedure_id="procedure-1",
        file=upload_path,
    )

    assert result.ok
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/runbooks/engagement-procedures/procedure-1/attachments/upload"
    assert seen["files"]["file"][0] == "evidence.txt"


def test_explicit_report_export_uses_snake_case_query_options(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["path"] = path
        seen["params"] = kwargs["params"]
        return httpx.Response(200, content=b"%PDF")

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    reports.export_report_to_pdf(
        session,
        client_id="client-1",
        report_id="report-1",
        include_evidence=True,
    )

    assert seen["path"] == "/api/v1/client/client-1/report/report-1/export/pdf"
    assert seen["params"] == {"includeEvidence": True}


def test_explicit_client_create_uses_reusable_input(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"created": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    clients.create_client(session, ClientInput(name="Example Client"))

    assert seen["method"] == "POST"
    assert seen["json"] == {"name": "Example Client"}


def test_explicit_asset_create_uses_reusable_input(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success", "id": "asset-1"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = assets.create_asset(
        session,
        client_id="client-1",
        asset=AssetInput(name="host1", type=AssetType.SERVER, tags=["external"]),
    )

    assert result.asset_id == "asset-1"
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v1/client/client-1/asset/0"
    assert seen["json"] == {"asset": "host1", "type": "Server", "tags": ["external"]}


def test_explicit_client_asset_list_uses_assets_group_v2_endpoint(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"data": [{"id": "asset-1", "asset": "host1"}], "total": 1},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    page = assets.list_client_assets(
        session,
        client_id="client-1",
        limit=ClientAssetPageLimit.FIFTY,
        sort=[ClientAssetSort(by=ClientAssetSortField.ASSET, order=SortOrder.ASCENDING)],
    )

    assert page.total_count == 1
    assert page.assets[0].name == "host1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/clients/client-1/assets"
    assert seen["json"] == {
        "pagination": {"offset": 0, "limit": 50},
        "sort": [{"by": "asset", "order": "ASC"}],
    }

    assets.list_client_assets(
        session,
        client_id="client-1",
        limit=ClientAssetPageLimit.ONE_THOUSAND,
    )

    assert seen["json"] == {"pagination": {"offset": 0, "limit": 1000}}


def test_explicit_report_create_uses_reusable_input(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"message": "success", "report_id": 42})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = reports.create_report(
        session,
        client_id="client-1",
        report=ReportInput(name="Example Report", status=ReportStatus.DRAFT),
    )

    assert result.report_id == 42
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/client/client-1/report/create"
    assert seen["json"] == {"name": "Example Report", "status": "Draft"}


def test_explicit_report_list_uses_live_pagination_limits(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"data": [], "total": 0})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    reports.list_reports(
        session,
        pagination=ReportPagination(limit=ReportPageLimit.ONE_THOUSAND),
    )

    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/reports"
    assert seen["json"] == {"pagination": {"offset": 0, "limit": 1000}}


def test_explicit_report_replace_returns_replace_result(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success", "data": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = reports.replace_report_text(session, report_id=42, search="old", replace="new")

    assert result.replaced is True
    assert result.status == "success"
    assert seen["json"] == {"search": "old", "replace": "new", "report_id": 42}


def test_explicit_finding_create_uses_reusable_input_and_enums(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success", "flaw_id": 99})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = findings.create_finding(
        session,
        client_id="client-1",
        report_id="report-1",
        finding=FindingInput(
            title="Example Finding",
            severity=FindingSeverity.HIGH,
            status=FindingStatus.OPEN,
            description="Example description",
            affected_assets={
                "asset-1": AffectedAsset(
                    asset_id="asset-1",
                    name="host1",
                    status=AffectedAssetStatus.OPEN,
                    assigned_to="analyst@example.com",
                    comment="triage note",
                )
            },
            fields=[FindingField(key="synopsis", label="Synopsis", value="Example")],
        ),
    )

    assert result.status == "success"
    assert result.flaw_id == 99
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/client/client-1/report/report-1/flaw/create"
    assert seen["json"] == {
        "title": "Example Finding",
        "severity": "High",
        "status": "Open",
        "description": "Example description",
        "affected_assets": {
            "asset-1": {
                "id": "asset-1",
                "asset": "host1",
                "status": "Open",
                "assignedTo": "analyst@example.com",
                "comment": "triage note",
            }
        },
        "fields": [{"key": "synopsis", "label": "Synopsis", "value": "Example"}],
    }


def test_explicit_affected_asset_bulk_statuses_return_typed_map(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"asset-1": {"status": "Closed", "comment": "fixed"}},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    statuses = affected_assets.bulk_get_affected_asset_statuses(
        session,
        client_id="client-1",
        report_id="report-1",
        finding_id="finding-1",
        asset_ids=["asset-1"],
    )

    assert isinstance(statuses, AffectedAssetStatusMap)
    assert statuses["asset-1"].status is AffectedAssetStatus.CLOSED
    assert statuses.get("asset-1") is statuses["asset-1"]
    assert len(statuses) == 1
    assert statuses["asset-1"].comment == "fixed"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/client/client-1/report/report-1/flaw/finding-1/assets/status"
    assert seen["json"] == {"assetIds": ["asset-1"]}


def test_explicit_affected_asset_bulk_create_statuses_uses_reusable_update(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = affected_assets.bulk_create_affected_asset_status_updates(
        session,
        client_id="client-1",
        report_id="report-1",
        finding_id="finding-1",
        update=AffectedAssetBulkStatusUpdate(
            asset_ids=["asset-1"],
            status=AffectedAssetStatus.IN_PROCESS,
            assigned_to="analyst@example.com",
            comment="triaging",
        ),
    )

    assert result.ok
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/client/client-1/report/report-1/finding/finding-1/asset/status"
    assert seen["json"] == {
        "assetIds": ["asset-1"],
        "status": "In Process",
        "assignedTo": "analyst@example.com",
        "comment": "triaging",
    }


def test_explicit_files_list_artifacts_uses_typed_relations(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "status": "ok",
                "data": [
                    {
                        "id": "artifact-1",
                        "filename": "proof.png",
                        "content_type": "image/png",
                    }
                ],
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    artifacts = files.list_artifacts(
        session,
        components=["report_artifacts"],
        relations=[ArtifactRelation(model=ArtifactRelationModel.REPORT, id=42)],
    )

    assert artifacts[0].artifact_id == "artifact-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/file-manager/artifacts"
    assert seen["json"] == {
        "components": ["report_artifacts"],
        "relations": [{"model": "report", "id": 42}],
    }


def test_explicit_files_list_artifacts_requires_relation_filter():
    session = session_from_token("https://example.plextrac.com", "test-token")

    with pytest.raises(ValueError, match="relation filter"):
        files.list_artifacts(session)


def test_explicit_files_upload_artifact_uses_documented_form_fields(monkeypatch, tmp_path):
    seen = {}
    artifact_path = tmp_path / "proof.txt"
    artifact_path.write_text("proof", encoding="utf-8")

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["data"] = kwargs["data"]
        seen["files"] = kwargs["files"]
        return httpx.Response(200, json={"status": "ok", "data": {"id": "artifact-1"}})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = files.upload_artifact(
        session,
        artifact_path,
        description="proof file",
        components=["report_artifacts"],
        relations=[ArtifactRelation(model=ArtifactRelationModel.CLIENT, id=123)],
        content_type="text/plain",
    )

    assert result.artifact_id == "artifact-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/file-manager/upload"
    assert seen["data"] == {
        "description": "proof file",
        "components": "[\"report_artifacts\"]",
        "relations": "[{\"model\": \"client\", \"id\": 123}]",
    }
    assert seen["files"]["file"][0] == "proof.txt"
    assert seen["files"]["file"][2] == "text/plain"


def test_explicit_files_get_upload_uses_session_cookie(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["headers"] = kwargs["headers"]
        return httpx.Response(200, content=b"image-bytes")

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token(
        "https://example.plextrac.com",
        "test-token",
        cookie="upload-cookie",
    )

    result = files.get_upload_by_name(session, "logo.png")

    assert result == b"image-bytes"
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v1/uploads/logo.png"
    assert seen["headers"] == {"Cookie": "token=upload-cookie"}


def test_explicit_files_get_upload_requires_session_cookie():
    session = session_from_token("https://example.plextrac.com", "test-token")

    with pytest.raises(ValueError, match="upload cookie"):
        files.get_upload_by_name(session, "logo.png")


def test_explicit_mailer_upsert_template_uses_template_enum(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = mailer.upsert_email_template(
        session,
        tenant_id=1,
        template=EmailTemplateKind.FORGOTTEN_PASSWORD,
        subject="Reset",
        body="<html>Reset</html>",
    )

    assert result.ok
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v2/tenants/1/mailer/templates/FORGOTTEN_PASSWORD"
    assert seen["json"] == {"body": "<html>Reset</html>", "subject": "Reset"}


def test_explicit_substatus_create_uses_reusable_input(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "cuid": "substatus-1",
                    "tenantCuid": "tenant-1",
                    "status": "Open",
                    "value": "Ready",
                }
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = substatus.create_substatus(
        session,
        SubstatusInput(status=SubstatusStatus.OPEN, value="Ready"),
    )

    assert result.cuid == "substatus-1"
    assert result.status is SubstatusStatus.OPEN
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v3/substatus"
    assert seen["json"] == {"status": "Open", "value": "Ready"}


def test_explicit_analytics_findings_uses_filter_type(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "status": "success",
                "data": {
                    "total": 1,
                    "rows": [{"id": 99, "clientName": "Example", "reportName": "Report"}],
                },
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = analytics.retrieve_analytics_findings(
        session,
        AnalyticsFilter(
            client_ids=[1045],
            tags=AnalyticsTags(findings=["pci"]),
            statuses=[FindingStatus.OPEN],
            limit=10,
            offset=0,
        ),
    )

    assert result.status == "success"
    assert result.records[0].finding_id == 99
    assert result.records[0].client_name == "Example"
    assert result.records[0].report_name == "Report"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/clients/analytics/findings"
    assert seen["json"] == {
        "clients": [1045],
        "tags": {"findings": ["pci"]},
        "statuses": ["Open"],
        "limit": 10,
        "offset": 0,
    }


def test_explicit_analytics_assets_with_filter_uses_documented_default_pagination(
    monkeypatch,
):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["params"] = kwargs["params"]
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"data": []})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = analytics.retrieve_analytics_assets_with_filter(
        session,
        AssetAnalyticsFilter(client_ids=[1045]),
    )

    assert result.records == []
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/clients/analytics/assets"
    assert seen["params"] == {"limit": 10, "offset": 0}
    assert seen["json"] == {"clients": [1045]}


def test_live_unavailable_analytics_age_of_open_findings_is_not_exposed():
    assert not hasattr(analytics, "retrieve_analytics_trends_age_of_open_findings")


def test_explicit_tenant_settings_uses_named_parameters(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = tenant.update_settings(
        session,
        tenant_id=1,
        visibility=FindingVisibility.PUBLISHED,
        sender_email_address="reports@example.com",
    )

    assert result.ok
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v2/tenants/1/settings"
    assert seen["json"] == {
        "visibility": "published",
        "senderEmailAddress": "reports@example.com",
    }


def test_explicit_template_create_finding_template_uses_input_type(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"status": "success", "message": "template saved successfully", "doc_id": "tpl-1"},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = templates.create_finding_template(
        session,
        tenant_id=1,
        template=FindingTemplateInput(
            template_name="Finding Template",
            fields={"synopsis": TemplateField(label="Synopsis", value="<p>Example</p>")},
        ),
    )

    assert result.template_id == "tpl-1"
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v1/tenant/1/field-template"
    assert seen["json"] == {
        "template_name": "Finding Template",
        "fields": {"synopsis": {"label": "Synopsis", "value": "<p>Example</p>"}},
    }


def test_explicit_template_import_uses_named_template_type(monkeypatch, tmp_path):
    seen = {}
    template_path = tmp_path / "export.docx"
    template_path.write_bytes(b"docx")

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["params"] = kwargs["params"]
        seen["files"] = kwargs["files"]
        return httpx.Response(200, json={"status": "success", "doc_id": "tpl-1"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = templates.import_export_template(
        session,
        tenant_id=1,
        file=template_path,
        name="Export Template",
        template_type=ExportTemplateType.CUSTOM,
    )

    assert result.template_id == "tpl-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/tenant/1/template/import"
    assert seen["params"] == {"name": "Export Template", "type": "custom"}
    assert seen["files"]["file"][0] == "export.docx"


def test_explicit_integration_create_jira_connection_uses_enum(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"integrationId": "jira-1", "syncFrequency": "Hourly"},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = integrations.create_jira_connection(
        session,
        JiraConnectionInput(
            url="https://jira.example.com",
            username="api@example.com",
            api_token="secret",
            sync_frequency=JiraSyncFrequency.HOURLY,
        ),
    )

    assert result.integration_id == "jira-1"
    assert result.sync_frequency is JiraSyncFrequency.HOURLY
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/jira/connect"
    assert seen["json"] == {
        "url": "https://jira.example.com",
        "username": "api@example.com",
        "apiToken": "secret",
        "syncFrequency": "Hourly",
    }


def test_explicit_parser_action_list_uses_named_action_type(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["params"] = kwargs["params"]
        return httpx.Response(200, json=[{"id": "sql-1", "action": "IGNORE"}])

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    actions = parser_actions.list_tenant_parser_actions(
        session,
        tenant_id=1,
        parser_name="nessus",
        action_type=ParserActionSearchType.IGNORE,
        query="sql",
    )

    assert actions[0].id == "sql-1"
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v1/tenant/1/actions/nessus"
    assert seen["params"] == {"limit": 985, "skip": 0, "type": "IGNORE", "query": "sql"}


def test_explicit_scheduler_search_uses_search_type(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"data": [{"cuid": "event-1", "name": "Assessment"}], "total": 1},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    page = scheduler.search_engagement_schedule_events(
        session,
        EngagementScheduleEventSearch(
            filters={"status": "APPROVED"},
            pagination={"offset": 0, "limit": 10},
        ),
    )

    assert page.total_count == 1
    assert page.events[0].cuid == "event-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/engagement-schedule-events/search"
    assert seen["json"] == {
        "filters": {"status": "APPROVED"},
        "pagination": {"offset": 0, "limit": 10},
    }


def test_explicit_users_paginated_list_uses_search_name(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["params"] = kwargs["params"]
        return httpx.Response(
            200,
            json={"data": [{"id": "user-1", "email": "ada@example.com"}], "total": 1},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    page = users.list_tenant_users_paginated(
        session,
        tenant_id=1,
        sort_by=UserSortField.EMAIL,
        order=UserSortOrder.ASCENDING,
        search="ada",
    )

    assert page.total_count == 1
    assert page.users[0].email == "ada@example.com"
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v2/tenants/1/users"
    assert seen["params"] == {
        "offset": 0,
        "limit": 10,
        "sortBy": "email",
        "order": "ASCEND",
        "filter": "ada",
    }


def test_explicit_admin_updates_provider_configuration(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = admin.update_tenant_authentication_provider_configuration(
        session,
        tenant_id=1,
        enabled=True,
        provider=AuthenticationProviderName.OKTA,
        uri="https://dev.okta.com",
        provider_client_id="client-id",
        provider_client_secret="secret",
        auth_server_id="default",
    )

    assert result.ok
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/tenants/1/providers/plextrac"
    assert seen["json"] == {
        "enabled": True,
        "provider": "okta",
        "uri": "https://dev.okta.com",
        "providerClientId": "client-id",
        "providerClientSecret": "secret",
        "authServerId": "default",
    }


def test_explicit_admin_updates_user_authentication_method_uses_refined_names(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = admin.update_tenant_user_authentication_method(
        session,
        tenant_id=1,
        user_id="user-1",
        authentication_provider=AuthenticationProviderName.OKTA,
        mfa_enabled=True,
        mfa_qr_code="qr-code",
        mfa_secret="secret",
        mfa_url="otpauth://example",
    )

    assert result.ok
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v2/authenticate/tenants/1/users/user-1/configuration"
    assert seen["json"] == {
        "authentication_provider": "okta",
        "mfa": {
            "enabled": True,
            "qrcode": "qr-code",
            "secret": "secret",
            "url": "otpauth://example",
        },
    }


def test_explicit_admin_lists_security_roles_from_data_wrapper(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        return httpx.Response(
            200,
            json={
                "status": "success",
                "data": [
                    {
                        "id": "role-1",
                        "key": "ADMIN",
                        "title": "Administrator",
                        "permissions": ["ADMINISTRATION.ADMINISTRATION_ACCESS"],
                    }
                ],
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    roles = admin.list_security_roles(session, tenant_id=1)

    assert roles[0].role_id == "role-1"
    assert roles[0].permissions == ["ADMINISTRATION.ADMINISTRATION_ACCESS"]
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v2/tenants/1/security/role"


def test_explicit_admin_checks_security_role_name_availability_with_role_key(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"available": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = admin.check_security_role_name_availability(
        session,
        tenant_id=1,
        role_key="TENANT_1_ROLE_TEST",
    )

    assert result.available is True
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/tenants/1/security/role/availability"
    assert seen["json"] == {"key": "TENANT_1_ROLE_TEST"}


def test_explicit_admin_tenant_tag_operations_handle_live_response_shapes(monkeypatch):
    seen = []

    def fake_send(session, method, path, **kwargs):
        seen.append({
            "method": method,
            "path": path,
            "json": kwargs.get("json"),
            "params": kwargs.get("params"),
        })
        return httpx.Response(200, json=[])

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    create_result = admin.create_tenant_tag(session, tenant_id=1, name="codex-temp")
    delete_result = admin.delete_tenant_tag(session, tenant_id=1, tag_id="tag-1")

    assert create_result.ok
    assert delete_result.ok
    assert seen == [
        {
            "method": "POST",
            "path": "/api/v1/tenant/1/tag",
            "json": {"name": "codex-temp", "scope": "tenant", "ownerId": 1},
            "params": None,
        },
        {
            "method": "DELETE",
            "path": "/api/v1/tenant/1/tag/tag-1",
            "json": None,
            "params": None,
        },
    ]


def test_explicit_admin_get_tenant_tag_by_name_raises_not_found_for_empty_list(
    monkeypatch,
):
    def fake_send(session, method, path, **kwargs):
        return httpx.Response(200, json=[])

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    with pytest.raises(PlexTracNotFoundError):
        admin.get_tenant_tag_by_name(session, tenant_id=1, name="missing")


def test_explicit_admin_get_tenant_tag_by_name_raises_not_found_for_no_content(
    monkeypatch,
):
    def fake_send(session, method, path, **kwargs):
        return httpx.Response(204)

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    with pytest.raises(PlexTracNotFoundError):
        admin.get_tenant_tag_by_name(session, tenant_id=1, name="missing")


def test_explicit_admin_creates_sla_benchmark(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "status": "success",
                "data": {
                    "id": "sla-1",
                    "name": "Critical SLA",
                    "daysToClose": 5,
                    "findingSeverity": ["Critical"],
                    "enabled": True,
                },
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    benchmark = admin.create_sla_benchmark(
        session,
        SLABenchmark(
            name="Critical SLA",
            days_to_close=5,
            finding_severity=[FindingSeverity.CRITICAL],
            asset_criticality=[AssetCriticality.CRITICAL],
            enabled=True,
            notification_settings=SLABenchmarkNotificationSettings(
                hours_before_expiration_notify=12,
                recipients=["ada@example.com"],
            ),
        ),
    )

    assert benchmark.benchmark_id == "sla-1"
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/sla/benchmarks"
    assert seen["json"] == {
        "name": "Critical SLA",
        "daysToClose": 5,
        "findingSeverity": ["Critical"],
        "assetCriticality": ["Critical"],
        "enabled": True,
        "notificationSettings": {
            "hoursBeforeExpirationNotify": 12,
            "recipients": ["ada@example.com"],
        },
    }


def test_explicit_admin_get_sla_benchmark_preserves_requested_id_when_response_omits_it(
    monkeypatch,
):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        return httpx.Response(
            200,
            json={
                "name": "Critical SLA",
                "daysToClose": 5,
                "findingSeverity": ["Critical"],
                "enabled": True,
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    benchmark = admin.get_sla_benchmark(session, benchmark_id="sla-1")

    assert benchmark.benchmark_id == "sla-1"
    assert benchmark.raw == {
        "name": "Critical SLA",
        "daysToClose": 5,
        "findingSeverity": ["Critical"],
        "enabled": True,
    }
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v2/sla/benchmarks/sla-1"


def test_explicit_admin_updates_sla_benchmark_with_benchmark_id(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"status": "success", "id": "sla-1"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = admin.update_sla_benchmark(
        session,
        benchmark_id="sla-1",
        benchmark=SLABenchmark(
            name="Critical SLA",
            days_to_close=5,
            finding_severity=[FindingSeverity.CRITICAL],
            enabled=True,
        ),
    )

    assert result.benchmark_id == "sla-1"
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v2/sla/benchmarks/sla-1"
    assert seen["json"] == {
        "name": "Critical SLA",
        "daysToClose": 5,
        "findingSeverity": ["Critical"],
        "enabled": True,
    }


def test_explicit_admin_lists_audit_log_entries(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["params"] = kwargs["params"]
        return httpx.Response(
            200,
            json={
                "data": [
                    {
                        "cuid": "audit-1",
                        "user_info": "Ada Test (ada@example.com)",
                        "message": "Successful login",
                        "event_type": "LoginSuccess",
                        "timestamp": "2024-08-08T20:45:24.286Z",
                    }
                ]
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    entries = admin.list_audit_log_entries(session, limit=5, offset=10)

    assert entries[0].event_type is AuditLogEventType.LOGIN_SUCCESS
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v2/auditlog"
    assert seen["params"] == {"limit": 5, "offset": 10}


def test_explicit_assessment_create_question_uses_question_type(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={
                "status": "success",
                "data": {
                    "qid": "q-1",
                    "title": "New Question",
                    "text": "Question text",
                    "severity": "High",
                },
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    question = assessments.create_question(
        session,
        questionnaire_id=123,
        question=QuestionInput(
            title="New Question",
            text="Question text",
            severity=FindingSeverity.HIGH,
            answer_type=[
                QuestionAnswerType(
                    key="answer_type_1",
                    label="Response",
                    value="freeForm",
                    required=False,
                )
            ],
        ),
    )

    assert question.question_id == "q-1"
    assert question.severity is FindingSeverity.HIGH
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/assessments/questionnaires/123/questions"
    assert seen["json"] == {
        "answer_type": [
            {
                "key": "answer_type_1",
                "label": "Response",
                "value": "freeForm",
                "required": False,
            }
        ],
        "severity": "High",
        "text": "Question text",
        "title": "New Question",
    }


def test_explicit_assessment_list_client_assessments_uses_latest_endpoint(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["params"] = kwargs["params"]
        return httpx.Response(
            200,
            json={
                "assessments": [
                    {
                        "assess_id": 3151,
                        "assessment_title": "CIS Control 12",
                        "client_id": 4155,
                    }
                ]
            },
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    results = assessments.list_client_assessments(session, tenant_id=1, client_id=2)

    assert results[0].assessment_id == 3151
    assert seen["method"] == "GET"
    assert seen["path"] == "/api/v2/tenants/1/clients/2/assessments"
    assert seen["params"] == {"limit": 10, "offset": 0, "order": "ascend", "sort": 0}

    assessments.list_client_assessments(
        session,
        tenant_id=1,
        client_id=2,
        order=AssessmentSortOrder.DESCENDING,
    )

    assert seen["params"] == {"limit": 10, "offset": 0, "order": "descend", "sort": 0}


def test_explicit_assessment_update_answers_serializes_answers(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"assess_id": 3151, "assessment_title": "CIS Control 12"},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = assessments.update_assessment_answers(
        session,
        tenant_id=1,
        client_id=2,
        assessment_id=3,
        answers=[
            AssessmentAnswer(
                question_id="12.6",
                title="CIS 12.6",
                answer=[
                    AssessmentAnswerField(
                        key="answer_type_1",
                        label="Response",
                        value=["Operational"],
                        required=False,
                    )
                ],
                note="adding a note",
                status="completed",
            )
        ],
    )

    assert result.assessment_id == 3151
    assert seen["method"] == "PUT"
    assert seen["path"] == "/api/v2/tenants/1/clients/2/assessments/3/answers"
    assert seen["json"] == {
        "answers": [
            {
                "qid": "12.6",
                "title": "CIS 12.6",
                "answer": [
                    {
                        "key": "answer_type_1",
                        "label": "Response",
                        "value": ["Operational"],
                        "required": False,
                    }
                ],
                "note": "adding a note",
                "status": "completed",
            }
        ]
    }


def test_explicit_finding_list_uses_latest_paginated_endpoint(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(
            200,
            json={"data": [{"flaw_id": 99, "title": "Example", "severity": "Low"}], "total": 1},
        )

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    page = findings.list_report_findings(session, client_id="client-1", report_id="report-1")

    assert page.total_count == 1
    assert page.findings[0].severity is FindingSeverity.LOW
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/clients/client-1/reports/report-1/findings"
    assert seen["json"] == {"pagination": {"offset": 0, "limit": 10}}


def test_request_maps_http_errors(monkeypatch):
    def fake_send(session, method, path, **kwargs):
        return httpx.Response(404, json={"message": "missing"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    with pytest.raises(PlexTracNotFoundError):
        clients.get_client(session, client_id="missing")


def test_auth_session_preserves_upload_cookie_from_auth_response():
    session = AuthSession.from_auth_response(
        {"token": "test-token", "cookie": "upload-cookie"},
        base_url="https://example.plextrac.com",
        username="person@example.com",
    )

    assert session.cookie == "upload-cookie"
    assert session.to_dict()["cookie"] == "upload-cookie"
    assert AuthSession.from_dict(session.to_dict()).cookie == "upload-cookie"


def test_request_refreshes_before_request_when_token_expires_within_five_minutes(monkeypatch):
    calls = []
    old_token = _jwt_expiring_in(299)

    def fake_send(session, method, path, **kwargs):
        calls.append((method, path, kwargs["headers"].get("Authorization")))
        if path == "/api/v1/token/refresh":
            return httpx.Response(200, json={"token": "new-token", "cookie": "new-cookie"})
        return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", old_token)

    result = clients.delete_client(session, client_id="client-1")

    assert result.ok
    assert session.token == "new-token"
    assert session.cookie == "new-cookie"
    assert calls == [
        ("PUT", "/api/v1/token/refresh", f"Bearer {old_token}"),
        ("DELETE", "/api/v1/client/client-1", "Bearer new-token"),
    ]


def test_request_does_not_refresh_after_401_when_expiration_is_known(monkeypatch):
    calls = []
    token = _jwt_expiring_in(600)

    def fake_send(session, method, path, **kwargs):
        calls.append((method, path, kwargs["headers"].get("Authorization")))
        return httpx.Response(401, json={"message": "unauthorized"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", token)

    with pytest.raises(PlexTracAuthError):
        clients.delete_client(session, client_id="client-1")

    assert calls == [("DELETE", "/api/v1/client/client-1", f"Bearer {token}")]


def test_request_rejects_locally_expired_token(monkeypatch):
    calls = []

    def fake_send(session, method, path, **kwargs):
        calls.append((method, path))
        return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", _jwt_expiring_in(-1))

    with pytest.raises(PlexTracAuthError):
        clients.delete_client(session, client_id="client-1")

    assert calls == []


def test_request_uses_401_refresh_fallback_only_when_expiration_is_unknown(monkeypatch):
    calls = []

    def fake_send(session, method, path, **kwargs):
        calls.append((method, path, kwargs["headers"].get("Authorization")))
        if path == "/api/v1/token/refresh":
            return httpx.Response(200, json={"token": "new-token"})
        if len(calls) == 1:
            return httpx.Response(401, json={"message": "unauthorized"})
        return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "opaque-token")

    result = clients.delete_client(session, client_id="client-1")

    assert result.ok
    assert calls == [
        ("DELETE", "/api/v1/client/client-1", "Bearer opaque-token"),
        ("PUT", "/api/v1/token/refresh", "Bearer opaque-token"),
        ("DELETE", "/api/v1/client/client-1", "Bearer new-token"),
    ]


def _jwt_expiring_in(seconds: int) -> str:
    header = _base64_json({"alg": "none", "typ": "JWT"})
    payload = _base64_json({"exp": int(time.time()) + seconds})
    return f"{header}.{payload}.signature"


def _base64_json(data: dict[str, object]) -> str:
    encoded = base64.urlsafe_b64encode(json.dumps(data).encode()).decode()
    return encoded.rstrip("=")
