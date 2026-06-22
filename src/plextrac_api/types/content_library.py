from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from plextrac_api.types.common import JsonDict, clean
from plextrac_api.types.findings import CommonIdentifiers, FindingField, FindingSeverity


class WriteupImportSource(StrEnum):
    CSV = "csv"


@dataclass(slots=True)
class ContentLibraryUserInput:
    user_id: int | str
    permission_level: str | None = None

    def to_api(self) -> JsonDict:
        return clean({"userId": self.user_id, "permissionLevel": self.permission_level})


@dataclass(slots=True)
class ContentLibraryUser:
    user_id: int | str | None = None
    email: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    full_name: str | None = None
    permission_level: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> ContentLibraryUser:
        source = _nested_object(data)
        return cls(
            user_id=_first_value(source, ("userId", "user_id", "id")),
            email=source.get("email"),
            username=source.get("username"),
            first_name=_first_value(source, ("firstName", "first_name", "first")),
            last_name=_first_value(source, ("lastName", "last_name", "last")),
            full_name=_first_value(source, ("fullName", "full_name", "name")),
            permission_level=_first_value(
                source,
                ("permissionLevel", "permission_level", "permissionsLevel", "role"),
            ),
            raw=dict(data),
        )


@dataclass(slots=True)
class NarrativeSectionInput:
    title: str
    repository_id: int | str
    section_id: int | str | None = None
    text: str | None = None
    parent_id: int | str | None = None
    order: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "label": self.title,
                "id": self.section_id,
                "repositoryId": self.repository_id,
                "text": self.text,
                "parentId": self.parent_id,
                "order": self.order,
            }
        )


@dataclass(slots=True)
class NarrativeSection:
    section_id: int | str | None = None
    repository_id: int | str | None = None
    title: str | None = None
    text: str | None = None
    parent_id: int | str | None = None
    order: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> NarrativeSection:
        source = _nested_object(data)
        return cls(
            section_id=_first_value(source, ("sectionId", "section_id", "id")),
            repository_id=_first_value(source, ("repositoryId", "repositoryID", "repository_id")),
            title=_first_value(source, ("title", "label", "name")),
            text=_first_value(source, ("text", "body", "content")),
            parent_id=_first_value(source, ("parentId", "parent_id")),
            order=source.get("order"),
            raw=dict(data),
        )


@dataclass(slots=True)
class NarrativeRepositoryInput:
    name: str
    description: str | None = None
    permission_level: str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "name": self.name,
                "description": self.description,
                "permissionsLevel": self.permission_level,
            }
        )


@dataclass(slots=True)
class NarrativeRepository:
    repository_id: int | str | None = None
    name: str | None = None
    description: str | None = None
    permission_level: str | None = None
    sections: list[NarrativeSection] | None = None
    users: list[ContentLibraryUser] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> NarrativeRepository:
        source = _nested_object(data)
        sections = source.get("sections")
        users = source.get("users") or source.get("repositoryUsers")
        return cls(
            repository_id=_first_value(
                source,
                ("repositoryId", "repositoryID", "repository_id", "id"),
            ),
            name=_first_value(source, ("name", "title")),
            description=source.get("description"),
            permission_level=_first_value(
                source,
                ("permissionsLevel", "permissionLevel", "permission_level"),
            ),
            sections=[
                NarrativeSection.from_api(item) for item in sections if isinstance(item, dict)
            ]
            if isinstance(sections, list)
            else None,
            users=[ContentLibraryUser.from_api(item) for item in users if isinstance(item, dict)]
            if isinstance(users, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class WriteupInput:
    title: str
    repository_id: int | str
    severity: FindingSeverity
    description: str | None = None
    recommendations: str | None = None
    references: str | None = None
    fields: list[FindingField] | None = None
    tags: list[str] | None = None
    risk_score: float | None = None
    calculated_severity: bool | None = None
    common_identifiers: CommonIdentifiers | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "title": self.title,
                "repositoryId": self.repository_id,
                "severity": self.severity.value,
                "description": self.description,
                "recommendations": self.recommendations,
                "references": self.references,
                "fields": [field.to_api() for field in self.fields]
                if self.fields is not None
                else None,
                "tags": self.tags,
                "risk_score": self.risk_score,
                "calculated_severity": self.calculated_severity,
                "common_identifiers": self.common_identifiers.to_api()
                if self.common_identifiers is not None
                else None,
            }
        )


