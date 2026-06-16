from __future__ import annotations

from dataclasses import dataclass

from plextrac_api.types.common import (
    JsonDict,
    ObjectReference,
    Port,
    VulnerableParameter,
    clean,
)


@dataclass(slots=True)
class Asset:
    id: str | None = None
    cuid: str | None = None
    name: str | None = None
    client_id: int | str | None = None
    type: str | None = None
    criticality: str | None = None
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
            type=data.get("type"),
            criticality=data.get("assetCriticality"),
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
        return clean(
            {
                "id": self.id,
                "cuid": self.cuid,
                "asset": self.name,
                "client_id": self.client_id,
                "type": self.type,
                "assetCriticality": self.criticality,
                "description": self.description,
                "hostname": self.hostname,
                "dns_name": self.dns_name,
                "host_fqdn": self.host_fqdn,
                "host_rdns": self.host_rdns,
                "mac_address": self.mac_address,
                "knownIps": self.known_ips,
                "operating_system": self.operating_system,
                "parent_asset": self.parent_asset.to_api()
                if self.parent_asset is not None
                else None,
                "ports": {key: port.to_api() for key, port in self.ports.items()}
                if self.ports is not None
                else None,
                "tags": self.tags,
                "doc_type": self.doc_type,
            }
        )


@dataclass(slots=True)
class AffectedAsset(Asset):
    status: str | None = None
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
            status=data.get("status"),
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
                    "status": self.status,
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
