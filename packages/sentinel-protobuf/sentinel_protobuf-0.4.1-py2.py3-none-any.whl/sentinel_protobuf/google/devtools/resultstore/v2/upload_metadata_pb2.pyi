from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class UploadMetadata(_message.Message):
    __slots__ = ('name', 'resume_token', 'uploader_state')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    resume_token: str
    uploader_state: bytes

    def __init__(self, name: _Optional[str]=..., resume_token: _Optional[str]=..., uploader_state: _Optional[bytes]=...) -> None:
        ...