from google.devtools.source.v1 import source_context_pb2 as _source_context_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FormatMessage(_message.Message):
    __slots__ = ('format', 'parameters')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    format: str
    parameters: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, format: _Optional[str]=..., parameters: _Optional[_Iterable[str]]=...) -> None:
        ...

class StatusMessage(_message.Message):
    __slots__ = ('is_error', 'refers_to', 'description')

    class Reference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[StatusMessage.Reference]
        BREAKPOINT_SOURCE_LOCATION: _ClassVar[StatusMessage.Reference]
        BREAKPOINT_CONDITION: _ClassVar[StatusMessage.Reference]
        BREAKPOINT_EXPRESSION: _ClassVar[StatusMessage.Reference]
        BREAKPOINT_AGE: _ClassVar[StatusMessage.Reference]
        VARIABLE_NAME: _ClassVar[StatusMessage.Reference]
        VARIABLE_VALUE: _ClassVar[StatusMessage.Reference]
    UNSPECIFIED: StatusMessage.Reference
    BREAKPOINT_SOURCE_LOCATION: StatusMessage.Reference
    BREAKPOINT_CONDITION: StatusMessage.Reference
    BREAKPOINT_EXPRESSION: StatusMessage.Reference
    BREAKPOINT_AGE: StatusMessage.Reference
    VARIABLE_NAME: StatusMessage.Reference
    VARIABLE_VALUE: StatusMessage.Reference
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    REFERS_TO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    is_error: bool
    refers_to: StatusMessage.Reference
    description: FormatMessage

    def __init__(self, is_error: bool=..., refers_to: _Optional[_Union[StatusMessage.Reference, str]]=..., description: _Optional[_Union[FormatMessage, _Mapping]]=...) -> None:
        ...

class SourceLocation(_message.Message):
    __slots__ = ('path', 'line', 'column')
    PATH_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    path: str
    line: int
    column: int

    def __init__(self, path: _Optional[str]=..., line: _Optional[int]=..., column: _Optional[int]=...) -> None:
        ...

class Variable(_message.Message):
    __slots__ = ('name', 'value', 'type', 'members', 'var_table_index', 'status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    VAR_TABLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    type: str
    members: _containers.RepeatedCompositeFieldContainer[Variable]
    var_table_index: _wrappers_pb2.Int32Value
    status: StatusMessage

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=..., type: _Optional[str]=..., members: _Optional[_Iterable[_Union[Variable, _Mapping]]]=..., var_table_index: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., status: _Optional[_Union[StatusMessage, _Mapping]]=...) -> None:
        ...

class StackFrame(_message.Message):
    __slots__ = ('function', 'location', 'arguments', 'locals')
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    LOCALS_FIELD_NUMBER: _ClassVar[int]
    function: str
    location: SourceLocation
    arguments: _containers.RepeatedCompositeFieldContainer[Variable]
    locals: _containers.RepeatedCompositeFieldContainer[Variable]

    def __init__(self, function: _Optional[str]=..., location: _Optional[_Union[SourceLocation, _Mapping]]=..., arguments: _Optional[_Iterable[_Union[Variable, _Mapping]]]=..., locals: _Optional[_Iterable[_Union[Variable, _Mapping]]]=...) -> None:
        ...

class Breakpoint(_message.Message):
    __slots__ = ('id', 'action', 'location', 'condition', 'expressions', 'log_message_format', 'log_level', 'is_final_state', 'create_time', 'final_time', 'user_email', 'status', 'stack_frames', 'evaluated_expressions', 'variable_table', 'labels')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPTURE: _ClassVar[Breakpoint.Action]
        LOG: _ClassVar[Breakpoint.Action]
    CAPTURE: Breakpoint.Action
    LOG: Breakpoint.Action

    class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INFO: _ClassVar[Breakpoint.LogLevel]
        WARNING: _ClassVar[Breakpoint.LogLevel]
        ERROR: _ClassVar[Breakpoint.LogLevel]
    INFO: Breakpoint.LogLevel
    WARNING: Breakpoint.LogLevel
    ERROR: Breakpoint.LogLevel

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    LOG_MESSAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FINAL_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STACK_FRAMES_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_TABLE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    action: Breakpoint.Action
    location: SourceLocation
    condition: str
    expressions: _containers.RepeatedScalarFieldContainer[str]
    log_message_format: str
    log_level: Breakpoint.LogLevel
    is_final_state: bool
    create_time: _timestamp_pb2.Timestamp
    final_time: _timestamp_pb2.Timestamp
    user_email: str
    status: StatusMessage
    stack_frames: _containers.RepeatedCompositeFieldContainer[StackFrame]
    evaluated_expressions: _containers.RepeatedCompositeFieldContainer[Variable]
    variable_table: _containers.RepeatedCompositeFieldContainer[Variable]
    labels: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., action: _Optional[_Union[Breakpoint.Action, str]]=..., location: _Optional[_Union[SourceLocation, _Mapping]]=..., condition: _Optional[str]=..., expressions: _Optional[_Iterable[str]]=..., log_message_format: _Optional[str]=..., log_level: _Optional[_Union[Breakpoint.LogLevel, str]]=..., is_final_state: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., final_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., user_email: _Optional[str]=..., status: _Optional[_Union[StatusMessage, _Mapping]]=..., stack_frames: _Optional[_Iterable[_Union[StackFrame, _Mapping]]]=..., evaluated_expressions: _Optional[_Iterable[_Union[Variable, _Mapping]]]=..., variable_table: _Optional[_Iterable[_Union[Variable, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Debuggee(_message.Message):
    __slots__ = ('id', 'project', 'uniquifier', 'description', 'is_inactive', 'agent_version', 'is_disabled', 'status', 'source_contexts', 'ext_source_contexts', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    UNIQUIFIER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    EXT_SOURCE_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project: str
    uniquifier: str
    description: str
    is_inactive: bool
    agent_version: str
    is_disabled: bool
    status: StatusMessage
    source_contexts: _containers.RepeatedCompositeFieldContainer[_source_context_pb2.SourceContext]
    ext_source_contexts: _containers.RepeatedCompositeFieldContainer[_source_context_pb2.ExtendedSourceContext]
    labels: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., project: _Optional[str]=..., uniquifier: _Optional[str]=..., description: _Optional[str]=..., is_inactive: bool=..., agent_version: _Optional[str]=..., is_disabled: bool=..., status: _Optional[_Union[StatusMessage, _Mapping]]=..., source_contexts: _Optional[_Iterable[_Union[_source_context_pb2.SourceContext, _Mapping]]]=..., ext_source_contexts: _Optional[_Iterable[_Union[_source_context_pb2.ExtendedSourceContext, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...