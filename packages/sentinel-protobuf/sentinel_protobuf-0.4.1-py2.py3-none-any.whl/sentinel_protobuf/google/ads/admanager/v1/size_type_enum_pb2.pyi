from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SizeTypeEnum(_message.Message):
    __slots__ = ()

    class SizeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIZE_TYPE_UNSPECIFIED: _ClassVar[SizeTypeEnum.SizeType]
        PIXEL: _ClassVar[SizeTypeEnum.SizeType]
        ASPECT_RATIO: _ClassVar[SizeTypeEnum.SizeType]
        INTERSTITIAL: _ClassVar[SizeTypeEnum.SizeType]
        IGNORED: _ClassVar[SizeTypeEnum.SizeType]
        NATIVE: _ClassVar[SizeTypeEnum.SizeType]
        FLUID: _ClassVar[SizeTypeEnum.SizeType]
        AUDIO: _ClassVar[SizeTypeEnum.SizeType]
    SIZE_TYPE_UNSPECIFIED: SizeTypeEnum.SizeType
    PIXEL: SizeTypeEnum.SizeType
    ASPECT_RATIO: SizeTypeEnum.SizeType
    INTERSTITIAL: SizeTypeEnum.SizeType
    IGNORED: SizeTypeEnum.SizeType
    NATIVE: SizeTypeEnum.SizeType
    FLUID: SizeTypeEnum.SizeType
    AUDIO: SizeTypeEnum.SizeType

    def __init__(self) -> None:
        ...