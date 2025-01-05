from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdRotationModeEnum(_message.Message):
    __slots__ = ()

    class AdGroupAdRotationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupAdRotationModeEnum.AdGroupAdRotationMode]
        UNKNOWN: _ClassVar[AdGroupAdRotationModeEnum.AdGroupAdRotationMode]
        OPTIMIZE: _ClassVar[AdGroupAdRotationModeEnum.AdGroupAdRotationMode]
        ROTATE_FOREVER: _ClassVar[AdGroupAdRotationModeEnum.AdGroupAdRotationMode]
    UNSPECIFIED: AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    UNKNOWN: AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    OPTIMIZE: AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    ROTATE_FOREVER: AdGroupAdRotationModeEnum.AdGroupAdRotationMode

    def __init__(self) -> None:
        ...