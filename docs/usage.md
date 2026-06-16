# Usage

## Create A Client

```python
from plextrac_api.functions.auth import create_session
from plextrac_api.functions import clients, findings

session = create_session(
    base_url="https://example.plextrac.com",
    username="user@example.com",
    password="secret",
)

client = clients.create_client(session, name="Example Client")
```

## Grouped Function Modules

```python
from plextrac_api.functions import clients, reports, findings

clients.get_client(session, client_id="client-cuid")
reports.export_report_to_pdf(session, client_id="client-cuid", report_id="report-cuid")
findings.list_report_findings(session, clientId="client-cuid", reportId="report-cuid")
```

## Use Explicit Request Data

Generated methods accept `json`, `params`, `data`, `files`, `headers`, and `content`
for cases where the endpoint needs a precise request shape.

```python
finding = findings.create_finding(
    session,
    clientId="client-cuid",
    reportId="report-cuid",
    json={"title": "Example finding"},
)
```

## Raw Escape Hatch

```python
from plextrac_api.functions.common import rest_request

result = rest_request(session, "POST", "/api/v2/clients", json={"pagination": {"limit": 50}})
```
