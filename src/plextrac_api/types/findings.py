from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum

from plextrac_api.types.assets import AffectedAsset
from plextrac_api.types.common import JsonDict, SortOrder, clean


class FindingSeverity(StrEnum):
    INFORMATIONAL = "Informational"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class FindingStatus(StrEnum):
    OPEN = "Open"
    IN_PROCESS = "In Process"
    CLOSED = "Closed"


class FindingVisibility(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"


class FindingImportSource(StrEnum):
    BURP = "burp"
    BURP_HTML = "burphtml"
    HORIZON = "horizon"
    NESSUS = "nessus"
    NEXPOSE = "nexpose"
    PLEXTRAC = "ptrac"
    VERACODE = "veracode"


class FindingSortField(StrEnum):
    ASSIGNED_TO = "assignedTo"
    CLIENT_ID = "clientId"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"
    REOPENED_AT = "reopenedAt"
    CLOSED_AT = "closedAt"
    FLAW_ID = "flawId"
    REPORT_ID = "reportId"
    SEVERITY = "severity"
    SOURCE = "source"
    STATUS = "status"
    SUBSTATUS = "subStatus"
    TITLE = "title"
    VISIBILITY = "visibility"
    CVSS_3_1 = "cvss3_1"
    CVE_ID = "cve_id"
    CWE_ID = "cwe_id"


class FindingFilterField(StrEnum):
    FINDING_TAGS = "findingTags"
    SEARCH_TERM = "searchTerm"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"
    REOPENED_AT = "reopenedAt"
    CLOSED_AT = "closedAt"
    ASSIGNED_TO = "assignedTo"
    FLAW_ID = "flaw_id"
    CLIENT_ID = "client_id"
    REPORT_ID = "report_id"
    SEVERITY = "severity"
    SOURCE = "source"
    STATUS = "status"
    SUBSTATUS = "subStatus"
    TITLE = "title"
    VISIBILITY = "visibility"


class FindingPageLimit(IntEnum):
    ONE = 1
    TEN = 10
    FIFTY = 50
    ONE_HUNDRED = 100


FindingFilterValue = (
    str
    | int
    | bool
    | FindingSeverity
    | FindingStatus
    | FindingVisibility
    | list[str]
    | list[int]
    | list[FindingSeverity]
    | list[FindingStatus]
    | list[FindingVisibility]
)


@dataclass(slots=True)
class FindingPagination:
    offset: int = 0
    limit: FindingPageLimit = FindingPageLimit.TEN

    def to_api(self) -> JsonDict:
        return {"offset": self.offset, "limit": int(self.limit)}


@dataclass(slots=True)
class Identifier:
    name: str | None = None
    id: int | str | None = None
    year: int | None = None
    link: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> Identifier | None:
        if not data:
            return None
        return cls(
            name=data.get("name"),
            id=data.get("id"),
            year=data.get("year"),
            link=data.get("link"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"name": self.name, "id": self.id, "year": self.year, "link": self.link})


@dataclass(slots=True)
class CodeSample:
    id: str | None = None
    caption: str | None = None
    code: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> CodeSample | None:
        if not data:
            return None
        return cls(
            id=data.get("id"),
            caption=data.get("caption"),
            code=data.get("code"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"id": self.id, "caption": self.caption, "code": self.code})


@dataclass(slots=True)
class CommonIdentifiers:
    cves: list[Identifier] | None = None
    cwes: list[Identifier] | None = None
    code_samples: list[CodeSample] | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> CommonIdentifiers | None:
        if not isinstance(data, dict):
            return None
        cves = data.get("CVE")
        cwes = data.get("CWE")
        code_samples = data.get("code_samples")
        return cls(
            cves=[item for item in (Identifier.from_api(value) for value in cves or []) if item]
            if isinstance(cves, list)
            else None,
            cwes=[item for item in (Identifier.from_api(value) for value in cwes or []) if item]
            if isinstance(cwes, list)
            else None,
            code_samples=[
                item
                for item in (CodeSample.from_api(value) for value in code_samples or [])
                if item
            ]
            if isinstance(code_samples, list)
            else None,
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "CVE": [item.to_api() for item in self.cves] if self.cves is not None else None,
                "CWE": [item.to_api() for item in self.cwes] if self.cwes is not None else None,
                "code_samples": [item.to_api() for item in self.code_samples]
                if self.code_samples is not None
                else None,
            }
        )


