from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcRoute(_message.Message):
    __slots__ = ("name", "self_link", "create_time", "update_time", "labels", "description", "hostnames", "meshes", "gateways", "rules")
    class MethodMatch(_message.Message):
        __slots__ = ("type", "grpc_service", "grpc_method", "case_sensitive")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[GrpcRoute.MethodMatch.Type]
            EXACT: _ClassVar[GrpcRoute.MethodMatch.Type]
            REGULAR_EXPRESSION: _ClassVar[GrpcRoute.MethodMatch.Type]
        TYPE_UNSPECIFIED: GrpcRoute.MethodMatch.Type
        EXACT: GrpcRoute.MethodMatch.Type
        REGULAR_EXPRESSION: GrpcRoute.MethodMatch.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        GRPC_SERVICE_FIELD_NUMBER: _ClassVar[int]
        GRPC_METHOD_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        type: GrpcRoute.MethodMatch.Type
        grpc_service: str
        grpc_method: str
        case_sensitive: bool
        def __init__(self, type: _Optional[_Union[GrpcRoute.MethodMatch.Type, str]] = ..., grpc_service: _Optional[str] = ..., grpc_method: _Optional[str] = ..., case_sensitive: bool = ...) -> None: ...
    class HeaderMatch(_message.Message):
        __slots__ = ("type", "key", "value")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[GrpcRoute.HeaderMatch.Type]
            EXACT: _ClassVar[GrpcRoute.HeaderMatch.Type]
            REGULAR_EXPRESSION: _ClassVar[GrpcRoute.HeaderMatch.Type]
        TYPE_UNSPECIFIED: GrpcRoute.HeaderMatch.Type
        EXACT: GrpcRoute.HeaderMatch.Type
        REGULAR_EXPRESSION: GrpcRoute.HeaderMatch.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        type: GrpcRoute.HeaderMatch.Type
        key: str
        value: str
        def __init__(self, type: _Optional[_Union[GrpcRoute.HeaderMatch.Type, str]] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RouteMatch(_message.Message):
        __slots__ = ("method", "headers")
        METHOD_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        method: GrpcRoute.MethodMatch
        headers: _containers.RepeatedCompositeFieldContainer[GrpcRoute.HeaderMatch]
        def __init__(self, method: _Optional[_Union[GrpcRoute.MethodMatch, _Mapping]] = ..., headers: _Optional[_Iterable[_Union[GrpcRoute.HeaderMatch, _Mapping]]] = ...) -> None: ...
    class Destination(_message.Message):
        __slots__ = ("service_name", "weight")
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        weight: int
        def __init__(self, service_name: _Optional[str] = ..., weight: _Optional[int] = ...) -> None: ...
    class FaultInjectionPolicy(_message.Message):
        __slots__ = ("delay", "abort")
        class Delay(_message.Message):
            __slots__ = ("fixed_delay", "percentage")
            FIXED_DELAY_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            fixed_delay: _duration_pb2.Duration
            percentage: int
            def __init__(self, fixed_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., percentage: _Optional[int] = ...) -> None: ...
        class Abort(_message.Message):
            __slots__ = ("http_status", "percentage")
            HTTP_STATUS_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            http_status: int
            percentage: int
            def __init__(self, http_status: _Optional[int] = ..., percentage: _Optional[int] = ...) -> None: ...
        DELAY_FIELD_NUMBER: _ClassVar[int]
        ABORT_FIELD_NUMBER: _ClassVar[int]
        delay: GrpcRoute.FaultInjectionPolicy.Delay
        abort: GrpcRoute.FaultInjectionPolicy.Abort
        def __init__(self, delay: _Optional[_Union[GrpcRoute.FaultInjectionPolicy.Delay, _Mapping]] = ..., abort: _Optional[_Union[GrpcRoute.FaultInjectionPolicy.Abort, _Mapping]] = ...) -> None: ...
    class RetryPolicy(_message.Message):
        __slots__ = ("retry_conditions", "num_retries")
        RETRY_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
        retry_conditions: _containers.RepeatedScalarFieldContainer[str]
        num_retries: int
        def __init__(self, retry_conditions: _Optional[_Iterable[str]] = ..., num_retries: _Optional[int] = ...) -> None: ...
    class RouteAction(_message.Message):
        __slots__ = ("destinations", "fault_injection_policy", "timeout", "retry_policy")
        DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        FAULT_INJECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
        destinations: _containers.RepeatedCompositeFieldContainer[GrpcRoute.Destination]
        fault_injection_policy: GrpcRoute.FaultInjectionPolicy
        timeout: _duration_pb2.Duration
        retry_policy: GrpcRoute.RetryPolicy
        def __init__(self, destinations: _Optional[_Iterable[_Union[GrpcRoute.Destination, _Mapping]]] = ..., fault_injection_policy: _Optional[_Union[GrpcRoute.FaultInjectionPolicy, _Mapping]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retry_policy: _Optional[_Union[GrpcRoute.RetryPolicy, _Mapping]] = ...) -> None: ...
    class RouteRule(_message.Message):
        __slots__ = ("matches", "action")
        MATCHES_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        matches: _containers.RepeatedCompositeFieldContainer[GrpcRoute.RouteMatch]
        action: GrpcRoute.RouteAction
        def __init__(self, matches: _Optional[_Iterable[_Union[GrpcRoute.RouteMatch, _Mapping]]] = ..., action: _Optional[_Union[GrpcRoute.RouteAction, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    MESHES_FIELD_NUMBER: _ClassVar[int]
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    self_link: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    meshes: _containers.RepeatedScalarFieldContainer[str]
    gateways: _containers.RepeatedScalarFieldContainer[str]
    rules: _containers.RepeatedCompositeFieldContainer[GrpcRoute.RouteRule]
    def __init__(self, name: _Optional[str] = ..., self_link: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., hostnames: _Optional[_Iterable[str]] = ..., meshes: _Optional[_Iterable[str]] = ..., gateways: _Optional[_Iterable[str]] = ..., rules: _Optional[_Iterable[_Union[GrpcRoute.RouteRule, _Mapping]]] = ...) -> None: ...

class ListGrpcRoutesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGrpcRoutesResponse(_message.Message):
    __slots__ = ("grpc_routes", "next_page_token")
    GRPC_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    grpc_routes: _containers.RepeatedCompositeFieldContainer[GrpcRoute]
    next_page_token: str
    def __init__(self, grpc_routes: _Optional[_Iterable[_Union[GrpcRoute, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetGrpcRouteRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateGrpcRouteRequest(_message.Message):
    __slots__ = ("parent", "grpc_route_id", "grpc_route")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRPC_ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    GRPC_ROUTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    grpc_route_id: str
    grpc_route: GrpcRoute
    def __init__(self, parent: _Optional[str] = ..., grpc_route_id: _Optional[str] = ..., grpc_route: _Optional[_Union[GrpcRoute, _Mapping]] = ...) -> None: ...

class UpdateGrpcRouteRequest(_message.Message):
    __slots__ = ("update_mask", "grpc_route")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GRPC_ROUTE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    grpc_route: GrpcRoute
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., grpc_route: _Optional[_Union[GrpcRoute, _Mapping]] = ...) -> None: ...

class DeleteGrpcRouteRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
