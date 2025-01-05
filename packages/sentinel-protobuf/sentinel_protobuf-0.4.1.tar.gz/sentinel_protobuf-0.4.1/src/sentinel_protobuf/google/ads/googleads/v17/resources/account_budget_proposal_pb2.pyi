from google.ads.googleads.v17.enums import account_budget_proposal_status_pb2 as _account_budget_proposal_status_pb2
from google.ads.googleads.v17.enums import account_budget_proposal_type_pb2 as _account_budget_proposal_type_pb2
from google.ads.googleads.v17.enums import spending_limit_type_pb2 as _spending_limit_type_pb2
from google.ads.googleads.v17.enums import time_type_pb2 as _time_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountBudgetProposal(_message.Message):
    __slots__ = ("resource_name", "id", "billing_setup", "account_budget", "proposal_type", "status", "proposed_name", "approved_start_date_time", "proposed_purchase_order_number", "proposed_notes", "creation_date_time", "approval_date_time", "proposed_start_date_time", "proposed_start_time_type", "proposed_end_date_time", "proposed_end_time_type", "approved_end_date_time", "approved_end_time_type", "proposed_spending_limit_micros", "proposed_spending_limit_type", "approved_spending_limit_micros", "approved_spending_limit_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_SETUP_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_BUDGET_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVED_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_PURCHASE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_NOTES_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_START_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_END_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVED_END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVED_END_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_SPENDING_LIMIT_MICROS_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_SPENDING_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVED_SPENDING_LIMIT_MICROS_FIELD_NUMBER: _ClassVar[int]
    APPROVED_SPENDING_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    billing_setup: str
    account_budget: str
    proposal_type: _account_budget_proposal_type_pb2.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    status: _account_budget_proposal_status_pb2.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    proposed_name: str
    approved_start_date_time: str
    proposed_purchase_order_number: str
    proposed_notes: str
    creation_date_time: str
    approval_date_time: str
    proposed_start_date_time: str
    proposed_start_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    proposed_end_date_time: str
    proposed_end_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    approved_end_date_time: str
    approved_end_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    proposed_spending_limit_micros: int
    proposed_spending_limit_type: _spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_micros: int
    approved_spending_limit_type: _spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., billing_setup: _Optional[str] = ..., account_budget: _Optional[str] = ..., proposal_type: _Optional[_Union[_account_budget_proposal_type_pb2.AccountBudgetProposalTypeEnum.AccountBudgetProposalType, str]] = ..., status: _Optional[_Union[_account_budget_proposal_status_pb2.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, str]] = ..., proposed_name: _Optional[str] = ..., approved_start_date_time: _Optional[str] = ..., proposed_purchase_order_number: _Optional[str] = ..., proposed_notes: _Optional[str] = ..., creation_date_time: _Optional[str] = ..., approval_date_time: _Optional[str] = ..., proposed_start_date_time: _Optional[str] = ..., proposed_start_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., proposed_end_date_time: _Optional[str] = ..., proposed_end_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., approved_end_date_time: _Optional[str] = ..., approved_end_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., proposed_spending_limit_micros: _Optional[int] = ..., proposed_spending_limit_type: _Optional[_Union[_spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType, str]] = ..., approved_spending_limit_micros: _Optional[int] = ..., approved_spending_limit_type: _Optional[_Union[_spending_limit_type_pb2.SpendingLimitTypeEnum.SpendingLimitType, str]] = ...) -> None: ...
