import base64
import json
import time

import httpx
import pytest

from plextrac_api.functions import affected_assets, assets, clients, files, findings, reports
from plextrac_api.functions.auth import session_from_token
from plextrac_api.functions.common import PlexTracAuthError, PlexTracNotFoundError
from plextrac_api.types import (
    AffectedAsset,
    AffectedAssetStatus,
    AffectedAssetStatusUpdate,
    ArtifactRelation,
    ArtifactRelationModel,
    AssetInput,
    AssetType,
    ClientAssetPageLimit,
    ClientAssetSort,
    ClientAssetSortField,
    ClientInput,
    FindingField,
    FindingInput,
    FindingSeverity,
    FindingStatus,
    ReportInput,
    ReportStatus,
    SortOrder,
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
                    id="asset-1",
                    name="host1",
                    status=AffectedAssetStatus.OPEN,
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
        "affected_assets": {"asset-1": {"id": "asset-1", "asset": "host1", "status": "Open"}},
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

    assert statuses["asset-1"].status is AffectedAssetStatus.CLOSED
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
        updates=[
            AffectedAssetStatusUpdate(
                asset_id="asset-1",
                status=AffectedAssetStatus.IN_PROCESS,
                assigned_to="analyst@example.com",
                comment="triaging",
            )
        ],
    )

    assert result.ok
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v2/client/client-1/report/report-1/finding/finding-1/asset/status"
    assert seen["json"] == [
        {
            "assetId": "asset-1",
            "status": "In Process",
            "assignedTo": "analyst@example.com",
            "comment": "triaging",
        }
    ]


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


def test_request_refreshes_before_request_when_token_expires_within_five_minutes(monkeypatch):
    calls = []
    old_token = _jwt_expiring_in(299)

    def fake_send(session, method, path, **kwargs):
        calls.append((method, path, kwargs["headers"].get("Authorization")))
        if path == "/api/v1/token/refresh":
            return httpx.Response(200, json={"token": "new-token"})
        return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", old_token)

    result = clients.delete_client(session, client_id="client-1")

    assert result.ok
    assert session.token == "new-token"
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
