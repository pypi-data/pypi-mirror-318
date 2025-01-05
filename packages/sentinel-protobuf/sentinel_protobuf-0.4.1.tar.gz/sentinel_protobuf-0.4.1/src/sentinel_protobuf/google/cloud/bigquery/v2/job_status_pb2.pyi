from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobStatus(_message.Message):
    __slots__ = ('error_result', 'errors', 'state')
    ERROR_RESULT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    error_result: _error_pb2.ErrorProto
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    state: str

    def __init__(self, error_result: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]]=..., errors: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]]=..., state: _Optional[str]=...) -> None:
        ...