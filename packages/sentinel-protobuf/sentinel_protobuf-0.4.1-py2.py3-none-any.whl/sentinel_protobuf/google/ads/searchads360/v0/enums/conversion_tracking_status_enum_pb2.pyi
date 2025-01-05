from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionTrackingStatusEnum(_message.Message):
    __slots__ = ()

    class ConversionTrackingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionTrackingStatusEnum.ConversionTrackingStatus]
        UNKNOWN: _ClassVar[ConversionTrackingStatusEnum.ConversionTrackingStatus]
        NOT_CONVERSION_TRACKED: _ClassVar[ConversionTrackingStatusEnum.ConversionTrackingStatus]
        CONVERSION_TRACKING_MANAGED_BY_SELF: _ClassVar[ConversionTrackingStatusEnum.ConversionTrackingStatus]
        CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER: _ClassVar[ConversionTrackingStatusEnum.ConversionTrackingStatus]
        CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER: _ClassVar[ConversionTrackingStatusEnum.ConversionTrackingStatus]
    UNSPECIFIED: ConversionTrackingStatusEnum.ConversionTrackingStatus
    UNKNOWN: ConversionTrackingStatusEnum.ConversionTrackingStatus
    NOT_CONVERSION_TRACKED: ConversionTrackingStatusEnum.ConversionTrackingStatus
    CONVERSION_TRACKING_MANAGED_BY_SELF: ConversionTrackingStatusEnum.ConversionTrackingStatus
    CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER: ConversionTrackingStatusEnum.ConversionTrackingStatus
    CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER: ConversionTrackingStatusEnum.ConversionTrackingStatus

    def __init__(self) -> None:
        ...