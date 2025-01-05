from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataproc.v1 import clusters_pb2 as _clusters_pb2
from google.cloud.dataproc.v1 import jobs_pb2 as _jobs_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkflowTemplate(_message.Message):
    __slots__ = ("id", "name", "version", "create_time", "update_time", "labels", "placement", "jobs", "parameters", "dag_timeout", "encryption_config")
    class EncryptionConfig(_message.Message):
        __slots__ = ("kms_key",)
        KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        kms_key: str
        def __init__(self, kms_key: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DAG_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    placement: WorkflowTemplatePlacement
    jobs: _containers.RepeatedCompositeFieldContainer[OrderedJob]
    parameters: _containers.RepeatedCompositeFieldContainer[TemplateParameter]
    dag_timeout: _duration_pb2.Duration
    encryption_config: WorkflowTemplate.EncryptionConfig
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., placement: _Optional[_Union[WorkflowTemplatePlacement, _Mapping]] = ..., jobs: _Optional[_Iterable[_Union[OrderedJob, _Mapping]]] = ..., parameters: _Optional[_Iterable[_Union[TemplateParameter, _Mapping]]] = ..., dag_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., encryption_config: _Optional[_Union[WorkflowTemplate.EncryptionConfig, _Mapping]] = ...) -> None: ...

class WorkflowTemplatePlacement(_message.Message):
    __slots__ = ("managed_cluster", "cluster_selector")
    MANAGED_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    managed_cluster: ManagedCluster
    cluster_selector: ClusterSelector
    def __init__(self, managed_cluster: _Optional[_Union[ManagedCluster, _Mapping]] = ..., cluster_selector: _Optional[_Union[ClusterSelector, _Mapping]] = ...) -> None: ...

