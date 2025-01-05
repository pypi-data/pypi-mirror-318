
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import renewal_pb2 as _renewal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Lease(_message.Message):
    __slots__ = ['hours', 'id', 'inactive_at', 'max_hours', 'node_address', 'payout_at', 'price', 'prov_address', 'renewal_price_policy']
    HOURS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_AT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    hours: int
    id: int
    inactive_at: _timestamp_pb2.Timestamp
    max_hours: int
    node_address: str
    payout_at: _timestamp_pb2.Timestamp
    price: _price_pb2.Price
    prov_address: str
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., node_address: _Optional[str]=..., price: _Optional[_Union[(_price_pb2.Price, _Mapping)]]=..., hours: _Optional[int]=..., max_hours: _Optional[int]=..., renewal_price_policy: _Optional[_Union[(_renewal_pb2.RenewalPricePolicy, str)]]=..., inactive_at: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=..., payout_at: _Optional[_Union[(_timestamp_pb2.Timestamp, _Mapping)]]=...) -> None:
        ...
