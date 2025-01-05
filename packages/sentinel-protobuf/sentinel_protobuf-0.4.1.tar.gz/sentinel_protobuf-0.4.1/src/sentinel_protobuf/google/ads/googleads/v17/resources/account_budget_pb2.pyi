from google.ads.googleads.v17.enums import account_budget_proposal_type_pb2 as _account_budget_proposal_type_pb2
from google.ads.googleads.v17.enums import account_budget_status_pb2 as _account_budget_status_pb2
from google.ads.googleads.v17.enums import spending_limit_type_pb2 as _spending_limit_type_pb2
from google.ads.googleads.v17.enums import time_type_pb2 as _time_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountBudget(_message.Message):
    __slots__ = ("resource_name", "id", "billing_setup", "status", "name", "proposed_start_date_time", "approved_start_date_time", "total_adjustments_micros", "amount_served_micros", "purchase_order_number", "notes", "pending_proposal", "proposed_end_date_time", "proposed_end_time_type", "approved_end_date_time", "approved_end_time_type", "proposed_spending_limit_micros", "proposed_spending_limit_type", "approved_spending_limit_micros", "approved_spending_limit_type", "adjusted_spending_limit_micros", "adjusted_spending_limit_type")
    class PendingAccountBudgetProposal(_message.Message):
        __slots__ = ("account_budget_proposal", "proposal_type", "name", "start_date_time", "purchase_order_number", "notes", "creation_date_time", "end_date_time", "end_time_type", "spending_limit_micros", "spending_limit_type")
        ACCOUNT_BUDGET_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
        PROPOSAL_TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NOTES_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        SPENDING_LIMIT_MICROS_FIELD_NUMBER: _ClassVar[int]
        SPENDING_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
        account_budget_proposal: str
        proposal_type: _account_budget_proposal_type_pb2.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
        name: str
        start_date_time: str
        purchase_order_number: str
        notes: str
        creation_date_time: str
        end_date_time: str
        end_time_type: _time_type_pb2.TimeTypeEnum.TimeType
        spending_limit_micros: int
        spending_limit_type: _spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType
        def __init__(self, account_budget_proposal: _Optional[str] = ..., proposal_type: _Optional[_Union[_account_budget_proposal_type_pb2.AccountBudgetProposalTypeEnum.AccountBudgetProposalType, str]] = ..., name: _Optional[str] = ..., start_date_time: _Optional[str] = ..., purchase_order_number: _Optional[str] = ..., notes: _Optional[str] = ..., creation_date_time: _Optional[str] = ..., end_date_time: _Optional[str] = ..., end_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., spending_limit_micros: _Optional[int] = ..., spending_limit_type: _Optional[_Union[_spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType, str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_SETUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVED_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ADJUSTMENTS_MICROS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SERVED_MICROS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PENDING_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_END_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVED_END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVED_END_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_SPENDING_LIMIT_MICROS_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_SPENDING_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVED_SPENDING_LIMIT_MICROS_FIELD_NUMBER: _ClassVar[int]
    APPROVED_SPENDING_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADJUSTED_SPENDING_LIMIT_MICROS_FIELD_NUMBER: _ClassVar[int]
    ADJUSTED_SPENDING_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    billing_setup: str
    status: _account_budget_status_pb2.AccountBudgetStatusEnum.AccountBudgetStatus
    name: str
    proposed_start_date_time: str
    approved_start_date_time: str
    total_adjustments_micros: int
    amount_served_micros: int
    purchase_order_number: str
    notes: str
    pending_proposal: AccountBudget.PendingAccountBudgetProposal
    proposed_end_date_time: str
    proposed_end_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    approved_end_date_time: str
    approved_end_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    proposed_spending_limit_micros: int
    proposed_spending_limit_type: _spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_micros: int
    approved_spending_limit_type: _spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType
    adjusted_spending_limit_micros: int
    adjusted_spending_limit_type: _spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., billing_setup: _Optional[str] = ..., status: _Optional[_Union[_account_budget_status_pb2.AccountBudgetStatusEnum.AccountBudgetStatus, str]] = ..., name: _Optional[str] = ..., proposed_start_date_time: _Optional[str] = ..., approved_start_date_time: _Optional[str] = ..., total_adjustments_micros: _Optional[int] = ..., amount_served_micros: _Optional[int] = ..., purchase_order_number: _Optional[str] = ..., notes: _Optional[str] = ..., pending_proposal: _Optional[_Union[AccountBudget.PendingAccountBudgetProposal, _Mapping]] = ..., proposed_end_date_time: _Optional[str] = ..., proposed_end_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., approved_end_date_time: _Optional[str] = ..., approved_end_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., proposed_spending_limit_micros: _Optional[int] = ..., proposed_spending_limit_type: _Optional[_Union[_spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType, str]] = ..., approved_spending_limit_micros: _Optional[int] = ..., approved_spending_limit_type: _Optional[_Union[_spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType, str]] = ..., adjusted_spending_limit_micros: _Optional[int] = ..., adjusted_spending_limit_type: _Optional[_Union[_spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType, str]] = ...) -> None: ...
