from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccessReasonEnum(_message.Message):
    __slots__ = ()

    class AccessReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccessReasonEnum.AccessReason]
        UNKNOWN: _ClassVar[AccessReasonEnum.AccessReason]
        OWNED: _ClassVar[AccessReasonEnum.AccessReason]
        SHARED: _ClassVar[AccessReasonEnum.AccessReason]
        LICENSED: _ClassVar[AccessReasonEnum.AccessReason]
        SUBSCRIBED: _ClassVar[AccessReasonEnum.AccessReason]
        AFFILIATED: _ClassVar[AccessReasonEnum.AccessReason]
    UNSPECIFIED: AccessReasonEnum.AccessReason
    UNKNOWN: AccessReasonEnum.AccessReason
    OWNED: AccessReasonEnum.AccessReason
    SHARED: AccessReasonEnum.AccessReason
    LICENSED: AccessReasonEnum.AccessReason
    SUBSCRIBED: AccessReasonEnum.AccessReason
    AFFILIATED: AccessReasonEnum.AccessReason

    def __init__(self) -> None:
        ...