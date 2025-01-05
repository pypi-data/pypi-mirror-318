from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdxErrorEnum(_message.Message):
    __slots__ = ()

    class AdxError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdxErrorEnum.AdxError]
        UNKNOWN: _ClassVar[AdxErrorEnum.AdxError]
        UNSUPPORTED_FEATURE: _ClassVar[AdxErrorEnum.AdxError]
    UNSPECIFIED: AdxErrorEnum.AdxError
    UNKNOWN: AdxErrorEnum.AdxError
    UNSUPPORTED_FEATURE: AdxErrorEnum.AdxError

    def __init__(self) -> None:
        ...