from google.type import money_pb2 as _money_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PriceRange(_message.Message):
    __slots__ = ('start_price', 'end_price')
    START_PRICE_FIELD_NUMBER: _ClassVar[int]
    END_PRICE_FIELD_NUMBER: _ClassVar[int]
    start_price: _money_pb2.Money
    end_price: _money_pb2.Money

    def __init__(self, start_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., end_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
        ...