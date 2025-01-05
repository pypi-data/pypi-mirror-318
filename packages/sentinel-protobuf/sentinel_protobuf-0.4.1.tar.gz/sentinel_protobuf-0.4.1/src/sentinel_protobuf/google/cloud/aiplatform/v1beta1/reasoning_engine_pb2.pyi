from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReasoningEngineSpec(_message.Message):
    __slots__ = ('package_spec', 'class_methods')

    class PackageSpec(_message.Message):
        __slots__ = ('pickle_object_gcs_uri', 'dependency_files_gcs_uri', 'requirements_gcs_uri', 'python_version')
        PICKLE_OBJECT_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCY_FILES_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        REQUIREMENTS_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        PYTHON_VERSION_FIELD_NUMBER: _ClassVar[int]
        pickle_object_gcs_uri: str
        dependency_files_gcs_uri: str
        requirements_gcs_uri: str
        python_version: str

        def __init__(self, pickle_object_gcs_uri: _Optional[str]=..., dependency_files_gcs_uri: _Optional[str]=..., requirements_gcs_uri: _Optional[str]=..., python_version: _Optional[str]=...) -> None:
            ...
    PACKAGE_SPEC_FIELD_NUMBER: _ClassVar[int]
    CLASS_METHODS_FIELD_NUMBER: _ClassVar[int]
    package_spec: ReasoningEngineSpec.PackageSpec
    class_methods: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]

    def __init__(self, package_spec: _Optional[_Union[ReasoningEngineSpec.PackageSpec, _Mapping]]=..., class_methods: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]]=...) -> None:
        ...

class ReasoningEngine(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'spec', 'create_time', 'update_time', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    spec: ReasoningEngineSpec
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., spec: _Optional[_Union[ReasoningEngineSpec, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...