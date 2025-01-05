from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[SubscriptionType]
    TYPE_NODE: _ClassVar[SubscriptionType]
    TYPE_PLAN: _ClassVar[SubscriptionType]
TYPE_UNSPECIFIED: SubscriptionType
TYPE_NODE: SubscriptionType
TYPE_PLAN: SubscriptionType

class BaseSubscription(_message.Message):
    __slots__ = ('id', 'address', 'inactive_at', 'status', 'status_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    address: str
    inactive_at: _timestamp_pb2.Timestamp
    status: _status_pb2.Status
    status_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., address: _Optional[str]=..., inactive_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., status_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class NodeSubscription(_message.Message):
    __slots__ = ('base', 'node_address', 'gigabytes', 'hours', 'deposit')
    BASE_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    base: BaseSubscription
    node_address: str
    gigabytes: int
    hours: int
    deposit: _coin_pb2.Coin

    def __init__(self, base: _Optional[_Union[BaseSubscription, _Mapping]]=..., node_address: _Optional[str]=..., gigabytes: _Optional[int]=..., hours: _Optional[int]=..., deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class PlanSubscription(_message.Message):
    __slots__ = ('base', 'plan_id', 'denom')
    BASE_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    base: BaseSubscription
    plan_id: int
    denom: str

    def __init__(self, base: _Optional[_Union[BaseSubscription, _Mapping]]=..., plan_id: _Optional[int]=..., denom: _Optional[str]=...) -> None:
        ...