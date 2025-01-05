from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RouteLabel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_LABEL_UNSPECIFIED: _ClassVar[RouteLabel]
    DEFAULT_ROUTE: _ClassVar[RouteLabel]
    DEFAULT_ROUTE_ALTERNATE: _ClassVar[RouteLabel]
    FUEL_EFFICIENT: _ClassVar[RouteLabel]
    SHORTER_DISTANCE: _ClassVar[RouteLabel]
ROUTE_LABEL_UNSPECIFIED: RouteLabel
DEFAULT_ROUTE: RouteLabel
DEFAULT_ROUTE_ALTERNATE: RouteLabel
FUEL_EFFICIENT: RouteLabel
SHORTER_DISTANCE: RouteLabel