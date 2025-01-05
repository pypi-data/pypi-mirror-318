from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ('reason', 'location', 'debug_info', 'message')
    REASON_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    reason: str
    location: str
    debug_info: str
    message: str

    def __init__(self, reason: _Optional[str]=..., location: _Optional[str]=..., debug_info: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...