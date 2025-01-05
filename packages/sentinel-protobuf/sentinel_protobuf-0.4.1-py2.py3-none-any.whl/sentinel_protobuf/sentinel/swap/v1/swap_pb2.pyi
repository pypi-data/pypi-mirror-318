from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Swap(_message.Message):
    __slots__ = ('tx_hash', 'receiver', 'amount')
    TX_HASH_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    tx_hash: bytes
    receiver: str
    amount: _coin_pb2.Coin

    def __init__(self, tx_hash: _Optional[bytes]=..., receiver: _Optional[str]=..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...