from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('swap_enabled', 'swap_denom', 'approve_by')
    SWAP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SWAP_DENOM_FIELD_NUMBER: _ClassVar[int]
    APPROVE_BY_FIELD_NUMBER: _ClassVar[int]
    swap_enabled: bool
    swap_denom: str
    approve_by: str

    def __init__(self, swap_enabled: bool=..., swap_denom: _Optional[str]=..., approve_by: _Optional[str]=...) -> None:
        ...