from __future__ import annotations

import json
from pathlib import Path
from typing import BinaryIO

from plextrac_api.functions.common import rest_request
from plextrac_api.types.auth import AuthSession
from plextrac_api.types.common import OperationResult
from plextrac_api.types.files import (
    Artifact,
    ArtifactRelation,
    ArtifactUploadResult,
    TenantImageUploadResult,
    artifact_filter_payload,
)


def list_artifacts(
    session: AuthSession,
    *,
    components: list[str] | None = None,
    relations: list[ArtifactRelation] | None = None,
) -> list[Artifact]:
    """List file-manager artifacts using documented component and relation filters."""
    if not relations:
        raise ValueError("list_artifacts requires at least one relation filter.")
    data = rest_request(
        session,
        "POST",
        "/api/v1/file-manager/artifacts",
        json=artifact_filter_payload(components=components, relations=relations),
    )
    return _artifact_list(data)


def download_artifact(
    session: AuthSession,
    artifact_id: str,
) -> bytes:
    """Download one file-manager artifact."""
    data = rest_request(session, "GET", f"/api/v1/file-manager/artifacts/{artifact_id}")
    if isinstance(data, bytes):
        return data
    raise ValueError("PlexTrac artifact download response was not bytes.")


def upload_artifact(
    session: AuthSession,
    file: str | Path | BinaryIO,
    *,
    description: str | None = None,
    components: list[str] | None = None,
    relations: list[ArtifactRelation] | None = None,
    filename: str | None = None,
    content_type: str | None = None,
) -> ArtifactUploadResult:
    """Upload a tenant artifact file with optional components and relations."""
    data_fields = _artifact_upload_fields(
        description=description,
        components=components,
        relations=relations,
    )
    data = _upload_file(
        session,
        "/api/v1/file-manager/upload",
        file,
        data=data_fields,
        filename=filename,
        content_type=content_type,
        fallback_name="artifact",
    )
    return ArtifactUploadResult.from_api(data if isinstance(data, dict) else {"data": data})


def delete_artifact(
    session: AuthSession,
    artifact_id: str,
) -> OperationResult:
    """Delete one file-manager artifact."""
    data = rest_request(session, "DELETE", f"/api/v1/file-manager/artifacts/{artifact_id}")
    return OperationResult.from_api(data if isinstance(data, dict) else {"data": data})


def get_upload_by_name(
    session: AuthSession,
    upload_name: str,
) -> bytes:
    """Get an inline rich-text upload using PlexTrac's cookie-only upload auth."""
    if not session.cookie:
        raise ValueError("PlexTrac session did not include an upload cookie. Log in again.")
    data = rest_request(
        session,
        "GET",
        f"/api/v1/uploads/{upload_name}",
        headers={"Cookie": _token_cookie(session.cookie)},
        authenticated=False,
    )
    if isinstance(data, bytes):
        return data
    raise ValueError("PlexTrac upload response was not bytes.")


def upload_tenant_image(
    session: AuthSession,
    file: str | Path | BinaryIO,
    *,
    scopes: list[str] | None = None,
    filename: str | None = None,
    content_type: str | None = None,
) -> TenantImageUploadResult:
    """Upload an inline tenant image."""
    data = _upload_file(
        session,
        "/api/v1/uploads",
        file,
        data={"setScope": json.dumps(scopes)} if scopes is not None else None,
        filename=filename,
        content_type=content_type,
        fallback_name="image",
    )
    if not isinstance(data, dict):
        raise ValueError("PlexTrac tenant image upload response was not a JSON object.")
    return TenantImageUploadResult.from_api(data)


def _upload_file(
    session: AuthSession,
    path: str,
    file: str | Path | BinaryIO,
    *,
    data: dict[str, str] | None = None,
    filename: str | None = None,
    content_type: str | None = None,
    fallback_name: str,
) -> object:
    close_after = None
    if isinstance(file, (str, Path)):
        file_path = Path(file)
        close_after = file_path.open("rb")
        file_obj: BinaryIO = close_after
        upload_name = filename or file_path.name
    else:
        file_obj = file
        upload_name = filename or Path(getattr(file, "name", fallback_name)).name

    files = {"file": (upload_name, file_obj, content_type) if content_type else (upload_name, file_obj)}
    try:
        return rest_request(session, "POST", path, data=data, files=files)
    finally:
        if close_after is not None:
            close_after.close()


def _artifact_upload_fields(
    *,
    description: str | None,
    components: list[str] | None,
    relations: list[ArtifactRelation] | None,
) -> dict[str, str]:
    data: dict[str, str] = {}
    if description is not None:
        data["description"] = description
    if components is not None:
        data["components"] = json.dumps(components)
    if relations is not None:
        data["relations"] = json.dumps([relation.to_api() for relation in relations])
    return data


def _artifact_list(data: object) -> list[Artifact]:
    if isinstance(data, list):
        return [Artifact.from_api(item) for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        items = data.get("data") or data.get("artifacts")
        if isinstance(items, list):
            return [Artifact.from_api(item) for item in items if isinstance(item, dict)]
    return []


def _token_cookie(cookie: str) -> str:
    return cookie if cookie.startswith("token=") else f"token={cookie}"
