from __future__ import annotations

from collections.abc import ItemsView, KeysView, ValuesView
from dataclasses import dataclass
from enum import Enum, IntEnum

from plextrac_api.types.common import (
    JsonDict,
    ObjectReference,
    Port,
    SortOrder,
    VulnerableParameter,
    clean,
)


class TenantAssetPageLimit(IntEnum):
    FIVE = 5
    TEN = 10
    TWENTY_FIVE = 25
    FIFTY = 50
    ONE_HUNDRED = 100
    ONE_THOUSAND = 1000


class ClientAssetPageLimit(IntEnum):
    FIVE = 5
    TEN = 10
    TWENTY_FIVE = 25
    FIFTY = 50
    ONE_HUNDRED = 100


class TenantAssetSortField(str, Enum):
    SEARCH_TERM = "searchTerm"
    CLIENT_ID = "client_id"
    ASSET_CRITICALITY = "assetCriticality"
    TAGS = "tags"
    TYPE = "type"
    PCI_STATUS = "pci_status"
    SYSTEM_OWNER = "system_owner"
    DATA_OWNER = "data_owner"


class TenantAssetFilterField(str, Enum):
    SEARCH_TERM = "searchTerm"
    CLIENT_ID = "client_id"
    ASSET_CRITICALITY = "assetCriticality"
    TAGS = "tags"
    TYPE = "type"
    PCI_STATUS = "pci_status"
    SYSTEM_OWNER = "system_owner"
    DATA_OWNER = "data_owner"


class ClientAssetSortField(str, Enum):
    ASSET = "asset"
    TAGS = "tags"


class ClientAssetFilterField(str, Enum):
    ASSET = "asset"
    TAGS = "tags"


class AssetImportSource(str, Enum):
    NMAP_XML = "nmap-xml"
    NMAP_CSV = "nmap-csv"
    LEGACY_NMAP = "nmap"
    LEGACY_CSV = "csv"


class AssetType(str, Enum):
    SERVER = "Server"
    WORKSTATION = "Workstation"
    NETWORK_DEVICE = "Network Device"
    APPLICATION = "Application"
    GENERAL = "General"


class AssetCriticality(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFORMATION = "Information"


class AffectedAssetImportSource(str, Enum):
    CSV = "csv"
    XML = "xml"


class AffectedAssetStatus(str, Enum):
    OPEN = "Open"
    IN_PROCESS = "In Process"
    CLOSED = "Closed"


@dataclass(slots=True)
class TenantAssetSort:
    by: TenantAssetSortField
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "order": self.order.value}


@dataclass(slots=True)
class TenantAssetFilter:
    by: TenantAssetFilterField
    value: str | int | list[str] | list[int]

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "value": self.value}


@dataclass(slots=True)
class ClientAssetSort:
    by: ClientAssetSortField
    order: SortOrder = SortOrder.ASCENDING

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "order": self.order.value}


@dataclass(slots=True)
class ClientAssetFilter:
    by: ClientAssetFilterField
    value: str | list[str]

    def to_api(self) -> JsonDict:
        return {"by": self.by.value, "value": self.value}


@dataclass(slots=True)
class AssetInput:
    name: str | None = None
    type: AssetType | None = None
    criticality: AssetCriticality | None = None
    description: str | None = None
    hostname: str | None = None
    dns_name: str | None = None
    host_fqdn: str | None = None
    host_rdns: str | None = None
    mac_address: str | None = None
    known_ips: list[str] | None = None
    operating_system: list[str] | None = None
    parent_asset: ObjectReference | None = None
    ports: dict[str, Port] | None = None
    tags: list[str] | None = None

    def to_api(self) -> JsonDict:
        return _asset_payload(
            name=self.name,
            type=self.type,
            criticality=self.criticality,
            description=self.description,
            hostname=self.hostname,
            dns_name=self.dns_name,
            host_fqdn=self.host_fqdn,
            host_rdns=self.host_rdns,
            mac_address=self.mac_address,
            known_ips=self.known_ips,
            operating_system=self.operating_system,
            parent_asset=self.parent_asset,
            ports=self.ports,
            tags=self.tags,
        )


@dataclass(slots=True)
class AssetCreateResult:
    asset_id: int | str | None = None
    status: str | None = None
    message: str | None = None
    raw: JsonDict | None = None

    @property
    def ok(self) -> bool:
        return _is_success_text(self.status) or _is_success_text(self.message)

    @classmethod
    def from_api(cls, data: JsonDict) -> AssetCreateResult:
        return cls(
            asset_id=data.get("asset_id") or data.get("id") or data.get("cuid"),
            status=data.get("status") or data.get("result"),
            message=data.get("message") or data.get("detail"),
            raw=dict(data),
        )


