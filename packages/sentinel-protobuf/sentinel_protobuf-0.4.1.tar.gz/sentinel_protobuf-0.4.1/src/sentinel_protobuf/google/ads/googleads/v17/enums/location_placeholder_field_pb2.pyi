from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocationPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class LocationPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        UNKNOWN: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        BUSINESS_NAME: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        ADDRESS_LINE_1: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        ADDRESS_LINE_2: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        CITY: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        PROVINCE: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        POSTAL_CODE: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        COUNTRY_CODE: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
        PHONE_NUMBER: _ClassVar[LocationPlaceholderFieldEnum.LocationPlaceholderField]
    UNSPECIFIED: LocationPlaceholderFieldEnum.LocationPlaceholderField
    UNKNOWN: LocationPlaceholderFieldEnum.LocationPlaceholderField
    BUSINESS_NAME: LocationPlaceholderFieldEnum.LocationPlaceholderField
    ADDRESS_LINE_1: LocationPlaceholderFieldEnum.LocationPlaceholderField
    ADDRESS_LINE_2: LocationPlaceholderFieldEnum.LocationPlaceholderField
    CITY: LocationPlaceholderFieldEnum.LocationPlaceholderField
    PROVINCE: LocationPlaceholderFieldEnum.LocationPlaceholderField
    POSTAL_CODE: LocationPlaceholderFieldEnum.LocationPlaceholderField
    COUNTRY_CODE: LocationPlaceholderFieldEnum.LocationPlaceholderField
    PHONE_NUMBER: LocationPlaceholderFieldEnum.LocationPlaceholderField

    def __init__(self) -> None:
        ...