from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BrandStateEnum(_message.Message):
    __slots__ = ()

    class BrandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BrandStateEnum.BrandState]
        UNKNOWN: _ClassVar[BrandStateEnum.BrandState]
        ENABLED: _ClassVar[BrandStateEnum.BrandState]
        DEPRECATED: _ClassVar[BrandStateEnum.BrandState]
        UNVERIFIED: _ClassVar[BrandStateEnum.BrandState]
        APPROVED: _ClassVar[BrandStateEnum.BrandState]
        CANCELLED: _ClassVar[BrandStateEnum.BrandState]
        REJECTED: _ClassVar[BrandStateEnum.BrandState]
    UNSPECIFIED: BrandStateEnum.BrandState
    UNKNOWN: BrandStateEnum.BrandState
    ENABLED: BrandStateEnum.BrandState
    DEPRECATED: BrandStateEnum.BrandState
    UNVERIFIED: BrandStateEnum.BrandState
    APPROVED: BrandStateEnum.BrandState
    CANCELLED: BrandStateEnum.BrandState
    REJECTED: BrandStateEnum.BrandState

    def __init__(self) -> None:
        ...