@dataclass(slots=True)
class FindingField:
    key: str | None = None
    label: str | None = None
    value: str | int | float | bool | list[str] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | None) -> FindingField | None:
        if not data:
            return None
        value = data.get("value")
        return cls(
            key=data.get("key"),
            label=data.get("label"),
            value=value
            if isinstance(value, (str, int, float, bool, list)) or value is None
            else None,
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean({"key": self.key, "label": self.label, "value": self.value})


@dataclass(slots=True)
class FindingInput:
    title: str | None = None
    severity: FindingSeverity | None = None
    status: FindingStatus | None = None
    description: str | None = None
    assigned_to: str | None = None
    source: str | None = None
    visibility: FindingVisibility | None = None
    selected_score: str | None = None
    tags: list[str] | None = None
    affected_assets: dict[str, AffectedAsset] | None = None
    common_identifiers: CommonIdentifiers | None = None
    fields: list[FindingField] | None = None
    recommendations: str | None = None
    references: str | None = None

    def to_api(self) -> JsonDict:
        return _finding_payload(
            title=self.title,
            severity=self.severity,
            status=self.status,
            description=self.description,
            assigned_to=self.assigned_to,
            source=self.source,
            visibility=self.visibility,
            selected_score=self.selected_score,
            tags=self.tags,
            affected_assets=self.affected_assets,
            common_identifiers=self.common_identifiers,
            fields=self.fields,
            recommendations=self.recommendations,
            references=self.references,
        )


@dataclass(slots=True)
class FindingCreateResult:
    flaw_id: int | str | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return _is_success_text(self.status) or _is_success_text(self.message)

    @classmethod
    def from_api(cls, data: JsonDict) -> FindingCreateResult:
        return cls(
            flaw_id=data.get("flaw_id") or data.get("finding_id"),
            status=data.get("status") or data.get("result"),
            message=data.get("message") or data.get("detail"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Finding:
    cuid: str | None = None
    flaw_id: int | str | None = None
    client_id: int | str | None = None
    report_id: int | str | None = None
    title: str | None = None
    description: str | None = None
    severity: FindingSeverity | None = None
    status: FindingStatus | None = None
    substatus: str | None = None
    substatus_cuid: str | None = None
    assigned_to: str | None = None
    source: str | None = None
    visibility: FindingVisibility | None = None
    selected_score: str | None = None
    tags: list[str] | None = None
    affected_assets: dict[str, AffectedAsset] | None = None
    common_identifiers: CommonIdentifiers | None = None
    cves: list[Identifier] | None = None
    cwes: list[Identifier] | None = None
    code_samples: list[CodeSample] | None = None
    fields: list[FindingField] | None = None
    created_at: int | None = None
    closed_at: int | None = None
    reopened_at: int | None = None
    last_update: int | None = None
    doc_type: str | None = None
    doc_version: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Finding:
        common_identifiers = CommonIdentifiers.from_api(data.get("common_identifiers"))
        affected_assets = data.get("affected_assets")
        fields = data.get("fields")
        return cls(
            cuid=data.get("cuid") or data.get("id"),
            flaw_id=data.get("flaw_id"),
            client_id=data.get("client_id"),
            report_id=data.get("report_id"),
            title=data.get("title"),
            description=data.get("description"),
            severity=_finding_severity(data.get("severity")),
            status=_finding_status(data.get("status")),
            substatus=data.get("subStatus"),
            substatus_cuid=data.get("substatusCuid"),
            assigned_to=data.get("assignedTo"),
            source=data.get("source"),
            visibility=_finding_visibility(data.get("visibility")),
            selected_score=data.get("selectedScore"),
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            affected_assets={
                key: asset
                for key, asset in (
                    (key, AffectedAsset.from_api(value))
                    for key, value in affected_assets.items()
                    if isinstance(value, dict)
                )
                if asset is not None
            }
            if isinstance(affected_assets, dict)
            else None,
            common_identifiers=common_identifiers,
            cves=common_identifiers.cves if common_identifiers is not None else None,
            cwes=common_identifiers.cwes if common_identifiers is not None else None,
            code_samples=common_identifiers.code_samples
            if common_identifiers is not None
            else None,
            fields=[
                field
                for field in (FindingField.from_api(item) for item in fields or [])
                if field is not None
            ]
            if isinstance(fields, list)
            else None,
            created_at=data.get("createdAt"),
            closed_at=data.get("closedAt"),
            reopened_at=data.get("reopenedAt") or data.get("repoenedAt"),
            last_update=data.get("last_update"),
            doc_type=data.get("doc_type"),
            doc_version=data.get("doc_version"),
            raw=dict(data),
        )


@dataclass(slots=True)
class FindingPage:
    findings: list[Finding]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> FindingPage:
        if isinstance(data, list):
            return cls(
                findings=[Finding.from_api(item) for item in data if isinstance(item, dict)],
                raw={"data": data},
            )

        items = _first_list(data, ("findings", "data", "items", "results"))
        return cls(
            findings=[Finding.from_api(item) for item in items if isinstance(item, dict)],
            total_count=_first_int(data, ("total", "totalCount", "count")),
            raw=dict(data),
        )


@dataclass(slots=True)
class FindingSort:
    by: FindingSortField
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "order": self.order.value}


@dataclass(slots=True)
class FindingFilter:
    by: FindingFilterField
    value: FindingFilterValue

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "value": _api_value(self.value)}


@dataclass(slots=True)
class FindingImportUpload:
    filename: str | None = None
    key: str | None = None
    content_type: str | None = None
    size: int | None = None
    import_id: str | None = None

    def to_presigned_api(self) -> JsonDict:
        return clean(
            {
                "filename": self.filename,
                "contentType": self.content_type,
                "size": self.size,
            }
        )

    def to_preuploaded_import_api(self) -> JsonDict:
        return clean({"key": self.key, "filename": self.filename, "importId": self.import_id})


@dataclass(slots=True)
class PresignedUpload:
    url: str | None = None
    key: str | None = None
    fields: dict[str, str] | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> PresignedUpload:
        fields = data.get("fields")
        return cls(
            url=data.get("url") or data.get("signedUrl") or data.get("uploadUrl"),
            key=data.get("key") or data.get("fileKey") or data.get("filename"),
            fields={str(key): value for key, value in fields.items() if isinstance(value, str)}
            if isinstance(fields, dict)
            else None,
            raw=dict(data),
        )


@dataclass(slots=True)
class FindingImportStatus:
    id: str | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> FindingImportStatus:
        return cls(
            id=data.get("id") or data.get("importId") or data.get("cuid"),
            status=data.get("status"),
            message=data.get("message") or data.get("detail"),
            raw=dict(data),
        )


@dataclass(slots=True)
class FindingEvidenceUpdate:
    id: str | None = None
    name: str | None = None
    description: str | None = None
    file_url: str | None = None
    content_type: str | None = None
    assets: list[int | str] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "fileUrl": self.file_url,
                "contentType": self.content_type,
                "assets": self.assets,
            }
        )


