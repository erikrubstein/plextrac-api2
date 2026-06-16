# Usage Notes

This SDK is still being polished group by group. Treat `clients` and `reports` as the current
examples of the intended public API shape.

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
from plextrac_api.types import Pagination, Sort, SortOrder

page = clients.list_clients(
    session,
    pagination=Pagination(limit=50, offset=0),
    sort=[Sort(by="name", order=SortOrder.ASCENDING)],
)

client = clients.get_client(session, client_id="client-cuid")
created = clients.create_client(session, name="Example Client")
```

## Reports

```python
from plextrac_api.functions import reports
from plextrac_api.types import ReportSort, ReportSortField, ReportStatus, SortOrder

report_page = reports.list_reports(
    session,
    sort=[ReportSort(by=ReportSortField.STATUS, order=SortOrder.DESCENDING)],
)

created = reports.create_report(
    session,
    client_id="client-cuid",
    name="Example Report",
    status=ReportStatus.DRAFT,
)

pdf_bytes = reports.export_report_to_pdf(
    session,
    client_id="client-cuid",
    report_id="report-cuid",
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
