from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SubmitBuildRequest(_message.Message):
    __slots__ = ('parent', 'storage_source', 'image_uri', 'buildpack_build', 'docker_build', 'service_account', 'worker_pool', 'tags')

    class DockerBuild(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class BuildpacksBuild(_message.Message):
        __slots__ = ('runtime', 'function_target', 'cache_image_uri', 'base_image', 'environment_variables', 'enable_automatic_updates')

        class EnvironmentVariablesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        FUNCTION_TARGET_FIELD_NUMBER: _ClassVar[int]
        CACHE_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
        BASE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
        ENABLE_AUTOMATIC_UPDATES_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        function_target: str
        cache_image_uri: str
        base_image: str
        environment_variables: _containers.ScalarMap[str, str]
        enable_automatic_updates: bool

        def __init__(self, runtime: _Optional[str]=..., function_target: _Optional[str]=..., cache_image_uri: _Optional[str]=..., base_image: _Optional[str]=..., environment_variables: _Optional[_Mapping[str, str]]=..., enable_automatic_updates: bool=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    BUILDPACK_BUILD_FIELD_NUMBER: _ClassVar[int]
    DOCKER_BUILD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    storage_source: StorageSource
    image_uri: str
    buildpack_build: SubmitBuildRequest.BuildpacksBuild
    docker_build: SubmitBuildRequest.DockerBuild
    service_account: str
    worker_pool: str
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., storage_source: _Optional[_Union[StorageSource, _Mapping]]=..., image_uri: _Optional[str]=..., buildpack_build: _Optional[_Union[SubmitBuildRequest.BuildpacksBuild, _Mapping]]=..., docker_build: _Optional[_Union[SubmitBuildRequest.DockerBuild, _Mapping]]=..., service_account: _Optional[str]=..., worker_pool: _Optional[str]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class SubmitBuildResponse(_message.Message):
    __slots__ = ('build_operation', 'base_image_uri', 'base_image_warning')
    BUILD_OPERATION_FIELD_NUMBER: _ClassVar[int]
    BASE_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    BASE_IMAGE_WARNING_FIELD_NUMBER: _ClassVar[int]
    build_operation: _operations_pb2.Operation
    base_image_uri: str
    base_image_warning: str

    def __init__(self, build_operation: _Optional[_Union[_operations_pb2.Operation, _Mapping]]=..., base_image_uri: _Optional[str]=..., base_image_warning: _Optional[str]=...) -> None:
        ...

class StorageSource(_message.Message):
    __slots__ = ('bucket', 'object', 'generation')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=...) -> None:
        ...