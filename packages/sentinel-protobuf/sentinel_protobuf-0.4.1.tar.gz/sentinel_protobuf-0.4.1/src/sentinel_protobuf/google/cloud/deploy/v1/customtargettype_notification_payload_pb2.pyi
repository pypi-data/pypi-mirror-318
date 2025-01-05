from google.cloud.deploy.v1 import log_enums_pb2 as _log_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomTargetTypeNotificationEvent(_message.Message):
    __slots__ = ('message', 'custom_target_type_uid', 'custom_target_type', 'type')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_UID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    custom_target_type_uid: str
    custom_target_type: str
    type: _log_enums_pb2.Type

    def __init__(self, message: _Optional[str]=..., custom_target_type_uid: _Optional[str]=..., custom_target_type: _Optional[str]=..., type: _Optional[_Union[_log_enums_pb2.Type, str]]=...) -> None:
        ...