from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Condition(_message.Message):
    __slots__ = ('query_terms', 'active_time_range', 'query_regex')

    class QueryTerm(_message.Message):
        __slots__ = ('value', 'full_match')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        FULL_MATCH_FIELD_NUMBER: _ClassVar[int]
        value: str
        full_match: bool

        def __init__(self, value: _Optional[str]=..., full_match: bool=...) -> None:
            ...

    class TimeRange(_message.Message):
        __slots__ = ('start_time', 'end_time')
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp

        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    QUERY_TERMS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_REGEX_FIELD_NUMBER: _ClassVar[int]
    query_terms: _containers.RepeatedCompositeFieldContainer[Condition.QueryTerm]
    active_time_range: _containers.RepeatedCompositeFieldContainer[Condition.TimeRange]
    query_regex: str

    def __init__(self, query_terms: _Optional[_Iterable[_Union[Condition.QueryTerm, _Mapping]]]=..., active_time_range: _Optional[_Iterable[_Union[Condition.TimeRange, _Mapping]]]=..., query_regex: _Optional[str]=...) -> None:
        ...

class Control(_message.Message):
    __slots__ = ('boost_action', 'filter_action', 'redirect_action', 'synonyms_action', 'name', 'display_name', 'associated_serving_config_ids', 'solution_type', 'use_cases', 'conditions')

    class BoostAction(_message.Message):
        __slots__ = ('boost', 'filter', 'data_store')
        BOOST_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        DATA_STORE_FIELD_NUMBER: _ClassVar[int]
        boost: float
        filter: str
        data_store: str

        def __init__(self, boost: _Optional[float]=..., filter: _Optional[str]=..., data_store: _Optional[str]=...) -> None:
            ...

    class FilterAction(_message.Message):
        __slots__ = ('filter', 'data_store')
        FILTER_FIELD_NUMBER: _ClassVar[int]
        DATA_STORE_FIELD_NUMBER: _ClassVar[int]
        filter: str
        data_store: str

        def __init__(self, filter: _Optional[str]=..., data_store: _Optional[str]=...) -> None:
            ...

    class RedirectAction(_message.Message):
        __slots__ = ('redirect_uri',)
        REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
        redirect_uri: str

        def __init__(self, redirect_uri: _Optional[str]=...) -> None:
            ...

    class SynonymsAction(_message.Message):
        __slots__ = ('synonyms',)
        SYNONYMS_FIELD_NUMBER: _ClassVar[int]
        synonyms: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, synonyms: _Optional[_Iterable[str]]=...) -> None:
            ...
    BOOST_ACTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_ACTION_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_ACTION_FIELD_NUMBER: _ClassVar[int]
    SYNONYMS_ACTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_SERVING_CONFIG_IDS_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_CASES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    boost_action: Control.BoostAction
    filter_action: Control.FilterAction
    redirect_action: Control.RedirectAction
    synonyms_action: Control.SynonymsAction
    name: str
    display_name: str
    associated_serving_config_ids: _containers.RepeatedScalarFieldContainer[str]
    solution_type: _common_pb2.SolutionType
    use_cases: _containers.RepeatedScalarFieldContainer[_common_pb2.SearchUseCase]
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]

    def __init__(self, boost_action: _Optional[_Union[Control.BoostAction, _Mapping]]=..., filter_action: _Optional[_Union[Control.FilterAction, _Mapping]]=..., redirect_action: _Optional[_Union[Control.RedirectAction, _Mapping]]=..., synonyms_action: _Optional[_Union[Control.SynonymsAction, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., associated_serving_config_ids: _Optional[_Iterable[str]]=..., solution_type: _Optional[_Union[_common_pb2.SolutionType, str]]=..., use_cases: _Optional[_Iterable[_Union[_common_pb2.SearchUseCase, str]]]=..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]]=...) -> None:
        ...