from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Deployment(_message.Message):
    __slots__ = ('files', 'container', 'zip', 'cloud_build_options')

    class FilesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FileInfo

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[FileInfo, _Mapping]]=...) -> None:
            ...
    FILES_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BUILD_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    files: _containers.MessageMap[str, FileInfo]
    container: ContainerInfo
    zip: ZipInfo
    cloud_build_options: CloudBuildOptions

    def __init__(self, files: _Optional[_Mapping[str, FileInfo]]=..., container: _Optional[_Union[ContainerInfo, _Mapping]]=..., zip: _Optional[_Union[ZipInfo, _Mapping]]=..., cloud_build_options: _Optional[_Union[CloudBuildOptions, _Mapping]]=...) -> None:
        ...

class FileInfo(_message.Message):
    __slots__ = ('source_url', 'sha1_sum', 'mime_type')
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    SHA1_SUM_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    source_url: str
    sha1_sum: str
    mime_type: str

    def __init__(self, source_url: _Optional[str]=..., sha1_sum: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class ContainerInfo(_message.Message):
    __slots__ = ('image',)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: str

    def __init__(self, image: _Optional[str]=...) -> None:
        ...

class CloudBuildOptions(_message.Message):
    __slots__ = ('app_yaml_path', 'cloud_build_timeout')
    APP_YAML_PATH_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BUILD_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    app_yaml_path: str
    cloud_build_timeout: _duration_pb2.Duration

    def __init__(self, app_yaml_path: _Optional[str]=..., cloud_build_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ZipInfo(_message.Message):
    __slots__ = ('source_url', 'files_count')
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    FILES_COUNT_FIELD_NUMBER: _ClassVar[int]
    source_url: str
    files_count: int

    def __init__(self, source_url: _Optional[str]=..., files_count: _Optional[int]=...) -> None:
        ...