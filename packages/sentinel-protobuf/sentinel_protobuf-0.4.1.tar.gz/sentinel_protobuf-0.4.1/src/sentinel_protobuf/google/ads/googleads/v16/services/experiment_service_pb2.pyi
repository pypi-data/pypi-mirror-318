from google.ads.googleads.v16.resources import experiment_pb2 as _experiment_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateExperimentsRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[ExperimentOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[ExperimentOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...

class ExperimentOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _experiment_pb2.Experiment
    update: _experiment_pb2.Experiment
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_experiment_pb2.Experiment, _Mapping]] = ..., update: _Optional[_Union[_experiment_pb2.Experiment, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateExperimentsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateExperimentResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[MutateExperimentResult, _Mapping]]] = ...) -> None: ...

class MutateExperimentResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class EndExperimentRequest(_message.Message):
    __slots__ = ("experiment", "validate_only")
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    experiment: str
    validate_only: bool
    def __init__(self, experiment: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ListExperimentAsyncErrorsRequest(_message.Message):
    __slots__ = ("resource_name", "page_token", "page_size")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    page_token: str
    page_size: int
    def __init__(self, resource_name: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListExperimentAsyncErrorsResponse(_message.Message):
    __slots__ = ("errors", "next_page_token")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    next_page_token: str
    def __init__(self, errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GraduateExperimentRequest(_message.Message):
    __slots__ = ("experiment", "campaign_budget_mappings", "validate_only")
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    experiment: str
    campaign_budget_mappings: _containers.RepeatedCompositeFieldContainer[CampaignBudgetMapping]
    validate_only: bool
    def __init__(self, experiment: _Optional[str] = ..., campaign_budget_mappings: _Optional[_Iterable[_Union[CampaignBudgetMapping, _Mapping]]] = ..., validate_only: bool = ...) -> None: ...

class CampaignBudgetMapping(_message.Message):
    __slots__ = ("experiment_campaign", "campaign_budget")
    EXPERIMENT_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    experiment_campaign: str
    campaign_budget: str
    def __init__(self, experiment_campaign: _Optional[str] = ..., campaign_budget: _Optional[str] = ...) -> None: ...

class ScheduleExperimentRequest(_message.Message):
    __slots__ = ("resource_name", "validate_only")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    validate_only: bool
    def __init__(self, resource_name: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ScheduleExperimentMetadata(_message.Message):
    __slots__ = ("experiment",)
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    experiment: str
    def __init__(self, experiment: _Optional[str] = ...) -> None: ...

class PromoteExperimentRequest(_message.Message):
    __slots__ = ("resource_name", "validate_only")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    validate_only: bool
    def __init__(self, resource_name: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class PromoteExperimentMetadata(_message.Message):
    __slots__ = ("experiment",)
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    experiment: str
    def __init__(self, experiment: _Optional[str] = ...) -> None: ...
