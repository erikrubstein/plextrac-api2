from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum, StrEnum

from plextrac_api.types.common import JsonDict


class EngagementSchedulePageLimit(IntEnum):
    TEN = 10
    TWENTY_FIVE = 25
    FIFTY = 50
    ONE_HUNDRED = 100
    FIVE_HUNDRED = 500


class EngagementScheduleOrder(StrEnum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class EngagementScheduleStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    SCHEDULED = "SCHEDULED"
    IN_REVIEW = "IN_REVIEW"
    COMPLETE = "COMPLETE"
    CANCELED = "CANCELED"


@dataclass(slots=True)
class EngagementScheduleArtifact:
    artifact_cuid: str | None = None
    filename: str | None = None
    client_cuid: str | None = None
    engagement_schedule_event_cuid: str | None = None
    content_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleArtifact:
        source = _data_object(data)
        return cls(
            artifact_cuid=source.get("cuid") or source.get("engagementScheduleArtifactCuid"),
            filename=source.get("filename") or source.get("name"),
            client_cuid=source.get("clientCuid"),
            engagement_schedule_event_cuid=source.get("engagementScheduleEventCuid"),
            content_type=source.get("contentType") or source.get("content_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class EngagementScheduleArtifactUploadResult:
    artifact_cuid: str | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.artifact_cuid is not None or self.status in {"created", "ok", "success"}

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleArtifactUploadResult:
        nested = _data_object(data)
        return cls(
            artifact_cuid=data.get("cuid")
            or data.get("engagementScheduleArtifactCuid")
            or nested.get("cuid")
            or nested.get("engagementScheduleArtifactCuid"),
            status=data.get("status"),
            message=data.get("message"),
            raw=dict(data),
        )


@dataclass(slots=True)
class EngagementScheduleEventInput:
    payload: JsonDict

    def to_api(self) -> JsonDict:
        return dict(self.payload)


@dataclass(slots=True)
class EngagementScheduleEventSearch:
    criteria: JsonDict = field(default_factory=dict)
    pagination: EngagementSchedulePagination = field(
        default_factory=lambda: EngagementSchedulePagination()
    )

    def to_api(self) -> JsonDict:
        return {"filter": self.criteria, "pagination": self.pagination.to_api()}


@dataclass(slots=True)
class EngagementSchedulePagination:
    offset: int = 0
    limit: EngagementSchedulePageLimit = EngagementSchedulePageLimit.TEN
    order: EngagementScheduleOrder = EngagementScheduleOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"offset": self.offset, "limit": int(self.limit), "order": self.order.value}


@dataclass(slots=True)
class EngagementScheduleEvent:
    event_cuid: str | None = None
    tenant_cuid: str | None = None
    title: str | None = None
    client_cuid: str | None = None
    client_id: int | str | None = None
    client_name: str | None = None
    report_id: int | str | None = None
    report_cuid: str | None = None
    report_name: str | None = None
    status: EngagementScheduleStatus | None = None
    start: str | None = None
    end: str | None = None
    test_window: str | None = None
    test_type: str | None = None
    objective: str | None = None
    scope: str | None = None
    access_info: str | None = None
    special_instructions: str | None = None
    version: int | None = None
    created_at: str | None = None
    created_by: str | None = None
    last_update_at: str | None = None
    last_updated_by: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleEvent:
        source = _data_object(data)
        client = source.get("client")
        report = source.get("report")
        return cls(
            event_cuid=source.get("cuid") or source.get("engagementScheduleEventCuid"),
            tenant_cuid=source.get("tenantCuid"),
            title=source.get("title") or source.get("name") or source.get("engagementName"),
            client_cuid=_nested_value(client, "cuid") or source.get("clientCuid"),
            client_id=_nested_value(client, "id") or source.get("clientId"),
            client_name=_nested_value(client, "name") or source.get("clientName"),
            report_id=_nested_value(report, "id") or source.get("reportId"),
            report_cuid=_nested_value(report, "cuid") or source.get("reportCuid"),
            report_name=_nested_value(report, "name") or source.get("reportName"),
            status=_schedule_status(source.get("status")),
            start=source.get("start"),
            end=source.get("end"),
            test_window=source.get("testWindow"),
            test_type=source.get("testType"),
            objective=source.get("objective"),
            scope=source.get("scope"),
            access_info=source.get("accessInfo"),
            special_instructions=source.get("specialInstructions"),
            version=source.get("version") if isinstance(source.get("version"), int) else None,
            created_at=source.get("createdAt"),
            created_by=source.get("createdBy"),
            last_update_at=source.get("lastUpdateAt"),
            last_updated_by=source.get("lastUpdatedBy"),
            raw=dict(data),
        )


@dataclass(slots=True)
class EngagementScheduleEventPage:
    events: list[EngagementScheduleEvent]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleEventPage:
        items = data.get("data") or data.get("items") or data.get("events")
        return cls(
            events=[
                EngagementScheduleEvent.from_api(item)
                for item in items
                if isinstance(item, dict)
            ]
            if isinstance(items, list)
            else [],
            total_count=data.get("total") or data.get("totalCount"),
            raw=dict(data),
        )


def _nested_value(value: object, key: str) -> object:
    return value.get(key) if isinstance(value, dict) else None


def _data_object(data: JsonDict) -> JsonDict:
    nested = data.get("data")
    return nested if isinstance(nested, dict) else data


def _schedule_status(value: object) -> EngagementScheduleStatus | None:
    if isinstance(value, EngagementScheduleStatus):
        return value
    if isinstance(value, str):
        try:
            return EngagementScheduleStatus(value)
        except ValueError:
            return None
    return None
