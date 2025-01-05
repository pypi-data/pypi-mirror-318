from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExpandedDataSetFilter(_message.Message):
    __slots__ = ('string_filter', 'in_list_filter', 'field_name')

    class StringFilter(_message.Message):
        __slots__ = ('match_type', 'value', 'case_sensitive')

        class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MATCH_TYPE_UNSPECIFIED: _ClassVar[ExpandedDataSetFilter.StringFilter.MatchType]
            EXACT: _ClassVar[ExpandedDataSetFilter.StringFilter.MatchType]
            CONTAINS: _ClassVar[ExpandedDataSetFilter.StringFilter.MatchType]
        MATCH_TYPE_UNSPECIFIED: ExpandedDataSetFilter.StringFilter.MatchType
        EXACT: ExpandedDataSetFilter.StringFilter.MatchType
        CONTAINS: ExpandedDataSetFilter.StringFilter.MatchType
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        match_type: ExpandedDataSetFilter.StringFilter.MatchType
        value: str
        case_sensitive: bool

        def __init__(self, match_type: _Optional[_Union[ExpandedDataSetFilter.StringFilter.MatchType, str]]=..., value: _Optional[str]=..., case_sensitive: bool=...) -> None:
            ...

    class InListFilter(_message.Message):
        __slots__ = ('values', 'case_sensitive')
        VALUES_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        case_sensitive: bool

        def __init__(self, values: _Optional[_Iterable[str]]=..., case_sensitive: bool=...) -> None:
            ...
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    string_filter: ExpandedDataSetFilter.StringFilter
    in_list_filter: ExpandedDataSetFilter.InListFilter
    field_name: str

    def __init__(self, string_filter: _Optional[_Union[ExpandedDataSetFilter.StringFilter, _Mapping]]=..., in_list_filter: _Optional[_Union[ExpandedDataSetFilter.InListFilter, _Mapping]]=..., field_name: _Optional[str]=...) -> None:
        ...

class ExpandedDataSetFilterExpression(_message.Message):
    __slots__ = ('and_group', 'not_expression', 'filter')
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: ExpandedDataSetFilterExpressionList
    not_expression: ExpandedDataSetFilterExpression
    filter: ExpandedDataSetFilter

    def __init__(self, and_group: _Optional[_Union[ExpandedDataSetFilterExpressionList, _Mapping]]=..., not_expression: _Optional[_Union[ExpandedDataSetFilterExpression, _Mapping]]=..., filter: _Optional[_Union[ExpandedDataSetFilter, _Mapping]]=...) -> None:
        ...

class ExpandedDataSetFilterExpressionList(_message.Message):
    __slots__ = ('filter_expressions',)
    FILTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    filter_expressions: _containers.RepeatedCompositeFieldContainer[ExpandedDataSetFilterExpression]

    def __init__(self, filter_expressions: _Optional[_Iterable[_Union[ExpandedDataSetFilterExpression, _Mapping]]]=...) -> None:
        ...

class ExpandedDataSet(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'dimension_names', 'metric_names', 'dimension_filter_expression', 'data_collection_start_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_NAMES_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECTION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    dimension_names: _containers.RepeatedScalarFieldContainer[str]
    metric_names: _containers.RepeatedScalarFieldContainer[str]
    dimension_filter_expression: ExpandedDataSetFilterExpression
    data_collection_start_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., dimension_names: _Optional[_Iterable[str]]=..., metric_names: _Optional[_Iterable[str]]=..., dimension_filter_expression: _Optional[_Union[ExpandedDataSetFilterExpression, _Mapping]]=..., data_collection_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...