from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccessDimension(_message.Message):
    __slots__ = ('dimension_name',)
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    dimension_name: str

    def __init__(self, dimension_name: _Optional[str]=...) -> None:
        ...

class AccessMetric(_message.Message):
    __slots__ = ('metric_name',)
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    metric_name: str

    def __init__(self, metric_name: _Optional[str]=...) -> None:
        ...

class AccessDateRange(_message.Message):
    __slots__ = ('start_date', 'end_date')
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str

    def __init__(self, start_date: _Optional[str]=..., end_date: _Optional[str]=...) -> None:
        ...

class AccessFilterExpression(_message.Message):
    __slots__ = ('and_group', 'or_group', 'not_expression', 'access_filter')
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: AccessFilterExpressionList
    or_group: AccessFilterExpressionList
    not_expression: AccessFilterExpression
    access_filter: AccessFilter

    def __init__(self, and_group: _Optional[_Union[AccessFilterExpressionList, _Mapping]]=..., or_group: _Optional[_Union[AccessFilterExpressionList, _Mapping]]=..., not_expression: _Optional[_Union[AccessFilterExpression, _Mapping]]=..., access_filter: _Optional[_Union[AccessFilter, _Mapping]]=...) -> None:
        ...

class AccessFilterExpressionList(_message.Message):
    __slots__ = ('expressions',)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: _containers.RepeatedCompositeFieldContainer[AccessFilterExpression]

    def __init__(self, expressions: _Optional[_Iterable[_Union[AccessFilterExpression, _Mapping]]]=...) -> None:
        ...

class AccessFilter(_message.Message):
    __slots__ = ('string_filter', 'in_list_filter', 'numeric_filter', 'between_filter', 'field_name')
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    string_filter: AccessStringFilter
    in_list_filter: AccessInListFilter
    numeric_filter: AccessNumericFilter
    between_filter: AccessBetweenFilter
    field_name: str

    def __init__(self, string_filter: _Optional[_Union[AccessStringFilter, _Mapping]]=..., in_list_filter: _Optional[_Union[AccessInListFilter, _Mapping]]=..., numeric_filter: _Optional[_Union[AccessNumericFilter, _Mapping]]=..., between_filter: _Optional[_Union[AccessBetweenFilter, _Mapping]]=..., field_name: _Optional[str]=...) -> None:
        ...

class AccessStringFilter(_message.Message):
    __slots__ = ('match_type', 'value', 'case_sensitive')

    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCH_TYPE_UNSPECIFIED: _ClassVar[AccessStringFilter.MatchType]
        EXACT: _ClassVar[AccessStringFilter.MatchType]
        BEGINS_WITH: _ClassVar[AccessStringFilter.MatchType]
        ENDS_WITH: _ClassVar[AccessStringFilter.MatchType]
        CONTAINS: _ClassVar[AccessStringFilter.MatchType]
        FULL_REGEXP: _ClassVar[AccessStringFilter.MatchType]
        PARTIAL_REGEXP: _ClassVar[AccessStringFilter.MatchType]
    MATCH_TYPE_UNSPECIFIED: AccessStringFilter.MatchType
    EXACT: AccessStringFilter.MatchType
    BEGINS_WITH: AccessStringFilter.MatchType
    ENDS_WITH: AccessStringFilter.MatchType
    CONTAINS: AccessStringFilter.MatchType
    FULL_REGEXP: AccessStringFilter.MatchType
    PARTIAL_REGEXP: AccessStringFilter.MatchType
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    match_type: AccessStringFilter.MatchType
    value: str
    case_sensitive: bool

    def __init__(self, match_type: _Optional[_Union[AccessStringFilter.MatchType, str]]=..., value: _Optional[str]=..., case_sensitive: bool=...) -> None:
        ...

class AccessInListFilter(_message.Message):
    __slots__ = ('values', 'case_sensitive')
    VALUES_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    case_sensitive: bool

    def __init__(self, values: _Optional[_Iterable[str]]=..., case_sensitive: bool=...) -> None:
        ...

class AccessNumericFilter(_message.Message):
    __slots__ = ('operation', 'value')

    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[AccessNumericFilter.Operation]
        EQUAL: _ClassVar[AccessNumericFilter.Operation]
        LESS_THAN: _ClassVar[AccessNumericFilter.Operation]
        LESS_THAN_OR_EQUAL: _ClassVar[AccessNumericFilter.Operation]
        GREATER_THAN: _ClassVar[AccessNumericFilter.Operation]
        GREATER_THAN_OR_EQUAL: _ClassVar[AccessNumericFilter.Operation]
    OPERATION_UNSPECIFIED: AccessNumericFilter.Operation
    EQUAL: AccessNumericFilter.Operation
    LESS_THAN: AccessNumericFilter.Operation
    LESS_THAN_OR_EQUAL: AccessNumericFilter.Operation
    GREATER_THAN: AccessNumericFilter.Operation
    GREATER_THAN_OR_EQUAL: AccessNumericFilter.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operation: AccessNumericFilter.Operation
    value: NumericValue

    def __init__(self, operation: _Optional[_Union[AccessNumericFilter.Operation, str]]=..., value: _Optional[_Union[NumericValue, _Mapping]]=...) -> None:
        ...

