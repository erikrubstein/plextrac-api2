from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.common import JsonDict, clean


@dataclass(slots=True)
class EngagementScheduleArtifact:
    cuid: str | None = None
    filename: str | None = None
    client_cuid: str | None = None
    engagement_schedule_event_cuid: str | None = None
    content_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleArtifact:
        return cls(
            cuid=data.get("cuid") or data.get("engagementScheduleArtifactCuid"),
            filename=data.get("filename") or data.get("name"),
            client_cuid=data.get("clientCuid"),
            engagement_schedule_event_cuid=data.get("engagementScheduleEventCuid"),
            content_type=data.get("contentType") or data.get("content_type"),
            raw=dict(data),
        )


@dataclass(slots=True)
class EngagementScheduleArtifactUploadResult:
    cuid: str | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.cuid is not None or self.status == "success"

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleArtifactUploadResult:
        return cls(
            cuid=data.get("cuid") or data.get("engagementScheduleArtifactCuid"),
            status=data.get("status"),
            message=data.get("message"),
            raw=dict(data),
        )


@dataclass(slots=True)
class EngagementScheduleEventInput:
    data: JsonDict

    def to_api(self) -> JsonDict:
        return dict(self.data)


@dataclass(slots=True)
class EngagementScheduleEventSearch:
    filters: JsonDict | None = None
    pagination: JsonDict | None = None
    sort: JsonDict | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "filters": self.filters,
                "pagination": self.pagination,
                "sort": self.sort,
            }
        )


@dataclass(slots=True)
class EngagementScheduleEvent:
    cuid: str | None = None
    client_cuid: str | None = None
    status: str | None = None
    name: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> EngagementScheduleEvent:
        return cls(
            cuid=data.get("cuid") or data.get("engagementScheduleEventCuid"),
            client_cuid=data.get("clientCuid"),
            status=data.get("status"),
            name=data.get("name") or data.get("engagementName"),
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
