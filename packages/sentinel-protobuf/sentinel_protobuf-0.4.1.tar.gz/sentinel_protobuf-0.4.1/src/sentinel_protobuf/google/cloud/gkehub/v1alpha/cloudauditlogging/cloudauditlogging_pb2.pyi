from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureSpec(_message.Message):
    __slots__ = ('allowlisted_service_accounts',)
    ALLOWLISTED_SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    allowlisted_service_accounts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, allowlisted_service_accounts: _Optional[_Iterable[str]]=...) -> None:
        ...