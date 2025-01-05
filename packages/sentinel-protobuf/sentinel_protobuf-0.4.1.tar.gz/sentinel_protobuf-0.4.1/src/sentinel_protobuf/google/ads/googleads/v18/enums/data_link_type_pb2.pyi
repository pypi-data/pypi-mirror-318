from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DataLinkTypeEnum(_message.Message):
    __slots__ = ()

    class DataLinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DataLinkTypeEnum.DataLinkType]
        UNKNOWN: _ClassVar[DataLinkTypeEnum.DataLinkType]
        VIDEO: _ClassVar[DataLinkTypeEnum.DataLinkType]
    UNSPECIFIED: DataLinkTypeEnum.DataLinkType
    UNKNOWN: DataLinkTypeEnum.DataLinkType
    VIDEO: DataLinkTypeEnum.DataLinkType

    def __init__(self) -> None:
        ...