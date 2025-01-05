from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PlacementTypeEnum(_message.Message):
    __slots__ = ()

    class PlacementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PlacementTypeEnum.PlacementType]
        UNKNOWN: _ClassVar[PlacementTypeEnum.PlacementType]
        WEBSITE: _ClassVar[PlacementTypeEnum.PlacementType]
        MOBILE_APP_CATEGORY: _ClassVar[PlacementTypeEnum.PlacementType]
        MOBILE_APPLICATION: _ClassVar[PlacementTypeEnum.PlacementType]
        YOUTUBE_VIDEO: _ClassVar[PlacementTypeEnum.PlacementType]
        YOUTUBE_CHANNEL: _ClassVar[PlacementTypeEnum.PlacementType]
        GOOGLE_PRODUCTS: _ClassVar[PlacementTypeEnum.PlacementType]
    UNSPECIFIED: PlacementTypeEnum.PlacementType
    UNKNOWN: PlacementTypeEnum.PlacementType
    WEBSITE: PlacementTypeEnum.PlacementType
    MOBILE_APP_CATEGORY: PlacementTypeEnum.PlacementType
    MOBILE_APPLICATION: PlacementTypeEnum.PlacementType
    YOUTUBE_VIDEO: PlacementTypeEnum.PlacementType
    YOUTUBE_CHANNEL: PlacementTypeEnum.PlacementType
    GOOGLE_PRODUCTS: PlacementTypeEnum.PlacementType

    def __init__(self) -> None:
        ...