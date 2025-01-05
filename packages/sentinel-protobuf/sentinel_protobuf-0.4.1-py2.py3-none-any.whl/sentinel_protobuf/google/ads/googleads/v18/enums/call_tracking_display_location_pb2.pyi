from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CallTrackingDisplayLocationEnum(_message.Message):
    __slots__ = ()

    class CallTrackingDisplayLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation]
        UNKNOWN: _ClassVar[CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation]
        AD: _ClassVar[CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation]
        LANDING_PAGE: _ClassVar[CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation]
    UNSPECIFIED: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    UNKNOWN: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    AD: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    LANDING_PAGE: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation

    def __init__(self) -> None:
        ...