from google.ads.googleads.v16.enums import policy_topic_entry_type_pb2 as _policy_topic_entry_type_pb2
from google.ads.googleads.v16.enums import policy_topic_evidence_destination_mismatch_url_type_pb2 as _policy_topic_evidence_destination_mismatch_url_type_pb2
from google.ads.googleads.v16.enums import policy_topic_evidence_destination_not_working_device_pb2 as _policy_topic_evidence_destination_not_working_device_pb2
from google.ads.googleads.v16.enums import policy_topic_evidence_destination_not_working_dns_error_type_pb2 as _policy_topic_evidence_destination_not_working_dns_error_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyViolationKey(_message.Message):
    __slots__ = ("policy_name", "violating_text")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    VIOLATING_TEXT_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    violating_text: str
    def __init__(self, policy_name: _Optional[str] = ..., violating_text: _Optional[str] = ...) -> None: ...

class PolicyValidationParameter(_message.Message):
    __slots__ = ("ignorable_policy_topics", "exempt_policy_violation_keys")
    IGNORABLE_POLICY_TOPICS_FIELD_NUMBER: _ClassVar[int]
    EXEMPT_POLICY_VIOLATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    ignorable_policy_topics: _containers.RepeatedScalarFieldContainer[str]
    exempt_policy_violation_keys: _containers.RepeatedCompositeFieldContainer[PolicyViolationKey]
    def __init__(self, ignorable_policy_topics: _Optional[_Iterable[str]] = ..., exempt_policy_violation_keys: _Optional[_Iterable[_Union[PolicyViolationKey, _Mapping]]] = ...) -> None: ...

class PolicyTopicEntry(_message.Message):
    __slots__ = ("topic", "type", "evidences", "constraints")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    topic: str
    type: _policy_topic_entry_type_pb2.PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    evidences: _containers.RepeatedCompositeFieldContainer[PolicyTopicEvidence]
    constraints: _containers.RepeatedCompositeFieldContainer[PolicyTopicConstraint]
    def __init__(self, topic: _Optional[str] = ..., type: _Optional[_Union[_policy_topic_entry_type_pb2.PolicyTopicEntryTypeEnum.PolicyTopicEntryType, str]] = ..., evidences: _Optional[_Iterable[_Union[PolicyTopicEvidence, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[PolicyTopicConstraint, _Mapping]]] = ...) -> None: ...

class PolicyTopicEvidence(_message.Message):
    __slots__ = ("website_list", "text_list", "language_code", "destination_text_list", "destination_mismatch", "destination_not_working")
    class TextList(_message.Message):
        __slots__ = ("texts",)
        TEXTS_FIELD_NUMBER: _ClassVar[int]
        texts: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, texts: _Optional[_Iterable[str]] = ...) -> None: ...
    class WebsiteList(_message.Message):
        __slots__ = ("websites",)
        WEBSITES_FIELD_NUMBER: _ClassVar[int]
        websites: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, websites: _Optional[_Iterable[str]] = ...) -> None: ...
    class DestinationTextList(_message.Message):
        __slots__ = ("destination_texts",)
        DESTINATION_TEXTS_FIELD_NUMBER: _ClassVar[int]
        destination_texts: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, destination_texts: _Optional[_Iterable[str]] = ...) -> None: ...
    class DestinationMismatch(_message.Message):
        __slots__ = ("url_types",)
        URL_TYPES_FIELD_NUMBER: _ClassVar[int]
        url_types: _containers.RepeatedScalarFieldContainer[_policy_topic_evidence_destination_mismatch_url_type_pb2.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType]
        def __init__(self, url_types: _Optional[_Iterable[_Union[_policy_topic_evidence_destination_mismatch_url_type_pb2.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType, str]]] = ...) -> None: ...
    class DestinationNotWorking(_message.Message):
        __slots__ = ("expanded_url", "device", "last_checked_date_time", "dns_error_type", "http_error_code")
        EXPANDED_URL_FIELD_NUMBER: _ClassVar[int]
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        LAST_CHECKED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        DNS_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        HTTP_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        expanded_url: str
        device: _policy_topic_evidence_destination_not_working_device_pb2.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
        last_checked_date_time: str
        dns_error_type: _policy_topic_evidence_destination_not_working_dns_error_type_pb2.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
        http_error_code: int
        def __init__(self, expanded_url: _Optional[str] = ..., device: _Optional[_Union[_policy_topic_evidence_destination_not_working_device_pb2.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice, str]] = ..., last_checked_date_time: _Optional[str] = ..., dns_error_type: _Optional[_Union[_policy_topic_evidence_destination_not_working_dns_error_type_pb2.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType, str]] = ..., http_error_code: _Optional[int] = ...) -> None: ...
    WEBSITE_LIST_FIELD_NUMBER: _ClassVar[int]
    TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_MISMATCH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NOT_WORKING_FIELD_NUMBER: _ClassVar[int]
    website_list: PolicyTopicEvidence.WebsiteList
    text_list: PolicyTopicEvidence.TextList
    language_code: str
    destination_text_list: PolicyTopicEvidence.DestinationTextList
    destination_mismatch: PolicyTopicEvidence.DestinationMismatch
    destination_not_working: PolicyTopicEvidence.DestinationNotWorking
    def __init__(self, website_list: _Optional[_Union[PolicyTopicEvidence.WebsiteList, _Mapping]] = ..., text_list: _Optional[_Union[PolicyTopicEvidence.TextList, _Mapping]] = ..., language_code: _Optional[str] = ..., destination_text_list: _Optional[_Union[PolicyTopicEvidence.DestinationTextList, _Mapping]] = ..., destination_mismatch: _Optional[_Union[PolicyTopicEvidence.DestinationMismatch, _Mapping]] = ..., destination_not_working: _Optional[_Union[PolicyTopicEvidence.DestinationNotWorking, _Mapping]] = ...) -> None: ...

