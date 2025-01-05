from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppUrlOperatingSystemTypeEnum(_message.Message):
    __slots__ = ()

    class AppUrlOperatingSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType]
        UNKNOWN: _ClassVar[AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType]
        IOS: _ClassVar[AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType]
        ANDROID: _ClassVar[AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType]
    UNSPECIFIED: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    UNKNOWN: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    IOS: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    ANDROID: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType

    def __init__(self) -> None:
        ...