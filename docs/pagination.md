# Pagination

The SDK includes conservative limit/offset request types for endpoints with common pagination
parameters.

```python
from plextrac_api.functions import clients
from plextrac_api.types import Pagination

page = clients.list_clients(session, pagination=Pagination(limit=50, offset=0))
```

Avoid relying on oversized limits. PlexTrac's API change policy has included pagination-related
changes, so workflow code should iterate pages deliberately.
