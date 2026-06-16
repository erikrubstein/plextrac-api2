# PlexTrac Python API

This project is an early unofficial Python API for PlexTrac. It mirrors the high-level
organization of the public PlexTrac API documentation with Monarch-style function modules
and dataclass types.

```python
from plextrac_api.functions.auth import create_session
from plextrac_api.functions import clients, reports

session = create_session(
    base_url="https://example.plextrac.com",
    username="user@example.com",
    password="secret",
)

client_page = clients.list_clients(session)
report = reports.get(session, clientId="client-id", reportId="report-id")
```

## Current Scope

- Installable Python package.
- Function modules grouped like the PlexTrac API docs.
- Session object passed explicitly into every API function.
- Shared HTTP helpers using `httpx`.
- Bearer token, username/password login, token refresh, and raw-token support.
- Generated endpoint functions from the public PlexTrac Postman reference.
- Raw REST and GraphQL helpers.
- Dataclass types for documented PlexTrac object structures.
- Webhook signature helper.

Generated endpoint functions intentionally return decoded JSON dictionaries by default.
Use the dataclass types in `plextrac_api.types` when you want to normalize documented
object structures.

## Function Modules

```python
from plextrac_api.functions import findings

created = findings.create(
    session,
    clientId="client-cuid",
    reportId="report-cuid",
    title="Example finding",
    severity="Medium",
    status="Open",
    description="Example description",
)
```

## Types

```python
from plextrac_api.types import Client

client = Client.from_api(raw_client)
print(client.name)
```

## Raw Requests

```python
from plextrac_api.functions.common import rest_request

roles = rest_request(
    session,
    "GET",
    "/api/v2/tenants/{tenantId}/security/role",
    params={"limit": 50},
)
```

## Generated Functions

Endpoint placeholders can be passed directly as keyword arguments:

```python
pdf = reports.export_report_to_pdf(
    session,
    clientId="client-cuid",
    reportId="report-cuid",
    includeEvidence=False,
)
```

You can also use explicit request options:

```python
result = findings.create_finding(
    session,
    clientId="client-cuid",
    reportId="report-cuid",
    json={"title": "Example finding"},
)
```

## GraphQL

```python
from plextrac_api.functions.common import execute_graphql

result = execute_graphql(
    session,
    "query Example($tenantId: String!) { tenant(id: $tenantId) { id } }",
    variables={"tenantId": "tenant-cuid"},
)
```

## Documentation

See [docs/methodology.md](docs/methodology.md) for SDK design rules,
[ROADMAP.md](ROADMAP.md) for the implementation roadmap, and
[docs/endpoint-coverage.md](docs/endpoint-coverage.md) for the generated endpoint coverage snapshot.
