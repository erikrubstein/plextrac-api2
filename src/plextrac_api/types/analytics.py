from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from plextrac_api.types.assets import AssetCriticality
from plextrac_api.types.common import JsonDict, clean
from plextrac_api.types.findings import FindingSeverity, FindingStatus

AnalyticsRecordKind = Literal["generic", "client", "report", "finding", "asset"]


@dataclass(slots=True)
class AnalyticsTags:
    clients: list[str] | None = None
    reports: list[str] | None = None
    findings: list[str] | None = None
    assets: list[str] | None = None
    client_tags_is_union: bool | None = None
    report_tags_is_union: bool | None = None
    finding_tags_is_union: bool | None = None
    asset_tags_is_union: bool | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.clients,
                "reports": self.reports,
                "findings": self.findings,
                "assets": self.assets,
                "clientTagsIsUnion": self.client_tags_is_union,
                "reportTagsIsUnion": self.report_tags_is_union,
                "findingTagsIsUnion": self.finding_tags_is_union,
                "assetTagsIsUnion": self.asset_tags_is_union,
            }
        )


@dataclass(slots=True)
class AnalyticsFilter:
    client_ids: list[int] | None = None
    report_ids: list[int] | None = None
    asset_ids: list[int | str] | None = None
    tags: AnalyticsTags | None = None
    severity_ids: list[int] | None = None
    statuses: list[FindingStatus] | None = None
    substatuses: list[str] | None = None
    date_from: str | None = None
    date_to: str | None = None
    limit: int | None = None
    offset: int | None = None
    assignees: list[str] | None = None
    cve_ids: list[str] | None = None
    cwe_ids: list[str] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.client_ids,
                "reports": self.report_ids,
                "assets": self.asset_ids,
                "tags": self.tags.to_api() if self.tags is not None else None,
                "severities": self.severity_ids,
                "statuses": [status.value for status in self.statuses]
                if self.statuses is not None
                else None,
                "subStatuses": self.substatuses,
                "dateFrom": self.date_from,
                "dateTo": self.date_to,
                "limit": self.limit,
                "offset": self.offset,
                "assignees": self.assignees,
                "cveIDs": self.cve_ids,
                "cweIDs": self.cwe_ids,
            }
        )


@dataclass(slots=True)
class FindingAnalyticsBootstrapFilter:
    client_ids: list[int] | None = None
    client_tags: list[str] | None = None
    asset_tags: list[str] | None = None
    report_ids: list[int] | None = None
    report_tags: list[str] | None = None
    finding_tags: list[str] | None = None
    order: list[str] | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.client_ids,
                "clientTags": self.client_tags,
                "assetTags": self.asset_tags,
                "reports": self.report_ids,
                "reportTags": self.report_tags,
                "findingTags": self.finding_tags,
                "order": self.order,
            }
        )


@dataclass(slots=True)
class AssetAnalyticsFilter:
    client_ids: list[int] | None = None
    criticality: list[AssetCriticality] | None = None
    finding_severities: list[FindingSeverity] | None = None
    asset_types: list[str] | None = None
    asset_tags: list[str] | None = None
    limit: int | None = None
    offset: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.client_ids,
                "criticality": [item.value for item in self.criticality]
                if self.criticality is not None
                else None,
                "findings": {"severity": [item.value for item in self.finding_severities]}
                if self.finding_severities is not None
                else None,
                "type": self.asset_types,
                "tags": {"assets": self.asset_tags} if self.asset_tags is not None else None,
            }
        )


@dataclass(slots=True)
class AnalyticsTrendFilter:
    client_ids: list[int] | None = None
    report_ids: list[int] | None = None
    finding_severities: list[FindingSeverity] | None = None
    finding_tags: list[str] | None = None
    report_tags: list[str] | None = None
    age: int | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.client_ids,
                "reports": self.report_ids,
                "severity": [item.value for item in self.finding_severities]
                if self.finding_severities is not None
                else None,
                "tags": clean({"findings": self.finding_tags, "reports": self.report_tags})
                if self.finding_tags is not None or self.report_tags is not None
                else None,
                "age": self.age,
            }
        )


@dataclass(slots=True)
class SlaAnalyticsFilter:
    client_ids: list[int] | None = None
    date_from: str | None = None
    date_to: str | None = None
    report_ids: list[int] | None = None
    finding_severities: list[FindingSeverity] | None = None
    client_tags: list[str] | None = None
    report_tags: list[str] | None = None
    finding_tags: list[str] | None = None
    asset_criticality: list[AssetCriticality] | None = None
    asset_tags: list[str] | None = None
    finding_tags_is_union: bool | None = None
    asset_tags_is_union: bool | None = None

    def to_api(self) -> JsonDict:
        return clean(
            {
                "clients": self.client_ids,
                "dateFrom": self.date_from,
                "dateTo": self.date_to,
                "reports": self.report_ids,
                "findingSeverities": [item.value for item in self.finding_severities]
                if self.finding_severities is not None
                else None,
                "clientTags": self.client_tags,
                "reportTags": self.report_tags,
                "findingTags": self.finding_tags,
                "assetCriticality": [item.value for item in self.asset_criticality]
                if self.asset_criticality is not None
                else None,
                "assetTags": self.asset_tags,
                "findingTagsIsUnion": self.finding_tags_is_union,
                "assetTagsIsUnion": self.asset_tags_is_union,
            }
        )


