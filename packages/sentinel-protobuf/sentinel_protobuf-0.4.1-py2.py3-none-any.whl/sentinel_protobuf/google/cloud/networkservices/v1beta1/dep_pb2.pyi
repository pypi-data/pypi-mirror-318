from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkservices.v1beta1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_TYPE_UNSPECIFIED: _ClassVar[EventType]
    REQUEST_HEADERS: _ClassVar[EventType]
    REQUEST_BODY: _ClassVar[EventType]
    RESPONSE_HEADERS: _ClassVar[EventType]
    RESPONSE_BODY: _ClassVar[EventType]
    REQUEST_TRAILERS: _ClassVar[EventType]
    RESPONSE_TRAILERS: _ClassVar[EventType]

class LoadBalancingScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOAD_BALANCING_SCHEME_UNSPECIFIED: _ClassVar[LoadBalancingScheme]
    INTERNAL_MANAGED: _ClassVar[LoadBalancingScheme]
    EXTERNAL_MANAGED: _ClassVar[LoadBalancingScheme]
EVENT_TYPE_UNSPECIFIED: EventType
REQUEST_HEADERS: EventType
REQUEST_BODY: EventType
RESPONSE_HEADERS: EventType
RESPONSE_BODY: EventType
REQUEST_TRAILERS: EventType
RESPONSE_TRAILERS: EventType
LOAD_BALANCING_SCHEME_UNSPECIFIED: LoadBalancingScheme
INTERNAL_MANAGED: LoadBalancingScheme
EXTERNAL_MANAGED: LoadBalancingScheme

class ExtensionChain(_message.Message):
    __slots__ = ('name', 'match_condition', 'extensions')

    class MatchCondition(_message.Message):
        __slots__ = ('cel_expression',)
        CEL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        cel_expression: str

        def __init__(self, cel_expression: _Optional[str]=...) -> None:
            ...

    class Extension(_message.Message):
        __slots__ = ('name', 'authority', 'service', 'supported_events', 'timeout', 'fail_open', 'forward_headers')
        NAME_FIELD_NUMBER: _ClassVar[int]
        AUTHORITY_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_EVENTS_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        FAIL_OPEN_FIELD_NUMBER: _ClassVar[int]
        FORWARD_HEADERS_FIELD_NUMBER: _ClassVar[int]
        name: str
        authority: str
        service: str
        supported_events: _containers.RepeatedScalarFieldContainer[EventType]
        timeout: _duration_pb2.Duration
        fail_open: bool
        forward_headers: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, name: _Optional[str]=..., authority: _Optional[str]=..., service: _Optional[str]=..., supported_events: _Optional[_Iterable[_Union[EventType, str]]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., fail_open: bool=..., forward_headers: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MATCH_CONDITION_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    match_condition: ExtensionChain.MatchCondition
    extensions: _containers.RepeatedCompositeFieldContainer[ExtensionChain.Extension]

    def __init__(self, name: _Optional[str]=..., match_condition: _Optional[_Union[ExtensionChain.MatchCondition, _Mapping]]=..., extensions: _Optional[_Iterable[_Union[ExtensionChain.Extension, _Mapping]]]=...) -> None:
        ...

class LbTrafficExtension(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'description', 'labels', 'forwarding_rules', 'extension_chains', 'load_balancing_scheme')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULES_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_CHAINS_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCING_SCHEME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    forwarding_rules: _containers.RepeatedScalarFieldContainer[str]
    extension_chains: _containers.RepeatedCompositeFieldContainer[ExtensionChain]
    load_balancing_scheme: LoadBalancingScheme

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., forwarding_rules: _Optional[_Iterable[str]]=..., extension_chains: _Optional[_Iterable[_Union[ExtensionChain, _Mapping]]]=..., load_balancing_scheme: _Optional[_Union[LoadBalancingScheme, str]]=...) -> None:
        ...

class ListLbTrafficExtensionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListLbTrafficExtensionsResponse(_message.Message):
    __slots__ = ('lb_traffic_extensions', 'next_page_token', 'unreachable')
    LB_TRAFFIC_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    lb_traffic_extensions: _containers.RepeatedCompositeFieldContainer[LbTrafficExtension]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, lb_traffic_extensions: _Optional[_Iterable[_Union[LbTrafficExtension, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetLbTrafficExtensionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateLbTrafficExtensionRequest(_message.Message):
    __slots__ = ('parent', 'lb_traffic_extension_id', 'lb_traffic_extension', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LB_TRAFFIC_EXTENSION_ID_FIELD_NUMBER: _ClassVar[int]
    LB_TRAFFIC_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lb_traffic_extension_id: str
    lb_traffic_extension: LbTrafficExtension
    request_id: str

    def __init__(self, parent: _Optional[str]=..., lb_traffic_extension_id: _Optional[str]=..., lb_traffic_extension: _Optional[_Union[LbTrafficExtension, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateLbTrafficExtensionRequest(_message.Message):
    __slots__ = ('update_mask', 'lb_traffic_extension', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LB_TRAFFIC_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    lb_traffic_extension: LbTrafficExtension
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., lb_traffic_extension: _Optional[_Union[LbTrafficExtension, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteLbTrafficExtensionRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class LbRouteExtension(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'description', 'labels', 'forwarding_rules', 'extension_chains', 'load_balancing_scheme')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULES_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_CHAINS_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCING_SCHEME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    forwarding_rules: _containers.RepeatedScalarFieldContainer[str]
    extension_chains: _containers.RepeatedCompositeFieldContainer[ExtensionChain]
    load_balancing_scheme: LoadBalancingScheme

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., forwarding_rules: _Optional[_Iterable[str]]=..., extension_chains: _Optional[_Iterable[_Union[ExtensionChain, _Mapping]]]=..., load_balancing_scheme: _Optional[_Union[LoadBalancingScheme, str]]=...) -> None:
        ...

class ListLbRouteExtensionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListLbRouteExtensionsResponse(_message.Message):
    __slots__ = ('lb_route_extensions', 'next_page_token', 'unreachable')
    LB_ROUTE_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    lb_route_extensions: _containers.RepeatedCompositeFieldContainer[LbRouteExtension]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, lb_route_extensions: _Optional[_Iterable[_Union[LbRouteExtension, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetLbRouteExtensionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateLbRouteExtensionRequest(_message.Message):
    __slots__ = ('parent', 'lb_route_extension_id', 'lb_route_extension', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LB_ROUTE_EXTENSION_ID_FIELD_NUMBER: _ClassVar[int]
    LB_ROUTE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lb_route_extension_id: str
    lb_route_extension: LbRouteExtension
    request_id: str

    def __init__(self, parent: _Optional[str]=..., lb_route_extension_id: _Optional[str]=..., lb_route_extension: _Optional[_Union[LbRouteExtension, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateLbRouteExtensionRequest(_message.Message):
    __slots__ = ('update_mask', 'lb_route_extension', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LB_ROUTE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    lb_route_extension: LbRouteExtension
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., lb_route_extension: _Optional[_Union[LbRouteExtension, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteLbRouteExtensionRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...