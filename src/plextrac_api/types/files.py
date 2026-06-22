from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict, clean


class ArtifactRelationModel(StrEnum):
    CLIENT = "client"
    REPORT = "report"
    ASSESSMENT_QUESTION = "assessment_question"


@dataclass(slots=True)
class ArtifactRelation:
    model: ArtifactRelationModel
    object_id: int | str
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ArtifactRelation | None:
        model = _artifact_relation_model(data.get("model"))
        relation_id = data.get("id")
        if model is None or relation_id is None:
            return None
        return cls(model=model, object_id=relation_id, raw=dict(data))

    def to_api(self) -> JsonDict:
        return {"model": self.model.value, "id": str(self.object_id)}


@dataclass(slots=True)
class Artifact:
    artifact_id: str | None = None
    filename: str | None = None
    content_type: str | None = None
    description: str | None = None
    size: int | None = None
    created_at: int | None = None
    components: list[str] | None = None
    relations: list[ArtifactRelation] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Artifact:
        source = _nested_object(data)
        relations = source.get("relations")
        return cls(
            artifact_id=_first_value(source, ("id", "artifactId", "artifact_id")),
            filename=_first_value(source, ("filename", "name")),
            content_type=_first_value(source, ("content_type", "contentType")),
            description=source.get("description"),
            size=source.get("size") if isinstance(source.get("size"), int) else None,
            created_at=_first_value(source, ("createdAt", "created_at")),
            components=source.get("components")
            if isinstance(source.get("components"), list)
            else None,
            relations=[
                relation
                for relation in (
                    ArtifactRelation.from_api(item) for item in relations if isinstance(item, dict)
                )
                if relation is not None
            ]
            if isinstance(relations, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class ArtifactUploadResult:
    artifact_id: str | None = None
    status: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "ok" or self.artifact_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> ArtifactUploadResult:
        nested = data.get("data")
        return cls(
            artifact_id=_artifact_id(nested) or _artifact_id(data),
            status=_first_value(_nested_object(data), ("status",)) or data.get("status"),
            raw=dict(data),
        )


@dataclass(slots=True)
class TenantImageUploadResult:
    file_url: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> TenantImageUploadResult:
        source = _nested_object(data)
        return cls(file_url=_first_value(source, ("fileUrl", "file_url", "url")), raw=dict(data))


def artifact_filter_payload(
    *,
    components: list[str] | None = None,
    relations: list[ArtifactRelation] | None = None,
) -> JsonDict:
    return clean(
        {
            "components": components,
            "relations": [relation.to_api() for relation in relations]
            if relations is not None
            else None,
        }
    )


def _artifact_relation_model(value: object) -> ArtifactRelationModel | None:
    if isinstance(value, ArtifactRelationModel):
        return value
    if isinstance(value, str):
        try:
            return ArtifactRelationModel(value)
        except ValueError:
            return None
    return None


def _artifact_id(data: object) -> str | None:
    if not isinstance(data, dict):
        return None
    value = _first_value(data, ("id", "artifactId", "artifact_id"))
    return str(value) if value is not None else None


def _nested_object(data: JsonDict) -> JsonDict:
    nested = data.get("data")
    if isinstance(nested, dict):
        return nested
    return data


def _first_value(data: JsonDict, keys: tuple[str, ...]) -> object:
    for key in keys:
        if key in data and data[key] is not None:
            return data[key]
    return None
