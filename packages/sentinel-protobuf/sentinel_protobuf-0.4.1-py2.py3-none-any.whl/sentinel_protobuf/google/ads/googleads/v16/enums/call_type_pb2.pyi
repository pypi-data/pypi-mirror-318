from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CallTypeEnum(_message.Message):
    __slots__ = ()

    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CallTypeEnum.CallType]
        UNKNOWN: _ClassVar[CallTypeEnum.CallType]
        MANUALLY_DIALED: _ClassVar[CallTypeEnum.CallType]
        HIGH_END_MOBILE_SEARCH: _ClassVar[CallTypeEnum.CallType]
    UNSPECIFIED: CallTypeEnum.CallType
    UNKNOWN: CallTypeEnum.CallType
    MANUALLY_DIALED: CallTypeEnum.CallType
    HIGH_END_MOBILE_SEARCH: CallTypeEnum.CallType

    def __init__(self) -> None:
        ...