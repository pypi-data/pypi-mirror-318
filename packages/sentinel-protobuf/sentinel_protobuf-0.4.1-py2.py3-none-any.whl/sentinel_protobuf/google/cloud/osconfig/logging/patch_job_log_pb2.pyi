from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PatchJobCompletedLog(_message.Message):
    __slots__ = ('patch_job', 'state', 'instance_details_summary', 'dry_run', 'error_message', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PatchJobCompletedLog.State]
        STARTED: _ClassVar[PatchJobCompletedLog.State]
        INSTANCE_LOOKUP: _ClassVar[PatchJobCompletedLog.State]
        PATCHING: _ClassVar[PatchJobCompletedLog.State]
        SUCCEEDED: _ClassVar[PatchJobCompletedLog.State]
        COMPLETED_WITH_ERRORS: _ClassVar[PatchJobCompletedLog.State]
        CANCELED: _ClassVar[PatchJobCompletedLog.State]
        TIMED_OUT: _ClassVar[PatchJobCompletedLog.State]
    STATE_UNSPECIFIED: PatchJobCompletedLog.State
    STARTED: PatchJobCompletedLog.State
    INSTANCE_LOOKUP: PatchJobCompletedLog.State
    PATCHING: PatchJobCompletedLog.State
    SUCCEEDED: PatchJobCompletedLog.State
    COMPLETED_WITH_ERRORS: PatchJobCompletedLog.State
    CANCELED: PatchJobCompletedLog.State
    TIMED_OUT: PatchJobCompletedLog.State

    class InstanceDetailsSummary(_message.Message):
        __slots__ = ('instances_pending', 'instances_inactive', 'instances_notified', 'instances_started', 'instances_downloading_patches', 'instances_applying_patches', 'instances_rebooting', 'instances_succeeded', 'instances_succeeded_reboot_required', 'instances_failed', 'instances_acked', 'instances_timed_out', 'instances_running_pre_patch_step', 'instances_running_post_patch_step')
        INSTANCES_PENDING_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_INACTIVE_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_STARTED_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_DOWNLOADING_PATCHES_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_APPLYING_PATCHES_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_REBOOTING_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_SUCCEEDED_REBOOT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_FAILED_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_ACKED_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_RUNNING_PRE_PATCH_STEP_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_RUNNING_POST_PATCH_STEP_FIELD_NUMBER: _ClassVar[int]
        instances_pending: int
        instances_inactive: int
        instances_notified: int
        instances_started: int
        instances_downloading_patches: int
        instances_applying_patches: int
        instances_rebooting: int
        instances_succeeded: int
        instances_succeeded_reboot_required: int
        instances_failed: int
        instances_acked: int
        instances_timed_out: int
        instances_running_pre_patch_step: int
        instances_running_post_patch_step: int

        def __init__(self, instances_pending: _Optional[int]=..., instances_inactive: _Optional[int]=..., instances_notified: _Optional[int]=..., instances_started: _Optional[int]=..., instances_downloading_patches: _Optional[int]=..., instances_applying_patches: _Optional[int]=..., instances_rebooting: _Optional[int]=..., instances_succeeded: _Optional[int]=..., instances_succeeded_reboot_required: _Optional[int]=..., instances_failed: _Optional[int]=..., instances_acked: _Optional[int]=..., instances_timed_out: _Optional[int]=..., instances_running_pre_patch_step: _Optional[int]=..., instances_running_post_patch_step: _Optional[int]=...) -> None:
            ...
    PATCH_JOB_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_DETAILS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    patch_job: str
    state: PatchJobCompletedLog.State
    instance_details_summary: PatchJobCompletedLog.InstanceDetailsSummary
    dry_run: bool
    error_message: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, patch_job: _Optional[str]=..., state: _Optional[_Union[PatchJobCompletedLog.State, str]]=..., instance_details_summary: _Optional[_Union[PatchJobCompletedLog.InstanceDetailsSummary, _Mapping]]=..., dry_run: bool=..., error_message: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...