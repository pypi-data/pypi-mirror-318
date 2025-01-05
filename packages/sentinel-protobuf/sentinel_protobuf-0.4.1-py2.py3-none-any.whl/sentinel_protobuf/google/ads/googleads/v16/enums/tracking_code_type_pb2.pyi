from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TrackingCodeTypeEnum(_message.Message):
    __slots__ = ()

    class TrackingCodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TrackingCodeTypeEnum.TrackingCodeType]
        UNKNOWN: _ClassVar[TrackingCodeTypeEnum.TrackingCodeType]
        WEBPAGE: _ClassVar[TrackingCodeTypeEnum.TrackingCodeType]
        WEBPAGE_ONCLICK: _ClassVar[TrackingCodeTypeEnum.TrackingCodeType]
        CLICK_TO_CALL: _ClassVar[TrackingCodeTypeEnum.TrackingCodeType]
        WEBSITE_CALL: _ClassVar[TrackingCodeTypeEnum.TrackingCodeType]
    UNSPECIFIED: TrackingCodeTypeEnum.TrackingCodeType
    UNKNOWN: TrackingCodeTypeEnum.TrackingCodeType
    WEBPAGE: TrackingCodeTypeEnum.TrackingCodeType
    WEBPAGE_ONCLICK: TrackingCodeTypeEnum.TrackingCodeType
    CLICK_TO_CALL: TrackingCodeTypeEnum.TrackingCodeType
    WEBSITE_CALL: TrackingCodeTypeEnum.TrackingCodeType

    def __init__(self) -> None:
        ...