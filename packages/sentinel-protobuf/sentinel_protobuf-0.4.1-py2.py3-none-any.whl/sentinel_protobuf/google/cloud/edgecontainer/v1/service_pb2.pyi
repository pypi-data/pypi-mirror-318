from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.edgecontainer.v1 import resources_pb2 as _resources_pb2
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

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version', 'warnings', 'status_reason')

    class StatusReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_REASON_UNSPECIFIED: _ClassVar[OperationMetadata.StatusReason]
        UPGRADE_PAUSED: _ClassVar[OperationMetadata.StatusReason]
    STATUS_REASON_UNSPECIFIED: OperationMetadata.StatusReason
    UPGRADE_PAUSED: OperationMetadata.StatusReason
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    status_reason: OperationMetadata.StatusReason

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=..., warnings: _Optional[_Iterable[str]]=..., status_reason: _Optional[_Union[OperationMetadata.StatusReason, str]]=...) -> None:
        ...

class ListClustersRequest(_message.Message):
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

class ListClustersResponse(_message.Message):
    __slots__ = ('clusters', 'next_page_token', 'unreachable')
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, clusters: _Optional[_Iterable[_Union[_resources_pb2.Cluster, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetClusterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateClusterRequest(_message.Message):
    __slots__ = ('parent', 'cluster_id', 'cluster', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: _resources_pb2.Cluster
    request_id: str

    def __init__(self, parent: _Optional[str]=..., cluster_id: _Optional[str]=..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ('update_mask', 'cluster', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cluster: _resources_pb2.Cluster
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpgradeClusterRequest(_message.Message):
    __slots__ = ('name', 'target_version', 'schedule', 'request_id')

    class Schedule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEDULE_UNSPECIFIED: _ClassVar[UpgradeClusterRequest.Schedule]
        IMMEDIATELY: _ClassVar[UpgradeClusterRequest.Schedule]
    SCHEDULE_UNSPECIFIED: UpgradeClusterRequest.Schedule
    IMMEDIATELY: UpgradeClusterRequest.Schedule
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_version: str
    schedule: UpgradeClusterRequest.Schedule
    request_id: str

    def __init__(self, name: _Optional[str]=..., target_version: _Optional[str]=..., schedule: _Optional[_Union[UpgradeClusterRequest.Schedule, str]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GenerateAccessTokenRequest(_message.Message):
    __slots__ = ('cluster',)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: str

    def __init__(self, cluster: _Optional[str]=...) -> None:
        ...

class GenerateAccessTokenResponse(_message.Message):
    __slots__ = ('access_token', 'expire_time')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, access_token: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GenerateOfflineCredentialRequest(_message.Message):
    __slots__ = ('cluster',)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: str

    def __init__(self, cluster: _Optional[str]=...) -> None:
        ...

class GenerateOfflineCredentialResponse(_message.Message):
    __slots__ = ('client_certificate', 'client_key', 'user_id', 'expire_time')
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    client_certificate: str
    client_key: str
    user_id: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, client_certificate: _Optional[str]=..., client_key: _Optional[str]=..., user_id: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListNodePoolsRequest(_message.Message):
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

class ListNodePoolsResponse(_message.Message):
    __slots__ = ('node_pools', 'next_page_token', 'unreachable')
    NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    node_pools: _containers.RepeatedCompositeFieldContainer[_resources_pb2.NodePool]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, node_pools: _Optional[_Iterable[_Union[_resources_pb2.NodePool, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetNodePoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateNodePoolRequest(_message.Message):
    __slots__ = ('parent', 'node_pool_id', 'node_pool', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    node_pool_id: str
    node_pool: _resources_pb2.NodePool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., node_pool_id: _Optional[str]=..., node_pool: _Optional[_Union[_resources_pb2.NodePool, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateNodePoolRequest(_message.Message):
    __slots__ = ('update_mask', 'node_pool', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    node_pool: _resources_pb2.NodePool
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., node_pool: _Optional[_Union[_resources_pb2.NodePool, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteNodePoolRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListMachinesRequest(_message.Message):
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

class ListMachinesResponse(_message.Message):
    __slots__ = ('machines', 'next_page_token', 'unreachable')
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    machines: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Machine]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, machines: _Optional[_Iterable[_Union[_resources_pb2.Machine, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMachineRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVpnConnectionsRequest(_message.Message):
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

class ListVpnConnectionsResponse(_message.Message):
    __slots__ = ('vpn_connections', 'next_page_token', 'unreachable')
    VPN_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    vpn_connections: _containers.RepeatedCompositeFieldContainer[_resources_pb2.VpnConnection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, vpn_connections: _Optional[_Iterable[_Union[_resources_pb2.VpnConnection, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetVpnConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateVpnConnectionRequest(_message.Message):
    __slots__ = ('parent', 'vpn_connection_id', 'vpn_connection', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VPN_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VPN_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    vpn_connection_id: str
    vpn_connection: _resources_pb2.VpnConnection
    request_id: str

    def __init__(self, parent: _Optional[str]=..., vpn_connection_id: _Optional[str]=..., vpn_connection: _Optional[_Union[_resources_pb2.VpnConnection, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteVpnConnectionRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetServerConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...