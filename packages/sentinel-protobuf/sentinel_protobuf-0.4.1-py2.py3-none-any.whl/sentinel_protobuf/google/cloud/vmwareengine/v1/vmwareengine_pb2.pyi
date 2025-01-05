from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.vmwareengine.v1 import vmwareengine_resources_pb2 as _vmwareengine_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPrivateCloudsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListPrivateCloudsResponse(_message.Message):
    __slots__ = ("private_clouds", "next_page_token", "unreachable")
    PRIVATE_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    private_clouds: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.PrivateCloud]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, private_clouds: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.PrivateCloud, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPrivateCloudRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreatePrivateCloudRequest(_message.Message):
    __slots__ = ("parent", "private_cloud_id", "private_cloud", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CLOUD_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    private_cloud_id: str
    private_cloud: _vmwareengine_resources_pb2.PrivateCloud
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., private_cloud_id: _Optional[str] = ..., private_cloud: _Optional[_Union[_vmwareengine_resources_pb2.PrivateCloud, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdatePrivateCloudRequest(_message.Message):
    __slots__ = ("private_cloud", "update_mask", "request_id")
    PRIVATE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    private_cloud: _vmwareengine_resources_pb2.PrivateCloud
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, private_cloud: _Optional[_Union[_vmwareengine_resources_pb2.PrivateCloud, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeletePrivateCloudRequest(_message.Message):
    __slots__ = ("name", "request_id", "force", "delay_hours")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    DELAY_HOURS_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    delay_hours: int
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ..., delay_hours: _Optional[int] = ...) -> None: ...

class UndeletePrivateCloudRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page_token", "unreachable")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clusters: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.Cluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster_id", "cluster", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: _vmwareengine_resources_pb2.Cluster
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[_vmwareengine_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("update_mask", "cluster", "request_id", "validate_only")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cluster: _vmwareengine_resources_pb2.Cluster
    request_id: str
    validate_only: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cluster: _Optional[_Union[_vmwareengine_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListNodesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListNodesResponse(_message.Message):
    __slots__ = ("nodes", "next_page_token")
    NODES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.Node]
    next_page_token: str
    def __init__(self, nodes: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.Node, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetNodeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListExternalAddressesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListExternalAddressesResponse(_message.Message):
    __slots__ = ("external_addresses", "next_page_token", "unreachable")
    EXTERNAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    external_addresses: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.ExternalAddress]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, external_addresses: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.ExternalAddress, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchNetworkPolicyExternalAddressesRequest(_message.Message):
    __slots__ = ("network_policy", "page_size", "page_token")
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    network_policy: str
    page_size: int
    page_token: str
    def __init__(self, network_policy: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class FetchNetworkPolicyExternalAddressesResponse(_message.Message):
    __slots__ = ("external_addresses", "next_page_token")
    EXTERNAL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    external_addresses: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.ExternalAddress]
    next_page_token: str
    def __init__(self, external_addresses: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.ExternalAddress, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetExternalAddressRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateExternalAddressRequest(_message.Message):
    __slots__ = ("parent", "external_address", "external_address_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    external_address: _vmwareengine_resources_pb2.ExternalAddress
    external_address_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., external_address: _Optional[_Union[_vmwareengine_resources_pb2.ExternalAddress, _Mapping]] = ..., external_address_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateExternalAddressRequest(_message.Message):
    __slots__ = ("update_mask", "external_address", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    external_address: _vmwareengine_resources_pb2.ExternalAddress
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., external_address: _Optional[_Union[_vmwareengine_resources_pb2.ExternalAddress, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteExternalAddressRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListSubnetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSubnetsResponse(_message.Message):
    __slots__ = ("subnets", "next_page_token", "unreachable")
    SUBNETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    subnets: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.Subnet]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subnets: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.Subnet, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSubnetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateSubnetRequest(_message.Message):
    __slots__ = ("update_mask", "subnet")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    subnet: _vmwareengine_resources_pb2.Subnet
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., subnet: _Optional[_Union[_vmwareengine_resources_pb2.Subnet, _Mapping]] = ...) -> None: ...

class ListExternalAccessRulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListExternalAccessRulesResponse(_message.Message):
    __slots__ = ("external_access_rules", "next_page_token", "unreachable")
    EXTERNAL_ACCESS_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    external_access_rules: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.ExternalAccessRule]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, external_access_rules: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.ExternalAccessRule, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetExternalAccessRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateExternalAccessRuleRequest(_message.Message):
    __slots__ = ("parent", "external_access_rule", "external_access_rule_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCESS_RULE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCESS_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    external_access_rule: _vmwareengine_resources_pb2.ExternalAccessRule
    external_access_rule_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., external_access_rule: _Optional[_Union[_vmwareengine_resources_pb2.ExternalAccessRule, _Mapping]] = ..., external_access_rule_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateExternalAccessRuleRequest(_message.Message):
    __slots__ = ("update_mask", "external_access_rule", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCESS_RULE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    external_access_rule: _vmwareengine_resources_pb2.ExternalAccessRule
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., external_access_rule: _Optional[_Union[_vmwareengine_resources_pb2.ExternalAccessRule, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteExternalAccessRuleRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListLoggingServersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListLoggingServersResponse(_message.Message):
    __slots__ = ("logging_servers", "next_page_token", "unreachable")
    LOGGING_SERVERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    logging_servers: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.LoggingServer]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, logging_servers: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.LoggingServer, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetLoggingServerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateLoggingServerRequest(_message.Message):
    __slots__ = ("parent", "logging_server", "logging_server_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SERVER_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    logging_server: _vmwareengine_resources_pb2.LoggingServer
    logging_server_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., logging_server: _Optional[_Union[_vmwareengine_resources_pb2.LoggingServer, _Mapping]] = ..., logging_server_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateLoggingServerRequest(_message.Message):
    __slots__ = ("update_mask", "logging_server", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SERVER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    logging_server: _vmwareengine_resources_pb2.LoggingServer
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., logging_server: _Optional[_Union[_vmwareengine_resources_pb2.LoggingServer, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteLoggingServerRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
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
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...

class ListNodeTypesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListNodeTypesResponse(_message.Message):
    __slots__ = ("node_types", "next_page_token", "unreachable")
    NODE_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    node_types: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.NodeType]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, node_types: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.NodeType, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNodeTypeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ShowNsxCredentialsRequest(_message.Message):
    __slots__ = ("private_cloud",)
    PRIVATE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    private_cloud: str
    def __init__(self, private_cloud: _Optional[str] = ...) -> None: ...

class ShowVcenterCredentialsRequest(_message.Message):
    __slots__ = ("private_cloud", "username")
    PRIVATE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    private_cloud: str
    username: str
    def __init__(self, private_cloud: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class ResetNsxCredentialsRequest(_message.Message):
    __slots__ = ("private_cloud", "request_id")
    PRIVATE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    private_cloud: str
    request_id: str
    def __init__(self, private_cloud: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ResetVcenterCredentialsRequest(_message.Message):
    __slots__ = ("private_cloud", "request_id", "username")
    PRIVATE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    private_cloud: str
    request_id: str
    username: str
    def __init__(self, private_cloud: _Optional[str] = ..., request_id: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class ListHcxActivationKeysResponse(_message.Message):
    __slots__ = ("hcx_activation_keys", "next_page_token", "unreachable")
    HCX_ACTIVATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    hcx_activation_keys: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.HcxActivationKey]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hcx_activation_keys: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.HcxActivationKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class ListHcxActivationKeysRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetHcxActivationKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateHcxActivationKeyRequest(_message.Message):
    __slots__ = ("parent", "hcx_activation_key", "hcx_activation_key_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HCX_ACTIVATION_KEY_FIELD_NUMBER: _ClassVar[int]
    HCX_ACTIVATION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hcx_activation_key: _vmwareengine_resources_pb2.HcxActivationKey
    hcx_activation_key_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., hcx_activation_key: _Optional[_Union[_vmwareengine_resources_pb2.HcxActivationKey, _Mapping]] = ..., hcx_activation_key_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetDnsForwardingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateDnsForwardingRequest(_message.Message):
    __slots__ = ("dns_forwarding", "update_mask", "request_id")
    DNS_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    dns_forwarding: _vmwareengine_resources_pb2.DnsForwarding
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, dns_forwarding: _Optional[_Union[_vmwareengine_resources_pb2.DnsForwarding, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateNetworkPeeringRequest(_message.Message):
    __slots__ = ("parent", "network_peering_id", "network_peering", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PEERING_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PEERING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    network_peering_id: str
    network_peering: _vmwareengine_resources_pb2.NetworkPeering
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., network_peering_id: _Optional[str] = ..., network_peering: _Optional[_Union[_vmwareengine_resources_pb2.NetworkPeering, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteNetworkPeeringRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetNetworkPeeringRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListNetworkPeeringsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class UpdateNetworkPeeringRequest(_message.Message):
    __slots__ = ("network_peering", "update_mask", "request_id")
    NETWORK_PEERING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    network_peering: _vmwareengine_resources_pb2.NetworkPeering
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, network_peering: _Optional[_Union[_vmwareengine_resources_pb2.NetworkPeering, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListNetworkPeeringsResponse(_message.Message):
    __slots__ = ("network_peerings", "next_page_token", "unreachable")
    NETWORK_PEERINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    network_peerings: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.NetworkPeering]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, network_peerings: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.NetworkPeering, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class ListPeeringRoutesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListPeeringRoutesResponse(_message.Message):
    __slots__ = ("peering_routes", "next_page_token")
    PEERING_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    peering_routes: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.PeeringRoute]
    next_page_token: str
    def __init__(self, peering_routes: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.PeeringRoute, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListNetworkPoliciesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListNetworkPoliciesResponse(_message.Message):
    __slots__ = ("network_policies", "next_page_token", "unreachable")
    NETWORK_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    network_policies: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.NetworkPolicy]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, network_policies: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.NetworkPolicy, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNetworkPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateNetworkPolicyRequest(_message.Message):
    __slots__ = ("network_policy", "update_mask", "request_id")
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    network_policy: _vmwareengine_resources_pb2.NetworkPolicy
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, network_policy: _Optional[_Union[_vmwareengine_resources_pb2.NetworkPolicy, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateNetworkPolicyRequest(_message.Message):
    __slots__ = ("parent", "network_policy_id", "network_policy", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    network_policy_id: str
    network_policy: _vmwareengine_resources_pb2.NetworkPolicy
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., network_policy_id: _Optional[str] = ..., network_policy: _Optional[_Union[_vmwareengine_resources_pb2.NetworkPolicy, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteNetworkPolicyRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListManagementDnsZoneBindingsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListManagementDnsZoneBindingsResponse(_message.Message):
    __slots__ = ("management_dns_zone_bindings", "next_page_token", "unreachable")
    MANAGEMENT_DNS_ZONE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    management_dns_zone_bindings: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.ManagementDnsZoneBinding]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, management_dns_zone_bindings: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.ManagementDnsZoneBinding, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetManagementDnsZoneBindingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateManagementDnsZoneBindingRequest(_message.Message):
    __slots__ = ("parent", "management_dns_zone_binding", "management_dns_zone_binding_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_DNS_ZONE_BINDING_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_DNS_ZONE_BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    management_dns_zone_binding: _vmwareengine_resources_pb2.ManagementDnsZoneBinding
    management_dns_zone_binding_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., management_dns_zone_binding: _Optional[_Union[_vmwareengine_resources_pb2.ManagementDnsZoneBinding, _Mapping]] = ..., management_dns_zone_binding_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateManagementDnsZoneBindingRequest(_message.Message):
    __slots__ = ("update_mask", "management_dns_zone_binding", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_DNS_ZONE_BINDING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    management_dns_zone_binding: _vmwareengine_resources_pb2.ManagementDnsZoneBinding
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., management_dns_zone_binding: _Optional[_Union[_vmwareengine_resources_pb2.ManagementDnsZoneBinding, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteManagementDnsZoneBindingRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class RepairManagementDnsZoneBindingRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateVmwareEngineNetworkRequest(_message.Message):
    __slots__ = ("parent", "vmware_engine_network_id", "vmware_engine_network", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    vmware_engine_network_id: str
    vmware_engine_network: _vmwareengine_resources_pb2.VmwareEngineNetwork
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., vmware_engine_network_id: _Optional[str] = ..., vmware_engine_network: _Optional[_Union[_vmwareengine_resources_pb2.VmwareEngineNetwork, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateVmwareEngineNetworkRequest(_message.Message):
    __slots__ = ("vmware_engine_network", "update_mask", "request_id")
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    vmware_engine_network: _vmwareengine_resources_pb2.VmwareEngineNetwork
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, vmware_engine_network: _Optional[_Union[_vmwareengine_resources_pb2.VmwareEngineNetwork, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteVmwareEngineNetworkRequest(_message.Message):
    __slots__ = ("name", "request_id", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., etag: _Optional[str] = ...) -> None: ...

class GetVmwareEngineNetworkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListVmwareEngineNetworksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListVmwareEngineNetworksResponse(_message.Message):
    __slots__ = ("vmware_engine_networks", "next_page_token", "unreachable")
    VMWARE_ENGINE_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    vmware_engine_networks: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.VmwareEngineNetwork]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vmware_engine_networks: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.VmwareEngineNetwork, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePrivateConnectionRequest(_message.Message):
    __slots__ = ("parent", "private_connection_id", "private_connection", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    private_connection_id: str
    private_connection: _vmwareengine_resources_pb2.PrivateConnection
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., private_connection_id: _Optional[str] = ..., private_connection: _Optional[_Union[_vmwareengine_resources_pb2.PrivateConnection, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetPrivateConnectionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPrivateConnectionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListPrivateConnectionsResponse(_message.Message):
    __slots__ = ("private_connections", "next_page_token", "unreachable")
    PRIVATE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    private_connections: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.PrivateConnection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, private_connections: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.PrivateConnection, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdatePrivateConnectionRequest(_message.Message):
    __slots__ = ("private_connection", "update_mask", "request_id")
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    private_connection: _vmwareengine_resources_pb2.PrivateConnection
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, private_connection: _Optional[_Union[_vmwareengine_resources_pb2.PrivateConnection, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeletePrivateConnectionRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListPrivateConnectionPeeringRoutesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPrivateConnectionPeeringRoutesResponse(_message.Message):
    __slots__ = ("peering_routes", "next_page_token")
    PEERING_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    peering_routes: _containers.RepeatedCompositeFieldContainer[_vmwareengine_resources_pb2.PeeringRoute]
    next_page_token: str
    def __init__(self, peering_routes: _Optional[_Iterable[_Union[_vmwareengine_resources_pb2.PeeringRoute, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GrantDnsBindPermissionRequest(_message.Message):
    __slots__ = ("name", "principal", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    principal: _vmwareengine_resources_pb2.Principal
    request_id: str
    def __init__(self, name: _Optional[str] = ..., principal: _Optional[_Union[_vmwareengine_resources_pb2.Principal, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class RevokeDnsBindPermissionRequest(_message.Message):
    __slots__ = ("name", "principal", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    principal: _vmwareengine_resources_pb2.Principal
    request_id: str
    def __init__(self, name: _Optional[str] = ..., principal: _Optional[_Union[_vmwareengine_resources_pb2.Principal, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetDnsBindPermissionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
