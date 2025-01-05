from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DisplayUploadProductTypeEnum(_message.Message):
    __slots__ = ()

    class DisplayUploadProductType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        UNKNOWN: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        HTML5_UPLOAD_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_EDUCATION_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_FLIGHT_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_HOTEL_RENTAL_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_JOB_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_LOCAL_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_REAL_ESTATE_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_CUSTOM_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_TRAVEL_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
        DYNAMIC_HTML5_HOTEL_AD: _ClassVar[DisplayUploadProductTypeEnum.DisplayUploadProductType]
    UNSPECIFIED: DisplayUploadProductTypeEnum.DisplayUploadProductType
    UNKNOWN: DisplayUploadProductTypeEnum.DisplayUploadProductType
    HTML5_UPLOAD_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_EDUCATION_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_FLIGHT_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_HOTEL_RENTAL_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_JOB_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_LOCAL_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_REAL_ESTATE_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_CUSTOM_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_TRAVEL_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType
    DYNAMIC_HTML5_HOTEL_AD: DisplayUploadProductTypeEnum.DisplayUploadProductType

    def __init__(self) -> None:
        ...