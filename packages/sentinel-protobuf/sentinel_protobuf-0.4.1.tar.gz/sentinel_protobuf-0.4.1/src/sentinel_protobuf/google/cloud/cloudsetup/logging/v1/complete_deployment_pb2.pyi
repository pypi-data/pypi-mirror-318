from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CompleteDeploymentEvent(_message.Message):
    __slots__ = ('value', 'error', 'state', 'preview_only')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CompleteDeploymentEvent.State]
        SUCCEEDED: _ClassVar[CompleteDeploymentEvent.State]
        FAILED: _ClassVar[CompleteDeploymentEvent.State]
    STATE_UNSPECIFIED: CompleteDeploymentEvent.State
    SUCCEEDED: CompleteDeploymentEvent.State
    FAILED: CompleteDeploymentEvent.State
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ONLY_FIELD_NUMBER: _ClassVar[int]
    value: CompleteDeploymentResult
    error: _status_pb2.Status
    state: CompleteDeploymentEvent.State
    preview_only: bool

    def __init__(self, value: _Optional[_Union[CompleteDeploymentResult, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., state: _Optional[_Union[CompleteDeploymentEvent.State, str]]=..., preview_only: bool=...) -> None:
        ...

class CompleteDeploymentResult(_message.Message):
    __slots__ = ('deployment', 'preview', 'message')
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    deployment: str
    preview: str
    message: str

    def __init__(self, deployment: _Optional[str]=..., preview: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...