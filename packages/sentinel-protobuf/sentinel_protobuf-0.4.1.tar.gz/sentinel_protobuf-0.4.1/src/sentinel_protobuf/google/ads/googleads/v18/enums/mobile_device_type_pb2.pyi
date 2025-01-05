from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MobileDeviceTypeEnum(_message.Message):
    __slots__ = ()

    class MobileDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MobileDeviceTypeEnum.MobileDeviceType]
        UNKNOWN: _ClassVar[MobileDeviceTypeEnum.MobileDeviceType]
        MOBILE: _ClassVar[MobileDeviceTypeEnum.MobileDeviceType]
        TABLET: _ClassVar[MobileDeviceTypeEnum.MobileDeviceType]
    UNSPECIFIED: MobileDeviceTypeEnum.MobileDeviceType
    UNKNOWN: MobileDeviceTypeEnum.MobileDeviceType
    MOBILE: MobileDeviceTypeEnum.MobileDeviceType
    TABLET: MobileDeviceTypeEnum.MobileDeviceType

    def __init__(self) -> None:
        ...