class AccessBetweenFilter(_message.Message):
    __slots__ = ('from_value', 'to_value')
    FROM_VALUE_FIELD_NUMBER: _ClassVar[int]
    TO_VALUE_FIELD_NUMBER: _ClassVar[int]
    from_value: NumericValue
    to_value: NumericValue

    def __init__(self, from_value: _Optional[_Union[NumericValue, _Mapping]]=..., to_value: _Optional[_Union[NumericValue, _Mapping]]=...) -> None:
        ...

class NumericValue(_message.Message):
    __slots__ = ('int64_value', 'double_value')
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    int64_value: int
    double_value: float

    def __init__(self, int64_value: _Optional[int]=..., double_value: _Optional[float]=...) -> None:
        ...

class AccessOrderBy(_message.Message):
    __slots__ = ('metric', 'dimension', 'desc')

    class MetricOrderBy(_message.Message):
        __slots__ = ('metric_name',)
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        metric_name: str

        def __init__(self, metric_name: _Optional[str]=...) -> None:
            ...

    class DimensionOrderBy(_message.Message):
        __slots__ = ('dimension_name', 'order_type')

        class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ORDER_TYPE_UNSPECIFIED: _ClassVar[AccessOrderBy.DimensionOrderBy.OrderType]
            ALPHANUMERIC: _ClassVar[AccessOrderBy.DimensionOrderBy.OrderType]
            CASE_INSENSITIVE_ALPHANUMERIC: _ClassVar[AccessOrderBy.DimensionOrderBy.OrderType]
            NUMERIC: _ClassVar[AccessOrderBy.DimensionOrderBy.OrderType]
        ORDER_TYPE_UNSPECIFIED: AccessOrderBy.DimensionOrderBy.OrderType
        ALPHANUMERIC: AccessOrderBy.DimensionOrderBy.OrderType
        CASE_INSENSITIVE_ALPHANUMERIC: AccessOrderBy.DimensionOrderBy.OrderType
        NUMERIC: AccessOrderBy.DimensionOrderBy.OrderType
        DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
        ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        dimension_name: str
        order_type: AccessOrderBy.DimensionOrderBy.OrderType

        def __init__(self, dimension_name: _Optional[str]=..., order_type: _Optional[_Union[AccessOrderBy.DimensionOrderBy.OrderType, str]]=...) -> None:
            ...
    METRIC_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    metric: AccessOrderBy.MetricOrderBy
    dimension: AccessOrderBy.DimensionOrderBy
    desc: bool

    def __init__(self, metric: _Optional[_Union[AccessOrderBy.MetricOrderBy, _Mapping]]=..., dimension: _Optional[_Union[AccessOrderBy.DimensionOrderBy, _Mapping]]=..., desc: bool=...) -> None:
        ...

class AccessDimensionHeader(_message.Message):
    __slots__ = ('dimension_name',)
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    dimension_name: str

    def __init__(self, dimension_name: _Optional[str]=...) -> None:
        ...

class AccessMetricHeader(_message.Message):
    __slots__ = ('metric_name',)
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    metric_name: str

    def __init__(self, metric_name: _Optional[str]=...) -> None:
        ...

class AccessRow(_message.Message):
    __slots__ = ('dimension_values', 'metric_values')
    DIMENSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_values: _containers.RepeatedCompositeFieldContainer[AccessDimensionValue]
    metric_values: _containers.RepeatedCompositeFieldContainer[AccessMetricValue]

    def __init__(self, dimension_values: _Optional[_Iterable[_Union[AccessDimensionValue, _Mapping]]]=..., metric_values: _Optional[_Iterable[_Union[AccessMetricValue, _Mapping]]]=...) -> None:
        ...

class AccessDimensionValue(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class AccessMetricValue(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...

class AccessQuota(_message.Message):
    __slots__ = ('tokens_per_day', 'tokens_per_hour', 'concurrent_requests', 'server_errors_per_project_per_hour', 'tokens_per_project_per_hour')
    TOKENS_PER_DAY_FIELD_NUMBER: _ClassVar[int]
    TOKENS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SERVER_ERRORS_PER_PROJECT_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    TOKENS_PER_PROJECT_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    tokens_per_day: AccessQuotaStatus
    tokens_per_hour: AccessQuotaStatus
    concurrent_requests: AccessQuotaStatus
    server_errors_per_project_per_hour: AccessQuotaStatus
    tokens_per_project_per_hour: AccessQuotaStatus

    def __init__(self, tokens_per_day: _Optional[_Union[AccessQuotaStatus, _Mapping]]=..., tokens_per_hour: _Optional[_Union[AccessQuotaStatus, _Mapping]]=..., concurrent_requests: _Optional[_Union[AccessQuotaStatus, _Mapping]]=..., server_errors_per_project_per_hour: _Optional[_Union[AccessQuotaStatus, _Mapping]]=..., tokens_per_project_per_hour: _Optional[_Union[AccessQuotaStatus, _Mapping]]=...) -> None:
        ...

class AccessQuotaStatus(_message.Message):
    __slots__ = ('consumed', 'remaining')
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    consumed: int
    remaining: int

    def __init__(self, consumed: _Optional[int]=..., remaining: _Optional[int]=...) -> None:
        ...