from plextrac_api.generated.endpoints import GROUPS
from plextrac_api.types import AffectedAsset, Client, Filter, Finding, Pagination, Report, Sort


def test_generated_registry_covers_public_snapshot():
    total = sum(len(group["endpoints"]) for group in GROUPS.values())

    assert total == 357
    assert "clients" in GROUPS
    assert "reports" in GROUPS
    assert "findings" in GROUPS
    assert "runbooks" in GROUPS


def test_generated_registry_exposes_canonical_latest_names():
    method_names = [
        endpoint["method_name"]
        for group in GROUPS.values()
        for endpoint in group["endpoints"]
    ]

    assert "get_authenticated_user" in method_names
    assert "get_authenticated_user_v1" not in method_names
    assert "get_authenticated_user_v2" not in method_names
    assert "runbook_engagement_list" in method_names
    assert "list_available_tenant_users" in method_names
    assert "available_tenant_users" not in method_names
    assert "assign_users_to_client" in method_names
    assert "assign_user_to_client" not in method_names
    assert "remove_users_from_client" in method_names
    assert "remove_user_from_client" not in method_names
    assert all(not name.endswith(("_v1", "_v2", "_v3")) for name in method_names)


def test_client_type_parses_documented_fields():
    client = Client.from_api(
        {
            "client_id": 1,
            "tenant_id": 2,
            "name": "Example",
            "poc": "Alice",
            "poc_email": "alice@example.com",
            "custom_field": [{"label": "Region", "value": "North"}],
            "users": {"user@example.com": {"role": "ADMIN", "classificationId": "abc"}},
        }
    )

    assert client.id == 1
    assert client.name == "Example"
    assert client.custom_fields[0].label == "Region"
    assert client.users["user@example.com"].role == "ADMIN"


def test_common_request_shape_types_serialize_for_clients():
    assert Pagination(limit=50, offset=25).to_api() == {"offset": 25, "limit": 50}
    assert Sort(by="name", order="DESC").to_api() == {"by": "name", "order": "DESC"}
    assert Filter(by="tags", value=["external"]).to_api() == {"by": "tags", "value": ["external"]}


def test_report_type_parses_narratives():
    report = Report.from_api(
        {
            "report_id": 10,
            "client_id": 1,
            "name": "Assessment",
            "status": "Draft",
            "exec_summary": {
                "custom_fields": [{"id": "n1", "label": "Executive Summary", "text": "Text"}]
            },
        }
    )

    assert report.id == 10
    assert report.narratives[0].label == "Executive Summary"


def test_finding_type_parses_affected_assets_and_identifiers():
    finding = Finding.from_api(
        {
            "flaw_id": 99,
            "title": "Example finding",
            "severity": "High",
            "status": "Open",
            "common_identifiers": {
                "CVE": [{"name": "CVE-2024-0001", "year": 2024, "id": 1}],
                "CWE": [{"name": "CWE-79", "id": 79}],
                "code_samples": [{"id": "cs1", "caption": "example", "code": "print(1)"}],
            },
            "affected_assets": {
                "asset-1": {
                    "id": "asset-1",
                    "asset": "host1",
                    "status": "Open",
                    "vulnerableParameters": [{"id": "p1", "text": "q"}],
                }
            },
        }
    )

    assert finding.flaw_id == 99
    assert finding.cves[0].name == "CVE-2024-0001"
    assert isinstance(finding.affected_assets["asset-1"], AffectedAsset)
    assert finding.affected_assets["asset-1"].vulnerable_parameters[0].text == "q"
