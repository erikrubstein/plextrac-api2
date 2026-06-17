# Usage Notes

This SDK is still being polished group by group. Treat `clients`, `reports`, `findings`, and
`assets` as the current examples of the intended public API shape.

Generated function modules remain available for broad endpoint coverage, but they are scaffolding:
their signatures and return values may be less explicit until that group is polished.

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
    ClientAssetPageLimit,
    ClientAssetSort,
    ClientAssetSortField,
    SortOrder,
)

asset_page = assets.list_client_assets(
    session,
    client_id="client-cuid",
    limit=ClientAssetPageLimit.FIFTY,
    sort=[ClientAssetSort(by=ClientAssetSortField.ASSET, order=SortOrder.ASCENDING)],
)

created = assets.create_asset(
    session,
    client_id="client-cuid",
    asset=AssetInput(name="host1.example.com", type="hostname"),
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

Use `rest_request` for unsupported workflows or while a group is still generated-only.

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
