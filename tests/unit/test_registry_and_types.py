from plextrac_api.generated.endpoints import GROUPS
from plextrac_api.types import (
    AffectedAsset,
    AffectedAssetStatus,
    AffectedAssetStatusUpdate,
    Artifact,
    ArtifactRelation,
    ArtifactRelationModel,
    ArtifactUploadResult,
    Asset,
    AssetCreateResult,
    AssetCriticality,
    AssetInput,
    AssetType,
    Client,
    ClientAssetFilter,
    ClientAssetFilterField,
    ClientAssetSort,
    ClientAssetSortField,
    ClientCreateResult,
    ClientFilter,
    ClientFilterField,
    ClientFindingFilter,
    ClientFindingFilterField,
    ClientPageLimit,
    ClientPagination,
    ClientSort,
    ClientSortField,
    EmailTemplate,
    EmailTemplateKind,
    Filter,
    Finding,
    FindingCreateResult,
    FindingField,
    FindingFilter,
    FindingFilterField,
    FindingPageLimit,
    FindingPagination,
    FindingSeverity,
    FindingSort,
    FindingSortField,
    FindingStatus,
    FindingVisibility,
    OperationResult,
    Pagination,
    Report,
    ReportCreateResult,
    ReportFilter,
    ReportFilterField,
    ReportSort,
    ReportSortField,
    ReportStatus,
    Sort,
    SortOrder,
    Substatus,
    SubstatusInput,
    SubstatusStatus,
    TenantAssetFilter,
    TenantAssetFilterField,
    TenantAssetSort,
    TenantAssetSortField,
    TenantImageUploadResult,
)


def test_generated_registry_covers_public_snapshot():
    total = sum(len(group["endpoints"]) for group in GROUPS.values())

    assert total == 357
    assert "clients" in GROUPS
    assert "assets" in GROUPS
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
    assert client.custom_fields[0].label == "Region"
    assert client.users["user@example.com"].role == "ADMIN"


def test_asset_type_parses_documented_fields():
    asset = Asset.from_api(
        {
            "id": "asset-1",
            "asset": "host1",
            "client_id": 1,
            "assetCriticality": "High",
            "type": "Server",
            "knownIps": ["192.0.2.1"],
            "ports": {"443": {"number": "443", "service": "https", "protocol": "tcp"}},
        }
    )

    assert asset.id == "asset-1"
    assert asset.name == "host1"
    assert asset.criticality is AssetCriticality.HIGH
    assert asset.type is AssetType.SERVER
    assert asset.ports["443"].protocol == "tcp"


def test_client_request_shape_types_serialize_with_verified_fields():
    assert Pagination(limit=50, offset=25).to_api() == {"offset": 25, "limit": 50}
    assert Sort(by="name", order=SortOrder.DESCENDING).to_api() == {"by": "name", "order": "DESC"}
    assert Filter(by="tags", value=["external"]).to_api() == {"by": "tags", "value": ["external"]}
    assert ClientPagination(limit=ClientPageLimit.FIFTY, offset=25).to_api() == {
        "offset": 25,
        "limit": 50,
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


def test_create_result_types_preserve_specific_identifiers():
    assert ClientCreateResult.from_api({"client_id": 1, "created": True}).client_id == 1
    assert AssetCreateResult.from_api({"id": "asset-1", "status": "success"}).asset_id == "asset-1"
    assert ReportCreateResult.from_api({"report_id": 42, "message": "success"}).report_id == 42
    assert FindingCreateResult.from_api({"flaw_id": 99, "status": "success"}).flaw_id == 99


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
        type=AssetType.SERVER,
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
    assert artifact.relations[0].id == 500824
    assert ArtifactRelation(model=ArtifactRelationModel.CLIENT, id=1045).to_api() == {
        "model": "client",
        "id": 1045,
    }
    upload_result = ArtifactUploadResult.from_api(
        {"status": "ok", "data": {"id": "artifact-2"}}
    )
    assert upload_result.artifact_id == "artifact-2"
    assert TenantImageUploadResult.from_api(
        {"fileUrl": "uploads/image.png"}
    ).file_url == "uploads/image.png"


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


def test_report_request_shape_types_serialize_with_verified_fields():
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
    assert FindingField(key="synopsis", label="Synopsis", value="Example").to_api() == {
        "key": "synopsis",
        "label": "Synopsis",
        "value": "Example",
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
            "fields": [{"key": "synopsis", "label": "Synopsis", "value": "Example"}],
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
    assert finding.cuid == "finding-cuid"
    assert finding.severity is FindingSeverity.HIGH
    assert finding.status is FindingStatus.OPEN
    assert finding.visibility is FindingVisibility.PUBLISHED
    assert finding.cves[0].name == "CVE-2024-0001"
    assert finding.fields[0].key == "synopsis"
    assert isinstance(finding.affected_assets["asset-1"], AffectedAsset)
    assert finding.affected_assets["asset-1"].status is AffectedAssetStatus.OPEN
    assert finding.affected_assets["asset-1"].vulnerable_parameters[0].text == "q"


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
