from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BillingSetupErrorEnum(_message.Message):
    __slots__ = ()

    class BillingSetupError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        UNKNOWN: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        CANNOT_USE_EXISTING_AND_NEW_ACCOUNT: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        CANNOT_REMOVE_STARTED_BILLING_SETUP: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        INVALID_PAYMENTS_ACCOUNT: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        INVALID_START_TIME_TYPE: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        THIRD_PARTY_ALREADY_HAS_BILLING: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        BILLING_SETUP_IN_PROGRESS: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        NO_SIGNUP_PERMISSION: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        CHANGE_OF_BILL_TO_IN_PROGRESS: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        PAYMENTS_PROFILE_NOT_FOUND: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        PAYMENTS_ACCOUNT_NOT_FOUND: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        PAYMENTS_PROFILE_INELIGIBLE: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        PAYMENTS_ACCOUNT_INELIGIBLE: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        CUSTOMER_NEEDS_INTERNAL_APPROVAL: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        PAYMENTS_PROFILE_NEEDS_SERVICE_AGREEMENT_ACCEPTANCE: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        FUTURE_START_TIME_PROHIBITED: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
        TOO_MANY_BILLING_SETUPS_FOR_PAYMENTS_ACCOUNT: _ClassVar[BillingSetupErrorEnum.BillingSetupError]
    UNSPECIFIED: BillingSetupErrorEnum.BillingSetupError
    UNKNOWN: BillingSetupErrorEnum.BillingSetupError
    CANNOT_USE_EXISTING_AND_NEW_ACCOUNT: BillingSetupErrorEnum.BillingSetupError
    CANNOT_REMOVE_STARTED_BILLING_SETUP: BillingSetupErrorEnum.BillingSetupError
    CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT: BillingSetupErrorEnum.BillingSetupError
    BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS: BillingSetupErrorEnum.BillingSetupError
    INVALID_PAYMENTS_ACCOUNT: BillingSetupErrorEnum.BillingSetupError
    BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY: BillingSetupErrorEnum.BillingSetupError
    INVALID_START_TIME_TYPE: BillingSetupErrorEnum.BillingSetupError
    THIRD_PARTY_ALREADY_HAS_BILLING: BillingSetupErrorEnum.BillingSetupError
    BILLING_SETUP_IN_PROGRESS: BillingSetupErrorEnum.BillingSetupError
    NO_SIGNUP_PERMISSION: BillingSetupErrorEnum.BillingSetupError
    CHANGE_OF_BILL_TO_IN_PROGRESS: BillingSetupErrorEnum.BillingSetupError
    PAYMENTS_PROFILE_NOT_FOUND: BillingSetupErrorEnum.BillingSetupError
    PAYMENTS_ACCOUNT_NOT_FOUND: BillingSetupErrorEnum.BillingSetupError
    PAYMENTS_PROFILE_INELIGIBLE: BillingSetupErrorEnum.BillingSetupError
    PAYMENTS_ACCOUNT_INELIGIBLE: BillingSetupErrorEnum.BillingSetupError
    CUSTOMER_NEEDS_INTERNAL_APPROVAL: BillingSetupErrorEnum.BillingSetupError
    PAYMENTS_PROFILE_NEEDS_SERVICE_AGREEMENT_ACCEPTANCE: BillingSetupErrorEnum.BillingSetupError
    PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH: BillingSetupErrorEnum.BillingSetupError
    FUTURE_START_TIME_PROHIBITED: BillingSetupErrorEnum.BillingSetupError
    TOO_MANY_BILLING_SETUPS_FOR_PAYMENTS_ACCOUNT: BillingSetupErrorEnum.BillingSetupError

    def __init__(self) -> None:
        ...