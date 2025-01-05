from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import custom_job_pb2 as _custom_job_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1 import study_pb2 as _study_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HyperparameterTuningJob(_message.Message):
    __slots__ = ("name", "display_name", "study_spec", "max_trial_count", "parallel_trial_count", "max_failed_trial_count", "trial_job_spec", "trials", "state", "create_time", "start_time", "end_time", "update_time", "error", "labels", "encryption_spec", "satisfies_pzs", "satisfies_pzi")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STUDY_SPEC_FIELD_NUMBER: _ClassVar[int]
    MAX_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_FAILED_TRIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIAL_JOB_SPEC_FIELD_NUMBER: _ClassVar[int]
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    study_spec: _study_pb2.StudySpec
    max_trial_count: int
    parallel_trial_count: int
    max_failed_trial_count: int
    trial_job_spec: _custom_job_pb2.CustomJobSpec
    trials: _containers.RepeatedCompositeFieldContainer[_study_pb2.Trial]
    state: _job_state_pb2.JobState
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., study_spec: _Optional[_Union[_study_pb2.StudySpec, _Mapping]] = ..., max_trial_count: _Optional[int] = ..., parallel_trial_count: _Optional[int] = ..., max_failed_trial_count: _Optional[int] = ..., trial_job_spec: _Optional[_Union[_custom_job_pb2.CustomJobSpec, _Mapping]] = ..., trials: _Optional[_Iterable[_Union[_study_pb2.Trial, _Mapping]]] = ..., state: _Optional[_Union[_job_state_pb2.JobState, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...
