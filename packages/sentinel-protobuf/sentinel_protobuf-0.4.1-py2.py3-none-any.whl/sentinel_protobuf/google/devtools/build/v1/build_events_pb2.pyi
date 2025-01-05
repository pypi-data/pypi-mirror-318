from google.devtools.build.v1 import build_status_pb2 as _build_status_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConsoleOutputStream(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ConsoleOutputStream]
    STDOUT: _ClassVar[ConsoleOutputStream]
    STDERR: _ClassVar[ConsoleOutputStream]
UNKNOWN: ConsoleOutputStream
STDOUT: ConsoleOutputStream
STDERR: ConsoleOutputStream

class BuildEvent(_message.Message):
    __slots__ = ('event_time', 'invocation_attempt_started', 'invocation_attempt_finished', 'build_enqueued', 'build_finished', 'console_output', 'component_stream_finished', 'bazel_event', 'build_execution_event', 'source_fetch_event')

    class InvocationAttemptStarted(_message.Message):
        __slots__ = ('attempt_number', 'details')
        ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        attempt_number: int
        details: _any_pb2.Any

        def __init__(self, attempt_number: _Optional[int]=..., details: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
            ...

    class InvocationAttemptFinished(_message.Message):
        __slots__ = ('invocation_status', 'details')
        INVOCATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        invocation_status: _build_status_pb2.BuildStatus
        details: _any_pb2.Any

        def __init__(self, invocation_status: _Optional[_Union[_build_status_pb2.BuildStatus, _Mapping]]=..., details: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
            ...

    class BuildEnqueued(_message.Message):
        __slots__ = ('details',)
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        details: _any_pb2.Any

        def __init__(self, details: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
            ...

    class BuildFinished(_message.Message):
        __slots__ = ('status', 'details')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        status: _build_status_pb2.BuildStatus
        details: _any_pb2.Any

        def __init__(self, status: _Optional[_Union[_build_status_pb2.BuildStatus, _Mapping]]=..., details: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
            ...

    class ConsoleOutput(_message.Message):
        __slots__ = ('type', 'text_output', 'binary_output')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TEXT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        BINARY_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        type: ConsoleOutputStream
        text_output: str
        binary_output: bytes

        def __init__(self, type: _Optional[_Union[ConsoleOutputStream, str]]=..., text_output: _Optional[str]=..., binary_output: _Optional[bytes]=...) -> None:
            ...

    class BuildComponentStreamFinished(_message.Message):
        __slots__ = ('type',)

        class FinishType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FINISH_TYPE_UNSPECIFIED: _ClassVar[BuildEvent.BuildComponentStreamFinished.FinishType]
            FINISHED: _ClassVar[BuildEvent.BuildComponentStreamFinished.FinishType]
            EXPIRED: _ClassVar[BuildEvent.BuildComponentStreamFinished.FinishType]
        FINISH_TYPE_UNSPECIFIED: BuildEvent.BuildComponentStreamFinished.FinishType
        FINISHED: BuildEvent.BuildComponentStreamFinished.FinishType
        EXPIRED: BuildEvent.BuildComponentStreamFinished.FinishType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: BuildEvent.BuildComponentStreamFinished.FinishType

        def __init__(self, type: _Optional[_Union[BuildEvent.BuildComponentStreamFinished.FinishType, str]]=...) -> None:
            ...
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_ATTEMPT_STARTED_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_ATTEMPT_FINISHED_FIELD_NUMBER: _ClassVar[int]
    BUILD_ENQUEUED_FIELD_NUMBER: _ClassVar[int]
    BUILD_FINISHED_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_STREAM_FINISHED_FIELD_NUMBER: _ClassVar[int]
    BAZEL_EVENT_FIELD_NUMBER: _ClassVar[int]
    BUILD_EXECUTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FETCH_EVENT_FIELD_NUMBER: _ClassVar[int]
    event_time: _timestamp_pb2.Timestamp
    invocation_attempt_started: BuildEvent.InvocationAttemptStarted
    invocation_attempt_finished: BuildEvent.InvocationAttemptFinished
    build_enqueued: BuildEvent.BuildEnqueued
    build_finished: BuildEvent.BuildFinished
    console_output: BuildEvent.ConsoleOutput
    component_stream_finished: BuildEvent.BuildComponentStreamFinished
    bazel_event: _any_pb2.Any
    build_execution_event: _any_pb2.Any
    source_fetch_event: _any_pb2.Any

    def __init__(self, event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., invocation_attempt_started: _Optional[_Union[BuildEvent.InvocationAttemptStarted, _Mapping]]=..., invocation_attempt_finished: _Optional[_Union[BuildEvent.InvocationAttemptFinished, _Mapping]]=..., build_enqueued: _Optional[_Union[BuildEvent.BuildEnqueued, _Mapping]]=..., build_finished: _Optional[_Union[BuildEvent.BuildFinished, _Mapping]]=..., console_output: _Optional[_Union[BuildEvent.ConsoleOutput, _Mapping]]=..., component_stream_finished: _Optional[_Union[BuildEvent.BuildComponentStreamFinished, _Mapping]]=..., bazel_event: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., build_execution_event: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., source_fetch_event: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
        ...

class StreamId(_message.Message):
    __slots__ = ('build_id', 'invocation_id', 'component')

    class BuildComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_COMPONENT: _ClassVar[StreamId.BuildComponent]
        CONTROLLER: _ClassVar[StreamId.BuildComponent]
        WORKER: _ClassVar[StreamId.BuildComponent]
        TOOL: _ClassVar[StreamId.BuildComponent]
    UNKNOWN_COMPONENT: StreamId.BuildComponent
    CONTROLLER: StreamId.BuildComponent
    WORKER: StreamId.BuildComponent
    TOOL: StreamId.BuildComponent
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    build_id: str
    invocation_id: str
    component: StreamId.BuildComponent

    def __init__(self, build_id: _Optional[str]=..., invocation_id: _Optional[str]=..., component: _Optional[_Union[StreamId.BuildComponent, str]]=...) -> None:
        ...