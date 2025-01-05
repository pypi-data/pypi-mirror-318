from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TableReference(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'table_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class TableModifiers(_message.Message):
    __slots__ = ('snapshot_time',)
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    snapshot_time: _timestamp_pb2.Timestamp

    def __init__(self, snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...