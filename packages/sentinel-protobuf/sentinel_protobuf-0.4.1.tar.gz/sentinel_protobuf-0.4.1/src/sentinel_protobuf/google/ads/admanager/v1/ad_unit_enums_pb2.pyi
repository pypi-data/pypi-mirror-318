from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdUnitStatusEnum(_message.Message):
    __slots__ = ()

    class AdUnitStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AD_UNIT_STATUS_UNSPECIFIED: _ClassVar[AdUnitStatusEnum.AdUnitStatus]
        ACTIVE: _ClassVar[AdUnitStatusEnum.AdUnitStatus]
        INACTIVE: _ClassVar[AdUnitStatusEnum.AdUnitStatus]
        ARCHIVED: _ClassVar[AdUnitStatusEnum.AdUnitStatus]
    AD_UNIT_STATUS_UNSPECIFIED: AdUnitStatusEnum.AdUnitStatus
    ACTIVE: AdUnitStatusEnum.AdUnitStatus
    INACTIVE: AdUnitStatusEnum.AdUnitStatus
    ARCHIVED: AdUnitStatusEnum.AdUnitStatus

    def __init__(self) -> None:
        ...

class SmartSizeModeEnum(_message.Message):
    __slots__ = ()

    class SmartSizeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SMART_SIZE_MODE_UNSPECIFIED: _ClassVar[SmartSizeModeEnum.SmartSizeMode]
        NONE: _ClassVar[SmartSizeModeEnum.SmartSizeMode]
        SMART_BANNER: _ClassVar[SmartSizeModeEnum.SmartSizeMode]
        DYNAMIC_SIZE: _ClassVar[SmartSizeModeEnum.SmartSizeMode]
    SMART_SIZE_MODE_UNSPECIFIED: SmartSizeModeEnum.SmartSizeMode
    NONE: SmartSizeModeEnum.SmartSizeMode
    SMART_BANNER: SmartSizeModeEnum.SmartSizeMode
    DYNAMIC_SIZE: SmartSizeModeEnum.SmartSizeMode

    def __init__(self) -> None:
        ...

class TargetWindowEnum(_message.Message):
    __slots__ = ()

    class TargetWindow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_WINDOW_UNSPECIFIED: _ClassVar[TargetWindowEnum.TargetWindow]
        TOP: _ClassVar[TargetWindowEnum.TargetWindow]
        BLANK: _ClassVar[TargetWindowEnum.TargetWindow]
    TARGET_WINDOW_UNSPECIFIED: TargetWindowEnum.TargetWindow
    TOP: TargetWindowEnum.TargetWindow
    BLANK: TargetWindowEnum.TargetWindow

    def __init__(self) -> None:
        ...