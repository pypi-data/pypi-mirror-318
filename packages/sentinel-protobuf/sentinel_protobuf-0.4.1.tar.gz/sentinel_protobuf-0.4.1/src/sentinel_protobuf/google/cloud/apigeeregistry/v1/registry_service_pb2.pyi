from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apigeeregistry.v1 import registry_models_pb2 as _registry_models_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListApisRequest(_message.Message):
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

class ListApisResponse(_message.Message):
    __slots__ = ('apis', 'next_page_token')
    APIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    apis: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.Api]
    next_page_token: str

    def __init__(self, apis: _Optional[_Iterable[_Union[_registry_models_pb2.Api, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetApiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateApiRequest(_message.Message):
    __slots__ = ('parent', 'api', 'api_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    API_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api: _registry_models_pb2.Api
    api_id: str

    def __init__(self, parent: _Optional[str]=..., api: _Optional[_Union[_registry_models_pb2.Api, _Mapping]]=..., api_id: _Optional[str]=...) -> None:
        ...

class UpdateApiRequest(_message.Message):
    __slots__ = ('api', 'update_mask', 'allow_missing')
    API_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    api: _registry_models_pb2.Api
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, api: _Optional[_Union[_registry_models_pb2.Api, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteApiRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListApiVersionsRequest(_message.Message):
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

class ListApiVersionsResponse(_message.Message):
    __slots__ = ('api_versions', 'next_page_token')
    API_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_versions: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.ApiVersion]
    next_page_token: str

    def __init__(self, api_versions: _Optional[_Iterable[_Union[_registry_models_pb2.ApiVersion, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetApiVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateApiVersionRequest(_message.Message):
    __slots__ = ('parent', 'api_version', 'api_version_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_version: _registry_models_pb2.ApiVersion
    api_version_id: str

    def __init__(self, parent: _Optional[str]=..., api_version: _Optional[_Union[_registry_models_pb2.ApiVersion, _Mapping]]=..., api_version_id: _Optional[str]=...) -> None:
        ...

class UpdateApiVersionRequest(_message.Message):
    __slots__ = ('api_version', 'update_mask', 'allow_missing')
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    api_version: _registry_models_pb2.ApiVersion
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, api_version: _Optional[_Union[_registry_models_pb2.ApiVersion, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteApiVersionRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListApiSpecsRequest(_message.Message):
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

class ListApiSpecsResponse(_message.Message):
    __slots__ = ('api_specs', 'next_page_token')
    API_SPECS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_specs: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.ApiSpec]
    next_page_token: str

    def __init__(self, api_specs: _Optional[_Iterable[_Union[_registry_models_pb2.ApiSpec, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetApiSpecRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetApiSpecContentsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateApiSpecRequest(_message.Message):
    __slots__ = ('parent', 'api_spec', 'api_spec_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_SPEC_FIELD_NUMBER: _ClassVar[int]
    API_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_spec: _registry_models_pb2.ApiSpec
    api_spec_id: str

    def __init__(self, parent: _Optional[str]=..., api_spec: _Optional[_Union[_registry_models_pb2.ApiSpec, _Mapping]]=..., api_spec_id: _Optional[str]=...) -> None:
        ...

class UpdateApiSpecRequest(_message.Message):
    __slots__ = ('api_spec', 'update_mask', 'allow_missing')
    API_SPEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    api_spec: _registry_models_pb2.ApiSpec
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, api_spec: _Optional[_Union[_registry_models_pb2.ApiSpec, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteApiSpecRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class TagApiSpecRevisionRequest(_message.Message):
    __slots__ = ('name', 'tag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag: str

    def __init__(self, name: _Optional[str]=..., tag: _Optional[str]=...) -> None:
        ...

class ListApiSpecRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListApiSpecRevisionsResponse(_message.Message):
    __slots__ = ('api_specs', 'next_page_token')
    API_SPECS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_specs: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.ApiSpec]
    next_page_token: str

    def __init__(self, api_specs: _Optional[_Iterable[_Union[_registry_models_pb2.ApiSpec, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RollbackApiSpecRequest(_message.Message):
    __slots__ = ('name', 'revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...

class DeleteApiSpecRevisionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListApiDeploymentsRequest(_message.Message):
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

class ListApiDeploymentsResponse(_message.Message):
    __slots__ = ('api_deployments', 'next_page_token')
    API_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_deployments: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.ApiDeployment]
    next_page_token: str

    def __init__(self, api_deployments: _Optional[_Iterable[_Union[_registry_models_pb2.ApiDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetApiDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateApiDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'api_deployment', 'api_deployment_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    API_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_deployment: _registry_models_pb2.ApiDeployment
    api_deployment_id: str

    def __init__(self, parent: _Optional[str]=..., api_deployment: _Optional[_Union[_registry_models_pb2.ApiDeployment, _Mapping]]=..., api_deployment_id: _Optional[str]=...) -> None:
        ...

class UpdateApiDeploymentRequest(_message.Message):
    __slots__ = ('api_deployment', 'update_mask', 'allow_missing')
    API_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    api_deployment: _registry_models_pb2.ApiDeployment
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, api_deployment: _Optional[_Union[_registry_models_pb2.ApiDeployment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class DeleteApiDeploymentRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class TagApiDeploymentRevisionRequest(_message.Message):
    __slots__ = ('name', 'tag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag: str

    def __init__(self, name: _Optional[str]=..., tag: _Optional[str]=...) -> None:
        ...

class ListApiDeploymentRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListApiDeploymentRevisionsResponse(_message.Message):
    __slots__ = ('api_deployments', 'next_page_token')
    API_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_deployments: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.ApiDeployment]
    next_page_token: str

    def __init__(self, api_deployments: _Optional[_Iterable[_Union[_registry_models_pb2.ApiDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RollbackApiDeploymentRequest(_message.Message):
    __slots__ = ('name', 'revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...

class DeleteApiDeploymentRevisionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListArtifactsRequest(_message.Message):
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

class ListArtifactsResponse(_message.Message):
    __slots__ = ('artifacts', 'next_page_token')
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[_registry_models_pb2.Artifact]
    next_page_token: str

    def __init__(self, artifacts: _Optional[_Iterable[_Union[_registry_models_pb2.Artifact, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetArtifactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetArtifactContentsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateArtifactRequest(_message.Message):
    __slots__ = ('parent', 'artifact', 'artifact_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    artifact: _registry_models_pb2.Artifact
    artifact_id: str

    def __init__(self, parent: _Optional[str]=..., artifact: _Optional[_Union[_registry_models_pb2.Artifact, _Mapping]]=..., artifact_id: _Optional[str]=...) -> None:
        ...

class ReplaceArtifactRequest(_message.Message):
    __slots__ = ('artifact',)
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    artifact: _registry_models_pb2.Artifact

    def __init__(self, artifact: _Optional[_Union[_registry_models_pb2.Artifact, _Mapping]]=...) -> None:
        ...

class DeleteArtifactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...