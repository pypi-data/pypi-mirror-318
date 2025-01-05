from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apihub.v1 import common_fields_pb2 as _common_fields_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateApiRequest(_message.Message):
    __slots__ = ('parent', 'api_id', 'api')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_ID_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_id: str
    api: _common_fields_pb2.Api

    def __init__(self, parent: _Optional[str]=..., api_id: _Optional[str]=..., api: _Optional[_Union[_common_fields_pb2.Api, _Mapping]]=...) -> None:
        ...

class GetApiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateApiRequest(_message.Message):
    __slots__ = ('api', 'update_mask')
    API_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    api: _common_fields_pb2.Api
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, api: _Optional[_Union[_common_fields_pb2.Api, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteApiRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListApisRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListApisResponse(_message.Message):
    __slots__ = ('apis', 'next_page_token')
    APIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    apis: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.Api]
    next_page_token: str

    def __init__(self, apis: _Optional[_Iterable[_Union[_common_fields_pb2.Api, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateVersionRequest(_message.Message):
    __slots__ = ('parent', 'version_id', 'version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    version_id: str
    version: _common_fields_pb2.Version

    def __init__(self, parent: _Optional[str]=..., version_id: _Optional[str]=..., version: _Optional[_Union[_common_fields_pb2.Version, _Mapping]]=...) -> None:
        ...

class GetVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateVersionRequest(_message.Message):
    __slots__ = ('version', 'update_mask')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    version: _common_fields_pb2.Version
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, version: _Optional[_Union[_common_fields_pb2.Version, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteVersionRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVersionsResponse(_message.Message):
    __slots__ = ('versions', 'next_page_token')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.Version]
    next_page_token: str

    def __init__(self, versions: _Optional[_Iterable[_Union[_common_fields_pb2.Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateSpecRequest(_message.Message):
    __slots__ = ('parent', 'spec_id', 'spec')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    spec_id: str
    spec: _common_fields_pb2.Spec

    def __init__(self, parent: _Optional[str]=..., spec_id: _Optional[str]=..., spec: _Optional[_Union[_common_fields_pb2.Spec, _Mapping]]=...) -> None:
        ...

class GetSpecRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSpecRequest(_message.Message):
    __slots__ = ('spec', 'update_mask')
    SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    spec: _common_fields_pb2.Spec
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, spec: _Optional[_Union[_common_fields_pb2.Spec, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSpecRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSpecsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSpecsResponse(_message.Message):
    __slots__ = ('specs', 'next_page_token')
    SPECS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    specs: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.Spec]
    next_page_token: str

    def __init__(self, specs: _Optional[_Iterable[_Union[_common_fields_pb2.Spec, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetSpecContentsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetApiOperationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListApiOperationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListApiOperationsResponse(_message.Message):
    __slots__ = ('api_operations', 'next_page_token')
    API_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_operations: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.ApiOperation]
    next_page_token: str

    def __init__(self, api_operations: _Optional[_Iterable[_Union[_common_fields_pb2.ApiOperation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDefinitionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'deployment_id', 'deployment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment_id: str
    deployment: _common_fields_pb2.Deployment

    def __init__(self, parent: _Optional[str]=..., deployment_id: _Optional[str]=..., deployment: _Optional[_Union[_common_fields_pb2.Deployment, _Mapping]]=...) -> None:
        ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDeploymentRequest(_message.Message):
    __slots__ = ('deployment', 'update_mask')
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    deployment: _common_fields_pb2.Deployment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, deployment: _Optional[_Union[_common_fields_pb2.Deployment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDeploymentsResponse(_message.Message):
    __slots__ = ('deployments', 'next_page_token')
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.Deployment]
    next_page_token: str

    def __init__(self, deployments: _Optional[_Iterable[_Union[_common_fields_pb2.Deployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateAttributeRequest(_message.Message):
    __slots__ = ('parent', 'attribute_id', 'attribute')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    attribute_id: str
    attribute: _common_fields_pb2.Attribute

    def __init__(self, parent: _Optional[str]=..., attribute_id: _Optional[str]=..., attribute: _Optional[_Union[_common_fields_pb2.Attribute, _Mapping]]=...) -> None:
        ...

class GetAttributeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAttributeRequest(_message.Message):
    __slots__ = ('attribute', 'update_mask')
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    attribute: _common_fields_pb2.Attribute
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, attribute: _Optional[_Union[_common_fields_pb2.Attribute, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAttributeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAttributesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAttributesResponse(_message.Message):
    __slots__ = ('attributes', 'next_page_token')
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.Attribute]
    next_page_token: str

    def __init__(self, attributes: _Optional[_Iterable[_Union[_common_fields_pb2.Attribute, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchResourcesRequest(_message.Message):
    __slots__ = ('location', 'query', 'filter', 'page_size', 'page_token')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: str
    query: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, location: _Optional[str]=..., query: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ApiHubResource(_message.Message):
    __slots__ = ('api', 'operation', 'deployment', 'spec', 'definition', 'version')
    API_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    api: _common_fields_pb2.Api
    operation: _common_fields_pb2.ApiOperation
    deployment: _common_fields_pb2.Deployment
    spec: _common_fields_pb2.Spec
    definition: _common_fields_pb2.Definition
    version: _common_fields_pb2.Version

    def __init__(self, api: _Optional[_Union[_common_fields_pb2.Api, _Mapping]]=..., operation: _Optional[_Union[_common_fields_pb2.ApiOperation, _Mapping]]=..., deployment: _Optional[_Union[_common_fields_pb2.Deployment, _Mapping]]=..., spec: _Optional[_Union[_common_fields_pb2.Spec, _Mapping]]=..., definition: _Optional[_Union[_common_fields_pb2.Definition, _Mapping]]=..., version: _Optional[_Union[_common_fields_pb2.Version, _Mapping]]=...) -> None:
        ...

class SearchResult(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: ApiHubResource

    def __init__(self, resource: _Optional[_Union[ApiHubResource, _Mapping]]=...) -> None:
        ...

class SearchResourcesResponse(_message.Message):
    __slots__ = ('search_results', 'next_page_token')
    SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    next_page_token: str

    def __init__(self, search_results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDependencyRequest(_message.Message):
    __slots__ = ('parent', 'dependency_id', 'dependency')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dependency_id: str
    dependency: _common_fields_pb2.Dependency

    def __init__(self, parent: _Optional[str]=..., dependency_id: _Optional[str]=..., dependency: _Optional[_Union[_common_fields_pb2.Dependency, _Mapping]]=...) -> None:
        ...

class GetDependencyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDependencyRequest(_message.Message):
    __slots__ = ('dependency', 'update_mask')
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dependency: _common_fields_pb2.Dependency
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dependency: _Optional[_Union[_common_fields_pb2.Dependency, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDependencyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDependenciesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDependenciesResponse(_message.Message):
    __slots__ = ('dependencies', 'next_page_token')
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    dependencies: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.Dependency]
    next_page_token: str

    def __init__(self, dependencies: _Optional[_Iterable[_Union[_common_fields_pb2.Dependency, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateExternalApiRequest(_message.Message):
    __slots__ = ('parent', 'external_api_id', 'external_api')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_API_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_API_FIELD_NUMBER: _ClassVar[int]
    parent: str
    external_api_id: str
    external_api: _common_fields_pb2.ExternalApi

    def __init__(self, parent: _Optional[str]=..., external_api_id: _Optional[str]=..., external_api: _Optional[_Union[_common_fields_pb2.ExternalApi, _Mapping]]=...) -> None:
        ...

class GetExternalApiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateExternalApiRequest(_message.Message):
    __slots__ = ('external_api', 'update_mask')
    EXTERNAL_API_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    external_api: _common_fields_pb2.ExternalApi
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, external_api: _Optional[_Union[_common_fields_pb2.ExternalApi, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteExternalApiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListExternalApisRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListExternalApisResponse(_message.Message):
    __slots__ = ('external_apis', 'next_page_token')
    EXTERNAL_APIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    external_apis: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.ExternalApi]
    next_page_token: str

    def __init__(self, external_apis: _Optional[_Iterable[_Union[_common_fields_pb2.ExternalApi, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...