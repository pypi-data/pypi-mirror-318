from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('id', 'prov_address', 'gigabytes', 'hours', 'prices', 'private')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    prov_address: str
    gigabytes: int
    hours: int
    prices: str
    private: bool

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., gigabytes: _Optional[int]=..., hours: _Optional[int]=..., prices: _Optional[str]=..., private: bool=...) -> None:
        ...

class EventLinkNode(_message.Message):
    __slots__ = ('id', 'prov_address', 'node_address')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    prov_address: str
    node_address: str

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., node_address: _Optional[str]=...) -> None:
        ...

class EventUnlinkNode(_message.Message):
    __slots__ = ('id', 'prov_address', 'node_address')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    prov_address: str
    node_address: str

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., node_address: _Optional[str]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ('id', 'prov_address', 'status')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    prov_address: str
    status: _status_pb2.Status

    def __init__(self, id: _Optional[int]=..., prov_address: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=...) -> None:
        ...