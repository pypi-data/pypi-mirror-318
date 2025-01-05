from google.api import resource_pb2 as _resource_pb2
from google.cloud.datalabeling.v1beta1 import dataset_pb2 as _dataset_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Instruction(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'data_type', 'csv_instruction', 'pdf_instruction', 'blocking_resources')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CSV_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    PDF_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    data_type: _dataset_pb2.DataType
    csv_instruction: CsvInstruction
    pdf_instruction: PdfInstruction
    blocking_resources: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_type: _Optional[_Union[_dataset_pb2.DataType, str]]=..., csv_instruction: _Optional[_Union[CsvInstruction, _Mapping]]=..., pdf_instruction: _Optional[_Union[PdfInstruction, _Mapping]]=..., blocking_resources: _Optional[_Iterable[str]]=...) -> None:
        ...

class CsvInstruction(_message.Message):
    __slots__ = ('gcs_file_uri',)
    GCS_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    gcs_file_uri: str

    def __init__(self, gcs_file_uri: _Optional[str]=...) -> None:
        ...

class PdfInstruction(_message.Message):
    __slots__ = ('gcs_file_uri',)
    GCS_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    gcs_file_uri: str

    def __init__(self, gcs_file_uri: _Optional[str]=...) -> None:
        ...