from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceFilterScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIENCE_FILTER_SCOPE_UNSPECIFIED: _ClassVar[AudienceFilterScope]
    AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT: _ClassVar[AudienceFilterScope]
    AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION: _ClassVar[AudienceFilterScope]
    AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS: _ClassVar[AudienceFilterScope]
AUDIENCE_FILTER_SCOPE_UNSPECIFIED: AudienceFilterScope
AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT: AudienceFilterScope
AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION: AudienceFilterScope
AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS: AudienceFilterScope

class AudienceDimensionOrMetricFilter(_message.Message):
    __slots__ = ('string_filter', 'in_list_filter', 'numeric_filter', 'between_filter', 'field_name', 'at_any_point_in_time', 'in_any_n_day_period')

    class StringFilter(_message.Message):
        __slots__ = ('match_type', 'value', 'case_sensitive')

        class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MATCH_TYPE_UNSPECIFIED: _ClassVar[AudienceDimensionOrMetricFilter.StringFilter.MatchType]
            EXACT: _ClassVar[AudienceDimensionOrMetricFilter.StringFilter.MatchType]
            BEGINS_WITH: _ClassVar[AudienceDimensionOrMetricFilter.StringFilter.MatchType]
            ENDS_WITH: _ClassVar[AudienceDimensionOrMetricFilter.StringFilter.MatchType]
            CONTAINS: _ClassVar[AudienceDimensionOrMetricFilter.StringFilter.MatchType]
            FULL_REGEXP: _ClassVar[AudienceDimensionOrMetricFilter.StringFilter.MatchType]
        MATCH_TYPE_UNSPECIFIED: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        EXACT: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        BEGINS_WITH: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        ENDS_WITH: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        CONTAINS: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        FULL_REGEXP: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        match_type: AudienceDimensionOrMetricFilter.StringFilter.MatchType
        value: str
        case_sensitive: bool

        def __init__(self, match_type: _Optional[_Union[AudienceDimensionOrMetricFilter.StringFilter.MatchType, str]]=..., value: _Optional[str]=..., case_sensitive: bool=...) -> None:
            ...

    class InListFilter(_message.Message):
        __slots__ = ('values', 'case_sensitive')
        VALUES_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        case_sensitive: bool

        def __init__(self, values: _Optional[_Iterable[str]]=..., case_sensitive: bool=...) -> None:
            ...

    class NumericValue(_message.Message):
        __slots__ = ('int64_value', 'double_value')
        INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        int64_value: int
        double_value: float

        def __init__(self, int64_value: _Optional[int]=..., double_value: _Optional[float]=...) -> None:
            ...

    class NumericFilter(_message.Message):
        __slots__ = ('operation', 'value')

        class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATION_UNSPECIFIED: _ClassVar[AudienceDimensionOrMetricFilter.NumericFilter.Operation]
            EQUAL: _ClassVar[AudienceDimensionOrMetricFilter.NumericFilter.Operation]
            LESS_THAN: _ClassVar[AudienceDimensionOrMetricFilter.NumericFilter.Operation]
            GREATER_THAN: _ClassVar[AudienceDimensionOrMetricFilter.NumericFilter.Operation]
        OPERATION_UNSPECIFIED: AudienceDimensionOrMetricFilter.NumericFilter.Operation
        EQUAL: AudienceDimensionOrMetricFilter.NumericFilter.Operation
        LESS_THAN: AudienceDimensionOrMetricFilter.NumericFilter.Operation
        GREATER_THAN: AudienceDimensionOrMetricFilter.NumericFilter.Operation
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operation: AudienceDimensionOrMetricFilter.NumericFilter.Operation
        value: AudienceDimensionOrMetricFilter.NumericValue

        def __init__(self, operation: _Optional[_Union[AudienceDimensionOrMetricFilter.NumericFilter.Operation, str]]=..., value: _Optional[_Union[AudienceDimensionOrMetricFilter.NumericValue, _Mapping]]=...) -> None:
            ...

    class BetweenFilter(_message.Message):
        __slots__ = ('from_value', 'to_value')
        FROM_VALUE_FIELD_NUMBER: _ClassVar[int]
        TO_VALUE_FIELD_NUMBER: _ClassVar[int]
        from_value: AudienceDimensionOrMetricFilter.NumericValue
        to_value: AudienceDimensionOrMetricFilter.NumericValue

        def __init__(self, from_value: _Optional[_Union[AudienceDimensionOrMetricFilter.NumericValue, _Mapping]]=..., to_value: _Optional[_Union[AudienceDimensionOrMetricFilter.NumericValue, _Mapping]]=...) -> None:
            ...
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    AT_ANY_POINT_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    IN_ANY_N_DAY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    string_filter: AudienceDimensionOrMetricFilter.StringFilter
    in_list_filter: AudienceDimensionOrMetricFilter.InListFilter
    numeric_filter: AudienceDimensionOrMetricFilter.NumericFilter
    between_filter: AudienceDimensionOrMetricFilter.BetweenFilter
    field_name: str
    at_any_point_in_time: bool
    in_any_n_day_period: int

    def __init__(self, string_filter: _Optional[_Union[AudienceDimensionOrMetricFilter.StringFilter, _Mapping]]=..., in_list_filter: _Optional[_Union[AudienceDimensionOrMetricFilter.InListFilter, _Mapping]]=..., numeric_filter: _Optional[_Union[AudienceDimensionOrMetricFilter.NumericFilter, _Mapping]]=..., between_filter: _Optional[_Union[AudienceDimensionOrMetricFilter.BetweenFilter, _Mapping]]=..., field_name: _Optional[str]=..., at_any_point_in_time: bool=..., in_any_n_day_period: _Optional[int]=...) -> None:
        ...

