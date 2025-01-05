from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoggingConfig(_message.Message):
    __slots__ = ('driver_log_levels',)

    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEVEL_UNSPECIFIED: _ClassVar[LoggingConfig.Level]
        ALL: _ClassVar[LoggingConfig.Level]
        TRACE: _ClassVar[LoggingConfig.Level]
        DEBUG: _ClassVar[LoggingConfig.Level]
        INFO: _ClassVar[LoggingConfig.Level]
        WARN: _ClassVar[LoggingConfig.Level]
        ERROR: _ClassVar[LoggingConfig.Level]
        FATAL: _ClassVar[LoggingConfig.Level]
        OFF: _ClassVar[LoggingConfig.Level]
    LEVEL_UNSPECIFIED: LoggingConfig.Level
    ALL: LoggingConfig.Level
    TRACE: LoggingConfig.Level
    DEBUG: LoggingConfig.Level
    INFO: LoggingConfig.Level
    WARN: LoggingConfig.Level
    ERROR: LoggingConfig.Level
    FATAL: LoggingConfig.Level
    OFF: LoggingConfig.Level

    class DriverLogLevelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: LoggingConfig.Level

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[LoggingConfig.Level, str]]=...) -> None:
            ...
    DRIVER_LOG_LEVELS_FIELD_NUMBER: _ClassVar[int]
    driver_log_levels: _containers.ScalarMap[str, LoggingConfig.Level]

    def __init__(self, driver_log_levels: _Optional[_Mapping[str, LoggingConfig.Level]]=...) -> None:
        ...

