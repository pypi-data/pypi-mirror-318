from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import renewal_pb2 as _renewal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Lease(_message.Message):
    __slots__ = ('id', 'prov_address', 'node_address', 'price', 'hours', 'max_hours', 'renewal_price_policy', 'inactive_at', 'payout_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    prov_address: str
    node_address: str
    price: _price_pb2.Price
    hours: int
    max_hours: int
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy
    inactive_at: _timestamp_pb2.Timestamp
    payout_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., node_address: _Optional[str]=..., price: _Optional[_Union[_price_pb2.Price, _Mapping]]=..., hours: _Optional[int]=..., max_hours: _Optional[int]=..., renewal_price_policy: _Optional[_Union[_renewal_pb2.RenewalPricePolicy, str]]=..., inactive_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., payout_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...