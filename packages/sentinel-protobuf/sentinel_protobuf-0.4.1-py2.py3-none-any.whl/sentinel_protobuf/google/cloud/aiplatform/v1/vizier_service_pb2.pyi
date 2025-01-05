from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1 import study_pb2 as _study_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStudyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateStudyRequest(_message.Message):
    __slots__ = ("parent", "study")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STUDY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    study: _study_pb2.Study
    def __init__(self, parent: _Optional[str] = ..., study: _Optional[_Union[_study_pb2.Study, _Mapping]] = ...) -> None: ...

class ListStudiesRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListStudiesResponse(_message.Message):
    __slots__ = ("studies", "next_page_token")
    STUDIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    studies: _containers.RepeatedCompositeFieldContainer[_study_pb2.Study]
    next_page_token: str
    def __init__(self, studies: _Optional[_Iterable[_Union[_study_pb2.Study, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteStudyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LookupStudyRequest(_message.Message):
    __slots__ = ("parent", "display_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_name: str
    def __init__(self, parent: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class SuggestTrialsRequest(_message.Message):
    __slots__ = ("parent", "suggestion_count", "client_id", "contexts")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    suggestion_count: int
    client_id: str
    contexts: _containers.RepeatedCompositeFieldContainer[_study_pb2.TrialContext]
    def __init__(self, parent: _Optional[str] = ..., suggestion_count: _Optional[int] = ..., client_id: _Optional[str] = ..., contexts: _Optional[_Iterable[_Union[_study_pb2.TrialContext, _Mapping]]] = ...) -> None: ...

class SuggestTrialsResponse(_message.Message):
    __slots__ = ("trials", "study_state", "start_time", "end_time")
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    STUDY_STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    trials: _containers.RepeatedCompositeFieldContainer[_study_pb2.Trial]
    study_state: _study_pb2.Study.State
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, trials: _Optional[_Iterable[_Union[_study_pb2.Trial, _Mapping]]] = ..., study_state: _Optional[_Union[_study_pb2.Study.State, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SuggestTrialsMetadata(_message.Message):
    __slots__ = ("generic_metadata", "client_id")
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    client_id: str
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., client_id: _Optional[str] = ...) -> None: ...

class CreateTrialRequest(_message.Message):
    __slots__ = ("parent", "trial")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    trial: _study_pb2.Trial
    def __init__(self, parent: _Optional[str] = ..., trial: _Optional[_Union[_study_pb2.Trial, _Mapping]] = ...) -> None: ...

class GetTrialRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTrialsRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListTrialsResponse(_message.Message):
    __slots__ = ("trials", "next_page_token")
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    trials: _containers.RepeatedCompositeFieldContainer[_study_pb2.Trial]
    next_page_token: str
    def __init__(self, trials: _Optional[_Iterable[_Union[_study_pb2.Trial, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddTrialMeasurementRequest(_message.Message):
    __slots__ = ("trial_name", "measurement")
    TRIAL_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    trial_name: str
    measurement: _study_pb2.Measurement
    def __init__(self, trial_name: _Optional[str] = ..., measurement: _Optional[_Union[_study_pb2.Measurement, _Mapping]] = ...) -> None: ...

class CompleteTrialRequest(_message.Message):
    __slots__ = ("name", "final_measurement", "trial_infeasible", "infeasible_reason")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FINAL_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    TRIAL_INFEASIBLE_FIELD_NUMBER: _ClassVar[int]
    INFEASIBLE_REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    final_measurement: _study_pb2.Measurement
    trial_infeasible: bool
    infeasible_reason: str
    def __init__(self, name: _Optional[str] = ..., final_measurement: _Optional[_Union[_study_pb2.Measurement, _Mapping]] = ..., trial_infeasible: bool = ..., infeasible_reason: _Optional[str] = ...) -> None: ...

class DeleteTrialRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CheckTrialEarlyStoppingStateRequest(_message.Message):
    __slots__ = ("trial_name",)
    TRIAL_NAME_FIELD_NUMBER: _ClassVar[int]
    trial_name: str
    def __init__(self, trial_name: _Optional[str] = ...) -> None: ...

class CheckTrialEarlyStoppingStateResponse(_message.Message):
    __slots__ = ("should_stop",)
    SHOULD_STOP_FIELD_NUMBER: _ClassVar[int]
    should_stop: bool
    def __init__(self, should_stop: bool = ...) -> None: ...

class CheckTrialEarlyStoppingStateMetatdata(_message.Message):
    __slots__ = ("generic_metadata", "study", "trial")
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    STUDY_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    study: str
    trial: str
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ..., study: _Optional[str] = ..., trial: _Optional[str] = ...) -> None: ...

class StopTrialRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListOptimalTrialsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListOptimalTrialsResponse(_message.Message):
    __slots__ = ("optimal_trials",)
    OPTIMAL_TRIALS_FIELD_NUMBER: _ClassVar[int]
    optimal_trials: _containers.RepeatedCompositeFieldContainer[_study_pb2.Trial]
    def __init__(self, optimal_trials: _Optional[_Iterable[_Union[_study_pb2.Trial, _Mapping]]] = ...) -> None: ...
