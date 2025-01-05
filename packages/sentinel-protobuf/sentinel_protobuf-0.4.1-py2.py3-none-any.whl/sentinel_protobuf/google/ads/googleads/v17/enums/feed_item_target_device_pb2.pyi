from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemTargetDeviceEnum(_message.Message):
    __slots__ = ()

    class FeedItemTargetDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemTargetDeviceEnum.FeedItemTargetDevice]
        UNKNOWN: _ClassVar[FeedItemTargetDeviceEnum.FeedItemTargetDevice]
        MOBILE: _ClassVar[FeedItemTargetDeviceEnum.FeedItemTargetDevice]
    UNSPECIFIED: FeedItemTargetDeviceEnum.FeedItemTargetDevice
    UNKNOWN: FeedItemTargetDeviceEnum.FeedItemTargetDevice
    MOBILE: FeedItemTargetDeviceEnum.FeedItemTargetDevice

    def __init__(self) -> None:
        ...