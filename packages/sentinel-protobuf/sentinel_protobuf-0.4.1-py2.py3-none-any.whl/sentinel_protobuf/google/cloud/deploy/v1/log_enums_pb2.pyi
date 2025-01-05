from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[Type]
    TYPE_PUBSUB_NOTIFICATION_FAILURE: _ClassVar[Type]
    TYPE_RESOURCE_STATE_CHANGE: _ClassVar[Type]
    TYPE_PROCESS_ABORTED: _ClassVar[Type]
    TYPE_RESTRICTION_VIOLATED: _ClassVar[Type]
    TYPE_RESOURCE_DELETED: _ClassVar[Type]
    TYPE_ROLLOUT_UPDATE: _ClassVar[Type]
    TYPE_DEPLOY_POLICY_EVALUATION: _ClassVar[Type]
    TYPE_RENDER_STATUES_CHANGE: _ClassVar[Type]
TYPE_UNSPECIFIED: Type
TYPE_PUBSUB_NOTIFICATION_FAILURE: Type
TYPE_RESOURCE_STATE_CHANGE: Type
TYPE_PROCESS_ABORTED: Type
TYPE_RESTRICTION_VIOLATED: Type
TYPE_RESOURCE_DELETED: Type
TYPE_ROLLOUT_UPDATE: Type
TYPE_DEPLOY_POLICY_EVALUATION: Type
TYPE_RENDER_STATUES_CHANGE: Type