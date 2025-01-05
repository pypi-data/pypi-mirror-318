
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ['acc_address', 'download_bytes', 'duration', 'id', 'inactive_at', 'node_address', 'status', 'status_at', 'subscription_id', 'upload_bytes']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    download_bytes: str
    duration: _duration_pb2.Duration
    id: int
    inactive_at: _timestamp_pb2.Timestamp
    node_address: str
    status: _status_pb2.Status
    status_at: _timestamp_pb2.Timestamp
    subscription_id: int
    upload_bytes: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., subscription_id: _Optional[int]=..., download_bytes: _Optional[str]=..., upload_bytes: _Optional[str]=..., duration: _Optional[_Union[(_duration_pb2.Duration, _Mapping)]]=..., status: _Optional[_Union[(_status_pb2.Status, str)]]=..., inactive_at: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=..., status_at: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...
