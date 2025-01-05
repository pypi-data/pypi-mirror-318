from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomizerValueStatusEnum(_message.Message):
    __slots__ = ()

    class CustomizerValueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomizerValueStatusEnum.CustomizerValueStatus]
        UNKNOWN: _ClassVar[CustomizerValueStatusEnum.CustomizerValueStatus]
        ENABLED: _ClassVar[CustomizerValueStatusEnum.CustomizerValueStatus]
        REMOVED: _ClassVar[CustomizerValueStatusEnum.CustomizerValueStatus]
    UNSPECIFIED: CustomizerValueStatusEnum.CustomizerValueStatus
    UNKNOWN: CustomizerValueStatusEnum.CustomizerValueStatus
    ENABLED: CustomizerValueStatusEnum.CustomizerValueStatus
    REMOVED: CustomizerValueStatusEnum.CustomizerValueStatus

    def __init__(self) -> None:
        ...