from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict, clean


class SubstatusStatus(StrEnum):
    OPEN = "Open"
    IN_PROCESS = "In Process"
    CLOSED = "Closed"


@dataclass(slots=True)
class SubstatusInput:
    status: SubstatusStatus | None = None
    value: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "status": self.status.value if self.status is not None else None,
                "value": self.value,
            }
        )


@dataclass(slots=True)
class Substatus:
    cuid: str | None = None
    tenant_cuid: str | None = None
    status: SubstatusStatus | None = None
    value: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Substatus:
        return cls(
            cuid=data.get("cuid"),
            tenant_cuid=data.get("tenantCuid"),
            status=_substatus_status(data.get("status")),
            value=data.get("value"),
            raw=dict(data),
        )


def _substatus_status(value: object) -> SubstatusStatus | None:
    if isinstance(value, SubstatusStatus):
        return value
    if isinstance(value, str):
        try:
            return SubstatusStatus(value)
        except ValueError:
            return None
    return None
