from google.api import annotations_pb2 as _annotations_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_TYPE_UNSPECIFIED: _ClassVar[OperationType]
    EXPORT_ENTITIES: _ClassVar[OperationType]
    IMPORT_ENTITIES: _ClassVar[OperationType]
OPERATION_TYPE_UNSPECIFIED: OperationType
EXPORT_ENTITIES: OperationType
IMPORT_ENTITIES: OperationType

class CommonMetadata(_message.Message):
    __slots__ = ('start_time', 'end_time', 'operation_type', 'labels', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CommonMetadata.State]
        INITIALIZING: _ClassVar[CommonMetadata.State]
        PROCESSING: _ClassVar[CommonMetadata.State]
        CANCELLING: _ClassVar[CommonMetadata.State]
        FINALIZING: _ClassVar[CommonMetadata.State]
        SUCCESSFUL: _ClassVar[CommonMetadata.State]
        FAILED: _ClassVar[CommonMetadata.State]
        CANCELLED: _ClassVar[CommonMetadata.State]
    STATE_UNSPECIFIED: CommonMetadata.State
    INITIALIZING: CommonMetadata.State
    PROCESSING: CommonMetadata.State
    CANCELLING: CommonMetadata.State
    FINALIZING: CommonMetadata.State
    SUCCESSFUL: CommonMetadata.State
    FAILED: CommonMetadata.State
    CANCELLED: CommonMetadata.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    operation_type: OperationType
    labels: _containers.ScalarMap[str, str]
    state: CommonMetadata.State

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operation_type: _Optional[_Union[OperationType, str]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[CommonMetadata.State, str]]=...) -> None:
        ...

class Progress(_message.Message):
    __slots__ = ('work_completed', 'work_estimated')
    WORK_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    WORK_ESTIMATED_FIELD_NUMBER: _ClassVar[int]
    work_completed: int
    work_estimated: int

    def __init__(self, work_completed: _Optional[int]=..., work_estimated: _Optional[int]=...) -> None:
        ...

class ExportEntitiesRequest(_message.Message):
    __slots__ = ('project_id', 'labels', 'entity_filter', 'output_url_prefix')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    labels: _containers.ScalarMap[str, str]
    entity_filter: EntityFilter
    output_url_prefix: str

    def __init__(self, project_id: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., entity_filter: _Optional[_Union[EntityFilter, _Mapping]]=..., output_url_prefix: _Optional[str]=...) -> None:
        ...

class ImportEntitiesRequest(_message.Message):
    __slots__ = ('project_id', 'labels', 'input_url', 'entity_filter')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    labels: _containers.ScalarMap[str, str]
    input_url: str
    entity_filter: EntityFilter

    def __init__(self, project_id: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., input_url: _Optional[str]=..., entity_filter: _Optional[_Union[EntityFilter, _Mapping]]=...) -> None:
        ...

class ExportEntitiesResponse(_message.Message):
    __slots__ = ('output_url',)
    OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
    output_url: str

    def __init__(self, output_url: _Optional[str]=...) -> None:
        ...

class ExportEntitiesMetadata(_message.Message):
    __slots__ = ('common', 'progress_entities', 'progress_bytes', 'entity_filter', 'output_url_prefix')
    COMMON_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    common: CommonMetadata
    progress_entities: Progress
    progress_bytes: Progress
    entity_filter: EntityFilter
    output_url_prefix: str

    def __init__(self, common: _Optional[_Union[CommonMetadata, _Mapping]]=..., progress_entities: _Optional[_Union[Progress, _Mapping]]=..., progress_bytes: _Optional[_Union[Progress, _Mapping]]=..., entity_filter: _Optional[_Union[EntityFilter, _Mapping]]=..., output_url_prefix: _Optional[str]=...) -> None:
        ...

class ImportEntitiesMetadata(_message.Message):
    __slots__ = ('common', 'progress_entities', 'progress_bytes', 'entity_filter', 'input_url')
    COMMON_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    common: CommonMetadata
    progress_entities: Progress
    progress_bytes: Progress
    entity_filter: EntityFilter
    input_url: str

    def __init__(self, common: _Optional[_Union[CommonMetadata, _Mapping]]=..., progress_entities: _Optional[_Union[Progress, _Mapping]]=..., progress_bytes: _Optional[_Union[Progress, _Mapping]]=..., entity_filter: _Optional[_Union[EntityFilter, _Mapping]]=..., input_url: _Optional[str]=...) -> None:
        ...

class EntityFilter(_message.Message):
    __slots__ = ('kinds', 'namespace_ids')
    KINDS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_IDS_FIELD_NUMBER: _ClassVar[int]
    kinds: _containers.RepeatedScalarFieldContainer[str]
    namespace_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, kinds: _Optional[_Iterable[str]]=..., namespace_ids: _Optional[_Iterable[str]]=...) -> None:
        ...