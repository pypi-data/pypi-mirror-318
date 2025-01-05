
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Price(_message.Message):
    __slots__ = ['base_value', 'denom', 'quote_value']
    BASE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    QUOTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    base_value: str
    denom: str
    quote_value: str

    def __init__(self, denom: _Optional[str]=..., base_value: _Optional[str]=..., quote_value: _Optional[str]=...) -> None:
        ...
