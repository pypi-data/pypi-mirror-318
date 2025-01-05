from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConsentStatusEnum(_message.Message):
    __slots__ = ()

    class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConsentStatusEnum.ConsentStatus]
        UNKNOWN: _ClassVar[ConsentStatusEnum.ConsentStatus]
        GRANTED: _ClassVar[ConsentStatusEnum.ConsentStatus]
        DENIED: _ClassVar[ConsentStatusEnum.ConsentStatus]
    UNSPECIFIED: ConsentStatusEnum.ConsentStatus
    UNKNOWN: ConsentStatusEnum.ConsentStatus
    GRANTED: ConsentStatusEnum.ConsentStatus
    DENIED: ConsentStatusEnum.ConsentStatus

    def __init__(self) -> None:
        ...