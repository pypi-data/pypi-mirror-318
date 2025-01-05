from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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

class VolumeTypeEnum(_message.Message):
    __slots__ = ()

    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME_TYPE_UNSPECIFIED: _ClassVar[VolumeTypeEnum.VolumeType]
        GCE_PERSISTENT_DISK: _ClassVar[VolumeTypeEnum.VolumeType]
    VOLUME_TYPE_UNSPECIFIED: VolumeTypeEnum.VolumeType
    GCE_PERSISTENT_DISK: VolumeTypeEnum.VolumeType

    def __init__(self) -> None:
        ...