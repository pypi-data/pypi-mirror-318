from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LinkedAccountTypeEnum(_message.Message):
    __slots__ = ()

    class LinkedAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LinkedAccountTypeEnum.LinkedAccountType]
        UNKNOWN: _ClassVar[LinkedAccountTypeEnum.LinkedAccountType]
        THIRD_PARTY_APP_ANALYTICS: _ClassVar[LinkedAccountTypeEnum.LinkedAccountType]
    UNSPECIFIED: LinkedAccountTypeEnum.LinkedAccountType
    UNKNOWN: LinkedAccountTypeEnum.LinkedAccountType
    THIRD_PARTY_APP_ANALYTICS: LinkedAccountTypeEnum.LinkedAccountType

    def __init__(self) -> None:
        ...