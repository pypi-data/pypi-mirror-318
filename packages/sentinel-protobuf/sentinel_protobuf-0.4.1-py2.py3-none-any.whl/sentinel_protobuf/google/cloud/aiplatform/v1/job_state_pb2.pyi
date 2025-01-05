from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class JobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_STATE_UNSPECIFIED: _ClassVar[JobState]
    JOB_STATE_QUEUED: _ClassVar[JobState]
    JOB_STATE_PENDING: _ClassVar[JobState]
    JOB_STATE_RUNNING: _ClassVar[JobState]
    JOB_STATE_SUCCEEDED: _ClassVar[JobState]
    JOB_STATE_FAILED: _ClassVar[JobState]
    JOB_STATE_CANCELLING: _ClassVar[JobState]
    JOB_STATE_CANCELLED: _ClassVar[JobState]
    JOB_STATE_PAUSED: _ClassVar[JobState]
    JOB_STATE_EXPIRED: _ClassVar[JobState]
    JOB_STATE_UPDATING: _ClassVar[JobState]
    JOB_STATE_PARTIALLY_SUCCEEDED: _ClassVar[JobState]
JOB_STATE_UNSPECIFIED: JobState
JOB_STATE_QUEUED: JobState
JOB_STATE_PENDING: JobState
JOB_STATE_RUNNING: JobState
JOB_STATE_SUCCEEDED: JobState
JOB_STATE_FAILED: JobState
JOB_STATE_CANCELLING: JobState
JOB_STATE_CANCELLED: JobState
JOB_STATE_PAUSED: JobState
JOB_STATE_EXPIRED: JobState
JOB_STATE_UPDATING: JobState
JOB_STATE_PARTIALLY_SUCCEEDED: JobState