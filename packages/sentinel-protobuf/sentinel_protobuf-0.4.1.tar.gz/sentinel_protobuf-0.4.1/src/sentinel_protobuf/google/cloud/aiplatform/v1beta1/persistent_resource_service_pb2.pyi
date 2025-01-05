from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import persistent_resource_pb2 as _persistent_resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePersistentResourceRequest(_message.Message):
    __slots__ = ("parent", "persistent_resource", "persistent_resource_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    persistent_resource: _persistent_resource_pb2.PersistentResource
    persistent_resource_id: str
    def __init__(self, parent: _Optional[str] = ..., persistent_resource: _Optional[_Union[_persistent_resource_pb2.PersistentResource, _Mapping]] = ..., persistent_resource_id: _Optional[str] = ...) -> None: ...

class CreatePersistentResourceOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata", "progress_message")
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., progress_message: _Optional[str] = ...) -> None: ...

class UpdatePersistentResourceOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata", "progress_message")
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., progress_message: _Optional[str] = ...) -> None: ...

class RebootPersistentResourceOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata", "progress_message")
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., progress_message: _Optional[str] = ...) -> None: ...

class GetPersistentResourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPersistentResourcesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPersistentResourcesResponse(_message.Message):
    __slots__ = ("persistent_resources", "next_page_token")
    PERSISTENT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    persistent_resources: _containers.RepeatedCompositeFieldContainer[_persistent_resource_pb2.PersistentResource]
    next_page_token: str
    def __init__(self, persistent_resources: _Optional[_Iterable[_Union[_persistent_resource_pb2.PersistentResource, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeletePersistentResourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdatePersistentResourceRequest(_message.Message):
    __slots__ = ("persistent_resource", "update_mask")
    PERSISTENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    persistent_resource: _persistent_resource_pb2.PersistentResource
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, persistent_resource: _Optional[_Union[_persistent_resource_pb2.PersistentResource, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class RebootPersistentResourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
