from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TollInfo(_message.Message):
    __slots__ = ('estimated_price',)
    ESTIMATED_PRICE_FIELD_NUMBER: _ClassVar[int]
    estimated_price: _containers.RepeatedCompositeFieldContainer[_money_pb2.Money]

    def __init__(self, estimated_price: _Optional[_Iterable[_Union[_money_pb2.Money, _Mapping]]]=...) -> None:
        ...