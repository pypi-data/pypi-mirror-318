from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Proof(_message.Message):
    __slots__ = ('id', 'download_bytes', 'upload_bytes', 'duration')
    ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    download_bytes: str
    upload_bytes: str
    duration: _duration_pb2.Duration

    def __init__(self, id: _Optional[int]=..., download_bytes: _Optional[str]=..., upload_bytes: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...