@dataclass(slots=True)
class FindingStatusUpdate:
    status: FindingStatus | None = None
    substatus: str | None = None
    substatus_cuid: str | None = None
    assigned_to: str | None = None
    comments: str | None = None
    created_at: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> FindingStatusUpdate:
        return cls(
            status=_finding_status(data.get("status")),
            substatus=data.get("subStatus"),
            substatus_cuid=data.get("substatusCuid"),
            assigned_to=data.get("assignedTo"),
            comments=data.get("comments") or data.get("comment"),
            created_at=data.get("createdAt"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        return clean(
            {
                "status": self.status.value if self.status is not None else None,
                "subStatus": self.substatus,
                "substatusCuid": self.substatus_cuid,
                "assignedTo": self.assigned_to,
                "comments": self.comments,
            }
        )


def _finding_payload(
    *,
    title: str | None = None,
    severity: FindingSeverity | None = None,
    status: FindingStatus | None = None,
    description: str | None = None,
    assigned_to: str | None = None,
    source: str | None = None,
    visibility: FindingVisibility | None = None,
    selected_score: str | None = None,
    tags: list[str] | None = None,
    affected_assets: dict[str, AffectedAsset] | None = None,
    common_identifiers: CommonIdentifiers | None = None,
    fields: list[FindingField] | None = None,
    recommendations: str | None = None,
    references: str | None = None,
) -> JsonDict:
    return clean(
        {
            "title": title,
            "severity": severity.value if severity is not None else None,
            "status": status.value if status is not None else None,
            "description": description,
            "assignedTo": assigned_to,
            "source": source,
            "visibility": visibility.value if visibility is not None else None,
            "selectedScore": selected_score,
            "tags": tags,
            "affected_assets": {key: asset.to_api() for key, asset in affected_assets.items()}
            if affected_assets is not None
            else None,
            "common_identifiers": common_identifiers.to_api()
            if common_identifiers is not None
            else None,
            "fields": [field.to_api() for field in fields] if fields is not None else None,
            "recommendations": recommendations,
            "references": references,
        }
    )


def _finding_severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        try:
            return FindingSeverity(value)
        except ValueError:
            return None
    return None


def _finding_status(value: object) -> FindingStatus | None:
    if isinstance(value, FindingStatus):
        return value
    if isinstance(value, str):
        try:
            return FindingStatus(value)
        except ValueError:
            return None
    return None


def _finding_visibility(value: object) -> FindingVisibility | None:
    if isinstance(value, FindingVisibility):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        try:
            return FindingVisibility(normalized)
        except ValueError:
            return None
    return None


def _api_value(value: object) -> object:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, list):
        return [_api_value(item) for item in value]
    return value


def _is_success_text(value: object) -> bool:
    if not isinstance(value, str):
        return False
    return value.lower() in {
        "ok",
        "success",
        "successful",
        "created",
    }


def _first_list(data: JsonDict, keys: tuple[str, ...]) -> list[JsonDict]:
    for key in keys:
        value = data.get(key)
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            nested = _first_list(value, keys)
            if nested:
                return nested
    return []


def _first_int(data: JsonDict, keys: tuple[str, ...]) -> int | None:
    for key in keys:
        value = data.get(key)
        if isinstance(value, int):
            return value
        if isinstance(value, dict):
            nested = _first_int(value, keys)
            if nested is not None:
                return nested
    return None
