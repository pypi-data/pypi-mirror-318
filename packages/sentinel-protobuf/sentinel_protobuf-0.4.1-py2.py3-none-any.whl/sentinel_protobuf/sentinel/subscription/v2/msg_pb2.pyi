from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class MsgAllocateRequest(_message.Message):
    __slots__ = ('id', 'address', 'bytes')
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    id: int
    address: str
    bytes: str

    def __init__(self, id: _Optional[int]=..., address: _Optional[str]=..., bytes: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgCancelRequest(_message.Message):
    __slots__ = ('id',)
    FROM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=..., **kwargs) -> None:
        ...

class MsgAllocateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgCancelResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...