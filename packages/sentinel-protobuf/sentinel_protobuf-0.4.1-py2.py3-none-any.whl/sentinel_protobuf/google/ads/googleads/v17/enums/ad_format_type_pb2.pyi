from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdFormatTypeEnum(_message.Message):
    __slots__ = ()

    class AdFormatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdFormatTypeEnum.AdFormatType]
        UNKNOWN: _ClassVar[AdFormatTypeEnum.AdFormatType]
        OTHER: _ClassVar[AdFormatTypeEnum.AdFormatType]
        UNSEGMENTED: _ClassVar[AdFormatTypeEnum.AdFormatType]
        INSTREAM_SKIPPABLE: _ClassVar[AdFormatTypeEnum.AdFormatType]
        INSTREAM_NON_SKIPPABLE: _ClassVar[AdFormatTypeEnum.AdFormatType]
        INFEED: _ClassVar[AdFormatTypeEnum.AdFormatType]
        BUMPER: _ClassVar[AdFormatTypeEnum.AdFormatType]
        OUTSTREAM: _ClassVar[AdFormatTypeEnum.AdFormatType]
        MASTHEAD: _ClassVar[AdFormatTypeEnum.AdFormatType]
        AUDIO: _ClassVar[AdFormatTypeEnum.AdFormatType]
        SHORTS: _ClassVar[AdFormatTypeEnum.AdFormatType]
    UNSPECIFIED: AdFormatTypeEnum.AdFormatType
    UNKNOWN: AdFormatTypeEnum.AdFormatType
    OTHER: AdFormatTypeEnum.AdFormatType
    UNSEGMENTED: AdFormatTypeEnum.AdFormatType
    INSTREAM_SKIPPABLE: AdFormatTypeEnum.AdFormatType
    INSTREAM_NON_SKIPPABLE: AdFormatTypeEnum.AdFormatType
    INFEED: AdFormatTypeEnum.AdFormatType
    BUMPER: AdFormatTypeEnum.AdFormatType
    OUTSTREAM: AdFormatTypeEnum.AdFormatType
    MASTHEAD: AdFormatTypeEnum.AdFormatType
    AUDIO: AdFormatTypeEnum.AdFormatType
    SHORTS: AdFormatTypeEnum.AdFormatType

    def __init__(self) -> None:
        ...