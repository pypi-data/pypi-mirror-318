from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocationOwnershipTypeEnum(_message.Message):
    __slots__ = ()

    class LocationOwnershipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocationOwnershipTypeEnum.LocationOwnershipType]
        UNKNOWN: _ClassVar[LocationOwnershipTypeEnum.LocationOwnershipType]
        BUSINESS_OWNER: _ClassVar[LocationOwnershipTypeEnum.LocationOwnershipType]
        AFFILIATE: _ClassVar[LocationOwnershipTypeEnum.LocationOwnershipType]
    UNSPECIFIED: LocationOwnershipTypeEnum.LocationOwnershipType
    UNKNOWN: LocationOwnershipTypeEnum.LocationOwnershipType
    BUSINESS_OWNER: LocationOwnershipTypeEnum.LocationOwnershipType
    AFFILIATE: LocationOwnershipTypeEnum.LocationOwnershipType

    def __init__(self) -> None:
        ...