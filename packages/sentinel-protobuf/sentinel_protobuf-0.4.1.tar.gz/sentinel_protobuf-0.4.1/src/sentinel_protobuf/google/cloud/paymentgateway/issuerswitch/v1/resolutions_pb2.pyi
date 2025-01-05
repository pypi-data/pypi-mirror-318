from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransactionSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_SUB_TYPE_UNSPECIFIED: _ClassVar[TransactionSubType]
    TRANSACTION_SUB_TYPE_BENEFICIARY: _ClassVar[TransactionSubType]
    TRANSACTION_SUB_TYPE_REMITTER: _ClassVar[TransactionSubType]
TRANSACTION_SUB_TYPE_UNSPECIFIED: TransactionSubType
TRANSACTION_SUB_TYPE_BENEFICIARY: TransactionSubType
TRANSACTION_SUB_TYPE_REMITTER: TransactionSubType

class Complaint(_message.Message):
    __slots__ = ('name', 'raise_complaint_adjustment', 'details', 'response', 'resolve_complaint_adjustment')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RAISE_COMPLAINT_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_COMPLAINT_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    raise_complaint_adjustment: RaiseComplaintAdjustment
    details: CaseDetails
    response: CaseResponse
    resolve_complaint_adjustment: ResolveComplaintAdjustment

    def __init__(self, name: _Optional[str]=..., raise_complaint_adjustment: _Optional[_Union[RaiseComplaintAdjustment, _Mapping]]=..., details: _Optional[_Union[CaseDetails, _Mapping]]=..., response: _Optional[_Union[CaseResponse, _Mapping]]=..., resolve_complaint_adjustment: _Optional[_Union[ResolveComplaintAdjustment, _Mapping]]=...) -> None:
        ...

class CreateComplaintRequest(_message.Message):
    __slots__ = ('parent', 'complaint')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPLAINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    complaint: Complaint

    def __init__(self, parent: _Optional[str]=..., complaint: _Optional[_Union[Complaint, _Mapping]]=...) -> None:
        ...

class ResolveComplaintRequest(_message.Message):
    __slots__ = ('complaint',)
    COMPLAINT_FIELD_NUMBER: _ClassVar[int]
    complaint: Complaint

    def __init__(self, complaint: _Optional[_Union[Complaint, _Mapping]]=...) -> None:
        ...

class Dispute(_message.Message):
    __slots__ = ('name', 'raise_dispute_adjustment', 'details', 'response', 'resolve_dispute_adjustment')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RAISE_DISPUTE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_DISPUTE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    raise_dispute_adjustment: RaiseDisputeAdjustment
    details: CaseDetails
    response: CaseResponse
    resolve_dispute_adjustment: ResolveDisputeAdjustment

    def __init__(self, name: _Optional[str]=..., raise_dispute_adjustment: _Optional[_Union[RaiseDisputeAdjustment, _Mapping]]=..., details: _Optional[_Union[CaseDetails, _Mapping]]=..., response: _Optional[_Union[CaseResponse, _Mapping]]=..., resolve_dispute_adjustment: _Optional[_Union[ResolveDisputeAdjustment, _Mapping]]=...) -> None:
        ...

class CreateDisputeRequest(_message.Message):
    __slots__ = ('parent', 'dispute')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dispute: Dispute

    def __init__(self, parent: _Optional[str]=..., dispute: _Optional[_Union[Dispute, _Mapping]]=...) -> None:
        ...

class ResolveDisputeRequest(_message.Message):
    __slots__ = ('dispute',)
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    dispute: Dispute

    def __init__(self, dispute: _Optional[_Union[Dispute, _Mapping]]=...) -> None:
        ...

