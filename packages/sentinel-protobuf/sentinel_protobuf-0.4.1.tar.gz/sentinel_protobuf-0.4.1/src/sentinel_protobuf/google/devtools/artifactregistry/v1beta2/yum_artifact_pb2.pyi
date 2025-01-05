from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class YumArtifact(_message.Message):
    __slots__ = ('name', 'package_name', 'package_type', 'architecture')

    class PackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PACKAGE_TYPE_UNSPECIFIED: _ClassVar[YumArtifact.PackageType]
        BINARY: _ClassVar[YumArtifact.PackageType]
        SOURCE: _ClassVar[YumArtifact.PackageType]
    PACKAGE_TYPE_UNSPECIFIED: YumArtifact.PackageType
    BINARY: YumArtifact.PackageType
    SOURCE: YumArtifact.PackageType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    name: str
    package_name: str
    package_type: YumArtifact.PackageType
    architecture: str

    def __init__(self, name: _Optional[str]=..., package_name: _Optional[str]=..., package_type: _Optional[_Union[YumArtifact.PackageType, str]]=..., architecture: _Optional[str]=...) -> None:
        ...

class ImportYumArtifactsGcsSource(_message.Message):
    __slots__ = ('uris', 'use_wildcards')
    URIS_FIELD_NUMBER: _ClassVar[int]
    USE_WILDCARDS_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]
    use_wildcards: bool

    def __init__(self, uris: _Optional[_Iterable[str]]=..., use_wildcards: bool=...) -> None:
        ...

class ImportYumArtifactsRequest(_message.Message):
    __slots__ = ('gcs_source', 'parent')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    gcs_source: ImportYumArtifactsGcsSource
    parent: str

    def __init__(self, gcs_source: _Optional[_Union[ImportYumArtifactsGcsSource, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class ImportYumArtifactsErrorInfo(_message.Message):
    __slots__ = ('gcs_source', 'error')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    gcs_source: ImportYumArtifactsGcsSource
    error: _status_pb2.Status

    def __init__(self, gcs_source: _Optional[_Union[ImportYumArtifactsGcsSource, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ImportYumArtifactsResponse(_message.Message):
    __slots__ = ('yum_artifacts', 'errors')
    YUM_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    yum_artifacts: _containers.RepeatedCompositeFieldContainer[YumArtifact]
    errors: _containers.RepeatedCompositeFieldContainer[ImportYumArtifactsErrorInfo]

    def __init__(self, yum_artifacts: _Optional[_Iterable[_Union[YumArtifact, _Mapping]]]=..., errors: _Optional[_Iterable[_Union[ImportYumArtifactsErrorInfo, _Mapping]]]=...) -> None:
        ...

class ImportYumArtifactsMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...