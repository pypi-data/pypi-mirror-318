from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ChannelGroupFilter(_message.Message):
    __slots__ = ('string_filter', 'in_list_filter', 'field_name')

    class StringFilter(_message.Message):
        __slots__ = ('match_type', 'value')

        class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MATCH_TYPE_UNSPECIFIED: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
            EXACT: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
            BEGINS_WITH: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
            ENDS_WITH: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
            CONTAINS: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
            FULL_REGEXP: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
            PARTIAL_REGEXP: _ClassVar[ChannelGroupFilter.StringFilter.MatchType]
        MATCH_TYPE_UNSPECIFIED: ChannelGroupFilter.StringFilter.MatchType
        EXACT: ChannelGroupFilter.StringFilter.MatchType
        BEGINS_WITH: ChannelGroupFilter.StringFilter.MatchType
        ENDS_WITH: ChannelGroupFilter.StringFilter.MatchType
        CONTAINS: ChannelGroupFilter.StringFilter.MatchType
        FULL_REGEXP: ChannelGroupFilter.StringFilter.MatchType
        PARTIAL_REGEXP: ChannelGroupFilter.StringFilter.MatchType
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        match_type: ChannelGroupFilter.StringFilter.MatchType
        value: str

        def __init__(self, match_type: _Optional[_Union[ChannelGroupFilter.StringFilter.MatchType, str]]=..., value: _Optional[str]=...) -> None:
            ...

    class InListFilter(_message.Message):
        __slots__ = ('values',)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
            ...
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    string_filter: ChannelGroupFilter.StringFilter
    in_list_filter: ChannelGroupFilter.InListFilter
    field_name: str

    def __init__(self, string_filter: _Optional[_Union[ChannelGroupFilter.StringFilter, _Mapping]]=..., in_list_filter: _Optional[_Union[ChannelGroupFilter.InListFilter, _Mapping]]=..., field_name: _Optional[str]=...) -> None:
        ...

class ChannelGroupFilterExpression(_message.Message):
    __slots__ = ('and_group', 'or_group', 'not_expression', 'filter')
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: ChannelGroupFilterExpressionList
    or_group: ChannelGroupFilterExpressionList
    not_expression: ChannelGroupFilterExpression
    filter: ChannelGroupFilter

    def __init__(self, and_group: _Optional[_Union[ChannelGroupFilterExpressionList, _Mapping]]=..., or_group: _Optional[_Union[ChannelGroupFilterExpressionList, _Mapping]]=..., not_expression: _Optional[_Union[ChannelGroupFilterExpression, _Mapping]]=..., filter: _Optional[_Union[ChannelGroupFilter, _Mapping]]=...) -> None:
        ...

class ChannelGroupFilterExpressionList(_message.Message):
    __slots__ = ('filter_expressions',)
    FILTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    filter_expressions: _containers.RepeatedCompositeFieldContainer[ChannelGroupFilterExpression]

    def __init__(self, filter_expressions: _Optional[_Iterable[_Union[ChannelGroupFilterExpression, _Mapping]]]=...) -> None:
        ...

class GroupingRule(_message.Message):
    __slots__ = ('display_name', 'expression')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    expression: ChannelGroupFilterExpression

    def __init__(self, display_name: _Optional[str]=..., expression: _Optional[_Union[ChannelGroupFilterExpression, _Mapping]]=...) -> None:
        ...

class ChannelGroup(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'grouping_rule', 'system_defined', 'primary')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUPING_RULE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_DEFINED_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    grouping_rule: _containers.RepeatedCompositeFieldContainer[GroupingRule]
    system_defined: bool
    primary: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., grouping_rule: _Optional[_Iterable[_Union[GroupingRule, _Mapping]]]=..., system_defined: bool=..., primary: bool=...) -> None:
        ...