from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanIdeaErrorEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanIdeaError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError]
        UNKNOWN: _ClassVar[KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError]
        URL_CRAWL_ERROR: _ClassVar[KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError]
        INVALID_VALUE: _ClassVar[KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError]
    UNSPECIFIED: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError
    UNKNOWN: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError
    URL_CRAWL_ERROR: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError
    INVALID_VALUE: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError

    def __init__(self) -> None:
        ...