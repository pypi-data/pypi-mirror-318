from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IntegrationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTEGRATION_STATE_UNSPECIFIED: _ClassVar[IntegrationState]
    DRAFT: _ClassVar[IntegrationState]
    ACTIVE: _ClassVar[IntegrationState]
    ARCHIVED: _ClassVar[IntegrationState]
    SNAPSHOT: _ClassVar[IntegrationState]
INTEGRATION_STATE_UNSPECIFIED: IntegrationState
DRAFT: IntegrationState
ACTIVE: IntegrationState
ARCHIVED: IntegrationState
SNAPSHOT: IntegrationState