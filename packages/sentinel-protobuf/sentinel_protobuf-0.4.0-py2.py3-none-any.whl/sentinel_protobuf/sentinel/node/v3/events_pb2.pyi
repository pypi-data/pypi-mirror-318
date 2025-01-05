
from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ['gigabyte_prices', 'hourly_prices', 'node_address', 'remote_url']
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    gigabyte_prices: str
    hourly_prices: str
    node_address: str
    remote_url: str

    def __init__(self, node_address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_url: _Optional[str]=...) -> None:
        ...

class EventCreateSession(_message.Message):
    __slots__ = ['acc_address', 'id', 'max_gigabytes', 'max_hours', 'node_address', 'price']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    max_gigabytes: int
    max_hours: int
    node_address: str
    price: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., price: _Optional[str]=..., max_gigabytes: _Optional[int]=..., max_hours: _Optional[int]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ['acc_address', 'id', 'node_address', 'payment', 'staking_reward']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    node_address: str
    payment: str
    staking_reward: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRefund(_message.Message):
    __slots__ = ['acc_address', 'amount', 'id']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    amount: str
    id: int

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., amount: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ['gigabyte_prices', 'hourly_prices', 'node_address', 'remote_url']
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    gigabyte_prices: str
    hourly_prices: str
    node_address: str
    remote_url: str

    def __init__(self, node_address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_url: _Optional[str]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ['node_address', 'status']
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    status: _status_pb2.Status

    def __init__(self, node_address: _Optional[str]=..., status: _Optional[_Union[(_status_pb2.Status, str)]]=...) -> None:
        ...
