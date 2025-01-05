from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocationSourceTypeEnum(_message.Message):
    __slots__ = ()

    class LocationSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocationSourceTypeEnum.LocationSourceType]
        UNKNOWN: _ClassVar[LocationSourceTypeEnum.LocationSourceType]
        GOOGLE_MY_BUSINESS: _ClassVar[LocationSourceTypeEnum.LocationSourceType]
        AFFILIATE: _ClassVar[LocationSourceTypeEnum.LocationSourceType]
    UNSPECIFIED: LocationSourceTypeEnum.LocationSourceType
    UNKNOWN: LocationSourceTypeEnum.LocationSourceType
    GOOGLE_MY_BUSINESS: LocationSourceTypeEnum.LocationSourceType
    AFFILIATE: LocationSourceTypeEnum.LocationSourceType

    def __init__(self) -> None:
        ...