"""Generated PlexTrac endpoint functions.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

from __future__ import annotations

from typing import Any

from plextrac_api.functions.common import endpoint_request
from plextrac_api.types.auth import AuthSession


def get_artifacts(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/file-manager/artifacts\n\nPlexTrac endpoint: Get artifacts"""
    return endpoint_request(session, "files", "get_artifacts", **kwargs)


def download_an_artifact(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/file-manager/artifacts/{artifactId}\n\nPlexTrac endpoint: Download an artifact"""
    return endpoint_request(session, "files", "download_an_artifact", **kwargs)


def upload_an_artifact_file(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/file-manager/upload\n\nPlexTrac endpoint: Upload an artifact (file)"""
    return endpoint_request(session, "files", "upload_an_artifact_file", **kwargs)


def delete_an_artifact(session: AuthSession, **kwargs: Any) -> Any:
    """DELETE /api/v1/file-manager/artifacts/{artifactId}\n\nPlexTrac endpoint: Delete an artifact"""
    return endpoint_request(session, "files", "delete_an_artifact", **kwargs)


def get_upload_by_name(session: AuthSession, **kwargs: Any) -> Any:
    """GET /api/v1/uploads/9bee9f28-7e25-4b4f-8b64-b520fc3c0b7c.png\n\nPlexTrac endpoint: Get Upload by Name"""
    return endpoint_request(session, "files", "get_upload_by_name", **kwargs)


def upload_image_to_tenant(session: AuthSession, **kwargs: Any) -> Any:
    """POST /api/v1/uploads\n\nPlexTrac endpoint: Upload Image to Tenant"""
    return endpoint_request(session, "files", "upload_image_to_tenant", **kwargs)

