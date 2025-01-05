from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import artifact_pb2 as _artifact_pb2
from google.cloud.aiplatform.v1beta1 import context_pb2 as _context_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import execution_pb2 as _execution_pb2
from google.cloud.aiplatform.v1beta1 import pipeline_failure_policy_pb2 as _pipeline_failure_policy_pb2
from google.cloud.aiplatform.v1beta1 import pipeline_state_pb2 as _pipeline_state_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.cloud.aiplatform.v1beta1 import ui_pipeline_spec_pb2 as _ui_pipeline_spec_pb2
from google.cloud.aiplatform.v1beta1 import value_pb2 as _value_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PipelineJob(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'start_time', 'end_time', 'update_time', 'pipeline_spec', 'state', 'job_detail', 'error', 'labels', 'runtime_config', 'encryption_spec', 'service_account', 'network', 'reserved_ip_ranges', 'psc_interface_config', 'template_uri', 'template_metadata', 'schedule_name', 'preflight_validations', 'satisfies_pzs', 'satisfies_pzi', 'original_pipeline_job_id', 'pipeline_task_rerun_configs')

    class RuntimeConfig(_message.Message):
        __slots__ = ('parameters', 'gcs_output_directory', 'parameter_values', 'failure_policy', 'input_artifacts', 'default_runtime')

        class InputArtifact(_message.Message):
            __slots__ = ('artifact_id',)
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str

            def __init__(self, artifact_id: _Optional[str]=...) -> None:
                ...

        class PersistentResourceRuntimeDetail(_message.Message):
            __slots__ = ('persistent_resource_name', 'task_resource_unavailable_wait_time_ms', 'task_resource_unavailable_timeout_behavior')

            class TaskResourceUnavailableTimeoutBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TASK_RESOURCE_UNAVAILABLE_TIMEOUT_BEHAVIOR_UNSPECIFIED: _ClassVar[PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior]
                FAIL: _ClassVar[PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior]
                FALL_BACK_TO_ON_DEMAND: _ClassVar[PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior]
            TASK_RESOURCE_UNAVAILABLE_TIMEOUT_BEHAVIOR_UNSPECIFIED: PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior
            FAIL: PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior
            FALL_BACK_TO_ON_DEMAND: PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior
            PERSISTENT_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
            TASK_RESOURCE_UNAVAILABLE_WAIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
            TASK_RESOURCE_UNAVAILABLE_TIMEOUT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            persistent_resource_name: str
            task_resource_unavailable_wait_time_ms: int
            task_resource_unavailable_timeout_behavior: PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior

            def __init__(self, persistent_resource_name: _Optional[str]=..., task_resource_unavailable_wait_time_ms: _Optional[int]=..., task_resource_unavailable_timeout_behavior: _Optional[_Union[PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail.TaskResourceUnavailableTimeoutBehavior, str]]=...) -> None:
                ...

        class DefaultRuntime(_message.Message):
            __slots__ = ('persistent_resource_runtime_detail',)
            PERSISTENT_RESOURCE_RUNTIME_DETAIL_FIELD_NUMBER: _ClassVar[int]
            persistent_resource_runtime_detail: PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail

            def __init__(self, persistent_resource_runtime_detail: _Optional[_Union[PipelineJob.RuntimeConfig.PersistentResourceRuntimeDetail, _Mapping]]=...) -> None:
                ...

        class ParametersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _value_pb2.Value

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_value_pb2.Value, _Mapping]]=...) -> None:
                ...

        class ParameterValuesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
                ...

        class InputArtifactsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PipelineJob.RuntimeConfig.InputArtifact

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[PipelineJob.RuntimeConfig.InputArtifact, _Mapping]]=...) -> None:
                ...
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_VALUES_FIELD_NUMBER: _ClassVar[int]
        FAILURE_POLICY_FIELD_NUMBER: _ClassVar[int]
        INPUT_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_RUNTIME_FIELD_NUMBER: _ClassVar[int]
        parameters: _containers.MessageMap[str, _value_pb2.Value]
        gcs_output_directory: str
        parameter_values: _containers.MessageMap[str, _struct_pb2.Value]
        failure_policy: _pipeline_failure_policy_pb2.PipelineFailurePolicy
        input_artifacts: _containers.MessageMap[str, PipelineJob.RuntimeConfig.InputArtifact]
        default_runtime: PipelineJob.RuntimeConfig.DefaultRuntime

        def __init__(self, parameters: _Optional[_Mapping[str, _value_pb2.Value]]=..., gcs_output_directory: _Optional[str]=..., parameter_values: _Optional[_Mapping[str, _struct_pb2.Value]]=..., failure_policy: _Optional[_Union[_pipeline_failure_policy_pb2.PipelineFailurePolicy, str]]=..., input_artifacts: _Optional[_Mapping[str, PipelineJob.RuntimeConfig.InputArtifact]]=..., default_runtime: _Optional[_Union[PipelineJob.RuntimeConfig.DefaultRuntime, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    PSC_INTERFACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_URI_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFLIGHT_VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PIPELINE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_TASK_RERUN_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    pipeline_spec: _struct_pb2.Struct
    state: _pipeline_state_pb2.PipelineState
    job_detail: PipelineJobDetail
    error: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    runtime_config: PipelineJob.RuntimeConfig
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    service_account: str
    network: str
    reserved_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    psc_interface_config: _service_networking_pb2.PscInterfaceConfig
    template_uri: str
    template_metadata: PipelineTemplateMetadata
    schedule_name: str
    preflight_validations: bool
    satisfies_pzs: bool
    satisfies_pzi: bool
    original_pipeline_job_id: int
    pipeline_task_rerun_configs: _containers.RepeatedCompositeFieldContainer[PipelineTaskRerunConfig]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., pipeline_spec: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., state: _Optional[_Union[_pipeline_state_pb2.PipelineState, str]]=..., job_detail: _Optional[_Union[PipelineJobDetail, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., runtime_config: _Optional[_Union[PipelineJob.RuntimeConfig, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., service_account: _Optional[str]=..., network: _Optional[str]=..., reserved_ip_ranges: _Optional[_Iterable[str]]=..., psc_interface_config: _Optional[_Union[_service_networking_pb2.PscInterfaceConfig, _Mapping]]=..., template_uri: _Optional[str]=..., template_metadata: _Optional[_Union[PipelineTemplateMetadata, _Mapping]]=..., schedule_name: _Optional[str]=..., preflight_validations: bool=..., satisfies_pzs: bool=..., satisfies_pzi: bool=..., original_pipeline_job_id: _Optional[int]=..., pipeline_task_rerun_configs: _Optional[_Iterable[_Union[PipelineTaskRerunConfig, _Mapping]]]=...) -> None:
        ...

class PipelineTemplateMetadata(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str

    def __init__(self, version: _Optional[str]=...) -> None:
        ...

class PipelineJobDetail(_message.Message):
    __slots__ = ('pipeline_context', 'pipeline_run_context', 'task_details')
    PIPELINE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_RUN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TASK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    pipeline_context: _context_pb2.Context
    pipeline_run_context: _context_pb2.Context
    task_details: _containers.RepeatedCompositeFieldContainer[PipelineTaskDetail]

    def __init__(self, pipeline_context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., pipeline_run_context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., task_details: _Optional[_Iterable[_Union[PipelineTaskDetail, _Mapping]]]=...) -> None:
        ...

class PipelineTaskDetail(_message.Message):
    __slots__ = ('task_id', 'parent_task_id', 'task_name', 'create_time', 'start_time', 'end_time', 'executor_detail', 'state', 'execution', 'error', 'pipeline_task_status', 'inputs', 'outputs')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PipelineTaskDetail.State]
        PENDING: _ClassVar[PipelineTaskDetail.State]
        RUNNING: _ClassVar[PipelineTaskDetail.State]
        SUCCEEDED: _ClassVar[PipelineTaskDetail.State]
        CANCEL_PENDING: _ClassVar[PipelineTaskDetail.State]
        CANCELLING: _ClassVar[PipelineTaskDetail.State]
        CANCELLED: _ClassVar[PipelineTaskDetail.State]
        FAILED: _ClassVar[PipelineTaskDetail.State]
        SKIPPED: _ClassVar[PipelineTaskDetail.State]
        NOT_TRIGGERED: _ClassVar[PipelineTaskDetail.State]
    STATE_UNSPECIFIED: PipelineTaskDetail.State
    PENDING: PipelineTaskDetail.State
    RUNNING: PipelineTaskDetail.State
    SUCCEEDED: PipelineTaskDetail.State
    CANCEL_PENDING: PipelineTaskDetail.State
    CANCELLING: PipelineTaskDetail.State
    CANCELLED: PipelineTaskDetail.State
    FAILED: PipelineTaskDetail.State
    SKIPPED: PipelineTaskDetail.State
    NOT_TRIGGERED: PipelineTaskDetail.State

    class PipelineTaskStatus(_message.Message):
        __slots__ = ('update_time', 'state', 'error')
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        update_time: _timestamp_pb2.Timestamp
        state: PipelineTaskDetail.State
        error: _status_pb2.Status

        def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[PipelineTaskDetail.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class ArtifactList(_message.Message):
        __slots__ = ('artifacts',)
        ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
        artifacts: _containers.RepeatedCompositeFieldContainer[_artifact_pb2.Artifact]

        def __init__(self, artifacts: _Optional[_Iterable[_Union[_artifact_pb2.Artifact, _Mapping]]]=...) -> None:
            ...

    class InputsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PipelineTaskDetail.ArtifactList

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[PipelineTaskDetail.ArtifactList, _Mapping]]=...) -> None:
            ...

    class OutputsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PipelineTaskDetail.ArtifactList

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[PipelineTaskDetail.ArtifactList, _Mapping]]=...) -> None:
            ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    parent_task_id: int
    task_name: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    executor_detail: PipelineTaskExecutorDetail
    state: PipelineTaskDetail.State
    execution: _execution_pb2.Execution
    error: _status_pb2.Status
    pipeline_task_status: _containers.RepeatedCompositeFieldContainer[PipelineTaskDetail.PipelineTaskStatus]
    inputs: _containers.MessageMap[str, PipelineTaskDetail.ArtifactList]
    outputs: _containers.MessageMap[str, PipelineTaskDetail.ArtifactList]

    def __init__(self, task_id: _Optional[int]=..., parent_task_id: _Optional[int]=..., task_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., executor_detail: _Optional[_Union[PipelineTaskExecutorDetail, _Mapping]]=..., state: _Optional[_Union[PipelineTaskDetail.State, str]]=..., execution: _Optional[_Union[_execution_pb2.Execution, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., pipeline_task_status: _Optional[_Iterable[_Union[PipelineTaskDetail.PipelineTaskStatus, _Mapping]]]=..., inputs: _Optional[_Mapping[str, PipelineTaskDetail.ArtifactList]]=..., outputs: _Optional[_Mapping[str, PipelineTaskDetail.ArtifactList]]=...) -> None:
        ...

class PipelineTaskExecutorDetail(_message.Message):
    __slots__ = ('container_detail', 'custom_job_detail')

    class ContainerDetail(_message.Message):
        __slots__ = ('main_job', 'pre_caching_check_job', 'failed_main_jobs', 'failed_pre_caching_check_jobs')
        MAIN_JOB_FIELD_NUMBER: _ClassVar[int]
        PRE_CACHING_CHECK_JOB_FIELD_NUMBER: _ClassVar[int]
        FAILED_MAIN_JOBS_FIELD_NUMBER: _ClassVar[int]
        FAILED_PRE_CACHING_CHECK_JOBS_FIELD_NUMBER: _ClassVar[int]
        main_job: str
        pre_caching_check_job: str
        failed_main_jobs: _containers.RepeatedScalarFieldContainer[str]
        failed_pre_caching_check_jobs: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, main_job: _Optional[str]=..., pre_caching_check_job: _Optional[str]=..., failed_main_jobs: _Optional[_Iterable[str]]=..., failed_pre_caching_check_jobs: _Optional[_Iterable[str]]=...) -> None:
            ...

    class CustomJobDetail(_message.Message):
        __slots__ = ('job', 'failed_jobs')
        JOB_FIELD_NUMBER: _ClassVar[int]
        FAILED_JOBS_FIELD_NUMBER: _ClassVar[int]
        job: str
        failed_jobs: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, job: _Optional[str]=..., failed_jobs: _Optional[_Iterable[str]]=...) -> None:
            ...
    CONTAINER_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_JOB_DETAIL_FIELD_NUMBER: _ClassVar[int]
    container_detail: PipelineTaskExecutorDetail.ContainerDetail
    custom_job_detail: PipelineTaskExecutorDetail.CustomJobDetail

    def __init__(self, container_detail: _Optional[_Union[PipelineTaskExecutorDetail.ContainerDetail, _Mapping]]=..., custom_job_detail: _Optional[_Union[PipelineTaskExecutorDetail.CustomJobDetail, _Mapping]]=...) -> None:
        ...

class PipelineTaskRerunConfig(_message.Message):
    __slots__ = ('task_id', 'task_name', 'inputs', 'skip_task', 'skip_downstream_tasks')

    class ArtifactList(_message.Message):
        __slots__ = ('artifacts',)
        ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
        artifacts: _containers.RepeatedCompositeFieldContainer[_ui_pipeline_spec_pb2.RuntimeArtifact]

        def __init__(self, artifacts: _Optional[_Iterable[_Union[_ui_pipeline_spec_pb2.RuntimeArtifact, _Mapping]]]=...) -> None:
            ...

    class Inputs(_message.Message):
        __slots__ = ('artifacts', 'parameter_values')

        class ArtifactsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PipelineTaskRerunConfig.ArtifactList

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[PipelineTaskRerunConfig.ArtifactList, _Mapping]]=...) -> None:
                ...

        class ParameterValuesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
                ...
        ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_VALUES_FIELD_NUMBER: _ClassVar[int]
        artifacts: _containers.MessageMap[str, PipelineTaskRerunConfig.ArtifactList]
        parameter_values: _containers.MessageMap[str, _struct_pb2.Value]

        def __init__(self, artifacts: _Optional[_Mapping[str, PipelineTaskRerunConfig.ArtifactList]]=..., parameter_values: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
            ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    SKIP_TASK_FIELD_NUMBER: _ClassVar[int]
    SKIP_DOWNSTREAM_TASKS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    task_name: str
    inputs: PipelineTaskRerunConfig.Inputs
    skip_task: bool
    skip_downstream_tasks: bool

    def __init__(self, task_id: _Optional[int]=..., task_name: _Optional[str]=..., inputs: _Optional[_Union[PipelineTaskRerunConfig.Inputs, _Mapping]]=..., skip_task: bool=..., skip_downstream_tasks: bool=...) -> None:
        ...