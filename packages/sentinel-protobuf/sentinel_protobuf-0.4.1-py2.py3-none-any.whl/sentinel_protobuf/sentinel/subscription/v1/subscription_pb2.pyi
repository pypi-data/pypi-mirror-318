from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ('id', 'owner', 'node', 'price', 'deposit', 'plan', 'denom', 'expiry', 'free', 'status', 'status_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    owner: str
    node: str
    price: _coin_pb2.Coin
    deposit: _coin_pb2.Coin
    plan: int
    denom: str
    expiry: _timestamp_pb2.Timestamp
    free: str
    status: _status_pb2.Status
    status_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., owner: _Optional[str]=..., node: _Optional[str]=..., price: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., plan: _Optional[int]=..., denom: _Optional[str]=..., expiry: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., free: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., status_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...