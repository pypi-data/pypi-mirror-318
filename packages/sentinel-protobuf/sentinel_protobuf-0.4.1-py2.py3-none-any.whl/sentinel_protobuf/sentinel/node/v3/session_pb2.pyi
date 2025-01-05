from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ('id', 'acc_address', 'node_address', 'price', 'download_bytes', 'upload_bytes', 'max_gigabytes', 'duration', 'max_hours', 'status', 'inactive_at', 'status_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    node_address: str
    price: _price_pb2.Price
    download_bytes: str
    upload_bytes: str
    max_gigabytes: int
    duration: _duration_pb2.Duration
    max_hours: int
    status: _status_pb2.Status
    inactive_at: _timestamp_pb2.Timestamp
    status_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., price: _Optional[_Union[_price_pb2.Price, _Mapping]]=..., download_bytes: _Optional[str]=..., upload_bytes: _Optional[str]=..., max_gigabytes: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_hours: _Optional[int]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., inactive_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...