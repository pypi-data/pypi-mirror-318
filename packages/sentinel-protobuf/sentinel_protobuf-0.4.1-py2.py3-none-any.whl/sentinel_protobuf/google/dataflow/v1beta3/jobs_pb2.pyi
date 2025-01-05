from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.dataflow.v1beta3 import environment_pb2 as _environment_pb2
from google.dataflow.v1beta3 import snapshots_pb2 as _snapshots_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class KindType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_KIND: _ClassVar[KindType]
    PAR_DO_KIND: _ClassVar[KindType]
    GROUP_BY_KEY_KIND: _ClassVar[KindType]
    FLATTEN_KIND: _ClassVar[KindType]
    READ_KIND: _ClassVar[KindType]
    WRITE_KIND: _ClassVar[KindType]
    CONSTANT_KIND: _ClassVar[KindType]
    SINGLETON_KIND: _ClassVar[KindType]
    SHUFFLE_KIND: _ClassVar[KindType]

class JobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_STATE_UNKNOWN: _ClassVar[JobState]
    JOB_STATE_STOPPED: _ClassVar[JobState]
    JOB_STATE_RUNNING: _ClassVar[JobState]
    JOB_STATE_DONE: _ClassVar[JobState]
    JOB_STATE_FAILED: _ClassVar[JobState]
    JOB_STATE_CANCELLED: _ClassVar[JobState]
    JOB_STATE_UPDATED: _ClassVar[JobState]
    JOB_STATE_DRAINING: _ClassVar[JobState]
    JOB_STATE_DRAINED: _ClassVar[JobState]
    JOB_STATE_PENDING: _ClassVar[JobState]
    JOB_STATE_CANCELLING: _ClassVar[JobState]
    JOB_STATE_QUEUED: _ClassVar[JobState]
    JOB_STATE_RESOURCE_CLEANING_UP: _ClassVar[JobState]

class JobView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_VIEW_UNKNOWN: _ClassVar[JobView]
    JOB_VIEW_SUMMARY: _ClassVar[JobView]
    JOB_VIEW_ALL: _ClassVar[JobView]
    JOB_VIEW_DESCRIPTION: _ClassVar[JobView]
UNKNOWN_KIND: KindType
PAR_DO_KIND: KindType
GROUP_BY_KEY_KIND: KindType
FLATTEN_KIND: KindType
READ_KIND: KindType
WRITE_KIND: KindType
CONSTANT_KIND: KindType
SINGLETON_KIND: KindType
SHUFFLE_KIND: KindType
JOB_STATE_UNKNOWN: JobState
JOB_STATE_STOPPED: JobState
JOB_STATE_RUNNING: JobState
JOB_STATE_DONE: JobState
JOB_STATE_FAILED: JobState
JOB_STATE_CANCELLED: JobState
JOB_STATE_UPDATED: JobState
JOB_STATE_DRAINING: JobState
JOB_STATE_DRAINED: JobState
JOB_STATE_PENDING: JobState
JOB_STATE_CANCELLING: JobState
JOB_STATE_QUEUED: JobState
JOB_STATE_RESOURCE_CLEANING_UP: JobState
JOB_VIEW_UNKNOWN: JobView
JOB_VIEW_SUMMARY: JobView
JOB_VIEW_ALL: JobView
JOB_VIEW_DESCRIPTION: JobView

