from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentTypeEnum(_message.Message):
    __slots__ = ()

    class EnvironmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENVIRONMENT_TYPE_UNSPECIFIED: _ClassVar[EnvironmentTypeEnum.EnvironmentType]
        BROWSER: _ClassVar[EnvironmentTypeEnum.EnvironmentType]
        VIDEO_PLAYER: _ClassVar[EnvironmentTypeEnum.EnvironmentType]
    ENVIRONMENT_TYPE_UNSPECIFIED: EnvironmentTypeEnum.EnvironmentType
    BROWSER: EnvironmentTypeEnum.EnvironmentType
    VIDEO_PLAYER: EnvironmentTypeEnum.EnvironmentType

    def __init__(self) -> None:
        ...