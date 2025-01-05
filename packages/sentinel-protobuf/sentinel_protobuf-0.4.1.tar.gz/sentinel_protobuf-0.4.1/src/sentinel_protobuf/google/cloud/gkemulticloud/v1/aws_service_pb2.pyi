from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkemulticloud.v1 import aws_resources_pb2 as _aws_resources_pb2
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

class CreateAwsClusterRequest(_message.Message):
    __slots__ = ("parent", "aws_cluster", "aws_cluster_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    AWS_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    aws_cluster: _aws_resources_pb2.AwsCluster
    aws_cluster_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., aws_cluster: _Optional[_Union[_aws_resources_pb2.AwsCluster, _Mapping]] = ..., aws_cluster_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateAwsClusterRequest(_message.Message):
    __slots__ = ("aws_cluster", "validate_only", "update_mask")
    AWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    aws_cluster: _aws_resources_pb2.AwsCluster
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, aws_cluster: _Optional[_Union[_aws_resources_pb2.AwsCluster, _Mapping]] = ..., validate_only: bool = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAwsClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAwsClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAwsClustersResponse(_message.Message):
    __slots__ = ("aws_clusters", "next_page_token")
    AWS_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    aws_clusters: _containers.RepeatedCompositeFieldContainer[_aws_resources_pb2.AwsCluster]
    next_page_token: str
    def __init__(self, aws_clusters: _Optional[_Iterable[_Union[_aws_resources_pb2.AwsCluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAwsClusterRequest(_message.Message):
    __slots__ = ("name", "validate_only", "allow_missing", "ignore_errors", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    ignore_errors: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ..., ignore_errors: bool = ..., etag: _Optional[str] = ...) -> None: ...

class CreateAwsNodePoolRequest(_message.Message):
    __slots__ = ("parent", "aws_node_pool", "aws_node_pool_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AWS_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    AWS_NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    aws_node_pool: _aws_resources_pb2.AwsNodePool
    aws_node_pool_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., aws_node_pool: _Optional[_Union[_aws_resources_pb2.AwsNodePool, _Mapping]] = ..., aws_node_pool_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateAwsNodePoolRequest(_message.Message):
    __slots__ = ("aws_node_pool", "validate_only", "update_mask")
    AWS_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    aws_node_pool: _aws_resources_pb2.AwsNodePool
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, aws_node_pool: _Optional[_Union[_aws_resources_pb2.AwsNodePool, _Mapping]] = ..., validate_only: bool = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class RollbackAwsNodePoolUpdateRequest(_message.Message):
    __slots__ = ("name", "respect_pdb")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPECT_PDB_FIELD_NUMBER: _ClassVar[int]
    name: str
    respect_pdb: bool
    def __init__(self, name: _Optional[str] = ..., respect_pdb: bool = ...) -> None: ...

class GetAwsNodePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAwsNodePoolsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAwsNodePoolsResponse(_message.Message):
    __slots__ = ("aws_node_pools", "next_page_token")
    AWS_NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    aws_node_pools: _containers.RepeatedCompositeFieldContainer[_aws_resources_pb2.AwsNodePool]
    next_page_token: str
    def __init__(self, aws_node_pools: _Optional[_Iterable[_Union[_aws_resources_pb2.AwsNodePool, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAwsNodePoolRequest(_message.Message):
    __slots__ = ("name", "validate_only", "allow_missing", "ignore_errors", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    ignore_errors: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ..., ignore_errors: bool = ..., etag: _Optional[str] = ...) -> None: ...

class GetAwsOpenIdConfigRequest(_message.Message):
    __slots__ = ("aws_cluster",)
    AWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    aws_cluster: str
    def __init__(self, aws_cluster: _Optional[str] = ...) -> None: ...

class GetAwsJsonWebKeysRequest(_message.Message):
    __slots__ = ("aws_cluster",)
    AWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    aws_cluster: str
    def __init__(self, aws_cluster: _Optional[str] = ...) -> None: ...

class GetAwsServerConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GenerateAwsAccessTokenRequest(_message.Message):
    __slots__ = ("aws_cluster",)
    AWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    aws_cluster: str
    def __init__(self, aws_cluster: _Optional[str] = ...) -> None: ...

class GenerateAwsAccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "expiration_time")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenerateAwsClusterAgentTokenRequest(_message.Message):
    __slots__ = ("aws_cluster", "subject_token", "subject_token_type", "version", "node_pool_id", "grant_type", "audience", "scope", "requested_token_type", "options")
    AWS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    aws_cluster: str
    subject_token: str
    subject_token_type: str
    version: str
    node_pool_id: str
    grant_type: str
    audience: str
    scope: str
    requested_token_type: str
    options: str
    def __init__(self, aws_cluster: _Optional[str] = ..., subject_token: _Optional[str] = ..., subject_token_type: _Optional[str] = ..., version: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., grant_type: _Optional[str] = ..., audience: _Optional[str] = ..., scope: _Optional[str] = ..., requested_token_type: _Optional[str] = ..., options: _Optional[str] = ...) -> None: ...

class GenerateAwsClusterAgentTokenResponse(_message.Message):
    __slots__ = ("access_token", "expires_in", "token_type")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: int
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., expires_in: _Optional[int] = ..., token_type: _Optional[str] = ...) -> None: ...
