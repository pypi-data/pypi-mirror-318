from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkemulticloud.v1 import azure_resources_pb2 as _azure_resources_pb2
from google.cloud.gkemulticloud.v1 import common_resources_pb2 as _common_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAzureClusterRequest(_message.Message):
    __slots__ = ("parent", "azure_cluster", "azure_cluster_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AZURE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    AZURE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    azure_cluster: _azure_resources_pb2.AzureCluster
    azure_cluster_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., azure_cluster: _Optional[_Union[_azure_resources_pb2.AzureCluster, _Mapping]] = ..., azure_cluster_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateAzureClusterRequest(_message.Message):
    __slots__ = ("azure_cluster", "validate_only", "update_mask")
    AZURE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    azure_cluster: _azure_resources_pb2.AzureCluster
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, azure_cluster: _Optional[_Union[_azure_resources_pb2.AzureCluster, _Mapping]] = ..., validate_only: bool = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAzureClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAzureClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAzureClustersResponse(_message.Message):
    __slots__ = ("azure_clusters", "next_page_token")
    AZURE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    azure_clusters: _containers.RepeatedCompositeFieldContainer[_azure_resources_pb2.AzureCluster]
    next_page_token: str
    def __init__(self, azure_clusters: _Optional[_Iterable[_Union[_azure_resources_pb2.AzureCluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAzureClusterRequest(_message.Message):
    __slots__ = ("name", "allow_missing", "validate_only", "etag", "ignore_errors")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool
    validate_only: bool
    etag: str
    ignore_errors: bool
    def __init__(self, name: _Optional[str] = ..., allow_missing: bool = ..., validate_only: bool = ..., etag: _Optional[str] = ..., ignore_errors: bool = ...) -> None: ...

class CreateAzureNodePoolRequest(_message.Message):
    __slots__ = ("parent", "azure_node_pool", "azure_node_pool_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AZURE_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    AZURE_NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    azure_node_pool: _azure_resources_pb2.AzureNodePool
    azure_node_pool_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., azure_node_pool: _Optional[_Union[_azure_resources_pb2.AzureNodePool, _Mapping]] = ..., azure_node_pool_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateAzureNodePoolRequest(_message.Message):
    __slots__ = ("azure_node_pool", "validate_only", "update_mask")
    AZURE_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    azure_node_pool: _azure_resources_pb2.AzureNodePool
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, azure_node_pool: _Optional[_Union[_azure_resources_pb2.AzureNodePool, _Mapping]] = ..., validate_only: bool = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAzureNodePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAzureNodePoolsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAzureNodePoolsResponse(_message.Message):
    __slots__ = ("azure_node_pools", "next_page_token")
    AZURE_NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    azure_node_pools: _containers.RepeatedCompositeFieldContainer[_azure_resources_pb2.AzureNodePool]
    next_page_token: str
    def __init__(self, azure_node_pools: _Optional[_Iterable[_Union[_azure_resources_pb2.AzureNodePool, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAzureNodePoolRequest(_message.Message):
    __slots__ = ("name", "validate_only", "allow_missing", "etag", "ignore_errors")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    etag: str
    ignore_errors: bool
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ..., etag: _Optional[str] = ..., ignore_errors: bool = ...) -> None: ...

class GetAzureOpenIdConfigRequest(_message.Message):
    __slots__ = ("azure_cluster",)
    AZURE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    azure_cluster: str
    def __init__(self, azure_cluster: _Optional[str] = ...) -> None: ...

class GetAzureJsonWebKeysRequest(_message.Message):
    __slots__ = ("azure_cluster",)
    AZURE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    azure_cluster: str
    def __init__(self, azure_cluster: _Optional[str] = ...) -> None: ...

class GetAzureServerConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAzureClientRequest(_message.Message):
    __slots__ = ("parent", "azure_client", "azure_client_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AZURE_CLIENT_FIELD_NUMBER: _ClassVar[int]
    AZURE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    azure_client: _azure_resources_pb2.AzureClient
    azure_client_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., azure_client: _Optional[_Union[_azure_resources_pb2.AzureClient, _Mapping]] = ..., azure_client_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class GetAzureClientRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAzureClientsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAzureClientsResponse(_message.Message):
    __slots__ = ("azure_clients", "next_page_token")
    AZURE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    azure_clients: _containers.RepeatedCompositeFieldContainer[_azure_resources_pb2.AzureClient]
    next_page_token: str
    def __init__(self, azure_clients: _Optional[_Iterable[_Union[_azure_resources_pb2.AzureClient, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAzureClientRequest(_message.Message):
    __slots__ = ("name", "allow_missing", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., allow_missing: bool = ..., validate_only: bool = ...) -> None: ...

class GenerateAzureAccessTokenRequest(_message.Message):
    __slots__ = ("azure_cluster",)
    AZURE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    azure_cluster: str
    def __init__(self, azure_cluster: _Optional[str] = ...) -> None: ...

class GenerateAzureAccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "expiration_time")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenerateAzureClusterAgentTokenRequest(_message.Message):
    __slots__ = ("azure_cluster", "subject_token", "subject_token_type", "version", "node_pool_id", "grant_type", "audience", "scope", "requested_token_type", "options")
    AZURE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    azure_cluster: str
    subject_token: str
    subject_token_type: str
    version: str
    node_pool_id: str
    grant_type: str
    audience: str
    scope: str
    requested_token_type: str
    options: str
    def __init__(self, azure_cluster: _Optional[str] = ..., subject_token: _Optional[str] = ..., subject_token_type: _Optional[str] = ..., version: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., grant_type: _Optional[str] = ..., audience: _Optional[str] = ..., scope: _Optional[str] = ..., requested_token_type: _Optional[str] = ..., options: _Optional[str] = ...) -> None: ...

class GenerateAzureClusterAgentTokenResponse(_message.Message):
    __slots__ = ("access_token", "expires_in", "token_type")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: int
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., expires_in: _Optional[int] = ..., token_type: _Optional[str] = ...) -> None: ...