class Job(_message.Message):
    __slots__ = ('id', 'project_id', 'name', 'type', 'environment', 'steps', 'steps_location', 'current_state', 'current_state_time', 'requested_state', 'execution_info', 'create_time', 'replace_job_id', 'transform_name_mapping', 'client_request_id', 'replaced_by_job_id', 'temp_files', 'labels', 'location', 'pipeline_description', 'stage_states', 'job_metadata', 'start_time', 'created_from_snapshot_id', 'satisfies_pzs')

    class TransformNameMappingEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    STEPS_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REPLACE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NAME_MAPPING_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REPLACED_BY_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TEMP_FILES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STAGE_STATES_FIELD_NUMBER: _ClassVar[int]
    JOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FROM_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    type: _environment_pb2.JobType
    environment: _environment_pb2.Environment
    steps: _containers.RepeatedCompositeFieldContainer[Step]
    steps_location: str
    current_state: JobState
    current_state_time: _timestamp_pb2.Timestamp
    requested_state: JobState
    execution_info: JobExecutionInfo
    create_time: _timestamp_pb2.Timestamp
    replace_job_id: str
    transform_name_mapping: _containers.ScalarMap[str, str]
    client_request_id: str
    replaced_by_job_id: str
    temp_files: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.ScalarMap[str, str]
    location: str
    pipeline_description: PipelineDescription
    stage_states: _containers.RepeatedCompositeFieldContainer[ExecutionStageState]
    job_metadata: JobMetadata
    start_time: _timestamp_pb2.Timestamp
    created_from_snapshot_id: str
    satisfies_pzs: bool

    def __init__(self, id: _Optional[str]=..., project_id: _Optional[str]=..., name: _Optional[str]=..., type: _Optional[_Union[_environment_pb2.JobType, str]]=..., environment: _Optional[_Union[_environment_pb2.Environment, _Mapping]]=..., steps: _Optional[_Iterable[_Union[Step, _Mapping]]]=..., steps_location: _Optional[str]=..., current_state: _Optional[_Union[JobState, str]]=..., current_state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., requested_state: _Optional[_Union[JobState, str]]=..., execution_info: _Optional[_Union[JobExecutionInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., replace_job_id: _Optional[str]=..., transform_name_mapping: _Optional[_Mapping[str, str]]=..., client_request_id: _Optional[str]=..., replaced_by_job_id: _Optional[str]=..., temp_files: _Optional[_Iterable[str]]=..., labels: _Optional[_Mapping[str, str]]=..., location: _Optional[str]=..., pipeline_description: _Optional[_Union[PipelineDescription, _Mapping]]=..., stage_states: _Optional[_Iterable[_Union[ExecutionStageState, _Mapping]]]=..., job_metadata: _Optional[_Union[JobMetadata, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., created_from_snapshot_id: _Optional[str]=..., satisfies_pzs: bool=...) -> None:
        ...

class DatastoreIODetails(_message.Message):
    __slots__ = ('namespace', 'project_id')
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    project_id: str

    def __init__(self, namespace: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class PubSubIODetails(_message.Message):
    __slots__ = ('topic', 'subscription')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    topic: str
    subscription: str

    def __init__(self, topic: _Optional[str]=..., subscription: _Optional[str]=...) -> None:
        ...

class FileIODetails(_message.Message):
    __slots__ = ('file_pattern',)
    FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    file_pattern: str

    def __init__(self, file_pattern: _Optional[str]=...) -> None:
        ...

class BigTableIODetails(_message.Message):
    __slots__ = ('project_id', 'instance_id', 'table_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    table_id: str

    def __init__(self, project_id: _Optional[str]=..., instance_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class BigQueryIODetails(_message.Message):
    __slots__ = ('table', 'dataset', 'project_id', 'query')
    TABLE_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    table: str
    dataset: str
    project_id: str
    query: str

    def __init__(self, table: _Optional[str]=..., dataset: _Optional[str]=..., project_id: _Optional[str]=..., query: _Optional[str]=...) -> None:
        ...

class SpannerIODetails(_message.Message):
    __slots__ = ('project_id', 'instance_id', 'database_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    database_id: str

    def __init__(self, project_id: _Optional[str]=..., instance_id: _Optional[str]=..., database_id: _Optional[str]=...) -> None:
        ...

class SdkVersion(_message.Message):
    __slots__ = ('version', 'version_display_name', 'sdk_support_status')

    class SdkSupportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SdkVersion.SdkSupportStatus]
        SUPPORTED: _ClassVar[SdkVersion.SdkSupportStatus]
        STALE: _ClassVar[SdkVersion.SdkSupportStatus]
        DEPRECATED: _ClassVar[SdkVersion.SdkSupportStatus]
        UNSUPPORTED: _ClassVar[SdkVersion.SdkSupportStatus]
    UNKNOWN: SdkVersion.SdkSupportStatus
    SUPPORTED: SdkVersion.SdkSupportStatus
    STALE: SdkVersion.SdkSupportStatus
    DEPRECATED: SdkVersion.SdkSupportStatus
    UNSUPPORTED: SdkVersion.SdkSupportStatus
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SDK_SUPPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    version: str
    version_display_name: str
    sdk_support_status: SdkVersion.SdkSupportStatus

    def __init__(self, version: _Optional[str]=..., version_display_name: _Optional[str]=..., sdk_support_status: _Optional[_Union[SdkVersion.SdkSupportStatus, str]]=...) -> None:
        ...

class JobMetadata(_message.Message):
    __slots__ = ('sdk_version', 'spanner_details', 'bigquery_details', 'big_table_details', 'pubsub_details', 'file_details', 'datastore_details')
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPANNER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BIG_TABLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FILE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    sdk_version: SdkVersion
    spanner_details: _containers.RepeatedCompositeFieldContainer[SpannerIODetails]
    bigquery_details: _containers.RepeatedCompositeFieldContainer[BigQueryIODetails]
    big_table_details: _containers.RepeatedCompositeFieldContainer[BigTableIODetails]
    pubsub_details: _containers.RepeatedCompositeFieldContainer[PubSubIODetails]
    file_details: _containers.RepeatedCompositeFieldContainer[FileIODetails]
    datastore_details: _containers.RepeatedCompositeFieldContainer[DatastoreIODetails]

    def __init__(self, sdk_version: _Optional[_Union[SdkVersion, _Mapping]]=..., spanner_details: _Optional[_Iterable[_Union[SpannerIODetails, _Mapping]]]=..., bigquery_details: _Optional[_Iterable[_Union[BigQueryIODetails, _Mapping]]]=..., big_table_details: _Optional[_Iterable[_Union[BigTableIODetails, _Mapping]]]=..., pubsub_details: _Optional[_Iterable[_Union[PubSubIODetails, _Mapping]]]=..., file_details: _Optional[_Iterable[_Union[FileIODetails, _Mapping]]]=..., datastore_details: _Optional[_Iterable[_Union[DatastoreIODetails, _Mapping]]]=...) -> None:
        ...

class ExecutionStageState(_message.Message):
    __slots__ = ('execution_stage_name', 'execution_stage_state', 'current_state_time')
    EXECUTION_STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STAGE_STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    execution_stage_name: str
    execution_stage_state: JobState
    current_state_time: _timestamp_pb2.Timestamp

    def __init__(self, execution_stage_name: _Optional[str]=..., execution_stage_state: _Optional[_Union[JobState, str]]=..., current_state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PipelineDescription(_message.Message):
    __slots__ = ('original_pipeline_transform', 'execution_pipeline_stage', 'display_data')
    ORIGINAL_PIPELINE_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PIPELINE_STAGE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_FIELD_NUMBER: _ClassVar[int]
    original_pipeline_transform: _containers.RepeatedCompositeFieldContainer[TransformSummary]
    execution_pipeline_stage: _containers.RepeatedCompositeFieldContainer[ExecutionStageSummary]
    display_data: _containers.RepeatedCompositeFieldContainer[DisplayData]

    def __init__(self, original_pipeline_transform: _Optional[_Iterable[_Union[TransformSummary, _Mapping]]]=..., execution_pipeline_stage: _Optional[_Iterable[_Union[ExecutionStageSummary, _Mapping]]]=..., display_data: _Optional[_Iterable[_Union[DisplayData, _Mapping]]]=...) -> None:
        ...

class TransformSummary(_message.Message):
    __slots__ = ('kind', 'id', 'name', 'display_data', 'output_collection_name', 'input_collection_name')
    KIND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    kind: KindType
    id: str
    name: str
    display_data: _containers.RepeatedCompositeFieldContainer[DisplayData]
    output_collection_name: _containers.RepeatedScalarFieldContainer[str]
    input_collection_name: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, kind: _Optional[_Union[KindType, str]]=..., id: _Optional[str]=..., name: _Optional[str]=..., display_data: _Optional[_Iterable[_Union[DisplayData, _Mapping]]]=..., output_collection_name: _Optional[_Iterable[str]]=..., input_collection_name: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExecutionStageSummary(_message.Message):
    __slots__ = ('name', 'id', 'kind', 'input_source', 'output_source', 'prerequisite_stage', 'component_transform', 'component_source')

    class StageSource(_message.Message):
        __slots__ = ('user_name', 'name', 'original_transform_or_collection', 'size_bytes')
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_TRANSFORM_OR_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        user_name: str
        name: str
        original_transform_or_collection: str
        size_bytes: int

        def __init__(self, user_name: _Optional[str]=..., name: _Optional[str]=..., original_transform_or_collection: _Optional[str]=..., size_bytes: _Optional[int]=...) -> None:
            ...

    class ComponentTransform(_message.Message):
        __slots__ = ('user_name', 'name', 'original_transform')
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
        user_name: str
        name: str
        original_transform: str

        def __init__(self, user_name: _Optional[str]=..., name: _Optional[str]=..., original_transform: _Optional[str]=...) -> None:
            ...

    class ComponentSource(_message.Message):
        __slots__ = ('user_name', 'name', 'original_transform_or_collection')
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_TRANSFORM_OR_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        user_name: str
        name: str
        original_transform_or_collection: str

        def __init__(self, user_name: _Optional[str]=..., name: _Optional[str]=..., original_transform_or_collection: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    INPUT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_STAGE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    kind: KindType
    input_source: _containers.RepeatedCompositeFieldContainer[ExecutionStageSummary.StageSource]
    output_source: _containers.RepeatedCompositeFieldContainer[ExecutionStageSummary.StageSource]
    prerequisite_stage: _containers.RepeatedScalarFieldContainer[str]
    component_transform: _containers.RepeatedCompositeFieldContainer[ExecutionStageSummary.ComponentTransform]
    component_source: _containers.RepeatedCompositeFieldContainer[ExecutionStageSummary.ComponentSource]

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., kind: _Optional[_Union[KindType, str]]=..., input_source: _Optional[_Iterable[_Union[ExecutionStageSummary.StageSource, _Mapping]]]=..., output_source: _Optional[_Iterable[_Union[ExecutionStageSummary.StageSource, _Mapping]]]=..., prerequisite_stage: _Optional[_Iterable[str]]=..., component_transform: _Optional[_Iterable[_Union[ExecutionStageSummary.ComponentTransform, _Mapping]]]=..., component_source: _Optional[_Iterable[_Union[ExecutionStageSummary.ComponentSource, _Mapping]]]=...) -> None:
        ...

class DisplayData(_message.Message):
    __slots__ = ('key', 'namespace', 'str_value', 'int64_value', 'float_value', 'java_class_value', 'timestamp_value', 'duration_value', 'bool_value', 'short_str_value', 'url', 'label')
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    JAVA_CLASS_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHORT_STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    key: str
    namespace: str
    str_value: str
    int64_value: int
    float_value: float
    java_class_value: str
    timestamp_value: _timestamp_pb2.Timestamp
    duration_value: _duration_pb2.Duration
    bool_value: bool
    short_str_value: str
    url: str
    label: str

    def __init__(self, key: _Optional[str]=..., namespace: _Optional[str]=..., str_value: _Optional[str]=..., int64_value: _Optional[int]=..., float_value: _Optional[float]=..., java_class_value: _Optional[str]=..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration_value: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., bool_value: bool=..., short_str_value: _Optional[str]=..., url: _Optional[str]=..., label: _Optional[str]=...) -> None:
        ...

class Step(_message.Message):
    __slots__ = ('kind', 'name', 'properties')
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    properties: _struct_pb2.Struct

    def __init__(self, kind: _Optional[str]=..., name: _Optional[str]=..., properties: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class JobExecutionInfo(_message.Message):
    __slots__ = ('stages',)

    class StagesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: JobExecutionStageInfo

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[JobExecutionStageInfo, _Mapping]]=...) -> None:
            ...
    STAGES_FIELD_NUMBER: _ClassVar[int]
    stages: _containers.MessageMap[str, JobExecutionStageInfo]

    def __init__(self, stages: _Optional[_Mapping[str, JobExecutionStageInfo]]=...) -> None:
        ...

class JobExecutionStageInfo(_message.Message):
    __slots__ = ('step_name',)
    STEP_NAME_FIELD_NUMBER: _ClassVar[int]
    step_name: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, step_name: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateJobRequest(_message.Message):
    __slots__ = ('project_id', 'job', 'view', 'replace_job_id', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    REPLACE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job: Job
    view: JobView
    replace_job_id: str
    location: str

    def __init__(self, project_id: _Optional[str]=..., job: _Optional[_Union[Job, _Mapping]]=..., view: _Optional[_Union[JobView, str]]=..., replace_job_id: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class GetJobRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'view', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    view: JobView
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., view: _Optional[_Union[JobView, str]]=..., location: _Optional[str]=...) -> None:
        ...

class UpdateJobRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'job', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    job: Job
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., job: _Optional[_Union[Job, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class ListJobsRequest(_message.Message):
    __slots__ = ('filter', 'project_id', 'view', 'page_size', 'page_token', 'location')

    class Filter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ListJobsRequest.Filter]
        ALL: _ClassVar[ListJobsRequest.Filter]
        TERMINATED: _ClassVar[ListJobsRequest.Filter]
        ACTIVE: _ClassVar[ListJobsRequest.Filter]
    UNKNOWN: ListJobsRequest.Filter
    ALL: ListJobsRequest.Filter
    TERMINATED: ListJobsRequest.Filter
    ACTIVE: ListJobsRequest.Filter
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    filter: ListJobsRequest.Filter
    project_id: str
    view: JobView
    page_size: int
    page_token: str
    location: str

    def __init__(self, filter: _Optional[_Union[ListJobsRequest.Filter, str]]=..., project_id: _Optional[str]=..., view: _Optional[_Union[JobView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class FailedLocation(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListJobsResponse(_message.Message):
    __slots__ = ('jobs', 'next_page_token', 'failed_location')
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    next_page_token: str
    failed_location: _containers.RepeatedCompositeFieldContainer[FailedLocation]

    def __init__(self, jobs: _Optional[_Iterable[_Union[Job, _Mapping]]]=..., next_page_token: _Optional[str]=..., failed_location: _Optional[_Iterable[_Union[FailedLocation, _Mapping]]]=...) -> None:
        ...

class SnapshotJobRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'ttl', 'location', 'snapshot_sources', 'description')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SOURCES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    ttl: _duration_pb2.Duration
    location: str
    snapshot_sources: bool
    description: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., location: _Optional[str]=..., snapshot_sources: bool=..., description: _Optional[str]=...) -> None:
        ...

class CheckActiveJobsRequest(_message.Message):
    __slots__ = ('project_id',)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str

    def __init__(self, project_id: _Optional[str]=...) -> None:
        ...

class CheckActiveJobsResponse(_message.Message):
    __slots__ = ('active_jobs_exist',)
    ACTIVE_JOBS_EXIST_FIELD_NUMBER: _ClassVar[int]
    active_jobs_exist: bool

    def __init__(self, active_jobs_exist: bool=...) -> None:
        ...