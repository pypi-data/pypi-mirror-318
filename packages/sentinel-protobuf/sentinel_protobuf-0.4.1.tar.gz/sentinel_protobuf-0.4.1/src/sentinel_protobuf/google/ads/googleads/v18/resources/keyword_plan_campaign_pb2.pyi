from google.ads.googleads.v18.enums import keyword_plan_network_pb2 as _keyword_plan_network_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanCampaign(_message.Message):
    __slots__ = ("resource_name", "keyword_plan", "id", "name", "language_constants", "keyword_plan_network", "cpc_bid_micros", "geo_targets")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_PLAN_NETWORK_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGETS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    keyword_plan: str
    id: int
    name: str
    language_constants: _containers.RepeatedScalarFieldContainer[str]
    keyword_plan_network: _keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork
    cpc_bid_micros: int
    geo_targets: _containers.RepeatedCompositeFieldContainer[KeywordPlanGeoTarget]
    def __init__(self, resource_name: _Optional[str] = ..., keyword_plan: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., language_constants: _Optional[_Iterable[str]] = ..., keyword_plan_network: _Optional[_Union[_keyword_plan_network_pb2.KeywordPlanNetworkEnum.KeywordPlanNetwork, str]] = ..., cpc_bid_micros: _Optional[int] = ..., geo_targets: _Optional[_Iterable[_Union[KeywordPlanGeoTarget, _Mapping]]] = ...) -> None: ...

class KeywordPlanGeoTarget(_message.Message):
    __slots__ = ("geo_target_constant",)
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    geo_target_constant: str
    def __init__(self, geo_target_constant: _Optional[str] = ...) -> None: ...
