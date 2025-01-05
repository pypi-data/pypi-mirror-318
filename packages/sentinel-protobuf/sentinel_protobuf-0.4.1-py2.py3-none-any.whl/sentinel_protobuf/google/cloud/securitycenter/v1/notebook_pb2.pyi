from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Notebook(_message.Message):
    __slots__ = ('name', 'service', 'last_author', 'notebook_update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTHOR_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    service: str
    last_author: str
    notebook_update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., service: _Optional[str]=..., last_author: _Optional[str]=..., notebook_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...