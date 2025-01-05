from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchTermInsightErrorEnum(_message.Message):
    __slots__ = ()

    class SearchTermInsightError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        UNKNOWN: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        FILTERING_NOT_ALLOWED_WITH_SEGMENTS: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        LIMIT_NOT_ALLOWED_WITH_SEGMENTS: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        MISSING_FIELD_IN_SELECT_CLAUSE: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        REQUIRES_FILTER_BY_SINGLE_RESOURCE: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        SORTING_NOT_ALLOWED_WITH_SEGMENTS: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
        SUMMARY_ROW_NOT_ALLOWED_WITH_SEGMENTS: _ClassVar[SearchTermInsightErrorEnum.SearchTermInsightError]
    UNSPECIFIED: SearchTermInsightErrorEnum.SearchTermInsightError
    UNKNOWN: SearchTermInsightErrorEnum.SearchTermInsightError
    FILTERING_NOT_ALLOWED_WITH_SEGMENTS: SearchTermInsightErrorEnum.SearchTermInsightError
    LIMIT_NOT_ALLOWED_WITH_SEGMENTS: SearchTermInsightErrorEnum.SearchTermInsightError
    MISSING_FIELD_IN_SELECT_CLAUSE: SearchTermInsightErrorEnum.SearchTermInsightError
    REQUIRES_FILTER_BY_SINGLE_RESOURCE: SearchTermInsightErrorEnum.SearchTermInsightError
    SORTING_NOT_ALLOWED_WITH_SEGMENTS: SearchTermInsightErrorEnum.SearchTermInsightError
    SUMMARY_ROW_NOT_ALLOWED_WITH_SEGMENTS: SearchTermInsightErrorEnum.SearchTermInsightError

    def __init__(self) -> None:
        ...