from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_LEVEL_UNSPECIFIED: _ClassVar[ServiceLevel]
    PREMIUM: _ClassVar[ServiceLevel]
    EXTREME: _ClassVar[ServiceLevel]
    STANDARD: _ClassVar[ServiceLevel]
    FLEX: _ClassVar[ServiceLevel]

class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_TYPE_UNSPECIFIED: _ClassVar[EncryptionType]
    SERVICE_MANAGED: _ClassVar[EncryptionType]
    CLOUD_KMS: _ClassVar[EncryptionType]
SERVICE_LEVEL_UNSPECIFIED: ServiceLevel
PREMIUM: ServiceLevel
EXTREME: ServiceLevel
STANDARD: ServiceLevel
FLEX: ServiceLevel
ENCRYPTION_TYPE_UNSPECIFIED: EncryptionType
SERVICE_MANAGED: EncryptionType
CLOUD_KMS: EncryptionType

class LocationMetadata(_message.Message):
    __slots__ = ('supported_service_levels',)
    SUPPORTED_SERVICE_LEVELS_FIELD_NUMBER: _ClassVar[int]
    supported_service_levels: _containers.RepeatedScalarFieldContainer[ServiceLevel]

    def __init__(self, supported_service_levels: _Optional[_Iterable[_Union[ServiceLevel, str]]]=...) -> None:
        ...