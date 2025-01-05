from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdManagerError(_message.Message):
    __slots__ = ('error_code', 'message', 'field_path', 'trigger', 'stack_trace', 'details')
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    message: str
    field_path: str
    trigger: str
    stack_trace: str
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]

    def __init__(self, error_code: _Optional[str]=..., message: _Optional[str]=..., field_path: _Optional[str]=..., trigger: _Optional[str]=..., stack_trace: _Optional[str]=..., details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=...) -> None:
        ...