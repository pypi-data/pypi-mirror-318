from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubpropertyEventFilterCondition(_message.Message):
    __slots__ = ("null_filter", "string_filter", "field_name")
    class StringFilter(_message.Message):
        __slots__ = ("match_type", "value", "case_sensitive")
        class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MATCH_TYPE_UNSPECIFIED: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
            EXACT: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
            BEGINS_WITH: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
            ENDS_WITH: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
            CONTAINS: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
            FULL_REGEXP: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
            PARTIAL_REGEXP: _ClassVar[SubpropertyEventFilterCondition.StringFilter.MatchType]
        MATCH_TYPE_UNSPECIFIED: SubpropertyEventFilterCondition.StringFilter.MatchType
        EXACT: SubpropertyEventFilterCondition.StringFilter.MatchType
        BEGINS_WITH: SubpropertyEventFilterCondition.StringFilter.MatchType
        ENDS_WITH: SubpropertyEventFilterCondition.StringFilter.MatchType
        CONTAINS: SubpropertyEventFilterCondition.StringFilter.MatchType
        FULL_REGEXP: SubpropertyEventFilterCondition.StringFilter.MatchType
        PARTIAL_REGEXP: SubpropertyEventFilterCondition.StringFilter.MatchType
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        match_type: SubpropertyEventFilterCondition.StringFilter.MatchType
        value: str
        case_sensitive: bool
        def __init__(self, match_type: _Optional[_Union[SubpropertyEventFilterCondition.StringFilter.MatchType, str]] = ..., value: _Optional[str] = ..., case_sensitive: bool = ...) -> None: ...
    NULL_FILTER_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    null_filter: bool
    string_filter: SubpropertyEventFilterCondition.StringFilter
    field_name: str
    def __init__(self, null_filter: bool = ..., string_filter: _Optional[_Union[SubpropertyEventFilterCondition.StringFilter, _Mapping]] = ..., field_name: _Optional[str] = ...) -> None: ...

class SubpropertyEventFilterExpression(_message.Message):
    __slots__ = ("or_group", "not_expression", "filter_condition")
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    or_group: SubpropertyEventFilterExpressionList
    not_expression: SubpropertyEventFilterExpression
    filter_condition: SubpropertyEventFilterCondition
    def __init__(self, or_group: _Optional[_Union[SubpropertyEventFilterExpressionList, _Mapping]] = ..., not_expression: _Optional[_Union[SubpropertyEventFilterExpression, _Mapping]] = ..., filter_condition: _Optional[_Union[SubpropertyEventFilterCondition, _Mapping]] = ...) -> None: ...

class SubpropertyEventFilterExpressionList(_message.Message):
    __slots__ = ("filter_expressions",)
    FILTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    filter_expressions: _containers.RepeatedCompositeFieldContainer[SubpropertyEventFilterExpression]
    def __init__(self, filter_expressions: _Optional[_Iterable[_Union[SubpropertyEventFilterExpression, _Mapping]]] = ...) -> None: ...

class SubpropertyEventFilterClause(_message.Message):
    __slots__ = ("filter_clause_type", "filter_expression")
    class FilterClauseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILTER_CLAUSE_TYPE_UNSPECIFIED: _ClassVar[SubpropertyEventFilterClause.FilterClauseType]
        INCLUDE: _ClassVar[SubpropertyEventFilterClause.FilterClauseType]
        EXCLUDE: _ClassVar[SubpropertyEventFilterClause.FilterClauseType]
    FILTER_CLAUSE_TYPE_UNSPECIFIED: SubpropertyEventFilterClause.FilterClauseType
    INCLUDE: SubpropertyEventFilterClause.FilterClauseType
    EXCLUDE: SubpropertyEventFilterClause.FilterClauseType
    FILTER_CLAUSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    filter_clause_type: SubpropertyEventFilterClause.FilterClauseType
    filter_expression: SubpropertyEventFilterExpression
    def __init__(self, filter_clause_type: _Optional[_Union[SubpropertyEventFilterClause.FilterClauseType, str]] = ..., filter_expression: _Optional[_Union[SubpropertyEventFilterExpression, _Mapping]] = ...) -> None: ...

class SubpropertyEventFilter(_message.Message):
    __slots__ = ("name", "apply_to_property", "filter_clauses")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLY_TO_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    FILTER_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    name: str
    apply_to_property: str
    filter_clauses: _containers.RepeatedCompositeFieldContainer[SubpropertyEventFilterClause]
    def __init__(self, name: _Optional[str] = ..., apply_to_property: _Optional[str] = ..., filter_clauses: _Optional[_Iterable[_Union[SubpropertyEventFilterClause, _Mapping]]] = ...) -> None: ...
