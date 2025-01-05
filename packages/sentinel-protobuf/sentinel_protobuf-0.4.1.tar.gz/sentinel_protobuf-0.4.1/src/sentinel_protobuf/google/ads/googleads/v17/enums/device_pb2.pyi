from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DeviceEnum(_message.Message):
    __slots__ = ()

    class Device(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DeviceEnum.Device]
        UNKNOWN: _ClassVar[DeviceEnum.Device]
        MOBILE: _ClassVar[DeviceEnum.Device]
        TABLET: _ClassVar[DeviceEnum.Device]
        DESKTOP: _ClassVar[DeviceEnum.Device]
        CONNECTED_TV: _ClassVar[DeviceEnum.Device]
        OTHER: _ClassVar[DeviceEnum.Device]
    UNSPECIFIED: DeviceEnum.Device
    UNKNOWN: DeviceEnum.Device
    MOBILE: DeviceEnum.Device
    TABLET: DeviceEnum.Device
    DESKTOP: DeviceEnum.Device
    CONNECTED_TV: DeviceEnum.Device
    OTHER: DeviceEnum.Device

    def __init__(self) -> None:
        ...