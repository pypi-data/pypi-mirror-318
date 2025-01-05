from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EngineCallLog(_message.Message):
    __slots__ = ('execution_id', 'activity_time', 'state', 'step', 'callee', 'begun', 'succeeded', 'exception_raised', 'exception_handled')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[EngineCallLog.State]
        BEGUN: _ClassVar[EngineCallLog.State]
        SUCCEEDED: _ClassVar[EngineCallLog.State]
        EXCEPTION_RAISED: _ClassVar[EngineCallLog.State]
        EXCEPTION_HANDLED: _ClassVar[EngineCallLog.State]
    STATE_UNSPECIFIED: EngineCallLog.State
    BEGUN: EngineCallLog.State
    SUCCEEDED: EngineCallLog.State
    EXCEPTION_RAISED: EngineCallLog.State
    EXCEPTION_HANDLED: EngineCallLog.State

    class CallArg(_message.Message):
        __slots__ = ('argument',)
        ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        argument: str

        def __init__(self, argument: _Optional[str]=...) -> None:
            ...

    class Begun(_message.Message):
        __slots__ = ('args', 'named_args')

        class NamedArgsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
                ...
        ARGS_FIELD_NUMBER: _ClassVar[int]
        NAMED_ARGS_FIELD_NUMBER: _ClassVar[int]
        args: _containers.RepeatedCompositeFieldContainer[EngineCallLog.CallArg]
        named_args: _containers.MessageMap[str, _struct_pb2.Value]

        def __init__(self, args: _Optional[_Iterable[_Union[EngineCallLog.CallArg, _Mapping]]]=..., named_args: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
            ...

    class Succeeded(_message.Message):
        __slots__ = ('call_start_time', 'response')
        CALL_START_TIME_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_FIELD_NUMBER: _ClassVar[int]
        call_start_time: _timestamp_pb2.Timestamp
        response: str

        def __init__(self, call_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., response: _Optional[str]=...) -> None:
            ...

    class ExceptionRaised(_message.Message):
        __slots__ = ('call_start_time', 'exception', 'origin')
        CALL_START_TIME_FIELD_NUMBER: _ClassVar[int]
        EXCEPTION_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_FIELD_NUMBER: _ClassVar[int]
        call_start_time: _timestamp_pb2.Timestamp
        exception: str
        origin: str

        def __init__(self, call_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., exception: _Optional[str]=..., origin: _Optional[str]=...) -> None:
            ...

    class ExceptionHandled(_message.Message):
        __slots__ = ('call_start_time', 'exception', 'origin')
        CALL_START_TIME_FIELD_NUMBER: _ClassVar[int]
        EXCEPTION_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_FIELD_NUMBER: _ClassVar[int]
        call_start_time: _timestamp_pb2.Timestamp
        exception: str
        origin: str

        def __init__(self, call_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., exception: _Optional[str]=..., origin: _Optional[str]=...) -> None:
            ...
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    CALLEE_FIELD_NUMBER: _ClassVar[int]
    BEGUN_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_RAISED_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_HANDLED_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    activity_time: _timestamp_pb2.Timestamp
    state: EngineCallLog.State
    step: str
    callee: str
    begun: EngineCallLog.Begun
    succeeded: EngineCallLog.Succeeded
    exception_raised: EngineCallLog.ExceptionRaised
    exception_handled: EngineCallLog.ExceptionHandled

    def __init__(self, execution_id: _Optional[str]=..., activity_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[EngineCallLog.State, str]]=..., step: _Optional[str]=..., callee: _Optional[str]=..., begun: _Optional[_Union[EngineCallLog.Begun, _Mapping]]=..., succeeded: _Optional[_Union[EngineCallLog.Succeeded, _Mapping]]=..., exception_raised: _Optional[_Union[EngineCallLog.ExceptionRaised, _Mapping]]=..., exception_handled: _Optional[_Union[EngineCallLog.ExceptionHandled, _Mapping]]=...) -> None:
        ...