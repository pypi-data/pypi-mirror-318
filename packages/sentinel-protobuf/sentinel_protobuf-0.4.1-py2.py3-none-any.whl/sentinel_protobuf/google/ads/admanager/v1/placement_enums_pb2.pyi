from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PlacementStatusEnum(_message.Message):
    __slots__ = ()

    class PlacementStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLACEMENT_STATUS_UNSPECIFIED: _ClassVar[PlacementStatusEnum.PlacementStatus]
        ACTIVE: _ClassVar[PlacementStatusEnum.PlacementStatus]
        INACTIVE: _ClassVar[PlacementStatusEnum.PlacementStatus]
        ARCHIVED: _ClassVar[PlacementStatusEnum.PlacementStatus]
    PLACEMENT_STATUS_UNSPECIFIED: PlacementStatusEnum.PlacementStatus
    ACTIVE: PlacementStatusEnum.PlacementStatus
    INACTIVE: PlacementStatusEnum.PlacementStatus
    ARCHIVED: PlacementStatusEnum.PlacementStatus

    def __init__(self) -> None:
        ...