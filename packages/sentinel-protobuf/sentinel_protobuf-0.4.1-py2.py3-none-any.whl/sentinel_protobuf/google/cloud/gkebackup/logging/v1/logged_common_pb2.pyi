from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Namespaces(_message.Message):
    __slots__ = ('namespaces',)
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    namespaces: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, namespaces: _Optional[_Iterable[str]]=...) -> None:
        ...

class NamespacedName(_message.Message):
    __slots__ = ('namespace', 'name')
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str

    def __init__(self, namespace: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class NamespacedNames(_message.Message):
    __slots__ = ('namespaced_names',)
    NAMESPACED_NAMES_FIELD_NUMBER: _ClassVar[int]
    namespaced_names: _containers.RepeatedCompositeFieldContainer[NamespacedName]

    def __init__(self, namespaced_names: _Optional[_Iterable[_Union[NamespacedName, _Mapping]]]=...) -> None:
        ...

class EncryptionKey(_message.Message):
    __slots__ = ('gcp_kms_encryption_key',)
    GCP_KMS_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    gcp_kms_encryption_key: str

    def __init__(self, gcp_kms_encryption_key: _Optional[str]=...) -> None:
        ...