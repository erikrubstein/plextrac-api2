# Pagination

The SDK includes conservative limit/offset request types for endpoints with common pagination
parameters.

```python
from plextrac_api.functions import clients
from plextrac_api.types import ClientPageLimit, ClientPagination

page = clients.list_clients(session, pagination=ClientPagination(limit=ClientPageLimit.FIFTY, offset=0))
```

Avoid relying on oversized limits. PlexTrac's API change policy has included pagination-related
changes, so workflow code should iterate pages deliberately.
