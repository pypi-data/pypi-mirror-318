from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventAllocate(_message.Message):
    __slots__ = ('id', 'acc_address', 'granted_bytes', 'utilised_bytes')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UTILISED_BYTES_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    granted_bytes: str
    utilised_bytes: str

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., granted_bytes: _Optional[str]=..., utilised_bytes: _Optional[str]=...) -> None:
        ...

class EventCreate(_message.Message):
    __slots__ = ('id', 'plan_id', 'acc_address', 'prov_address', 'price')
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    plan_id: int
    acc_address: str
    prov_address: str
    price: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., price: _Optional[str]=...) -> None:
        ...

class EventCreateSession(_message.Message):
    __slots__ = ('id', 'acc_address', 'node_address', 'subscription_id')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    node_address: str
    subscription_id: int

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., subscription_id: _Optional[int]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ('id', 'plan_id', 'acc_address', 'prov_address', 'payment', 'staking_reward')
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    plan_id: int
    acc_address: str
    prov_address: str
    payment: str
    staking_reward: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRenew(_message.Message):
    __slots__ = ('id', 'plan_id', 'acc_address', 'prov_address', 'price')
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    plan_id: int
    acc_address: str
    prov_address: str
    price: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., price: _Optional[str]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ('id', 'plan_id', 'acc_address', 'renewal_price_policy', 'status', 'inactive_at', 'status_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    plan_id: int
    acc_address: str
    renewal_price_policy: str
    status: _status_pb2.Status
    inactive_at: str
    status_at: str

    def __init__(self, id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., renewal_price_policy: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., inactive_at: _Optional[str]=..., status_at: _Optional[str]=...) -> None:
        ...