from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ReachPlanNetworkEnum(_message.Message):
    __slots__ = ()

    class ReachPlanNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReachPlanNetworkEnum.ReachPlanNetwork]
        UNKNOWN: _ClassVar[ReachPlanNetworkEnum.ReachPlanNetwork]
        YOUTUBE: _ClassVar[ReachPlanNetworkEnum.ReachPlanNetwork]
        GOOGLE_VIDEO_PARTNERS: _ClassVar[ReachPlanNetworkEnum.ReachPlanNetwork]
        YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS: _ClassVar[ReachPlanNetworkEnum.ReachPlanNetwork]
    UNSPECIFIED: ReachPlanNetworkEnum.ReachPlanNetwork
    UNKNOWN: ReachPlanNetworkEnum.ReachPlanNetwork
    YOUTUBE: ReachPlanNetworkEnum.ReachPlanNetwork
    GOOGLE_VIDEO_PARTNERS: ReachPlanNetworkEnum.ReachPlanNetwork
    YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS: ReachPlanNetworkEnum.ReachPlanNetwork

    def __init__(self) -> None:
        ...