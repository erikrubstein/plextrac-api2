from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.scheduler import (
    EngagementScheduleArtifact,
    EngagementScheduleArtifactUploadResult,
    EngagementScheduleEvent,
    EngagementScheduleEventInput,
    EngagementScheduleEventPage,
    EngagementScheduleEventSearch,
)


def upload_engagement_schedule_event_artifact(
    session: AuthSession,
    engagement_schedule_event_cuid: str,
    client_cuid: str,
    file: str | Path | BinaryIO,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> EngagementScheduleArtifactUploadResult:
    """Upload a file artifact to an engagement schedule event."""
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", "schedule-artifact")).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        data = rest_request(
            session,
            "POST",
            "/api/v2/engagement-schedule-artifacts",
            data={
                "cuid": engagement_schedule_event_cuid,
                "clientCuid": client_cuid,
            },
            files=files,
        )
    finally:
        if close_after is not None:
            close_after.close()
    return EngagementScheduleArtifactUploadResult.from_api(data if isinstance(data, dict) else {"data": data})


def list_engagement_schedule_event_artifacts(
    session: AuthSession,
    engagement_schedule_event_cuid: str,
    client_cuid: str,
) -> list[EngagementScheduleArtifact]:
    """List file artifacts attached to an engagement schedule event."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/engagement-schedule-events/{engagement_schedule_event_cuid}/engagement-schedule-artifacts",
        params={"clientCuid": client_cuid},
    )
    return [EngagementScheduleArtifact.from_api(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []


def update_engagement_schedule_event_artifact(
    session: AuthSession,
    engagement_schedule_artifact_cuid: str,
    *,
    client_cuid: str | None = None,
    engagement_schedule_event_cuid: str | None = None,
) -> EngagementScheduleArtifact:
    """Move an artifact to a different client or engagement schedule event."""
    payload = {
        "clientCuid": client_cuid,
        "engagementScheduleEventCuid": engagement_schedule_event_cuid,
    }
    data = rest_request(
        session,
        "PATCH",
        f"/api/v2/engagement-schedule-artifacts/{engagement_schedule_artifact_cuid}",
        json={key: value for key, value in payload.items() if value is not None},
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac schedule artifact response was not a JSON object.")
    return EngagementScheduleArtifact.from_api(data)


def delete_engagement_schedule_event_artifact(
    session: AuthSession,
    engagement_schedule_artifact_cuid: str,
    client_cuid: str,
) -> OperationResult:
    """Delete an engagement schedule event artifact."""
    data = rest_request(
        session,
        "DELETE",
        f"/api/v2/engagement-schedule-artifacts/{engagement_schedule_artifact_cuid}",
        params={"clientCuid": client_cuid},
    )
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def download_engagement_schedule_event_artifact(
    session: AuthSession,
    engagement_schedule_event_cuid: str,
    engagement_schedule_artifact_cuid: str,
    client_cuid: str,
) -> bytes:
    """Download an engagement schedule event artifact."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/engagement-schedule-events/{engagement_schedule_event_cuid}/engagement-schedule-artifacts/{engagement_schedule_artifact_cuid}",
        params={"clientCuid": client_cuid},
    )
    if isinstance(data, bytes):
        return data
    raise ValueError("PlexTrac schedule artifact download response was not bytes.")


def search_engagement_schedule_events(
    session: AuthSession,
    search: EngagementScheduleEventSearch,
) -> EngagementScheduleEventPage:
    """Search engagement schedule events."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/engagement-schedule-events/search",
        json=search.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac schedule event search response was not a JSON object.")
    return EngagementScheduleEventPage.from_api(data)


def get_engagement_schedule_event(
    session: AuthSession,
    engagement_schedule_event_cuid: str,
) -> EngagementScheduleEvent:
    """Get one engagement schedule event."""
    data = rest_request(
        session,
        "GET",
        f"/api/v2/engagement-schedule-events/{engagement_schedule_event_cuid}",
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac schedule event response was not a JSON object.")
    return EngagementScheduleEvent.from_api(data)


def create_engagement_schedule_event(
    session: AuthSession,
    event: EngagementScheduleEventInput,
) -> EngagementScheduleEvent:
    """Create the initial engagement schedule event details."""
    data = rest_request(
        session,
        "POST",
        "/api/v2/engagement-schedule-events",
        json=event.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac schedule event response was not a JSON object.")
    return EngagementScheduleEvent.from_api(data)


def approve_engagement_schedule_event(
    session: AuthSession,
    engagement_schedule_event_cuid: str,
    event: EngagementScheduleEventInput,
) -> EngagementScheduleEvent:
    """Approve or finalize report/date/operator details for a schedule event."""
    data = rest_request(
        session,
        "POST",
        f"/api/v2/engagement-schedule-events/{engagement_schedule_event_cuid}/approve",
        json=event.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac schedule event response was not a JSON object.")
    return EngagementScheduleEvent.from_api(data)


def update_engagement_schedule_event(
    session: AuthSession,
    engagement_schedule_event_cuid: str,
    event: EngagementScheduleEventInput,
) -> EngagementScheduleEvent:
    """Update an engagement schedule event."""
    data = rest_request(
        session,
        "PATCH",
        f"/api/v2/engagement-schedule-events/{engagement_schedule_event_cuid}",
        json=event.to_api(),
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac schedule event response was not a JSON object.")
    return EngagementScheduleEvent.from_api(data)