class HadoopJob(_message.Message):
    __slots__ = ('main_jar_file_uri', 'main_class', 'args', 'jar_file_uris', 'file_uris', 'archive_uris', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MAIN_JAR_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    main_jar_file_uri: str
    main_class: str
    args: _containers.RepeatedScalarFieldContainer[str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, main_jar_file_uri: _Optional[str]=..., main_class: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class SparkJob(_message.Message):
    __slots__ = ('main_jar_file_uri', 'main_class', 'args', 'jar_file_uris', 'file_uris', 'archive_uris', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MAIN_JAR_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    main_jar_file_uri: str
    main_class: str
    args: _containers.RepeatedScalarFieldContainer[str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, main_jar_file_uri: _Optional[str]=..., main_class: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class PySparkJob(_message.Message):
    __slots__ = ('main_python_file_uri', 'args', 'python_file_uris', 'jar_file_uris', 'file_uris', 'archive_uris', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MAIN_PYTHON_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    PYTHON_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    main_python_file_uri: str
    args: _containers.RepeatedScalarFieldContainer[str]
    python_file_uris: _containers.RepeatedScalarFieldContainer[str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, main_python_file_uri: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., python_file_uris: _Optional[_Iterable[str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class QueryList(_message.Message):
    __slots__ = ('queries',)
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    queries: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, queries: _Optional[_Iterable[str]]=...) -> None:
        ...

class HiveJob(_message.Message):
    __slots__ = ('query_file_uri', 'query_list', 'continue_on_failure', 'script_variables', 'properties', 'jar_file_uris')

    class ScriptVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    query_file_uri: str
    query_list: QueryList
    continue_on_failure: bool
    script_variables: _containers.ScalarMap[str, str]
    properties: _containers.ScalarMap[str, str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, query_file_uri: _Optional[str]=..., query_list: _Optional[_Union[QueryList, _Mapping]]=..., continue_on_failure: bool=..., script_variables: _Optional[_Mapping[str, str]]=..., properties: _Optional[_Mapping[str, str]]=..., jar_file_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class SparkSqlJob(_message.Message):
    __slots__ = ('query_file_uri', 'query_list', 'script_variables', 'properties', 'jar_file_uris', 'logging_config')

    class ScriptVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    query_file_uri: str
    query_list: QueryList
    script_variables: _containers.ScalarMap[str, str]
    properties: _containers.ScalarMap[str, str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    logging_config: LoggingConfig

    def __init__(self, query_file_uri: _Optional[str]=..., query_list: _Optional[_Union[QueryList, _Mapping]]=..., script_variables: _Optional[_Mapping[str, str]]=..., properties: _Optional[_Mapping[str, str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class PigJob(_message.Message):
    __slots__ = ('query_file_uri', 'query_list', 'continue_on_failure', 'script_variables', 'properties', 'jar_file_uris', 'logging_config')

    class ScriptVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    query_file_uri: str
    query_list: QueryList
    continue_on_failure: bool
    script_variables: _containers.ScalarMap[str, str]
    properties: _containers.ScalarMap[str, str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    logging_config: LoggingConfig

    def __init__(self, query_file_uri: _Optional[str]=..., query_list: _Optional[_Union[QueryList, _Mapping]]=..., continue_on_failure: bool=..., script_variables: _Optional[_Mapping[str, str]]=..., properties: _Optional[_Mapping[str, str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class SparkRJob(_message.Message):
    __slots__ = ('main_r_file_uri', 'args', 'file_uris', 'archive_uris', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MAIN_R_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_URIS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    main_r_file_uri: str
    args: _containers.RepeatedScalarFieldContainer[str]
    file_uris: _containers.RepeatedScalarFieldContainer[str]
    archive_uris: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, main_r_file_uri: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., file_uris: _Optional[_Iterable[str]]=..., archive_uris: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class PrestoJob(_message.Message):
    __slots__ = ('query_file_uri', 'query_list', 'continue_on_failure', 'output_format', 'client_tags', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TAGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    query_file_uri: str
    query_list: QueryList
    continue_on_failure: bool
    output_format: str
    client_tags: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, query_file_uri: _Optional[str]=..., query_list: _Optional[_Union[QueryList, _Mapping]]=..., continue_on_failure: bool=..., output_format: _Optional[str]=..., client_tags: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class TrinoJob(_message.Message):
    __slots__ = ('query_file_uri', 'query_list', 'continue_on_failure', 'output_format', 'client_tags', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TAGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    query_file_uri: str
    query_list: QueryList
    continue_on_failure: bool
    output_format: str
    client_tags: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, query_file_uri: _Optional[str]=..., query_list: _Optional[_Union[QueryList, _Mapping]]=..., continue_on_failure: bool=..., output_format: _Optional[str]=..., client_tags: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class FlinkJob(_message.Message):
    __slots__ = ('main_jar_file_uri', 'main_class', 'args', 'jar_file_uris', 'savepoint_uri', 'properties', 'logging_config')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MAIN_JAR_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    JAR_FILE_URIS_FIELD_NUMBER: _ClassVar[int]
    SAVEPOINT_URI_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    main_jar_file_uri: str
    main_class: str
    args: _containers.RepeatedScalarFieldContainer[str]
    jar_file_uris: _containers.RepeatedScalarFieldContainer[str]
    savepoint_uri: str
    properties: _containers.ScalarMap[str, str]
    logging_config: LoggingConfig

    def __init__(self, main_jar_file_uri: _Optional[str]=..., main_class: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., jar_file_uris: _Optional[_Iterable[str]]=..., savepoint_uri: _Optional[str]=..., properties: _Optional[_Mapping[str, str]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=...) -> None:
        ...

class JobPlacement(_message.Message):
    __slots__ = ('cluster_name', 'cluster_uuid', 'cluster_labels')

    class ClusterLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LABELS_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    cluster_uuid: str
    cluster_labels: _containers.ScalarMap[str, str]

    def __init__(self, cluster_name: _Optional[str]=..., cluster_uuid: _Optional[str]=..., cluster_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class JobStatus(_message.Message):
    __slots__ = ('state', 'details', 'state_start_time', 'substate')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[JobStatus.State]
        PENDING: _ClassVar[JobStatus.State]
        SETUP_DONE: _ClassVar[JobStatus.State]
        RUNNING: _ClassVar[JobStatus.State]
        CANCEL_PENDING: _ClassVar[JobStatus.State]
        CANCEL_STARTED: _ClassVar[JobStatus.State]
        CANCELLED: _ClassVar[JobStatus.State]
        DONE: _ClassVar[JobStatus.State]
        ERROR: _ClassVar[JobStatus.State]
        ATTEMPT_FAILURE: _ClassVar[JobStatus.State]
    STATE_UNSPECIFIED: JobStatus.State
    PENDING: JobStatus.State
    SETUP_DONE: JobStatus.State
    RUNNING: JobStatus.State
    CANCEL_PENDING: JobStatus.State
    CANCEL_STARTED: JobStatus.State
    CANCELLED: JobStatus.State
    DONE: JobStatus.State
    ERROR: JobStatus.State
    ATTEMPT_FAILURE: JobStatus.State

    class Substate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[JobStatus.Substate]
        SUBMITTED: _ClassVar[JobStatus.Substate]
        QUEUED: _ClassVar[JobStatus.Substate]
        STALE_STATUS: _ClassVar[JobStatus.Substate]
    UNSPECIFIED: JobStatus.Substate
    SUBMITTED: JobStatus.Substate
    QUEUED: JobStatus.Substate
    STALE_STATUS: JobStatus.Substate
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBSTATE_FIELD_NUMBER: _ClassVar[int]
    state: JobStatus.State
    details: str
    state_start_time: _timestamp_pb2.Timestamp
    substate: JobStatus.Substate

    def __init__(self, state: _Optional[_Union[JobStatus.State, str]]=..., details: _Optional[str]=..., state_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., substate: _Optional[_Union[JobStatus.Substate, str]]=...) -> None:
        ...

class JobReference(_message.Message):
    __slots__ = ('project_id', 'job_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
        ...

class YarnApplication(_message.Message):
    __slots__ = ('name', 'state', 'progress', 'tracking_url')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[YarnApplication.State]
        NEW: _ClassVar[YarnApplication.State]
        NEW_SAVING: _ClassVar[YarnApplication.State]
        SUBMITTED: _ClassVar[YarnApplication.State]
        ACCEPTED: _ClassVar[YarnApplication.State]
        RUNNING: _ClassVar[YarnApplication.State]
        FINISHED: _ClassVar[YarnApplication.State]
        FAILED: _ClassVar[YarnApplication.State]
        KILLED: _ClassVar[YarnApplication.State]
    STATE_UNSPECIFIED: YarnApplication.State
    NEW: YarnApplication.State
    NEW_SAVING: YarnApplication.State
    SUBMITTED: YarnApplication.State
    ACCEPTED: YarnApplication.State
    RUNNING: YarnApplication.State
    FINISHED: YarnApplication.State
    FAILED: YarnApplication.State
    KILLED: YarnApplication.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: YarnApplication.State
    progress: float
    tracking_url: str

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[YarnApplication.State, str]]=..., progress: _Optional[float]=..., tracking_url: _Optional[str]=...) -> None:
        ...

class Job(_message.Message):
    __slots__ = ('reference', 'placement', 'hadoop_job', 'spark_job', 'pyspark_job', 'hive_job', 'pig_job', 'spark_r_job', 'spark_sql_job', 'presto_job', 'trino_job', 'flink_job', 'status', 'status_history', 'yarn_applications', 'driver_output_resource_uri', 'driver_control_files_uri', 'labels', 'scheduling', 'job_uuid', 'done', 'driver_scheduling_config')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    HADOOP_JOB_FIELD_NUMBER: _ClassVar[int]
    SPARK_JOB_FIELD_NUMBER: _ClassVar[int]
    PYSPARK_JOB_FIELD_NUMBER: _ClassVar[int]
    HIVE_JOB_FIELD_NUMBER: _ClassVar[int]
    PIG_JOB_FIELD_NUMBER: _ClassVar[int]
    SPARK_R_JOB_FIELD_NUMBER: _ClassVar[int]
    SPARK_SQL_JOB_FIELD_NUMBER: _ClassVar[int]
    PRESTO_JOB_FIELD_NUMBER: _ClassVar[int]
    TRINO_JOB_FIELD_NUMBER: _ClassVar[int]
    FLINK_JOB_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    YARN_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    DRIVER_OUTPUT_RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    DRIVER_CONTROL_FILES_URI_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    JOB_UUID_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    DRIVER_SCHEDULING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    reference: JobReference
    placement: JobPlacement
    hadoop_job: HadoopJob
    spark_job: SparkJob
    pyspark_job: PySparkJob
    hive_job: HiveJob
    pig_job: PigJob
    spark_r_job: SparkRJob
    spark_sql_job: SparkSqlJob
    presto_job: PrestoJob
    trino_job: TrinoJob
    flink_job: FlinkJob
    status: JobStatus
    status_history: _containers.RepeatedCompositeFieldContainer[JobStatus]
    yarn_applications: _containers.RepeatedCompositeFieldContainer[YarnApplication]
    driver_output_resource_uri: str
    driver_control_files_uri: str
    labels: _containers.ScalarMap[str, str]
    scheduling: JobScheduling
    job_uuid: str
    done: bool
    driver_scheduling_config: DriverSchedulingConfig

    def __init__(self, reference: _Optional[_Union[JobReference, _Mapping]]=..., placement: _Optional[_Union[JobPlacement, _Mapping]]=..., hadoop_job: _Optional[_Union[HadoopJob, _Mapping]]=..., spark_job: _Optional[_Union[SparkJob, _Mapping]]=..., pyspark_job: _Optional[_Union[PySparkJob, _Mapping]]=..., hive_job: _Optional[_Union[HiveJob, _Mapping]]=..., pig_job: _Optional[_Union[PigJob, _Mapping]]=..., spark_r_job: _Optional[_Union[SparkRJob, _Mapping]]=..., spark_sql_job: _Optional[_Union[SparkSqlJob, _Mapping]]=..., presto_job: _Optional[_Union[PrestoJob, _Mapping]]=..., trino_job: _Optional[_Union[TrinoJob, _Mapping]]=..., flink_job: _Optional[_Union[FlinkJob, _Mapping]]=..., status: _Optional[_Union[JobStatus, _Mapping]]=..., status_history: _Optional[_Iterable[_Union[JobStatus, _Mapping]]]=..., yarn_applications: _Optional[_Iterable[_Union[YarnApplication, _Mapping]]]=..., driver_output_resource_uri: _Optional[str]=..., driver_control_files_uri: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., scheduling: _Optional[_Union[JobScheduling, _Mapping]]=..., job_uuid: _Optional[str]=..., done: bool=..., driver_scheduling_config: _Optional[_Union[DriverSchedulingConfig, _Mapping]]=...) -> None:
        ...

class DriverSchedulingConfig(_message.Message):
    __slots__ = ('memory_mb', 'vcores')
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    VCORES_FIELD_NUMBER: _ClassVar[int]
    memory_mb: int
    vcores: int

    def __init__(self, memory_mb: _Optional[int]=..., vcores: _Optional[int]=...) -> None:
        ...

class JobScheduling(_message.Message):
    __slots__ = ('max_failures_per_hour', 'max_failures_total')
    MAX_FAILURES_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    MAX_FAILURES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    max_failures_per_hour: int
    max_failures_total: int

    def __init__(self, max_failures_per_hour: _Optional[int]=..., max_failures_total: _Optional[int]=...) -> None:
        ...

class SubmitJobRequest(_message.Message):
    __slots__ = ('project_id', 'region', 'job', 'request_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    job: Job
    request_id: str

    def __init__(self, project_id: _Optional[str]=..., region: _Optional[str]=..., job: _Optional[_Union[Job, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class JobMetadata(_message.Message):
    __slots__ = ('job_id', 'status', 'operation_type', 'start_time')
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: JobStatus
    operation_type: str
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, job_id: _Optional[str]=..., status: _Optional[_Union[JobStatus, _Mapping]]=..., operation_type: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetJobRequest(_message.Message):
    __slots__ = ('project_id', 'region', 'job_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    job_id: str

    def __init__(self, project_id: _Optional[str]=..., region: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
        ...

class ListJobsRequest(_message.Message):
    __slots__ = ('project_id', 'region', 'page_size', 'page_token', 'cluster_name', 'job_state_matcher', 'filter')

    class JobStateMatcher(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[ListJobsRequest.JobStateMatcher]
        ACTIVE: _ClassVar[ListJobsRequest.JobStateMatcher]
        NON_ACTIVE: _ClassVar[ListJobsRequest.JobStateMatcher]
    ALL: ListJobsRequest.JobStateMatcher
    ACTIVE: ListJobsRequest.JobStateMatcher
    NON_ACTIVE: ListJobsRequest.JobStateMatcher
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_STATE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    page_size: int
    page_token: str
    cluster_name: str
    job_state_matcher: ListJobsRequest.JobStateMatcher
    filter: str

    def __init__(self, project_id: _Optional[str]=..., region: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., cluster_name: _Optional[str]=..., job_state_matcher: _Optional[_Union[ListJobsRequest.JobStateMatcher, str]]=..., filter: _Optional[str]=...) -> None:
        ...

class UpdateJobRequest(_message.Message):
    __slots__ = ('project_id', 'region', 'job_id', 'job', 'update_mask')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    job_id: str
    job: Job
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, project_id: _Optional[str]=..., region: _Optional[str]=..., job_id: _Optional[str]=..., job: _Optional[_Union[Job, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListJobsResponse(_message.Message):
    __slots__ = ('jobs', 'next_page_token', 'unreachable')
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, jobs: _Optional[_Iterable[_Union[Job, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CancelJobRequest(_message.Message):
    __slots__ = ('project_id', 'region', 'job_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    job_id: str

    def __init__(self, project_id: _Optional[str]=..., region: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
        ...

class DeleteJobRequest(_message.Message):
    __slots__ = ('project_id', 'region', 'job_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    job_id: str

    def __init__(self, project_id: _Optional[str]=..., region: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
        ...