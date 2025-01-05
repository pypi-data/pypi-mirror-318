from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class QuotaErrorEnum(_message.Message):
    __slots__ = ()

    class QuotaError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[QuotaErrorEnum.QuotaError]
        UNKNOWN: _ClassVar[QuotaErrorEnum.QuotaError]
        RESOURCE_EXHAUSTED: _ClassVar[QuotaErrorEnum.QuotaError]
        RESOURCE_TEMPORARILY_EXHAUSTED: _ClassVar[QuotaErrorEnum.QuotaError]
    UNSPECIFIED: QuotaErrorEnum.QuotaError
    UNKNOWN: QuotaErrorEnum.QuotaError
    RESOURCE_EXHAUSTED: QuotaErrorEnum.QuotaError
    RESOURCE_TEMPORARILY_EXHAUSTED: QuotaErrorEnum.QuotaError

    def __init__(self) -> None:
        ...