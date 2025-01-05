from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('id', 'node_address', 'prov_address', 'max_hours', 'price', 'renewal_price_policy')
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    prov_address: str
    max_hours: int
    price: str
    renewal_price_policy: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., max_hours: _Optional[int]=..., price: _Optional[str]=..., renewal_price_policy: _Optional[str]=...) -> None:
        ...

class EventEnd(_message.Message):
    __slots__ = ('id', 'node_address', 'prov_address')
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    prov_address: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ('id', 'node_address', 'prov_address', 'payment', 'staking_reward')
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    prov_address: str
    payment: str
    staking_reward: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRefund(_message.Message):
    __slots__ = ('id', 'prov_address', 'amount')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    prov_address: str
    amount: str

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., amount: _Optional[str]=...) -> None:
        ...

class EventRenew(_message.Message):
    __slots__ = ('id', 'node_address', 'prov_address', 'max_hours', 'price')
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    prov_address: str
    max_hours: int
    price: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., max_hours: _Optional[int]=..., price: _Optional[str]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ('id', 'node_address', 'prov_address', 'hours', 'renewal_price_policy', 'payout_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_address: str
    prov_address: str
    hours: int
    renewal_price_policy: str
    payout_at: str

    def __init__(self, id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., hours: _Optional[int]=..., renewal_price_policy: _Optional[str]=..., payout_at: _Optional[str]=...) -> None:
        ...