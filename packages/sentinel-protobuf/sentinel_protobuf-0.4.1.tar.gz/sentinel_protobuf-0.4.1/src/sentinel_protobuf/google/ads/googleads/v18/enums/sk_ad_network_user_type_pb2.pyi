from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SkAdNetworkUserTypeEnum(_message.Message):
    __slots__ = ()

    class SkAdNetworkUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
        UNKNOWN: _ClassVar[SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
        UNAVAILABLE: _ClassVar[SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
        NEW_INSTALLER: _ClassVar[SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
        REINSTALLER: _ClassVar[SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
    UNSPECIFIED: SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    UNKNOWN: SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    UNAVAILABLE: SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    NEW_INSTALLER: SkAdNetworkUserTypeEnum.SkAdNetworkUserType
    REINSTALLER: SkAdNetworkUserTypeEnum.SkAdNetworkUserType

    def __init__(self) -> None:
        ...