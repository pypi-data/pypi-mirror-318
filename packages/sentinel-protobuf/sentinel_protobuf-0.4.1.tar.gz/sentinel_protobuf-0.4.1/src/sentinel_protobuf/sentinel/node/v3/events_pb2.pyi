from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('node_address', 'gigabyte_prices', 'hourly_prices', 'remote_url')
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    gigabyte_prices: str
    hourly_prices: str
    remote_url: str

    def __init__(self, node_address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_url: _Optional[str]=...) -> None:
        ...

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
    __slots__ = ('node_address', 'gigabyte_prices', 'hourly_prices', 'remote_url')
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    gigabyte_prices: str
    hourly_prices: str
    remote_url: str

    def __init__(self, node_address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_url: _Optional[str]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('node_address', 'status')
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    status: _status_pb2.Status

    def __init__(self, node_address: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=...) -> None:
        ...

class EventCreateSession(_message.Message):
    __slots__ = ('id', 'acc_address', 'node_address', 'price', 'max_gigabytes', 'max_hours')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    MAX_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    node_address: str
    price: str
    max_gigabytes: int
    max_hours: int

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., price: _Optional[str]=..., max_gigabytes: _Optional[int]=..., max_hours: _Optional[int]=...) -> None:
        ...