from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetPerformanceLabelEnum(_message.Message):
    __slots__ = ()

    class AssetPerformanceLabel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
        UNKNOWN: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
        PENDING: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
        LEARNING: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
        LOW: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
        GOOD: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
        BEST: _ClassVar[AssetPerformanceLabelEnum.AssetPerformanceLabel]
    UNSPECIFIED: AssetPerformanceLabelEnum.AssetPerformanceLabel
    UNKNOWN: AssetPerformanceLabelEnum.AssetPerformanceLabel
    PENDING: AssetPerformanceLabelEnum.AssetPerformanceLabel
    LEARNING: AssetPerformanceLabelEnum.AssetPerformanceLabel
    LOW: AssetPerformanceLabelEnum.AssetPerformanceLabel
    GOOD: AssetPerformanceLabelEnum.AssetPerformanceLabel
    BEST: AssetPerformanceLabelEnum.AssetPerformanceLabel

    def __init__(self) -> None:
        ...