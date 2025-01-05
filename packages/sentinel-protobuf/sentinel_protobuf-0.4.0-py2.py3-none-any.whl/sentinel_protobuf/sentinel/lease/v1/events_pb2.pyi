
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ['id', 'max_hours', 'node_address', 'price', 'prov_address', 'renewal_price_policy']
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: int
    max_hours: int
    node_address: str
    price: str
    prov_address: str
    renewal_price_policy: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., max_hours: _Optional[int]=..., price: _Optional[str]=..., renewal_price_policy: _Optional[str]=...) -> None:
        ...

class EventEnd(_message.Message):
    __slots__ = ['id', 'node_address', 'prov_address']
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    prov_address: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ['id', 'node_address', 'payment', 'prov_address', 'staking_reward']
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    payment: str
    prov_address: str
    staking_reward: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRefund(_message.Message):
    __slots__ = ['amount', 'id', 'prov_address']
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    amount: str
    id: int
    prov_address: str

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., amount: _Optional[str]=...) -> None:
        ...

class EventRenew(_message.Message):
    __slots__ = ['id', 'max_hours', 'node_address', 'price', 'prov_address']
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    max_hours: int
    node_address: str
    price: str
    prov_address: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., max_hours: _Optional[int]=..., price: _Optional[str]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ['hours', 'id', 'node_address', 'payout_at', 'prov_address', 'renewal_price_policy']
    HOURS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_AT_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    hours: int
    id: int
    node_address: str
    payout_at: str
    prov_address: str
    renewal_price_policy: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., hours: _Optional[int]=..., renewal_price_policy: _Optional[str]=..., payout_at: _Optional[str]=...) -> None:
        ...
