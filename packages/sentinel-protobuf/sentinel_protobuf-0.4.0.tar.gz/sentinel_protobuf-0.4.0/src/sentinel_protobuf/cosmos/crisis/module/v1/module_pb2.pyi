
from cosmos.app.v1alpha1 import module_pb2 as _module_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Module(_message.Message):
    __slots__ = ['authority', 'fee_collector_name']
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    FEE_COLLECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    authority: str
    fee_collector_name: str

    def __init__(self, fee_collector_name: _Optional[str]=..., authority: _Optional[str]=...) -> None:
        ...
