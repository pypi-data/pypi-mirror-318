from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkconnectivity.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyBasedRoute(_message.Message):
    __slots__ = ('virtual_machine', 'interconnect_attachment', 'next_hop_ilb_ip', 'next_hop_other_routes', 'name', 'create_time', 'update_time', 'labels', 'description', 'network', 'filter', 'priority', 'warnings', 'self_link', 'kind')

    class OtherRoutes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OTHER_ROUTES_UNSPECIFIED: _ClassVar[PolicyBasedRoute.OtherRoutes]
        DEFAULT_ROUTING: _ClassVar[PolicyBasedRoute.OtherRoutes]
    OTHER_ROUTES_UNSPECIFIED: PolicyBasedRoute.OtherRoutes
    DEFAULT_ROUTING: PolicyBasedRoute.OtherRoutes

    class VirtualMachine(_message.Message):
        __slots__ = ('tags',)
        TAGS_FIELD_NUMBER: _ClassVar[int]
        tags: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, tags: _Optional[_Iterable[str]]=...) -> None:
            ...

    class InterconnectAttachment(_message.Message):
        __slots__ = ('region',)
        REGION_FIELD_NUMBER: _ClassVar[int]
        region: str

        def __init__(self, region: _Optional[str]=...) -> None:
            ...

    class Filter(_message.Message):
        __slots__ = ('ip_protocol', 'src_range', 'dest_range', 'protocol_version')

        class ProtocolVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PROTOCOL_VERSION_UNSPECIFIED: _ClassVar[PolicyBasedRoute.Filter.ProtocolVersion]
            IPV4: _ClassVar[PolicyBasedRoute.Filter.ProtocolVersion]
        PROTOCOL_VERSION_UNSPECIFIED: PolicyBasedRoute.Filter.ProtocolVersion
        IPV4: PolicyBasedRoute.Filter.ProtocolVersion
        IP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        SRC_RANGE_FIELD_NUMBER: _ClassVar[int]
        DEST_RANGE_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        ip_protocol: str
        src_range: str
        dest_range: str
        protocol_version: PolicyBasedRoute.Filter.ProtocolVersion

        def __init__(self, ip_protocol: _Optional[str]=..., src_range: _Optional[str]=..., dest_range: _Optional[str]=..., protocol_version: _Optional[_Union[PolicyBasedRoute.Filter.ProtocolVersion, str]]=...) -> None:
            ...

    class Warnings(_message.Message):
        __slots__ = ('code', 'data', 'warning_message')

        class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WARNING_UNSPECIFIED: _ClassVar[PolicyBasedRoute.Warnings.Code]
            RESOURCE_NOT_ACTIVE: _ClassVar[PolicyBasedRoute.Warnings.Code]
            RESOURCE_BEING_MODIFIED: _ClassVar[PolicyBasedRoute.Warnings.Code]
        WARNING_UNSPECIFIED: PolicyBasedRoute.Warnings.Code
        RESOURCE_NOT_ACTIVE: PolicyBasedRoute.Warnings.Code
        RESOURCE_BEING_MODIFIED: PolicyBasedRoute.Warnings.Code

        class DataEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        CODE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        WARNING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: PolicyBasedRoute.Warnings.Code
        data: _containers.ScalarMap[str, str]
        warning_message: str

        def __init__(self, code: _Optional[_Union[PolicyBasedRoute.Warnings.Code, str]]=..., data: _Optional[_Mapping[str, str]]=..., warning_message: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_ILB_IP_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_OTHER_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    virtual_machine: PolicyBasedRoute.VirtualMachine
    interconnect_attachment: PolicyBasedRoute.InterconnectAttachment
    next_hop_ilb_ip: str
    next_hop_other_routes: PolicyBasedRoute.OtherRoutes
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    network: str
    filter: PolicyBasedRoute.Filter
    priority: int
    warnings: _containers.RepeatedCompositeFieldContainer[PolicyBasedRoute.Warnings]
    self_link: str
    kind: str

    def __init__(self, virtual_machine: _Optional[_Union[PolicyBasedRoute.VirtualMachine, _Mapping]]=..., interconnect_attachment: _Optional[_Union[PolicyBasedRoute.InterconnectAttachment, _Mapping]]=..., next_hop_ilb_ip: _Optional[str]=..., next_hop_other_routes: _Optional[_Union[PolicyBasedRoute.OtherRoutes, str]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., network: _Optional[str]=..., filter: _Optional[_Union[PolicyBasedRoute.Filter, _Mapping]]=..., priority: _Optional[int]=..., warnings: _Optional[_Iterable[_Union[PolicyBasedRoute.Warnings, _Mapping]]]=..., self_link: _Optional[str]=..., kind: _Optional[str]=...) -> None:
        ...

class ListPolicyBasedRoutesRequest(_message.Message):
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

class ListPolicyBasedRoutesResponse(_message.Message):
    __slots__ = ('policy_based_routes', 'next_page_token', 'unreachable')
    POLICY_BASED_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    policy_based_routes: _containers.RepeatedCompositeFieldContainer[PolicyBasedRoute]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, policy_based_routes: _Optional[_Iterable[_Union[PolicyBasedRoute, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetPolicyBasedRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePolicyBasedRouteRequest(_message.Message):
    __slots__ = ('parent', 'policy_based_route_id', 'policy_based_route', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_BASED_ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_BASED_ROUTE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy_based_route_id: str
    policy_based_route: PolicyBasedRoute
    request_id: str

    def __init__(self, parent: _Optional[str]=..., policy_based_route_id: _Optional[str]=..., policy_based_route: _Optional[_Union[PolicyBasedRoute, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeletePolicyBasedRouteRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...