from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import artifact_pb2 as _artifact_pb2
from google.cloud.aiplatform.v1beta1 import context_pb2 as _context_pb2
from google.cloud.aiplatform.v1beta1 import event_pb2 as _event_pb2
from google.cloud.aiplatform.v1beta1 import execution_pb2 as _execution_pb2
from google.cloud.aiplatform.v1beta1 import lineage_subgraph_pb2 as _lineage_subgraph_pb2
from google.cloud.aiplatform.v1beta1 import metadata_schema_pb2 as _metadata_schema_pb2
from google.cloud.aiplatform.v1beta1 import metadata_store_pb2 as _metadata_store_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateMetadataStoreRequest(_message.Message):
    __slots__ = ('parent', 'metadata_store', 'metadata_store_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_STORE_FIELD_NUMBER: _ClassVar[int]
    METADATA_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metadata_store: _metadata_store_pb2.MetadataStore
    metadata_store_id: str

    def __init__(self, parent: _Optional[str]=..., metadata_store: _Optional[_Union[_metadata_store_pb2.MetadataStore, _Mapping]]=..., metadata_store_id: _Optional[str]=...) -> None:
        ...

class CreateMetadataStoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetMetadataStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMetadataStoresRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMetadataStoresResponse(_message.Message):
    __slots__ = ('metadata_stores', 'next_page_token')
    METADATA_STORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metadata_stores: _containers.RepeatedCompositeFieldContainer[_metadata_store_pb2.MetadataStore]
    next_page_token: str

    def __init__(self, metadata_stores: _Optional[_Iterable[_Union[_metadata_store_pb2.MetadataStore, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteMetadataStoreRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class DeleteMetadataStoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateArtifactRequest(_message.Message):
    __slots__ = ('parent', 'artifact', 'artifact_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    artifact: _artifact_pb2.Artifact
    artifact_id: str

    def __init__(self, parent: _Optional[str]=..., artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]]=..., artifact_id: _Optional[str]=...) -> None:
        ...

class GetArtifactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListArtifactsRequest(_message.Message):
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

class ListArtifactsResponse(_message.Message):
    __slots__ = ('artifacts', 'next_page_token')
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[_artifact_pb2.Artifact]
    next_page_token: str

    def __init__(self, artifacts: _Optional[_Iterable[_Union[_artifact_pb2.Artifact, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateArtifactRequest(_message.Message):
    __slots__ = ('artifact', 'update_mask', 'allow_missing')
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    artifact: _artifact_pb2.Artifact
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, artifact: _Optional[_Union[_artifact_pb2.Artifact, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteArtifactRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class PurgeArtifactsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'force')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class PurgeArtifactsResponse(_message.Message):
    __slots__ = ('purge_count', 'purge_sample')
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PURGE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    purge_sample: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, purge_count: _Optional[int]=..., purge_sample: _Optional[_Iterable[str]]=...) -> None:
        ...

class PurgeArtifactsMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateContextRequest(_message.Message):
    __slots__ = ('parent', 'context', 'context_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    context: _context_pb2.Context
    context_id: str

    def __init__(self, parent: _Optional[str]=..., context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., context_id: _Optional[str]=...) -> None:
        ...

class GetContextRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListContextsRequest(_message.Message):
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

class ListContextsResponse(_message.Message):
    __slots__ = ('contexts', 'next_page_token')
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contexts: _containers.RepeatedCompositeFieldContainer[_context_pb2.Context]
    next_page_token: str

    def __init__(self, contexts: _Optional[_Iterable[_Union[_context_pb2.Context, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateContextRequest(_message.Message):
    __slots__ = ('context', 'update_mask', 'allow_missing')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    context: _context_pb2.Context
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteContextRequest(_message.Message):
    __slots__ = ('name', 'force', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., force: bool=..., etag: _Optional[str]=...) -> None:
        ...

class PurgeContextsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'force')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class PurgeContextsResponse(_message.Message):
    __slots__ = ('purge_count', 'purge_sample')
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PURGE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    purge_sample: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, purge_count: _Optional[int]=..., purge_sample: _Optional[_Iterable[str]]=...) -> None:
        ...

class PurgeContextsMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class AddContextArtifactsAndExecutionsRequest(_message.Message):
    __slots__ = ('context', 'artifacts', 'executions')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    context: str
    artifacts: _containers.RepeatedScalarFieldContainer[str]
    executions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, context: _Optional[str]=..., artifacts: _Optional[_Iterable[str]]=..., executions: _Optional[_Iterable[str]]=...) -> None:
        ...

class AddContextArtifactsAndExecutionsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AddContextChildrenRequest(_message.Message):
    __slots__ = ('context', 'child_contexts')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CHILD_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    context: str
    child_contexts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, context: _Optional[str]=..., child_contexts: _Optional[_Iterable[str]]=...) -> None:
        ...

class AddContextChildrenResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemoveContextChildrenRequest(_message.Message):
    __slots__ = ('context', 'child_contexts')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CHILD_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    context: str
    child_contexts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, context: _Optional[str]=..., child_contexts: _Optional[_Iterable[str]]=...) -> None:
        ...

class RemoveContextChildrenResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class QueryContextLineageSubgraphRequest(_message.Message):
    __slots__ = ('context',)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: str

    def __init__(self, context: _Optional[str]=...) -> None:
        ...

class CreateExecutionRequest(_message.Message):
    __slots__ = ('parent', 'execution', 'execution_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    execution: _execution_pb2.Execution
    execution_id: str

    def __init__(self, parent: _Optional[str]=..., execution: _Optional[_Union[_execution_pb2.Execution, _Mapping]]=..., execution_id: _Optional[str]=...) -> None:
        ...

class GetExecutionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListExecutionsRequest(_message.Message):
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

class ListExecutionsResponse(_message.Message):
    __slots__ = ('executions', 'next_page_token')
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_execution_pb2.Execution]
    next_page_token: str

    def __init__(self, executions: _Optional[_Iterable[_Union[_execution_pb2.Execution, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateExecutionRequest(_message.Message):
    __slots__ = ('execution', 'update_mask', 'allow_missing')
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    execution: _execution_pb2.Execution
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, execution: _Optional[_Union[_execution_pb2.Execution, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteExecutionRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class PurgeExecutionsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'force')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class PurgeExecutionsResponse(_message.Message):
    __slots__ = ('purge_count', 'purge_sample')
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PURGE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    purge_sample: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, purge_count: _Optional[int]=..., purge_sample: _Optional[_Iterable[str]]=...) -> None:
        ...

class PurgeExecutionsMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class AddExecutionEventsRequest(_message.Message):
    __slots__ = ('execution', 'events')
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    execution: str
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]

    def __init__(self, execution: _Optional[str]=..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]]=...) -> None:
        ...

class AddExecutionEventsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class QueryExecutionInputsAndOutputsRequest(_message.Message):
    __slots__ = ('execution',)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: str

    def __init__(self, execution: _Optional[str]=...) -> None:
        ...

class CreateMetadataSchemaRequest(_message.Message):
    __slots__ = ('parent', 'metadata_schema', 'metadata_schema_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    METADATA_SCHEMA_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metadata_schema: _metadata_schema_pb2.MetadataSchema
    metadata_schema_id: str

    def __init__(self, parent: _Optional[str]=..., metadata_schema: _Optional[_Union[_metadata_schema_pb2.MetadataSchema, _Mapping]]=..., metadata_schema_id: _Optional[str]=...) -> None:
        ...

class GetMetadataSchemaRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMetadataSchemasRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListMetadataSchemasResponse(_message.Message):
    __slots__ = ('metadata_schemas', 'next_page_token')
    METADATA_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metadata_schemas: _containers.RepeatedCompositeFieldContainer[_metadata_schema_pb2.MetadataSchema]
    next_page_token: str

    def __init__(self, metadata_schemas: _Optional[_Iterable[_Union[_metadata_schema_pb2.MetadataSchema, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class QueryArtifactLineageSubgraphRequest(_message.Message):
    __slots__ = ('artifact', 'max_hops', 'filter')
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    MAX_HOPS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    artifact: str
    max_hops: int
    filter: str

    def __init__(self, artifact: _Optional[str]=..., max_hops: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...