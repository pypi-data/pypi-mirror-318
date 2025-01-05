from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreateSubscription(_message.Message):
    __slots__ = ('address', 'node_address', 'id')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    node_address: str
    id: int

    def __init__(self, address: _Optional[str]=..., node_address: _Optional[str]=..., id: _Optional[int]=...) -> None:
        ...

class EventRegister(_message.Message):
    __slots__ = ('address',)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str

    def __init__(self, address: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('address', 'gigabyte_prices', 'hourly_prices', 'remote_url')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    address: str
    gigabyte_prices: str
    hourly_prices: str
    remote_url: str

    def __init__(self, address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_url: _Optional[str]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('status', 'address')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    address: str

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, str]]=..., address: _Optional[str]=...) -> None:
        ...