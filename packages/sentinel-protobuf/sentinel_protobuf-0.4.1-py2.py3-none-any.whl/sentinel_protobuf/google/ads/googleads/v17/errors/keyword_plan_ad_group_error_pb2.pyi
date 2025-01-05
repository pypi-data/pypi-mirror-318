from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanAdGroupErrorEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanAdGroupError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError]
        UNKNOWN: _ClassVar[KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError]
        INVALID_NAME: _ClassVar[KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError]
        DUPLICATE_NAME: _ClassVar[KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError]
    UNSPECIFIED: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError
    UNKNOWN: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError
    INVALID_NAME: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError
    DUPLICATE_NAME: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError

    def __init__(self) -> None:
        ...