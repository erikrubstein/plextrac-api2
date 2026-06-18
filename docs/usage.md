# Usage Notes

The SDK exposes PlexTrac through grouped function modules and explicit dataclasses. Functions that
call PlexTrac accept an `AuthSession` as their first argument.

## Authentication

```python
from plextrac_api.functions.auth import create_session

session = create_session(
    base_url="https://example.plextrac.com",
    username="user@example.com",
    password="secret",
)
```

For token-based workflows:

```python
from plextrac_api.functions.auth import session_from_token

session = session_from_token("https://example.plextrac.com", "token")
```

## Clients

```python
from plextrac_api.functions import clients
from plextrac_api.types import (
    ClientInput,
    ClientPageLimit,
    ClientPagination,
    ClientSort,
    ClientSortField,
    SortOrder,
)

page = clients.list_clients(
    session,
    pagination=ClientPagination(limit=ClientPageLimit.FIFTY, offset=0),
    sort=[ClientSort(by=ClientSortField.NAME, order=SortOrder.ASCENDING)],
)

client = clients.get_client(session, client_id="client-cuid")
created = clients.create_client(session, ClientInput(name="Example Client"))
```

## Assets

```python
from plextrac_api.functions import assets
from plextrac_api.types import (
    AssetInput,
    AssetType,
    ClientAssetPageLimit,
    ClientAssetSort,
    ClientAssetSortField,
    SortOrder,
)

asset_page = assets.list_client_assets(
    session,
    client_id="client-1",
    limit=ClientAssetPageLimit.FIFTY,
    sort=[ClientAssetSort(by=ClientAssetSortField.ASSET, order=SortOrder.ASCENDING)],
)

created = assets.create_asset(
    session,
    client_id="client-1",
    asset=AssetInput(name="host1.example.com", type=AssetType.SERVER),
)
```

## Reports

```python
from plextrac_api.functions import reports
from plextrac_api.types import ReportInput, ReportSort, ReportSortField, ReportStatus, SortOrder

report_page = reports.list_reports(
    session,
    sort=[ReportSort(by=ReportSortField.STATUS, order=SortOrder.DESCENDING)],
)

created = reports.create_report(
    session,
    client_id="client-cuid",
    report=ReportInput(name="Example Report", status=ReportStatus.DRAFT),
)

pdf_bytes = reports.export_report_to_pdf(
    session,
    client_id="client-cuid",
    report_id="report-cuid",
)
```

## Findings

```python
from plextrac_api.functions import findings
from plextrac_api.types import (
    FindingInput,
    FindingPageLimit,
    FindingPagination,
    FindingSeverity,
    FindingStatus,
)

page = findings.list_report_findings(
    session,
    client_id="client-cuid",
    report_id="report-cuid",
    pagination=FindingPagination(limit=FindingPageLimit.TEN),
)

created = findings.create_finding(
    session,
    client_id="client-cuid",
    report_id="report-cuid",
    finding=FindingInput(
        title="Example Finding",
        severity=FindingSeverity.HIGH,
        status=FindingStatus.OPEN,
        description="Example description",
    ),
)
```

## Raw REST Escape Hatch

Use `rest_request` for unsupported workflows, newly documented endpoints that have not been added
yet, or payload fields PlexTrac supports but this SDK has not modeled.

```python
from plextrac_api.functions.common import rest_request

result = rest_request(
    session,
    "POST",
    "/api/v2/clients",
    json={"pagination": {"limit": 50, "offset": 0}},
)
```

## GraphQL

GraphQL exists as a raw helper for documented GraphQL operations. It is not currently a polished
first-class SDK surface.

```python
from plextrac_api.functions.common import execute_graphql

result = execute_graphql(
    session,
    "query Example($tenantId: String!) { tenant(id: $tenantId) { id } }",
    variables={"tenantId": "tenant-cuid"},
)
```

## Webhooks

Webhook helpers verify and parse inbound PlexTrac requests without depending on a web framework.

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
