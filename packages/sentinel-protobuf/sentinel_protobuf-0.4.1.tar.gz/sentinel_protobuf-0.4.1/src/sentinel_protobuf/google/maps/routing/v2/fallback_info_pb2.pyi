from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FallbackReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FALLBACK_REASON_UNSPECIFIED: _ClassVar[FallbackReason]
    SERVER_ERROR: _ClassVar[FallbackReason]
    LATENCY_EXCEEDED: _ClassVar[FallbackReason]

class FallbackRoutingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FALLBACK_ROUTING_MODE_UNSPECIFIED: _ClassVar[FallbackRoutingMode]
    FALLBACK_TRAFFIC_UNAWARE: _ClassVar[FallbackRoutingMode]
    FALLBACK_TRAFFIC_AWARE: _ClassVar[FallbackRoutingMode]
FALLBACK_REASON_UNSPECIFIED: FallbackReason
SERVER_ERROR: FallbackReason
LATENCY_EXCEEDED: FallbackReason
FALLBACK_ROUTING_MODE_UNSPECIFIED: FallbackRoutingMode
FALLBACK_TRAFFIC_UNAWARE: FallbackRoutingMode
FALLBACK_TRAFFIC_AWARE: FallbackRoutingMode

class FallbackInfo(_message.Message):
    __slots__ = ('routing_mode', 'reason')
    ROUTING_MODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    routing_mode: FallbackRoutingMode
    reason: FallbackReason

    def __init__(self, routing_mode: _Optional[_Union[FallbackRoutingMode, str]]=..., reason: _Optional[_Union[FallbackReason, str]]=...) -> None:
        ...