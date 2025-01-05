from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PartialFailureErrorEnum(_message.Message):
    __slots__ = ()

    class PartialFailureError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PartialFailureErrorEnum.PartialFailureError]
        UNKNOWN: _ClassVar[PartialFailureErrorEnum.PartialFailureError]
        PARTIAL_FAILURE_MODE_REQUIRED: _ClassVar[PartialFailureErrorEnum.PartialFailureError]
    UNSPECIFIED: PartialFailureErrorEnum.PartialFailureError
    UNKNOWN: PartialFailureErrorEnum.PartialFailureError
    PARTIAL_FAILURE_MODE_REQUIRED: PartialFailureErrorEnum.PartialFailureError

    def __init__(self) -> None:
        ...