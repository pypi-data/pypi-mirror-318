from google.cloud.securitycenter.v1 import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Process(_message.Message):
    __slots__ = ('name', 'binary', 'libraries', 'script', 'args', 'arguments_truncated', 'env_variables', 'env_variables_truncated', 'pid', 'parent_pid')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BINARY_FIELD_NUMBER: _ClassVar[int]
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    ENV_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    ENV_VARIABLES_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PARENT_PID_FIELD_NUMBER: _ClassVar[int]
    name: str
    binary: _file_pb2.File
    libraries: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    script: _file_pb2.File
    args: _containers.RepeatedScalarFieldContainer[str]
    arguments_truncated: bool
    env_variables: _containers.RepeatedCompositeFieldContainer[EnvironmentVariable]
    env_variables_truncated: bool
    pid: int
    parent_pid: int

    def __init__(self, name: _Optional[str]=..., binary: _Optional[_Union[_file_pb2.File, _Mapping]]=..., libraries: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., script: _Optional[_Union[_file_pb2.File, _Mapping]]=..., args: _Optional[_Iterable[str]]=..., arguments_truncated: bool=..., env_variables: _Optional[_Iterable[_Union[EnvironmentVariable, _Mapping]]]=..., env_variables_truncated: bool=..., pid: _Optional[int]=..., parent_pid: _Optional[int]=...) -> None:
        ...

class EnvironmentVariable(_message.Message):
    __slots__ = ('name', 'val')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    val: str

    def __init__(self, name: _Optional[str]=..., val: _Optional[str]=...) -> None:
        ...