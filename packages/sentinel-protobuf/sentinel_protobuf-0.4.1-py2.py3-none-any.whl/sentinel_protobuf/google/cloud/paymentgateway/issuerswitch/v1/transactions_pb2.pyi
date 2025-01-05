from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import resolutions_pb2 as _resolutions_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransactionInfo(_message.Message):
    __slots__ = ('id', 'api_type', 'transaction_type', 'transaction_sub_type', 'state', 'metadata', 'error_details', 'adapter_info', 'risk_info')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[TransactionInfo.State]
        SUCCEEDED: _ClassVar[TransactionInfo.State]
        FAILED: _ClassVar[TransactionInfo.State]
        TIMED_OUT: _ClassVar[TransactionInfo.State]
    STATE_UNSPECIFIED: TransactionInfo.State
    SUCCEEDED: TransactionInfo.State
    FAILED: TransactionInfo.State
    TIMED_OUT: TransactionInfo.State

    class TransactionSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSACTION_SUB_TYPE_UNSPECIFIED: _ClassVar[TransactionInfo.TransactionSubType]
        COLLECT: _ClassVar[TransactionInfo.TransactionSubType]
        DEBIT: _ClassVar[TransactionInfo.TransactionSubType]
        PAY: _ClassVar[TransactionInfo.TransactionSubType]
        BENEFICIARY: _ClassVar[TransactionInfo.TransactionSubType]
        REMITTER: _ClassVar[TransactionInfo.TransactionSubType]
        REFUND: _ClassVar[TransactionInfo.TransactionSubType]
        CREDIT: _ClassVar[TransactionInfo.TransactionSubType]
    TRANSACTION_SUB_TYPE_UNSPECIFIED: TransactionInfo.TransactionSubType
    COLLECT: TransactionInfo.TransactionSubType
    DEBIT: TransactionInfo.TransactionSubType
    PAY: TransactionInfo.TransactionSubType
    BENEFICIARY: TransactionInfo.TransactionSubType
    REMITTER: TransactionInfo.TransactionSubType
    REFUND: TransactionInfo.TransactionSubType
    CREDIT: TransactionInfo.TransactionSubType

    class TransactionMetadata(_message.Message):
        __slots__ = ('create_time', 'update_time', 'reference_id', 'reference_uri', 'description', 'initiation_mode', 'purpose_code', 'reference_category')
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_URI_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INITIATION_MODE_FIELD_NUMBER: _ClassVar[int]
        PURPOSE_CODE_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        create_time: _timestamp_pb2.Timestamp
        update_time: _timestamp_pb2.Timestamp
        reference_id: str
        reference_uri: str
        description: str
        initiation_mode: str
        purpose_code: str
        reference_category: str

        def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., reference_id: _Optional[str]=..., reference_uri: _Optional[str]=..., description: _Optional[str]=..., initiation_mode: _Optional[str]=..., purpose_code: _Optional[str]=..., reference_category: _Optional[str]=...) -> None:
            ...

    class TransactionErrorDetails(_message.Message):
        __slots__ = ('error_code', 'error_message', 'upi_error_code')
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        UPI_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        error_code: str
        error_message: str
        upi_error_code: str

        def __init__(self, error_code: _Optional[str]=..., error_message: _Optional[str]=..., upi_error_code: _Optional[str]=...) -> None:
            ...

    class AdapterInfo(_message.Message):
        __slots__ = ('request_ids', 'response_metadata')

        class ResponseMetadata(_message.Message):
            __slots__ = ('values',)

            class ValuesEntry(_message.Message):
                __slots__ = ('key', 'value')
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str

                def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                    ...
            VALUES_FIELD_NUMBER: _ClassVar[int]
            values: _containers.ScalarMap[str, str]

            def __init__(self, values: _Optional[_Mapping[str, str]]=...) -> None:
                ...
        REQUEST_IDS_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_METADATA_FIELD_NUMBER: _ClassVar[int]
        request_ids: str
        response_metadata: TransactionInfo.AdapterInfo.ResponseMetadata

        def __init__(self, request_ids: _Optional[str]=..., response_metadata: _Optional[_Union[TransactionInfo.AdapterInfo.ResponseMetadata, _Mapping]]=...) -> None:
            ...

    class TransactionRiskInfo(_message.Message):
        __slots__ = ('provider', 'type', 'value')
        PROVIDER_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        provider: str
        type: str
        value: str

        def __init__(self, provider: _Optional[str]=..., type: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    API_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_INFO_FIELD_NUMBER: _ClassVar[int]
    RISK_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    api_type: _common_fields_pb2.ApiType
    transaction_type: _common_fields_pb2.TransactionType
    transaction_sub_type: TransactionInfo.TransactionSubType
    state: TransactionInfo.State
    metadata: TransactionInfo.TransactionMetadata
    error_details: TransactionInfo.TransactionErrorDetails
    adapter_info: TransactionInfo.AdapterInfo
    risk_info: _containers.RepeatedCompositeFieldContainer[TransactionInfo.TransactionRiskInfo]

    def __init__(self, id: _Optional[str]=..., api_type: _Optional[_Union[_common_fields_pb2.ApiType, str]]=..., transaction_type: _Optional[_Union[_common_fields_pb2.TransactionType, str]]=..., transaction_sub_type: _Optional[_Union[TransactionInfo.TransactionSubType, str]]=..., state: _Optional[_Union[TransactionInfo.State, str]]=..., metadata: _Optional[_Union[TransactionInfo.TransactionMetadata, _Mapping]]=..., error_details: _Optional[_Union[TransactionInfo.TransactionErrorDetails, _Mapping]]=..., adapter_info: _Optional[_Union[TransactionInfo.AdapterInfo, _Mapping]]=..., risk_info: _Optional[_Iterable[_Union[TransactionInfo.TransactionRiskInfo, _Mapping]]]=...) -> None:
        ...

class MetadataTransaction(_message.Message):
    __slots__ = ('name', 'info', 'initiator')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    info: TransactionInfo
    initiator: _common_fields_pb2.Participant

    def __init__(self, name: _Optional[str]=..., info: _Optional[_Union[TransactionInfo, _Mapping]]=..., initiator: _Optional[_Union[_common_fields_pb2.Participant, _Mapping]]=...) -> None:
        ...

class FinancialTransaction(_message.Message):
    __slots__ = ('name', 'info', 'retrieval_reference_number', 'payer', 'payee', 'amount', 'payment_rules')

    class PaymentRule(_message.Message):
        __slots__ = ('payment_rule', 'value')

        class PaymentRuleName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PAYMENT_RULE_NAME_UNSPECIFIED: _ClassVar[FinancialTransaction.PaymentRule.PaymentRuleName]
            EXPIRE_AFTER: _ClassVar[FinancialTransaction.PaymentRule.PaymentRuleName]
            MIN_AMOUNT: _ClassVar[FinancialTransaction.PaymentRule.PaymentRuleName]
        PAYMENT_RULE_NAME_UNSPECIFIED: FinancialTransaction.PaymentRule.PaymentRuleName
        EXPIRE_AFTER: FinancialTransaction.PaymentRule.PaymentRuleName
        MIN_AMOUNT: FinancialTransaction.PaymentRule.PaymentRuleName
        PAYMENT_RULE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        payment_rule: FinancialTransaction.PaymentRule.PaymentRuleName
        value: str

        def __init__(self, payment_rule: _Optional[_Union[FinancialTransaction.PaymentRule.PaymentRuleName, str]]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAYER_FIELD_NUMBER: _ClassVar[int]
    PAYEE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    info: TransactionInfo
    retrieval_reference_number: str
    payer: _common_fields_pb2.SettlementParticipant
    payee: _common_fields_pb2.SettlementParticipant
    amount: _money_pb2.Money
    payment_rules: _containers.RepeatedCompositeFieldContainer[FinancialTransaction.PaymentRule]

    def __init__(self, name: _Optional[str]=..., info: _Optional[_Union[TransactionInfo, _Mapping]]=..., retrieval_reference_number: _Optional[str]=..., payer: _Optional[_Union[_common_fields_pb2.SettlementParticipant, _Mapping]]=..., payee: _Optional[_Union[_common_fields_pb2.SettlementParticipant, _Mapping]]=..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., payment_rules: _Optional[_Iterable[_Union[FinancialTransaction.PaymentRule, _Mapping]]]=...) -> None:
        ...

class MandateTransaction(_message.Message):
    __slots__ = ('name', 'transaction_info', 'unique_mandate_number', 'payer', 'payee', 'recurrence_pattern', 'recurrence_rule_type', 'recurrence_rule_value', 'start_date', 'end_date', 'revokable', 'amount', 'amount_rule', 'approval_reference', 'block_funds', 'mandate_name')

    class RecurrencePatternType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECURRENCE_PATTERN_TYPE_UNSPECIFIED: _ClassVar[MandateTransaction.RecurrencePatternType]
        AS_PRESENTED: _ClassVar[MandateTransaction.RecurrencePatternType]
        BIMONTHLY: _ClassVar[MandateTransaction.RecurrencePatternType]
        DAILY: _ClassVar[MandateTransaction.RecurrencePatternType]
        FORTNIGHTLY: _ClassVar[MandateTransaction.RecurrencePatternType]
        HALF_YEARLY: _ClassVar[MandateTransaction.RecurrencePatternType]
        MONTHLY: _ClassVar[MandateTransaction.RecurrencePatternType]
        ONE_TIME: _ClassVar[MandateTransaction.RecurrencePatternType]
        QUARTERLY: _ClassVar[MandateTransaction.RecurrencePatternType]
        WEEKLY: _ClassVar[MandateTransaction.RecurrencePatternType]
        YEARLY: _ClassVar[MandateTransaction.RecurrencePatternType]
    RECURRENCE_PATTERN_TYPE_UNSPECIFIED: MandateTransaction.RecurrencePatternType
    AS_PRESENTED: MandateTransaction.RecurrencePatternType
    BIMONTHLY: MandateTransaction.RecurrencePatternType
    DAILY: MandateTransaction.RecurrencePatternType
    FORTNIGHTLY: MandateTransaction.RecurrencePatternType
    HALF_YEARLY: MandateTransaction.RecurrencePatternType
    MONTHLY: MandateTransaction.RecurrencePatternType
    ONE_TIME: MandateTransaction.RecurrencePatternType
    QUARTERLY: MandateTransaction.RecurrencePatternType
    WEEKLY: MandateTransaction.RecurrencePatternType
    YEARLY: MandateTransaction.RecurrencePatternType

    class RecurrenceRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECURRENCE_RULE_TYPE_UNSPECIFIED: _ClassVar[MandateTransaction.RecurrenceRuleType]
        AFTER: _ClassVar[MandateTransaction.RecurrenceRuleType]
        BEFORE: _ClassVar[MandateTransaction.RecurrenceRuleType]
        ON: _ClassVar[MandateTransaction.RecurrenceRuleType]
    RECURRENCE_RULE_TYPE_UNSPECIFIED: MandateTransaction.RecurrenceRuleType
    AFTER: MandateTransaction.RecurrenceRuleType
    BEFORE: MandateTransaction.RecurrenceRuleType
    ON: MandateTransaction.RecurrenceRuleType

    class AmountRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AMOUNT_RULE_TYPE_UNSPECIFIED: _ClassVar[MandateTransaction.AmountRuleType]
        EXACT: _ClassVar[MandateTransaction.AmountRuleType]
        MAX: _ClassVar[MandateTransaction.AmountRuleType]
    AMOUNT_RULE_TYPE_UNSPECIFIED: MandateTransaction.AmountRuleType
    EXACT: MandateTransaction.AmountRuleType
    MAX: MandateTransaction.AmountRuleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_INFO_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_MANDATE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAYER_FIELD_NUMBER: _ClassVar[int]
    PAYEE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_RULE_VALUE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    REVOKABLE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RULE_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FUNDS_FIELD_NUMBER: _ClassVar[int]
    MANDATE_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    transaction_info: TransactionInfo
    unique_mandate_number: str
    payer: _common_fields_pb2.SettlementParticipant
    payee: _common_fields_pb2.SettlementParticipant
    recurrence_pattern: MandateTransaction.RecurrencePatternType
    recurrence_rule_type: MandateTransaction.RecurrenceRuleType
    recurrence_rule_value: int
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date
    revokable: bool
    amount: float
    amount_rule: MandateTransaction.AmountRuleType
    approval_reference: str
    block_funds: bool
    mandate_name: str

    def __init__(self, name: _Optional[str]=..., transaction_info: _Optional[_Union[TransactionInfo, _Mapping]]=..., unique_mandate_number: _Optional[str]=..., payer: _Optional[_Union[_common_fields_pb2.SettlementParticipant, _Mapping]]=..., payee: _Optional[_Union[_common_fields_pb2.SettlementParticipant, _Mapping]]=..., recurrence_pattern: _Optional[_Union[MandateTransaction.RecurrencePatternType, str]]=..., recurrence_rule_type: _Optional[_Union[MandateTransaction.RecurrenceRuleType, str]]=..., recurrence_rule_value: _Optional[int]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., revokable: bool=..., amount: _Optional[float]=..., amount_rule: _Optional[_Union[MandateTransaction.AmountRuleType, str]]=..., approval_reference: _Optional[str]=..., block_funds: bool=..., mandate_name: _Optional[str]=...) -> None:
        ...

class ComplaintTransaction(_message.Message):
    __slots__ = ('name', 'info', 'complaint', 'dispute')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    COMPLAINT_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    name: str
    info: TransactionInfo
    complaint: _resolutions_pb2.Complaint
    dispute: _resolutions_pb2.Dispute

    def __init__(self, name: _Optional[str]=..., info: _Optional[_Union[TransactionInfo, _Mapping]]=..., complaint: _Optional[_Union[_resolutions_pb2.Complaint, _Mapping]]=..., dispute: _Optional[_Union[_resolutions_pb2.Dispute, _Mapping]]=...) -> None:
        ...

class ListMetadataTransactionsRequest(_message.Message):
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

class ListFinancialTransactionsRequest(_message.Message):
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

class ListMandateTransactionsRequest(_message.Message):
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

class ListComplaintTransactionsRequest(_message.Message):
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

class ListMetadataTransactionsResponse(_message.Message):
    __slots__ = ('metadata_transactions', 'next_page_token')
    METADATA_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metadata_transactions: _containers.RepeatedCompositeFieldContainer[MetadataTransaction]
    next_page_token: str

    def __init__(self, metadata_transactions: _Optional[_Iterable[_Union[MetadataTransaction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListFinancialTransactionsResponse(_message.Message):
    __slots__ = ('financial_transactions', 'next_page_token')
    FINANCIAL_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    financial_transactions: _containers.RepeatedCompositeFieldContainer[FinancialTransaction]
    next_page_token: str

    def __init__(self, financial_transactions: _Optional[_Iterable[_Union[FinancialTransaction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListMandateTransactionsResponse(_message.Message):
    __slots__ = ('mandate_transactions', 'next_page_token')
    MANDATE_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    mandate_transactions: _containers.RepeatedCompositeFieldContainer[MandateTransaction]
    next_page_token: str

    def __init__(self, mandate_transactions: _Optional[_Iterable[_Union[MandateTransaction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListComplaintTransactionsResponse(_message.Message):
    __slots__ = ('complaint_transactions', 'next_page_token')
    COMPLAINT_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    complaint_transactions: _containers.RepeatedCompositeFieldContainer[ComplaintTransaction]
    next_page_token: str

    def __init__(self, complaint_transactions: _Optional[_Iterable[_Union[ComplaintTransaction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ExportFinancialTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'transaction_type', 'start_time', 'end_time')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    transaction_type: _common_fields_pb2.TransactionType
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., transaction_type: _Optional[_Union[_common_fields_pb2.TransactionType, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportMetadataTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'api_type', 'start_time', 'end_time')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_type: _common_fields_pb2.ApiType
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., api_type: _Optional[_Union[_common_fields_pb2.ApiType, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportMandateTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'transaction_type', 'start_time', 'end_time')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    transaction_type: _common_fields_pb2.TransactionType
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., transaction_type: _Optional[_Union[_common_fields_pb2.TransactionType, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportComplaintTransactionsRequest(_message.Message):
    __slots__ = ('parent', 'transaction_type', 'start_time', 'end_time')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    transaction_type: _common_fields_pb2.TransactionType
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., transaction_type: _Optional[_Union[_common_fields_pb2.TransactionType, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportFinancialTransactionsResponse(_message.Message):
    __slots__ = ('target_uri',)
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    target_uri: str

    def __init__(self, target_uri: _Optional[str]=...) -> None:
        ...

class ExportMetadataTransactionsResponse(_message.Message):
    __slots__ = ('target_uri',)
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    target_uri: str

    def __init__(self, target_uri: _Optional[str]=...) -> None:
        ...

class ExportMandateTransactionsResponse(_message.Message):
    __slots__ = ('target_uri',)
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    target_uri: str

    def __init__(self, target_uri: _Optional[str]=...) -> None:
        ...

class ExportComplaintTransactionsResponse(_message.Message):
    __slots__ = ('target_uri',)
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    target_uri: str

    def __init__(self, target_uri: _Optional[str]=...) -> None:
        ...

class ExportFinancialTransactionsMetadata(_message.Message):
    __slots__ = ('create_time',)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportMandateTransactionsMetadata(_message.Message):
    __slots__ = ('create_time',)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportMetadataTransactionsMetadata(_message.Message):
    __slots__ = ('create_time',)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportComplaintTransactionsMetadata(_message.Message):
    __slots__ = ('create_time',)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...