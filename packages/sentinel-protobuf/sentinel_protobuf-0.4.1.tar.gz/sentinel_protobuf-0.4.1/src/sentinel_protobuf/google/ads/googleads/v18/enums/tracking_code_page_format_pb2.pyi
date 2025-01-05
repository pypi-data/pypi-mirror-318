from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TrackingCodePageFormatEnum(_message.Message):
    __slots__ = ()

    class TrackingCodePageFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TrackingCodePageFormatEnum.TrackingCodePageFormat]
        UNKNOWN: _ClassVar[TrackingCodePageFormatEnum.TrackingCodePageFormat]
        HTML: _ClassVar[TrackingCodePageFormatEnum.TrackingCodePageFormat]
        AMP: _ClassVar[TrackingCodePageFormatEnum.TrackingCodePageFormat]
    UNSPECIFIED: TrackingCodePageFormatEnum.TrackingCodePageFormat
    UNKNOWN: TrackingCodePageFormatEnum.TrackingCodePageFormat
    HTML: TrackingCodePageFormatEnum.TrackingCodePageFormat
    AMP: TrackingCodePageFormatEnum.TrackingCodePageFormat

    def __init__(self) -> None:
        ...