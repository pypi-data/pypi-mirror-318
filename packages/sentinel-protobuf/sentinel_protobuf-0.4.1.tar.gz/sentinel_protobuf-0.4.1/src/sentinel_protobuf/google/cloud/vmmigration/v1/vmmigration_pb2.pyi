from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import error_details_pb2 as _error_details_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UtilizationReportView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UTILIZATION_REPORT_VIEW_UNSPECIFIED: _ClassVar[UtilizationReportView]
    BASIC: _ClassVar[UtilizationReportView]
    FULL: _ClassVar[UtilizationReportView]

class MigratingVmView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIGRATING_VM_VIEW_UNSPECIFIED: _ClassVar[MigratingVmView]
    MIGRATING_VM_VIEW_BASIC: _ClassVar[MigratingVmView]
    MIGRATING_VM_VIEW_FULL: _ClassVar[MigratingVmView]

class ComputeEngineDiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_STANDARD: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_SSD: _ClassVar[ComputeEngineDiskType]
    COMPUTE_ENGINE_DISK_TYPE_BALANCED: _ClassVar[ComputeEngineDiskType]

class ComputeEngineLicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT: _ClassVar[ComputeEngineLicenseType]
    COMPUTE_ENGINE_LICENSE_TYPE_PAYG: _ClassVar[ComputeEngineLicenseType]
    COMPUTE_ENGINE_LICENSE_TYPE_BYOL: _ClassVar[ComputeEngineLicenseType]

class ComputeEngineBootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED: _ClassVar[ComputeEngineBootOption]
    COMPUTE_ENGINE_BOOT_OPTION_EFI: _ClassVar[ComputeEngineBootOption]
    COMPUTE_ENGINE_BOOT_OPTION_BIOS: _ClassVar[ComputeEngineBootOption]
UTILIZATION_REPORT_VIEW_UNSPECIFIED: UtilizationReportView
BASIC: UtilizationReportView
FULL: UtilizationReportView
MIGRATING_VM_VIEW_UNSPECIFIED: MigratingVmView
MIGRATING_VM_VIEW_BASIC: MigratingVmView
MIGRATING_VM_VIEW_FULL: MigratingVmView
COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_STANDARD: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_SSD: ComputeEngineDiskType
COMPUTE_ENGINE_DISK_TYPE_BALANCED: ComputeEngineDiskType
COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT: ComputeEngineLicenseType
COMPUTE_ENGINE_LICENSE_TYPE_PAYG: ComputeEngineLicenseType
COMPUTE_ENGINE_LICENSE_TYPE_BYOL: ComputeEngineLicenseType
COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED: ComputeEngineBootOption
COMPUTE_ENGINE_BOOT_OPTION_EFI: ComputeEngineBootOption
COMPUTE_ENGINE_BOOT_OPTION_BIOS: ComputeEngineBootOption

