from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventPay(_message.Message):
    __slots__ = ('id', 'acc_address', 'node_address', 'payment', 'staking_reward')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    node_address: str
    payment: str
    staking_reward: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRefund(_message.Message):
    __slots__ = ('id', 'acc_address', 'amount')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    amount: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., amount: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('id', 'acc_address', 'node_address', 'download_bytes', 'upload_bytes', 'duration')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    node_address: str
    download_bytes: str
    upload_bytes: str
    duration: _duration_pb2.Duration

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., download_bytes: _Optional[str]=..., upload_bytes: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('id', 'acc_address', 'node_address', 'status', 'status_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    node_address: str
    status: _status_pb2.Status
    status_at: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., status_at: _Optional[str]=...) -> None:
        ...