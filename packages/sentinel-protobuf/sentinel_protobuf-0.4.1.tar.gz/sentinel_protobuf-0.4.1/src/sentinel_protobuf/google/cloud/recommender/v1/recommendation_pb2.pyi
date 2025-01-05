from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Recommendation(_message.Message):
    __slots__ = ('name', 'description', 'recommender_subtype', 'last_refresh_time', 'primary_impact', 'additional_impact', 'priority', 'content', 'state_info', 'etag', 'associated_insights', 'xor_group_id')

    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIORITY_UNSPECIFIED: _ClassVar[Recommendation.Priority]
        P4: _ClassVar[Recommendation.Priority]
        P3: _ClassVar[Recommendation.Priority]
        P2: _ClassVar[Recommendation.Priority]
        P1: _ClassVar[Recommendation.Priority]
    PRIORITY_UNSPECIFIED: Recommendation.Priority
    P4: Recommendation.Priority
    P3: Recommendation.Priority
    P2: Recommendation.Priority
    P1: Recommendation.Priority

    class InsightReference(_message.Message):
        __slots__ = ('insight',)
        INSIGHT_FIELD_NUMBER: _ClassVar[int]
        insight: str

        def __init__(self, insight: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDER_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_IMPACT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_IMPACT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    XOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    recommender_subtype: str
    last_refresh_time: _timestamp_pb2.Timestamp
    primary_impact: Impact
    additional_impact: _containers.RepeatedCompositeFieldContainer[Impact]
    priority: Recommendation.Priority
    content: RecommendationContent
    state_info: RecommendationStateInfo
    etag: str
    associated_insights: _containers.RepeatedCompositeFieldContainer[Recommendation.InsightReference]
    xor_group_id: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., recommender_subtype: _Optional[str]=..., last_refresh_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., primary_impact: _Optional[_Union[Impact, _Mapping]]=..., additional_impact: _Optional[_Iterable[_Union[Impact, _Mapping]]]=..., priority: _Optional[_Union[Recommendation.Priority, str]]=..., content: _Optional[_Union[RecommendationContent, _Mapping]]=..., state_info: _Optional[_Union[RecommendationStateInfo, _Mapping]]=..., etag: _Optional[str]=..., associated_insights: _Optional[_Iterable[_Union[Recommendation.InsightReference, _Mapping]]]=..., xor_group_id: _Optional[str]=...) -> None:
        ...

class RecommendationContent(_message.Message):
    __slots__ = ('operation_groups', 'overview')
    OPERATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    operation_groups: _containers.RepeatedCompositeFieldContainer[OperationGroup]
    overview: _struct_pb2.Struct

    def __init__(self, operation_groups: _Optional[_Iterable[_Union[OperationGroup, _Mapping]]]=..., overview: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class OperationGroup(_message.Message):
    __slots__ = ('operations',)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[Operation]

    def __init__(self, operations: _Optional[_Iterable[_Union[Operation, _Mapping]]]=...) -> None:
        ...

class Operation(_message.Message):
    __slots__ = ('action', 'resource_type', 'resource', 'path', 'source_resource', 'source_path', 'value', 'value_matcher', 'path_filters', 'path_value_matchers')

    class PathFiltersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...

    class PathValueMatchersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ValueMatcher

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ValueMatcher, _Mapping]]=...) -> None:
            ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    PATH_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PATH_VALUE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    action: str
    resource_type: str
    resource: str
    path: str
    source_resource: str
    source_path: str
    value: _struct_pb2.Value
    value_matcher: ValueMatcher
    path_filters: _containers.MessageMap[str, _struct_pb2.Value]
    path_value_matchers: _containers.MessageMap[str, ValueMatcher]

    def __init__(self, action: _Optional[str]=..., resource_type: _Optional[str]=..., resource: _Optional[str]=..., path: _Optional[str]=..., source_resource: _Optional[str]=..., source_path: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., value_matcher: _Optional[_Union[ValueMatcher, _Mapping]]=..., path_filters: _Optional[_Mapping[str, _struct_pb2.Value]]=..., path_value_matchers: _Optional[_Mapping[str, ValueMatcher]]=...) -> None:
        ...

class ValueMatcher(_message.Message):
    __slots__ = ('matches_pattern',)
    MATCHES_PATTERN_FIELD_NUMBER: _ClassVar[int]
    matches_pattern: str

    def __init__(self, matches_pattern: _Optional[str]=...) -> None:
        ...

