from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum

from plextrac_api.types.common import JsonDict


class WebhookEventType(str, Enum):
    REPORT_FINDING_CREATED_OR_EDITED = "report_finding_created_or_edited"
    REPORT_CREATED_OR_EDITED = "report_created_or_edited"
    REPORT_PUBLISHED = "ReportPublished"
    FINDING_PUBLISHED = "FindingPublished"
    ASSESSMENT_SUBMITTED = "AssessmentSubmitted"
    SCHEDULER_ENGAGEMENT_SUBMITTED = "SchedulerEngagementSubmitted"
    UNKNOWN = "unknown"


class WebhookSignatureAlgorithm(str, Enum):
    SHA256 = "sha256"


@dataclass(slots=True)
class ReportFindingCreatedOrEditedEvent:
    client_id: int | str | None = None
    report_id: int | str | None = None
    finding_id: int | str | None = None
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(
        default=WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED,
        init=False,
    )

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportFindingCreatedOrEditedEvent:
        return cls(
            client_id=_identifier(data, "clientId", "client_id"),
            report_id=_identifier(data, "reportId", "report_id"),
            finding_id=_identifier(data, "findingId", "finding_id", "flawId", "flaw_id"),
            event_name=_event_name(data),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportCreatedOrEditedEvent:
    client_id: int | str | None = None
    report_id: int | str | None = None
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(
        default=WebhookEventType.REPORT_CREATED_OR_EDITED,
        init=False,
    )

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportCreatedOrEditedEvent:
        return cls(
            client_id=_identifier(data, "clientId", "client_id"),
            report_id=_identifier(data, "reportId", "report_id"),
            event_name=_event_name(data),
            raw=dict(data),
        )


@dataclass(slots=True)
class ReportPublishedEvent:
    target_cuid: str | None = None
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(default=WebhookEventType.REPORT_PUBLISHED, init=False)

    @classmethod
    def from_api(cls, data: JsonDict) -> ReportPublishedEvent:
        return cls(
            target_cuid=_string(data, "targetCuid", "target_cuid", "cuid"),
            event_name=_event_name(data),
            raw=dict(data),
        )


@dataclass(slots=True)
class FindingPublishedEvent:
    client_id: int | str | None = None
    report_id: int | str | None = None
    finding_id: int | str | None = None
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(default=WebhookEventType.FINDING_PUBLISHED, init=False)

    @classmethod
    def from_api(cls, data: JsonDict) -> FindingPublishedEvent:
        return cls(
            client_id=_identifier(data, "clientId", "client_id"),
            report_id=_identifier(data, "reportId", "report_id"),
            finding_id=_identifier(data, "findingId", "finding_id", "flawId", "flaw_id"),
            event_name=_event_name(data),
            raw=dict(data),
        )


@dataclass(slots=True)
class AssessmentSubmittedEvent:
    client_id: int | str | None = None
    report_id: int | str | None = None
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(
        default=WebhookEventType.ASSESSMENT_SUBMITTED,
        init=False,
    )

    @classmethod
    def from_api(cls, data: JsonDict) -> AssessmentSubmittedEvent:
        return cls(
            client_id=_identifier(data, "clientId", "client_id"),
            report_id=_identifier(data, "reportId", "report_id"),
            event_name=_event_name(data),
            raw=dict(data),
        )


@dataclass(slots=True)
class SchedulerEngagementSubmittedEvent:
    target_cuid: str | None = None
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(
        default=WebhookEventType.SCHEDULER_ENGAGEMENT_SUBMITTED,
        init=False,
    )

    @classmethod
    def from_api(cls, data: JsonDict) -> SchedulerEngagementSubmittedEvent:
        return cls(
            target_cuid=_string(data, "targetCuid", "target_cuid", "engagementScheduleEventCuid"),
            event_name=_event_name(data),
            raw=dict(data),
        )


@dataclass(slots=True)
class UnknownWebhookEvent:
    event_name: str | None = None
    raw: JsonDict | None = None
    event_type: WebhookEventType = field(default=WebhookEventType.UNKNOWN, init=False)

    @classmethod
    def from_api(cls, data: JsonDict) -> UnknownWebhookEvent:
        return cls(event_name=_event_name(data), raw=dict(data))


ParsedWebhookEvent = (
    ReportFindingCreatedOrEditedEvent
    | ReportCreatedOrEditedEvent
    | ReportPublishedEvent
    | FindingPublishedEvent
    | AssessmentSubmittedEvent
    | SchedulerEngagementSubmittedEvent
    | UnknownWebhookEvent
)


def classify_webhook_event(
    data: JsonDict,
    event_type: WebhookEventType | None = None,
) -> WebhookEventType:
    if event_type is not None:
        return event_type

    event_name = _event_name(data)
    if event_name is None:
        return WebhookEventType.UNKNOWN

    normalized = re.sub(r"[^a-z0-9]+", "", event_name.lower())
    return _EVENT_NAME_MAP.get(normalized, WebhookEventType.UNKNOWN)


def webhook_event_from_api(
    data: JsonDict,
    event_type: WebhookEventType | None = None,
) -> ParsedWebhookEvent:
    resolved_type = classify_webhook_event(data, event_type)
    event_cls = _EVENT_CLASS_MAP.get(resolved_type, UnknownWebhookEvent)
    return event_cls.from_api(data)


def _event_name(data: JsonDict) -> str | None:
    return _string(data, "event", "eventName", "eventType", "type", "name")


def _identifier(data: JsonDict, *keys: str) -> int | str | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, (int, str)) and value != "":
            return value
    return None


def _string(data: JsonDict, *keys: str) -> str | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value:
            return value
    return None


_EVENT_NAME_MAP = {
    "wfaonreportfindingcreationedit": WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED,
    "reportfindingcreationedit": WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED,
    "reportfindingcreatededited": WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED,
    "wfaonreportcreationedit": WebhookEventType.REPORT_CREATED_OR_EDITED,
    "reportcreationedit": WebhookEventType.REPORT_CREATED_OR_EDITED,
    "reportcreatededited": WebhookEventType.REPORT_CREATED_OR_EDITED,
    "reportpublished": WebhookEventType.REPORT_PUBLISHED,
    "findingpublished": WebhookEventType.FINDING_PUBLISHED,
    "assessmentsubmitted": WebhookEventType.ASSESSMENT_SUBMITTED,
    "schedulerengagementsubmitted": WebhookEventType.SCHEDULER_ENGAGEMENT_SUBMITTED,
}

_EVENT_CLASS_MAP = {
    WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED: ReportFindingCreatedOrEditedEvent,
    WebhookEventType.REPORT_CREATED_OR_EDITED: ReportCreatedOrEditedEvent,
    WebhookEventType.REPORT_PUBLISHED: ReportPublishedEvent,
    WebhookEventType.FINDING_PUBLISHED: FindingPublishedEvent,
    WebhookEventType.ASSESSMENT_SUBMITTED: AssessmentSubmittedEvent,
    WebhookEventType.SCHEDULER_ENGAGEMENT_SUBMITTED: SchedulerEngagementSubmittedEvent,
    WebhookEventType.UNKNOWN: UnknownWebhookEvent,
}
