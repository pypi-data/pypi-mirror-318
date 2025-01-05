from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.migration.v2 import migration_error_details_pb2 as _migration_error_details_pb2
from google.cloud.bigquery.migration.v2 import migration_metrics_pb2 as _migration_metrics_pb2
from google.cloud.bigquery.migration.v2 import translation_config_pb2 as _translation_config_pb2
from google.cloud.bigquery.migration.v2 import translation_details_pb2 as _translation_details_pb2
from google.cloud.bigquery.migration.v2 import translation_usability_pb2 as _translation_usability_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import error_details_pb2 as _error_details_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MigrationWorkflow(_message.Message):
    __slots__ = ('name', 'display_name', 'tasks', 'state', 'create_time', 'last_update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MigrationWorkflow.State]
        DRAFT: _ClassVar[MigrationWorkflow.State]
        RUNNING: _ClassVar[MigrationWorkflow.State]
        PAUSED: _ClassVar[MigrationWorkflow.State]
        COMPLETED: _ClassVar[MigrationWorkflow.State]
    STATE_UNSPECIFIED: MigrationWorkflow.State
    DRAFT: MigrationWorkflow.State
    RUNNING: MigrationWorkflow.State
    PAUSED: MigrationWorkflow.State
    COMPLETED: MigrationWorkflow.State

    class TasksEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MigrationTask

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[MigrationTask, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    tasks: _containers.MessageMap[str, MigrationTask]
    state: MigrationWorkflow.State
    create_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., tasks: _Optional[_Mapping[str, MigrationTask]]=..., state: _Optional[_Union[MigrationWorkflow.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class MigrationTask(_message.Message):
    __slots__ = ('translation_config_details', 'translation_details', 'id', 'type', 'state', 'processing_error', 'create_time', 'last_update_time', 'resource_error_details', 'resource_error_count', 'metrics', 'task_result', 'total_processing_error_count', 'total_resource_error_count')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MigrationTask.State]
        PENDING: _ClassVar[MigrationTask.State]
        ORCHESTRATING: _ClassVar[MigrationTask.State]
        RUNNING: _ClassVar[MigrationTask.State]
        PAUSED: _ClassVar[MigrationTask.State]
        SUCCEEDED: _ClassVar[MigrationTask.State]
        FAILED: _ClassVar[MigrationTask.State]
    STATE_UNSPECIFIED: MigrationTask.State
    PENDING: MigrationTask.State
    ORCHESTRATING: MigrationTask.State
    RUNNING: MigrationTask.State
    PAUSED: MigrationTask.State
    SUCCEEDED: MigrationTask.State
    FAILED: MigrationTask.State
    TRANSLATION_CONFIG_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROCESSING_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESOURCE_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    translation_config_details: _translation_config_pb2.TranslationConfigDetails
    translation_details: _translation_details_pb2.TranslationDetails
    id: str
    type: str
    state: MigrationTask.State
    processing_error: _error_details_pb2.ErrorInfo
    create_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    resource_error_details: _containers.RepeatedCompositeFieldContainer[_migration_error_details_pb2.ResourceErrorDetail]
    resource_error_count: int
    metrics: _containers.RepeatedCompositeFieldContainer[_migration_metrics_pb2.TimeSeries]
    task_result: MigrationTaskResult
    total_processing_error_count: int
    total_resource_error_count: int

    def __init__(self, translation_config_details: _Optional[_Union[_translation_config_pb2.TranslationConfigDetails, _Mapping]]=..., translation_details: _Optional[_Union[_translation_details_pb2.TranslationDetails, _Mapping]]=..., id: _Optional[str]=..., type: _Optional[str]=..., state: _Optional[_Union[MigrationTask.State, str]]=..., processing_error: _Optional[_Union[_error_details_pb2.ErrorInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., resource_error_details: _Optional[_Iterable[_Union[_migration_error_details_pb2.ResourceErrorDetail, _Mapping]]]=..., resource_error_count: _Optional[int]=..., metrics: _Optional[_Iterable[_Union[_migration_metrics_pb2.TimeSeries, _Mapping]]]=..., task_result: _Optional[_Union[MigrationTaskResult, _Mapping]]=..., total_processing_error_count: _Optional[int]=..., total_resource_error_count: _Optional[int]=...) -> None:
        ...

class MigrationSubtask(_message.Message):
    __slots__ = ('name', 'task_id', 'type', 'state', 'processing_error', 'resource_error_details', 'resource_error_count', 'create_time', 'last_update_time', 'metrics')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MigrationSubtask.State]
        ACTIVE: _ClassVar[MigrationSubtask.State]
        RUNNING: _ClassVar[MigrationSubtask.State]
        SUCCEEDED: _ClassVar[MigrationSubtask.State]
        FAILED: _ClassVar[MigrationSubtask.State]
        PAUSED: _ClassVar[MigrationSubtask.State]
        PENDING_DEPENDENCY: _ClassVar[MigrationSubtask.State]
    STATE_UNSPECIFIED: MigrationSubtask.State
    ACTIVE: MigrationSubtask.State
    RUNNING: MigrationSubtask.State
    SUCCEEDED: MigrationSubtask.State
    FAILED: MigrationSubtask.State
    PAUSED: MigrationSubtask.State
    PENDING_DEPENDENCY: MigrationSubtask.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    task_id: str
    type: str
    state: MigrationSubtask.State
    processing_error: _error_details_pb2.ErrorInfo
    resource_error_details: _containers.RepeatedCompositeFieldContainer[_migration_error_details_pb2.ResourceErrorDetail]
    resource_error_count: int
    create_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp
    metrics: _containers.RepeatedCompositeFieldContainer[_migration_metrics_pb2.TimeSeries]

    def __init__(self, name: _Optional[str]=..., task_id: _Optional[str]=..., type: _Optional[str]=..., state: _Optional[_Union[MigrationSubtask.State, str]]=..., processing_error: _Optional[_Union[_error_details_pb2.ErrorInfo, _Mapping]]=..., resource_error_details: _Optional[_Iterable[_Union[_migration_error_details_pb2.ResourceErrorDetail, _Mapping]]]=..., resource_error_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., metrics: _Optional[_Iterable[_Union[_migration_metrics_pb2.TimeSeries, _Mapping]]]=...) -> None:
        ...

class MigrationTaskResult(_message.Message):
    __slots__ = ('translation_task_result',)
    TRANSLATION_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    translation_task_result: TranslationTaskResult

    def __init__(self, translation_task_result: _Optional[_Union[TranslationTaskResult, _Mapping]]=...) -> None:
        ...

class TranslationTaskResult(_message.Message):
    __slots__ = ('translated_literals', 'report_log_messages')
    TRANSLATED_LITERALS_FIELD_NUMBER: _ClassVar[int]
    REPORT_LOG_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    translated_literals: _containers.RepeatedCompositeFieldContainer[_translation_details_pb2.Literal]
    report_log_messages: _containers.RepeatedCompositeFieldContainer[_translation_usability_pb2.GcsReportLogMessage]

    def __init__(self, translated_literals: _Optional[_Iterable[_Union[_translation_details_pb2.Literal, _Mapping]]]=..., report_log_messages: _Optional[_Iterable[_Union[_translation_usability_pb2.GcsReportLogMessage, _Mapping]]]=...) -> None:
        ...