from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkemulticloud.v1 import attached_resources_pb2 as _attached_resources_pb2
from google.cloud.gkemulticloud.v1 import common_resources_pb2 as _common_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateAttachedClusterInstallManifestRequest(_message.Message):
    __slots__ = ("parent", "attached_cluster_id", "platform_version", "proxy_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    attached_cluster_id: str
    platform_version: str
    proxy_config: _attached_resources_pb2.AttachedProxyConfig
    def __init__(self, parent: _Optional[str] = ..., attached_cluster_id: _Optional[str] = ..., platform_version: _Optional[str] = ..., proxy_config: _Optional[_Union[_attached_resources_pb2.AttachedProxyConfig, _Mapping]] = ...) -> None: ...

class GenerateAttachedClusterInstallManifestResponse(_message.Message):
    __slots__ = ("manifest",)
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    manifest: str
    def __init__(self, manifest: _Optional[str] = ...) -> None: ...

class CreateAttachedClusterRequest(_message.Message):
    __slots__ = ("parent", "attached_cluster", "attached_cluster_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    attached_cluster: _attached_resources_pb2.AttachedCluster
    attached_cluster_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., attached_cluster: _Optional[_Union[_attached_resources_pb2.AttachedCluster, _Mapping]] = ..., attached_cluster_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ImportAttachedClusterRequest(_message.Message):
    __slots__ = ("parent", "validate_only", "fleet_membership", "platform_version", "distribution", "proxy_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FLEET_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    validate_only: bool
    fleet_membership: str
    platform_version: str
    distribution: str
    proxy_config: _attached_resources_pb2.AttachedProxyConfig
    def __init__(self, parent: _Optional[str] = ..., validate_only: bool = ..., fleet_membership: _Optional[str] = ..., platform_version: _Optional[str] = ..., distribution: _Optional[str] = ..., proxy_config: _Optional[_Union[_attached_resources_pb2.AttachedProxyConfig, _Mapping]] = ...) -> None: ...

class UpdateAttachedClusterRequest(_message.Message):
    __slots__ = ("attached_cluster", "validate_only", "update_mask")
    ATTACHED_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    attached_cluster: _attached_resources_pb2.AttachedCluster
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, attached_cluster: _Optional[_Union[_attached_resources_pb2.AttachedCluster, _Mapping]] = ..., validate_only: bool = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAttachedClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAttachedClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAttachedClustersResponse(_message.Message):
    __slots__ = ("attached_clusters", "next_page_token")
    ATTACHED_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attached_clusters: _containers.RepeatedCompositeFieldContainer[_attached_resources_pb2.AttachedCluster]
    next_page_token: str
    def __init__(self, attached_clusters: _Optional[_Iterable[_Union[_attached_resources_pb2.AttachedCluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAttachedClusterRequest(_message.Message):
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

class GetAttachedServerConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GenerateAttachedClusterAgentTokenRequest(_message.Message):
    __slots__ = ("attached_cluster", "subject_token", "subject_token_type", "version", "grant_type", "audience", "scope", "requested_token_type", "options")
    ATTACHED_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    attached_cluster: str
    subject_token: str
    subject_token_type: str
    version: str
    grant_type: str
    audience: str
    scope: str
    requested_token_type: str
    options: str
    def __init__(self, attached_cluster: _Optional[str] = ..., subject_token: _Optional[str] = ..., subject_token_type: _Optional[str] = ..., version: _Optional[str] = ..., grant_type: _Optional[str] = ..., audience: _Optional[str] = ..., scope: _Optional[str] = ..., requested_token_type: _Optional[str] = ..., options: _Optional[str] = ...) -> None: ...

class GenerateAttachedClusterAgentTokenResponse(_message.Message):
    __slots__ = ("access_token", "expires_in", "token_type")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: int
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., expires_in: _Optional[int] = ..., token_type: _Optional[str] = ...) -> None: ...
