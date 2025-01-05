from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AptArtifact(_message.Message):
    __slots__ = ('name', 'package_name', 'package_type', 'architecture', 'component', 'control_file')

    class PackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PACKAGE_TYPE_UNSPECIFIED: _ClassVar[AptArtifact.PackageType]
        BINARY: _ClassVar[AptArtifact.PackageType]
        SOURCE: _ClassVar[AptArtifact.PackageType]
    PACKAGE_TYPE_UNSPECIFIED: AptArtifact.PackageType
    BINARY: AptArtifact.PackageType
    SOURCE: AptArtifact.PackageType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FILE_FIELD_NUMBER: _ClassVar[int]
    name: str
    package_name: str
    package_type: AptArtifact.PackageType
    architecture: str
    component: str
    control_file: bytes

    def __init__(self, name: _Optional[str]=..., package_name: _Optional[str]=..., package_type: _Optional[_Union[AptArtifact.PackageType, str]]=..., architecture: _Optional[str]=..., component: _Optional[str]=..., control_file: _Optional[bytes]=...) -> None:
        ...

class ImportAptArtifactsGcsSource(_message.Message):
    __slots__ = ('uris', 'use_wildcards')
    URIS_FIELD_NUMBER: _ClassVar[int]
    USE_WILDCARDS_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]
    use_wildcards: bool

    def __init__(self, uris: _Optional[_Iterable[str]]=..., use_wildcards: bool=...) -> None:
        ...

class ImportAptArtifactsRequest(_message.Message):
    __slots__ = ('gcs_source', 'parent')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    gcs_source: ImportAptArtifactsGcsSource
    parent: str

    def __init__(self, gcs_source: _Optional[_Union[ImportAptArtifactsGcsSource, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class ImportAptArtifactsErrorInfo(_message.Message):
    __slots__ = ('gcs_source', 'error')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    gcs_source: ImportAptArtifactsGcsSource
    error: _status_pb2.Status

    def __init__(self, gcs_source: _Optional[_Union[ImportAptArtifactsGcsSource, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ImportAptArtifactsResponse(_message.Message):
    __slots__ = ('apt_artifacts', 'errors')
    APT_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    apt_artifacts: _containers.RepeatedCompositeFieldContainer[AptArtifact]
    errors: _containers.RepeatedCompositeFieldContainer[ImportAptArtifactsErrorInfo]

    def __init__(self, apt_artifacts: _Optional[_Iterable[_Union[AptArtifact, _Mapping]]]=..., errors: _Optional[_Iterable[_Union[ImportAptArtifactsErrorInfo, _Mapping]]]=...) -> None:
        ...

class ImportAptArtifactsMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...