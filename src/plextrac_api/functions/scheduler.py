"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def create_engagement_schedule_event_artifact(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/engagement-schedule-artifacts\n\nPlexTrac endpoint: Create Engagement Schedule Event Artifact"""
    return endpoint_request(session, "scheduler", "create_engagement_schedule_event_artifact", **kwargs)


def get_engagement_schedule_event_artifacts(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts\n\nPlexTrac endpoint: Get Engagement Schedule Event Artifacts"""
    return endpoint_request(session, "scheduler", "get_engagement_schedule_event_artifacts", **kwargs)


def update_engagement_schedule_event_artifact(session: AuthSession, **kwargs: Any) -> Any:
    """PATCH /api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}\n\nPlexTrac endpoint: Update Engagement Schedule Event Artifact"""
    return endpoint_request(session, "scheduler", "update_engagement_schedule_event_artifact", **kwargs)


def delete_engagement_schedule_event_artifact(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}\n\nPlexTrac endpoint: Delete Engagement Schedule Event Artifact"""
    return endpoint_request(session, "scheduler", "delete_engagement_schedule_event_artifact", **kwargs)


def download_engagement_schedule_event_artifact(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}\n\nPlexTrac endpoint: Download Engagement Schedule Event Artifact"""
    return endpoint_request(session, "scheduler", "download_engagement_schedule_event_artifact", **kwargs)


def find_many_engagement_schedule_events(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/engagement-schedule-events/search\n\nPlexTrac endpoint: Find Many Engagement Schedule Events"""
    return endpoint_request(session, "scheduler", "find_many_engagement_schedule_events", **kwargs)


def get_engagement_schedule_event_by_id(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v2/engagement-schedule-events/{engagementScheduleEventCuid}\n\nPlexTrac endpoint: Get Engagement Schedule Event by ID"""
    return endpoint_request(session, "scheduler", "get_engagement_schedule_event_by_id", **kwargs)


def create_engagement_schedule_event(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/engagement-schedule-events\n\nPlexTrac endpoint: Create Engagement Schedule Event"""
    return endpoint_request(session, "scheduler", "create_engagement_schedule_event", **kwargs)


def approve_engagement_schedule_event(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/approve\n\nPlexTrac endpoint: Approve Engagement Schedule Event"""
    return endpoint_request(session, "scheduler", "approve_engagement_schedule_event", **kwargs)


def update_engagement_schedule_event(session: AuthSession, **kwargs: Any) -> Any:
    """PATCH /api/v2/engagement-schedule-events/{engagementScheduleEventCuid}\n\nPlexTrac endpoint: Update Engagement Schedule Event"""
    return endpoint_request(session, "scheduler", "update_engagement_schedule_event", **kwargs)

