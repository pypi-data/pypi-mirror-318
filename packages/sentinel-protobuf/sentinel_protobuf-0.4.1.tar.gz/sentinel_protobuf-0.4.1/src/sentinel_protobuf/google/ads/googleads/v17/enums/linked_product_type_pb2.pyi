from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LinkedProductTypeEnum(_message.Message):
    __slots__ = ()

    class LinkedProductType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
        UNKNOWN: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
        DATA_PARTNER: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
        GOOGLE_ADS: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
        HOTEL_CENTER: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
        MERCHANT_CENTER: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
        ADVERTISING_PARTNER: _ClassVar[LinkedProductTypeEnum.LinkedProductType]
    UNSPECIFIED: LinkedProductTypeEnum.LinkedProductType
    UNKNOWN: LinkedProductTypeEnum.LinkedProductType
    DATA_PARTNER: LinkedProductTypeEnum.LinkedProductType
    GOOGLE_ADS: LinkedProductTypeEnum.LinkedProductType
    HOTEL_CENTER: LinkedProductTypeEnum.LinkedProductType
    MERCHANT_CENTER: LinkedProductTypeEnum.LinkedProductType
    ADVERTISING_PARTNER: LinkedProductTypeEnum.LinkedProductType

    def __init__(self) -> None:
        ...