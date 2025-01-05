from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DomainCategory(_message.Message):
    __slots__ = ("resource_name", "campaign", "category", "language_code", "domain", "coverage_fraction", "category_rank", "has_children", "recommended_cpc_bid_micros")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_RANK_FIELD_NUMBER: _ClassVar[int]
    HAS_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    category: str
    language_code: str
    domain: str
    coverage_fraction: float
    category_rank: int
    has_children: bool
    recommended_cpc_bid_micros: int
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., category: _Optional[str] = ..., language_code: _Optional[str] = ..., domain: _Optional[str] = ..., coverage_fraction: _Optional[float] = ..., category_rank: _Optional[int] = ..., has_children: bool = ..., recommended_cpc_bid_micros: _Optional[int] = ...) -> None: ...
