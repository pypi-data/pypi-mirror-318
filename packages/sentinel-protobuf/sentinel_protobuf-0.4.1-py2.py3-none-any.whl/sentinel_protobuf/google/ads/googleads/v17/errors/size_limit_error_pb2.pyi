from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SizeLimitErrorEnum(_message.Message):
    __slots__ = ()

    class SizeLimitError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SizeLimitErrorEnum.SizeLimitError]
        UNKNOWN: _ClassVar[SizeLimitErrorEnum.SizeLimitError]
        REQUEST_SIZE_LIMIT_EXCEEDED: _ClassVar[SizeLimitErrorEnum.SizeLimitError]
        RESPONSE_SIZE_LIMIT_EXCEEDED: _ClassVar[SizeLimitErrorEnum.SizeLimitError]
    UNSPECIFIED: SizeLimitErrorEnum.SizeLimitError
    UNKNOWN: SizeLimitErrorEnum.SizeLimitError
    REQUEST_SIZE_LIMIT_EXCEEDED: SizeLimitErrorEnum.SizeLimitError
    RESPONSE_SIZE_LIMIT_EXCEEDED: SizeLimitErrorEnum.SizeLimitError

    def __init__(self) -> None:
        ...