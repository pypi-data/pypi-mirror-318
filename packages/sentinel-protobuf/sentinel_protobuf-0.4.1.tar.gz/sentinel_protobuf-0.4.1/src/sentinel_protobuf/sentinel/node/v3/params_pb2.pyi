from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('deposit', 'active_duration', 'min_gigabyte_prices', 'min_hourly_prices', 'max_session_gigabytes', 'min_session_gigabytes', 'max_session_hours', 'min_session_hours', 'staking_share')
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    MIN_HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    MAX_SESSION_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    MIN_SESSION_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_SESSION_HOURS_FIELD_NUMBER: _ClassVar[int]
    MIN_SESSION_HOURS_FIELD_NUMBER: _ClassVar[int]
    STAKING_SHARE_FIELD_NUMBER: _ClassVar[int]
    deposit: _coin_pb2.Coin
    active_duration: _duration_pb2.Duration
    min_gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    min_hourly_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    max_session_gigabytes: int
    min_session_gigabytes: int
    max_session_hours: int
    min_session_hours: int
    staking_share: str

    def __init__(self, deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., active_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., min_gigabyte_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., min_hourly_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., max_session_gigabytes: _Optional[int]=..., min_session_gigabytes: _Optional[int]=..., max_session_hours: _Optional[int]=..., min_session_hours: _Optional[int]=..., staking_share: _Optional[str]=...) -> None:
        ...