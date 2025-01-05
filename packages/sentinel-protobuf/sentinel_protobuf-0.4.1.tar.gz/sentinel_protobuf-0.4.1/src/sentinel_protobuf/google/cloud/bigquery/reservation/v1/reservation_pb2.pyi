from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Edition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDITION_UNSPECIFIED: _ClassVar[Edition]
    STANDARD: _ClassVar[Edition]
    ENTERPRISE: _ClassVar[Edition]
    ENTERPRISE_PLUS: _ClassVar[Edition]
EDITION_UNSPECIFIED: Edition
STANDARD: Edition
ENTERPRISE: Edition
ENTERPRISE_PLUS: Edition

class Reservation(_message.Message):
    __slots__ = ('name', 'slot_capacity', 'ignore_idle_slots', 'autoscale', 'concurrency', 'creation_time', 'update_time', 'multi_region_auxiliary', 'edition', 'primary_location', 'secondary_location', 'original_primary_location')

    class Autoscale(_message.Message):
        __slots__ = ('current_slots', 'max_slots')
        CURRENT_SLOTS_FIELD_NUMBER: _ClassVar[int]
        MAX_SLOTS_FIELD_NUMBER: _ClassVar[int]
        current_slots: int
        max_slots: int

        def __init__(self, current_slots: _Optional[int]=..., max_slots: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLOT_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    IGNORE_IDLE_SLOTS_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_AUXILIARY_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PRIMARY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    slot_capacity: int
    ignore_idle_slots: bool
    autoscale: Reservation.Autoscale
    concurrency: int
    creation_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    multi_region_auxiliary: bool
    edition: Edition
    primary_location: str
    secondary_location: str
    original_primary_location: str

    def __init__(self, name: _Optional[str]=..., slot_capacity: _Optional[int]=..., ignore_idle_slots: bool=..., autoscale: _Optional[_Union[Reservation.Autoscale, _Mapping]]=..., concurrency: _Optional[int]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., multi_region_auxiliary: bool=..., edition: _Optional[_Union[Edition, str]]=..., primary_location: _Optional[str]=..., secondary_location: _Optional[str]=..., original_primary_location: _Optional[str]=...) -> None:
        ...

class CapacityCommitment(_message.Message):
    __slots__ = ('name', 'slot_count', 'plan', 'state', 'commitment_start_time', 'commitment_end_time', 'failure_status', 'renewal_plan', 'multi_region_auxiliary', 'edition', 'is_flat_rate')

    class CommitmentPlan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMITMENT_PLAN_UNSPECIFIED: _ClassVar[CapacityCommitment.CommitmentPlan]
        FLEX: _ClassVar[CapacityCommitment.CommitmentPlan]
        FLEX_FLAT_RATE: _ClassVar[CapacityCommitment.CommitmentPlan]
        TRIAL: _ClassVar[CapacityCommitment.CommitmentPlan]
        MONTHLY: _ClassVar[CapacityCommitment.CommitmentPlan]
        MONTHLY_FLAT_RATE: _ClassVar[CapacityCommitment.CommitmentPlan]
        ANNUAL: _ClassVar[CapacityCommitment.CommitmentPlan]
        ANNUAL_FLAT_RATE: _ClassVar[CapacityCommitment.CommitmentPlan]
        THREE_YEAR: _ClassVar[CapacityCommitment.CommitmentPlan]
        NONE: _ClassVar[CapacityCommitment.CommitmentPlan]
    COMMITMENT_PLAN_UNSPECIFIED: CapacityCommitment.CommitmentPlan
    FLEX: CapacityCommitment.CommitmentPlan
    FLEX_FLAT_RATE: CapacityCommitment.CommitmentPlan
    TRIAL: CapacityCommitment.CommitmentPlan
    MONTHLY: CapacityCommitment.CommitmentPlan
    MONTHLY_FLAT_RATE: CapacityCommitment.CommitmentPlan
    ANNUAL: CapacityCommitment.CommitmentPlan
    ANNUAL_FLAT_RATE: CapacityCommitment.CommitmentPlan
    THREE_YEAR: CapacityCommitment.CommitmentPlan
    NONE: CapacityCommitment.CommitmentPlan

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CapacityCommitment.State]
        PENDING: _ClassVar[CapacityCommitment.State]
        ACTIVE: _ClassVar[CapacityCommitment.State]
        FAILED: _ClassVar[CapacityCommitment.State]
    STATE_UNSPECIFIED: CapacityCommitment.State
    PENDING: CapacityCommitment.State
    ACTIVE: CapacityCommitment.State
    FAILED: CapacityCommitment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLOT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STATUS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PLAN_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_AUXILIARY_FIELD_NUMBER: _ClassVar[int]
    EDITION_FIELD_NUMBER: _ClassVar[int]
    IS_FLAT_RATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    slot_count: int
    plan: CapacityCommitment.CommitmentPlan
    state: CapacityCommitment.State
    commitment_start_time: _timestamp_pb2.Timestamp
    commitment_end_time: _timestamp_pb2.Timestamp
    failure_status: _status_pb2.Status
    renewal_plan: CapacityCommitment.CommitmentPlan
    multi_region_auxiliary: bool
    edition: Edition
    is_flat_rate: bool

    def __init__(self, name: _Optional[str]=..., slot_count: _Optional[int]=..., plan: _Optional[_Union[CapacityCommitment.CommitmentPlan, str]]=..., state: _Optional[_Union[CapacityCommitment.State, str]]=..., commitment_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., commitment_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., failure_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., renewal_plan: _Optional[_Union[CapacityCommitment.CommitmentPlan, str]]=..., multi_region_auxiliary: bool=..., edition: _Optional[_Union[Edition, str]]=..., is_flat_rate: bool=...) -> None:
        ...