@dataclass(slots=True)
class AnalyticsRecord:
    client_id: int | str | None = None
    report_id: int | str | None = None
    finding_id: int | str | None = None
    asset_id: int | str | None = None
    client_name: str | None = None
    report_name: str | None = None
    finding_title: str | None = None
    asset_name: str | None = None
    asset_type: str | None = None
    severity: FindingSeverity | None = None
    status: FindingStatus | None = None
    severity_counts: dict[str, int] | None = None
    finding_count: int | None = None
    report_count: int | None = None
    asset_count: int | None = None
    total_count: int | None = None
    count: int | None = None
    percentage: str | float | None = None
    date_from: str | None = None
    date_to: str | None = None
    last_update_at: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(
        cls,
        data: JsonDict,
        *,
        record_kind: AnalyticsRecordKind = "generic",
    ) -> AnalyticsRecord:
        raw_id = _first(data, "id")
        return cls(
            client_id=_first(data, "client_id", "clientId")
            or (raw_id if record_kind == "client" else None),
            report_id=_first(data, "report_id", "reportId")
            or (raw_id if record_kind == "report" else None),
            finding_id=_first(data, "finding_id", "findingId", "flaw_id", "flawId")
            or (raw_id if record_kind == "finding" else None),
            asset_id=_first(data, "asset_id", "assetId")
            or (raw_id if record_kind == "asset" else None),
            client_name=_string(data, "client_name", "clientName"),
            report_name=_string(data, "report_name", "reportName"),
            finding_title=_string(data, "finding_title", "findingTitle", "title", "name"),
            asset_name=_string(data, "asset_name", "assetName", "asset"),
            asset_type=_string(data, "asset_type", "assetType", "type"),
            severity=_finding_severity(_first(data, "severity")),
            status=_finding_status(_first(data, "status")),
            severity_counts=_severity_counts(
                _first(data, "severity_counts", "severityCounts", "severities")
            ),
            finding_count=_integer(data, "finding_count", "findingCount", "findings"),
            report_count=_integer(data, "report_count", "reportCount", "reports"),
            asset_count=_integer(data, "asset_count", "assetCount", "assets"),
            total_count=_integer(data, "total_count", "totalCount", "total"),
            count=_integer(data, "count"),
            percentage=_first(data, "percentage"),
            date_from=_string(data, "date_from", "dateFrom"),
            date_to=_string(data, "date_to", "dateTo"),
            last_update_at=_string(
                data,
                "last_update_at",
                "lastUpdateAt",
                "updated_at",
                "updatedAt",
            ),
            raw=dict(data),
        )


@dataclass(slots=True)
class AnalyticsResult:
    status: str | None = None
    message: str | None = None
    data: JsonDict | list[JsonDict] | None = None
    records: list[AnalyticsRecord] = field(default_factory=list)
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(
        cls,
        data: JsonDict | list[JsonDict],
        *,
        record_kind: AnalyticsRecordKind = "generic",
    ) -> AnalyticsResult:
        if isinstance(data, dict):
            payload = data.get("data")
            return cls(
                status=data.get("status"),
                message=data.get("message"),
                data=payload if isinstance(payload, (dict, list)) else None,
                records=_records_from_payload(payload, record_kind=record_kind),
                total_count=_first_int(data, ("total", "totalCount", "count"))
                or _first_int(payload, ("total", "totalCount", "count")),
                raw=dict(data),
            )
        return cls(
            data=data,
            records=_records_from_payload(data, record_kind=record_kind),
            raw={"data": data},
        )


def _records_from_payload(
    payload: object,
    *,
    record_kind: AnalyticsRecordKind,
) -> list[AnalyticsRecord]:
    if isinstance(payload, list):
        return [
            AnalyticsRecord.from_api(item, record_kind=record_kind)
            for item in payload
            if isinstance(item, dict)
        ]
    if isinstance(payload, dict):
        items = _first_list(
            payload,
            ("data", "items", "results", "rows", "findings", "assets", "reports", "clients"),
        )
        return [
            AnalyticsRecord.from_api(item, record_kind=record_kind)
            for item in items
            if isinstance(item, dict)
        ]
    return []


def _first(data: JsonDict, *keys: str) -> object:
    for key in keys:
        if key in data:
            return data[key]
    return None


def _string(data: JsonDict, *keys: str) -> str | None:
    value = _first(data, *keys)
    return value if isinstance(value, str) else None


def _integer(data: JsonDict, *keys: str) -> int | None:
    value = _first(data, *keys)
    return value if isinstance(value, int) else None


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


def _first_int(data: object, keys: tuple[str, ...]) -> int | None:
    if not isinstance(data, dict):
        return None
    for key in keys:
        value = data.get(key)
        if isinstance(value, int):
            return value
        if isinstance(value, dict):
            nested = _first_int(value, keys)
            if nested is not None:
                return nested
    return None


def _finding_severity(value: object) -> FindingSeverity | None:
    if isinstance(value, FindingSeverity):
        return value
    if isinstance(value, str):
        for severity in FindingSeverity:
            if value.lower() == severity.value.lower():
                return severity
    return None


def _finding_status(value: object) -> FindingStatus | None:
    if isinstance(value, FindingStatus):
        return value
    if isinstance(value, str):
        for status in FindingStatus:
            if value.lower() == status.value.lower():
                return status
    return None


def _severity_counts(value: object) -> dict[str, int] | None:
    if isinstance(value, dict):
        return {str(key): count for key, count in value.items() if isinstance(count, int)}
    if isinstance(value, list):
        counts: dict[str, int] = {}
        for item in value:
            if not isinstance(item, dict):
                continue
            name = item.get("severity") or item.get("name") or item.get("label")
            count = item.get("count") or item.get("total")
            if isinstance(name, str) and isinstance(count, int):
                counts[name] = count
        return counts or None
    return None
