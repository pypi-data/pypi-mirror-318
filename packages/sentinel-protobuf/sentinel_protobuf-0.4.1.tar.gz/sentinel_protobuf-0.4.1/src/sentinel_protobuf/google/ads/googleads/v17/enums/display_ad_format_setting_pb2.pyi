from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DisplayAdFormatSettingEnum(_message.Message):
    __slots__ = ()

    class DisplayAdFormatSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DisplayAdFormatSettingEnum.DisplayAdFormatSetting]
        UNKNOWN: _ClassVar[DisplayAdFormatSettingEnum.DisplayAdFormatSetting]
        ALL_FORMATS: _ClassVar[DisplayAdFormatSettingEnum.DisplayAdFormatSetting]
        NON_NATIVE: _ClassVar[DisplayAdFormatSettingEnum.DisplayAdFormatSetting]
        NATIVE: _ClassVar[DisplayAdFormatSettingEnum.DisplayAdFormatSetting]
    UNSPECIFIED: DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    UNKNOWN: DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    ALL_FORMATS: DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    NON_NATIVE: DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    NATIVE: DisplayAdFormatSettingEnum.DisplayAdFormatSetting

    def __init__(self) -> None:
        ...