class ReplicationCycle(_message.Message):
    __slots__ = ('name', 'cycle_number', 'start_time', 'end_time', 'total_pause_duration', 'progress_percent', 'steps', 'state', 'error')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ReplicationCycle.State]
        RUNNING: _ClassVar[ReplicationCycle.State]
        PAUSED: _ClassVar[ReplicationCycle.State]
        FAILED: _ClassVar[ReplicationCycle.State]
        SUCCEEDED: _ClassVar[ReplicationCycle.State]
    STATE_UNSPECIFIED: ReplicationCycle.State
    RUNNING: ReplicationCycle.State
    PAUSED: ReplicationCycle.State
    FAILED: ReplicationCycle.State
    SUCCEEDED: ReplicationCycle.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CYCLE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAUSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    cycle_number: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    total_pause_duration: _duration_pb2.Duration
    progress_percent: int
    steps: _containers.RepeatedCompositeFieldContainer[CycleStep]
    state: ReplicationCycle.State
    error: _status_pb2.Status

    def __init__(self, name: _Optional[str]=..., cycle_number: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., total_pause_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., progress_percent: _Optional[int]=..., steps: _Optional[_Iterable[_Union[CycleStep, _Mapping]]]=..., state: _Optional[_Union[ReplicationCycle.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class CycleStep(_message.Message):
    __slots__ = ('initializing_replication', 'replicating', 'post_processing', 'start_time', 'end_time')
    INITIALIZING_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    REPLICATING_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    initializing_replication: InitializingReplicationStep
    replicating: ReplicatingStep
    post_processing: PostProcessingStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, initializing_replication: _Optional[_Union[InitializingReplicationStep, _Mapping]]=..., replicating: _Optional[_Union[ReplicatingStep, _Mapping]]=..., post_processing: _Optional[_Union[PostProcessingStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class InitializingReplicationStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReplicatingStep(_message.Message):
    __slots__ = ('total_bytes', 'replicated_bytes', 'last_two_minutes_average_bytes_per_second', 'last_thirty_minutes_average_bytes_per_second')
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_TWO_MINUTES_AVERAGE_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    LAST_THIRTY_MINUTES_AVERAGE_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    total_bytes: int
    replicated_bytes: int
    last_two_minutes_average_bytes_per_second: int
    last_thirty_minutes_average_bytes_per_second: int

    def __init__(self, total_bytes: _Optional[int]=..., replicated_bytes: _Optional[int]=..., last_two_minutes_average_bytes_per_second: _Optional[int]=..., last_thirty_minutes_average_bytes_per_second: _Optional[int]=...) -> None:
        ...

class PostProcessingStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReplicationSync(_message.Message):
    __slots__ = ('last_sync_time',)
    LAST_SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
    last_sync_time: _timestamp_pb2.Timestamp

    def __init__(self, last_sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class MigratingVm(_message.Message):
    __slots__ = ('compute_engine_target_defaults', 'aws_source_vm_details', 'name', 'source_vm_id', 'display_name', 'description', 'policy', 'create_time', 'update_time', 'last_sync', 'state', 'state_time', 'current_sync_info', 'group', 'labels', 'recent_clone_jobs', 'error', 'recent_cutover_jobs')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MigratingVm.State]
        PENDING: _ClassVar[MigratingVm.State]
        READY: _ClassVar[MigratingVm.State]
        FIRST_SYNC: _ClassVar[MigratingVm.State]
        ACTIVE: _ClassVar[MigratingVm.State]
        CUTTING_OVER: _ClassVar[MigratingVm.State]
        CUTOVER: _ClassVar[MigratingVm.State]
        FINAL_SYNC: _ClassVar[MigratingVm.State]
        PAUSED: _ClassVar[MigratingVm.State]
        FINALIZING: _ClassVar[MigratingVm.State]
        FINALIZED: _ClassVar[MigratingVm.State]
        ERROR: _ClassVar[MigratingVm.State]
    STATE_UNSPECIFIED: MigratingVm.State
    PENDING: MigratingVm.State
    READY: MigratingVm.State
    FIRST_SYNC: MigratingVm.State
    ACTIVE: MigratingVm.State
    CUTTING_OVER: MigratingVm.State
    CUTOVER: MigratingVm.State
    FINAL_SYNC: MigratingVm.State
    PAUSED: MigratingVm.State
    FINALIZING: MigratingVm.State
    FINALIZED: MigratingVm.State
    ERROR: MigratingVm.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    COMPUTE_ENGINE_TARGET_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    AWS_SOURCE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SYNC_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RECENT_CLONE_JOBS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RECENT_CUTOVER_JOBS_FIELD_NUMBER: _ClassVar[int]
    compute_engine_target_defaults: ComputeEngineTargetDefaults
    aws_source_vm_details: AwsSourceVmDetails
    name: str
    source_vm_id: str
    display_name: str
    description: str
    policy: SchedulePolicy
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    last_sync: ReplicationSync
    state: MigratingVm.State
    state_time: _timestamp_pb2.Timestamp
    current_sync_info: ReplicationCycle
    group: str
    labels: _containers.ScalarMap[str, str]
    recent_clone_jobs: _containers.RepeatedCompositeFieldContainer[CloneJob]
    error: _status_pb2.Status
    recent_cutover_jobs: _containers.RepeatedCompositeFieldContainer[CutoverJob]

    def __init__(self, compute_engine_target_defaults: _Optional[_Union[ComputeEngineTargetDefaults, _Mapping]]=..., aws_source_vm_details: _Optional[_Union[AwsSourceVmDetails, _Mapping]]=..., name: _Optional[str]=..., source_vm_id: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., policy: _Optional[_Union[SchedulePolicy, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_sync: _Optional[_Union[ReplicationSync, _Mapping]]=..., state: _Optional[_Union[MigratingVm.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., current_sync_info: _Optional[_Union[ReplicationCycle, _Mapping]]=..., group: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., recent_clone_jobs: _Optional[_Iterable[_Union[CloneJob, _Mapping]]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., recent_cutover_jobs: _Optional[_Iterable[_Union[CutoverJob, _Mapping]]]=...) -> None:
        ...

class CloneJob(_message.Message):
    __slots__ = ('compute_engine_target_details', 'create_time', 'end_time', 'name', 'state', 'state_time', 'error', 'steps')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CloneJob.State]
        PENDING: _ClassVar[CloneJob.State]
        ACTIVE: _ClassVar[CloneJob.State]
        FAILED: _ClassVar[CloneJob.State]
        SUCCEEDED: _ClassVar[CloneJob.State]
        CANCELLED: _ClassVar[CloneJob.State]
        CANCELLING: _ClassVar[CloneJob.State]
        ADAPTING_OS: _ClassVar[CloneJob.State]
    STATE_UNSPECIFIED: CloneJob.State
    PENDING: CloneJob.State
    ACTIVE: CloneJob.State
    FAILED: CloneJob.State
    SUCCEEDED: CloneJob.State
    CANCELLED: CloneJob.State
    CANCELLING: CloneJob.State
    ADAPTING_OS: CloneJob.State
    COMPUTE_ENGINE_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    compute_engine_target_details: ComputeEngineTargetDetails
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    name: str
    state: CloneJob.State
    state_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    steps: _containers.RepeatedCompositeFieldContainer[CloneStep]

    def __init__(self, compute_engine_target_details: _Optional[_Union[ComputeEngineTargetDetails, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[CloneJob.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., steps: _Optional[_Iterable[_Union[CloneStep, _Mapping]]]=...) -> None:
        ...

class CloneStep(_message.Message):
    __slots__ = ('adapting_os', 'preparing_vm_disks', 'instantiating_migrated_vm', 'start_time', 'end_time')
    ADAPTING_OS_FIELD_NUMBER: _ClassVar[int]
    PREPARING_VM_DISKS_FIELD_NUMBER: _ClassVar[int]
    INSTANTIATING_MIGRATED_VM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    adapting_os: AdaptingOSStep
    preparing_vm_disks: PreparingVMDisksStep
    instantiating_migrated_vm: InstantiatingMigratedVMStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, adapting_os: _Optional[_Union[AdaptingOSStep, _Mapping]]=..., preparing_vm_disks: _Optional[_Union[PreparingVMDisksStep, _Mapping]]=..., instantiating_migrated_vm: _Optional[_Union[InstantiatingMigratedVMStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AdaptingOSStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PreparingVMDisksStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class InstantiatingMigratedVMStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CutoverJob(_message.Message):
    __slots__ = ('compute_engine_target_details', 'create_time', 'end_time', 'name', 'state', 'state_time', 'progress_percent', 'error', 'state_message', 'steps')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CutoverJob.State]
        PENDING: _ClassVar[CutoverJob.State]
        FAILED: _ClassVar[CutoverJob.State]
        SUCCEEDED: _ClassVar[CutoverJob.State]
        CANCELLED: _ClassVar[CutoverJob.State]
        CANCELLING: _ClassVar[CutoverJob.State]
        ACTIVE: _ClassVar[CutoverJob.State]
        ADAPTING_OS: _ClassVar[CutoverJob.State]
    STATE_UNSPECIFIED: CutoverJob.State
    PENDING: CutoverJob.State
    FAILED: CutoverJob.State
    SUCCEEDED: CutoverJob.State
    CANCELLED: CutoverJob.State
    CANCELLING: CutoverJob.State
    ACTIVE: CutoverJob.State
    ADAPTING_OS: CutoverJob.State
    COMPUTE_ENGINE_TARGET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    compute_engine_target_details: ComputeEngineTargetDetails
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    name: str
    state: CutoverJob.State
    state_time: _timestamp_pb2.Timestamp
    progress_percent: int
    error: _status_pb2.Status
    state_message: str
    steps: _containers.RepeatedCompositeFieldContainer[CutoverStep]

    def __init__(self, compute_engine_target_details: _Optional[_Union[ComputeEngineTargetDetails, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[CutoverJob.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., progress_percent: _Optional[int]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., state_message: _Optional[str]=..., steps: _Optional[_Iterable[_Union[CutoverStep, _Mapping]]]=...) -> None:
        ...

class CutoverStep(_message.Message):
    __slots__ = ('previous_replication_cycle', 'shutting_down_source_vm', 'final_sync', 'preparing_vm_disks', 'instantiating_migrated_vm', 'start_time', 'end_time')
    PREVIOUS_REPLICATION_CYCLE_FIELD_NUMBER: _ClassVar[int]
    SHUTTING_DOWN_SOURCE_VM_FIELD_NUMBER: _ClassVar[int]
    FINAL_SYNC_FIELD_NUMBER: _ClassVar[int]
    PREPARING_VM_DISKS_FIELD_NUMBER: _ClassVar[int]
    INSTANTIATING_MIGRATED_VM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    previous_replication_cycle: ReplicationCycle
    shutting_down_source_vm: ShuttingDownSourceVMStep
    final_sync: ReplicationCycle
    preparing_vm_disks: PreparingVMDisksStep
    instantiating_migrated_vm: InstantiatingMigratedVMStep
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, previous_replication_cycle: _Optional[_Union[ReplicationCycle, _Mapping]]=..., shutting_down_source_vm: _Optional[_Union[ShuttingDownSourceVMStep, _Mapping]]=..., final_sync: _Optional[_Union[ReplicationCycle, _Mapping]]=..., preparing_vm_disks: _Optional[_Union[PreparingVMDisksStep, _Mapping]]=..., instantiating_migrated_vm: _Optional[_Union[InstantiatingMigratedVMStep, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ShuttingDownSourceVMStep(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateCloneJobRequest(_message.Message):
    __slots__ = ('parent', 'clone_job_id', 'clone_job', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLONE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CLONE_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    clone_job_id: str
    clone_job: CloneJob
    request_id: str

    def __init__(self, parent: _Optional[str]=..., clone_job_id: _Optional[str]=..., clone_job: _Optional[_Union[CloneJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class CancelCloneJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelCloneJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListCloneJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCloneJobsResponse(_message.Message):
    __slots__ = ('clone_jobs', 'next_page_token', 'unreachable')
    CLONE_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clone_jobs: _containers.RepeatedCompositeFieldContainer[CloneJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, clone_jobs: _Optional[_Iterable[_Union[CloneJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCloneJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Source(_message.Message):
    __slots__ = ('vmware', 'aws', 'name', 'create_time', 'update_time', 'labels', 'description')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VMWARE_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    vmware: VmwareSourceDetails
    aws: AwsSourceDetails
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str

    def __init__(self, vmware: _Optional[_Union[VmwareSourceDetails, _Mapping]]=..., aws: _Optional[_Union[AwsSourceDetails, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=...) -> None:
        ...

class VmwareSourceDetails(_message.Message):
    __slots__ = ('username', 'password', 'vcenter_ip', 'thumbprint')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    VCENTER_IP_FIELD_NUMBER: _ClassVar[int]
    THUMBPRINT_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    vcenter_ip: str
    thumbprint: str

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=..., vcenter_ip: _Optional[str]=..., thumbprint: _Optional[str]=...) -> None:
        ...

class AwsSourceDetails(_message.Message):
    __slots__ = ('access_key_creds', 'aws_region', 'state', 'error', 'inventory_tag_list', 'inventory_security_group_names', 'migration_resources_user_tags', 'public_ip')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AwsSourceDetails.State]
        PENDING: _ClassVar[AwsSourceDetails.State]
        FAILED: _ClassVar[AwsSourceDetails.State]
        ACTIVE: _ClassVar[AwsSourceDetails.State]
    STATE_UNSPECIFIED: AwsSourceDetails.State
    PENDING: AwsSourceDetails.State
    FAILED: AwsSourceDetails.State
    ACTIVE: AwsSourceDetails.State

    class AccessKeyCredentials(_message.Message):
        __slots__ = ('access_key_id', 'secret_access_key')
        ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        access_key_id: str
        secret_access_key: str

        def __init__(self, access_key_id: _Optional[str]=..., secret_access_key: _Optional[str]=...) -> None:
            ...

    class Tag(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MigrationResourcesUserTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ACCESS_KEY_CREDS_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_TAG_LIST_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_SECURITY_GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_RESOURCES_USER_TAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    access_key_creds: AwsSourceDetails.AccessKeyCredentials
    aws_region: str
    state: AwsSourceDetails.State
    error: _status_pb2.Status
    inventory_tag_list: _containers.RepeatedCompositeFieldContainer[AwsSourceDetails.Tag]
    inventory_security_group_names: _containers.RepeatedScalarFieldContainer[str]
    migration_resources_user_tags: _containers.ScalarMap[str, str]
    public_ip: str

    def __init__(self, access_key_creds: _Optional[_Union[AwsSourceDetails.AccessKeyCredentials, _Mapping]]=..., aws_region: _Optional[str]=..., state: _Optional[_Union[AwsSourceDetails.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., inventory_tag_list: _Optional[_Iterable[_Union[AwsSourceDetails.Tag, _Mapping]]]=..., inventory_security_group_names: _Optional[_Iterable[str]]=..., migration_resources_user_tags: _Optional[_Mapping[str, str]]=..., public_ip: _Optional[str]=...) -> None:
        ...

class DatacenterConnector(_message.Message):
    __slots__ = ('create_time', 'update_time', 'name', 'registration_id', 'service_account', 'version', 'bucket', 'state', 'state_time', 'error', 'appliance_infrastructure_version', 'appliance_software_version', 'available_versions', 'upgrade_status')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DatacenterConnector.State]
        PENDING: _ClassVar[DatacenterConnector.State]
        OFFLINE: _ClassVar[DatacenterConnector.State]
        FAILED: _ClassVar[DatacenterConnector.State]
        ACTIVE: _ClassVar[DatacenterConnector.State]
    STATE_UNSPECIFIED: DatacenterConnector.State
    PENDING: DatacenterConnector.State
    OFFLINE: DatacenterConnector.State
    FAILED: DatacenterConnector.State
    ACTIVE: DatacenterConnector.State
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_INFRASTRUCTURE_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    name: str
    registration_id: str
    service_account: str
    version: str
    bucket: str
    state: DatacenterConnector.State
    state_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    appliance_infrastructure_version: str
    appliance_software_version: str
    available_versions: AvailableUpdates
    upgrade_status: UpgradeStatus

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., registration_id: _Optional[str]=..., service_account: _Optional[str]=..., version: _Optional[str]=..., bucket: _Optional[str]=..., state: _Optional[_Union[DatacenterConnector.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., appliance_infrastructure_version: _Optional[str]=..., appliance_software_version: _Optional[str]=..., available_versions: _Optional[_Union[AvailableUpdates, _Mapping]]=..., upgrade_status: _Optional[_Union[UpgradeStatus, _Mapping]]=...) -> None:
        ...

class UpgradeStatus(_message.Message):
    __slots__ = ('version', 'state', 'error', 'start_time', 'previous_version')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[UpgradeStatus.State]
        RUNNING: _ClassVar[UpgradeStatus.State]
        FAILED: _ClassVar[UpgradeStatus.State]
        SUCCEEDED: _ClassVar[UpgradeStatus.State]
    STATE_UNSPECIFIED: UpgradeStatus.State
    RUNNING: UpgradeStatus.State
    FAILED: UpgradeStatus.State
    SUCCEEDED: UpgradeStatus.State
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    state: UpgradeStatus.State
    error: _status_pb2.Status
    start_time: _timestamp_pb2.Timestamp
    previous_version: str

    def __init__(self, version: _Optional[str]=..., state: _Optional[_Union[UpgradeStatus.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., previous_version: _Optional[str]=...) -> None:
        ...

class AvailableUpdates(_message.Message):
    __slots__ = ('new_deployable_appliance', 'in_place_update')
    NEW_DEPLOYABLE_APPLIANCE_FIELD_NUMBER: _ClassVar[int]
    IN_PLACE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    new_deployable_appliance: ApplianceVersion
    in_place_update: ApplianceVersion

    def __init__(self, new_deployable_appliance: _Optional[_Union[ApplianceVersion, _Mapping]]=..., in_place_update: _Optional[_Union[ApplianceVersion, _Mapping]]=...) -> None:
        ...

class ApplianceVersion(_message.Message):
    __slots__ = ('version', 'uri', 'critical', 'release_notes_uri')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTES_URI_FIELD_NUMBER: _ClassVar[int]
    version: str
    uri: str
    critical: bool
    release_notes_uri: str

    def __init__(self, version: _Optional[str]=..., uri: _Optional[str]=..., critical: bool=..., release_notes_uri: _Optional[str]=...) -> None:
        ...

class ListSourcesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSourcesResponse(_message.Message):
    __slots__ = ('sources', 'next_page_token', 'unreachable')
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, sources: _Optional[_Iterable[_Union[Source, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSourceRequest(_message.Message):
    __slots__ = ('parent', 'source_id', 'source', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_id: str
    source: Source
    request_id: str

    def __init__(self, parent: _Optional[str]=..., source_id: _Optional[str]=..., source: _Optional[_Union[Source, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ('update_mask', 'source', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    source: Source
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., source: _Optional[_Union[Source, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSourceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class FetchInventoryRequest(_message.Message):
    __slots__ = ('source', 'force_refresh')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    source: str
    force_refresh: bool

    def __init__(self, source: _Optional[str]=..., force_refresh: bool=...) -> None:
        ...

class VmwareVmDetails(_message.Message):
    __slots__ = ('vm_id', 'datacenter_id', 'datacenter_description', 'uuid', 'display_name', 'power_state', 'cpu_count', 'memory_mb', 'disk_count', 'committed_storage_mb', 'guest_description', 'boot_option')

    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[VmwareVmDetails.PowerState]
        ON: _ClassVar[VmwareVmDetails.PowerState]
        OFF: _ClassVar[VmwareVmDetails.PowerState]
        SUSPENDED: _ClassVar[VmwareVmDetails.PowerState]
    POWER_STATE_UNSPECIFIED: VmwareVmDetails.PowerState
    ON: VmwareVmDetails.PowerState
    OFF: VmwareVmDetails.PowerState
    SUSPENDED: VmwareVmDetails.PowerState

    class BootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOOT_OPTION_UNSPECIFIED: _ClassVar[VmwareVmDetails.BootOption]
        EFI: _ClassVar[VmwareVmDetails.BootOption]
        BIOS: _ClassVar[VmwareVmDetails.BootOption]
    BOOT_OPTION_UNSPECIFIED: VmwareVmDetails.BootOption
    EFI: VmwareVmDetails.BootOption
    BIOS: VmwareVmDetails.BootOption
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_ID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_MB_FIELD_NUMBER: _ClassVar[int]
    GUEST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    datacenter_id: str
    datacenter_description: str
    uuid: str
    display_name: str
    power_state: VmwareVmDetails.PowerState
    cpu_count: int
    memory_mb: int
    disk_count: int
    committed_storage_mb: int
    guest_description: str
    boot_option: VmwareVmDetails.BootOption

    def __init__(self, vm_id: _Optional[str]=..., datacenter_id: _Optional[str]=..., datacenter_description: _Optional[str]=..., uuid: _Optional[str]=..., display_name: _Optional[str]=..., power_state: _Optional[_Union[VmwareVmDetails.PowerState, str]]=..., cpu_count: _Optional[int]=..., memory_mb: _Optional[int]=..., disk_count: _Optional[int]=..., committed_storage_mb: _Optional[int]=..., guest_description: _Optional[str]=..., boot_option: _Optional[_Union[VmwareVmDetails.BootOption, str]]=...) -> None:
        ...

class AwsVmDetails(_message.Message):
    __slots__ = ('vm_id', 'display_name', 'source_id', 'source_description', 'power_state', 'cpu_count', 'memory_mb', 'disk_count', 'committed_storage_mb', 'os_description', 'boot_option', 'instance_type', 'vpc_id', 'security_groups', 'tags', 'zone', 'virtualization_type', 'architecture')

    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[AwsVmDetails.PowerState]
        ON: _ClassVar[AwsVmDetails.PowerState]
        OFF: _ClassVar[AwsVmDetails.PowerState]
        SUSPENDED: _ClassVar[AwsVmDetails.PowerState]
        PENDING: _ClassVar[AwsVmDetails.PowerState]
    POWER_STATE_UNSPECIFIED: AwsVmDetails.PowerState
    ON: AwsVmDetails.PowerState
    OFF: AwsVmDetails.PowerState
    SUSPENDED: AwsVmDetails.PowerState
    PENDING: AwsVmDetails.PowerState

    class BootOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOOT_OPTION_UNSPECIFIED: _ClassVar[AwsVmDetails.BootOption]
        EFI: _ClassVar[AwsVmDetails.BootOption]
        BIOS: _ClassVar[AwsVmDetails.BootOption]
    BOOT_OPTION_UNSPECIFIED: AwsVmDetails.BootOption
    EFI: AwsVmDetails.BootOption
    BIOS: AwsVmDetails.BootOption

    class VmVirtualizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM_VIRTUALIZATION_TYPE_UNSPECIFIED: _ClassVar[AwsVmDetails.VmVirtualizationType]
        HVM: _ClassVar[AwsVmDetails.VmVirtualizationType]
        PARAVIRTUAL: _ClassVar[AwsVmDetails.VmVirtualizationType]
    VM_VIRTUALIZATION_TYPE_UNSPECIFIED: AwsVmDetails.VmVirtualizationType
    HVM: AwsVmDetails.VmVirtualizationType
    PARAVIRTUAL: AwsVmDetails.VmVirtualizationType

    class VmArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM_ARCHITECTURE_UNSPECIFIED: _ClassVar[AwsVmDetails.VmArchitecture]
        I386: _ClassVar[AwsVmDetails.VmArchitecture]
        X86_64: _ClassVar[AwsVmDetails.VmArchitecture]
        ARM64: _ClassVar[AwsVmDetails.VmArchitecture]
        X86_64_MAC: _ClassVar[AwsVmDetails.VmArchitecture]
    VM_ARCHITECTURE_UNSPECIFIED: AwsVmDetails.VmArchitecture
    I386: AwsVmDetails.VmArchitecture
    X86_64: AwsVmDetails.VmArchitecture
    ARM64: AwsVmDetails.VmArchitecture
    X86_64_MAC: AwsVmDetails.VmArchitecture

    class TagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_MB_FIELD_NUMBER: _ClassVar[int]
    OS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    display_name: str
    source_id: str
    source_description: str
    power_state: AwsVmDetails.PowerState
    cpu_count: int
    memory_mb: int
    disk_count: int
    committed_storage_mb: int
    os_description: str
    boot_option: AwsVmDetails.BootOption
    instance_type: str
    vpc_id: str
    security_groups: _containers.RepeatedCompositeFieldContainer[AwsSecurityGroup]
    tags: _containers.ScalarMap[str, str]
    zone: str
    virtualization_type: AwsVmDetails.VmVirtualizationType
    architecture: AwsVmDetails.VmArchitecture

    def __init__(self, vm_id: _Optional[str]=..., display_name: _Optional[str]=..., source_id: _Optional[str]=..., source_description: _Optional[str]=..., power_state: _Optional[_Union[AwsVmDetails.PowerState, str]]=..., cpu_count: _Optional[int]=..., memory_mb: _Optional[int]=..., disk_count: _Optional[int]=..., committed_storage_mb: _Optional[int]=..., os_description: _Optional[str]=..., boot_option: _Optional[_Union[AwsVmDetails.BootOption, str]]=..., instance_type: _Optional[str]=..., vpc_id: _Optional[str]=..., security_groups: _Optional[_Iterable[_Union[AwsSecurityGroup, _Mapping]]]=..., tags: _Optional[_Mapping[str, str]]=..., zone: _Optional[str]=..., virtualization_type: _Optional[_Union[AwsVmDetails.VmVirtualizationType, str]]=..., architecture: _Optional[_Union[AwsVmDetails.VmArchitecture, str]]=...) -> None:
        ...

class AwsSecurityGroup(_message.Message):
    __slots__ = ('id', 'name')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class VmwareVmsDetails(_message.Message):
    __slots__ = ('details',)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[VmwareVmDetails]

    def __init__(self, details: _Optional[_Iterable[_Union[VmwareVmDetails, _Mapping]]]=...) -> None:
        ...

class AwsVmsDetails(_message.Message):
    __slots__ = ('details',)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[AwsVmDetails]

    def __init__(self, details: _Optional[_Iterable[_Union[AwsVmDetails, _Mapping]]]=...) -> None:
        ...

class FetchInventoryResponse(_message.Message):
    __slots__ = ('vmware_vms', 'aws_vms', 'update_time')
    VMWARE_VMS_FIELD_NUMBER: _ClassVar[int]
    AWS_VMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    vmware_vms: VmwareVmsDetails
    aws_vms: AwsVmsDetails
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, vmware_vms: _Optional[_Union[VmwareVmsDetails, _Mapping]]=..., aws_vms: _Optional[_Union[AwsVmsDetails, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UtilizationReport(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'state_time', 'error', 'create_time', 'time_frame', 'frame_end_time', 'vm_count', 'vms')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[UtilizationReport.State]
        CREATING: _ClassVar[UtilizationReport.State]
        SUCCEEDED: _ClassVar[UtilizationReport.State]
        FAILED: _ClassVar[UtilizationReport.State]
    STATE_UNSPECIFIED: UtilizationReport.State
    CREATING: UtilizationReport.State
    SUCCEEDED: UtilizationReport.State
    FAILED: UtilizationReport.State

    class TimeFrame(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_FRAME_UNSPECIFIED: _ClassVar[UtilizationReport.TimeFrame]
        WEEK: _ClassVar[UtilizationReport.TimeFrame]
        MONTH: _ClassVar[UtilizationReport.TimeFrame]
        YEAR: _ClassVar[UtilizationReport.TimeFrame]
    TIME_FRAME_UNSPECIFIED: UtilizationReport.TimeFrame
    WEEK: UtilizationReport.TimeFrame
    MONTH: UtilizationReport.TimeFrame
    YEAR: UtilizationReport.TimeFrame
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_FRAME_FIELD_NUMBER: _ClassVar[int]
    FRAME_END_TIME_FIELD_NUMBER: _ClassVar[int]
    VM_COUNT_FIELD_NUMBER: _ClassVar[int]
    VMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: UtilizationReport.State
    state_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    time_frame: UtilizationReport.TimeFrame
    frame_end_time: _timestamp_pb2.Timestamp
    vm_count: int
    vms: _containers.RepeatedCompositeFieldContainer[VmUtilizationInfo]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[UtilizationReport.State, str]]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., time_frame: _Optional[_Union[UtilizationReport.TimeFrame, str]]=..., frame_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vm_count: _Optional[int]=..., vms: _Optional[_Iterable[_Union[VmUtilizationInfo, _Mapping]]]=...) -> None:
        ...

class VmUtilizationInfo(_message.Message):
    __slots__ = ('vmware_vm_details', 'vm_id', 'utilization')
    VMWARE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    vmware_vm_details: VmwareVmDetails
    vm_id: str
    utilization: VmUtilizationMetrics

    def __init__(self, vmware_vm_details: _Optional[_Union[VmwareVmDetails, _Mapping]]=..., vm_id: _Optional[str]=..., utilization: _Optional[_Union[VmUtilizationMetrics, _Mapping]]=...) -> None:
        ...

class VmUtilizationMetrics(_message.Message):
    __slots__ = ('cpu_max_percent', 'cpu_average_percent', 'memory_max_percent', 'memory_average_percent', 'disk_io_rate_max_kbps', 'disk_io_rate_average_kbps', 'network_throughput_max_kbps', 'network_throughput_average_kbps')
    CPU_MAX_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CPU_AVERAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MAX_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_AVERAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DISK_IO_RATE_MAX_KBPS_FIELD_NUMBER: _ClassVar[int]
    DISK_IO_RATE_AVERAGE_KBPS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_THROUGHPUT_MAX_KBPS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_THROUGHPUT_AVERAGE_KBPS_FIELD_NUMBER: _ClassVar[int]
    cpu_max_percent: int
    cpu_average_percent: int
    memory_max_percent: int
    memory_average_percent: int
    disk_io_rate_max_kbps: int
    disk_io_rate_average_kbps: int
    network_throughput_max_kbps: int
    network_throughput_average_kbps: int

    def __init__(self, cpu_max_percent: _Optional[int]=..., cpu_average_percent: _Optional[int]=..., memory_max_percent: _Optional[int]=..., memory_average_percent: _Optional[int]=..., disk_io_rate_max_kbps: _Optional[int]=..., disk_io_rate_average_kbps: _Optional[int]=..., network_throughput_max_kbps: _Optional[int]=..., network_throughput_average_kbps: _Optional[int]=...) -> None:
        ...

class ListUtilizationReportsRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: UtilizationReportView
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[UtilizationReportView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListUtilizationReportsResponse(_message.Message):
    __slots__ = ('utilization_reports', 'next_page_token', 'unreachable')
    UTILIZATION_REPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    utilization_reports: _containers.RepeatedCompositeFieldContainer[UtilizationReport]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, utilization_reports: _Optional[_Iterable[_Union[UtilizationReport, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetUtilizationReportRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: UtilizationReportView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[UtilizationReportView, str]]=...) -> None:
        ...

class CreateUtilizationReportRequest(_message.Message):
    __slots__ = ('parent', 'utilization_report', 'utilization_report_id', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_REPORT_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    utilization_report: UtilizationReport
    utilization_report_id: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., utilization_report: _Optional[_Union[UtilizationReport, _Mapping]]=..., utilization_report_id: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteUtilizationReportRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListDatacenterConnectorsResponse(_message.Message):
    __slots__ = ('datacenter_connectors', 'next_page_token', 'unreachable')
    DATACENTER_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    datacenter_connectors: _containers.RepeatedCompositeFieldContainer[DatacenterConnector]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, datacenter_connectors: _Optional[_Iterable[_Union[DatacenterConnector, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDatacenterConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDatacenterConnectorRequest(_message.Message):
    __slots__ = ('parent', 'datacenter_connector_id', 'datacenter_connector', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    datacenter_connector_id: str
    datacenter_connector: DatacenterConnector
    request_id: str

    def __init__(self, parent: _Optional[str]=..., datacenter_connector_id: _Optional[str]=..., datacenter_connector: _Optional[_Union[DatacenterConnector, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteDatacenterConnectorRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpgradeApplianceRequest(_message.Message):
    __slots__ = ('datacenter_connector', 'request_id')
    DATACENTER_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    datacenter_connector: str
    request_id: str

    def __init__(self, datacenter_connector: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpgradeApplianceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListDatacenterConnectorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ComputeEngineTargetDefaults(_message.Message):
    __slots__ = ('vm_name', 'target_project', 'zone', 'machine_type_series', 'machine_type', 'network_tags', 'network_interfaces', 'service_account', 'disk_type', 'labels', 'license_type', 'applied_license', 'compute_scheduling', 'secure_boot', 'boot_option', 'metadata', 'additional_licenses', 'hostname')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_SERIES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LICENSE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    target_project: str
    zone: str
    machine_type_series: str
    machine_type: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    service_account: str
    disk_type: ComputeEngineDiskType
    labels: _containers.ScalarMap[str, str]
    license_type: ComputeEngineLicenseType
    applied_license: AppliedLicense
    compute_scheduling: ComputeScheduling
    secure_boot: bool
    boot_option: ComputeEngineBootOption
    metadata: _containers.ScalarMap[str, str]
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    hostname: str

    def __init__(self, vm_name: _Optional[str]=..., target_project: _Optional[str]=..., zone: _Optional[str]=..., machine_type_series: _Optional[str]=..., machine_type: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=..., service_account: _Optional[str]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=..., labels: _Optional[_Mapping[str, str]]=..., license_type: _Optional[_Union[ComputeEngineLicenseType, str]]=..., applied_license: _Optional[_Union[AppliedLicense, _Mapping]]=..., compute_scheduling: _Optional[_Union[ComputeScheduling, _Mapping]]=..., secure_boot: bool=..., boot_option: _Optional[_Union[ComputeEngineBootOption, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., additional_licenses: _Optional[_Iterable[str]]=..., hostname: _Optional[str]=...) -> None:
        ...

class ComputeEngineTargetDetails(_message.Message):
    __slots__ = ('vm_name', 'project', 'zone', 'machine_type_series', 'machine_type', 'network_tags', 'network_interfaces', 'service_account', 'disk_type', 'labels', 'license_type', 'applied_license', 'compute_scheduling', 'secure_boot', 'boot_option', 'metadata', 'additional_licenses', 'hostname')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_SERIES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LICENSE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    BOOT_OPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    project: str
    zone: str
    machine_type_series: str
    machine_type: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    service_account: str
    disk_type: ComputeEngineDiskType
    labels: _containers.ScalarMap[str, str]
    license_type: ComputeEngineLicenseType
    applied_license: AppliedLicense
    compute_scheduling: ComputeScheduling
    secure_boot: bool
    boot_option: ComputeEngineBootOption
    metadata: _containers.ScalarMap[str, str]
    additional_licenses: _containers.RepeatedScalarFieldContainer[str]
    hostname: str

    def __init__(self, vm_name: _Optional[str]=..., project: _Optional[str]=..., zone: _Optional[str]=..., machine_type_series: _Optional[str]=..., machine_type: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=..., service_account: _Optional[str]=..., disk_type: _Optional[_Union[ComputeEngineDiskType, str]]=..., labels: _Optional[_Mapping[str, str]]=..., license_type: _Optional[_Union[ComputeEngineLicenseType, str]]=..., applied_license: _Optional[_Union[AppliedLicense, _Mapping]]=..., compute_scheduling: _Optional[_Union[ComputeScheduling, _Mapping]]=..., secure_boot: bool=..., boot_option: _Optional[_Union[ComputeEngineBootOption, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., additional_licenses: _Optional[_Iterable[str]]=..., hostname: _Optional[str]=...) -> None:
        ...

class NetworkInterface(_message.Message):
    __slots__ = ('network', 'subnetwork', 'internal_ip', 'external_ip')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str
    internal_ip: str
    external_ip: str

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=..., internal_ip: _Optional[str]=..., external_ip: _Optional[str]=...) -> None:
        ...

class AppliedLicense(_message.Message):
    __slots__ = ('type', 'os_license')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AppliedLicense.Type]
        NONE: _ClassVar[AppliedLicense.Type]
        PAYG: _ClassVar[AppliedLicense.Type]
        BYOL: _ClassVar[AppliedLicense.Type]
    TYPE_UNSPECIFIED: AppliedLicense.Type
    NONE: AppliedLicense.Type
    PAYG: AppliedLicense.Type
    BYOL: AppliedLicense.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_LICENSE_FIELD_NUMBER: _ClassVar[int]
    type: AppliedLicense.Type
    os_license: str

    def __init__(self, type: _Optional[_Union[AppliedLicense.Type, str]]=..., os_license: _Optional[str]=...) -> None:
        ...

class SchedulingNodeAffinity(_message.Message):
    __slots__ = ('key', 'operator', 'values')

    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[SchedulingNodeAffinity.Operator]
        IN: _ClassVar[SchedulingNodeAffinity.Operator]
        NOT_IN: _ClassVar[SchedulingNodeAffinity.Operator]
    OPERATOR_UNSPECIFIED: SchedulingNodeAffinity.Operator
    IN: SchedulingNodeAffinity.Operator
    NOT_IN: SchedulingNodeAffinity.Operator
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: SchedulingNodeAffinity.Operator
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, key: _Optional[str]=..., operator: _Optional[_Union[SchedulingNodeAffinity.Operator, str]]=..., values: _Optional[_Iterable[str]]=...) -> None:
        ...

class ComputeScheduling(_message.Message):
    __slots__ = ('on_host_maintenance', 'restart_type', 'node_affinities', 'min_node_cpus')

    class OnHostMaintenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ON_HOST_MAINTENANCE_UNSPECIFIED: _ClassVar[ComputeScheduling.OnHostMaintenance]
        TERMINATE: _ClassVar[ComputeScheduling.OnHostMaintenance]
        MIGRATE: _ClassVar[ComputeScheduling.OnHostMaintenance]
    ON_HOST_MAINTENANCE_UNSPECIFIED: ComputeScheduling.OnHostMaintenance
    TERMINATE: ComputeScheduling.OnHostMaintenance
    MIGRATE: ComputeScheduling.OnHostMaintenance

    class RestartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTART_TYPE_UNSPECIFIED: _ClassVar[ComputeScheduling.RestartType]
        AUTOMATIC_RESTART: _ClassVar[ComputeScheduling.RestartType]
        NO_AUTOMATIC_RESTART: _ClassVar[ComputeScheduling.RestartType]
    RESTART_TYPE_UNSPECIFIED: ComputeScheduling.RestartType
    AUTOMATIC_RESTART: ComputeScheduling.RestartType
    NO_AUTOMATIC_RESTART: ComputeScheduling.RestartType
    ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    RESTART_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_AFFINITIES_FIELD_NUMBER: _ClassVar[int]
    MIN_NODE_CPUS_FIELD_NUMBER: _ClassVar[int]
    on_host_maintenance: ComputeScheduling.OnHostMaintenance
    restart_type: ComputeScheduling.RestartType
    node_affinities: _containers.RepeatedCompositeFieldContainer[SchedulingNodeAffinity]
    min_node_cpus: int

    def __init__(self, on_host_maintenance: _Optional[_Union[ComputeScheduling.OnHostMaintenance, str]]=..., restart_type: _Optional[_Union[ComputeScheduling.RestartType, str]]=..., node_affinities: _Optional[_Iterable[_Union[SchedulingNodeAffinity, _Mapping]]]=..., min_node_cpus: _Optional[int]=...) -> None:
        ...

class SchedulePolicy(_message.Message):
    __slots__ = ('idle_duration', 'skip_os_adaptation')
    IDLE_DURATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_OS_ADAPTATION_FIELD_NUMBER: _ClassVar[int]
    idle_duration: _duration_pb2.Duration
    skip_os_adaptation: bool

    def __init__(self, idle_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., skip_os_adaptation: bool=...) -> None:
        ...

class CreateMigratingVmRequest(_message.Message):
    __slots__ = ('parent', 'migrating_vm_id', 'migrating_vm', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    migrating_vm_id: str
    migrating_vm: MigratingVm
    request_id: str

    def __init__(self, parent: _Optional[str]=..., migrating_vm_id: _Optional[str]=..., migrating_vm: _Optional[_Union[MigratingVm, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListMigratingVmsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: MigratingVmView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[MigratingVmView, str]]=...) -> None:
        ...

class ListMigratingVmsResponse(_message.Message):
    __slots__ = ('migrating_vms', 'next_page_token', 'unreachable')
    MIGRATING_VMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    migrating_vms: _containers.RepeatedCompositeFieldContainer[MigratingVm]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, migrating_vms: _Optional[_Iterable[_Union[MigratingVm, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMigratingVmRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: MigratingVmView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[MigratingVmView, str]]=...) -> None:
        ...

class UpdateMigratingVmRequest(_message.Message):
    __slots__ = ('update_mask', 'migrating_vm', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    migrating_vm: MigratingVm
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., migrating_vm: _Optional[_Union[MigratingVm, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteMigratingVmRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class StartMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PauseMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class PauseMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResumeMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class ResumeMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FinalizeMigrationRequest(_message.Message):
    __slots__ = ('migrating_vm',)
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    migrating_vm: str

    def __init__(self, migrating_vm: _Optional[str]=...) -> None:
        ...

class FinalizeMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TargetProject(_message.Message):
    __slots__ = ('name', 'project', 'description', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., project: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetTargetProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTargetProjectsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListTargetProjectsResponse(_message.Message):
    __slots__ = ('target_projects', 'next_page_token', 'unreachable')
    TARGET_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    target_projects: _containers.RepeatedCompositeFieldContainer[TargetProject]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, target_projects: _Optional[_Iterable[_Union[TargetProject, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateTargetProjectRequest(_message.Message):
    __slots__ = ('parent', 'target_project_id', 'target_project', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    target_project_id: str
    target_project: TargetProject
    request_id: str

    def __init__(self, parent: _Optional[str]=..., target_project_id: _Optional[str]=..., target_project: _Optional[_Union[TargetProject, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateTargetProjectRequest(_message.Message):
    __slots__ = ('update_mask', 'target_project', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    target_project: TargetProject
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., target_project: _Optional[_Union[TargetProject, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteTargetProjectRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'description', 'display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class ListGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListGroupsResponse(_message.Message):
    __slots__ = ('groups', 'next_page_token', 'unreachable')
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateGroupRequest(_message.Message):
    __slots__ = ('parent', 'group_id', 'group', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    group_id: str
    group: Group
    request_id: str

    def __init__(self, parent: _Optional[str]=..., group_id: _Optional[str]=..., group: _Optional[_Union[Group, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ('update_mask', 'group', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    group: Group
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., group: _Optional[_Union[Group, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class AddGroupMigrationRequest(_message.Message):
    __slots__ = ('group', 'migrating_vm')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    group: str
    migrating_vm: str

    def __init__(self, group: _Optional[str]=..., migrating_vm: _Optional[str]=...) -> None:
        ...

class AddGroupMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemoveGroupMigrationRequest(_message.Message):
    __slots__ = ('group', 'migrating_vm')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MIGRATING_VM_FIELD_NUMBER: _ClassVar[int]
    group: str
    migrating_vm: str

    def __init__(self, group: _Optional[str]=..., migrating_vm: _Optional[str]=...) -> None:
        ...

class RemoveGroupMigrationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateCutoverJobRequest(_message.Message):
    __slots__ = ('parent', 'cutover_job_id', 'cutover_job', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUTOVER_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CUTOVER_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cutover_job_id: str
    cutover_job: CutoverJob
    request_id: str

    def __init__(self, parent: _Optional[str]=..., cutover_job_id: _Optional[str]=..., cutover_job: _Optional[_Union[CutoverJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class CancelCutoverJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelCutoverJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListCutoverJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCutoverJobsResponse(_message.Message):
    __slots__ = ('cutover_jobs', 'next_page_token', 'unreachable')
    CUTOVER_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    cutover_jobs: _containers.RepeatedCompositeFieldContainer[CutoverJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cutover_jobs: _Optional[_Iterable[_Union[CutoverJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCutoverJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class MigrationError(_message.Message):
    __slots__ = ('code', 'error_message', 'action_item', 'help_links', 'error_time')

    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[MigrationError.ErrorCode]
        UNKNOWN_ERROR: _ClassVar[MigrationError.ErrorCode]
        SOURCE_VALIDATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        SOURCE_REPLICATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        TARGET_REPLICATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        OS_ADAPTATION_ERROR: _ClassVar[MigrationError.ErrorCode]
        CLONE_ERROR: _ClassVar[MigrationError.ErrorCode]
        CUTOVER_ERROR: _ClassVar[MigrationError.ErrorCode]
        UTILIZATION_REPORT_ERROR: _ClassVar[MigrationError.ErrorCode]
        APPLIANCE_UPGRADE_ERROR: _ClassVar[MigrationError.ErrorCode]
    ERROR_CODE_UNSPECIFIED: MigrationError.ErrorCode
    UNKNOWN_ERROR: MigrationError.ErrorCode
    SOURCE_VALIDATION_ERROR: MigrationError.ErrorCode
    SOURCE_REPLICATION_ERROR: MigrationError.ErrorCode
    TARGET_REPLICATION_ERROR: MigrationError.ErrorCode
    OS_ADAPTATION_ERROR: MigrationError.ErrorCode
    CLONE_ERROR: MigrationError.ErrorCode
    CUTOVER_ERROR: MigrationError.ErrorCode
    UTILIZATION_REPORT_ERROR: MigrationError.ErrorCode
    APPLIANCE_UPGRADE_ERROR: MigrationError.ErrorCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
    HELP_LINKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    code: MigrationError.ErrorCode
    error_message: _error_details_pb2.LocalizedMessage
    action_item: _error_details_pb2.LocalizedMessage
    help_links: _containers.RepeatedCompositeFieldContainer[_error_details_pb2.Help.Link]
    error_time: _timestamp_pb2.Timestamp

    def __init__(self, code: _Optional[_Union[MigrationError.ErrorCode, str]]=..., error_message: _Optional[_Union[_error_details_pb2.LocalizedMessage, _Mapping]]=..., action_item: _Optional[_Union[_error_details_pb2.LocalizedMessage, _Mapping]]=..., help_links: _Optional[_Iterable[_Union[_error_details_pb2.Help.Link, _Mapping]]]=..., error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AwsSourceVmDetails(_message.Message):
    __slots__ = ('firmware', 'committed_storage_bytes')

    class Firmware(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRMWARE_UNSPECIFIED: _ClassVar[AwsSourceVmDetails.Firmware]
        EFI: _ClassVar[AwsSourceVmDetails.Firmware]
        BIOS: _ClassVar[AwsSourceVmDetails.Firmware]
    FIRMWARE_UNSPECIFIED: AwsSourceVmDetails.Firmware
    EFI: AwsSourceVmDetails.Firmware
    BIOS: AwsSourceVmDetails.Firmware
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    firmware: AwsSourceVmDetails.Firmware
    committed_storage_bytes: int

    def __init__(self, firmware: _Optional[_Union[AwsSourceVmDetails.Firmware, str]]=..., committed_storage_bytes: _Optional[int]=...) -> None:
        ...

class ListReplicationCyclesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListReplicationCyclesResponse(_message.Message):
    __slots__ = ('replication_cycles', 'next_page_token', 'unreachable')
    REPLICATION_CYCLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    replication_cycles: _containers.RepeatedCompositeFieldContainer[ReplicationCycle]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, replication_cycles: _Optional[_Iterable[_Union[ReplicationCycle, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReplicationCycleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...