from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetEncryptionSpecRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EncryptionSpec(_message.Message):
    __slots__ = ('name', 'kms_key')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key: str

    def __init__(self, name: _Optional[str]=..., kms_key: _Optional[str]=...) -> None:
        ...

class InitializeEncryptionSpecRequest(_message.Message):
    __slots__ = ('encryption_spec',)
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    encryption_spec: EncryptionSpec

    def __init__(self, encryption_spec: _Optional[_Union[EncryptionSpec, _Mapping]]=...) -> None:
        ...

class InitializeEncryptionSpecResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class InitializeEncryptionSpecMetadata(_message.Message):
    __slots__ = ('request',)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: InitializeEncryptionSpecRequest

    def __init__(self, request: _Optional[_Union[InitializeEncryptionSpecRequest, _Mapping]]=...) -> None:
        ...