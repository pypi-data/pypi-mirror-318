
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FlagOptions(_message.Message):
    __slots__ = ['default_value', 'deprecated', 'hidden', 'name', 'no_opt_default_value', 'shorthand', 'shorthand_deprecated', 'usage']
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_OPT_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHORTHAND_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    SHORTHAND_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    default_value: str
    deprecated: str
    hidden: bool
    name: str
    no_opt_default_value: str
    shorthand: str
    shorthand_deprecated: str
    usage: str

    def __init__(self, name: _Optional[str]=..., shorthand: _Optional[str]=..., usage: _Optional[str]=..., default_value: _Optional[str]=..., no_opt_default_value: _Optional[str]=..., deprecated: _Optional[str]=..., shorthand_deprecated: _Optional[str]=..., hidden: bool=...) -> None:
        ...

class ModuleOptions(_message.Message):
    __slots__ = ['query', 'tx']
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    query: ServiceCommandDescriptor
    tx: ServiceCommandDescriptor

    def __init__(self, tx: _Optional[_Union[(ServiceCommandDescriptor, _Mapping)]]=..., query: _Optional[_Union[(ServiceCommandDescriptor, _Mapping)]]=...) -> None:
        ...

class PositionalArgDescriptor(_message.Message):
    __slots__ = ['proto_field', 'varargs']
    PROTO_FIELD_FIELD_NUMBER: _ClassVar[int]
    VARARGS_FIELD_NUMBER: _ClassVar[int]
    proto_field: str
    varargs: bool

    def __init__(self, proto_field: _Optional[str]=..., varargs: bool=...) -> None:
        ...

class RpcCommandOptions(_message.Message):
    __slots__ = ['alias', 'deprecated', 'example', 'flag_options', 'long', 'positional_args', 'rpc_method', 'short', 'skip', 'suggest_for', 'use', 'version']

    class FlagOptionsEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FlagOptions

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[(FlagOptions, _Mapping)]]=...) -> None:
            ...
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    FLAG_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_ARGS_FIELD_NUMBER: _ClassVar[int]
    RPC_METHOD_FIELD_NUMBER: _ClassVar[int]
    SHORT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_FOR_FIELD_NUMBER: _ClassVar[int]
    USE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    alias: _containers.RepeatedScalarFieldContainer[str]
    deprecated: str
    example: str
    flag_options: _containers.MessageMap[(str, FlagOptions)]
    long: str
    positional_args: _containers.RepeatedCompositeFieldContainer[PositionalArgDescriptor]
    rpc_method: str
    short: str
    skip: bool
    suggest_for: _containers.RepeatedScalarFieldContainer[str]
    use: str
    version: str

    def __init__(self, rpc_method: _Optional[str]=..., use: _Optional[str]=..., long: _Optional[str]=..., short: _Optional[str]=..., example: _Optional[str]=..., alias: _Optional[_Iterable[str]]=..., suggest_for: _Optional[_Iterable[str]]=..., deprecated: _Optional[str]=..., version: _Optional[str]=..., flag_options: _Optional[_Mapping[(str, FlagOptions)]]=..., positional_args: _Optional[_Iterable[_Union[(PositionalArgDescriptor, _Mapping)]]]=..., skip: bool=...) -> None:
        ...

class ServiceCommandDescriptor(_message.Message):
    __slots__ = ['rpc_command_options', 'service', 'sub_commands']

    class SubCommandsEntry(_message.Message):
        __slots__ = ['key', 'value']
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ServiceCommandDescriptor

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[(ServiceCommandDescriptor, _Mapping)]]=...) -> None:
            ...
    RPC_COMMAND_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SUB_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    rpc_command_options: _containers.RepeatedCompositeFieldContainer[RpcCommandOptions]
    service: str
    sub_commands: _containers.MessageMap[(str, ServiceCommandDescriptor)]

    def __init__(self, service: _Optional[str]=..., rpc_command_options: _Optional[_Iterable[_Union[(RpcCommandOptions, _Mapping)]]]=..., sub_commands: _Optional[_Mapping[(str, ServiceCommandDescriptor)]]=...) -> None:
        ...