class AudienceEventFilter(_message.Message):
    __slots__ = ('event_name', 'event_parameter_filter_expression')
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_PARAMETER_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_parameter_filter_expression: AudienceFilterExpression

    def __init__(self, event_name: _Optional[str]=..., event_parameter_filter_expression: _Optional[_Union[AudienceFilterExpression, _Mapping]]=...) -> None:
        ...

class AudienceFilterExpression(_message.Message):
    __slots__ = ('and_group', 'or_group', 'not_expression', 'dimension_or_metric_filter', 'event_filter')
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_OR_METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: AudienceFilterExpressionList
    or_group: AudienceFilterExpressionList
    not_expression: AudienceFilterExpression
    dimension_or_metric_filter: AudienceDimensionOrMetricFilter
    event_filter: AudienceEventFilter

    def __init__(self, and_group: _Optional[_Union[AudienceFilterExpressionList, _Mapping]]=..., or_group: _Optional[_Union[AudienceFilterExpressionList, _Mapping]]=..., not_expression: _Optional[_Union[AudienceFilterExpression, _Mapping]]=..., dimension_or_metric_filter: _Optional[_Union[AudienceDimensionOrMetricFilter, _Mapping]]=..., event_filter: _Optional[_Union[AudienceEventFilter, _Mapping]]=...) -> None:
        ...

class AudienceFilterExpressionList(_message.Message):
    __slots__ = ('filter_expressions',)
    FILTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    filter_expressions: _containers.RepeatedCompositeFieldContainer[AudienceFilterExpression]

    def __init__(self, filter_expressions: _Optional[_Iterable[_Union[AudienceFilterExpression, _Mapping]]]=...) -> None:
        ...

class AudienceSimpleFilter(_message.Message):
    __slots__ = ('scope', 'filter_expression')
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    scope: AudienceFilterScope
    filter_expression: AudienceFilterExpression

    def __init__(self, scope: _Optional[_Union[AudienceFilterScope, str]]=..., filter_expression: _Optional[_Union[AudienceFilterExpression, _Mapping]]=...) -> None:
        ...

class AudienceSequenceFilter(_message.Message):
    __slots__ = ('scope', 'sequence_maximum_duration', 'sequence_steps')

    class AudienceSequenceStep(_message.Message):
        __slots__ = ('scope', 'immediately_follows', 'constraint_duration', 'filter_expression')
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        IMMEDIATELY_FOLLOWS_FIELD_NUMBER: _ClassVar[int]
        CONSTRAINT_DURATION_FIELD_NUMBER: _ClassVar[int]
        FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        scope: AudienceFilterScope
        immediately_follows: bool
        constraint_duration: _duration_pb2.Duration
        filter_expression: AudienceFilterExpression

        def __init__(self, scope: _Optional[_Union[AudienceFilterScope, str]]=..., immediately_follows: bool=..., constraint_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., filter_expression: _Optional[_Union[AudienceFilterExpression, _Mapping]]=...) -> None:
            ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_MAXIMUM_DURATION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_STEPS_FIELD_NUMBER: _ClassVar[int]
    scope: AudienceFilterScope
    sequence_maximum_duration: _duration_pb2.Duration
    sequence_steps: _containers.RepeatedCompositeFieldContainer[AudienceSequenceFilter.AudienceSequenceStep]

    def __init__(self, scope: _Optional[_Union[AudienceFilterScope, str]]=..., sequence_maximum_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., sequence_steps: _Optional[_Iterable[_Union[AudienceSequenceFilter.AudienceSequenceStep, _Mapping]]]=...) -> None:
        ...

