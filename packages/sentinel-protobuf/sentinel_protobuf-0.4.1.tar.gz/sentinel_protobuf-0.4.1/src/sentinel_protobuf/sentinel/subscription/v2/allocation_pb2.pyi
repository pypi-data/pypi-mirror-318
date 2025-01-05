from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Allocation(_message.Message):
    __slots__ = ('id', 'address', 'granted_bytes', 'utilised_bytes')
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UTILISED_BYTES_FIELD_NUMBER: _ClassVar[int]
    id: int
    address: str
    granted_bytes: str
    utilised_bytes: str

    def __init__(self, id: _Optional[int]=..., address: _Optional[str]=..., granted_bytes: _Optional[str]=..., utilised_bytes: _Optional[str]=...) -> None:
        ...