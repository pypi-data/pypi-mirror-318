from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IntegratedSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTEGRATED_SYSTEM_UNSPECIFIED: _ClassVar[IntegratedSystem]
    BIGQUERY: _ClassVar[IntegratedSystem]
    CLOUD_PUBSUB: _ClassVar[IntegratedSystem]

class ManagingSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGING_SYSTEM_UNSPECIFIED: _ClassVar[ManagingSystem]
    MANAGING_SYSTEM_DATAPLEX: _ClassVar[ManagingSystem]
    MANAGING_SYSTEM_OTHER: _ClassVar[ManagingSystem]
INTEGRATED_SYSTEM_UNSPECIFIED: IntegratedSystem
BIGQUERY: IntegratedSystem
CLOUD_PUBSUB: IntegratedSystem
MANAGING_SYSTEM_UNSPECIFIED: ManagingSystem
MANAGING_SYSTEM_DATAPLEX: ManagingSystem
MANAGING_SYSTEM_OTHER: ManagingSystem