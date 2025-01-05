from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TlsRoute(_message.Message):
    __slots__ = ('name', 'self_link', 'create_time', 'update_time', 'description', 'rules', 'meshes', 'gateways')

    class RouteRule(_message.Message):
        __slots__ = ('matches', 'action')
        MATCHES_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        matches: _containers.RepeatedCompositeFieldContainer[TlsRoute.RouteMatch]
        action: TlsRoute.RouteAction

        def __init__(self, matches: _Optional[_Iterable[_Union[TlsRoute.RouteMatch, _Mapping]]]=..., action: _Optional[_Union[TlsRoute.RouteAction, _Mapping]]=...) -> None:
            ...

    class RouteMatch(_message.Message):
        __slots__ = ('sni_host', 'alpn')
        SNI_HOST_FIELD_NUMBER: _ClassVar[int]
        ALPN_FIELD_NUMBER: _ClassVar[int]
        sni_host: _containers.RepeatedScalarFieldContainer[str]
        alpn: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, sni_host: _Optional[_Iterable[str]]=..., alpn: _Optional[_Iterable[str]]=...) -> None:
            ...

    class RouteAction(_message.Message):
        __slots__ = ('destinations',)
        DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        destinations: _containers.RepeatedCompositeFieldContainer[TlsRoute.RouteDestination]

        def __init__(self, destinations: _Optional[_Iterable[_Union[TlsRoute.RouteDestination, _Mapping]]]=...) -> None:
            ...

    class RouteDestination(_message.Message):
        __slots__ = ('service_name', 'weight')
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        weight: int

        def __init__(self, service_name: _Optional[str]=..., weight: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    MESHES_FIELD_NUMBER: _ClassVar[int]
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    self_link: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    rules: _containers.RepeatedCompositeFieldContainer[TlsRoute.RouteRule]
    meshes: _containers.RepeatedScalarFieldContainer[str]
    gateways: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., self_link: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., rules: _Optional[_Iterable[_Union[TlsRoute.RouteRule, _Mapping]]]=..., meshes: _Optional[_Iterable[str]]=..., gateways: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListTlsRoutesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTlsRoutesResponse(_message.Message):
    __slots__ = ('tls_routes', 'next_page_token')
    TLS_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tls_routes: _containers.RepeatedCompositeFieldContainer[TlsRoute]
    next_page_token: str

    def __init__(self, tls_routes: _Optional[_Iterable[_Union[TlsRoute, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTlsRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTlsRouteRequest(_message.Message):
    __slots__ = ('parent', 'tls_route_id', 'tls_route')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TLS_ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    TLS_ROUTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tls_route_id: str
    tls_route: TlsRoute

    def __init__(self, parent: _Optional[str]=..., tls_route_id: _Optional[str]=..., tls_route: _Optional[_Union[TlsRoute, _Mapping]]=...) -> None:
        ...

class UpdateTlsRouteRequest(_message.Message):
    __slots__ = ('update_mask', 'tls_route')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TLS_ROUTE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    tls_route: TlsRoute

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., tls_route: _Optional[_Union[TlsRoute, _Mapping]]=...) -> None:
        ...

class DeleteTlsRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...