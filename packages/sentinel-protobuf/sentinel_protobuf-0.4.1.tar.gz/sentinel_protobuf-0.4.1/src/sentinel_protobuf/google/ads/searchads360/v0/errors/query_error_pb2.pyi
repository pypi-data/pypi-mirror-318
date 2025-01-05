from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class QueryErrorEnum(_message.Message):
    __slots__ = ()

    class QueryError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[QueryErrorEnum.QueryError]
        UNKNOWN: _ClassVar[QueryErrorEnum.QueryError]
        QUERY_ERROR: _ClassVar[QueryErrorEnum.QueryError]
        BAD_ENUM_CONSTANT: _ClassVar[QueryErrorEnum.QueryError]
        BAD_ESCAPE_SEQUENCE: _ClassVar[QueryErrorEnum.QueryError]
        BAD_FIELD_NAME: _ClassVar[QueryErrorEnum.QueryError]
        BAD_LIMIT_VALUE: _ClassVar[QueryErrorEnum.QueryError]
        BAD_NUMBER: _ClassVar[QueryErrorEnum.QueryError]
        BAD_OPERATOR: _ClassVar[QueryErrorEnum.QueryError]
        BAD_PARAMETER_NAME: _ClassVar[QueryErrorEnum.QueryError]
        BAD_PARAMETER_VALUE: _ClassVar[QueryErrorEnum.QueryError]
        BAD_RESOURCE_TYPE_IN_FROM_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        BAD_SYMBOL: _ClassVar[QueryErrorEnum.QueryError]
        BAD_VALUE: _ClassVar[QueryErrorEnum.QueryError]
        DATE_RANGE_TOO_WIDE: _ClassVar[QueryErrorEnum.QueryError]
        DATE_RANGE_TOO_NARROW: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_AND: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_BY: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_FILTERS_ON_DATE_RANGE: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_FROM: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_LIST: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_SELECT: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_SINGLE_VALUE: _ClassVar[QueryErrorEnum.QueryError]
        EXPECTED_VALUE_WITH_BETWEEN_OPERATOR: _ClassVar[QueryErrorEnum.QueryError]
        INVALID_DATE_FORMAT: _ClassVar[QueryErrorEnum.QueryError]
        MISALIGNED_DATE_FOR_FILTER: _ClassVar[QueryErrorEnum.QueryError]
        INVALID_STRING_VALUE: _ClassVar[QueryErrorEnum.QueryError]
        INVALID_VALUE_WITH_BETWEEN_OPERATOR: _ClassVar[QueryErrorEnum.QueryError]
        INVALID_VALUE_WITH_DURING_OPERATOR: _ClassVar[QueryErrorEnum.QueryError]
        INVALID_VALUE_WITH_LIKE_OPERATOR: _ClassVar[QueryErrorEnum.QueryError]
        OPERATOR_FIELD_MISMATCH: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_EMPTY_LIST_IN_CONDITION: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_ENUM_CONSTANT: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_FIELD_IN_SELECT_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_FIELD_IN_WHERE_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        LIMIT_VALUE_TOO_LOW: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_NEWLINE_IN_STRING: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_VALUE_COMBINATION_IN_LIST: _ClassVar[QueryErrorEnum.QueryError]
        PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR: _ClassVar[QueryErrorEnum.QueryError]
        STRING_NOT_TERMINATED: _ClassVar[QueryErrorEnum.QueryError]
        TOO_MANY_SEGMENTS: _ClassVar[QueryErrorEnum.QueryError]
        UNEXPECTED_END_OF_QUERY: _ClassVar[QueryErrorEnum.QueryError]
        UNEXPECTED_FROM_CLAUSE: _ClassVar[QueryErrorEnum.QueryError]
        UNRECOGNIZED_FIELD: _ClassVar[QueryErrorEnum.QueryError]
        UNEXPECTED_INPUT: _ClassVar[QueryErrorEnum.QueryError]
        REQUESTED_METRICS_FOR_MANAGER: _ClassVar[QueryErrorEnum.QueryError]
        FILTER_HAS_TOO_MANY_VALUES: _ClassVar[QueryErrorEnum.QueryError]
    UNSPECIFIED: QueryErrorEnum.QueryError
    UNKNOWN: QueryErrorEnum.QueryError
    QUERY_ERROR: QueryErrorEnum.QueryError
    BAD_ENUM_CONSTANT: QueryErrorEnum.QueryError
    BAD_ESCAPE_SEQUENCE: QueryErrorEnum.QueryError
    BAD_FIELD_NAME: QueryErrorEnum.QueryError
    BAD_LIMIT_VALUE: QueryErrorEnum.QueryError
    BAD_NUMBER: QueryErrorEnum.QueryError
    BAD_OPERATOR: QueryErrorEnum.QueryError
    BAD_PARAMETER_NAME: QueryErrorEnum.QueryError
    BAD_PARAMETER_VALUE: QueryErrorEnum.QueryError
    BAD_RESOURCE_TYPE_IN_FROM_CLAUSE: QueryErrorEnum.QueryError
    BAD_SYMBOL: QueryErrorEnum.QueryError
    BAD_VALUE: QueryErrorEnum.QueryError
    DATE_RANGE_TOO_WIDE: QueryErrorEnum.QueryError
    DATE_RANGE_TOO_NARROW: QueryErrorEnum.QueryError
    EXPECTED_AND: QueryErrorEnum.QueryError
    EXPECTED_BY: QueryErrorEnum.QueryError
    EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE: QueryErrorEnum.QueryError
    EXPECTED_FILTERS_ON_DATE_RANGE: QueryErrorEnum.QueryError
    EXPECTED_FROM: QueryErrorEnum.QueryError
    EXPECTED_LIST: QueryErrorEnum.QueryError
    EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE: QueryErrorEnum.QueryError
    EXPECTED_SELECT: QueryErrorEnum.QueryError
    EXPECTED_SINGLE_VALUE: QueryErrorEnum.QueryError
    EXPECTED_VALUE_WITH_BETWEEN_OPERATOR: QueryErrorEnum.QueryError
    INVALID_DATE_FORMAT: QueryErrorEnum.QueryError
    MISALIGNED_DATE_FOR_FILTER: QueryErrorEnum.QueryError
    INVALID_STRING_VALUE: QueryErrorEnum.QueryError
    INVALID_VALUE_WITH_BETWEEN_OPERATOR: QueryErrorEnum.QueryError
    INVALID_VALUE_WITH_DURING_OPERATOR: QueryErrorEnum.QueryError
    INVALID_VALUE_WITH_LIKE_OPERATOR: QueryErrorEnum.QueryError
    OPERATOR_FIELD_MISMATCH: QueryErrorEnum.QueryError
    PROHIBITED_EMPTY_LIST_IN_CONDITION: QueryErrorEnum.QueryError
    PROHIBITED_ENUM_CONSTANT: QueryErrorEnum.QueryError
    PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_FIELD_IN_SELECT_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_FIELD_IN_WHERE_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE: QueryErrorEnum.QueryError
    PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE: QueryErrorEnum.QueryError
    LIMIT_VALUE_TOO_LOW: QueryErrorEnum.QueryError
    PROHIBITED_NEWLINE_IN_STRING: QueryErrorEnum.QueryError
    PROHIBITED_VALUE_COMBINATION_IN_LIST: QueryErrorEnum.QueryError
    PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR: QueryErrorEnum.QueryError
    STRING_NOT_TERMINATED: QueryErrorEnum.QueryError
    TOO_MANY_SEGMENTS: QueryErrorEnum.QueryError
    UNEXPECTED_END_OF_QUERY: QueryErrorEnum.QueryError
    UNEXPECTED_FROM_CLAUSE: QueryErrorEnum.QueryError
    UNRECOGNIZED_FIELD: QueryErrorEnum.QueryError
    UNEXPECTED_INPUT: QueryErrorEnum.QueryError
    REQUESTED_METRICS_FOR_MANAGER: QueryErrorEnum.QueryError
    FILTER_HAS_TOO_MANY_VALUES: QueryErrorEnum.QueryError

    def __init__(self) -> None:
        ...