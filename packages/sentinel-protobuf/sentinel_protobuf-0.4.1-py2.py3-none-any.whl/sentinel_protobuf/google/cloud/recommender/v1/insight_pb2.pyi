from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Insight(_message.Message):
    __slots__ = ('name', 'description', 'target_resources', 'insight_subtype', 'content', 'last_refresh_time', 'observation_period', 'state_info', 'category', 'severity', 'etag', 'associated_recommendations')

    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Insight.Category]
        COST: _ClassVar[Insight.Category]
        SECURITY: _ClassVar[Insight.Category]
        PERFORMANCE: _ClassVar[Insight.Category]
        MANAGEABILITY: _ClassVar[Insight.Category]
        SUSTAINABILITY: _ClassVar[Insight.Category]
        RELIABILITY: _ClassVar[Insight.Category]
    CATEGORY_UNSPECIFIED: Insight.Category
    COST: Insight.Category
    SECURITY: Insight.Category
    PERFORMANCE: Insight.Category
    MANAGEABILITY: Insight.Category
    SUSTAINABILITY: Insight.Category
    RELIABILITY: Insight.Category

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Insight.Severity]
        LOW: _ClassVar[Insight.Severity]
        MEDIUM: _ClassVar[Insight.Severity]
        HIGH: _ClassVar[Insight.Severity]
        CRITICAL: _ClassVar[Insight.Severity]
    SEVERITY_UNSPECIFIED: Insight.Severity
    LOW: Insight.Severity
    MEDIUM: Insight.Severity
    HIGH: Insight.Severity
    CRITICAL: Insight.Severity

    class RecommendationReference(_message.Message):
        __slots__ = ('recommendation',)
        RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
        recommendation: str

        def __init__(self, recommendation: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    target_resources: _containers.RepeatedScalarFieldContainer[str]
    insight_subtype: str
    content: _struct_pb2.Struct
    last_refresh_time: _timestamp_pb2.Timestamp
    observation_period: _duration_pb2.Duration
    state_info: InsightStateInfo
    category: Insight.Category
    severity: Insight.Severity
    etag: str
    associated_recommendations: _containers.RepeatedCompositeFieldContainer[Insight.RecommendationReference]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., target_resources: _Optional[_Iterable[str]]=..., insight_subtype: _Optional[str]=..., content: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., last_refresh_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., observation_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., state_info: _Optional[_Union[InsightStateInfo, _Mapping]]=..., category: _Optional[_Union[Insight.Category, str]]=..., severity: _Optional[_Union[Insight.Severity, str]]=..., etag: _Optional[str]=..., associated_recommendations: _Optional[_Iterable[_Union[Insight.RecommendationReference, _Mapping]]]=...) -> None:
        ...

class InsightStateInfo(_message.Message):
    __slots__ = ('state', 'state_metadata')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[InsightStateInfo.State]
        ACTIVE: _ClassVar[InsightStateInfo.State]
        ACCEPTED: _ClassVar[InsightStateInfo.State]
        DISMISSED: _ClassVar[InsightStateInfo.State]
    STATE_UNSPECIFIED: InsightStateInfo.State
    ACTIVE: InsightStateInfo.State
    ACCEPTED: InsightStateInfo.State
    DISMISSED: InsightStateInfo.State

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
    state: InsightStateInfo.State
    state_metadata: _containers.ScalarMap[str, str]

    def __init__(self, state: _Optional[_Union[InsightStateInfo.State, str]]=..., state_metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...