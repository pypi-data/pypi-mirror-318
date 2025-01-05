from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccountManagerTransactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNT_MANAGER_TRANSACTION_TYPE_UNSPECIFIED: _ClassVar[AccountManagerTransactionType]
    CREDIT: _ClassVar[AccountManagerTransactionType]
    CREDIT_REVERSAL: _ClassVar[AccountManagerTransactionType]
    DEBIT: _ClassVar[AccountManagerTransactionType]
    DEBIT_REVERSAL: _ClassVar[AccountManagerTransactionType]
ACCOUNT_MANAGER_TRANSACTION_TYPE_UNSPECIFIED: AccountManagerTransactionType
CREDIT: AccountManagerTransactionType
CREDIT_REVERSAL: AccountManagerTransactionType
DEBIT: AccountManagerTransactionType
DEBIT_REVERSAL: AccountManagerTransactionType

class AccountManagerTransaction(_message.Message):
    __slots__ = ('name', 'account_id', 'info', 'payer', 'payee', 'reconciliation_info', 'amount')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    PAYER_FIELD_NUMBER: _ClassVar[int]
    PAYEE_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_INFO_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_id: str
    info: AccountManagerTransactionInfo
    payer: AccountManagerSettlementParticipant
    payee: AccountManagerSettlementParticipant
    reconciliation_info: AccountManagerTransactionReconciliationInfo
    amount: _money_pb2.Money

    def __init__(self, name: _Optional[str]=..., account_id: _Optional[str]=..., info: _Optional[_Union[AccountManagerTransactionInfo, _Mapping]]=..., payer: _Optional[_Union[AccountManagerSettlementParticipant, _Mapping]]=..., payee: _Optional[_Union[AccountManagerSettlementParticipant, _Mapping]]=..., reconciliation_info: _Optional[_Union[AccountManagerTransactionReconciliationInfo, _Mapping]]=..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
        ...

class AccountManagerTransactionInfo(_message.Message):
    __slots__ = ('id', 'transaction_type', 'state', 'metadata', 'error_details')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AccountManagerTransactionInfo.State]
        SUCCEEDED: _ClassVar[AccountManagerTransactionInfo.State]
        FAILED: _ClassVar[AccountManagerTransactionInfo.State]
    STATE_UNSPECIFIED: AccountManagerTransactionInfo.State
    SUCCEEDED: AccountManagerTransactionInfo.State
    FAILED: AccountManagerTransactionInfo.State

    class AccountManagerTransactionMetadata(_message.Message):
        __slots__ = ('transaction_time', 'create_time', 'update_time', 'retrieval_reference_number', 'initiation_mode', 'purpose_code')
        TRANSACTION_TIME_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        RETRIEVAL_REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        INITIATION_MODE_FIELD_NUMBER: _ClassVar[int]
        PURPOSE_CODE_FIELD_NUMBER: _ClassVar[int]
        transaction_time: _timestamp_pb2.Timestamp
        create_time: _timestamp_pb2.Timestamp
        update_time: _timestamp_pb2.Timestamp
        retrieval_reference_number: str
        initiation_mode: str
        purpose_code: str

        def __init__(self, transaction_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., retrieval_reference_number: _Optional[str]=..., initiation_mode: _Optional[str]=..., purpose_code: _Optional[str]=...) -> None:
            ...

    class AccountManagerTransactionErrorDetails(_message.Message):
        __slots__ = ('error_code', 'error_message')
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_code: str
        error_message: str

        def __init__(self, error_code: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    transaction_type: AccountManagerTransactionType
    state: AccountManagerTransactionInfo.State
    metadata: AccountManagerTransactionInfo.AccountManagerTransactionMetadata
    error_details: AccountManagerTransactionInfo.AccountManagerTransactionErrorDetails

    def __init__(self, id: _Optional[str]=..., transaction_type: _Optional[_Union[AccountManagerTransactionType, str]]=..., state: _Optional[_Union[AccountManagerTransactionInfo.State, str]]=..., metadata: _Optional[_Union[AccountManagerTransactionInfo.AccountManagerTransactionMetadata, _Mapping]]=..., error_details: _Optional[_Union[AccountManagerTransactionInfo.AccountManagerTransactionErrorDetails, _Mapping]]=...) -> None:
        ...

class AccountManagerSettlementParticipant(_message.Message):
    __slots__ = ('participant', 'merchant_info')
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_INFO_FIELD_NUMBER: _ClassVar[int]
    participant: AccountManagerParticipant
    merchant_info: AccountManagerMerchantInfo

    def __init__(self, participant: _Optional[_Union[AccountManagerParticipant, _Mapping]]=..., merchant_info: _Optional[_Union[AccountManagerMerchantInfo, _Mapping]]=...) -> None:
        ...

class AccountManagerParticipant(_message.Message):
    __slots__ = ('payment_address', 'persona', 'account')

    class Persona(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSONA_UNSPECIFIED: _ClassVar[AccountManagerParticipant.Persona]
        ENTITY: _ClassVar[AccountManagerParticipant.Persona]
        PERSON: _ClassVar[AccountManagerParticipant.Persona]
    PERSONA_UNSPECIFIED: AccountManagerParticipant.Persona
    ENTITY: AccountManagerParticipant.Persona
    PERSON: AccountManagerParticipant.Persona
    PAYMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PERSONA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    payment_address: str
    persona: AccountManagerParticipant.Persona
    account: _common_fields_pb2.AccountReference

    def __init__(self, payment_address: _Optional[str]=..., persona: _Optional[_Union[AccountManagerParticipant.Persona, str]]=..., account: _Optional[_Union[_common_fields_pb2.AccountReference, _Mapping]]=...) -> None:
        ...

class AccountManagerMerchantInfo(_message.Message):
    __slots__ = ('category_code', 'id')
    CATEGORY_CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    category_code: str
    id: str

    def __init__(self, category_code: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...

class AccountManagerTransactionReconciliationInfo(_message.Message):
    __slots__ = ('state', 'reconciliation_time')

    class ReconciliationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECONCILIATION_STATE_UNSPECIFIED: _ClassVar[AccountManagerTransactionReconciliationInfo.ReconciliationState]
        SUCCEEDED: _ClassVar[AccountManagerTransactionReconciliationInfo.ReconciliationState]
        FAILED: _ClassVar[AccountManagerTransactionReconciliationInfo.ReconciliationState]
    RECONCILIATION_STATE_UNSPECIFIED: AccountManagerTransactionReconciliationInfo.ReconciliationState
    SUCCEEDED: AccountManagerTransactionReconciliationInfo.ReconciliationState
    FAILED: AccountManagerTransactionReconciliationInfo.ReconciliationState
    STATE_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_TIME_FIELD_NUMBER: _ClassVar[int]
    state: AccountManagerTransactionReconciliationInfo.ReconciliationState
    reconciliation_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[AccountManagerTransactionReconciliationInfo.ReconciliationState, str]]=..., reconciliation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportAccountManagerTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'transaction_type', 'start_time', 'end_time')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    transaction_type: AccountManagerTransactionType
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., transaction_type: _Optional[_Union[AccountManagerTransactionType, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAccountManagerTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListAccountManagerTransactionsResponse(_message.Message):
    __slots__ = ('account_manager_transactions', 'next_page_token')
    ACCOUNT_MANAGER_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_manager_transactions: _containers.RepeatedCompositeFieldContainer[AccountManagerTransaction]
    next_page_token: str

    def __init__(self, account_manager_transactions: _Optional[_Iterable[_Union[AccountManagerTransaction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ReconcileAccountManagerTransactionsRequest(_message.Message):
    __slots__ = ('transaction',)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: AccountManagerTransaction

    def __init__(self, transaction: _Optional[_Union[AccountManagerTransaction, _Mapping]]=...) -> None:
        ...

class BatchReconcileAccountManagerTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[ReconcileAccountManagerTransactionsRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[ReconcileAccountManagerTransactionsRequest, _Mapping]]]=...) -> None:
        ...

class BatchReconcileAccountManagerTransactionsResponse(_message.Message):
    __slots__ = ('account_manager_transactions',)
    ACCOUNT_MANAGER_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    account_manager_transactions: _containers.RepeatedCompositeFieldContainer[AccountManagerTransaction]

    def __init__(self, account_manager_transactions: _Optional[_Iterable[_Union[AccountManagerTransaction, _Mapping]]]=...) -> None:
        ...