from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from sentinel.types.v1 import bandwidth_pb2 as _bandwidth_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Proof(_message.Message):
    __slots__ = ('id', 'duration', 'bandwidth')
    ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    id: int
    duration: _duration_pb2.Duration
    bandwidth: _bandwidth_pb2.Bandwidth

    def __init__(self, id: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., bandwidth: _Optional[_Union[_bandwidth_pb2.Bandwidth, _Mapping]]=...) -> None:
        ...