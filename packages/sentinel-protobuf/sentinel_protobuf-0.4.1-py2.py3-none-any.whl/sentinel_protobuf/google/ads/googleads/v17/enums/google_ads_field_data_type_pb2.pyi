from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GoogleAdsFieldDataTypeEnum(_message.Message):
    __slots__ = ()

    class GoogleAdsFieldDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        UNKNOWN: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        BOOLEAN: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        DATE: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        DOUBLE: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        ENUM: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        FLOAT: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        INT32: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        INT64: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        MESSAGE: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        RESOURCE_NAME: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        STRING: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
        UINT64: _ClassVar[GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType]
    UNSPECIFIED: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    UNKNOWN: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    BOOLEAN: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    DATE: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    DOUBLE: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    ENUM: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    FLOAT: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    INT32: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    INT64: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    MESSAGE: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    RESOURCE_NAME: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    STRING: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    UINT64: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType

    def __init__(self) -> None:
        ...