from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RunMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_MODE_UNSPECIFIED: _ClassVar[RunMode]
    LIVE: _ClassVar[RunMode]
    SUBMISSION: _ClassVar[RunMode]
RUN_MODE_UNSPECIFIED: RunMode
LIVE: RunMode
SUBMISSION: RunMode

class OperatorDefinition(_message.Message):
    __slots__ = ('operator', 'input_args', 'output_args', 'attributes', 'resources', 'short_description', 'description')

    class ArgumentDefinition(_message.Message):
        __slots__ = ('argument', 'type')
        ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        argument: str
        type: str

        def __init__(self, argument: _Optional[str]=..., type: _Optional[str]=...) -> None:
            ...

    class AttributeDefinition(_message.Message):
        __slots__ = ('attribute', 'type', 'default_value')
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        attribute: str
        type: str
        default_value: AttributeValue

        def __init__(self, attribute: _Optional[str]=..., type: _Optional[str]=..., default_value: _Optional[_Union[AttributeValue, _Mapping]]=...) -> None:
            ...
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    INPUT_ARGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ARGS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    operator: str
    input_args: _containers.RepeatedCompositeFieldContainer[OperatorDefinition.ArgumentDefinition]
    output_args: _containers.RepeatedCompositeFieldContainer[OperatorDefinition.ArgumentDefinition]
    attributes: _containers.RepeatedCompositeFieldContainer[OperatorDefinition.AttributeDefinition]
    resources: ResourceSpecification
    short_description: str
    description: str

    def __init__(self, operator: _Optional[str]=..., input_args: _Optional[_Iterable[_Union[OperatorDefinition.ArgumentDefinition, _Mapping]]]=..., output_args: _Optional[_Iterable[_Union[OperatorDefinition.ArgumentDefinition, _Mapping]]]=..., attributes: _Optional[_Iterable[_Union[OperatorDefinition.AttributeDefinition, _Mapping]]]=..., resources: _Optional[_Union[ResourceSpecification, _Mapping]]=..., short_description: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class ResourceSpecification(_message.Message):
    __slots__ = ('cpu', 'cpu_limits', 'memory', 'memory_limits', 'gpus', 'latency_budget_ms')
    CPU_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMITS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMITS_FIELD_NUMBER: _ClassVar[int]
    GPUS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_BUDGET_MS_FIELD_NUMBER: _ClassVar[int]
    cpu: str
    cpu_limits: str
    memory: str
    memory_limits: str
    gpus: int
    latency_budget_ms: int

    def __init__(self, cpu: _Optional[str]=..., cpu_limits: _Optional[str]=..., memory: _Optional[str]=..., memory_limits: _Optional[str]=..., gpus: _Optional[int]=..., latency_budget_ms: _Optional[int]=...) -> None:
        ...

class AttributeValue(_message.Message):
    __slots__ = ('i', 'f', 'b', 's')
    I_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    i: int
    f: float
    b: bool
    s: bytes

    def __init__(self, i: _Optional[int]=..., f: _Optional[float]=..., b: bool=..., s: _Optional[bytes]=...) -> None:
        ...

class AnalyzerDefinition(_message.Message):
    __slots__ = ('analyzer', 'operator', 'inputs', 'attrs', 'debug_options', 'operator_option')

    class StreamInput(_message.Message):
        __slots__ = ('input',)
        INPUT_FIELD_NUMBER: _ClassVar[int]
        input: str

        def __init__(self, input: _Optional[str]=...) -> None:
            ...

    class DebugOptions(_message.Message):
        __slots__ = ('environment_variables',)

        class EnvironmentVariablesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
        environment_variables: _containers.ScalarMap[str, str]

        def __init__(self, environment_variables: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class OperatorOption(_message.Message):
        __slots__ = ('tag', 'registry')
        TAG_FIELD_NUMBER: _ClassVar[int]
        REGISTRY_FIELD_NUMBER: _ClassVar[int]
        tag: str
        registry: str

        def __init__(self, tag: _Optional[str]=..., registry: _Optional[str]=...) -> None:
            ...

    class AttrsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValue, _Mapping]]=...) -> None:
            ...
    ANALYZER_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_OPTION_FIELD_NUMBER: _ClassVar[int]
    analyzer: str
    operator: str
    inputs: _containers.RepeatedCompositeFieldContainer[AnalyzerDefinition.StreamInput]
    attrs: _containers.MessageMap[str, AttributeValue]
    debug_options: AnalyzerDefinition.DebugOptions
    operator_option: AnalyzerDefinition.OperatorOption

    def __init__(self, analyzer: _Optional[str]=..., operator: _Optional[str]=..., inputs: _Optional[_Iterable[_Union[AnalyzerDefinition.StreamInput, _Mapping]]]=..., attrs: _Optional[_Mapping[str, AttributeValue]]=..., debug_options: _Optional[_Union[AnalyzerDefinition.DebugOptions, _Mapping]]=..., operator_option: _Optional[_Union[AnalyzerDefinition.OperatorOption, _Mapping]]=...) -> None:
        ...

class AnalysisDefinition(_message.Message):
    __slots__ = ('analyzers',)
    ANALYZERS_FIELD_NUMBER: _ClassVar[int]
    analyzers: _containers.RepeatedCompositeFieldContainer[AnalyzerDefinition]

    def __init__(self, analyzers: _Optional[_Iterable[_Union[AnalyzerDefinition, _Mapping]]]=...) -> None:
        ...

class RunStatus(_message.Message):
    __slots__ = ('state', 'reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RunStatus.State]
        INITIALIZING: _ClassVar[RunStatus.State]
        RUNNING: _ClassVar[RunStatus.State]
        COMPLETED: _ClassVar[RunStatus.State]
        FAILED: _ClassVar[RunStatus.State]
        PENDING: _ClassVar[RunStatus.State]
    STATE_UNSPECIFIED: RunStatus.State
    INITIALIZING: RunStatus.State
    RUNNING: RunStatus.State
    COMPLETED: RunStatus.State
    FAILED: RunStatus.State
    PENDING: RunStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    state: RunStatus.State
    reason: str

    def __init__(self, state: _Optional[_Union[RunStatus.State, str]]=..., reason: _Optional[str]=...) -> None:
        ...