from google.maps.routes.v1 import custom_route_pb2 as _custom_route_pb2
from google.maps.routes.v1 import fallback_info_pb2 as _fallback_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeCustomRoutesResponse(_message.Message):
    __slots__ = ('routes', 'fastest_route', 'shortest_route', 'fallback_info')

    class FallbackInfo(_message.Message):
        __slots__ = ('routing_mode', 'routing_mode_reason', 'route_objective')

        class FallbackRouteObjective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FALLBACK_ROUTE_OBJECTIVE_UNSPECIFIED: _ClassVar[ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective]
            FALLBACK_RATECARD_WITHOUT_TOLL_PRICE_DATA: _ClassVar[ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective]
        FALLBACK_ROUTE_OBJECTIVE_UNSPECIFIED: ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective
        FALLBACK_RATECARD_WITHOUT_TOLL_PRICE_DATA: ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective
        ROUTING_MODE_FIELD_NUMBER: _ClassVar[int]
        ROUTING_MODE_REASON_FIELD_NUMBER: _ClassVar[int]
        ROUTE_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
        routing_mode: _fallback_info_pb2.FallbackRoutingMode
        routing_mode_reason: _fallback_info_pb2.FallbackReason
        route_objective: ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective

        def __init__(self, routing_mode: _Optional[_Union[_fallback_info_pb2.FallbackRoutingMode, str]]=..., routing_mode_reason: _Optional[_Union[_fallback_info_pb2.FallbackReason, str]]=..., route_objective: _Optional[_Union[ComputeCustomRoutesResponse.FallbackInfo.FallbackRouteObjective, str]]=...) -> None:
            ...
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    FASTEST_ROUTE_FIELD_NUMBER: _ClassVar[int]
    SHORTEST_ROUTE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[_custom_route_pb2.CustomRoute]
    fastest_route: _custom_route_pb2.CustomRoute
    shortest_route: _custom_route_pb2.CustomRoute
    fallback_info: ComputeCustomRoutesResponse.FallbackInfo

    def __init__(self, routes: _Optional[_Iterable[_Union[_custom_route_pb2.CustomRoute, _Mapping]]]=..., fastest_route: _Optional[_Union[_custom_route_pb2.CustomRoute, _Mapping]]=..., shortest_route: _Optional[_Union[_custom_route_pb2.CustomRoute, _Mapping]]=..., fallback_info: _Optional[_Union[ComputeCustomRoutesResponse.FallbackInfo, _Mapping]]=...) -> None:
        ...