from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import index_endpoint_pb2 as _index_endpoint_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateIndexEndpointRequest(_message.Message):
    __slots__ = ('parent', 'index_endpoint')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    index_endpoint: _index_endpoint_pb2.IndexEndpoint

    def __init__(self, parent: _Optional[str]=..., index_endpoint: _Optional[_Union[_index_endpoint_pb2.IndexEndpoint, _Mapping]]=...) -> None:
        ...

class CreateIndexEndpointOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetIndexEndpointRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIndexEndpointsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListIndexEndpointsResponse(_message.Message):
    __slots__ = ('index_endpoints', 'next_page_token')
    INDEX_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    index_endpoints: _containers.RepeatedCompositeFieldContainer[_index_endpoint_pb2.IndexEndpoint]
    next_page_token: str

    def __init__(self, index_endpoints: _Optional[_Iterable[_Union[_index_endpoint_pb2.IndexEndpoint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateIndexEndpointRequest(_message.Message):
    __slots__ = ('index_endpoint', 'update_mask')
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: _index_endpoint_pb2.IndexEndpoint
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, index_endpoint: _Optional[_Union[_index_endpoint_pb2.IndexEndpoint, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteIndexEndpointRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeployIndexRequest(_message.Message):
    __slots__ = ('index_endpoint', 'deployed_index')
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index: _index_endpoint_pb2.DeployedIndex

    def __init__(self, index_endpoint: _Optional[str]=..., deployed_index: _Optional[_Union[_index_endpoint_pb2.DeployedIndex, _Mapping]]=...) -> None:
        ...

class DeployIndexResponse(_message.Message):
    __slots__ = ('deployed_index',)
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    deployed_index: _index_endpoint_pb2.DeployedIndex

    def __init__(self, deployed_index: _Optional[_Union[_index_endpoint_pb2.DeployedIndex, _Mapping]]=...) -> None:
        ...

class DeployIndexOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'deployed_index_id')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    deployed_index_id: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., deployed_index_id: _Optional[str]=...) -> None:
        ...

class UndeployIndexRequest(_message.Message):
    __slots__ = ('index_endpoint', 'deployed_index_id')
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index_id: str

    def __init__(self, index_endpoint: _Optional[str]=..., deployed_index_id: _Optional[str]=...) -> None:
        ...

class UndeployIndexResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UndeployIndexOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class MutateDeployedIndexRequest(_message.Message):
    __slots__ = ('index_endpoint', 'deployed_index')
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index: _index_endpoint_pb2.DeployedIndex

    def __init__(self, index_endpoint: _Optional[str]=..., deployed_index: _Optional[_Union[_index_endpoint_pb2.DeployedIndex, _Mapping]]=...) -> None:
        ...

class MutateDeployedIndexResponse(_message.Message):
    __slots__ = ('deployed_index',)
    DEPLOYED_INDEX_FIELD_NUMBER: _ClassVar[int]
    deployed_index: _index_endpoint_pb2.DeployedIndex

    def __init__(self, deployed_index: _Optional[_Union[_index_endpoint_pb2.DeployedIndex, _Mapping]]=...) -> None:
        ...

class MutateDeployedIndexOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'deployed_index_id')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    deployed_index_id: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., deployed_index_id: _Optional[str]=...) -> None:
        ...