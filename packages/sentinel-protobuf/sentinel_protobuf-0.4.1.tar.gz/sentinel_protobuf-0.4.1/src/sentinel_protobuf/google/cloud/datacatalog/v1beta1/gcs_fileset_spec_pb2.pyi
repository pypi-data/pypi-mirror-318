from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.datacatalog.v1beta1 import timestamps_pb2 as _timestamps_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GcsFilesetSpec(_message.Message):
    __slots__ = ('file_patterns', 'sample_gcs_file_specs')
    FILE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_GCS_FILE_SPECS_FIELD_NUMBER: _ClassVar[int]
    file_patterns: _containers.RepeatedScalarFieldContainer[str]
    sample_gcs_file_specs: _containers.RepeatedCompositeFieldContainer[GcsFileSpec]

    def __init__(self, file_patterns: _Optional[_Iterable[str]]=..., sample_gcs_file_specs: _Optional[_Iterable[_Union[GcsFileSpec, _Mapping]]]=...) -> None:
        ...

class GcsFileSpec(_message.Message):
    __slots__ = ('file_path', 'gcs_timestamps', 'size_bytes')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    GCS_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    gcs_timestamps: _timestamps_pb2.SystemTimestamps
    size_bytes: int

    def __init__(self, file_path: _Optional[str]=..., gcs_timestamps: _Optional[_Union[_timestamps_pb2.SystemTimestamps, _Mapping]]=..., size_bytes: _Optional[int]=...) -> None:
        ...