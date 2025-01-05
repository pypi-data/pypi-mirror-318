from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AssessmentTaskDetails(_message.Message):
    __slots__ = ('input_path', 'output_dataset', 'querylogs_path', 'data_source')
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DATASET_FIELD_NUMBER: _ClassVar[int]
    QUERYLOGS_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    input_path: str
    output_dataset: str
    querylogs_path: str
    data_source: str

    def __init__(self, input_path: _Optional[str]=..., output_dataset: _Optional[str]=..., querylogs_path: _Optional[str]=..., data_source: _Optional[str]=...) -> None:
        ...

class AssessmentOrchestrationResultDetails(_message.Message):
    __slots__ = ('output_tables_schema_version',)
    OUTPUT_TABLES_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    output_tables_schema_version: str

    def __init__(self, output_tables_schema_version: _Optional[str]=...) -> None:
        ...