from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PerformanceMaxUpgradeStatusEnum(_message.Message):
    __slots__ = ()

    class PerformanceMaxUpgradeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus]
        UNKNOWN: _ClassVar[PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus]
        UPGRADE_IN_PROGRESS: _ClassVar[PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus]
        UPGRADE_COMPLETE: _ClassVar[PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus]
        UPGRADE_FAILED: _ClassVar[PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus]
        UPGRADE_ELIGIBLE: _ClassVar[PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus]
    UNSPECIFIED: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    UNKNOWN: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    UPGRADE_IN_PROGRESS: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    UPGRADE_COMPLETE: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    UPGRADE_FAILED: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    UPGRADE_ELIGIBLE: PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus

    def __init__(self) -> None:
        ...