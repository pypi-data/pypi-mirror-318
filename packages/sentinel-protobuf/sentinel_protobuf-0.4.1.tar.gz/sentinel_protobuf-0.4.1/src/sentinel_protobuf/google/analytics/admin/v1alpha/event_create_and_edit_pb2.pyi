from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ParameterMutation(_message.Message):
    __slots__ = ('parameter', 'parameter_value')
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VALUE_FIELD_NUMBER: _ClassVar[int]
    parameter: str
    parameter_value: str

    def __init__(self, parameter: _Optional[str]=..., parameter_value: _Optional[str]=...) -> None:
        ...

class EventCreateRule(_message.Message):
    __slots__ = ('name', 'destination_event', 'event_conditions', 'source_copy_parameters', 'parameter_mutations')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_COPY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_event: str
    event_conditions: _containers.RepeatedCompositeFieldContainer[MatchingCondition]
    source_copy_parameters: bool
    parameter_mutations: _containers.RepeatedCompositeFieldContainer[ParameterMutation]

    def __init__(self, name: _Optional[str]=..., destination_event: _Optional[str]=..., event_conditions: _Optional[_Iterable[_Union[MatchingCondition, _Mapping]]]=..., source_copy_parameters: bool=..., parameter_mutations: _Optional[_Iterable[_Union[ParameterMutation, _Mapping]]]=...) -> None:
        ...

class EventEditRule(_message.Message):
    __slots__ = ('name', 'display_name', 'event_conditions', 'parameter_mutations', 'processing_order')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_ORDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    event_conditions: _containers.RepeatedCompositeFieldContainer[MatchingCondition]
    parameter_mutations: _containers.RepeatedCompositeFieldContainer[ParameterMutation]
    processing_order: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., event_conditions: _Optional[_Iterable[_Union[MatchingCondition, _Mapping]]]=..., parameter_mutations: _Optional[_Iterable[_Union[ParameterMutation, _Mapping]]]=..., processing_order: _Optional[int]=...) -> None:
        ...

class MatchingCondition(_message.Message):
    __slots__ = ('field', 'comparison_type', 'value', 'negated')

    class ComparisonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPARISON_TYPE_UNSPECIFIED: _ClassVar[MatchingCondition.ComparisonType]
        EQUALS: _ClassVar[MatchingCondition.ComparisonType]
        EQUALS_CASE_INSENSITIVE: _ClassVar[MatchingCondition.ComparisonType]
        CONTAINS: _ClassVar[MatchingCondition.ComparisonType]
        CONTAINS_CASE_INSENSITIVE: _ClassVar[MatchingCondition.ComparisonType]
        STARTS_WITH: _ClassVar[MatchingCondition.ComparisonType]
        STARTS_WITH_CASE_INSENSITIVE: _ClassVar[MatchingCondition.ComparisonType]
        ENDS_WITH: _ClassVar[MatchingCondition.ComparisonType]
        ENDS_WITH_CASE_INSENSITIVE: _ClassVar[MatchingCondition.ComparisonType]
        GREATER_THAN: _ClassVar[MatchingCondition.ComparisonType]
        GREATER_THAN_OR_EQUAL: _ClassVar[MatchingCondition.ComparisonType]
        LESS_THAN: _ClassVar[MatchingCondition.ComparisonType]
        LESS_THAN_OR_EQUAL: _ClassVar[MatchingCondition.ComparisonType]
        REGULAR_EXPRESSION: _ClassVar[MatchingCondition.ComparisonType]
        REGULAR_EXPRESSION_CASE_INSENSITIVE: _ClassVar[MatchingCondition.ComparisonType]
    COMPARISON_TYPE_UNSPECIFIED: MatchingCondition.ComparisonType
    EQUALS: MatchingCondition.ComparisonType
    EQUALS_CASE_INSENSITIVE: MatchingCondition.ComparisonType
    CONTAINS: MatchingCondition.ComparisonType
    CONTAINS_CASE_INSENSITIVE: MatchingCondition.ComparisonType
    STARTS_WITH: MatchingCondition.ComparisonType
    STARTS_WITH_CASE_INSENSITIVE: MatchingCondition.ComparisonType
    ENDS_WITH: MatchingCondition.ComparisonType
    ENDS_WITH_CASE_INSENSITIVE: MatchingCondition.ComparisonType
    GREATER_THAN: MatchingCondition.ComparisonType
    GREATER_THAN_OR_EQUAL: MatchingCondition.ComparisonType
    LESS_THAN: MatchingCondition.ComparisonType
    LESS_THAN_OR_EQUAL: MatchingCondition.ComparisonType
    REGULAR_EXPRESSION: MatchingCondition.ComparisonType
    REGULAR_EXPRESSION_CASE_INSENSITIVE: MatchingCondition.ComparisonType
    FIELD_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    field: str
    comparison_type: MatchingCondition.ComparisonType
    value: str
    negated: bool

    def __init__(self, field: _Optional[str]=..., comparison_type: _Optional[_Union[MatchingCondition.ComparisonType, str]]=..., value: _Optional[str]=..., negated: bool=...) -> None:
        ...