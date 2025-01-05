from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoveryEvent(_message.Message):
    __slots__ = ("message", "lake_id", "zone_id", "asset_id", "data_location", "datascan_id", "type", "config", "entity", "partition", "action", "table")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[DiscoveryEvent.EventType]
        CONFIG: _ClassVar[DiscoveryEvent.EventType]
        ENTITY_CREATED: _ClassVar[DiscoveryEvent.EventType]
        ENTITY_UPDATED: _ClassVar[DiscoveryEvent.EventType]
        ENTITY_DELETED: _ClassVar[DiscoveryEvent.EventType]
        PARTITION_CREATED: _ClassVar[DiscoveryEvent.EventType]
        PARTITION_UPDATED: _ClassVar[DiscoveryEvent.EventType]
        PARTITION_DELETED: _ClassVar[DiscoveryEvent.EventType]
        TABLE_PUBLISHED: _ClassVar[DiscoveryEvent.EventType]
        TABLE_UPDATED: _ClassVar[DiscoveryEvent.EventType]
        TABLE_IGNORED: _ClassVar[DiscoveryEvent.EventType]
        TABLE_DELETED: _ClassVar[DiscoveryEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: DiscoveryEvent.EventType
    CONFIG: DiscoveryEvent.EventType
    ENTITY_CREATED: DiscoveryEvent.EventType
    ENTITY_UPDATED: DiscoveryEvent.EventType
    ENTITY_DELETED: DiscoveryEvent.EventType
    PARTITION_CREATED: DiscoveryEvent.EventType
    PARTITION_UPDATED: DiscoveryEvent.EventType
    PARTITION_DELETED: DiscoveryEvent.EventType
    TABLE_PUBLISHED: DiscoveryEvent.EventType
    TABLE_UPDATED: DiscoveryEvent.EventType
    TABLE_IGNORED: DiscoveryEvent.EventType
    TABLE_DELETED: DiscoveryEvent.EventType
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTITY_TYPE_UNSPECIFIED: _ClassVar[DiscoveryEvent.EntityType]
        TABLE: _ClassVar[DiscoveryEvent.EntityType]
        FILESET: _ClassVar[DiscoveryEvent.EntityType]
    ENTITY_TYPE_UNSPECIFIED: DiscoveryEvent.EntityType
    TABLE: DiscoveryEvent.EntityType
    FILESET: DiscoveryEvent.EntityType
    class TableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TABLE_TYPE_UNSPECIFIED: _ClassVar[DiscoveryEvent.TableType]
        EXTERNAL_TABLE: _ClassVar[DiscoveryEvent.TableType]
        BIGLAKE_TABLE: _ClassVar[DiscoveryEvent.TableType]
        OBJECT_TABLE: _ClassVar[DiscoveryEvent.TableType]
    TABLE_TYPE_UNSPECIFIED: DiscoveryEvent.TableType
    EXTERNAL_TABLE: DiscoveryEvent.TableType
    BIGLAKE_TABLE: DiscoveryEvent.TableType
    OBJECT_TABLE: DiscoveryEvent.TableType
    class ConfigDetails(_message.Message):
        __slots__ = ("parameters",)
        class ParametersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        parameters: _containers.ScalarMap[str, str]
        def __init__(self, parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class EntityDetails(_message.Message):
        __slots__ = ("entity", "type")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        entity: str
        type: DiscoveryEvent.EntityType
        def __init__(self, entity: _Optional[str] = ..., type: _Optional[_Union[DiscoveryEvent.EntityType, str]] = ...) -> None: ...
    class TableDetails(_message.Message):
        __slots__ = ("table", "type")
        TABLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        table: str
        type: DiscoveryEvent.TableType
        def __init__(self, table: _Optional[str] = ..., type: _Optional[_Union[DiscoveryEvent.TableType, str]] = ...) -> None: ...
    class PartitionDetails(_message.Message):
        __slots__ = ("partition", "entity", "type", "sampled_data_locations")
        PARTITION_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SAMPLED_DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        partition: str
        entity: str
        type: DiscoveryEvent.EntityType
        sampled_data_locations: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, partition: _Optional[str] = ..., entity: _Optional[str] = ..., type: _Optional[_Union[DiscoveryEvent.EntityType, str]] = ..., sampled_data_locations: _Optional[_Iterable[str]] = ...) -> None: ...
    class ActionDetails(_message.Message):
        __slots__ = ("type", "issue")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ISSUE_FIELD_NUMBER: _ClassVar[int]
        type: str
        issue: str
        def __init__(self, type: _Optional[str] = ..., issue: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAKE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DATASCAN_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    message: str
    lake_id: str
    zone_id: str
    asset_id: str
    data_location: str
    datascan_id: str
    type: DiscoveryEvent.EventType
    config: DiscoveryEvent.ConfigDetails
    entity: DiscoveryEvent.EntityDetails
    partition: DiscoveryEvent.PartitionDetails
    action: DiscoveryEvent.ActionDetails
    table: DiscoveryEvent.TableDetails
    def __init__(self, message: _Optional[str] = ..., lake_id: _Optional[str] = ..., zone_id: _Optional[str] = ..., asset_id: _Optional[str] = ..., data_location: _Optional[str] = ..., datascan_id: _Optional[str] = ..., type: _Optional[_Union[DiscoveryEvent.EventType, str]] = ..., config: _Optional[_Union[DiscoveryEvent.ConfigDetails, _Mapping]] = ..., entity: _Optional[_Union[DiscoveryEvent.EntityDetails, _Mapping]] = ..., partition: _Optional[_Union[DiscoveryEvent.PartitionDetails, _Mapping]] = ..., action: _Optional[_Union[DiscoveryEvent.ActionDetails, _Mapping]] = ..., table: _Optional[_Union[DiscoveryEvent.TableDetails, _Mapping]] = ...) -> None: ...

class JobEvent(_message.Message):
    __slots__ = ("message", "job_id", "start_time", "end_time", "state", "retries", "type", "service", "service_job", "execution_trigger")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[JobEvent.Type]
        SPARK: _ClassVar[JobEvent.Type]
        NOTEBOOK: _ClassVar[JobEvent.Type]
    TYPE_UNSPECIFIED: JobEvent.Type
    SPARK: JobEvent.Type
    NOTEBOOK: JobEvent.Type
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[JobEvent.State]
        SUCCEEDED: _ClassVar[JobEvent.State]
        FAILED: _ClassVar[JobEvent.State]
        CANCELLED: _ClassVar[JobEvent.State]
        ABORTED: _ClassVar[JobEvent.State]
    STATE_UNSPECIFIED: JobEvent.State
    SUCCEEDED: JobEvent.State
    FAILED: JobEvent.State
    CANCELLED: JobEvent.State
    ABORTED: JobEvent.State
    class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_UNSPECIFIED: _ClassVar[JobEvent.Service]
        DATAPROC: _ClassVar[JobEvent.Service]
    SERVICE_UNSPECIFIED: JobEvent.Service
    DATAPROC: JobEvent.Service
    class ExecutionTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXECUTION_TRIGGER_UNSPECIFIED: _ClassVar[JobEvent.ExecutionTrigger]
        TASK_CONFIG: _ClassVar[JobEvent.ExecutionTrigger]
        RUN_REQUEST: _ClassVar[JobEvent.ExecutionTrigger]
    EXECUTION_TRIGGER_UNSPECIFIED: JobEvent.ExecutionTrigger
    TASK_CONFIG: JobEvent.ExecutionTrigger
    RUN_REQUEST: JobEvent.ExecutionTrigger
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_JOB_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    message: str
    job_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: JobEvent.State
    retries: int
    type: JobEvent.Type
    service: JobEvent.Service
    service_job: str
    execution_trigger: JobEvent.ExecutionTrigger
    def __init__(self, message: _Optional[str] = ..., job_id: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[JobEvent.State, str]] = ..., retries: _Optional[int] = ..., type: _Optional[_Union[JobEvent.Type, str]] = ..., service: _Optional[_Union[JobEvent.Service, str]] = ..., service_job: _Optional[str] = ..., execution_trigger: _Optional[_Union[JobEvent.ExecutionTrigger, str]] = ...) -> None: ...

class SessionEvent(_message.Message):
    __slots__ = ("message", "user_id", "session_id", "type", "query", "event_succeeded", "fast_startup_enabled", "unassigned_duration")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[SessionEvent.EventType]
        START: _ClassVar[SessionEvent.EventType]
        STOP: _ClassVar[SessionEvent.EventType]
        QUERY: _ClassVar[SessionEvent.EventType]
        CREATE: _ClassVar[SessionEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: SessionEvent.EventType
    START: SessionEvent.EventType
    STOP: SessionEvent.EventType
    QUERY: SessionEvent.EventType
    CREATE: SessionEvent.EventType
    class QueryDetail(_message.Message):
        __slots__ = ("query_id", "query_text", "engine", "duration", "result_size_bytes", "data_processed_bytes")
        class Engine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENGINE_UNSPECIFIED: _ClassVar[SessionEvent.QueryDetail.Engine]
            SPARK_SQL: _ClassVar[SessionEvent.QueryDetail.Engine]
            BIGQUERY: _ClassVar[SessionEvent.QueryDetail.Engine]
        ENGINE_UNSPECIFIED: SessionEvent.QueryDetail.Engine
        SPARK_SQL: SessionEvent.QueryDetail.Engine
        BIGQUERY: SessionEvent.QueryDetail.Engine
        QUERY_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
        ENGINE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        DATA_PROCESSED_BYTES_FIELD_NUMBER: _ClassVar[int]
        query_id: str
        query_text: str
        engine: SessionEvent.QueryDetail.Engine
        duration: _duration_pb2.Duration
        result_size_bytes: int
        data_processed_bytes: int
        def __init__(self, query_id: _Optional[str] = ..., query_text: _Optional[str] = ..., engine: _Optional[_Union[SessionEvent.QueryDetail.Engine, str]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., result_size_bytes: _Optional[int] = ..., data_processed_bytes: _Optional[int] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    EVENT_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    FAST_STARTUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED_DURATION_FIELD_NUMBER: _ClassVar[int]
    message: str
    user_id: str
    session_id: str
    type: SessionEvent.EventType
    query: SessionEvent.QueryDetail
    event_succeeded: bool
    fast_startup_enabled: bool
    unassigned_duration: _duration_pb2.Duration
    def __init__(self, message: _Optional[str] = ..., user_id: _Optional[str] = ..., session_id: _Optional[str] = ..., type: _Optional[_Union[SessionEvent.EventType, str]] = ..., query: _Optional[_Union[SessionEvent.QueryDetail, _Mapping]] = ..., event_succeeded: bool = ..., fast_startup_enabled: bool = ..., unassigned_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GovernanceEvent(_message.Message):
    __slots__ = ("message", "event_type", "entity")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[GovernanceEvent.EventType]
        RESOURCE_IAM_POLICY_UPDATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_TABLE_CREATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_TABLE_UPDATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_TABLE_DELETE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_CONNECTION_CREATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_CONNECTION_UPDATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_CONNECTION_DELETE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_TAXONOMY_CREATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_POLICY_TAG_CREATE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_POLICY_TAG_DELETE: _ClassVar[GovernanceEvent.EventType]
        BIGQUERY_POLICY_TAG_SET_IAM_POLICY: _ClassVar[GovernanceEvent.EventType]
        ACCESS_POLICY_UPDATE: _ClassVar[GovernanceEvent.EventType]
        GOVERNANCE_RULE_MATCHED_RESOURCES: _ClassVar[GovernanceEvent.EventType]
        GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS: _ClassVar[GovernanceEvent.EventType]
        GOVERNANCE_RULE_ERRORS: _ClassVar[GovernanceEvent.EventType]
        GOVERNANCE_RULE_PROCESSING: _ClassVar[GovernanceEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: GovernanceEvent.EventType
    RESOURCE_IAM_POLICY_UPDATE: GovernanceEvent.EventType
    BIGQUERY_TABLE_CREATE: GovernanceEvent.EventType
    BIGQUERY_TABLE_UPDATE: GovernanceEvent.EventType
    BIGQUERY_TABLE_DELETE: GovernanceEvent.EventType
    BIGQUERY_CONNECTION_CREATE: GovernanceEvent.EventType
    BIGQUERY_CONNECTION_UPDATE: GovernanceEvent.EventType
    BIGQUERY_CONNECTION_DELETE: GovernanceEvent.EventType
    BIGQUERY_TAXONOMY_CREATE: GovernanceEvent.EventType
    BIGQUERY_POLICY_TAG_CREATE: GovernanceEvent.EventType
    BIGQUERY_POLICY_TAG_DELETE: GovernanceEvent.EventType
    BIGQUERY_POLICY_TAG_SET_IAM_POLICY: GovernanceEvent.EventType
    ACCESS_POLICY_UPDATE: GovernanceEvent.EventType
    GOVERNANCE_RULE_MATCHED_RESOURCES: GovernanceEvent.EventType
    GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS: GovernanceEvent.EventType
    GOVERNANCE_RULE_ERRORS: GovernanceEvent.EventType
    GOVERNANCE_RULE_PROCESSING: GovernanceEvent.EventType
    class Entity(_message.Message):
        __slots__ = ("entity", "entity_type")
        class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENTITY_TYPE_UNSPECIFIED: _ClassVar[GovernanceEvent.Entity.EntityType]
            TABLE: _ClassVar[GovernanceEvent.Entity.EntityType]
            FILESET: _ClassVar[GovernanceEvent.Entity.EntityType]
        ENTITY_TYPE_UNSPECIFIED: GovernanceEvent.Entity.EntityType
        TABLE: GovernanceEvent.Entity.EntityType
        FILESET: GovernanceEvent.Entity.EntityType
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        entity: str
        entity_type: GovernanceEvent.Entity.EntityType
        def __init__(self, entity: _Optional[str] = ..., entity_type: _Optional[_Union[GovernanceEvent.Entity.EntityType, str]] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    message: str
    event_type: GovernanceEvent.EventType
    entity: GovernanceEvent.Entity
    def __init__(self, message: _Optional[str] = ..., event_type: _Optional[_Union[GovernanceEvent.EventType, str]] = ..., entity: _Optional[_Union[GovernanceEvent.Entity, _Mapping]] = ...) -> None: ...

class DataScanEvent(_message.Message):
    __slots__ = ("data_source", "job_id", "create_time", "start_time", "end_time", "type", "state", "message", "spec_version", "trigger", "scope", "data_profile", "data_quality", "data_profile_configs", "data_quality_configs", "post_scan_actions_result")
    class ScanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCAN_TYPE_UNSPECIFIED: _ClassVar[DataScanEvent.ScanType]
        DATA_PROFILE: _ClassVar[DataScanEvent.ScanType]
        DATA_QUALITY: _ClassVar[DataScanEvent.ScanType]
        DATA_DISCOVERY: _ClassVar[DataScanEvent.ScanType]
    SCAN_TYPE_UNSPECIFIED: DataScanEvent.ScanType
    DATA_PROFILE: DataScanEvent.ScanType
    DATA_QUALITY: DataScanEvent.ScanType
    DATA_DISCOVERY: DataScanEvent.ScanType
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DataScanEvent.State]
        STARTED: _ClassVar[DataScanEvent.State]
        SUCCEEDED: _ClassVar[DataScanEvent.State]
        FAILED: _ClassVar[DataScanEvent.State]
        CANCELLED: _ClassVar[DataScanEvent.State]
        CREATED: _ClassVar[DataScanEvent.State]
    STATE_UNSPECIFIED: DataScanEvent.State
    STARTED: DataScanEvent.State
    SUCCEEDED: DataScanEvent.State
    FAILED: DataScanEvent.State
    CANCELLED: DataScanEvent.State
    CREATED: DataScanEvent.State
    class Trigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_UNSPECIFIED: _ClassVar[DataScanEvent.Trigger]
        ON_DEMAND: _ClassVar[DataScanEvent.Trigger]
        SCHEDULE: _ClassVar[DataScanEvent.Trigger]
    TRIGGER_UNSPECIFIED: DataScanEvent.Trigger
    ON_DEMAND: DataScanEvent.Trigger
    SCHEDULE: DataScanEvent.Trigger
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCOPE_UNSPECIFIED: _ClassVar[DataScanEvent.Scope]
        FULL: _ClassVar[DataScanEvent.Scope]
        INCREMENTAL: _ClassVar[DataScanEvent.Scope]
    SCOPE_UNSPECIFIED: DataScanEvent.Scope
    FULL: DataScanEvent.Scope
    INCREMENTAL: DataScanEvent.Scope
    class DataProfileResult(_message.Message):
        __slots__ = ("row_count",)
        ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
        row_count: int
        def __init__(self, row_count: _Optional[int] = ...) -> None: ...
    class DataQualityResult(_message.Message):
        __slots__ = ("row_count", "passed", "dimension_passed", "score", "dimension_score", "column_score")
        class DimensionPassedEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bool
            def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
        class DimensionScoreEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: float
            def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
        class ColumnScoreEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: float
            def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
        ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
        PASSED_FIELD_NUMBER: _ClassVar[int]
        DIMENSION_PASSED_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        DIMENSION_SCORE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_SCORE_FIELD_NUMBER: _ClassVar[int]
        row_count: int
        passed: bool
        dimension_passed: _containers.ScalarMap[str, bool]
        score: float
        dimension_score: _containers.ScalarMap[str, float]
        column_score: _containers.ScalarMap[str, float]
        def __init__(self, row_count: _Optional[int] = ..., passed: bool = ..., dimension_passed: _Optional[_Mapping[str, bool]] = ..., score: _Optional[float] = ..., dimension_score: _Optional[_Mapping[str, float]] = ..., column_score: _Optional[_Mapping[str, float]] = ...) -> None: ...
    class DataProfileAppliedConfigs(_message.Message):
        __slots__ = ("sampling_percent", "row_filter_applied", "column_filter_applied")
        SAMPLING_PERCENT_FIELD_NUMBER: _ClassVar[int]
        ROW_FILTER_APPLIED_FIELD_NUMBER: _ClassVar[int]
        COLUMN_FILTER_APPLIED_FIELD_NUMBER: _ClassVar[int]
        sampling_percent: float
        row_filter_applied: bool
        column_filter_applied: bool
        def __init__(self, sampling_percent: _Optional[float] = ..., row_filter_applied: bool = ..., column_filter_applied: bool = ...) -> None: ...
    class DataQualityAppliedConfigs(_message.Message):
        __slots__ = ("sampling_percent", "row_filter_applied")
        SAMPLING_PERCENT_FIELD_NUMBER: _ClassVar[int]
        ROW_FILTER_APPLIED_FIELD_NUMBER: _ClassVar[int]
        sampling_percent: float
        row_filter_applied: bool
        def __init__(self, sampling_percent: _Optional[float] = ..., row_filter_applied: bool = ...) -> None: ...
    class PostScanActionsResult(_message.Message):
        __slots__ = ("bigquery_export_result",)
        class BigQueryExportResult(_message.Message):
            __slots__ = ("state", "message")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[DataScanEvent.PostScanActionsResult.BigQueryExportResult.State]
                SUCCEEDED: _ClassVar[DataScanEvent.PostScanActionsResult.BigQueryExportResult.State]
                FAILED: _ClassVar[DataScanEvent.PostScanActionsResult.BigQueryExportResult.State]
                SKIPPED: _ClassVar[DataScanEvent.PostScanActionsResult.BigQueryExportResult.State]
            STATE_UNSPECIFIED: DataScanEvent.PostScanActionsResult.BigQueryExportResult.State
            SUCCEEDED: DataScanEvent.PostScanActionsResult.BigQueryExportResult.State
            FAILED: DataScanEvent.PostScanActionsResult.BigQueryExportResult.State
            SKIPPED: DataScanEvent.PostScanActionsResult.BigQueryExportResult.State
            STATE_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            state: DataScanEvent.PostScanActionsResult.BigQueryExportResult.State
            message: str
            def __init__(self, state: _Optional[_Union[DataScanEvent.PostScanActionsResult.BigQueryExportResult.State, str]] = ..., message: _Optional[str] = ...) -> None: ...
        BIGQUERY_EXPORT_RESULT_FIELD_NUMBER: _ClassVar[int]
        bigquery_export_result: DataScanEvent.PostScanActionsResult.BigQueryExportResult
        def __init__(self, bigquery_export_result: _Optional[_Union[DataScanEvent.PostScanActionsResult.BigQueryExportResult, _Mapping]] = ...) -> None: ...
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SPEC_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    DATA_PROFILE_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_FIELD_NUMBER: _ClassVar[int]
    DATA_PROFILE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_ACTIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
    data_source: str
    job_id: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    type: DataScanEvent.ScanType
    state: DataScanEvent.State
    message: str
    spec_version: str
    trigger: DataScanEvent.Trigger
    scope: DataScanEvent.Scope
    data_profile: DataScanEvent.DataProfileResult
    data_quality: DataScanEvent.DataQualityResult
    data_profile_configs: DataScanEvent.DataProfileAppliedConfigs
    data_quality_configs: DataScanEvent.DataQualityAppliedConfigs
    post_scan_actions_result: DataScanEvent.PostScanActionsResult
    def __init__(self, data_source: _Optional[str] = ..., job_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[DataScanEvent.ScanType, str]] = ..., state: _Optional[_Union[DataScanEvent.State, str]] = ..., message: _Optional[str] = ..., spec_version: _Optional[str] = ..., trigger: _Optional[_Union[DataScanEvent.Trigger, str]] = ..., scope: _Optional[_Union[DataScanEvent.Scope, str]] = ..., data_profile: _Optional[_Union[DataScanEvent.DataProfileResult, _Mapping]] = ..., data_quality: _Optional[_Union[DataScanEvent.DataQualityResult, _Mapping]] = ..., data_profile_configs: _Optional[_Union[DataScanEvent.DataProfileAppliedConfigs, _Mapping]] = ..., data_quality_configs: _Optional[_Union[DataScanEvent.DataQualityAppliedConfigs, _Mapping]] = ..., post_scan_actions_result: _Optional[_Union[DataScanEvent.PostScanActionsResult, _Mapping]] = ...) -> None: ...

class DataQualityScanRuleResult(_message.Message):
    __slots__ = ("job_id", "data_source", "column", "rule_name", "rule_type", "evalution_type", "rule_dimension", "threshold_percent", "result", "evaluated_row_count", "passed_row_count", "null_row_count", "assertion_row_count")
    class RuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RULE_TYPE_UNSPECIFIED: _ClassVar[DataQualityScanRuleResult.RuleType]
        NON_NULL_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        RANGE_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        REGEX_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        ROW_CONDITION_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        SET_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        STATISTIC_RANGE_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        TABLE_CONDITION_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        UNIQUENESS_EXPECTATION: _ClassVar[DataQualityScanRuleResult.RuleType]
        SQL_ASSERTION: _ClassVar[DataQualityScanRuleResult.RuleType]
    RULE_TYPE_UNSPECIFIED: DataQualityScanRuleResult.RuleType
    NON_NULL_EXPECTATION: DataQualityScanRuleResult.RuleType
    RANGE_EXPECTATION: DataQualityScanRuleResult.RuleType
    REGEX_EXPECTATION: DataQualityScanRuleResult.RuleType
    ROW_CONDITION_EXPECTATION: DataQualityScanRuleResult.RuleType
    SET_EXPECTATION: DataQualityScanRuleResult.RuleType
    STATISTIC_RANGE_EXPECTATION: DataQualityScanRuleResult.RuleType
    TABLE_CONDITION_EXPECTATION: DataQualityScanRuleResult.RuleType
    UNIQUENESS_EXPECTATION: DataQualityScanRuleResult.RuleType
    SQL_ASSERTION: DataQualityScanRuleResult.RuleType
    class EvaluationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_TYPE_UNSPECIFIED: _ClassVar[DataQualityScanRuleResult.EvaluationType]
        PER_ROW: _ClassVar[DataQualityScanRuleResult.EvaluationType]
        AGGREGATE: _ClassVar[DataQualityScanRuleResult.EvaluationType]
    EVALUATION_TYPE_UNSPECIFIED: DataQualityScanRuleResult.EvaluationType
    PER_ROW: DataQualityScanRuleResult.EvaluationType
    AGGREGATE: DataQualityScanRuleResult.EvaluationType
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_UNSPECIFIED: _ClassVar[DataQualityScanRuleResult.Result]
        PASSED: _ClassVar[DataQualityScanRuleResult.Result]
        FAILED: _ClassVar[DataQualityScanRuleResult.Result]
    RESULT_UNSPECIFIED: DataQualityScanRuleResult.Result
    PASSED: DataQualityScanRuleResult.Result
    FAILED: DataQualityScanRuleResult.Result
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_PERCENT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASSED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    NULL_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    data_source: str
    column: str
    rule_name: str
    rule_type: DataQualityScanRuleResult.RuleType
    evalution_type: DataQualityScanRuleResult.EvaluationType
    rule_dimension: str
    threshold_percent: float
    result: DataQualityScanRuleResult.Result
    evaluated_row_count: int
    passed_row_count: int
    null_row_count: int
    assertion_row_count: int
    def __init__(self, job_id: _Optional[str] = ..., data_source: _Optional[str] = ..., column: _Optional[str] = ..., rule_name: _Optional[str] = ..., rule_type: _Optional[_Union[DataQualityScanRuleResult.RuleType, str]] = ..., evalution_type: _Optional[_Union[DataQualityScanRuleResult.EvaluationType, str]] = ..., rule_dimension: _Optional[str] = ..., threshold_percent: _Optional[float] = ..., result: _Optional[_Union[DataQualityScanRuleResult.Result, str]] = ..., evaluated_row_count: _Optional[int] = ..., passed_row_count: _Optional[int] = ..., null_row_count: _Optional[int] = ..., assertion_row_count: _Optional[int] = ...) -> None: ...
