from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionOriginEnum(_message.Message):
    __slots__ = ()

    class ConversionOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        UNKNOWN: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        WEBSITE: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        GOOGLE_HOSTED: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        APP: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        CALL_FROM_ADS: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        STORE: _ClassVar[ConversionOriginEnum.ConversionOrigin]
        YOUTUBE_HOSTED: _ClassVar[ConversionOriginEnum.ConversionOrigin]
    UNSPECIFIED: ConversionOriginEnum.ConversionOrigin
    UNKNOWN: ConversionOriginEnum.ConversionOrigin
    WEBSITE: ConversionOriginEnum.ConversionOrigin
    GOOGLE_HOSTED: ConversionOriginEnum.ConversionOrigin
    APP: ConversionOriginEnum.ConversionOrigin
    CALL_FROM_ADS: ConversionOriginEnum.ConversionOrigin
    STORE: ConversionOriginEnum.ConversionOrigin
    YOUTUBE_HOSTED: ConversionOriginEnum.ConversionOrigin

    def __init__(self) -> None:
        ...