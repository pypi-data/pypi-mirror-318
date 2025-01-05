from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GeoTargetConstantStatusEnum(_message.Message):
    __slots__ = ()

    class GeoTargetConstantStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GeoTargetConstantStatusEnum.GeoTargetConstantStatus]
        UNKNOWN: _ClassVar[GeoTargetConstantStatusEnum.GeoTargetConstantStatus]
        ENABLED: _ClassVar[GeoTargetConstantStatusEnum.GeoTargetConstantStatus]
        REMOVAL_PLANNED: _ClassVar[GeoTargetConstantStatusEnum.GeoTargetConstantStatus]
    UNSPECIFIED: GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    UNKNOWN: GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    ENABLED: GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    REMOVAL_PLANNED: GeoTargetConstantStatusEnum.GeoTargetConstantStatus

    def __init__(self) -> None:
        ...