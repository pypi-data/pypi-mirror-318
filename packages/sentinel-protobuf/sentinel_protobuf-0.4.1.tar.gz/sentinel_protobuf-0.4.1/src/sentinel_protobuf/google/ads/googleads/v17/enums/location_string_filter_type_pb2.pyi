from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocationStringFilterTypeEnum(_message.Message):
    __slots__ = ()

    class LocationStringFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocationStringFilterTypeEnum.LocationStringFilterType]
        UNKNOWN: _ClassVar[LocationStringFilterTypeEnum.LocationStringFilterType]
        EXACT: _ClassVar[LocationStringFilterTypeEnum.LocationStringFilterType]
    UNSPECIFIED: LocationStringFilterTypeEnum.LocationStringFilterType
    UNKNOWN: LocationStringFilterTypeEnum.LocationStringFilterType
    EXACT: LocationStringFilterTypeEnum.LocationStringFilterType

    def __init__(self) -> None:
        ...