class OriginalTransaction(_message.Message):
    __slots__ = ('transaction_id', 'retrieval_reference_number', 'request_time')
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    retrieval_reference_number: str
    request_time: _timestamp_pb2.Timestamp

    def __init__(self, transaction_id: _Optional[str]=..., retrieval_reference_number: _Optional[str]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CaseDetails(_message.Message):
    __slots__ = ('original_transaction', 'transaction_sub_type', 'amount', 'original_settlement_response_code', 'current_cycle')
    ORIGINAL_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SETTLEMENT_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CYCLE_FIELD_NUMBER: _ClassVar[int]
    original_transaction: OriginalTransaction
    transaction_sub_type: TransactionSubType
    amount: _money_pb2.Money
    original_settlement_response_code: str
    current_cycle: bool

    def __init__(self, original_transaction: _Optional[_Union[OriginalTransaction, _Mapping]]=..., transaction_sub_type: _Optional[_Union[TransactionSubType, str]]=..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., original_settlement_response_code: _Optional[str]=..., current_cycle: bool=...) -> None:
        ...

class CaseResponse(_message.Message):
    __slots__ = ('complaint_reference_number', 'amount', 'adjustment_flag', 'adjustment_code', 'adjustment_reference_id', 'adjustment_remarks', 'approval_number', 'process_status', 'adjustment_time', 'payer', 'payee', 'result')

    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_UNSPECIFIED: _ClassVar[CaseResponse.Result]
        SUCCESS: _ClassVar[CaseResponse.Result]
        FAILURE: _ClassVar[CaseResponse.Result]
    RESULT_UNSPECIFIED: CaseResponse.Result
    SUCCESS: CaseResponse.Result
    FAILURE: CaseResponse.Result
    COMPLAINT_REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_FLAG_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_REMARKS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROCESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    PAYER_FIELD_NUMBER: _ClassVar[int]
    PAYEE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    complaint_reference_number: str
    amount: _money_pb2.Money
    adjustment_flag: str
    adjustment_code: str
    adjustment_reference_id: str
    adjustment_remarks: str
    approval_number: str
    process_status: str
    adjustment_time: _timestamp_pb2.Timestamp
    payer: _common_fields_pb2.Participant
    payee: _common_fields_pb2.Participant
    result: CaseResponse.Result

    def __init__(self, complaint_reference_number: _Optional[str]=..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., adjustment_flag: _Optional[str]=..., adjustment_code: _Optional[str]=..., adjustment_reference_id: _Optional[str]=..., adjustment_remarks: _Optional[str]=..., approval_number: _Optional[str]=..., process_status: _Optional[str]=..., adjustment_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., payer: _Optional[_Union[_common_fields_pb2.Participant, _Mapping]]=..., payee: _Optional[_Union[_common_fields_pb2.Participant, _Mapping]]=..., result: _Optional[_Union[CaseResponse.Result, str]]=...) -> None:
        ...

class RaiseComplaintAdjustment(_message.Message):
    __slots__ = ('adjustment_flag', 'adjustment_code')

    class AdjustmentFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADJUSTMENT_FLAG_UNSPECIFIED: _ClassVar[RaiseComplaintAdjustment.AdjustmentFlag]
        RAISE: _ClassVar[RaiseComplaintAdjustment.AdjustmentFlag]
    ADJUSTMENT_FLAG_UNSPECIFIED: RaiseComplaintAdjustment.AdjustmentFlag
    RAISE: RaiseComplaintAdjustment.AdjustmentFlag

    class ReasonCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_CODE_UNSPECIFIED: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        CUSTOMER_ACCOUNT_NOT_REVERSED: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        GOODS_SERVICES_NOT_PROVIDED: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        CUSTOMER_ACCOUNT_NOT_CREDITED_BACK: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        BENEFICIARY_ACCOUNT_NOT_CREDITED: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        GOODS_SERVICES_CREDIT_NOT_PROCESSED: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        MERCHANT_NOT_RECEIVED_CONFIRMATION: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
        PAID_BY_ALTERNATE_MEANS: _ClassVar[RaiseComplaintAdjustment.ReasonCode]
    REASON_CODE_UNSPECIFIED: RaiseComplaintAdjustment.ReasonCode
    CUSTOMER_ACCOUNT_NOT_REVERSED: RaiseComplaintAdjustment.ReasonCode
    GOODS_SERVICES_NOT_PROVIDED: RaiseComplaintAdjustment.ReasonCode
    CUSTOMER_ACCOUNT_NOT_CREDITED_BACK: RaiseComplaintAdjustment.ReasonCode
    BENEFICIARY_ACCOUNT_NOT_CREDITED: RaiseComplaintAdjustment.ReasonCode
    GOODS_SERVICES_CREDIT_NOT_PROCESSED: RaiseComplaintAdjustment.ReasonCode
    MERCHANT_NOT_RECEIVED_CONFIRMATION: RaiseComplaintAdjustment.ReasonCode
    PAID_BY_ALTERNATE_MEANS: RaiseComplaintAdjustment.ReasonCode
    ADJUSTMENT_FLAG_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    adjustment_flag: RaiseComplaintAdjustment.AdjustmentFlag
    adjustment_code: RaiseComplaintAdjustment.ReasonCode

    def __init__(self, adjustment_flag: _Optional[_Union[RaiseComplaintAdjustment.AdjustmentFlag, str]]=..., adjustment_code: _Optional[_Union[RaiseComplaintAdjustment.ReasonCode, str]]=...) -> None:
        ...

class ResolveComplaintAdjustment(_message.Message):
    __slots__ = ('adjustment_flag', 'adjustment_code')

    class AdjustmentFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADJUSTMENT_FLAG_UNSPECIFIED: _ClassVar[ResolveComplaintAdjustment.AdjustmentFlag]
        DEBIT_REVERSAL_CONFIRMATION: _ClassVar[ResolveComplaintAdjustment.AdjustmentFlag]
        RETURN: _ClassVar[ResolveComplaintAdjustment.AdjustmentFlag]
        REFUND_REVERSAL_CONFIRMATION: _ClassVar[ResolveComplaintAdjustment.AdjustmentFlag]
        TRANSACTION_CREDIT_CONFIRMATION: _ClassVar[ResolveComplaintAdjustment.AdjustmentFlag]
    ADJUSTMENT_FLAG_UNSPECIFIED: ResolveComplaintAdjustment.AdjustmentFlag
    DEBIT_REVERSAL_CONFIRMATION: ResolveComplaintAdjustment.AdjustmentFlag
    RETURN: ResolveComplaintAdjustment.AdjustmentFlag
    REFUND_REVERSAL_CONFIRMATION: ResolveComplaintAdjustment.AdjustmentFlag
    TRANSACTION_CREDIT_CONFIRMATION: ResolveComplaintAdjustment.AdjustmentFlag

    class ReasonCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_CODE_UNSPECIFIED: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        COMPLAINT_RESOLVED_ONLINE: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        COMPLAINT_RESOLVED_NOW_OR_MANUALLY: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        ORIGINAL_TRANSACTION_NOT_DONE: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_ACCOUNT_CLOSED: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_ACCOUNT_DOES_NOT_EXIST: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_PARTY_INSTRUCTIONS: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_NRI_ACCOUNT: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_CREDIT_FREEZED: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_INVALID_BENEFICIARY_DETAILS: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_ANY_OTHER_REASON: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_BENEFICIARY_CANNOT_CREDIT: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RET_MERCHANT_NOT_RECEIVED_CONFIRMATION: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
        RRC_CUSTOMER_ACCOUNT_CREDITED: _ClassVar[ResolveComplaintAdjustment.ReasonCode]
    REASON_CODE_UNSPECIFIED: ResolveComplaintAdjustment.ReasonCode
    COMPLAINT_RESOLVED_ONLINE: ResolveComplaintAdjustment.ReasonCode
    COMPLAINT_RESOLVED_NOW_OR_MANUALLY: ResolveComplaintAdjustment.ReasonCode
    ORIGINAL_TRANSACTION_NOT_DONE: ResolveComplaintAdjustment.ReasonCode
    RET_ACCOUNT_CLOSED: ResolveComplaintAdjustment.ReasonCode
    RET_ACCOUNT_DOES_NOT_EXIST: ResolveComplaintAdjustment.ReasonCode
    RET_PARTY_INSTRUCTIONS: ResolveComplaintAdjustment.ReasonCode
    RET_NRI_ACCOUNT: ResolveComplaintAdjustment.ReasonCode
    RET_CREDIT_FREEZED: ResolveComplaintAdjustment.ReasonCode
    RET_INVALID_BENEFICIARY_DETAILS: ResolveComplaintAdjustment.ReasonCode
    RET_ANY_OTHER_REASON: ResolveComplaintAdjustment.ReasonCode
    RET_BENEFICIARY_CANNOT_CREDIT: ResolveComplaintAdjustment.ReasonCode
    RET_MERCHANT_NOT_RECEIVED_CONFIRMATION: ResolveComplaintAdjustment.ReasonCode
    RRC_CUSTOMER_ACCOUNT_CREDITED: ResolveComplaintAdjustment.ReasonCode
    ADJUSTMENT_FLAG_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    adjustment_flag: ResolveComplaintAdjustment.AdjustmentFlag
    adjustment_code: ResolveComplaintAdjustment.ReasonCode

    def __init__(self, adjustment_flag: _Optional[_Union[ResolveComplaintAdjustment.AdjustmentFlag, str]]=..., adjustment_code: _Optional[_Union[ResolveComplaintAdjustment.ReasonCode, str]]=...) -> None:
        ...

class RaiseDisputeAdjustment(_message.Message):
    __slots__ = ('adjustment_flag', 'adjustment_code')

    class AdjustmentFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADJUSTMENT_FLAG_UNSPECIFIED: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        CHARGEBACK_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        FRAUD_CHARGEBACK_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        WRONG_CREDIT_CHARGEBACK_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        DEFERRED_CHARGEBACK_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        PRE_ARBITRATION_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        DEFERRED_PRE_ARBITRATION_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        ARBITRATION_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
        DEFERRED_ARBITRATION_RAISE: _ClassVar[RaiseDisputeAdjustment.AdjustmentFlag]
    ADJUSTMENT_FLAG_UNSPECIFIED: RaiseDisputeAdjustment.AdjustmentFlag
    CHARGEBACK_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    FRAUD_CHARGEBACK_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    WRONG_CREDIT_CHARGEBACK_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    DEFERRED_CHARGEBACK_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    PRE_ARBITRATION_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    DEFERRED_PRE_ARBITRATION_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    ARBITRATION_RAISE: RaiseDisputeAdjustment.AdjustmentFlag
    DEFERRED_ARBITRATION_RAISE: RaiseDisputeAdjustment.AdjustmentFlag

    class ReasonCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_CODE_UNSPECIFIED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        CHARGEBACK_RAISE_REMITTER_DEBITED_BENEFICIARY_NOT_CREDITED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        PRE_ARBITRATION_RAISE_BENEFICIARY_NOT_CREDITED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        DEFERRED_CHARGEBACK_RAISE_BENEFICIARY_NOT_CREDITED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        DEFERRED_PRE_ARBITRATION_RAISE_BENEFICIARY_NOT_CREDITED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        DEFERRED_ARBITRATION_RAISE_DEFERRED_CHARGEBACK_PRE_ARBITRATION_REJECTED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        CHARGEBACK_ON_FRAUD: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        GOODS_SERVICES_CREDIT_NOT_PROCESSED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        GOODS_SERVICES_DEFECTIVE: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        PAID_BY_ALTERNATE_MEANS: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        GOODS_SERVICES_NOT_RECEIVED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        MERCHANT_NOT_RECEIVED_CONFIRMATION: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        TRANSACTION_NOT_STEELED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        DUPLICATE_TRANSACTION: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        CHARGEBACK_CARD_HOLDER_CHARGED_MORE: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        CUSTOMER_CLAIMING_GOODS_SERVICES_NOT_DELIVERED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        PARTIES_DENIED: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
        FUNDS_TRANSFERRED_TO_UNINTENDED_BENEFICIARY: _ClassVar[RaiseDisputeAdjustment.ReasonCode]
    REASON_CODE_UNSPECIFIED: RaiseDisputeAdjustment.ReasonCode
    CHARGEBACK_RAISE_REMITTER_DEBITED_BENEFICIARY_NOT_CREDITED: RaiseDisputeAdjustment.ReasonCode
    PRE_ARBITRATION_RAISE_BENEFICIARY_NOT_CREDITED: RaiseDisputeAdjustment.ReasonCode
    DEFERRED_CHARGEBACK_RAISE_BENEFICIARY_NOT_CREDITED: RaiseDisputeAdjustment.ReasonCode
    DEFERRED_PRE_ARBITRATION_RAISE_BENEFICIARY_NOT_CREDITED: RaiseDisputeAdjustment.ReasonCode
    DEFERRED_ARBITRATION_RAISE_DEFERRED_CHARGEBACK_PRE_ARBITRATION_REJECTED: RaiseDisputeAdjustment.ReasonCode
    CHARGEBACK_ON_FRAUD: RaiseDisputeAdjustment.ReasonCode
    GOODS_SERVICES_CREDIT_NOT_PROCESSED: RaiseDisputeAdjustment.ReasonCode
    GOODS_SERVICES_DEFECTIVE: RaiseDisputeAdjustment.ReasonCode
    PAID_BY_ALTERNATE_MEANS: RaiseDisputeAdjustment.ReasonCode
    GOODS_SERVICES_NOT_RECEIVED: RaiseDisputeAdjustment.ReasonCode
    MERCHANT_NOT_RECEIVED_CONFIRMATION: RaiseDisputeAdjustment.ReasonCode
    TRANSACTION_NOT_STEELED: RaiseDisputeAdjustment.ReasonCode
    DUPLICATE_TRANSACTION: RaiseDisputeAdjustment.ReasonCode
    CHARGEBACK_CARD_HOLDER_CHARGED_MORE: RaiseDisputeAdjustment.ReasonCode
    CUSTOMER_CLAIMING_GOODS_SERVICES_NOT_DELIVERED: RaiseDisputeAdjustment.ReasonCode
    PARTIES_DENIED: RaiseDisputeAdjustment.ReasonCode
    FUNDS_TRANSFERRED_TO_UNINTENDED_BENEFICIARY: RaiseDisputeAdjustment.ReasonCode
    ADJUSTMENT_FLAG_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    adjustment_flag: RaiseDisputeAdjustment.AdjustmentFlag
    adjustment_code: RaiseDisputeAdjustment.ReasonCode

    def __init__(self, adjustment_flag: _Optional[_Union[RaiseDisputeAdjustment.AdjustmentFlag, str]]=..., adjustment_code: _Optional[_Union[RaiseDisputeAdjustment.ReasonCode, str]]=...) -> None:
        ...

class ResolveDisputeAdjustment(_message.Message):
    __slots__ = ('adjustment_flag', 'adjustment_code')

    class AdjustmentFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADJUSTMENT_FLAG_UNSPECIFIED: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        RE_PRESENTMENT_RAISE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        DEFERRED_RE_PRESENTMENT_RAISE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        CHARGEBACK_ACCEPTANCE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        DEFERRED_CHARGEBACK_ACCEPTANCE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        PRE_ARBITRATION_ACCEPTANCE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        DEFERRED_PRE_ARBITRATION_ACCEPTANCE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        PRE_ARBITRATION_DECLINED: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        DEFERRED_PRE_ARBITRATION_DECLINED: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        ARBITRATION_ACCEPTANCE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        ARBITRATION_CONTINUATION: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        ARBITRATION_WITHDRAWN: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        ARBITRATION_VERDICT: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        CREDIT_ADJUSTMENT: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        FRAUD_CHARGEBACK_REPRESENTMENT: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        FRAUD_CHARGEBACK_ACCEPT: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        WRONG_CREDIT_REPRESENTMENT: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        WRONG_CREDIT_CHARGEBACK_ACCEPTANCE: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
        MANUAL_ADJUSTMENT: _ClassVar[ResolveDisputeAdjustment.AdjustmentFlag]
    ADJUSTMENT_FLAG_UNSPECIFIED: ResolveDisputeAdjustment.AdjustmentFlag
    RE_PRESENTMENT_RAISE: ResolveDisputeAdjustment.AdjustmentFlag
    DEFERRED_RE_PRESENTMENT_RAISE: ResolveDisputeAdjustment.AdjustmentFlag
    CHARGEBACK_ACCEPTANCE: ResolveDisputeAdjustment.AdjustmentFlag
    DEFERRED_CHARGEBACK_ACCEPTANCE: ResolveDisputeAdjustment.AdjustmentFlag
    PRE_ARBITRATION_ACCEPTANCE: ResolveDisputeAdjustment.AdjustmentFlag
    DEFERRED_PRE_ARBITRATION_ACCEPTANCE: ResolveDisputeAdjustment.AdjustmentFlag
    PRE_ARBITRATION_DECLINED: ResolveDisputeAdjustment.AdjustmentFlag
    DEFERRED_PRE_ARBITRATION_DECLINED: ResolveDisputeAdjustment.AdjustmentFlag
    ARBITRATION_ACCEPTANCE: ResolveDisputeAdjustment.AdjustmentFlag
    ARBITRATION_CONTINUATION: ResolveDisputeAdjustment.AdjustmentFlag
    ARBITRATION_WITHDRAWN: ResolveDisputeAdjustment.AdjustmentFlag
    ARBITRATION_VERDICT: ResolveDisputeAdjustment.AdjustmentFlag
    CREDIT_ADJUSTMENT: ResolveDisputeAdjustment.AdjustmentFlag
    FRAUD_CHARGEBACK_REPRESENTMENT: ResolveDisputeAdjustment.AdjustmentFlag
    FRAUD_CHARGEBACK_ACCEPT: ResolveDisputeAdjustment.AdjustmentFlag
    WRONG_CREDIT_REPRESENTMENT: ResolveDisputeAdjustment.AdjustmentFlag
    WRONG_CREDIT_CHARGEBACK_ACCEPTANCE: ResolveDisputeAdjustment.AdjustmentFlag
    MANUAL_ADJUSTMENT: ResolveDisputeAdjustment.AdjustmentFlag

    class ReasonCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_CODE_UNSPECIFIED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CHARGEBACK_BENEFICIARY_CANNOT_CREDIT_OR_PRE_ARBITRATION_DUPLICATE_PROCESS: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        PRE_ARBITRATION_DECLINED_BENEFICIARY_CREDITED_ONLINE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        PRE_ARBITRATION_DECLINED_BENEFICIARY_CREDITED_MANUALLY: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        DEFERRED_CHARGEBACK_ACCEPTANCE_ACCOUNT_NOT_CREDITED_TCC_RAISED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        DEFERRED_RE_PRESENTMENT_RAISE_ACCOUNT_CREDITED_TCC_RAISED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        DEFERRED_PRE_ARBITRATION_ACCEPTANCE_ACCOUNT_NOT_CREDITED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        DEFERRED_PRE_ARBITRATION_DECLINED_ACCOUNT_CREDITED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        FRAUD_CHARGEBACK_ACCEPT_AMOUNT_RECOVERED_FROM_FRAUDULENT_ACCOUNT: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        FRAUD_CHARGEBACK_REPRESENTMENT_LIEN_MARKED_INSUFFICIENT_BALANCE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        FRAUD_CHARGEBACK_REPRESENTMENT_FIR_NOT_PROVIDED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        FRAUD_CHARGEBACK_REPRESENTMENT_REASON_OTHERS: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        RE_PRESENTMENT_RAISE_BENEFICIARY_CREDITED_ONLINE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        RE_PRESENTMENT_RAISE_BENEFICIARY_CREDITED_MANUALLY: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_GOODS_SERVICES_CREDIT_NOT_PROCESSED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_GOODS_SERVICES_DEFECTIVE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_PAID_BY_ALTERNATE_MEANS: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_GOODS_SERVICES_NOT_RECEIVED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_MERCHANT_NOT_RECEIVED_CONFIRMATION: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_DUPLICATE_TRANSACTION: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_REASON_OTHERS: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_NON_MATCHING_ACCOUNT_NUMBER: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_CARD_HOLDER_CHARGED_MORE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_CREDIT_NOT_PROCESSED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CREDIT_ADJUSTMENT_BENEFICIARY_CANNOT_CREDIT: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        CHARGEBACK_ACCEPTANCE_MERCHANT_CANNOT_PROVIDE_SERVICE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        RE_PRESENTMENT_RAISE_GOODS_SERVICES_PROVIDED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        PRE_ARBITRATION_DECLINED_SERVICES_PROVIDED_LATER: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        PRE_ARBITRATION_ACCEPTANCE_SERVICES_NOT_PROVIDED_BY_MERCHANT: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        ARBITRATION_ACCEPTANCE_ILLEGIBLE_FULFILMENT: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        ARBITRATION_CONTINUATION_CUSTOMER_STILL_NOT_RECEIVED_SERVICE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        ARBITRATION_WITHDRAWN_CUSTOMER_RECEIVED_SERVICE_LATER: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        ARBITRATION_VERDICT_PANEL_VERDICT: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        MANUAL_ADJUSTMENT_REASON: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        ATTRIBUTING_CUSTOMER: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        ATTRIBUTING_TECHNICAL_ISSUE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        WRONG_CREDIT_CHARGEBACK_ACCEPTANCE_AMOUNT_RECOVERED: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        WRONG_CREDIT_REPRESENTMENT_LIEN_MARKED_INSUFFICIENT_BALANCE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        WRONG_CREDIT_REPRESENTMENT_CUSTOMER_INACCESSIBLE: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
        WRONG_CREDIT_REPRESENTMENT_REASON_OTHERS: _ClassVar[ResolveDisputeAdjustment.ReasonCode]
    REASON_CODE_UNSPECIFIED: ResolveDisputeAdjustment.ReasonCode
    CHARGEBACK_BENEFICIARY_CANNOT_CREDIT_OR_PRE_ARBITRATION_DUPLICATE_PROCESS: ResolveDisputeAdjustment.ReasonCode
    PRE_ARBITRATION_DECLINED_BENEFICIARY_CREDITED_ONLINE: ResolveDisputeAdjustment.ReasonCode
    PRE_ARBITRATION_DECLINED_BENEFICIARY_CREDITED_MANUALLY: ResolveDisputeAdjustment.ReasonCode
    DEFERRED_CHARGEBACK_ACCEPTANCE_ACCOUNT_NOT_CREDITED_TCC_RAISED: ResolveDisputeAdjustment.ReasonCode
    DEFERRED_RE_PRESENTMENT_RAISE_ACCOUNT_CREDITED_TCC_RAISED: ResolveDisputeAdjustment.ReasonCode
    DEFERRED_PRE_ARBITRATION_ACCEPTANCE_ACCOUNT_NOT_CREDITED: ResolveDisputeAdjustment.ReasonCode
    DEFERRED_PRE_ARBITRATION_DECLINED_ACCOUNT_CREDITED: ResolveDisputeAdjustment.ReasonCode
    FRAUD_CHARGEBACK_ACCEPT_AMOUNT_RECOVERED_FROM_FRAUDULENT_ACCOUNT: ResolveDisputeAdjustment.ReasonCode
    FRAUD_CHARGEBACK_REPRESENTMENT_LIEN_MARKED_INSUFFICIENT_BALANCE: ResolveDisputeAdjustment.ReasonCode
    FRAUD_CHARGEBACK_REPRESENTMENT_FIR_NOT_PROVIDED: ResolveDisputeAdjustment.ReasonCode
    FRAUD_CHARGEBACK_REPRESENTMENT_REASON_OTHERS: ResolveDisputeAdjustment.ReasonCode
    RE_PRESENTMENT_RAISE_BENEFICIARY_CREDITED_ONLINE: ResolveDisputeAdjustment.ReasonCode
    RE_PRESENTMENT_RAISE_BENEFICIARY_CREDITED_MANUALLY: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_GOODS_SERVICES_CREDIT_NOT_PROCESSED: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_GOODS_SERVICES_DEFECTIVE: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_PAID_BY_ALTERNATE_MEANS: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_GOODS_SERVICES_NOT_RECEIVED: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_MERCHANT_NOT_RECEIVED_CONFIRMATION: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_DUPLICATE_TRANSACTION: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_REASON_OTHERS: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_NON_MATCHING_ACCOUNT_NUMBER: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_CARD_HOLDER_CHARGED_MORE: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_CREDIT_NOT_PROCESSED: ResolveDisputeAdjustment.ReasonCode
    CREDIT_ADJUSTMENT_BENEFICIARY_CANNOT_CREDIT: ResolveDisputeAdjustment.ReasonCode
    CHARGEBACK_ACCEPTANCE_MERCHANT_CANNOT_PROVIDE_SERVICE: ResolveDisputeAdjustment.ReasonCode
    RE_PRESENTMENT_RAISE_GOODS_SERVICES_PROVIDED: ResolveDisputeAdjustment.ReasonCode
    PRE_ARBITRATION_DECLINED_SERVICES_PROVIDED_LATER: ResolveDisputeAdjustment.ReasonCode
    PRE_ARBITRATION_ACCEPTANCE_SERVICES_NOT_PROVIDED_BY_MERCHANT: ResolveDisputeAdjustment.ReasonCode
    ARBITRATION_ACCEPTANCE_ILLEGIBLE_FULFILMENT: ResolveDisputeAdjustment.ReasonCode
    ARBITRATION_CONTINUATION_CUSTOMER_STILL_NOT_RECEIVED_SERVICE: ResolveDisputeAdjustment.ReasonCode
    ARBITRATION_WITHDRAWN_CUSTOMER_RECEIVED_SERVICE_LATER: ResolveDisputeAdjustment.ReasonCode
    ARBITRATION_VERDICT_PANEL_VERDICT: ResolveDisputeAdjustment.ReasonCode
    MANUAL_ADJUSTMENT_REASON: ResolveDisputeAdjustment.ReasonCode
    ATTRIBUTING_CUSTOMER: ResolveDisputeAdjustment.ReasonCode
    ATTRIBUTING_TECHNICAL_ISSUE: ResolveDisputeAdjustment.ReasonCode
    WRONG_CREDIT_CHARGEBACK_ACCEPTANCE_AMOUNT_RECOVERED: ResolveDisputeAdjustment.ReasonCode
    WRONG_CREDIT_REPRESENTMENT_LIEN_MARKED_INSUFFICIENT_BALANCE: ResolveDisputeAdjustment.ReasonCode
    WRONG_CREDIT_REPRESENTMENT_CUSTOMER_INACCESSIBLE: ResolveDisputeAdjustment.ReasonCode
    WRONG_CREDIT_REPRESENTMENT_REASON_OTHERS: ResolveDisputeAdjustment.ReasonCode
    ADJUSTMENT_FLAG_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_CODE_FIELD_NUMBER: _ClassVar[int]
    adjustment_flag: ResolveDisputeAdjustment.AdjustmentFlag
    adjustment_code: ResolveDisputeAdjustment.ReasonCode

    def __init__(self, adjustment_flag: _Optional[_Union[ResolveDisputeAdjustment.AdjustmentFlag, str]]=..., adjustment_code: _Optional[_Union[ResolveDisputeAdjustment.ReasonCode, str]]=...) -> None:
        ...

class CreateComplaintMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResolveComplaintMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateDisputeMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResolveDisputeMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...