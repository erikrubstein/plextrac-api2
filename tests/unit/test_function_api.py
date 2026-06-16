import httpx
import pytest

from plextrac_api.functions import clients, reports
from plextrac_api.functions.auth import session_from_token
from plextrac_api.functions.common import PlexTracNotFoundError


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

    assert result.id == 123
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


def test_explicit_client_create_uses_named_parameters(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"created": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    clients.create_client(session, name="Example Client")

    assert seen["method"] == "POST"
    assert seen["json"] == {"name": "Example Client"}


def test_explicit_report_create_uses_named_parameters(monkeypatch):
    seen = {}

    def fake_send(session, method, path, **kwargs):
        seen["method"] = method
        seen["path"] = path
        seen["json"] = kwargs["json"]
        return httpx.Response(200, json={"message": "success", "report_id": 42})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    result = reports.create_report(session, client_id="client-1", name="Example Report")

    assert result.id == 42
    assert seen["method"] == "POST"
    assert seen["path"] == "/api/v1/client/client-1/report/create"
    assert seen["json"] == {"name": "Example Report"}


def test_request_maps_http_errors(monkeypatch):
    def fake_send(session, method, path, **kwargs):
        return httpx.Response(404, json={"message": "missing"})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token("https://example.plextrac.com", "test-token")

    with pytest.raises(PlexTracNotFoundError):
        clients.get_client(session, client_id="missing")


def test_request_refreshes_once_after_401(monkeypatch):
    calls = []

    def fake_send(session, method, path, **kwargs):
        calls.append((method, path, kwargs["headers"].get("Authorization")))
        if path == "/api/v1/token/refresh":
            return httpx.Response(200, json={"token": "new-token"})
        if len(calls) == 1:
            return httpx.Response(401, json={"message": "expired"})
        return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr("plextrac_api.functions.common._send", fake_send)
    session = session_from_token(
        "https://example.plextrac.com",
        "old-token",
        refresh_token="refresh-token",
    )

    result = clients.delete_client(session, client_id="client-1")

    assert result.ok
    assert session.token == "new-token"
    assert calls == [
        ("DELETE", "/api/v1/client/client-1", "Bearer old-token"),
        ("PUT", "/api/v1/token/refresh", "Bearer old-token"),
        ("DELETE", "/api/v1/client/client-1", "Bearer new-token"),
    ]
