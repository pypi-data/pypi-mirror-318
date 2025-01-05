from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.osconfig.v1 import osconfig_common_pb2 as _osconfig_common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutePatchJobRequest(_message.Message):
    __slots__ = ('parent', 'description', 'instance_filter', 'patch_config', 'duration', 'dry_run', 'display_name', 'rollout')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    description: str
    instance_filter: PatchInstanceFilter
    patch_config: PatchConfig
    duration: _duration_pb2.Duration
    dry_run: bool
    display_name: str
    rollout: PatchRollout

    def __init__(self, parent: _Optional[str]=..., description: _Optional[str]=..., instance_filter: _Optional[_Union[PatchInstanceFilter, _Mapping]]=..., patch_config: _Optional[_Union[PatchConfig, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., dry_run: bool=..., display_name: _Optional[str]=..., rollout: _Optional[_Union[PatchRollout, _Mapping]]=...) -> None:
        ...

class GetPatchJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPatchJobInstanceDetailsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListPatchJobInstanceDetailsResponse(_message.Message):
    __slots__ = ('patch_job_instance_details', 'next_page_token')
    PATCH_JOB_INSTANCE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    patch_job_instance_details: _containers.RepeatedCompositeFieldContainer[PatchJobInstanceDetails]
    next_page_token: str

    def __init__(self, patch_job_instance_details: _Optional[_Iterable[_Union[PatchJobInstanceDetails, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class PatchJobInstanceDetails(_message.Message):
    __slots__ = ('name', 'instance_system_id', 'state', 'failure_reason', 'attempt_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_system_id: str
    state: Instance.PatchState
    failure_reason: str
    attempt_count: int

    def __init__(self, name: _Optional[str]=..., instance_system_id: _Optional[str]=..., state: _Optional[_Union[Instance.PatchState, str]]=..., failure_reason: _Optional[str]=..., attempt_count: _Optional[int]=...) -> None:
        ...

class ListPatchJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListPatchJobsResponse(_message.Message):
    __slots__ = ('patch_jobs', 'next_page_token')
    PATCH_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    patch_jobs: _containers.RepeatedCompositeFieldContainer[PatchJob]
    next_page_token: str

    def __init__(self, patch_jobs: _Optional[_Iterable[_Union[PatchJob, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class PatchJob(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'state', 'instance_filter', 'patch_config', 'duration', 'instance_details_summary', 'dry_run', 'error_message', 'percent_complete', 'patch_deployment', 'rollout')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PatchJob.State]
        STARTED: _ClassVar[PatchJob.State]
        INSTANCE_LOOKUP: _ClassVar[PatchJob.State]
        PATCHING: _ClassVar[PatchJob.State]
        SUCCEEDED: _ClassVar[PatchJob.State]
        COMPLETED_WITH_ERRORS: _ClassVar[PatchJob.State]
        CANCELED: _ClassVar[PatchJob.State]
        TIMED_OUT: _ClassVar[PatchJob.State]
    STATE_UNSPECIFIED: PatchJob.State
    STARTED: PatchJob.State
    INSTANCE_LOOKUP: PatchJob.State
    PATCHING: PatchJob.State
    SUCCEEDED: PatchJob.State
    COMPLETED_WITH_ERRORS: PatchJob.State
    CANCELED: PatchJob.State
    TIMED_OUT: PatchJob.State

    class InstanceDetailsSummary(_message.Message):
        __slots__ = ('pending_instance_count', 'inactive_instance_count', 'notified_instance_count', 'started_instance_count', 'downloading_patches_instance_count', 'applying_patches_instance_count', 'rebooting_instance_count', 'succeeded_instance_count', 'succeeded_reboot_required_instance_count', 'failed_instance_count', 'acked_instance_count', 'timed_out_instance_count', 'pre_patch_step_instance_count', 'post_patch_step_instance_count', 'no_agent_detected_instance_count')
        PENDING_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        NOTIFIED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        STARTED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_PATCHES_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        APPLYING_PATCHES_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        REBOOTING_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        SUCCEEDED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        SUCCEEDED_REBOOT_REQUIRED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        FAILED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        ACKED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TIMED_OUT_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        PRE_PATCH_STEP_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        POST_PATCH_STEP_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        NO_AGENT_DETECTED_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
        pending_instance_count: int
        inactive_instance_count: int
        notified_instance_count: int
        started_instance_count: int
        downloading_patches_instance_count: int
        applying_patches_instance_count: int
        rebooting_instance_count: int
        succeeded_instance_count: int
        succeeded_reboot_required_instance_count: int
        failed_instance_count: int
        acked_instance_count: int
        timed_out_instance_count: int
        pre_patch_step_instance_count: int
        post_patch_step_instance_count: int
        no_agent_detected_instance_count: int

        def __init__(self, pending_instance_count: _Optional[int]=..., inactive_instance_count: _Optional[int]=..., notified_instance_count: _Optional[int]=..., started_instance_count: _Optional[int]=..., downloading_patches_instance_count: _Optional[int]=..., applying_patches_instance_count: _Optional[int]=..., rebooting_instance_count: _Optional[int]=..., succeeded_instance_count: _Optional[int]=..., succeeded_reboot_required_instance_count: _Optional[int]=..., failed_instance_count: _Optional[int]=..., acked_instance_count: _Optional[int]=..., timed_out_instance_count: _Optional[int]=..., pre_patch_step_instance_count: _Optional[int]=..., post_patch_step_instance_count: _Optional[int]=..., no_agent_detected_instance_count: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_DETAILS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    PATCH_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: PatchJob.State
    instance_filter: PatchInstanceFilter
    patch_config: PatchConfig
    duration: _duration_pb2.Duration
    instance_details_summary: PatchJob.InstanceDetailsSummary
    dry_run: bool
    error_message: str
    percent_complete: float
    patch_deployment: str
    rollout: PatchRollout

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[PatchJob.State, str]]=..., instance_filter: _Optional[_Union[PatchInstanceFilter, _Mapping]]=..., patch_config: _Optional[_Union[PatchConfig, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., instance_details_summary: _Optional[_Union[PatchJob.InstanceDetailsSummary, _Mapping]]=..., dry_run: bool=..., error_message: _Optional[str]=..., percent_complete: _Optional[float]=..., patch_deployment: _Optional[str]=..., rollout: _Optional[_Union[PatchRollout, _Mapping]]=...) -> None:
        ...

class PatchConfig(_message.Message):
    __slots__ = ('reboot_config', 'apt', 'yum', 'goo', 'zypper', 'windows_update', 'pre_step', 'post_step', 'mig_instances_allowed')

    class RebootConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REBOOT_CONFIG_UNSPECIFIED: _ClassVar[PatchConfig.RebootConfig]
        DEFAULT: _ClassVar[PatchConfig.RebootConfig]
        ALWAYS: _ClassVar[PatchConfig.RebootConfig]
        NEVER: _ClassVar[PatchConfig.RebootConfig]
    REBOOT_CONFIG_UNSPECIFIED: PatchConfig.RebootConfig
    DEFAULT: PatchConfig.RebootConfig
    ALWAYS: PatchConfig.RebootConfig
    NEVER: PatchConfig.RebootConfig
    REBOOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    APT_FIELD_NUMBER: _ClassVar[int]
    YUM_FIELD_NUMBER: _ClassVar[int]
    GOO_FIELD_NUMBER: _ClassVar[int]
    ZYPPER_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PRE_STEP_FIELD_NUMBER: _ClassVar[int]
    POST_STEP_FIELD_NUMBER: _ClassVar[int]
    MIG_INSTANCES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    reboot_config: PatchConfig.RebootConfig
    apt: AptSettings
    yum: YumSettings
    goo: GooSettings
    zypper: ZypperSettings
    windows_update: WindowsUpdateSettings
    pre_step: ExecStep
    post_step: ExecStep
    mig_instances_allowed: bool

    def __init__(self, reboot_config: _Optional[_Union[PatchConfig.RebootConfig, str]]=..., apt: _Optional[_Union[AptSettings, _Mapping]]=..., yum: _Optional[_Union[YumSettings, _Mapping]]=..., goo: _Optional[_Union[GooSettings, _Mapping]]=..., zypper: _Optional[_Union[ZypperSettings, _Mapping]]=..., windows_update: _Optional[_Union[WindowsUpdateSettings, _Mapping]]=..., pre_step: _Optional[_Union[ExecStep, _Mapping]]=..., post_step: _Optional[_Union[ExecStep, _Mapping]]=..., mig_instances_allowed: bool=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ()

    class PatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATCH_STATE_UNSPECIFIED: _ClassVar[Instance.PatchState]
        PENDING: _ClassVar[Instance.PatchState]
        INACTIVE: _ClassVar[Instance.PatchState]
        NOTIFIED: _ClassVar[Instance.PatchState]
        STARTED: _ClassVar[Instance.PatchState]
        DOWNLOADING_PATCHES: _ClassVar[Instance.PatchState]
        APPLYING_PATCHES: _ClassVar[Instance.PatchState]
        REBOOTING: _ClassVar[Instance.PatchState]
        SUCCEEDED: _ClassVar[Instance.PatchState]
        SUCCEEDED_REBOOT_REQUIRED: _ClassVar[Instance.PatchState]
        FAILED: _ClassVar[Instance.PatchState]
        ACKED: _ClassVar[Instance.PatchState]
        TIMED_OUT: _ClassVar[Instance.PatchState]
        RUNNING_PRE_PATCH_STEP: _ClassVar[Instance.PatchState]
        RUNNING_POST_PATCH_STEP: _ClassVar[Instance.PatchState]
        NO_AGENT_DETECTED: _ClassVar[Instance.PatchState]
    PATCH_STATE_UNSPECIFIED: Instance.PatchState
    PENDING: Instance.PatchState
    INACTIVE: Instance.PatchState
    NOTIFIED: Instance.PatchState
    STARTED: Instance.PatchState
    DOWNLOADING_PATCHES: Instance.PatchState
    APPLYING_PATCHES: Instance.PatchState
    REBOOTING: Instance.PatchState
    SUCCEEDED: Instance.PatchState
    SUCCEEDED_REBOOT_REQUIRED: Instance.PatchState
    FAILED: Instance.PatchState
    ACKED: Instance.PatchState
    TIMED_OUT: Instance.PatchState
    RUNNING_PRE_PATCH_STEP: Instance.PatchState
    RUNNING_POST_PATCH_STEP: Instance.PatchState
    NO_AGENT_DETECTED: Instance.PatchState

    def __init__(self) -> None:
        ...

class CancelPatchJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class AptSettings(_message.Message):
    __slots__ = ('type', 'excludes', 'exclusive_packages')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AptSettings.Type]
        DIST: _ClassVar[AptSettings.Type]
        UPGRADE: _ClassVar[AptSettings.Type]
    TYPE_UNSPECIFIED: AptSettings.Type
    DIST: AptSettings.Type
    UPGRADE: AptSettings.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    type: AptSettings.Type
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_packages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, type: _Optional[_Union[AptSettings.Type, str]]=..., excludes: _Optional[_Iterable[str]]=..., exclusive_packages: _Optional[_Iterable[str]]=...) -> None:
        ...

class YumSettings(_message.Message):
    __slots__ = ('security', 'minimal', 'excludes', 'exclusive_packages')
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    MINIMAL_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    security: bool
    minimal: bool
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_packages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, security: bool=..., minimal: bool=..., excludes: _Optional[_Iterable[str]]=..., exclusive_packages: _Optional[_Iterable[str]]=...) -> None:
        ...

class GooSettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ZypperSettings(_message.Message):
    __slots__ = ('with_optional', 'with_update', 'categories', 'severities', 'excludes', 'exclusive_patches')
    WITH_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    WITH_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SEVERITIES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    with_optional: bool
    with_update: bool
    categories: _containers.RepeatedScalarFieldContainer[str]
    severities: _containers.RepeatedScalarFieldContainer[str]
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_patches: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, with_optional: bool=..., with_update: bool=..., categories: _Optional[_Iterable[str]]=..., severities: _Optional[_Iterable[str]]=..., excludes: _Optional[_Iterable[str]]=..., exclusive_patches: _Optional[_Iterable[str]]=...) -> None:
        ...

class WindowsUpdateSettings(_message.Message):
    __slots__ = ('classifications', 'excludes', 'exclusive_patches')

    class Classification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLASSIFICATION_UNSPECIFIED: _ClassVar[WindowsUpdateSettings.Classification]
        CRITICAL: _ClassVar[WindowsUpdateSettings.Classification]
        SECURITY: _ClassVar[WindowsUpdateSettings.Classification]
        DEFINITION: _ClassVar[WindowsUpdateSettings.Classification]
        DRIVER: _ClassVar[WindowsUpdateSettings.Classification]
        FEATURE_PACK: _ClassVar[WindowsUpdateSettings.Classification]
        SERVICE_PACK: _ClassVar[WindowsUpdateSettings.Classification]
        TOOL: _ClassVar[WindowsUpdateSettings.Classification]
        UPDATE_ROLLUP: _ClassVar[WindowsUpdateSettings.Classification]
        UPDATE: _ClassVar[WindowsUpdateSettings.Classification]
    CLASSIFICATION_UNSPECIFIED: WindowsUpdateSettings.Classification
    CRITICAL: WindowsUpdateSettings.Classification
    SECURITY: WindowsUpdateSettings.Classification
    DEFINITION: WindowsUpdateSettings.Classification
    DRIVER: WindowsUpdateSettings.Classification
    FEATURE_PACK: WindowsUpdateSettings.Classification
    SERVICE_PACK: WindowsUpdateSettings.Classification
    TOOL: WindowsUpdateSettings.Classification
    UPDATE_ROLLUP: WindowsUpdateSettings.Classification
    UPDATE: WindowsUpdateSettings.Classification
    CLASSIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    classifications: _containers.RepeatedScalarFieldContainer[WindowsUpdateSettings.Classification]
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_patches: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, classifications: _Optional[_Iterable[_Union[WindowsUpdateSettings.Classification, str]]]=..., excludes: _Optional[_Iterable[str]]=..., exclusive_patches: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExecStep(_message.Message):
    __slots__ = ('linux_exec_step_config', 'windows_exec_step_config')
    LINUX_EXEC_STEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_EXEC_STEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    linux_exec_step_config: ExecStepConfig
    windows_exec_step_config: ExecStepConfig

    def __init__(self, linux_exec_step_config: _Optional[_Union[ExecStepConfig, _Mapping]]=..., windows_exec_step_config: _Optional[_Union[ExecStepConfig, _Mapping]]=...) -> None:
        ...

class ExecStepConfig(_message.Message):
    __slots__ = ('local_path', 'gcs_object', 'allowed_success_codes', 'interpreter')

    class Interpreter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERPRETER_UNSPECIFIED: _ClassVar[ExecStepConfig.Interpreter]
        SHELL: _ClassVar[ExecStepConfig.Interpreter]
        POWERSHELL: _ClassVar[ExecStepConfig.Interpreter]
    INTERPRETER_UNSPECIFIED: ExecStepConfig.Interpreter
    SHELL: ExecStepConfig.Interpreter
    POWERSHELL: ExecStepConfig.Interpreter
    LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
    GCS_OBJECT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SUCCESS_CODES_FIELD_NUMBER: _ClassVar[int]
    INTERPRETER_FIELD_NUMBER: _ClassVar[int]
    local_path: str
    gcs_object: GcsObject
    allowed_success_codes: _containers.RepeatedScalarFieldContainer[int]
    interpreter: ExecStepConfig.Interpreter

    def __init__(self, local_path: _Optional[str]=..., gcs_object: _Optional[_Union[GcsObject, _Mapping]]=..., allowed_success_codes: _Optional[_Iterable[int]]=..., interpreter: _Optional[_Union[ExecStepConfig.Interpreter, str]]=...) -> None:
        ...

class GcsObject(_message.Message):
    __slots__ = ('bucket', 'object', 'generation_number')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation_number: int

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation_number: _Optional[int]=...) -> None:
        ...

class PatchInstanceFilter(_message.Message):
    __slots__ = ('all', 'group_labels', 'zones', 'instances', 'instance_name_prefixes')

    class GroupLabel(_message.Message):
        __slots__ = ('labels',)

        class LabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        LABELS_FIELD_NUMBER: _ClassVar[int]
        labels: _containers.ScalarMap[str, str]

        def __init__(self, labels: _Optional[_Mapping[str, str]]=...) -> None:
            ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    GROUP_LABELS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAME_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    all: bool
    group_labels: _containers.RepeatedCompositeFieldContainer[PatchInstanceFilter.GroupLabel]
    zones: _containers.RepeatedScalarFieldContainer[str]
    instances: _containers.RepeatedScalarFieldContainer[str]
    instance_name_prefixes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, all: bool=..., group_labels: _Optional[_Iterable[_Union[PatchInstanceFilter.GroupLabel, _Mapping]]]=..., zones: _Optional[_Iterable[str]]=..., instances: _Optional[_Iterable[str]]=..., instance_name_prefixes: _Optional[_Iterable[str]]=...) -> None:
        ...

class PatchRollout(_message.Message):
    __slots__ = ('mode', 'disruption_budget')

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[PatchRollout.Mode]
        ZONE_BY_ZONE: _ClassVar[PatchRollout.Mode]
        CONCURRENT_ZONES: _ClassVar[PatchRollout.Mode]
    MODE_UNSPECIFIED: PatchRollout.Mode
    ZONE_BY_ZONE: PatchRollout.Mode
    CONCURRENT_ZONES: PatchRollout.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    DISRUPTION_BUDGET_FIELD_NUMBER: _ClassVar[int]
    mode: PatchRollout.Mode
    disruption_budget: _osconfig_common_pb2.FixedOrPercent

    def __init__(self, mode: _Optional[_Union[PatchRollout.Mode, str]]=..., disruption_budget: _Optional[_Union[_osconfig_common_pb2.FixedOrPercent, _Mapping]]=...) -> None:
        ...