from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.common import JsonDict


@dataclass(slots=True)
class Evidence:
    id: str | None = None
    name: str | None = None
    description: str | None = None
    file_url: str | None = None
    content_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Evidence:
        return cls(
            id=data.get("id") or data.get("cuid") or data.get("evidenceId"),
            name=data.get("name") or data.get("filename"),
            description=data.get("description"),
            file_url=data.get("fileUrl") or data.get("url"),
            content_type=data.get("contentType") or data.get("mimeType"),
            raw=dict(data),
        )

