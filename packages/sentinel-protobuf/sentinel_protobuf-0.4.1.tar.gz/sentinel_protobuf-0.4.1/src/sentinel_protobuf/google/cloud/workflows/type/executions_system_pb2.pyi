from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionsSystemLog(_message.Message):
    __slots__ = ('message', 'activity_time', 'state', 'start', 'success', 'failure')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ExecutionsSystemLog.State]
        ACTIVE: _ClassVar[ExecutionsSystemLog.State]
        SUCCEEDED: _ClassVar[ExecutionsSystemLog.State]
        FAILED: _ClassVar[ExecutionsSystemLog.State]
        CANCELLED: _ClassVar[ExecutionsSystemLog.State]
    STATE_UNSPECIFIED: ExecutionsSystemLog.State
    ACTIVE: ExecutionsSystemLog.State
    SUCCEEDED: ExecutionsSystemLog.State
    FAILED: ExecutionsSystemLog.State
    CANCELLED: ExecutionsSystemLog.State

    class Start(_message.Message):
        __slots__ = ('argument',)
        ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        argument: str

        def __init__(self, argument: _Optional[str]=...) -> None:
            ...

    class Success(_message.Message):
        __slots__ = ('result',)
        RESULT_FIELD_NUMBER: _ClassVar[int]
        result: str

        def __init__(self, result: _Optional[str]=...) -> None:
            ...

    class Failure(_message.Message):
        __slots__ = ('exception', 'source')
        EXCEPTION_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        exception: str
        source: str

        def __init__(self, exception: _Optional[str]=..., source: _Optional[str]=...) -> None:
            ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    message: str
    activity_time: _timestamp_pb2.Timestamp
    state: ExecutionsSystemLog.State
    start: ExecutionsSystemLog.Start
    success: ExecutionsSystemLog.Success
    failure: ExecutionsSystemLog.Failure

    def __init__(self, message: _Optional[str]=..., activity_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ExecutionsSystemLog.State, str]]=..., start: _Optional[_Union[ExecutionsSystemLog.Start, _Mapping]]=..., success: _Optional[_Union[ExecutionsSystemLog.Success, _Mapping]]=..., failure: _Optional[_Union[ExecutionsSystemLog.Failure, _Mapping]]=...) -> None:
        ...