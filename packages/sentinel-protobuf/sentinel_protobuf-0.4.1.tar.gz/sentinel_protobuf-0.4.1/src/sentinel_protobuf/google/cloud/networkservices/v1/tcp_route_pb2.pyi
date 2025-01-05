from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TcpRoute(_message.Message):
    __slots__ = ('name', 'self_link', 'create_time', 'update_time', 'description', 'rules', 'meshes', 'gateways', 'labels')

    class RouteRule(_message.Message):
        __slots__ = ('matches', 'action')
        MATCHES_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        matches: _containers.RepeatedCompositeFieldContainer[TcpRoute.RouteMatch]
        action: TcpRoute.RouteAction

        def __init__(self, matches: _Optional[_Iterable[_Union[TcpRoute.RouteMatch, _Mapping]]]=..., action: _Optional[_Union[TcpRoute.RouteAction, _Mapping]]=...) -> None:
            ...

    class RouteMatch(_message.Message):
        __slots__ = ('address', 'port')
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        address: str
        port: str

        def __init__(self, address: _Optional[str]=..., port: _Optional[str]=...) -> None:
            ...

    class RouteAction(_message.Message):
        __slots__ = ('destinations', 'original_destination')
        DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        destinations: _containers.RepeatedCompositeFieldContainer[TcpRoute.RouteDestination]
        original_destination: bool

        def __init__(self, destinations: _Optional[_Iterable[_Union[TcpRoute.RouteDestination, _Mapping]]]=..., original_destination: bool=...) -> None:
            ...

    class RouteDestination(_message.Message):
        __slots__ = ('service_name', 'weight')
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        weight: int

        def __init__(self, service_name: _Optional[str]=..., weight: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    MESHES_FIELD_NUMBER: _ClassVar[int]
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    self_link: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    rules: _containers.RepeatedCompositeFieldContainer[TcpRoute.RouteRule]
    meshes: _containers.RepeatedScalarFieldContainer[str]
    gateways: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., self_link: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., rules: _Optional[_Iterable[_Union[TcpRoute.RouteRule, _Mapping]]]=..., meshes: _Optional[_Iterable[str]]=..., gateways: _Optional[_Iterable[str]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListTcpRoutesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTcpRoutesResponse(_message.Message):
    __slots__ = ('tcp_routes', 'next_page_token')
    TCP_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tcp_routes: _containers.RepeatedCompositeFieldContainer[TcpRoute]
    next_page_token: str

    def __init__(self, tcp_routes: _Optional[_Iterable[_Union[TcpRoute, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTcpRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTcpRouteRequest(_message.Message):
    __slots__ = ('parent', 'tcp_route_id', 'tcp_route')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TCP_ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    TCP_ROUTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tcp_route_id: str
    tcp_route: TcpRoute

    def __init__(self, parent: _Optional[str]=..., tcp_route_id: _Optional[str]=..., tcp_route: _Optional[_Union[TcpRoute, _Mapping]]=...) -> None:
        ...

class UpdateTcpRouteRequest(_message.Message):
    __slots__ = ('update_mask', 'tcp_route')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TCP_ROUTE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    tcp_route: TcpRoute

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., tcp_route: _Optional[_Union[TcpRoute, _Mapping]]=...) -> None:
        ...

class DeleteTcpRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...