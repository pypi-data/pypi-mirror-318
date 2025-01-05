from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.visionai.v1 import lva_pb2 as _lva_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Operator(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'operator_definition', 'docker_image')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    DOCKER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    operator_definition: _lva_pb2.OperatorDefinition
    docker_image: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., operator_definition: _Optional[_Union[_lva_pb2.OperatorDefinition, _Mapping]]=..., docker_image: _Optional[str]=...) -> None:
        ...

class Analysis(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'analysis_definition', 'input_streams_mapping', 'output_streams_mapping', 'disable_event_watch')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class InputStreamsMappingEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class OutputStreamsMappingEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    INPUT_STREAMS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STREAMS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EVENT_WATCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    analysis_definition: _lva_pb2.AnalysisDefinition
    input_streams_mapping: _containers.ScalarMap[str, str]
    output_streams_mapping: _containers.ScalarMap[str, str]
    disable_event_watch: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., analysis_definition: _Optional[_Union[_lva_pb2.AnalysisDefinition, _Mapping]]=..., input_streams_mapping: _Optional[_Mapping[str, str]]=..., output_streams_mapping: _Optional[_Mapping[str, str]]=..., disable_event_watch: bool=...) -> None:
        ...

class Process(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'analysis', 'attribute_overrides', 'run_status', 'run_mode', 'event_id', 'batch_id', 'retry_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
    RUN_MODE_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    analysis: str
    attribute_overrides: _containers.RepeatedScalarFieldContainer[str]
    run_status: _lva_pb2.RunStatus
    run_mode: _lva_pb2.RunMode
    event_id: str
    batch_id: str
    retry_count: int

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., analysis: _Optional[str]=..., attribute_overrides: _Optional[_Iterable[str]]=..., run_status: _Optional[_Union[_lva_pb2.RunStatus, _Mapping]]=..., run_mode: _Optional[_Union[_lva_pb2.RunMode, str]]=..., event_id: _Optional[str]=..., batch_id: _Optional[str]=..., retry_count: _Optional[int]=...) -> None:
        ...