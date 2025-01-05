from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.deposit.v1 import deposit_pb2 as _deposit_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ('deposits',)
    DEPOSITS_FIELD_NUMBER: _ClassVar[int]
    deposits: _containers.RepeatedCompositeFieldContainer[_deposit_pb2.Deposit]

    def __init__(self, deposits: _Optional[_Iterable[_Union[_deposit_pb2.Deposit, _Mapping]]]=...) -> None:
        ...