class CreateReservationRequest(_message.Message):
    __slots__ = ('parent', 'reservation_id', 'reservation')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reservation_id: str
    reservation: Reservation

    def __init__(self, parent: _Optional[str]=..., reservation_id: _Optional[str]=..., reservation: _Optional[_Union[Reservation, _Mapping]]=...) -> None:
        ...

class ListReservationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReservationsResponse(_message.Message):
    __slots__ = ('reservations', 'next_page_token')
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reservations: _containers.RepeatedCompositeFieldContainer[Reservation]
    next_page_token: str

    def __init__(self, reservations: _Optional[_Iterable[_Union[Reservation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetReservationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteReservationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateReservationRequest(_message.Message):
    __slots__ = ('reservation', 'update_mask')
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    reservation: Reservation
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, reservation: _Optional[_Union[Reservation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class FailoverReservationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCapacityCommitmentRequest(_message.Message):
    __slots__ = ('parent', 'capacity_commitment', 'enforce_single_admin_project_per_org', 'capacity_commitment_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_SINGLE_ADMIN_PROJECT_PER_ORG_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_COMMITMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    capacity_commitment: CapacityCommitment
    enforce_single_admin_project_per_org: bool
    capacity_commitment_id: str

    def __init__(self, parent: _Optional[str]=..., capacity_commitment: _Optional[_Union[CapacityCommitment, _Mapping]]=..., enforce_single_admin_project_per_org: bool=..., capacity_commitment_id: _Optional[str]=...) -> None:
        ...

class ListCapacityCommitmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCapacityCommitmentsResponse(_message.Message):
    __slots__ = ('capacity_commitments', 'next_page_token')
    CAPACITY_COMMITMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    capacity_commitments: _containers.RepeatedCompositeFieldContainer[CapacityCommitment]
    next_page_token: str

    def __init__(self, capacity_commitments: _Optional[_Iterable[_Union[CapacityCommitment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetCapacityCommitmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteCapacityCommitmentRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class UpdateCapacityCommitmentRequest(_message.Message):
    __slots__ = ('capacity_commitment', 'update_mask')
    CAPACITY_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    capacity_commitment: CapacityCommitment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, capacity_commitment: _Optional[_Union[CapacityCommitment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class SplitCapacityCommitmentRequest(_message.Message):
    __slots__ = ('name', 'slot_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLOT_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    slot_count: int

    def __init__(self, name: _Optional[str]=..., slot_count: _Optional[int]=...) -> None:
        ...

class SplitCapacityCommitmentResponse(_message.Message):
    __slots__ = ('first', 'second')
    FIRST_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    first: CapacityCommitment
    second: CapacityCommitment

    def __init__(self, first: _Optional[_Union[CapacityCommitment, _Mapping]]=..., second: _Optional[_Union[CapacityCommitment, _Mapping]]=...) -> None:
        ...

class MergeCapacityCommitmentsRequest(_message.Message):
    __slots__ = ('parent', 'capacity_commitment_ids')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_COMMITMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    capacity_commitment_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., capacity_commitment_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class Assignment(_message.Message):
    __slots__ = ('name', 'assignee', 'job_type', 'state')

    class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_TYPE_UNSPECIFIED: _ClassVar[Assignment.JobType]
        PIPELINE: _ClassVar[Assignment.JobType]
        QUERY: _ClassVar[Assignment.JobType]
        ML_EXTERNAL: _ClassVar[Assignment.JobType]
        BACKGROUND: _ClassVar[Assignment.JobType]
    JOB_TYPE_UNSPECIFIED: Assignment.JobType
    PIPELINE: Assignment.JobType
    QUERY: Assignment.JobType
    ML_EXTERNAL: Assignment.JobType
    BACKGROUND: Assignment.JobType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Assignment.State]
        PENDING: _ClassVar[Assignment.State]
        ACTIVE: _ClassVar[Assignment.State]
    STATE_UNSPECIFIED: Assignment.State
    PENDING: Assignment.State
    ACTIVE: Assignment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    assignee: str
    job_type: Assignment.JobType
    state: Assignment.State

    def __init__(self, name: _Optional[str]=..., assignee: _Optional[str]=..., job_type: _Optional[_Union[Assignment.JobType, str]]=..., state: _Optional[_Union[Assignment.State, str]]=...) -> None:
        ...

class CreateAssignmentRequest(_message.Message):
    __slots__ = ('parent', 'assignment', 'assignment_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    assignment: Assignment
    assignment_id: str

    def __init__(self, parent: _Optional[str]=..., assignment: _Optional[_Union[Assignment, _Mapping]]=..., assignment_id: _Optional[str]=...) -> None:
        ...

class ListAssignmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAssignmentsResponse(_message.Message):
    __slots__ = ('assignments', 'next_page_token')
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[Assignment]
    next_page_token: str

    def __init__(self, assignments: _Optional[_Iterable[_Union[Assignment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteAssignmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SearchAssignmentsRequest(_message.Message):
    __slots__ = ('parent', 'query', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchAllAssignmentsRequest(_message.Message):
    __slots__ = ('parent', 'query', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchAssignmentsResponse(_message.Message):
    __slots__ = ('assignments', 'next_page_token')
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[Assignment]
    next_page_token: str

    def __init__(self, assignments: _Optional[_Iterable[_Union[Assignment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchAllAssignmentsResponse(_message.Message):
    __slots__ = ('assignments', 'next_page_token')
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[Assignment]
    next_page_token: str

    def __init__(self, assignments: _Optional[_Iterable[_Union[Assignment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class MoveAssignmentRequest(_message.Message):
    __slots__ = ('name', 'destination_id', 'assignment_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_id: str
    assignment_id: str

    def __init__(self, name: _Optional[str]=..., destination_id: _Optional[str]=..., assignment_id: _Optional[str]=...) -> None:
        ...

class UpdateAssignmentRequest(_message.Message):
    __slots__ = ('assignment', 'update_mask')
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    assignment: Assignment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, assignment: _Optional[_Union[Assignment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class TableReference(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'table_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class BiReservation(_message.Message):
    __slots__ = ('name', 'update_time', 'size', 'preferred_tables')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_TABLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_time: _timestamp_pb2.Timestamp
    size: int
    preferred_tables: _containers.RepeatedCompositeFieldContainer[TableReference]

    def __init__(self, name: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., size: _Optional[int]=..., preferred_tables: _Optional[_Iterable[_Union[TableReference, _Mapping]]]=...) -> None:
        ...

class GetBiReservationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateBiReservationRequest(_message.Message):
    __slots__ = ('bi_reservation', 'update_mask')
    BI_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    bi_reservation: BiReservation
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, bi_reservation: _Optional[_Union[BiReservation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...