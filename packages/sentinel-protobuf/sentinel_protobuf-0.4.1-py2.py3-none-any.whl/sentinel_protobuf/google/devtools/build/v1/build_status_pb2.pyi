from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BuildStatus(_message.Message):
    __slots__ = ('result', 'final_invocation_id', 'build_tool_exit_code', 'error_message', 'details')

    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[BuildStatus.Result]
        COMMAND_SUCCEEDED: _ClassVar[BuildStatus.Result]
        COMMAND_FAILED: _ClassVar[BuildStatus.Result]
        USER_ERROR: _ClassVar[BuildStatus.Result]
        SYSTEM_ERROR: _ClassVar[BuildStatus.Result]
        RESOURCE_EXHAUSTED: _ClassVar[BuildStatus.Result]
        INVOCATION_DEADLINE_EXCEEDED: _ClassVar[BuildStatus.Result]
        REQUEST_DEADLINE_EXCEEDED: _ClassVar[BuildStatus.Result]
        CANCELLED: _ClassVar[BuildStatus.Result]
    UNKNOWN_STATUS: BuildStatus.Result
    COMMAND_SUCCEEDED: BuildStatus.Result
    COMMAND_FAILED: BuildStatus.Result
    USER_ERROR: BuildStatus.Result
    SYSTEM_ERROR: BuildStatus.Result
    RESOURCE_EXHAUSTED: BuildStatus.Result
    INVOCATION_DEADLINE_EXCEEDED: BuildStatus.Result
    REQUEST_DEADLINE_EXCEEDED: BuildStatus.Result
    CANCELLED: BuildStatus.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    FINAL_INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUILD_TOOL_EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    result: BuildStatus.Result
    final_invocation_id: str
    build_tool_exit_code: _wrappers_pb2.Int32Value
    error_message: str
    details: _any_pb2.Any

    def __init__(self, result: _Optional[_Union[BuildStatus.Result, str]]=..., final_invocation_id: _Optional[str]=..., build_tool_exit_code: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., error_message: _Optional[str]=..., details: _Optional[_Union[_any_pb2.Any, _Mapping]]=...) -> None:
        ...