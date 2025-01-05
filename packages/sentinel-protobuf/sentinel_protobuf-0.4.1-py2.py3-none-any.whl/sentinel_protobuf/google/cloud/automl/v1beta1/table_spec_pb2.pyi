from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1beta1 import io_pb2 as _io_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TableSpec(_message.Message):
    __slots__ = ('name', 'time_column_spec_id', 'row_count', 'valid_row_count', 'column_count', 'input_configs', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_COLUMN_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALID_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_column_spec_id: str
    row_count: int
    valid_row_count: int
    column_count: int
    input_configs: _containers.RepeatedCompositeFieldContainer[_io_pb2.InputConfig]
    etag: str

    def __init__(self, name: _Optional[str]=..., time_column_spec_id: _Optional[str]=..., row_count: _Optional[int]=..., valid_row_count: _Optional[int]=..., column_count: _Optional[int]=..., input_configs: _Optional[_Iterable[_Union[_io_pb2.InputConfig, _Mapping]]]=..., etag: _Optional[str]=...) -> None:
        ...