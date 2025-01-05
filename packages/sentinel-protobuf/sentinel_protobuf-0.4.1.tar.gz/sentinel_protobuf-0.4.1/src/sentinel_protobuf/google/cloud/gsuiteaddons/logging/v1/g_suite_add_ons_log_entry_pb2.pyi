from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GSuiteAddOnsLogEntry(_message.Message):
    __slots__ = ('deployment', 'error', 'deployment_function')
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    deployment: str
    error: _status_pb2.Status
    deployment_function: str

    def __init__(self, deployment: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., deployment_function: _Optional[str]=...) -> None:
        ...