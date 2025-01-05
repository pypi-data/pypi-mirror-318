from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FlightPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class FlightPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        UNKNOWN: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        DESTINATION_ID: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        ORIGIN_ID: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FLIGHT_DESCRIPTION: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        ORIGIN_NAME: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        DESTINATION_NAME: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FLIGHT_PRICE: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FORMATTED_PRICE: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FLIGHT_SALE_PRICE: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FORMATTED_SALE_PRICE: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        IMAGE_URL: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FINAL_URLS: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        FINAL_MOBILE_URLS: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        TRACKING_URL: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        ANDROID_APP_LINK: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        SIMILAR_DESTINATION_IDS: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        IOS_APP_LINK: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
        IOS_APP_STORE_ID: _ClassVar[FlightPlaceholderFieldEnum.FlightPlaceholderField]
    UNSPECIFIED: FlightPlaceholderFieldEnum.FlightPlaceholderField
    UNKNOWN: FlightPlaceholderFieldEnum.FlightPlaceholderField
    DESTINATION_ID: FlightPlaceholderFieldEnum.FlightPlaceholderField
    ORIGIN_ID: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FLIGHT_DESCRIPTION: FlightPlaceholderFieldEnum.FlightPlaceholderField
    ORIGIN_NAME: FlightPlaceholderFieldEnum.FlightPlaceholderField
    DESTINATION_NAME: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FLIGHT_PRICE: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FORMATTED_PRICE: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FLIGHT_SALE_PRICE: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FORMATTED_SALE_PRICE: FlightPlaceholderFieldEnum.FlightPlaceholderField
    IMAGE_URL: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FINAL_URLS: FlightPlaceholderFieldEnum.FlightPlaceholderField
    FINAL_MOBILE_URLS: FlightPlaceholderFieldEnum.FlightPlaceholderField
    TRACKING_URL: FlightPlaceholderFieldEnum.FlightPlaceholderField
    ANDROID_APP_LINK: FlightPlaceholderFieldEnum.FlightPlaceholderField
    SIMILAR_DESTINATION_IDS: FlightPlaceholderFieldEnum.FlightPlaceholderField
    IOS_APP_LINK: FlightPlaceholderFieldEnum.FlightPlaceholderField
    IOS_APP_STORE_ID: FlightPlaceholderFieldEnum.FlightPlaceholderField

    def __init__(self) -> None:
        ...