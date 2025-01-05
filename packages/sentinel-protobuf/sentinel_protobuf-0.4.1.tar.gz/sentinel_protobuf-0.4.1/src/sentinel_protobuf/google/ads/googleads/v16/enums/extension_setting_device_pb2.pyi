from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExtensionSettingDeviceEnum(_message.Message):
    __slots__ = ()

    class ExtensionSettingDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExtensionSettingDeviceEnum.ExtensionSettingDevice]
        UNKNOWN: _ClassVar[ExtensionSettingDeviceEnum.ExtensionSettingDevice]
        MOBILE: _ClassVar[ExtensionSettingDeviceEnum.ExtensionSettingDevice]
        DESKTOP: _ClassVar[ExtensionSettingDeviceEnum.ExtensionSettingDevice]
    UNSPECIFIED: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    UNKNOWN: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    MOBILE: ExtensionSettingDeviceEnum.ExtensionSettingDevice
    DESKTOP: ExtensionSettingDeviceEnum.ExtensionSettingDevice

    def __init__(self) -> None:
        ...