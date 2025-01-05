from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('prov_address', 'name', 'identity', 'website', 'description')
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    prov_address: str
    name: str
    identity: str
    website: str
    description: str

    def __init__(self, prov_address: _Optional[str]=..., name: _Optional[str]=..., identity: _Optional[str]=..., website: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('prov_address', 'name', 'identity', 'website', 'description')
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    prov_address: str
    name: str
    identity: str
    website: str
    description: str

    def __init__(self, prov_address: _Optional[str]=..., name: _Optional[str]=..., identity: _Optional[str]=..., website: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('prov_address', 'status')
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    prov_address: str
    status: _status_pb2.Status

    def __init__(self, prov_address: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=...) -> None:
        ...