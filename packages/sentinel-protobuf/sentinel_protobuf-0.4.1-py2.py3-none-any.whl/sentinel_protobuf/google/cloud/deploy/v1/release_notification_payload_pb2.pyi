from google.cloud.deploy.v1 import log_enums_pb2 as _log_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReleaseNotificationEvent(_message.Message):
    __slots__ = ('message', 'pipeline_uid', 'release_uid', 'release', 'type')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_UID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_UID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    pipeline_uid: str
    release_uid: str
    release: str
    type: _log_enums_pb2.Type

    def __init__(self, message: _Optional[str]=..., pipeline_uid: _Optional[str]=..., release_uid: _Optional[str]=..., release: _Optional[str]=..., type: _Optional[_Union[_log_enums_pb2.Type, str]]=...) -> None:
        ...