class PolicyTopicConstraint(_message.Message):
    __slots__ = ("country_constraint_list", "reseller_constraint", "certificate_missing_in_country_list", "certificate_domain_mismatch_in_country_list")
    class CountryConstraintList(_message.Message):
        __slots__ = ("total_targeted_countries", "countries")
        TOTAL_TARGETED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        total_targeted_countries: int
        countries: _containers.RepeatedCompositeFieldContainer[PolicyTopicConstraint.CountryConstraint]
        def __init__(self, total_targeted_countries: _Optional[int] = ..., countries: _Optional[_Iterable[_Union[PolicyTopicConstraint.CountryConstraint, _Mapping]]] = ...) -> None: ...
    class ResellerConstraint(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CountryConstraint(_message.Message):
        __slots__ = ("country_criterion",)
        COUNTRY_CRITERION_FIELD_NUMBER: _ClassVar[int]
        country_criterion: str
        def __init__(self, country_criterion: _Optional[str] = ...) -> None: ...
    COUNTRY_CONSTRAINT_LIST_FIELD_NUMBER: _ClassVar[int]
    RESELLER_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_MISSING_IN_COUNTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_DOMAIN_MISMATCH_IN_COUNTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    country_constraint_list: PolicyTopicConstraint.CountryConstraintList
    reseller_constraint: PolicyTopicConstraint.ResellerConstraint
    certificate_missing_in_country_list: PolicyTopicConstraint.CountryConstraintList
    certificate_domain_mismatch_in_country_list: PolicyTopicConstraint.CountryConstraintList
    def __init__(self, country_constraint_list: _Optional[_Union[PolicyTopicConstraint.CountryConstraintList, _Mapping]] = ..., reseller_constraint: _Optional[_Union[PolicyTopicConstraint.ResellerConstraint, _Mapping]] = ..., certificate_missing_in_country_list: _Optional[_Union[PolicyTopicConstraint.CountryConstraintList, _Mapping]] = ..., certificate_domain_mismatch_in_country_list: _Optional[_Union[PolicyTopicConstraint.CountryConstraintList, _Mapping]] = ...) -> None: ...
