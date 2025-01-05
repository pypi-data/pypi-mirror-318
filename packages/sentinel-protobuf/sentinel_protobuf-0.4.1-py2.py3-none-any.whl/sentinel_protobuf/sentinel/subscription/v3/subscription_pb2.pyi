from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import renewal_pb2 as _renewal_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ('id', 'acc_address', 'plan_id', 'price', 'renewal_price_policy', 'status', 'inactive_at', 'status_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    acc_address: str
    plan_id: int
    price: _price_pb2.Price
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy
    status: _status_pb2.Status
    inactive_at: _timestamp_pb2.Timestamp
    status_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., acc_address: _Optional[str]=..., plan_id: _Optional[int]=..., price: _Optional[_Union[_price_pb2.Price, _Mapping]]=..., renewal_price_policy: _Optional[_Union[_renewal_pb2.RenewalPricePolicy, str]]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., inactive_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...