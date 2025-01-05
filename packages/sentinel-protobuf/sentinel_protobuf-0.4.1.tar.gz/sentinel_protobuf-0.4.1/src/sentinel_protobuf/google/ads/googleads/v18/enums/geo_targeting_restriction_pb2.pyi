from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GeoTargetingRestrictionEnum(_message.Message):
    __slots__ = ()

    class GeoTargetingRestriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GeoTargetingRestrictionEnum.GeoTargetingRestriction]
        UNKNOWN: _ClassVar[GeoTargetingRestrictionEnum.GeoTargetingRestriction]
        LOCATION_OF_PRESENCE: _ClassVar[GeoTargetingRestrictionEnum.GeoTargetingRestriction]
    UNSPECIFIED: GeoTargetingRestrictionEnum.GeoTargetingRestriction
    UNKNOWN: GeoTargetingRestrictionEnum.GeoTargetingRestriction
    LOCATION_OF_PRESENCE: GeoTargetingRestrictionEnum.GeoTargetingRestriction

    def __init__(self) -> None:
        ...