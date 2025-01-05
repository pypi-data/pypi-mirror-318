
from cosmos.app.v1alpha1 import module_pb2 as _module_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Module(_message.Message):
    __slots__ = ['authority', 'blocked_module_accounts_override']
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_MODULE_ACCOUNTS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    authority: str
    blocked_module_accounts_override: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, blocked_module_accounts_override: _Optional[_Iterable[str]]=..., authority: _Optional[str]=...) -> None:
        ...