class ManagedCluster(_message.Message):
    __slots__ = ("cluster_name", "config", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    config: _clusters_pb2.ClusterConfig
    labels: _containers.ScalarMap[str, str]
    def __init__(self, cluster_name: _Optional[str] = ..., config: _Optional[_Union[_clusters_pb2.ClusterConfig, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ClusterSelector(_message.Message):
    __slots__ = ("zone", "cluster_labels")
    class ClusterLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LABELS_FIELD_NUMBER: _ClassVar[int]
    zone: str
    cluster_labels: _containers.ScalarMap[str, str]
    def __init__(self, zone: _Optional[str] = ..., cluster_labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class OrderedJob(_message.Message):
    __slots__ = ("step_id", "hadoop_job", "spark_job", "pyspark_job", "hive_job", "pig_job", "spark_r_job", "spark_sql_job", "presto_job", "trino_job", "flink_job", "labels", "scheduling", "prerequisite_step_ids")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
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
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_STEP_IDS_FIELD_NUMBER: _ClassVar[int]
    step_id: str
    hadoop_job: _jobs_pb2.HadoopJob
    spark_job: _jobs_pb2.SparkJob
    pyspark_job: _jobs_pb2.PySparkJob
    hive_job: _jobs_pb2.HiveJob
    pig_job: _jobs_pb2.PigJob
    spark_r_job: _jobs_pb2.SparkRJob
    spark_sql_job: _jobs_pb2.SparkSqlJob
    presto_job: _jobs_pb2.PrestoJob
    trino_job: _jobs_pb2.TrinoJob
    flink_job: _jobs_pb2.FlinkJob
    labels: _containers.ScalarMap[str, str]
    scheduling: _jobs_pb2.JobScheduling
    prerequisite_step_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, step_id: _Optional[str] = ..., hadoop_job: _Optional[_Union[_jobs_pb2.HadoopJob, _Mapping]] = ..., spark_job: _Optional[_Union[_jobs_pb2.SparkJob, _Mapping]] = ..., pyspark_job: _Optional[_Union[_jobs_pb2.PySparkJob, _Mapping]] = ..., hive_job: _Optional[_Union[_jobs_pb2.HiveJob, _Mapping]] = ..., pig_job: _Optional[_Union[_jobs_pb2.PigJob, _Mapping]] = ..., spark_r_job: _Optional[_Union[_jobs_pb2.SparkRJob, _Mapping]] = ..., spark_sql_job: _Optional[_Union[_jobs_pb2.SparkSqlJob, _Mapping]] = ..., presto_job: _Optional[_Union[_jobs_pb2.PrestoJob, _Mapping]] = ..., trino_job: _Optional[_Union[_jobs_pb2.TrinoJob, _Mapping]] = ..., flink_job: _Optional[_Union[_jobs_pb2.FlinkJob, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., scheduling: _Optional[_Union[_jobs_pb2.JobScheduling, _Mapping]] = ..., prerequisite_step_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TemplateParameter(_message.Message):
    __slots__ = ("name", "fields", "description", "validation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    description: str
    validation: ParameterValidation
    def __init__(self, name: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., validation: _Optional[_Union[ParameterValidation, _Mapping]] = ...) -> None: ...

class ParameterValidation(_message.Message):
    __slots__ = ("regex", "values")
    REGEX_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    regex: RegexValidation
    values: ValueValidation
    def __init__(self, regex: _Optional[_Union[RegexValidation, _Mapping]] = ..., values: _Optional[_Union[ValueValidation, _Mapping]] = ...) -> None: ...

class RegexValidation(_message.Message):
    __slots__ = ("regexes",)
    REGEXES_FIELD_NUMBER: _ClassVar[int]
    regexes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, regexes: _Optional[_Iterable[str]] = ...) -> None: ...

class ValueValidation(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class WorkflowMetadata(_message.Message):
    __slots__ = ("template", "version", "create_cluster", "graph", "delete_cluster", "state", "cluster_name", "parameters", "start_time", "end_time", "cluster_uuid", "dag_timeout", "dag_start_time", "dag_end_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[WorkflowMetadata.State]
        PENDING: _ClassVar[WorkflowMetadata.State]
        RUNNING: _ClassVar[WorkflowMetadata.State]
        DONE: _ClassVar[WorkflowMetadata.State]
    UNKNOWN: WorkflowMetadata.State
    PENDING: WorkflowMetadata.State
    RUNNING: WorkflowMetadata.State
    DONE: WorkflowMetadata.State
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    DAG_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DAG_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DAG_END_TIME_FIELD_NUMBER: _ClassVar[int]
    template: str
    version: int
    create_cluster: ClusterOperation
    graph: WorkflowGraph
    delete_cluster: ClusterOperation
    state: WorkflowMetadata.State
    cluster_name: str
    parameters: _containers.ScalarMap[str, str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    cluster_uuid: str
    dag_timeout: _duration_pb2.Duration
    dag_start_time: _timestamp_pb2.Timestamp
    dag_end_time: _timestamp_pb2.Timestamp
    def __init__(self, template: _Optional[str] = ..., version: _Optional[int] = ..., create_cluster: _Optional[_Union[ClusterOperation, _Mapping]] = ..., graph: _Optional[_Union[WorkflowGraph, _Mapping]] = ..., delete_cluster: _Optional[_Union[ClusterOperation, _Mapping]] = ..., state: _Optional[_Union[WorkflowMetadata.State, str]] = ..., cluster_name: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cluster_uuid: _Optional[str] = ..., dag_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., dag_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dag_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ClusterOperation(_message.Message):
    __slots__ = ("operation_id", "error", "done")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    error: str
    done: bool
    def __init__(self, operation_id: _Optional[str] = ..., error: _Optional[str] = ..., done: bool = ...) -> None: ...

class WorkflowGraph(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[WorkflowNode]
    def __init__(self, nodes: _Optional[_Iterable[_Union[WorkflowNode, _Mapping]]] = ...) -> None: ...

class WorkflowNode(_message.Message):
    __slots__ = ("step_id", "prerequisite_step_ids", "job_id", "state", "error")
    class NodeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_STATE_UNSPECIFIED: _ClassVar[WorkflowNode.NodeState]
        BLOCKED: _ClassVar[WorkflowNode.NodeState]
        RUNNABLE: _ClassVar[WorkflowNode.NodeState]
        RUNNING: _ClassVar[WorkflowNode.NodeState]
        COMPLETED: _ClassVar[WorkflowNode.NodeState]
        FAILED: _ClassVar[WorkflowNode.NodeState]
    NODE_STATE_UNSPECIFIED: WorkflowNode.NodeState
    BLOCKED: WorkflowNode.NodeState
    RUNNABLE: WorkflowNode.NodeState
    RUNNING: WorkflowNode.NodeState
    COMPLETED: WorkflowNode.NodeState
    FAILED: WorkflowNode.NodeState
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    PREREQUISITE_STEP_IDS_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    step_id: str
    prerequisite_step_ids: _containers.RepeatedScalarFieldContainer[str]
    job_id: str
    state: WorkflowNode.NodeState
    error: str
    def __init__(self, step_id: _Optional[str] = ..., prerequisite_step_ids: _Optional[_Iterable[str]] = ..., job_id: _Optional[str] = ..., state: _Optional[_Union[WorkflowNode.NodeState, str]] = ..., error: _Optional[str] = ...) -> None: ...

class CreateWorkflowTemplateRequest(_message.Message):
    __slots__ = ("parent", "template")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    template: WorkflowTemplate
    def __init__(self, parent: _Optional[str] = ..., template: _Optional[_Union[WorkflowTemplate, _Mapping]] = ...) -> None: ...

class GetWorkflowTemplateRequest(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class InstantiateWorkflowTemplateRequest(_message.Message):
    __slots__ = ("name", "version", "request_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: int
    request_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., request_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class InstantiateInlineWorkflowTemplateRequest(_message.Message):
    __slots__ = ("parent", "template", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    template: WorkflowTemplate
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., template: _Optional[_Union[WorkflowTemplate, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateWorkflowTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: WorkflowTemplate
    def __init__(self, template: _Optional[_Union[WorkflowTemplate, _Mapping]] = ...) -> None: ...

class ListWorkflowTemplatesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListWorkflowTemplatesResponse(_message.Message):
    __slots__ = ("templates", "next_page_token", "unreachable")
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[WorkflowTemplate]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, templates: _Optional[_Iterable[_Union[WorkflowTemplate, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteWorkflowTemplateRequest(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
