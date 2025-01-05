from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TargetImpressionShareLocationEnum(_message.Message):
    __slots__ = ()

    class TargetImpressionShareLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TargetImpressionShareLocationEnum.TargetImpressionShareLocation]
        UNKNOWN: _ClassVar[TargetImpressionShareLocationEnum.TargetImpressionShareLocation]
        ANYWHERE_ON_PAGE: _ClassVar[TargetImpressionShareLocationEnum.TargetImpressionShareLocation]
        TOP_OF_PAGE: _ClassVar[TargetImpressionShareLocationEnum.TargetImpressionShareLocation]
        ABSOLUTE_TOP_OF_PAGE: _ClassVar[TargetImpressionShareLocationEnum.TargetImpressionShareLocation]
    UNSPECIFIED: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    UNKNOWN: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    ANYWHERE_ON_PAGE: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    TOP_OF_PAGE: TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    ABSOLUTE_TOP_OF_PAGE: TargetImpressionShareLocationEnum.TargetImpressionShareLocation

    def __init__(self) -> None:
        ...