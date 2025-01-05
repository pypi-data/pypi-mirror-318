from google.rpc import code_pb2 as _code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ActionStatus(_message.Message):
    __slots__ = ('status_code', 'user_facing_message')
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    USER_FACING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status_code: _code_pb2.Code
    user_facing_message: str

    def __init__(self, status_code: _Optional[_Union[_code_pb2.Code, str]]=..., user_facing_message: _Optional[str]=...) -> None:
        ...