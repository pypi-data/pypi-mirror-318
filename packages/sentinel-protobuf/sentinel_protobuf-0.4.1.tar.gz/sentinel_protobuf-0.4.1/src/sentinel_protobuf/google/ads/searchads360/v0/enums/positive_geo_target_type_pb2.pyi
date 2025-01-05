from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PositiveGeoTargetTypeEnum(_message.Message):
    __slots__ = ()

    class PositiveGeoTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
        UNKNOWN: _ClassVar[PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
        PRESENCE_OR_INTEREST: _ClassVar[PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
        SEARCH_INTEREST: _ClassVar[PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
        PRESENCE: _ClassVar[PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
    UNSPECIFIED: PositiveGeoTargetTypeEnum.PositiveGeoTargetType
    UNKNOWN: PositiveGeoTargetTypeEnum.PositiveGeoTargetType
    PRESENCE_OR_INTEREST: PositiveGeoTargetTypeEnum.PositiveGeoTargetType
    SEARCH_INTEREST: PositiveGeoTargetTypeEnum.PositiveGeoTargetType
    PRESENCE: PositiveGeoTargetTypeEnum.PositiveGeoTargetType

    def __init__(self) -> None:
        ...