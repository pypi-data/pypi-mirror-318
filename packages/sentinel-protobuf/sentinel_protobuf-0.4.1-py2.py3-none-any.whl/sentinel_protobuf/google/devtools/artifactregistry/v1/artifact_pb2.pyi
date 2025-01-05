from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DockerImage(_message.Message):
    __slots__ = ('name', 'uri', 'tags', 'image_size_bytes', 'upload_time', 'media_type', 'build_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    image_size_bytes: int
    upload_time: _timestamp_pb2.Timestamp
    media_type: str
    build_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., uri: _Optional[str]=..., tags: _Optional[_Iterable[str]]=..., image_size_bytes: _Optional[int]=..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., media_type: _Optional[str]=..., build_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListDockerImagesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDockerImagesResponse(_message.Message):
    __slots__ = ('docker_images', 'next_page_token')
    DOCKER_IMAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    docker_images: _containers.RepeatedCompositeFieldContainer[DockerImage]
    next_page_token: str

    def __init__(self, docker_images: _Optional[_Iterable[_Union[DockerImage, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDockerImageRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MavenArtifact(_message.Message):
    __slots__ = ('name', 'pom_uri', 'group_id', 'artifact_id', 'version', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    POM_URI_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    pom_uri: str
    group_id: str
    artifact_id: str
    version: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., pom_uri: _Optional[str]=..., group_id: _Optional[str]=..., artifact_id: _Optional[str]=..., version: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListMavenArtifactsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMavenArtifactsResponse(_message.Message):
    __slots__ = ('maven_artifacts', 'next_page_token')
    MAVEN_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    maven_artifacts: _containers.RepeatedCompositeFieldContainer[MavenArtifact]
    next_page_token: str

    def __init__(self, maven_artifacts: _Optional[_Iterable[_Union[MavenArtifact, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetMavenArtifactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class NpmPackage(_message.Message):
    __slots__ = ('name', 'package_name', 'version', 'tags', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    package_name: str
    version: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., package_name: _Optional[str]=..., version: _Optional[str]=..., tags: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListNpmPackagesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListNpmPackagesResponse(_message.Message):
    __slots__ = ('npm_packages', 'next_page_token')
    NPM_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    npm_packages: _containers.RepeatedCompositeFieldContainer[NpmPackage]
    next_page_token: str

    def __init__(self, npm_packages: _Optional[_Iterable[_Union[NpmPackage, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetNpmPackageRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PythonPackage(_message.Message):
    __slots__ = ('name', 'uri', 'package_name', 'version', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri: str
    package_name: str
    version: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., uri: _Optional[str]=..., package_name: _Optional[str]=..., version: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListPythonPackagesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPythonPackagesResponse(_message.Message):
    __slots__ = ('python_packages', 'next_page_token')
    PYTHON_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    python_packages: _containers.RepeatedCompositeFieldContainer[PythonPackage]
    next_page_token: str

    def __init__(self, python_packages: _Optional[_Iterable[_Union[PythonPackage, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPythonPackageRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...