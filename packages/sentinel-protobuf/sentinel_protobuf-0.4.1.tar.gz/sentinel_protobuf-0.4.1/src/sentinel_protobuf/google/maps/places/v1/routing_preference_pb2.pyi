from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RoutingPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_PREFERENCE_UNSPECIFIED: _ClassVar[RoutingPreference]
    TRAFFIC_UNAWARE: _ClassVar[RoutingPreference]
    TRAFFIC_AWARE: _ClassVar[RoutingPreference]
    TRAFFIC_AWARE_OPTIMAL: _ClassVar[RoutingPreference]
ROUTING_PREFERENCE_UNSPECIFIED: RoutingPreference
TRAFFIC_UNAWARE: RoutingPreference
TRAFFIC_AWARE: RoutingPreference
TRAFFIC_AWARE_OPTIMAL: RoutingPreference