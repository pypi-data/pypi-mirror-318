from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionActionCategoryEnum(_message.Message):
    __slots__ = ()

    class ConversionActionCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        UNKNOWN: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        DEFAULT: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        PAGE_VIEW: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        PURCHASE: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        SIGNUP: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        LEAD: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        DOWNLOAD: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        ADD_TO_CART: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        BEGIN_CHECKOUT: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        SUBSCRIBE_PAID: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        PHONE_CALL_LEAD: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        IMPORTED_LEAD: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        SUBMIT_LEAD_FORM: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        BOOK_APPOINTMENT: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        REQUEST_QUOTE: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        GET_DIRECTIONS: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        OUTBOUND_CLICK: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        CONTACT: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        ENGAGEMENT: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        STORE_VISIT: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        STORE_SALE: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        QUALIFIED_LEAD: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
        CONVERTED_LEAD: _ClassVar[ConversionActionCategoryEnum.ConversionActionCategory]
    UNSPECIFIED: ConversionActionCategoryEnum.ConversionActionCategory
    UNKNOWN: ConversionActionCategoryEnum.ConversionActionCategory
    DEFAULT: ConversionActionCategoryEnum.ConversionActionCategory
    PAGE_VIEW: ConversionActionCategoryEnum.ConversionActionCategory
    PURCHASE: ConversionActionCategoryEnum.ConversionActionCategory
    SIGNUP: ConversionActionCategoryEnum.ConversionActionCategory
    LEAD: ConversionActionCategoryEnum.ConversionActionCategory
    DOWNLOAD: ConversionActionCategoryEnum.ConversionActionCategory
    ADD_TO_CART: ConversionActionCategoryEnum.ConversionActionCategory
    BEGIN_CHECKOUT: ConversionActionCategoryEnum.ConversionActionCategory
    SUBSCRIBE_PAID: ConversionActionCategoryEnum.ConversionActionCategory
    PHONE_CALL_LEAD: ConversionActionCategoryEnum.ConversionActionCategory
    IMPORTED_LEAD: ConversionActionCategoryEnum.ConversionActionCategory
    SUBMIT_LEAD_FORM: ConversionActionCategoryEnum.ConversionActionCategory
    BOOK_APPOINTMENT: ConversionActionCategoryEnum.ConversionActionCategory
    REQUEST_QUOTE: ConversionActionCategoryEnum.ConversionActionCategory
    GET_DIRECTIONS: ConversionActionCategoryEnum.ConversionActionCategory
    OUTBOUND_CLICK: ConversionActionCategoryEnum.ConversionActionCategory
    CONTACT: ConversionActionCategoryEnum.ConversionActionCategory
    ENGAGEMENT: ConversionActionCategoryEnum.ConversionActionCategory
    STORE_VISIT: ConversionActionCategoryEnum.ConversionActionCategory
    STORE_SALE: ConversionActionCategoryEnum.ConversionActionCategory
    QUALIFIED_LEAD: ConversionActionCategoryEnum.ConversionActionCategory
    CONVERTED_LEAD: ConversionActionCategoryEnum.ConversionActionCategory

    def __init__(self) -> None:
        ...