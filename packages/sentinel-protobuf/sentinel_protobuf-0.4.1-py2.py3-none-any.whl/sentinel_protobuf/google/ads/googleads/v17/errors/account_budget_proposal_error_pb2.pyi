from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountBudgetProposalErrorEnum(_message.Message):
    __slots__ = ()

    class AccountBudgetProposalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        UNKNOWN: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        FIELD_MASK_NOT_ALLOWED: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        IMMUTABLE_FIELD: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        REQUIRED_FIELD_MISSING: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_CANCEL_APPROVED_PROPOSAL: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_REMOVE_UNAPPROVED_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_REMOVE_RUNNING_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_END_UNAPPROVED_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_END_INACTIVE_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        BUDGET_NAME_REQUIRED: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_UPDATE_OLD_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_END_IN_PAST: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_EXTEND_END_TIME: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        PURCHASE_ORDER_NUMBER_REQUIRED: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        PENDING_UPDATE_PROPOSAL_EXISTS: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        UPDATE_IS_NO_OP: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        END_TIME_MUST_FOLLOW_START_TIME: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        NOT_AUTHORIZED: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        INVALID_BILLING_SETUP: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        OVERLAPS_EXISTING_BUDGET: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANNOT_CREATE_BUDGET_THROUGH_API: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        INVALID_MASTER_SERVICE_AGREEMENT: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
        CANCELED_BILLING_SETUP: _ClassVar[AccountBudgetProposalErrorEnum.AccountBudgetProposalError]
    UNSPECIFIED: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    UNKNOWN: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    FIELD_MASK_NOT_ALLOWED: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    IMMUTABLE_FIELD: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    REQUIRED_FIELD_MISSING: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_CANCEL_APPROVED_PROPOSAL: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_REMOVE_UNAPPROVED_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_REMOVE_RUNNING_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_END_UNAPPROVED_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_END_INACTIVE_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    BUDGET_NAME_REQUIRED: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_UPDATE_OLD_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_END_IN_PAST: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_EXTEND_END_TIME: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    PURCHASE_ORDER_NUMBER_REQUIRED: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    PENDING_UPDATE_PROPOSAL_EXISTS: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    UPDATE_IS_NO_OP: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    END_TIME_MUST_FOLLOW_START_TIME: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    NOT_AUTHORIZED: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    INVALID_BILLING_SETUP: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    OVERLAPS_EXISTING_BUDGET: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANNOT_CREATE_BUDGET_THROUGH_API: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    INVALID_MASTER_SERVICE_AGREEMENT: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    CANCELED_BILLING_SETUP: AccountBudgetProposalErrorEnum.AccountBudgetProposalError

    def __init__(self) -> None:
        ...