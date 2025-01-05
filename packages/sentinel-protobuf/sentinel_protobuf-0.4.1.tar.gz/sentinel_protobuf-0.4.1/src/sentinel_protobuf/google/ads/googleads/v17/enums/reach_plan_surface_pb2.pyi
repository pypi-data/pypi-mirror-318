from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ReachPlanSurfaceEnum(_message.Message):
    __slots__ = ()

    class ReachPlanSurface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
        UNKNOWN: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
        IN_FEED: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
        IN_STREAM_BUMPER: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
        IN_STREAM_NON_SKIPPABLE: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
        IN_STREAM_SKIPPABLE: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
        SHORTS: _ClassVar[ReachPlanSurfaceEnum.ReachPlanSurface]
    UNSPECIFIED: ReachPlanSurfaceEnum.ReachPlanSurface
    UNKNOWN: ReachPlanSurfaceEnum.ReachPlanSurface
    IN_FEED: ReachPlanSurfaceEnum.ReachPlanSurface
    IN_STREAM_BUMPER: ReachPlanSurfaceEnum.ReachPlanSurface
    IN_STREAM_NON_SKIPPABLE: ReachPlanSurfaceEnum.ReachPlanSurface
    IN_STREAM_SKIPPABLE: ReachPlanSurfaceEnum.ReachPlanSurface
    SHORTS: ReachPlanSurfaceEnum.ReachPlanSurface

    def __init__(self) -> None:
        ...