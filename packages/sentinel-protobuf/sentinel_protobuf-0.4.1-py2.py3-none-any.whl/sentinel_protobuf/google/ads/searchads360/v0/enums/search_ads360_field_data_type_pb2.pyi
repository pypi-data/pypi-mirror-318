from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchAds360FieldDataTypeEnum(_message.Message):
    __slots__ = ()

    class SearchAds360FieldDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        UNKNOWN: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        BOOLEAN: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        DATE: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        DOUBLE: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        ENUM: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        FLOAT: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        INT32: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        INT64: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        MESSAGE: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        RESOURCE_NAME: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        STRING: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
        UINT64: _ClassVar[SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType]
    UNSPECIFIED: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    UNKNOWN: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    BOOLEAN: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    DATE: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    DOUBLE: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    ENUM: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    FLOAT: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    INT32: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    INT64: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    MESSAGE: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    RESOURCE_NAME: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    STRING: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType
    UINT64: SearchAds360FieldDataTypeEnum.SearchAds360FieldDataType

    def __init__(self) -> None:
        ...