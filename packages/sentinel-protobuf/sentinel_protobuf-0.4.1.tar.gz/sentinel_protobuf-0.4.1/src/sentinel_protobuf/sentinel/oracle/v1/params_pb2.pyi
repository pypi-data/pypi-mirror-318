from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('block_interval', 'channel_id', 'port_id', 'timeout')
    BLOCK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    block_interval: int
    channel_id: str
    port_id: str
    timeout: _duration_pb2.Duration

    def __init__(self, block_interval: _Optional[int]=..., channel_id: _Optional[str]=..., port_id: _Optional[str]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...