class CostProjection(_message.Message):
    __slots__ = ('cost', 'duration', 'cost_in_local_currency')
    COST_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COST_IN_LOCAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    cost: _money_pb2.Money
    duration: _duration_pb2.Duration
    cost_in_local_currency: _money_pb2.Money

    def __init__(self, cost: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., cost_in_local_currency: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
        ...

class SecurityProjection(_message.Message):
    __slots__ = ('details',)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _struct_pb2.Struct

    def __init__(self, details: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class SustainabilityProjection(_message.Message):
    __slots__ = ('kg_c_o2e', 'duration')
    KG_C_O2E_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    kg_c_o2e: float
    duration: _duration_pb2.Duration

    def __init__(self, kg_c_o2e: _Optional[float]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ReliabilityProjection(_message.Message):
    __slots__ = ('risks', 'details')

    class RiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RISK_TYPE_UNSPECIFIED: _ClassVar[ReliabilityProjection.RiskType]
        SERVICE_DISRUPTION: _ClassVar[ReliabilityProjection.RiskType]
        DATA_LOSS: _ClassVar[ReliabilityProjection.RiskType]
        ACCESS_DENY: _ClassVar[ReliabilityProjection.RiskType]
    RISK_TYPE_UNSPECIFIED: ReliabilityProjection.RiskType
    SERVICE_DISRUPTION: ReliabilityProjection.RiskType
    DATA_LOSS: ReliabilityProjection.RiskType
    ACCESS_DENY: ReliabilityProjection.RiskType
    RISKS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    risks: _containers.RepeatedScalarFieldContainer[ReliabilityProjection.RiskType]
    details: _struct_pb2.Struct

    def __init__(self, risks: _Optional[_Iterable[_Union[ReliabilityProjection.RiskType, str]]]=..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class Impact(_message.Message):
    __slots__ = ('category', 'cost_projection', 'security_projection', 'sustainability_projection', 'reliability_projection')

    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Impact.Category]
        COST: _ClassVar[Impact.Category]
        SECURITY: _ClassVar[Impact.Category]
        PERFORMANCE: _ClassVar[Impact.Category]
        MANAGEABILITY: _ClassVar[Impact.Category]
        SUSTAINABILITY: _ClassVar[Impact.Category]
        RELIABILITY: _ClassVar[Impact.Category]
    CATEGORY_UNSPECIFIED: Impact.Category
    COST: Impact.Category
    SECURITY: Impact.Category
    PERFORMANCE: Impact.Category
    MANAGEABILITY: Impact.Category
    SUSTAINABILITY: Impact.Category
    RELIABILITY: Impact.Category
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    COST_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    SUSTAINABILITY_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    RELIABILITY_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    category: Impact.Category
    cost_projection: CostProjection
    security_projection: SecurityProjection
    sustainability_projection: SustainabilityProjection
    reliability_projection: ReliabilityProjection

    def __init__(self, category: _Optional[_Union[Impact.Category, str]]=..., cost_projection: _Optional[_Union[CostProjection, _Mapping]]=..., security_projection: _Optional[_Union[SecurityProjection, _Mapping]]=..., sustainability_projection: _Optional[_Union[SustainabilityProjection, _Mapping]]=..., reliability_projection: _Optional[_Union[ReliabilityProjection, _Mapping]]=...) -> None:
        ...

class RecommendationStateInfo(_message.Message):
    __slots__ = ('state', 'state_metadata')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RecommendationStateInfo.State]
        ACTIVE: _ClassVar[RecommendationStateInfo.State]
        CLAIMED: _ClassVar[RecommendationStateInfo.State]
        SUCCEEDED: _ClassVar[RecommendationStateInfo.State]
        FAILED: _ClassVar[RecommendationStateInfo.State]
        DISMISSED: _ClassVar[RecommendationStateInfo.State]
    STATE_UNSPECIFIED: RecommendationStateInfo.State
    ACTIVE: RecommendationStateInfo.State
    CLAIMED: RecommendationStateInfo.State
    SUCCEEDED: RecommendationStateInfo.State
    FAILED: RecommendationStateInfo.State
    DISMISSED: RecommendationStateInfo.State

    class StateMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    state: RecommendationStateInfo.State
    state_metadata: _containers.ScalarMap[str, str]

    def __init__(self, state: _Optional[_Union[RecommendationStateInfo.State, str]]=..., state_metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...