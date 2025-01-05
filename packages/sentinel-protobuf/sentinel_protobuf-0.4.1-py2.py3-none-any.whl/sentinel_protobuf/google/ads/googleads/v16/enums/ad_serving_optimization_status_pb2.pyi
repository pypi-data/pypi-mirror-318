from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdServingOptimizationStatusEnum(_message.Message):
    __slots__ = ()

    class AdServingOptimizationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
        UNKNOWN: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
        OPTIMIZE: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
        CONVERSION_OPTIMIZE: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
        ROTATE: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
        ROTATE_INDEFINITELY: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
        UNAVAILABLE: _ClassVar[AdServingOptimizationStatusEnum.AdServingOptimizationStatus]
    UNSPECIFIED: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    UNKNOWN: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    OPTIMIZE: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    CONVERSION_OPTIMIZE: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    ROTATE: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    ROTATE_INDEFINITELY: AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    UNAVAILABLE: AdServingOptimizationStatusEnum.AdServingOptimizationStatus

    def __init__(self) -> None:
        ...