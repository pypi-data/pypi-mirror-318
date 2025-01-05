from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.edgenetwork.v1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListZonesRequest(_message.Message):
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

class ListZonesResponse(_message.Message):
    __slots__ = ('zones', 'next_page_token', 'unreachable')
    ZONES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    zones: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Zone]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, zones: _Optional[_Iterable[_Union[_resources_pb2.Zone, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetZoneRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNetworksRequest(_message.Message):
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

class ListNetworksResponse(_message.Message):
    __slots__ = ('networks', 'next_page_token', 'unreachable')
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Network]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, networks: _Optional[_Iterable[_Union[_resources_pb2.Network, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetNetworkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateNetworkRequest(_message.Message):
    __slots__ = ('parent', 'network_id', 'network', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    network_id: str
    network: _resources_pb2.Network
    request_id: str

    def __init__(self, parent: _Optional[str]=..., network_id: _Optional[str]=..., network: _Optional[_Union[_resources_pb2.Network, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteNetworkRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListSubnetsRequest(_message.Message):
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

class ListSubnetsResponse(_message.Message):
    __slots__ = ('subnets', 'next_page_token', 'unreachable')
    SUBNETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    subnets: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Subnet]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, subnets: _Optional[_Iterable[_Union[_resources_pb2.Subnet, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSubnetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSubnetRequest(_message.Message):
    __slots__ = ('parent', 'subnet_id', 'subnet', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    subnet_id: str
    subnet: _resources_pb2.Subnet
    request_id: str

    def __init__(self, parent: _Optional[str]=..., subnet_id: _Optional[str]=..., subnet: _Optional[_Union[_resources_pb2.Subnet, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSubnetRequest(_message.Message):
    __slots__ = ('update_mask', 'subnet', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    subnet: _resources_pb2.Subnet
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., subnet: _Optional[_Union[_resources_pb2.Subnet, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSubnetRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListInterconnectsRequest(_message.Message):
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

class ListInterconnectsResponse(_message.Message):
    __slots__ = ('interconnects', 'next_page_token', 'unreachable')
    INTERCONNECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    interconnects: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Interconnect]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, interconnects: _Optional[_Iterable[_Union[_resources_pb2.Interconnect, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInterconnectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListInterconnectAttachmentsRequest(_message.Message):
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

class ListInterconnectAttachmentsResponse(_message.Message):
    __slots__ = ('interconnect_attachments', 'next_page_token', 'unreachable')
    INTERCONNECT_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    interconnect_attachments: _containers.RepeatedCompositeFieldContainer[_resources_pb2.InterconnectAttachment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, interconnect_attachments: _Optional[_Iterable[_Union[_resources_pb2.InterconnectAttachment, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInterconnectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInterconnectAttachmentRequest(_message.Message):
    __slots__ = ('parent', 'interconnect_attachment_id', 'interconnect_attachment', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    interconnect_attachment_id: str
    interconnect_attachment: _resources_pb2.InterconnectAttachment
    request_id: str

    def __init__(self, parent: _Optional[str]=..., interconnect_attachment_id: _Optional[str]=..., interconnect_attachment: _Optional[_Union[_resources_pb2.InterconnectAttachment, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInterconnectAttachmentRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListRoutersRequest(_message.Message):
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

class ListRoutersResponse(_message.Message):
    __slots__ = ('routers', 'next_page_token', 'unreachable')
    ROUTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    routers: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Router]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, routers: _Optional[_Iterable[_Union[_resources_pb2.Router, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRouterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRouterRequest(_message.Message):
    __slots__ = ('parent', 'router_id', 'router', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    router_id: str
    router: _resources_pb2.Router
    request_id: str

    def __init__(self, parent: _Optional[str]=..., router_id: _Optional[str]=..., router: _Optional[_Union[_resources_pb2.Router, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateRouterRequest(_message.Message):
    __slots__ = ('update_mask', 'router', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    router: _resources_pb2.Router
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., router: _Optional[_Union[_resources_pb2.Router, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteRouterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class DiagnoseNetworkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DiagnoseNetworkResponse(_message.Message):
    __slots__ = ('update_time', 'result')

    class NetworkStatus(_message.Message):
        __slots__ = ('subnet_status', 'macsec_status_internal_links')

        class MacsecStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MACSEC_STATUS_UNSPECIFIED: _ClassVar[DiagnoseNetworkResponse.NetworkStatus.MacsecStatus]
            SECURE: _ClassVar[DiagnoseNetworkResponse.NetworkStatus.MacsecStatus]
            UNSECURE: _ClassVar[DiagnoseNetworkResponse.NetworkStatus.MacsecStatus]
        MACSEC_STATUS_UNSPECIFIED: DiagnoseNetworkResponse.NetworkStatus.MacsecStatus
        SECURE: DiagnoseNetworkResponse.NetworkStatus.MacsecStatus
        UNSECURE: DiagnoseNetworkResponse.NetworkStatus.MacsecStatus
        SUBNET_STATUS_FIELD_NUMBER: _ClassVar[int]
        MACSEC_STATUS_INTERNAL_LINKS_FIELD_NUMBER: _ClassVar[int]
        subnet_status: _containers.RepeatedCompositeFieldContainer[_resources_pb2.SubnetStatus]
        macsec_status_internal_links: DiagnoseNetworkResponse.NetworkStatus.MacsecStatus

        def __init__(self, subnet_status: _Optional[_Iterable[_Union[_resources_pb2.SubnetStatus, _Mapping]]]=..., macsec_status_internal_links: _Optional[_Union[DiagnoseNetworkResponse.NetworkStatus.MacsecStatus, str]]=...) -> None:
            ...
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    result: DiagnoseNetworkResponse.NetworkStatus

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., result: _Optional[_Union[DiagnoseNetworkResponse.NetworkStatus, _Mapping]]=...) -> None:
        ...

class DiagnoseInterconnectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DiagnoseInterconnectResponse(_message.Message):
    __slots__ = ('update_time', 'result')
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    result: _resources_pb2.InterconnectDiagnostics

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., result: _Optional[_Union[_resources_pb2.InterconnectDiagnostics, _Mapping]]=...) -> None:
        ...

class DiagnoseRouterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DiagnoseRouterResponse(_message.Message):
    __slots__ = ('update_time', 'result')
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    result: _resources_pb2.RouterStatus

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., result: _Optional[_Union[_resources_pb2.RouterStatus, _Mapping]]=...) -> None:
        ...

class InitializeZoneRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class InitializeZoneResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...