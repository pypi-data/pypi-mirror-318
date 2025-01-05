from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import deployed_model_ref_pb2 as _deployed_model_ref_pb2
from google.cloud.aiplatform.v1 import deployment_resource_pool_pb2 as _deployment_resource_pool_pb2
from google.cloud.aiplatform.v1 import endpoint_pb2 as _endpoint_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDeploymentResourcePoolRequest(_message.Message):
    __slots__ = ("parent", "deployment_resource_pool", "deployment_resource_pool_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_RESOURCE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment_resource_pool: _deployment_resource_pool_pb2.DeploymentResourcePool
    deployment_resource_pool_id: str
    def __init__(self, parent: _Optional[str] = ..., deployment_resource_pool: _Optional[_Union[_deployment_resource_pool_pb2.DeploymentResourcePool, _Mapping]] = ..., deployment_resource_pool_id: _Optional[str] = ...) -> None: ...

class CreateDeploymentResourcePoolOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class GetDeploymentResourcePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDeploymentResourcePoolsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDeploymentResourcePoolsResponse(_message.Message):
    __slots__ = ("deployment_resource_pools", "next_page_token")
    DEPLOYMENT_RESOURCE_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployment_resource_pools: _containers.RepeatedCompositeFieldContainer[_deployment_resource_pool_pb2.DeploymentResourcePool]
    next_page_token: str
    def __init__(self, deployment_resource_pools: _Optional[_Iterable[_Union[_deployment_resource_pool_pb2.DeploymentResourcePool, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateDeploymentResourcePoolRequest(_message.Message):
    __slots__ = ("deployment_resource_pool", "update_mask")
    DEPLOYMENT_RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    deployment_resource_pool: _deployment_resource_pool_pb2.DeploymentResourcePool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, deployment_resource_pool: _Optional[_Union[_deployment_resource_pool_pb2.DeploymentResourcePool, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDeploymentResourcePoolOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class DeleteDeploymentResourcePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class QueryDeployedModelsRequest(_message.Message):
    __slots__ = ("deployment_resource_pool", "page_size", "page_token")
    DEPLOYMENT_RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployment_resource_pool: str
    page_size: int
    page_token: str
    def __init__(self, deployment_resource_pool: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class QueryDeployedModelsResponse(_message.Message):
    __slots__ = ("deployed_models", "next_page_token", "deployed_model_refs", "total_deployed_model_count", "total_endpoint_count")
    DEPLOYED_MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_REFS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DEPLOYED_MODEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ENDPOINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    deployed_models: _containers.RepeatedCompositeFieldContainer[_endpoint_pb2.DeployedModel]
    next_page_token: str
    deployed_model_refs: _containers.RepeatedCompositeFieldContainer[_deployed_model_ref_pb2.DeployedModelRef]
    total_deployed_model_count: int
    total_endpoint_count: int
    def __init__(self, deployed_models: _Optional[_Iterable[_Union[_endpoint_pb2.DeployedModel, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., deployed_model_refs: _Optional[_Iterable[_Union[_deployed_model_ref_pb2.DeployedModelRef, _Mapping]]] = ..., total_deployed_model_count: _Optional[int] = ..., total_endpoint_count: _Optional[int] = ...) -> None: ...
