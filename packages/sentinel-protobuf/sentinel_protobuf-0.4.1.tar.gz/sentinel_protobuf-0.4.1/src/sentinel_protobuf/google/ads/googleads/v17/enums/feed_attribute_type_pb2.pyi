from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedAttributeTypeEnum(_message.Message):
    __slots__ = ()

    class FeedAttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        UNKNOWN: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        INT64: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        DOUBLE: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        STRING: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        BOOLEAN: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        URL: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        DATE_TIME: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        INT64_LIST: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        DOUBLE_LIST: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        STRING_LIST: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        BOOLEAN_LIST: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        URL_LIST: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        DATE_TIME_LIST: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
        PRICE: _ClassVar[FeedAttributeTypeEnum.FeedAttributeType]
    UNSPECIFIED: FeedAttributeTypeEnum.FeedAttributeType
    UNKNOWN: FeedAttributeTypeEnum.FeedAttributeType
    INT64: FeedAttributeTypeEnum.FeedAttributeType
    DOUBLE: FeedAttributeTypeEnum.FeedAttributeType
    STRING: FeedAttributeTypeEnum.FeedAttributeType
    BOOLEAN: FeedAttributeTypeEnum.FeedAttributeType
    URL: FeedAttributeTypeEnum.FeedAttributeType
    DATE_TIME: FeedAttributeTypeEnum.FeedAttributeType
    INT64_LIST: FeedAttributeTypeEnum.FeedAttributeType
    DOUBLE_LIST: FeedAttributeTypeEnum.FeedAttributeType
    STRING_LIST: FeedAttributeTypeEnum.FeedAttributeType
    BOOLEAN_LIST: FeedAttributeTypeEnum.FeedAttributeType
    URL_LIST: FeedAttributeTypeEnum.FeedAttributeType
    DATE_TIME_LIST: FeedAttributeTypeEnum.FeedAttributeType
    PRICE: FeedAttributeTypeEnum.FeedAttributeType

    def __init__(self) -> None:
        ...