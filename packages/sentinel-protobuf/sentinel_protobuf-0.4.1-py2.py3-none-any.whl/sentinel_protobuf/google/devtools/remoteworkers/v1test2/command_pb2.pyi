from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CommandTask(_message.Message):
    __slots__ = ('inputs', 'expected_outputs', 'timeouts')

    class Inputs(_message.Message):
        __slots__ = ('arguments', 'files', 'inline_blobs', 'environment_variables', 'working_directory')

        class EnvironmentVariable(_message.Message):
            __slots__ = ('name', 'value')
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str

            def __init__(self, name: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        INLINE_BLOBS_FIELD_NUMBER: _ClassVar[int]
        ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
        WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        arguments: _containers.RepeatedScalarFieldContainer[str]
        files: _containers.RepeatedCompositeFieldContainer[Digest]
        inline_blobs: _containers.RepeatedCompositeFieldContainer[Blob]
        environment_variables: _containers.RepeatedCompositeFieldContainer[CommandTask.Inputs.EnvironmentVariable]
        working_directory: str

        def __init__(self, arguments: _Optional[_Iterable[str]]=..., files: _Optional[_Iterable[_Union[Digest, _Mapping]]]=..., inline_blobs: _Optional[_Iterable[_Union[Blob, _Mapping]]]=..., environment_variables: _Optional[_Iterable[_Union[CommandTask.Inputs.EnvironmentVariable, _Mapping]]]=..., working_directory: _Optional[str]=...) -> None:
            ...

    class Outputs(_message.Message):
        __slots__ = ('files', 'directories', 'stdout_destination', 'stderr_destination')
        FILES_FIELD_NUMBER: _ClassVar[int]
        DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
        STDOUT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        STDERR_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        files: _containers.RepeatedScalarFieldContainer[str]
        directories: _containers.RepeatedScalarFieldContainer[str]
        stdout_destination: str
        stderr_destination: str

        def __init__(self, files: _Optional[_Iterable[str]]=..., directories: _Optional[_Iterable[str]]=..., stdout_destination: _Optional[str]=..., stderr_destination: _Optional[str]=...) -> None:
            ...

    class Timeouts(_message.Message):
        __slots__ = ('execution', 'idle', 'shutdown')
        EXECUTION_FIELD_NUMBER: _ClassVar[int]
        IDLE_FIELD_NUMBER: _ClassVar[int]
        SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
        execution: _duration_pb2.Duration
        idle: _duration_pb2.Duration
        shutdown: _duration_pb2.Duration

        def __init__(self, execution: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., idle: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., shutdown: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: CommandTask.Inputs
    expected_outputs: CommandTask.Outputs
    timeouts: CommandTask.Timeouts

    def __init__(self, inputs: _Optional[_Union[CommandTask.Inputs, _Mapping]]=..., expected_outputs: _Optional[_Union[CommandTask.Outputs, _Mapping]]=..., timeouts: _Optional[_Union[CommandTask.Timeouts, _Mapping]]=...) -> None:
        ...

class CommandOutputs(_message.Message):
    __slots__ = ('exit_code', 'outputs')
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    exit_code: int
    outputs: Digest

    def __init__(self, exit_code: _Optional[int]=..., outputs: _Optional[_Union[Digest, _Mapping]]=...) -> None:
        ...

class CommandOverhead(_message.Message):
    __slots__ = ('duration', 'overhead')
    DURATION_FIELD_NUMBER: _ClassVar[int]
    OVERHEAD_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    overhead: _duration_pb2.Duration

    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., overhead: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class CommandResult(_message.Message):
    __slots__ = ('status', 'exit_code', 'outputs', 'duration', 'overhead', 'metadata')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    OVERHEAD_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    exit_code: int
    outputs: Digest
    duration: _duration_pb2.Duration
    overhead: _duration_pb2.Duration
    metadata: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., exit_code: _Optional[int]=..., outputs: _Optional[_Union[Digest, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., overhead: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., metadata: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]]=...) -> None:
        ...

class FileMetadata(_message.Message):
    __slots__ = ('path', 'digest', 'contents', 'is_executable')
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    IS_EXECUTABLE_FIELD_NUMBER: _ClassVar[int]
    path: str
    digest: Digest
    contents: bytes
    is_executable: bool

    def __init__(self, path: _Optional[str]=..., digest: _Optional[_Union[Digest, _Mapping]]=..., contents: _Optional[bytes]=..., is_executable: bool=...) -> None:
        ...

class DirectoryMetadata(_message.Message):
    __slots__ = ('path', 'digest')
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    path: str
    digest: Digest

    def __init__(self, path: _Optional[str]=..., digest: _Optional[_Union[Digest, _Mapping]]=...) -> None:
        ...

class Digest(_message.Message):
    __slots__ = ('hash', 'size_bytes')
    HASH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    hash: str
    size_bytes: int

    def __init__(self, hash: _Optional[str]=..., size_bytes: _Optional[int]=...) -> None:
        ...

class Blob(_message.Message):
    __slots__ = ('digest', 'contents')
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    digest: Digest
    contents: bytes

    def __init__(self, digest: _Optional[_Union[Digest, _Mapping]]=..., contents: _Optional[bytes]=...) -> None:
        ...

class Directory(_message.Message):
    __slots__ = ('files', 'directories')
    FILES_FIELD_NUMBER: _ClassVar[int]
    DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[FileMetadata]
    directories: _containers.RepeatedCompositeFieldContainer[DirectoryMetadata]

    def __init__(self, files: _Optional[_Iterable[_Union[FileMetadata, _Mapping]]]=..., directories: _Optional[_Iterable[_Union[DirectoryMetadata, _Mapping]]]=...) -> None:
        ...