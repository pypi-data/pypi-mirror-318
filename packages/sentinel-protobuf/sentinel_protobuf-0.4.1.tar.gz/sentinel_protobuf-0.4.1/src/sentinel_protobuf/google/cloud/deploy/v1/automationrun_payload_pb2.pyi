from google.cloud.deploy.v1 import log_enums_pb2 as _log_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutomationRunEvent(_message.Message):
    __slots__ = ('message', 'automation_run', 'pipeline_uid', 'automation_id', 'rule_id', 'destination_target_id', 'type')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_RUN_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_UID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    automation_run: str
    pipeline_uid: str
    automation_id: str
    rule_id: str
    destination_target_id: str
    type: _log_enums_pb2.Type

    def __init__(self, message: _Optional[str]=..., automation_run: _Optional[str]=..., pipeline_uid: _Optional[str]=..., automation_id: _Optional[str]=..., rule_id: _Optional[str]=..., destination_target_id: _Optional[str]=..., type: _Optional[_Union[_log_enums_pb2.Type, str]]=...) -> None:
        ...