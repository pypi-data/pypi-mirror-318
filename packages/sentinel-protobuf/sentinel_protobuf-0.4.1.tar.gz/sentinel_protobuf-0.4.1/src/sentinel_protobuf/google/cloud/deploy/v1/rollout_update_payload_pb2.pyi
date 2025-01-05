from google.cloud.deploy.v1 import log_enums_pb2 as _log_enums_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RolloutUpdateEvent(_message.Message):
    __slots__ = ('message', 'pipeline_uid', 'release_uid', 'release', 'rollout', 'target_id', 'type', 'rollout_update_type')

    class RolloutUpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLLOUT_UPDATE_TYPE_UNSPECIFIED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        PENDING: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        PENDING_RELEASE: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        IN_PROGRESS: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        CANCELLING: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        CANCELLED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        HALTED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        SUCCEEDED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        FAILED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        APPROVAL_REQUIRED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        APPROVED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        REJECTED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        ADVANCE_REQUIRED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
        ADVANCED: _ClassVar[RolloutUpdateEvent.RolloutUpdateType]
    ROLLOUT_UPDATE_TYPE_UNSPECIFIED: RolloutUpdateEvent.RolloutUpdateType
    PENDING: RolloutUpdateEvent.RolloutUpdateType
    PENDING_RELEASE: RolloutUpdateEvent.RolloutUpdateType
    IN_PROGRESS: RolloutUpdateEvent.RolloutUpdateType
    CANCELLING: RolloutUpdateEvent.RolloutUpdateType
    CANCELLED: RolloutUpdateEvent.RolloutUpdateType
    HALTED: RolloutUpdateEvent.RolloutUpdateType
    SUCCEEDED: RolloutUpdateEvent.RolloutUpdateType
    FAILED: RolloutUpdateEvent.RolloutUpdateType
    APPROVAL_REQUIRED: RolloutUpdateEvent.RolloutUpdateType
    APPROVED: RolloutUpdateEvent.RolloutUpdateType
    REJECTED: RolloutUpdateEvent.RolloutUpdateType
    ADVANCE_REQUIRED: RolloutUpdateEvent.RolloutUpdateType
    ADVANCED: RolloutUpdateEvent.RolloutUpdateType
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_UID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_UID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    pipeline_uid: str
    release_uid: str
    release: str
    rollout: str
    target_id: str
    type: _log_enums_pb2.Type
    rollout_update_type: RolloutUpdateEvent.RolloutUpdateType

    def __init__(self, message: _Optional[str]=..., pipeline_uid: _Optional[str]=..., release_uid: _Optional[str]=..., release: _Optional[str]=..., rollout: _Optional[str]=..., target_id: _Optional[str]=..., type: _Optional[_Union[_log_enums_pb2.Type, str]]=..., rollout_update_type: _Optional[_Union[RolloutUpdateEvent.RolloutUpdateType, str]]=...) -> None:
        ...