@dataclass(slots=True)
class Writeup:
    writeup_id: int | str | None = None
    doc_id: int | str | None = None
    doc_type: str | None = None
    repository_id: int | str | None = None
    tenant_id: int | str | None = None
    title: str | None = None
    severity: FindingSeverity | None = None
    description: str | None = None
    recommendations: str | None = None
    references: str | None = None
    source: str | None = None
    fields: list[FindingField] | None = None
    tags: list[str] | None = None
    risk_score: float | None = None
    calculated_severity: bool | None = None
    common_identifiers: CommonIdentifiers | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Writeup:
        source = _nested_object(data)
        fields = source.get("fields")
        tags = source.get("tags")
        risk_score = source.get("risk_score")
        return cls(
            writeup_id=_first_value(source, ("writeupId", "writeup_id", "template_id", "id")),
            doc_id=_first_value(source, ("doc_id", "docId")),
            doc_type=_first_value(source, ("doc_type", "docType")),
            repository_id=_first_value(source, ("repositoryId", "repositoryID", "repository_id")),
            tenant_id=_first_value(source, ("tenantId", "tenant_id")),
            title=source.get("title"),
            severity=_severity(source.get("severity")),
            description=source.get("description"),
            recommendations=source.get("recommendations"),
            references=source.get("references"),
            source=source.get("source"),
            fields=[
                field for field in (FindingField.from_api(item) for item in fields or []) if field
            ]
            if isinstance(fields, list)
            else None,
            tags=[str(item) for item in tags] if isinstance(tags, list) else None,
            risk_score=float(risk_score) if isinstance(risk_score, (int, float)) else None,
            calculated_severity=source.get("calculated_severity"),
            common_identifiers=CommonIdentifiers.from_api(source.get("common_identifiers")),
            raw=dict(data),
        )


@dataclass(slots=True)
class WriteupRepositoryInput:
    name: str
    description: str | None = None

    def to_api(self) -> JsonDict:
        return clean({"name": self.name, "description": self.description})


@dataclass(slots=True)
class WriteupRepository:
    repository_id: int | str | None = None
    name: str | None = None
    description: str | None = None
    writeups: list[Writeup] | None = None
    users: list[ContentLibraryUser] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> WriteupRepository:
        source = _nested_object(data)
        writeups = source.get("writeups")
        users = source.get("users") or source.get("repositoryUsers")
        return cls(
            repository_id=_first_value(
                source,
                ("repositoryId", "repositoryID", "repository_id", "id"),
            ),
            name=_first_value(source, ("name", "title")),
            description=source.get("description"),
            writeups=[Writeup.from_api(item) for item in writeups if isinstance(item, dict)]
            if isinstance(writeups, list)
            else None,
            users=[ContentLibraryUser.from_api(item) for item in users if isinstance(item, dict)]
            if isinstance(users, list)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class WriteupTransfer:
    writeup_ids: list[int | str]
    destination_repository_id: int | str
    source_repository_id: int | str | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "writeups": self.writeup_ids,
                "destinationRepositoryId": self.destination_repository_id,
                "sourceRepositoryId": self.source_repository_id,
            }
        )


@dataclass(slots=True)
class WriteupDeleteResult:
    message: str | None = None
    doc_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.message == "success" or self.doc_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> WriteupDeleteResult:
        source = _nested_object(data)
        doc_id = _first_value(source, ("doc_id", "docId"))
        if doc_id is None:
            doc_id = _first_value(data, ("doc_id", "docId"))
        return cls(
            message=source.get("message") or data.get("message"),
            doc_id=doc_id,
            raw=dict(data),
        )


@dataclass(slots=True)
class ContentLibraryImportResult:
    status: str | None = None
    message: str | None = None
    import_id: int | str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success" or self.import_id is not None

    @classmethod
    def from_api(cls, data: JsonDict) -> ContentLibraryImportResult:
        source = _nested_object(data)
        import_id = _first_value(source, ("import_id", "importId", "id"))
        if import_id is None:
            import_id = _first_value(data, ("import_id", "importId", "id"))
        return cls(
            status=source.get("status") or data.get("status"),
            message=source.get("message") or data.get("message"),
            import_id=import_id,
            raw=dict(data),
        )


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


def _severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        try:
            return FindingSeverity(value)
        except ValueError:
            return None
    return None
