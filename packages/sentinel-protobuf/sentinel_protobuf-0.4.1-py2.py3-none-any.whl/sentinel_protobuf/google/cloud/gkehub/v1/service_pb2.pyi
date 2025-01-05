from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkehub.v1 import feature_pb2 as _feature_pb2
from google.cloud.gkehub.v1 import membership_pb2 as _membership_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMembershipsRequest(_message.Message):
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

class ListMembershipsResponse(_message.Message):
    __slots__ = ("resources", "next_page_token", "unreachable")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[_membership_pb2.Membership]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resources: _Optional[_Iterable[_Union[_membership_pb2.Membership, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetMembershipRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateMembershipRequest(_message.Message):
    __slots__ = ("parent", "membership_id", "resource", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    membership_id: str
    resource: _membership_pb2.Membership
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., membership_id: _Optional[str] = ..., resource: _Optional[_Union[_membership_pb2.Membership, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteMembershipRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class UpdateMembershipRequest(_message.Message):
    __slots__ = ("name", "update_mask", "resource", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_mask: _field_mask_pb2.FieldMask
    resource: _membership_pb2.Membership
    request_id: str
    def __init__(self, name: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., resource: _Optional[_Union[_membership_pb2.Membership, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GenerateConnectManifestRequest(_message.Message):
    __slots__ = ("name", "namespace", "proxy", "version", "is_upgrade", "registry", "image_pull_secret_content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PULL_SECRET_CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    proxy: bytes
    version: str
    is_upgrade: bool
    registry: str
    image_pull_secret_content: bytes
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., proxy: _Optional[bytes] = ..., version: _Optional[str] = ..., is_upgrade: bool = ..., registry: _Optional[str] = ..., image_pull_secret_content: _Optional[bytes] = ...) -> None: ...

class GenerateConnectManifestResponse(_message.Message):
    __slots__ = ("manifest",)
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    manifest: _containers.RepeatedCompositeFieldContainer[ConnectAgentResource]
    def __init__(self, manifest: _Optional[_Iterable[_Union[ConnectAgentResource, _Mapping]]] = ...) -> None: ...

class ConnectAgentResource(_message.Message):
    __slots__ = ("type", "manifest")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    type: TypeMeta
    manifest: str
    def __init__(self, type: _Optional[_Union[TypeMeta, _Mapping]] = ..., manifest: _Optional[str] = ...) -> None: ...

class TypeMeta(_message.Message):
    __slots__ = ("kind", "api_version")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ...) -> None: ...

class ListFeaturesRequest(_message.Message):
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

class ListFeaturesResponse(_message.Message):
    __slots__ = ("resources", "next_page_token")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    next_page_token: str
    def __init__(self, resources: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetFeatureRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFeatureRequest(_message.Message):
    __slots__ = ("parent", "feature_id", "resource", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature_id: str
    resource: _feature_pb2.Feature
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., feature_id: _Optional[str] = ..., resource: _Optional[_Union[_feature_pb2.Feature, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteFeatureRequest(_message.Message):
    __slots__ = ("name", "force", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    request_id: str
    def __init__(self, name: _Optional[str] = ..., force: bool = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateFeatureRequest(_message.Message):
    __slots__ = ("name", "update_mask", "resource", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_mask: _field_mask_pb2.FieldMask
    resource: _feature_pb2.Feature
    request_id: str
    def __init__(self, name: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., resource: _Optional[_Union[_feature_pb2.Feature, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_detail", "cancel_requested", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_detail: _Optional[str] = ..., cancel_requested: bool = ..., api_version: _Optional[str] = ...) -> None: ...
