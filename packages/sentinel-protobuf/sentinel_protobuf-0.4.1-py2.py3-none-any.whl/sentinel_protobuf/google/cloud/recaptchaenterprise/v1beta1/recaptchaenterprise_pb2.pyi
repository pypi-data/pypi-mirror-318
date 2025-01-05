from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAssessmentRequest(_message.Message):
    __slots__ = ("parent", "assessment")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    assessment: Assessment
    def __init__(self, parent: _Optional[str] = ..., assessment: _Optional[_Union[Assessment, _Mapping]] = ...) -> None: ...

class TransactionEvent(_message.Message):
    __slots__ = ("event_type", "reason", "value", "event_time")
    class TransactionEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSACTION_EVENT_TYPE_UNSPECIFIED: _ClassVar[TransactionEvent.TransactionEventType]
        MERCHANT_APPROVE: _ClassVar[TransactionEvent.TransactionEventType]
        MERCHANT_DENY: _ClassVar[TransactionEvent.TransactionEventType]
        MANUAL_REVIEW: _ClassVar[TransactionEvent.TransactionEventType]
        AUTHORIZATION: _ClassVar[TransactionEvent.TransactionEventType]
        AUTHORIZATION_DECLINE: _ClassVar[TransactionEvent.TransactionEventType]
        PAYMENT_CAPTURE: _ClassVar[TransactionEvent.TransactionEventType]
        PAYMENT_CAPTURE_DECLINE: _ClassVar[TransactionEvent.TransactionEventType]
        CANCEL: _ClassVar[TransactionEvent.TransactionEventType]
        CHARGEBACK_INQUIRY: _ClassVar[TransactionEvent.TransactionEventType]
        CHARGEBACK_ALERT: _ClassVar[TransactionEvent.TransactionEventType]
        FRAUD_NOTIFICATION: _ClassVar[TransactionEvent.TransactionEventType]
        CHARGEBACK: _ClassVar[TransactionEvent.TransactionEventType]
        CHARGEBACK_REPRESENTMENT: _ClassVar[TransactionEvent.TransactionEventType]
        CHARGEBACK_REVERSE: _ClassVar[TransactionEvent.TransactionEventType]
        REFUND_REQUEST: _ClassVar[TransactionEvent.TransactionEventType]
        REFUND_DECLINE: _ClassVar[TransactionEvent.TransactionEventType]
        REFUND: _ClassVar[TransactionEvent.TransactionEventType]
        REFUND_REVERSE: _ClassVar[TransactionEvent.TransactionEventType]
    TRANSACTION_EVENT_TYPE_UNSPECIFIED: TransactionEvent.TransactionEventType
    MERCHANT_APPROVE: TransactionEvent.TransactionEventType
    MERCHANT_DENY: TransactionEvent.TransactionEventType
    MANUAL_REVIEW: TransactionEvent.TransactionEventType
    AUTHORIZATION: TransactionEvent.TransactionEventType
    AUTHORIZATION_DECLINE: TransactionEvent.TransactionEventType
    PAYMENT_CAPTURE: TransactionEvent.TransactionEventType
    PAYMENT_CAPTURE_DECLINE: TransactionEvent.TransactionEventType
    CANCEL: TransactionEvent.TransactionEventType
    CHARGEBACK_INQUIRY: TransactionEvent.TransactionEventType
    CHARGEBACK_ALERT: TransactionEvent.TransactionEventType
    FRAUD_NOTIFICATION: TransactionEvent.TransactionEventType
    CHARGEBACK: TransactionEvent.TransactionEventType
    CHARGEBACK_REPRESENTMENT: TransactionEvent.TransactionEventType
    CHARGEBACK_REVERSE: TransactionEvent.TransactionEventType
    REFUND_REQUEST: TransactionEvent.TransactionEventType
    REFUND_DECLINE: TransactionEvent.TransactionEventType
    REFUND: TransactionEvent.TransactionEventType
    REFUND_REVERSE: TransactionEvent.TransactionEventType
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    event_type: TransactionEvent.TransactionEventType
    reason: str
    value: float
    event_time: _timestamp_pb2.Timestamp
    def __init__(self, event_type: _Optional[_Union[TransactionEvent.TransactionEventType, str]] = ..., reason: _Optional[str] = ..., value: _Optional[float] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AnnotateAssessmentRequest(_message.Message):
    __slots__ = ("name", "annotation", "reasons", "hashed_account_id", "transaction_event")
    class Annotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANNOTATION_UNSPECIFIED: _ClassVar[AnnotateAssessmentRequest.Annotation]
        LEGITIMATE: _ClassVar[AnnotateAssessmentRequest.Annotation]
        FRAUDULENT: _ClassVar[AnnotateAssessmentRequest.Annotation]
        PASSWORD_CORRECT: _ClassVar[AnnotateAssessmentRequest.Annotation]
        PASSWORD_INCORRECT: _ClassVar[AnnotateAssessmentRequest.Annotation]
    ANNOTATION_UNSPECIFIED: AnnotateAssessmentRequest.Annotation
    LEGITIMATE: AnnotateAssessmentRequest.Annotation
    FRAUDULENT: AnnotateAssessmentRequest.Annotation
    PASSWORD_CORRECT: AnnotateAssessmentRequest.Annotation
    PASSWORD_INCORRECT: AnnotateAssessmentRequest.Annotation
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[AnnotateAssessmentRequest.Reason]
        CHARGEBACK: _ClassVar[AnnotateAssessmentRequest.Reason]
        CHARGEBACK_FRAUD: _ClassVar[AnnotateAssessmentRequest.Reason]
        CHARGEBACK_DISPUTE: _ClassVar[AnnotateAssessmentRequest.Reason]
        REFUND: _ClassVar[AnnotateAssessmentRequest.Reason]
        REFUND_FRAUD: _ClassVar[AnnotateAssessmentRequest.Reason]
        TRANSACTION_ACCEPTED: _ClassVar[AnnotateAssessmentRequest.Reason]
        TRANSACTION_DECLINED: _ClassVar[AnnotateAssessmentRequest.Reason]
        PAYMENT_HEURISTICS: _ClassVar[AnnotateAssessmentRequest.Reason]
        INITIATED_TWO_FACTOR: _ClassVar[AnnotateAssessmentRequest.Reason]
        PASSED_TWO_FACTOR: _ClassVar[AnnotateAssessmentRequest.Reason]
        FAILED_TWO_FACTOR: _ClassVar[AnnotateAssessmentRequest.Reason]
        CORRECT_PASSWORD: _ClassVar[AnnotateAssessmentRequest.Reason]
        INCORRECT_PASSWORD: _ClassVar[AnnotateAssessmentRequest.Reason]
        SOCIAL_SPAM: _ClassVar[AnnotateAssessmentRequest.Reason]
    REASON_UNSPECIFIED: AnnotateAssessmentRequest.Reason
    CHARGEBACK: AnnotateAssessmentRequest.Reason
    CHARGEBACK_FRAUD: AnnotateAssessmentRequest.Reason
    CHARGEBACK_DISPUTE: AnnotateAssessmentRequest.Reason
    REFUND: AnnotateAssessmentRequest.Reason
    REFUND_FRAUD: AnnotateAssessmentRequest.Reason
    TRANSACTION_ACCEPTED: AnnotateAssessmentRequest.Reason
    TRANSACTION_DECLINED: AnnotateAssessmentRequest.Reason
    PAYMENT_HEURISTICS: AnnotateAssessmentRequest.Reason
    INITIATED_TWO_FACTOR: AnnotateAssessmentRequest.Reason
    PASSED_TWO_FACTOR: AnnotateAssessmentRequest.Reason
    FAILED_TWO_FACTOR: AnnotateAssessmentRequest.Reason
    CORRECT_PASSWORD: AnnotateAssessmentRequest.Reason
    INCORRECT_PASSWORD: AnnotateAssessmentRequest.Reason
    SOCIAL_SPAM: AnnotateAssessmentRequest.Reason
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    HASHED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    annotation: AnnotateAssessmentRequest.Annotation
    reasons: _containers.RepeatedScalarFieldContainer[AnnotateAssessmentRequest.Reason]
    hashed_account_id: bytes
    transaction_event: TransactionEvent
    def __init__(self, name: _Optional[str] = ..., annotation: _Optional[_Union[AnnotateAssessmentRequest.Annotation, str]] = ..., reasons: _Optional[_Iterable[_Union[AnnotateAssessmentRequest.Reason, str]]] = ..., hashed_account_id: _Optional[bytes] = ..., transaction_event: _Optional[_Union[TransactionEvent, _Mapping]] = ...) -> None: ...

class AnnotateAssessmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PasswordLeakVerification(_message.Message):
    __slots__ = ("hashed_user_credentials", "credentials_leaked", "canonicalized_username")
    HASHED_USER_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_LEAKED_FIELD_NUMBER: _ClassVar[int]
    CANONICALIZED_USERNAME_FIELD_NUMBER: _ClassVar[int]
    hashed_user_credentials: bytes
    credentials_leaked: bool
    canonicalized_username: str
    def __init__(self, hashed_user_credentials: _Optional[bytes] = ..., credentials_leaked: bool = ..., canonicalized_username: _Optional[str] = ...) -> None: ...

class Assessment(_message.Message):
    __slots__ = ("name", "event", "score", "token_properties", "reasons", "password_leak_verification", "account_defender_assessment", "fraud_prevention_assessment")
    class ClassificationReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLASSIFICATION_REASON_UNSPECIFIED: _ClassVar[Assessment.ClassificationReason]
        AUTOMATION: _ClassVar[Assessment.ClassificationReason]
        UNEXPECTED_ENVIRONMENT: _ClassVar[Assessment.ClassificationReason]
        TOO_MUCH_TRAFFIC: _ClassVar[Assessment.ClassificationReason]
        UNEXPECTED_USAGE_PATTERNS: _ClassVar[Assessment.ClassificationReason]
        LOW_CONFIDENCE_SCORE: _ClassVar[Assessment.ClassificationReason]
        SUSPECTED_CARDING: _ClassVar[Assessment.ClassificationReason]
        SUSPECTED_CHARGEBACK: _ClassVar[Assessment.ClassificationReason]
    CLASSIFICATION_REASON_UNSPECIFIED: Assessment.ClassificationReason
    AUTOMATION: Assessment.ClassificationReason
    UNEXPECTED_ENVIRONMENT: Assessment.ClassificationReason
    TOO_MUCH_TRAFFIC: Assessment.ClassificationReason
    UNEXPECTED_USAGE_PATTERNS: Assessment.ClassificationReason
    LOW_CONFIDENCE_SCORE: Assessment.ClassificationReason
    SUSPECTED_CARDING: Assessment.ClassificationReason
    SUSPECTED_CHARGEBACK: Assessment.ClassificationReason
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_LEAK_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DEFENDER_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    FRAUD_PREVENTION_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    event: Event
    score: float
    token_properties: TokenProperties
    reasons: _containers.RepeatedScalarFieldContainer[Assessment.ClassificationReason]
    password_leak_verification: PasswordLeakVerification
    account_defender_assessment: AccountDefenderAssessment
    fraud_prevention_assessment: FraudPreventionAssessment
    def __init__(self, name: _Optional[str] = ..., event: _Optional[_Union[Event, _Mapping]] = ..., score: _Optional[float] = ..., token_properties: _Optional[_Union[TokenProperties, _Mapping]] = ..., reasons: _Optional[_Iterable[_Union[Assessment.ClassificationReason, str]]] = ..., password_leak_verification: _Optional[_Union[PasswordLeakVerification, _Mapping]] = ..., account_defender_assessment: _Optional[_Union[AccountDefenderAssessment, _Mapping]] = ..., fraud_prevention_assessment: _Optional[_Union[FraudPreventionAssessment, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("token", "site_key", "user_agent", "user_ip_address", "expected_action", "hashed_account_id", "transaction_data", "fraud_prevention")
    class FraudPrevention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FRAUD_PREVENTION_UNSPECIFIED: _ClassVar[Event.FraudPrevention]
        ENABLED: _ClassVar[Event.FraudPrevention]
        DISABLED: _ClassVar[Event.FraudPrevention]
    FRAUD_PREVENTION_UNSPECIFIED: Event.FraudPrevention
    ENABLED: Event.FraudPrevention
    DISABLED: Event.FraudPrevention
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SITE_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    USER_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ACTION_FIELD_NUMBER: _ClassVar[int]
    HASHED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_DATA_FIELD_NUMBER: _ClassVar[int]
    FRAUD_PREVENTION_FIELD_NUMBER: _ClassVar[int]
    token: str
    site_key: str
    user_agent: str
    user_ip_address: str
    expected_action: str
    hashed_account_id: bytes
    transaction_data: TransactionData
    fraud_prevention: Event.FraudPrevention
    def __init__(self, token: _Optional[str] = ..., site_key: _Optional[str] = ..., user_agent: _Optional[str] = ..., user_ip_address: _Optional[str] = ..., expected_action: _Optional[str] = ..., hashed_account_id: _Optional[bytes] = ..., transaction_data: _Optional[_Union[TransactionData, _Mapping]] = ..., fraud_prevention: _Optional[_Union[Event.FraudPrevention, str]] = ...) -> None: ...

class TransactionData(_message.Message):
    __slots__ = ("transaction_id", "payment_method", "card_bin", "card_last_four", "currency_code", "value", "shipping_value", "shipping_address", "billing_address", "user", "merchants", "items", "gateway_info")
    class Address(_message.Message):
        __slots__ = ("recipient", "address", "locality", "administrative_area", "region_code", "postal_code")
        RECIPIENT_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        LOCALITY_FIELD_NUMBER: _ClassVar[int]
        ADMINISTRATIVE_AREA_FIELD_NUMBER: _ClassVar[int]
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
        recipient: str
        address: _containers.RepeatedScalarFieldContainer[str]
        locality: str
        administrative_area: str
        region_code: str
        postal_code: str
        def __init__(self, recipient: _Optional[str] = ..., address: _Optional[_Iterable[str]] = ..., locality: _Optional[str] = ..., administrative_area: _Optional[str] = ..., region_code: _Optional[str] = ..., postal_code: _Optional[str] = ...) -> None: ...
    class User(_message.Message):
        __slots__ = ("account_id", "creation_ms", "email", "email_verified", "phone_number", "phone_verified")
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        CREATION_MS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
        account_id: str
        creation_ms: int
        email: str
        email_verified: bool
        phone_number: str
        phone_verified: bool
        def __init__(self, account_id: _Optional[str] = ..., creation_ms: _Optional[int] = ..., email: _Optional[str] = ..., email_verified: bool = ..., phone_number: _Optional[str] = ..., phone_verified: bool = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("name", "value", "quantity", "merchant_account_id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        MERCHANT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: float
        quantity: int
        merchant_account_id: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[float] = ..., quantity: _Optional[int] = ..., merchant_account_id: _Optional[str] = ...) -> None: ...
    class GatewayInfo(_message.Message):
        __slots__ = ("name", "gateway_response_code", "avs_response_code", "cvv_response_code")
        NAME_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
        AVS_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
        CVV_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
        name: str
        gateway_response_code: str
        avs_response_code: str
        cvv_response_code: str
        def __init__(self, name: _Optional[str] = ..., gateway_response_code: _Optional[str] = ..., avs_response_code: _Optional[str] = ..., cvv_response_code: _Optional[str] = ...) -> None: ...
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    CARD_BIN_FIELD_NUMBER: _ClassVar[int]
    CARD_LAST_FOUR_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    MERCHANTS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_INFO_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    payment_method: str
    card_bin: str
    card_last_four: str
    currency_code: str
    value: float
    shipping_value: float
    shipping_address: TransactionData.Address
    billing_address: TransactionData.Address
    user: TransactionData.User
    merchants: _containers.RepeatedCompositeFieldContainer[TransactionData.User]
    items: _containers.RepeatedCompositeFieldContainer[TransactionData.Item]
    gateway_info: TransactionData.GatewayInfo
    def __init__(self, transaction_id: _Optional[str] = ..., payment_method: _Optional[str] = ..., card_bin: _Optional[str] = ..., card_last_four: _Optional[str] = ..., currency_code: _Optional[str] = ..., value: _Optional[float] = ..., shipping_value: _Optional[float] = ..., shipping_address: _Optional[_Union[TransactionData.Address, _Mapping]] = ..., billing_address: _Optional[_Union[TransactionData.Address, _Mapping]] = ..., user: _Optional[_Union[TransactionData.User, _Mapping]] = ..., merchants: _Optional[_Iterable[_Union[TransactionData.User, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[TransactionData.Item, _Mapping]]] = ..., gateway_info: _Optional[_Union[TransactionData.GatewayInfo, _Mapping]] = ...) -> None: ...

class TokenProperties(_message.Message):
    __slots__ = ("valid", "invalid_reason", "create_time", "hostname", "action")
    class InvalidReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID_REASON_UNSPECIFIED: _ClassVar[TokenProperties.InvalidReason]
        UNKNOWN_INVALID_REASON: _ClassVar[TokenProperties.InvalidReason]
        MALFORMED: _ClassVar[TokenProperties.InvalidReason]
        EXPIRED: _ClassVar[TokenProperties.InvalidReason]
        DUPE: _ClassVar[TokenProperties.InvalidReason]
        SITE_MISMATCH: _ClassVar[TokenProperties.InvalidReason]
        MISSING: _ClassVar[TokenProperties.InvalidReason]
        BROWSER_ERROR: _ClassVar[TokenProperties.InvalidReason]
    INVALID_REASON_UNSPECIFIED: TokenProperties.InvalidReason
    UNKNOWN_INVALID_REASON: TokenProperties.InvalidReason
    MALFORMED: TokenProperties.InvalidReason
    EXPIRED: TokenProperties.InvalidReason
    DUPE: TokenProperties.InvalidReason
    SITE_MISMATCH: TokenProperties.InvalidReason
    MISSING: TokenProperties.InvalidReason
    BROWSER_ERROR: TokenProperties.InvalidReason
    VALID_FIELD_NUMBER: _ClassVar[int]
    INVALID_REASON_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    invalid_reason: TokenProperties.InvalidReason
    create_time: _timestamp_pb2.Timestamp
    hostname: str
    action: str
    def __init__(self, valid: bool = ..., invalid_reason: _Optional[_Union[TokenProperties.InvalidReason, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hostname: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class FraudPreventionAssessment(_message.Message):
    __slots__ = ("transaction_risk", "stolen_instrument_verdict", "card_testing_verdict", "behavioral_trust_verdict")
    class StolenInstrumentVerdict(_message.Message):
        __slots__ = ("risk",)
        RISK_FIELD_NUMBER: _ClassVar[int]
        risk: float
        def __init__(self, risk: _Optional[float] = ...) -> None: ...
    class CardTestingVerdict(_message.Message):
        __slots__ = ("risk",)
        RISK_FIELD_NUMBER: _ClassVar[int]
        risk: float
        def __init__(self, risk: _Optional[float] = ...) -> None: ...
    class BehavioralTrustVerdict(_message.Message):
        __slots__ = ("trust",)
        TRUST_FIELD_NUMBER: _ClassVar[int]
        trust: float
        def __init__(self, trust: _Optional[float] = ...) -> None: ...
    TRANSACTION_RISK_FIELD_NUMBER: _ClassVar[int]
    STOLEN_INSTRUMENT_VERDICT_FIELD_NUMBER: _ClassVar[int]
    CARD_TESTING_VERDICT_FIELD_NUMBER: _ClassVar[int]
    BEHAVIORAL_TRUST_VERDICT_FIELD_NUMBER: _ClassVar[int]
    transaction_risk: float
    stolen_instrument_verdict: FraudPreventionAssessment.StolenInstrumentVerdict
    card_testing_verdict: FraudPreventionAssessment.CardTestingVerdict
    behavioral_trust_verdict: FraudPreventionAssessment.BehavioralTrustVerdict
    def __init__(self, transaction_risk: _Optional[float] = ..., stolen_instrument_verdict: _Optional[_Union[FraudPreventionAssessment.StolenInstrumentVerdict, _Mapping]] = ..., card_testing_verdict: _Optional[_Union[FraudPreventionAssessment.CardTestingVerdict, _Mapping]] = ..., behavioral_trust_verdict: _Optional[_Union[FraudPreventionAssessment.BehavioralTrustVerdict, _Mapping]] = ...) -> None: ...

class AccountDefenderAssessment(_message.Message):
    __slots__ = ("labels",)
    class AccountDefenderLabel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCOUNT_DEFENDER_LABEL_UNSPECIFIED: _ClassVar[AccountDefenderAssessment.AccountDefenderLabel]
        PROFILE_MATCH: _ClassVar[AccountDefenderAssessment.AccountDefenderLabel]
        SUSPICIOUS_LOGIN_ACTIVITY: _ClassVar[AccountDefenderAssessment.AccountDefenderLabel]
        SUSPICIOUS_ACCOUNT_CREATION: _ClassVar[AccountDefenderAssessment.AccountDefenderLabel]
        RELATED_ACCOUNTS_NUMBER_HIGH: _ClassVar[AccountDefenderAssessment.AccountDefenderLabel]
    ACCOUNT_DEFENDER_LABEL_UNSPECIFIED: AccountDefenderAssessment.AccountDefenderLabel
    PROFILE_MATCH: AccountDefenderAssessment.AccountDefenderLabel
    SUSPICIOUS_LOGIN_ACTIVITY: AccountDefenderAssessment.AccountDefenderLabel
    SUSPICIOUS_ACCOUNT_CREATION: AccountDefenderAssessment.AccountDefenderLabel
    RELATED_ACCOUNTS_NUMBER_HIGH: AccountDefenderAssessment.AccountDefenderLabel
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[AccountDefenderAssessment.AccountDefenderLabel]
    def __init__(self, labels: _Optional[_Iterable[_Union[AccountDefenderAssessment.AccountDefenderLabel, str]]] = ...) -> None: ...
