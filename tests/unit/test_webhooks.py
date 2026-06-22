import hashlib
import hmac

import pytest

from plextrac_api.functions.webhooks import (
    parse_verified_webhook_event,
    parse_webhook_event,
    signature_from_headers,
    verify_signature,
)
from plextrac_api.types import (
    AssessmentSubmittedEvent,
    FindingPublishedEvent,
    ReportCreatedOrEditedEvent,
    ReportFindingCreatedOrEditedEvent,
    ReportPublishedEvent,
    SchedulerEngagementSubmittedEvent,
    UnknownWebhookEvent,
    WebhookEventType,
)


def test_verify_signature_accepts_prefixed_hmac_digest():
    payload = b'{"event":"created"}'
    secret = "secret"
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

    assert verify_signature(payload=payload, signature=f"sha256={digest}", secret=secret)


def test_signature_from_headers_is_case_insensitive():
    assert (
        signature_from_headers({"X-Authorization-Hmac-256": "sha256=abc"})
        == "sha256=abc"
    )


def test_parse_webhook_event_uses_documented_event_name():
    event = parse_webhook_event(
        '{"event":"FindingPublished","clientId":1,"reportId":2,"findingId":3}'
    )

    assert isinstance(event, FindingPublishedEvent)
    assert event.event_type is WebhookEventType.FINDING_PUBLISHED
    assert event.client_id == 1
    assert event.report_id == 2
    assert event.finding_id == 3


def test_parse_webhook_event_accepts_explicit_event_type_for_wfa_payloads():
    event = parse_webhook_event(
        {"clientId": "client-1", "reportId": "report-1", "findingId": "finding-1"},
        event_type=WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED,
    )

    assert event.event_type is WebhookEventType.REPORT_FINDING_CREATED_OR_EDITED
    assert event.client_id == "client-1"
    assert event.report_id == "report-1"
    assert event.finding_id == "finding-1"


def test_parse_webhook_event_maps_wfa_event_names():
    finding_event = parse_webhook_event(
        {
            "event": "WFA: On Report Finding Creation/Edit",
            "clientId": 0,
            "reportId": 2,
            "flawId": 3,
        }
    )
    report_event = parse_webhook_event(
        {
            "event": "WFA: On Report Creation/Edit",
            "clientId": 0,
            "reportId": 2,
        }
    )

    assert isinstance(finding_event, ReportFindingCreatedOrEditedEvent)
    assert finding_event.client_id == 0
    assert finding_event.finding_id == 3
    assert isinstance(report_event, ReportCreatedOrEditedEvent)
    assert report_event.client_id == 0
    assert report_event.report_id == 2


def test_parse_webhook_event_returns_unknown_for_unrecognized_payload():
    event = parse_webhook_event('{"event":"NewEvent","value":true}')

    assert isinstance(event, UnknownWebhookEvent)
    assert event.event_name == "NewEvent"
    assert event.raw == {"event": "NewEvent", "value": True}


def test_parse_verified_webhook_event_verifies_before_parsing():
    payload = b'{"event":"ReportPublished","targetCuid":"report-cuid"}'
    secret = "secret"
    digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

    event = parse_verified_webhook_event(
        payload=payload,
        signature=f"sha256={digest}",
        secret=secret,
    )

    assert isinstance(event, ReportPublishedEvent)
    assert event.report_cuid == "report-cuid"


def test_parse_webhook_event_maps_assessment_submission_report_ids():
    event = parse_webhook_event(
        '{"event":"AssessmentSubmitted","clientId":"client-1","reportId":"report-1"}'
    )

    assert isinstance(event, AssessmentSubmittedEvent)
    assert event.client_id == "client-1"
    assert event.report_id == "report-1"


def test_parse_verified_webhook_event_rejects_invalid_signature():
    with pytest.raises(ValueError):
        parse_verified_webhook_event(
            payload=b'{"event":"SchedulerEngagementSubmitted"}',
            signature="sha256=bad",
            secret="secret",
        )


def test_parse_webhook_event_maps_scheduler_target_cuid():
    event = parse_webhook_event(
        '{"event":"SchedulerEngagementSubmitted","targetCuid":"engagement-cuid"}'
    )

    assert isinstance(event, SchedulerEngagementSubmittedEvent)
    assert event.engagement_schedule_event_cuid == "engagement-cuid"