class AudienceFilterClause(_message.Message):
    __slots__ = ('simple_filter', 'sequence_filter', 'clause_type')

    class AudienceClauseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIENCE_CLAUSE_TYPE_UNSPECIFIED: _ClassVar[AudienceFilterClause.AudienceClauseType]
        INCLUDE: _ClassVar[AudienceFilterClause.AudienceClauseType]
        EXCLUDE: _ClassVar[AudienceFilterClause.AudienceClauseType]
    AUDIENCE_CLAUSE_TYPE_UNSPECIFIED: AudienceFilterClause.AudienceClauseType
    INCLUDE: AudienceFilterClause.AudienceClauseType
    EXCLUDE: AudienceFilterClause.AudienceClauseType
    SIMPLE_FILTER_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CLAUSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    simple_filter: AudienceSimpleFilter
    sequence_filter: AudienceSequenceFilter
    clause_type: AudienceFilterClause.AudienceClauseType

    def __init__(self, simple_filter: _Optional[_Union[AudienceSimpleFilter, _Mapping]]=..., sequence_filter: _Optional[_Union[AudienceSequenceFilter, _Mapping]]=..., clause_type: _Optional[_Union[AudienceFilterClause.AudienceClauseType, str]]=...) -> None:
        ...

class AudienceEventTrigger(_message.Message):
    __slots__ = ('event_name', 'log_condition')

    class LogCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_CONDITION_UNSPECIFIED: _ClassVar[AudienceEventTrigger.LogCondition]
        AUDIENCE_JOINED: _ClassVar[AudienceEventTrigger.LogCondition]
        AUDIENCE_MEMBERSHIP_RENEWED: _ClassVar[AudienceEventTrigger.LogCondition]
    LOG_CONDITION_UNSPECIFIED: AudienceEventTrigger.LogCondition
    AUDIENCE_JOINED: AudienceEventTrigger.LogCondition
    AUDIENCE_MEMBERSHIP_RENEWED: AudienceEventTrigger.LogCondition
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_CONDITION_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    log_condition: AudienceEventTrigger.LogCondition

    def __init__(self, event_name: _Optional[str]=..., log_condition: _Optional[_Union[AudienceEventTrigger.LogCondition, str]]=...) -> None:
        ...

class Audience(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'membership_duration_days', 'ads_personalization_enabled', 'event_trigger', 'exclusion_duration_mode', 'filter_clauses', 'create_time')

    class AudienceExclusionDurationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED: _ClassVar[Audience.AudienceExclusionDurationMode]
        EXCLUDE_TEMPORARILY: _ClassVar[Audience.AudienceExclusionDurationMode]
        EXCLUDE_PERMANENTLY: _ClassVar[Audience.AudienceExclusionDurationMode]
    AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED: Audience.AudienceExclusionDurationMode
    EXCLUDE_TEMPORARILY: Audience.AudienceExclusionDurationMode
    EXCLUDE_PERMANENTLY: Audience.AudienceExclusionDurationMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_DURATION_DAYS_FIELD_NUMBER: _ClassVar[int]
    ADS_PERSONALIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_DURATION_MODE_FIELD_NUMBER: _ClassVar[int]
    FILTER_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    membership_duration_days: int
    ads_personalization_enabled: bool
    event_trigger: AudienceEventTrigger
    exclusion_duration_mode: Audience.AudienceExclusionDurationMode
    filter_clauses: _containers.RepeatedCompositeFieldContainer[AudienceFilterClause]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., membership_duration_days: _Optional[int]=..., ads_personalization_enabled: bool=..., event_trigger: _Optional[_Union[AudienceEventTrigger, _Mapping]]=..., exclusion_duration_mode: _Optional[_Union[Audience.AudienceExclusionDurationMode, str]]=..., filter_clauses: _Optional[_Iterable[_Union[AudienceFilterClause, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...