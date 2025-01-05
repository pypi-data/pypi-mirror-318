
from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventAllocate(_message.Message):
    __slots__ = ['acc_address', 'granted_bytes', 'id', 'utilised_bytes']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UTILISED_BYTES_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    granted_bytes: str
    id: int
    utilised_bytes: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., granted_bytes: _Optional[str]=..., utilised_bytes: _Optional[str]=...) -> None:
        ...

class EventCreate(_message.Message):
    __slots__ = ['acc_address', 'id', 'plan_id', 'price', 'prov_address']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    plan_id: int
    price: str
    prov_address: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., price: _Optional[str]=...) -> None:
        ...

class EventCreateSession(_message.Message):
    __slots__ = ['acc_address', 'id', 'node_address', 'subscription_id']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    node_address: str
    subscription_id: int

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., subscription_id: _Optional[int]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ['acc_address', 'id', 'payment', 'plan_id', 'prov_address', 'staking_reward']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    payment: str
    plan_id: int
    prov_address: str
    staking_reward: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRenew(_message.Message):
    __slots__ = ['acc_address', 'id', 'plan_id', 'price', 'prov_address']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    plan_id: int
    price: str
    prov_address: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., price: _Optional[str]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ['acc_address', 'id', 'inactive_at', 'plan_id', 'renewal_price_policy', 'status', 'status_at']
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    id: int
    inactive_at: str
    plan_id: int
    renewal_price_policy: str
    status: _status_pb2.Status
    status_at: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., renewal_price_policy: _Optional[str]=..., status: _Optional[_Union[(_status_pb2.Status, str)]]=..., inactive_at: _Optional[str]=..., status_at: _Optional[str]=...) -> None:
        ...
