from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
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
    __slots__ = ("name", "annotation", "reasons", "account_id", "hashed_account_id", "transaction_event")
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
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HASHED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    annotation: AnnotateAssessmentRequest.Annotation
    reasons: _containers.RepeatedScalarFieldContainer[AnnotateAssessmentRequest.Reason]
    account_id: str
    hashed_account_id: bytes
    transaction_event: TransactionEvent
    def __init__(self, name: _Optional[str] = ..., annotation: _Optional[_Union[AnnotateAssessmentRequest.Annotation, str]] = ..., reasons: _Optional[_Iterable[_Union[AnnotateAssessmentRequest.Reason, str]]] = ..., account_id: _Optional[str] = ..., hashed_account_id: _Optional[bytes] = ..., transaction_event: _Optional[_Union[TransactionEvent, _Mapping]] = ...) -> None: ...

class AnnotateAssessmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointVerificationInfo(_message.Message):
    __slots__ = ("email_address", "phone_number", "request_token", "last_verification_time")
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LAST_VERIFICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    phone_number: str
    request_token: str
    last_verification_time: _timestamp_pb2.Timestamp
    def __init__(self, email_address: _Optional[str] = ..., phone_number: _Optional[str] = ..., request_token: _Optional[str] = ..., last_verification_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountVerificationInfo(_message.Message):
    __slots__ = ("endpoints", "language_code", "latest_verification_result", "username")
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_UNSPECIFIED: _ClassVar[AccountVerificationInfo.Result]
        SUCCESS_USER_VERIFIED: _ClassVar[AccountVerificationInfo.Result]
        ERROR_USER_NOT_VERIFIED: _ClassVar[AccountVerificationInfo.Result]
        ERROR_SITE_ONBOARDING_INCOMPLETE: _ClassVar[AccountVerificationInfo.Result]
        ERROR_RECIPIENT_NOT_ALLOWED: _ClassVar[AccountVerificationInfo.Result]
        ERROR_RECIPIENT_ABUSE_LIMIT_EXHAUSTED: _ClassVar[AccountVerificationInfo.Result]
        ERROR_CRITICAL_INTERNAL: _ClassVar[AccountVerificationInfo.Result]
        ERROR_CUSTOMER_QUOTA_EXHAUSTED: _ClassVar[AccountVerificationInfo.Result]
        ERROR_VERIFICATION_BYPASSED: _ClassVar[AccountVerificationInfo.Result]
        ERROR_VERDICT_MISMATCH: _ClassVar[AccountVerificationInfo.Result]
    RESULT_UNSPECIFIED: AccountVerificationInfo.Result
    SUCCESS_USER_VERIFIED: AccountVerificationInfo.Result
    ERROR_USER_NOT_VERIFIED: AccountVerificationInfo.Result
    ERROR_SITE_ONBOARDING_INCOMPLETE: AccountVerificationInfo.Result
    ERROR_RECIPIENT_NOT_ALLOWED: AccountVerificationInfo.Result
    ERROR_RECIPIENT_ABUSE_LIMIT_EXHAUSTED: AccountVerificationInfo.Result
    ERROR_CRITICAL_INTERNAL: AccountVerificationInfo.Result
    ERROR_CUSTOMER_QUOTA_EXHAUSTED: AccountVerificationInfo.Result
    ERROR_VERIFICATION_BYPASSED: AccountVerificationInfo.Result
    ERROR_VERDICT_MISMATCH: AccountVerificationInfo.Result
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERIFICATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[EndpointVerificationInfo]
    language_code: str
    latest_verification_result: AccountVerificationInfo.Result
    username: str
    def __init__(self, endpoints: _Optional[_Iterable[_Union[EndpointVerificationInfo, _Mapping]]] = ..., language_code: _Optional[str] = ..., latest_verification_result: _Optional[_Union[AccountVerificationInfo.Result, str]] = ..., username: _Optional[str] = ...) -> None: ...

class PrivatePasswordLeakVerification(_message.Message):
    __slots__ = ("lookup_hash_prefix", "encrypted_user_credentials_hash", "encrypted_leak_match_prefixes", "reencrypted_user_credentials_hash")
    LOOKUP_HASH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_USER_CREDENTIALS_HASH_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_LEAK_MATCH_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    REENCRYPTED_USER_CREDENTIALS_HASH_FIELD_NUMBER: _ClassVar[int]
    lookup_hash_prefix: bytes
    encrypted_user_credentials_hash: bytes
    encrypted_leak_match_prefixes: _containers.RepeatedScalarFieldContainer[bytes]
    reencrypted_user_credentials_hash: bytes
    def __init__(self, lookup_hash_prefix: _Optional[bytes] = ..., encrypted_user_credentials_hash: _Optional[bytes] = ..., encrypted_leak_match_prefixes: _Optional[_Iterable[bytes]] = ..., reencrypted_user_credentials_hash: _Optional[bytes] = ...) -> None: ...

class Assessment(_message.Message):
    __slots__ = ("name", "event", "risk_analysis", "token_properties", "account_verification", "account_defender_assessment", "private_password_leak_verification", "firewall_policy_assessment", "fraud_prevention_assessment", "fraud_signals", "phone_fraud_assessment", "assessment_environment")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    RISK_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DEFENDER_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_PASSWORD_LEAK_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_POLICY_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    FRAUD_PREVENTION_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    FRAUD_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FRAUD_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    ASSESSMENT_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    event: Event
    risk_analysis: RiskAnalysis
    token_properties: TokenProperties
    account_verification: AccountVerificationInfo
    account_defender_assessment: AccountDefenderAssessment
    private_password_leak_verification: PrivatePasswordLeakVerification
    firewall_policy_assessment: FirewallPolicyAssessment
    fraud_prevention_assessment: FraudPreventionAssessment
    fraud_signals: FraudSignals
    phone_fraud_assessment: PhoneFraudAssessment
    assessment_environment: AssessmentEnvironment
    def __init__(self, name: _Optional[str] = ..., event: _Optional[_Union[Event, _Mapping]] = ..., risk_analysis: _Optional[_Union[RiskAnalysis, _Mapping]] = ..., token_properties: _Optional[_Union[TokenProperties, _Mapping]] = ..., account_verification: _Optional[_Union[AccountVerificationInfo, _Mapping]] = ..., account_defender_assessment: _Optional[_Union[AccountDefenderAssessment, _Mapping]] = ..., private_password_leak_verification: _Optional[_Union[PrivatePasswordLeakVerification, _Mapping]] = ..., firewall_policy_assessment: _Optional[_Union[FirewallPolicyAssessment, _Mapping]] = ..., fraud_prevention_assessment: _Optional[_Union[FraudPreventionAssessment, _Mapping]] = ..., fraud_signals: _Optional[_Union[FraudSignals, _Mapping]] = ..., phone_fraud_assessment: _Optional[_Union[PhoneFraudAssessment, _Mapping]] = ..., assessment_environment: _Optional[_Union[AssessmentEnvironment, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("token", "site_key", "user_agent", "user_ip_address", "expected_action", "hashed_account_id", "express", "requested_uri", "waf_token_assessment", "ja3", "headers", "firewall_policy_evaluation", "transaction_data", "user_info", "fraud_prevention")
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
    EXPRESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_URI_FIELD_NUMBER: _ClassVar[int]
    WAF_TOKEN_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    JA3_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_POLICY_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    FRAUD_PREVENTION_FIELD_NUMBER: _ClassVar[int]
    token: str
    site_key: str
    user_agent: str
    user_ip_address: str
    expected_action: str
    hashed_account_id: bytes
    express: bool
    requested_uri: str
    waf_token_assessment: bool
    ja3: str
    headers: _containers.RepeatedScalarFieldContainer[str]
    firewall_policy_evaluation: bool
    transaction_data: TransactionData
    user_info: UserInfo
    fraud_prevention: Event.FraudPrevention
    def __init__(self, token: _Optional[str] = ..., site_key: _Optional[str] = ..., user_agent: _Optional[str] = ..., user_ip_address: _Optional[str] = ..., expected_action: _Optional[str] = ..., hashed_account_id: _Optional[bytes] = ..., express: bool = ..., requested_uri: _Optional[str] = ..., waf_token_assessment: bool = ..., ja3: _Optional[str] = ..., headers: _Optional[_Iterable[str]] = ..., firewall_policy_evaluation: bool = ..., transaction_data: _Optional[_Union[TransactionData, _Mapping]] = ..., user_info: _Optional[_Union[UserInfo, _Mapping]] = ..., fraud_prevention: _Optional[_Union[Event.FraudPrevention, str]] = ...) -> None: ...

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

class UserInfo(_message.Message):
    __slots__ = ("create_account_time", "account_id", "user_ids")
    CREATE_ACCOUNT_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    create_account_time: _timestamp_pb2.Timestamp
    account_id: str
    user_ids: _containers.RepeatedCompositeFieldContainer[UserId]
    def __init__(self, create_account_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[_Union[UserId, _Mapping]]] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ("email", "phone_number", "username")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    phone_number: str
    username: str
    def __init__(self, email: _Optional[str] = ..., phone_number: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class RiskAnalysis(_message.Message):
    __slots__ = ("score", "reasons", "extended_verdict_reasons", "challenge")
    class ClassificationReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLASSIFICATION_REASON_UNSPECIFIED: _ClassVar[RiskAnalysis.ClassificationReason]
        AUTOMATION: _ClassVar[RiskAnalysis.ClassificationReason]
        UNEXPECTED_ENVIRONMENT: _ClassVar[RiskAnalysis.ClassificationReason]
        TOO_MUCH_TRAFFIC: _ClassVar[RiskAnalysis.ClassificationReason]
        UNEXPECTED_USAGE_PATTERNS: _ClassVar[RiskAnalysis.ClassificationReason]
        LOW_CONFIDENCE_SCORE: _ClassVar[RiskAnalysis.ClassificationReason]
        SUSPECTED_CARDING: _ClassVar[RiskAnalysis.ClassificationReason]
        SUSPECTED_CHARGEBACK: _ClassVar[RiskAnalysis.ClassificationReason]
    CLASSIFICATION_REASON_UNSPECIFIED: RiskAnalysis.ClassificationReason
    AUTOMATION: RiskAnalysis.ClassificationReason
    UNEXPECTED_ENVIRONMENT: RiskAnalysis.ClassificationReason
    TOO_MUCH_TRAFFIC: RiskAnalysis.ClassificationReason
    UNEXPECTED_USAGE_PATTERNS: RiskAnalysis.ClassificationReason
    LOW_CONFIDENCE_SCORE: RiskAnalysis.ClassificationReason
    SUSPECTED_CARDING: RiskAnalysis.ClassificationReason
    SUSPECTED_CHARGEBACK: RiskAnalysis.ClassificationReason
    class Challenge(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHALLENGE_UNSPECIFIED: _ClassVar[RiskAnalysis.Challenge]
        NOCAPTCHA: _ClassVar[RiskAnalysis.Challenge]
        PASSED: _ClassVar[RiskAnalysis.Challenge]
        FAILED: _ClassVar[RiskAnalysis.Challenge]
    CHALLENGE_UNSPECIFIED: RiskAnalysis.Challenge
    NOCAPTCHA: RiskAnalysis.Challenge
    PASSED: RiskAnalysis.Challenge
    FAILED: RiskAnalysis.Challenge
    SCORE_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_VERDICT_REASONS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    score: float
    reasons: _containers.RepeatedScalarFieldContainer[RiskAnalysis.ClassificationReason]
    extended_verdict_reasons: _containers.RepeatedScalarFieldContainer[str]
    challenge: RiskAnalysis.Challenge
    def __init__(self, score: _Optional[float] = ..., reasons: _Optional[_Iterable[_Union[RiskAnalysis.ClassificationReason, str]]] = ..., extended_verdict_reasons: _Optional[_Iterable[str]] = ..., challenge: _Optional[_Union[RiskAnalysis.Challenge, str]] = ...) -> None: ...

class TokenProperties(_message.Message):
    __slots__ = ("valid", "invalid_reason", "create_time", "hostname", "android_package_name", "ios_bundle_id", "action")
    class InvalidReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID_REASON_UNSPECIFIED: _ClassVar[TokenProperties.InvalidReason]
        UNKNOWN_INVALID_REASON: _ClassVar[TokenProperties.InvalidReason]
        MALFORMED: _ClassVar[TokenProperties.InvalidReason]
        EXPIRED: _ClassVar[TokenProperties.InvalidReason]
        DUPE: _ClassVar[TokenProperties.InvalidReason]
        MISSING: _ClassVar[TokenProperties.InvalidReason]
        BROWSER_ERROR: _ClassVar[TokenProperties.InvalidReason]
    INVALID_REASON_UNSPECIFIED: TokenProperties.InvalidReason
    UNKNOWN_INVALID_REASON: TokenProperties.InvalidReason
    MALFORMED: TokenProperties.InvalidReason
    EXPIRED: TokenProperties.InvalidReason
    DUPE: TokenProperties.InvalidReason
    MISSING: TokenProperties.InvalidReason
    BROWSER_ERROR: TokenProperties.InvalidReason
    VALID_FIELD_NUMBER: _ClassVar[int]
    INVALID_REASON_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ANDROID_PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    IOS_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    invalid_reason: TokenProperties.InvalidReason
    create_time: _timestamp_pb2.Timestamp
    hostname: str
    android_package_name: str
    ios_bundle_id: str
    action: str
    def __init__(self, valid: bool = ..., invalid_reason: _Optional[_Union[TokenProperties.InvalidReason, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hostname: _Optional[str] = ..., android_package_name: _Optional[str] = ..., ios_bundle_id: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

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

class FraudSignals(_message.Message):
    __slots__ = ("user_signals", "card_signals")
    class UserSignals(_message.Message):
        __slots__ = ("active_days_lower_bound", "synthetic_risk")
        ACTIVE_DAYS_LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
        SYNTHETIC_RISK_FIELD_NUMBER: _ClassVar[int]
        active_days_lower_bound: int
        synthetic_risk: float
        def __init__(self, active_days_lower_bound: _Optional[int] = ..., synthetic_risk: _Optional[float] = ...) -> None: ...
    class CardSignals(_message.Message):
        __slots__ = ("card_labels",)
        class CardLabel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CARD_LABEL_UNSPECIFIED: _ClassVar[FraudSignals.CardSignals.CardLabel]
            PREPAID: _ClassVar[FraudSignals.CardSignals.CardLabel]
            VIRTUAL: _ClassVar[FraudSignals.CardSignals.CardLabel]
            UNEXPECTED_LOCATION: _ClassVar[FraudSignals.CardSignals.CardLabel]
        CARD_LABEL_UNSPECIFIED: FraudSignals.CardSignals.CardLabel
        PREPAID: FraudSignals.CardSignals.CardLabel
        VIRTUAL: FraudSignals.CardSignals.CardLabel
        UNEXPECTED_LOCATION: FraudSignals.CardSignals.CardLabel
        CARD_LABELS_FIELD_NUMBER: _ClassVar[int]
        card_labels: _containers.RepeatedScalarFieldContainer[FraudSignals.CardSignals.CardLabel]
        def __init__(self, card_labels: _Optional[_Iterable[_Union[FraudSignals.CardSignals.CardLabel, str]]] = ...) -> None: ...
    USER_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    CARD_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    user_signals: FraudSignals.UserSignals
    card_signals: FraudSignals.CardSignals
    def __init__(self, user_signals: _Optional[_Union[FraudSignals.UserSignals, _Mapping]] = ..., card_signals: _Optional[_Union[FraudSignals.CardSignals, _Mapping]] = ...) -> None: ...

class SmsTollFraudVerdict(_message.Message):
    __slots__ = ("risk", "reasons")
    class SmsTollFraudReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SMS_TOLL_FRAUD_REASON_UNSPECIFIED: _ClassVar[SmsTollFraudVerdict.SmsTollFraudReason]
        INVALID_PHONE_NUMBER: _ClassVar[SmsTollFraudVerdict.SmsTollFraudReason]
    SMS_TOLL_FRAUD_REASON_UNSPECIFIED: SmsTollFraudVerdict.SmsTollFraudReason
    INVALID_PHONE_NUMBER: SmsTollFraudVerdict.SmsTollFraudReason
    RISK_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    risk: float
    reasons: _containers.RepeatedScalarFieldContainer[SmsTollFraudVerdict.SmsTollFraudReason]
    def __init__(self, risk: _Optional[float] = ..., reasons: _Optional[_Iterable[_Union[SmsTollFraudVerdict.SmsTollFraudReason, str]]] = ...) -> None: ...

class PhoneFraudAssessment(_message.Message):
    __slots__ = ("sms_toll_fraud_verdict",)
    SMS_TOLL_FRAUD_VERDICT_FIELD_NUMBER: _ClassVar[int]
    sms_toll_fraud_verdict: SmsTollFraudVerdict
    def __init__(self, sms_toll_fraud_verdict: _Optional[_Union[SmsTollFraudVerdict, _Mapping]] = ...) -> None: ...

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

class CreateKeyRequest(_message.Message):
    __slots__ = ("parent", "key")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    key: Key
    def __init__(self, parent: _Optional[str] = ..., key: _Optional[_Union[Key, _Mapping]] = ...) -> None: ...

class ListKeysRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListKeysResponse(_message.Message):
    __slots__ = ("keys", "next_page_token")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[Key]
    next_page_token: str
    def __init__(self, keys: _Optional[_Iterable[_Union[Key, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class RetrieveLegacySecretKeyRequest(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class GetKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateKeyRequest(_message.Message):
    __slots__ = ("key", "update_mask")
    KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    key: Key
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, key: _Optional[_Union[Key, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteKeyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFirewallPolicyRequest(_message.Message):
    __slots__ = ("parent", "firewall_policy")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    firewall_policy: FirewallPolicy
    def __init__(self, parent: _Optional[str] = ..., firewall_policy: _Optional[_Union[FirewallPolicy, _Mapping]] = ...) -> None: ...

class ListFirewallPoliciesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListFirewallPoliciesResponse(_message.Message):
    __slots__ = ("firewall_policies", "next_page_token")
    FIREWALL_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    firewall_policies: _containers.RepeatedCompositeFieldContainer[FirewallPolicy]
    next_page_token: str
    def __init__(self, firewall_policies: _Optional[_Iterable[_Union[FirewallPolicy, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetFirewallPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateFirewallPolicyRequest(_message.Message):
    __slots__ = ("firewall_policy", "update_mask")
    FIREWALL_POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    firewall_policy: FirewallPolicy
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, firewall_policy: _Optional[_Union[FirewallPolicy, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFirewallPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReorderFirewallPoliciesRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class ReorderFirewallPoliciesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrateKeyRequest(_message.Message):
    __slots__ = ("name", "skip_billing_check")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_BILLING_CHECK_FIELD_NUMBER: _ClassVar[int]
    name: str
    skip_billing_check: bool
    def __init__(self, name: _Optional[str] = ..., skip_billing_check: bool = ...) -> None: ...

class GetMetricsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ("name", "start_time", "score_metrics", "challenge_metrics")
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    SCORE_METRICS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_METRICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    score_metrics: _containers.RepeatedCompositeFieldContainer[ScoreMetrics]
    challenge_metrics: _containers.RepeatedCompositeFieldContainer[ChallengeMetrics]
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., score_metrics: _Optional[_Iterable[_Union[ScoreMetrics, _Mapping]]] = ..., challenge_metrics: _Optional[_Iterable[_Union[ChallengeMetrics, _Mapping]]] = ...) -> None: ...

class RetrieveLegacySecretKeyResponse(_message.Message):
    __slots__ = ("legacy_secret_key",)
    LEGACY_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    legacy_secret_key: str
    def __init__(self, legacy_secret_key: _Optional[str] = ...) -> None: ...

class Key(_message.Message):
    __slots__ = ("name", "display_name", "web_settings", "android_settings", "ios_settings", "express_settings", "labels", "create_time", "testing_options", "waf_settings")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IOS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EXPRESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TESTING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WAF_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    web_settings: WebKeySettings
    android_settings: AndroidKeySettings
    ios_settings: IOSKeySettings
    express_settings: ExpressKeySettings
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    testing_options: TestingOptions
    waf_settings: WafSettings
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., web_settings: _Optional[_Union[WebKeySettings, _Mapping]] = ..., android_settings: _Optional[_Union[AndroidKeySettings, _Mapping]] = ..., ios_settings: _Optional[_Union[IOSKeySettings, _Mapping]] = ..., express_settings: _Optional[_Union[ExpressKeySettings, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., testing_options: _Optional[_Union[TestingOptions, _Mapping]] = ..., waf_settings: _Optional[_Union[WafSettings, _Mapping]] = ...) -> None: ...

class TestingOptions(_message.Message):
    __slots__ = ("testing_score", "testing_challenge")
    class TestingChallenge(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TESTING_CHALLENGE_UNSPECIFIED: _ClassVar[TestingOptions.TestingChallenge]
        NOCAPTCHA: _ClassVar[TestingOptions.TestingChallenge]
        UNSOLVABLE_CHALLENGE: _ClassVar[TestingOptions.TestingChallenge]
    TESTING_CHALLENGE_UNSPECIFIED: TestingOptions.TestingChallenge
    NOCAPTCHA: TestingOptions.TestingChallenge
    UNSOLVABLE_CHALLENGE: TestingOptions.TestingChallenge
    TESTING_SCORE_FIELD_NUMBER: _ClassVar[int]
    TESTING_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    testing_score: float
    testing_challenge: TestingOptions.TestingChallenge
    def __init__(self, testing_score: _Optional[float] = ..., testing_challenge: _Optional[_Union[TestingOptions.TestingChallenge, str]] = ...) -> None: ...

class WebKeySettings(_message.Message):
    __slots__ = ("allow_all_domains", "allowed_domains", "allow_amp_traffic", "integration_type", "challenge_security_preference")
    class IntegrationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTEGRATION_TYPE_UNSPECIFIED: _ClassVar[WebKeySettings.IntegrationType]
        SCORE: _ClassVar[WebKeySettings.IntegrationType]
        CHECKBOX: _ClassVar[WebKeySettings.IntegrationType]
        INVISIBLE: _ClassVar[WebKeySettings.IntegrationType]
    INTEGRATION_TYPE_UNSPECIFIED: WebKeySettings.IntegrationType
    SCORE: WebKeySettings.IntegrationType
    CHECKBOX: WebKeySettings.IntegrationType
    INVISIBLE: WebKeySettings.IntegrationType
    class ChallengeSecurityPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED: _ClassVar[WebKeySettings.ChallengeSecurityPreference]
        USABILITY: _ClassVar[WebKeySettings.ChallengeSecurityPreference]
        BALANCE: _ClassVar[WebKeySettings.ChallengeSecurityPreference]
        SECURITY: _ClassVar[WebKeySettings.ChallengeSecurityPreference]
    CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED: WebKeySettings.ChallengeSecurityPreference
    USABILITY: WebKeySettings.ChallengeSecurityPreference
    BALANCE: WebKeySettings.ChallengeSecurityPreference
    SECURITY: WebKeySettings.ChallengeSecurityPreference
    ALLOW_ALL_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AMP_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_SECURITY_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    allow_all_domains: bool
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    allow_amp_traffic: bool
    integration_type: WebKeySettings.IntegrationType
    challenge_security_preference: WebKeySettings.ChallengeSecurityPreference
    def __init__(self, allow_all_domains: bool = ..., allowed_domains: _Optional[_Iterable[str]] = ..., allow_amp_traffic: bool = ..., integration_type: _Optional[_Union[WebKeySettings.IntegrationType, str]] = ..., challenge_security_preference: _Optional[_Union[WebKeySettings.ChallengeSecurityPreference, str]] = ...) -> None: ...

class AndroidKeySettings(_message.Message):
    __slots__ = ("allow_all_package_names", "allowed_package_names", "support_non_google_app_store_distribution")
    ALLOW_ALL_PACKAGE_NAMES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_PACKAGE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_NON_GOOGLE_APP_STORE_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    allow_all_package_names: bool
    allowed_package_names: _containers.RepeatedScalarFieldContainer[str]
    support_non_google_app_store_distribution: bool
    def __init__(self, allow_all_package_names: bool = ..., allowed_package_names: _Optional[_Iterable[str]] = ..., support_non_google_app_store_distribution: bool = ...) -> None: ...

class IOSKeySettings(_message.Message):
    __slots__ = ("allow_all_bundle_ids", "allowed_bundle_ids", "apple_developer_id")
    ALLOW_ALL_BUNDLE_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_BUNDLE_IDS_FIELD_NUMBER: _ClassVar[int]
    APPLE_DEVELOPER_ID_FIELD_NUMBER: _ClassVar[int]
    allow_all_bundle_ids: bool
    allowed_bundle_ids: _containers.RepeatedScalarFieldContainer[str]
    apple_developer_id: AppleDeveloperId
    def __init__(self, allow_all_bundle_ids: bool = ..., allowed_bundle_ids: _Optional[_Iterable[str]] = ..., apple_developer_id: _Optional[_Union[AppleDeveloperId, _Mapping]] = ...) -> None: ...

class ExpressKeySettings(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppleDeveloperId(_message.Message):
    __slots__ = ("private_key", "key_id", "team_id")
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    private_key: str
    key_id: str
    team_id: str
    def __init__(self, private_key: _Optional[str] = ..., key_id: _Optional[str] = ..., team_id: _Optional[str] = ...) -> None: ...

class ScoreDistribution(_message.Message):
    __slots__ = ("score_buckets",)
    class ScoreBucketsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SCORE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    score_buckets: _containers.ScalarMap[int, int]
    def __init__(self, score_buckets: _Optional[_Mapping[int, int]] = ...) -> None: ...

class ScoreMetrics(_message.Message):
    __slots__ = ("overall_metrics", "action_metrics")
    class ActionMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ScoreDistribution
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ScoreDistribution, _Mapping]] = ...) -> None: ...
    OVERALL_METRICS_FIELD_NUMBER: _ClassVar[int]
    ACTION_METRICS_FIELD_NUMBER: _ClassVar[int]
    overall_metrics: ScoreDistribution
    action_metrics: _containers.MessageMap[str, ScoreDistribution]
    def __init__(self, overall_metrics: _Optional[_Union[ScoreDistribution, _Mapping]] = ..., action_metrics: _Optional[_Mapping[str, ScoreDistribution]] = ...) -> None: ...

class ChallengeMetrics(_message.Message):
    __slots__ = ("pageload_count", "nocaptcha_count", "failed_count", "passed_count")
    PAGELOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    NOCAPTCHA_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASSED_COUNT_FIELD_NUMBER: _ClassVar[int]
    pageload_count: int
    nocaptcha_count: int
    failed_count: int
    passed_count: int
    def __init__(self, pageload_count: _Optional[int] = ..., nocaptcha_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., passed_count: _Optional[int] = ...) -> None: ...

class FirewallPolicyAssessment(_message.Message):
    __slots__ = ("error", "firewall_policy")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FIREWALL_POLICY_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status
    firewall_policy: FirewallPolicy
    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., firewall_policy: _Optional[_Union[FirewallPolicy, _Mapping]] = ...) -> None: ...

class FirewallAction(_message.Message):
    __slots__ = ("allow", "block", "include_recaptcha_script", "redirect", "substitute", "set_header")
    class AllowAction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class BlockAction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class IncludeRecaptchaScriptAction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RedirectAction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SubstituteAction(_message.Message):
        __slots__ = ("path",)
        PATH_FIELD_NUMBER: _ClassVar[int]
        path: str
        def __init__(self, path: _Optional[str] = ...) -> None: ...
    class SetHeaderAction(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RECAPTCHA_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTE_FIELD_NUMBER: _ClassVar[int]
    SET_HEADER_FIELD_NUMBER: _ClassVar[int]
    allow: FirewallAction.AllowAction
    block: FirewallAction.BlockAction
    include_recaptcha_script: FirewallAction.IncludeRecaptchaScriptAction
    redirect: FirewallAction.RedirectAction
    substitute: FirewallAction.SubstituteAction
    set_header: FirewallAction.SetHeaderAction
    def __init__(self, allow: _Optional[_Union[FirewallAction.AllowAction, _Mapping]] = ..., block: _Optional[_Union[FirewallAction.BlockAction, _Mapping]] = ..., include_recaptcha_script: _Optional[_Union[FirewallAction.IncludeRecaptchaScriptAction, _Mapping]] = ..., redirect: _Optional[_Union[FirewallAction.RedirectAction, _Mapping]] = ..., substitute: _Optional[_Union[FirewallAction.SubstituteAction, _Mapping]] = ..., set_header: _Optional[_Union[FirewallAction.SetHeaderAction, _Mapping]] = ...) -> None: ...

class FirewallPolicy(_message.Message):
    __slots__ = ("name", "description", "path", "condition", "actions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    path: str
    condition: str
    actions: _containers.RepeatedCompositeFieldContainer[FirewallAction]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., path: _Optional[str] = ..., condition: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[FirewallAction, _Mapping]]] = ...) -> None: ...

class ListRelatedAccountGroupMembershipsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRelatedAccountGroupMembershipsResponse(_message.Message):
    __slots__ = ("related_account_group_memberships", "next_page_token")
    RELATED_ACCOUNT_GROUP_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    related_account_group_memberships: _containers.RepeatedCompositeFieldContainer[RelatedAccountGroupMembership]
    next_page_token: str
    def __init__(self, related_account_group_memberships: _Optional[_Iterable[_Union[RelatedAccountGroupMembership, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListRelatedAccountGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRelatedAccountGroupsResponse(_message.Message):
    __slots__ = ("related_account_groups", "next_page_token")
    RELATED_ACCOUNT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    related_account_groups: _containers.RepeatedCompositeFieldContainer[RelatedAccountGroup]
    next_page_token: str
    def __init__(self, related_account_groups: _Optional[_Iterable[_Union[RelatedAccountGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchRelatedAccountGroupMembershipsRequest(_message.Message):
    __slots__ = ("project", "account_id", "hashed_account_id", "page_size", "page_token")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HASHED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project: str
    account_id: str
    hashed_account_id: bytes
    page_size: int
    page_token: str
    def __init__(self, project: _Optional[str] = ..., account_id: _Optional[str] = ..., hashed_account_id: _Optional[bytes] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SearchRelatedAccountGroupMembershipsResponse(_message.Message):
    __slots__ = ("related_account_group_memberships", "next_page_token")
    RELATED_ACCOUNT_GROUP_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    related_account_group_memberships: _containers.RepeatedCompositeFieldContainer[RelatedAccountGroupMembership]
    next_page_token: str
    def __init__(self, related_account_group_memberships: _Optional[_Iterable[_Union[RelatedAccountGroupMembership, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddIpOverrideRequest(_message.Message):
    __slots__ = ("name", "ip_override_data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_OVERRIDE_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    ip_override_data: IpOverrideData
    def __init__(self, name: _Optional[str] = ..., ip_override_data: _Optional[_Union[IpOverrideData, _Mapping]] = ...) -> None: ...

class AddIpOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveIpOverrideRequest(_message.Message):
    __slots__ = ("name", "ip_override_data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_OVERRIDE_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    ip_override_data: IpOverrideData
    def __init__(self, name: _Optional[str] = ..., ip_override_data: _Optional[_Union[IpOverrideData, _Mapping]] = ...) -> None: ...

class RemoveIpOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListIpOverridesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListIpOverridesResponse(_message.Message):
    __slots__ = ("ip_overrides", "next_page_token")
    IP_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ip_overrides: _containers.RepeatedCompositeFieldContainer[IpOverrideData]
    next_page_token: str
    def __init__(self, ip_overrides: _Optional[_Iterable[_Union[IpOverrideData, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class RelatedAccountGroupMembership(_message.Message):
    __slots__ = ("name", "account_id", "hashed_account_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HASHED_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_id: str
    hashed_account_id: bytes
    def __init__(self, name: _Optional[str] = ..., account_id: _Optional[str] = ..., hashed_account_id: _Optional[bytes] = ...) -> None: ...

class RelatedAccountGroup(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class WafSettings(_message.Message):
    __slots__ = ("waf_service", "waf_feature")
    class WafFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WAF_FEATURE_UNSPECIFIED: _ClassVar[WafSettings.WafFeature]
        CHALLENGE_PAGE: _ClassVar[WafSettings.WafFeature]
        SESSION_TOKEN: _ClassVar[WafSettings.WafFeature]
        ACTION_TOKEN: _ClassVar[WafSettings.WafFeature]
        EXPRESS: _ClassVar[WafSettings.WafFeature]
    WAF_FEATURE_UNSPECIFIED: WafSettings.WafFeature
    CHALLENGE_PAGE: WafSettings.WafFeature
    SESSION_TOKEN: WafSettings.WafFeature
    ACTION_TOKEN: WafSettings.WafFeature
    EXPRESS: WafSettings.WafFeature
    class WafService(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WAF_SERVICE_UNSPECIFIED: _ClassVar[WafSettings.WafService]
        CA: _ClassVar[WafSettings.WafService]
        FASTLY: _ClassVar[WafSettings.WafService]
        CLOUDFLARE: _ClassVar[WafSettings.WafService]
        AKAMAI: _ClassVar[WafSettings.WafService]
    WAF_SERVICE_UNSPECIFIED: WafSettings.WafService
    CA: WafSettings.WafService
    FASTLY: WafSettings.WafService
    CLOUDFLARE: WafSettings.WafService
    AKAMAI: WafSettings.WafService
    WAF_SERVICE_FIELD_NUMBER: _ClassVar[int]
    WAF_FEATURE_FIELD_NUMBER: _ClassVar[int]
    waf_service: WafSettings.WafService
    waf_feature: WafSettings.WafFeature
    def __init__(self, waf_service: _Optional[_Union[WafSettings.WafService, str]] = ..., waf_feature: _Optional[_Union[WafSettings.WafFeature, str]] = ...) -> None: ...

class AssessmentEnvironment(_message.Message):
    __slots__ = ("client", "version")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client: str
    version: str
    def __init__(self, client: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class IpOverrideData(_message.Message):
    __slots__ = ("ip", "override_type")
    class OverrideType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OVERRIDE_TYPE_UNSPECIFIED: _ClassVar[IpOverrideData.OverrideType]
        ALLOW: _ClassVar[IpOverrideData.OverrideType]
    OVERRIDE_TYPE_UNSPECIFIED: IpOverrideData.OverrideType
    ALLOW: IpOverrideData.OverrideType
    IP_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ip: str
    override_type: IpOverrideData.OverrideType
    def __init__(self, ip: _Optional[str] = ..., override_type: _Optional[_Union[IpOverrideData.OverrideType, str]] = ...) -> None: ...