@dataclass(slots=True)
class Asset:
    id: str | None = None
    cuid: str | None = None
    name: str | None = None
    client_id: int | str | None = None
    type: AssetType | None = None
    criticality: AssetCriticality | None = None
    description: str | None = None
    hostname: str | None = None
    dns_name: str | None = None
    host_fqdn: str | None = None
    host_rdns: str | None = None
    mac_address: str | None = None
    known_ips: list[str] | None = None
    operating_system: list[str] | None = None
    parent_asset: ObjectReference | None = None
    ports: dict[str, Port] | None = None
    tags: list[str] | None = None
    doc_type: str | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> Asset:
        ports = data.get("ports")
        return cls(
            id=data.get("id"),
            cuid=data.get("cuid"),
            name=data.get("asset") or data.get("name"),
            client_id=data.get("client_id"),
            type=_asset_type(data.get("type")),
            criticality=_asset_criticality(data.get("assetCriticality")),
            description=data.get("description"),
            hostname=data.get("hostname"),
            dns_name=data.get("dns_name"),
            host_fqdn=data.get("host_fqdn"),
            host_rdns=data.get("host_rdns"),
            mac_address=data.get("mac_address"),
            known_ips=data.get("knownIps") if isinstance(data.get("knownIps"), list) else None,
            operating_system=data.get("operating_system")
            if isinstance(data.get("operating_system"), list)
            else None,
            parent_asset=ObjectReference.from_api(data.get("parent_asset")),
            ports={
                key: port
                for key, port in (
                    (key, Port.from_api(value))
                    for key, value in ports.items()
                    if isinstance(value, dict)
                )
                if port is not None
            }
            if isinstance(ports, dict)
            else None,
            tags=data.get("tags") if isinstance(data.get("tags"), list) else None,
            doc_type=data.get("doc_type"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        data = _asset_payload(
            name=self.name,
            type=self.type,
            criticality=self.criticality,
            description=self.description,
            hostname=self.hostname,
            dns_name=self.dns_name,
            host_fqdn=self.host_fqdn,
            host_rdns=self.host_rdns,
            mac_address=self.mac_address,
            known_ips=self.known_ips,
            operating_system=self.operating_system,
            parent_asset=self.parent_asset,
            ports=self.ports,
            tags=self.tags,
        )
        return {
            **clean(
                {
                    "id": self.id,
                    "cuid": self.cuid,
                    "client_id": self.client_id,
                    "doc_type": self.doc_type,
                }
            ),
            **data,
        }


@dataclass(slots=True)
class AssetPage:
    assets: list[Asset]
    total_count: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict | list[JsonDict]) -> AssetPage:
        if isinstance(data, list):
            return cls(
                assets=[Asset.from_api(item) for item in data if isinstance(item, dict)],
                raw={"data": data},
            )

        items = _first_list(data, ("assets", "data", "items", "results"))
        return cls(
            assets=[Asset.from_api(item) for item in items if isinstance(item, dict)],
            total_count=_first_int(data, ("total", "totalCount", "count")),
            raw=dict(data),
        )


@dataclass(slots=True)
class AffectedAsset(Asset):
    status: AffectedAssetStatus | None = None
    substatus: str | None = None
    substatus_cuid: str | None = None
    evidence: list[str] | None = None
    location_url: str | None = None
    vulnerable_parameters: list[VulnerableParameter] | None = None
    notes: str | None = None
    closed_at: str | int | None = None
    reopened_at: str | int | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AffectedAsset:
        asset = Asset.from_api(data)
        vulnerable_parameters = data.get("vulnerableParameters")
        return cls(
            id=asset.id,
            cuid=asset.cuid,
            name=asset.name,
            client_id=asset.client_id,
            type=asset.type,
            criticality=asset.criticality,
            description=asset.description,
            hostname=asset.hostname,
            dns_name=asset.dns_name,
            host_fqdn=asset.host_fqdn,
            host_rdns=asset.host_rdns,
            mac_address=asset.mac_address,
            known_ips=asset.known_ips,
            operating_system=asset.operating_system,
            parent_asset=asset.parent_asset,
            ports=asset.ports,
            tags=asset.tags,
            doc_type=asset.doc_type,
            status=_affected_asset_status(data.get("status")),
            substatus=data.get("subStatus"),
            substatus_cuid=data.get("substatusCuid"),
            evidence=data.get("evidence") if isinstance(data.get("evidence"), list) else None,
            location_url=data.get("locationUrl"),
            vulnerable_parameters=[
                parameter
                for parameter in (
                    VulnerableParameter.from_api(item) for item in vulnerable_parameters or []
                )
                if parameter is not None
            ]
            if isinstance(vulnerable_parameters, list)
            else None,
            notes=data.get("notes") if isinstance(data.get("notes"), str) else None,
            closed_at=data.get("closedAt"),
            reopened_at=data.get("reopenedAt"),
            raw=dict(data),
        )

    def to_api(self) -> JsonDict:
        data = self._asset_api()
        data.update(
            clean(
                {
                    "status": self.status.value if self.status is not None else None,
                    "subStatus": self.substatus,
                    "substatusCuid": self.substatus_cuid,
                    "evidence": self.evidence,
                    "locationUrl": self.location_url,
                    "vulnerableParameters": [
                        parameter.to_api() for parameter in self.vulnerable_parameters
                    ]
                    if self.vulnerable_parameters is not None
                    else None,
                    "notes": self.notes,
                    "closedAt": self.closed_at,
                    "reopenedAt": self.reopened_at,
                }
            )
        )
        return data

    def _asset_api(self) -> JsonDict:
        return super().to_api()


@dataclass(slots=True)
class AffectedAssetStatusUpdate:
    asset_id: int | str | None = None
    status: AffectedAssetStatus | None = None
    substatus: str | None = None
    assigned_to: str | None = None
    comment: str | None = None
    created_at: int | None = None
    raw: JsonDict | None = None

    @classmethod
    def from_api(cls, data: JsonDict) -> AffectedAssetStatusUpdate:
        return cls(
            asset_id=data.get("assetId") or data.get("asset_id") or data.get("id"),
            status=_affected_asset_status(data.get("status")),
            substatus=data.get("subStatus"),
            assigned_to=data.get("assignedTo"),
            comment=data.get("comment") or data.get("comments"),
            created_at=data.get("createdAt"),
            raw=dict(data),
        )

    def to_api(self, *, include_asset_id: bool = False) -> JsonDict:
        return clean(
            {
                "assetId": self.asset_id if include_asset_id else None,
                "status": self.status.value if self.status is not None else None,
                "subStatus": self.substatus,
                "assignedTo": self.assigned_to,
                "comment": self.comment,
            }
        )


@dataclass(slots=True)
class AffectedAssetStatusMap:
    statuses: dict[str, AffectedAssetStatusUpdate]
    raw: JsonDict | list[JsonDict] | None = None

    def __getitem__(self, asset_id: int | str) -> AffectedAssetStatusUpdate:
        return self.statuses[str(asset_id)]

    def get(self, asset_id: int | str) -> AffectedAssetStatusUpdate | None:
        return self.statuses.get(str(asset_id))

    def items(self) -> ItemsView[str, AffectedAssetStatusUpdate]:
        return self.statuses.items()

    def keys(self) -> KeysView[str]:
        return self.statuses.keys()

    def values(self) -> ValuesView[AffectedAssetStatusUpdate]:
        return self.statuses.values()

    def __contains__(self, asset_id: object) -> bool:
        return str(asset_id) in self.statuses

    def __len__(self) -> int:
        return len(self.statuses)

    @classmethod
    def from_api(cls, data: object) -> AffectedAssetStatusMap:
        if isinstance(data, dict):
            statuses: dict[str, AffectedAssetStatusUpdate] = {}
            for asset_id, value in data.items():
                if isinstance(value, dict):
                    update = AffectedAssetStatusUpdate.from_api(value)
                    update.asset_id = update.asset_id or asset_id
                    statuses[str(asset_id)] = update
            return cls(statuses=statuses, raw=dict(data))
        if isinstance(data, list):
            statuses = {
                str(update.asset_id): update
                for update in (
                    AffectedAssetStatusUpdate.from_api(item)
                    for item in data
                    if isinstance(item, dict)
                )
                if update.asset_id is not None
            }
            return cls(statuses=statuses, raw=list(data))
        return cls(statuses={}, raw={"data": data})


def _asset_payload(
    *,
    name: str | None = None,
    type: AssetType | None = None,
    criticality: AssetCriticality | None = None,
    description: str | None = None,
    hostname: str | None = None,
    dns_name: str | None = None,
    host_fqdn: str | None = None,
    host_rdns: str | None = None,
    mac_address: str | None = None,
    known_ips: list[str] | None = None,
    operating_system: list[str] | None = None,
    parent_asset: ObjectReference | None = None,
    ports: dict[str, Port] | None = None,
    tags: list[str] | None = None,
) -> JsonDict:
    return clean(
        {
            "asset": name,
            "type": type.value if type is not None else None,
            "assetCriticality": criticality.value if criticality is not None else None,
            "description": description,
            "hostname": hostname,
            "dns_name": dns_name,
            "host_fqdn": host_fqdn,
            "host_rdns": host_rdns,
            "mac_address": mac_address,
            "knownIps": known_ips,
            "operating_system": operating_system,
            "parent_asset": parent_asset.to_api() if parent_asset is not None else None,
            "ports": {key: port.to_api() for key, port in ports.items()}
            if ports is not None
            else None,
            "tags": tags,
        }
    )


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


def _affected_asset_status(value: object) -> AffectedAssetStatus | None:
    if isinstance(value, AffectedAssetStatus):
        return value
    if isinstance(value, str):
        try:
            return AffectedAssetStatus(value)
        except ValueError:
            return None
    return None


def _asset_type(value: object) -> AssetType | None:
    if isinstance(value, AssetType):
        return value
    if isinstance(value, str):
        try:
            return AssetType(value)
        except ValueError:
            return None
    return None


def _asset_criticality(value: object) -> AssetCriticality | None:
    if isinstance(value, AssetCriticality):
        return value
    if isinstance(value, str):
        try:
            return AssetCriticality(value)
        except ValueError:
            return None
    return None


def _is_success_text(value: object) -> bool:
    if not isinstance(value, str):
        return False
    return value.lower() in {
        "ok",
        "success",
        "successful",
        "created",
    }
