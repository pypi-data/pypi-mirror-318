from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ('name', 'description', 'global_policy_evaluation_mode', 'admission_whitelist_patterns', 'cluster_admission_rules', 'kubernetes_namespace_admission_rules', 'kubernetes_service_account_admission_rules', 'istio_service_identity_admission_rules', 'default_admission_rule', 'update_time')

    class GlobalPolicyEvaluationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED: _ClassVar[Policy.GlobalPolicyEvaluationMode]
        ENABLE: _ClassVar[Policy.GlobalPolicyEvaluationMode]
        DISABLE: _ClassVar[Policy.GlobalPolicyEvaluationMode]
    GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED: Policy.GlobalPolicyEvaluationMode
    ENABLE: Policy.GlobalPolicyEvaluationMode
    DISABLE: Policy.GlobalPolicyEvaluationMode

    class ClusterAdmissionRulesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdmissionRule

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AdmissionRule, _Mapping]]=...) -> None:
            ...

    class KubernetesNamespaceAdmissionRulesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdmissionRule

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AdmissionRule, _Mapping]]=...) -> None:
            ...

    class KubernetesServiceAccountAdmissionRulesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdmissionRule

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AdmissionRule, _Mapping]]=...) -> None:
            ...

    class IstioServiceIdentityAdmissionRulesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdmissionRule

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AdmissionRule, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_POLICY_EVALUATION_MODE_FIELD_NUMBER: _ClassVar[int]
    ADMISSION_WHITELIST_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ADMISSION_RULES_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_NAMESPACE_ADMISSION_RULES_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_SERVICE_ACCOUNT_ADMISSION_RULES_FIELD_NUMBER: _ClassVar[int]
    ISTIO_SERVICE_IDENTITY_ADMISSION_RULES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ADMISSION_RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    global_policy_evaluation_mode: Policy.GlobalPolicyEvaluationMode
    admission_whitelist_patterns: _containers.RepeatedCompositeFieldContainer[AdmissionWhitelistPattern]
    cluster_admission_rules: _containers.MessageMap[str, AdmissionRule]
    kubernetes_namespace_admission_rules: _containers.MessageMap[str, AdmissionRule]
    kubernetes_service_account_admission_rules: _containers.MessageMap[str, AdmissionRule]
    istio_service_identity_admission_rules: _containers.MessageMap[str, AdmissionRule]
    default_admission_rule: AdmissionRule
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., global_policy_evaluation_mode: _Optional[_Union[Policy.GlobalPolicyEvaluationMode, str]]=..., admission_whitelist_patterns: _Optional[_Iterable[_Union[AdmissionWhitelistPattern, _Mapping]]]=..., cluster_admission_rules: _Optional[_Mapping[str, AdmissionRule]]=..., kubernetes_namespace_admission_rules: _Optional[_Mapping[str, AdmissionRule]]=..., kubernetes_service_account_admission_rules: _Optional[_Mapping[str, AdmissionRule]]=..., istio_service_identity_admission_rules: _Optional[_Mapping[str, AdmissionRule]]=..., default_admission_rule: _Optional[_Union[AdmissionRule, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AdmissionWhitelistPattern(_message.Message):
    __slots__ = ('name_pattern',)
    NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    name_pattern: str

    def __init__(self, name_pattern: _Optional[str]=...) -> None:
        ...

class AdmissionRule(_message.Message):
    __slots__ = ('evaluation_mode', 'require_attestations_by', 'enforcement_mode')

    class EvaluationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_MODE_UNSPECIFIED: _ClassVar[AdmissionRule.EvaluationMode]
        ALWAYS_ALLOW: _ClassVar[AdmissionRule.EvaluationMode]
        REQUIRE_ATTESTATION: _ClassVar[AdmissionRule.EvaluationMode]
        ALWAYS_DENY: _ClassVar[AdmissionRule.EvaluationMode]
    EVALUATION_MODE_UNSPECIFIED: AdmissionRule.EvaluationMode
    ALWAYS_ALLOW: AdmissionRule.EvaluationMode
    REQUIRE_ATTESTATION: AdmissionRule.EvaluationMode
    ALWAYS_DENY: AdmissionRule.EvaluationMode

    class EnforcementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENFORCEMENT_MODE_UNSPECIFIED: _ClassVar[AdmissionRule.EnforcementMode]
        ENFORCED_BLOCK_AND_AUDIT_LOG: _ClassVar[AdmissionRule.EnforcementMode]
        DRYRUN_AUDIT_LOG_ONLY: _ClassVar[AdmissionRule.EnforcementMode]
    ENFORCEMENT_MODE_UNSPECIFIED: AdmissionRule.EnforcementMode
    ENFORCED_BLOCK_AND_AUDIT_LOG: AdmissionRule.EnforcementMode
    DRYRUN_AUDIT_LOG_ONLY: AdmissionRule.EnforcementMode
    EVALUATION_MODE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ATTESTATIONS_BY_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    evaluation_mode: AdmissionRule.EvaluationMode
    require_attestations_by: _containers.RepeatedScalarFieldContainer[str]
    enforcement_mode: AdmissionRule.EnforcementMode

    def __init__(self, evaluation_mode: _Optional[_Union[AdmissionRule.EvaluationMode, str]]=..., require_attestations_by: _Optional[_Iterable[str]]=..., enforcement_mode: _Optional[_Union[AdmissionRule.EnforcementMode, str]]=...) -> None:
        ...

class Attestor(_message.Message):
    __slots__ = ('name', 'description', 'user_owned_drydock_note', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_OWNED_DRYDOCK_NOTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    user_owned_drydock_note: UserOwnedDrydockNote
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., user_owned_drydock_note: _Optional[_Union[UserOwnedDrydockNote, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UserOwnedDrydockNote(_message.Message):
    __slots__ = ('note_reference', 'public_keys', 'delegation_service_account_email')
    NOTE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    DELEGATION_SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    note_reference: str
    public_keys: _containers.RepeatedCompositeFieldContainer[AttestorPublicKey]
    delegation_service_account_email: str

    def __init__(self, note_reference: _Optional[str]=..., public_keys: _Optional[_Iterable[_Union[AttestorPublicKey, _Mapping]]]=..., delegation_service_account_email: _Optional[str]=...) -> None:
        ...

class PkixPublicKey(_message.Message):
    __slots__ = ('public_key_pem', 'signature_algorithm')

    class SignatureAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIGNATURE_ALGORITHM_UNSPECIFIED: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_PSS_2048_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_PSS_3072_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_PSS_4096_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_PSS_4096_SHA512: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_SIGN_PKCS1_2048_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_SIGN_PKCS1_3072_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_SIGN_PKCS1_4096_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        RSA_SIGN_PKCS1_4096_SHA512: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        ECDSA_P256_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        EC_SIGN_P256_SHA256: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        ECDSA_P384_SHA384: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        EC_SIGN_P384_SHA384: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        ECDSA_P521_SHA512: _ClassVar[PkixPublicKey.SignatureAlgorithm]
        EC_SIGN_P521_SHA512: _ClassVar[PkixPublicKey.SignatureAlgorithm]
    SIGNATURE_ALGORITHM_UNSPECIFIED: PkixPublicKey.SignatureAlgorithm
    RSA_PSS_2048_SHA256: PkixPublicKey.SignatureAlgorithm
    RSA_PSS_3072_SHA256: PkixPublicKey.SignatureAlgorithm
    RSA_PSS_4096_SHA256: PkixPublicKey.SignatureAlgorithm
    RSA_PSS_4096_SHA512: PkixPublicKey.SignatureAlgorithm
    RSA_SIGN_PKCS1_2048_SHA256: PkixPublicKey.SignatureAlgorithm
    RSA_SIGN_PKCS1_3072_SHA256: PkixPublicKey.SignatureAlgorithm
    RSA_SIGN_PKCS1_4096_SHA256: PkixPublicKey.SignatureAlgorithm
    RSA_SIGN_PKCS1_4096_SHA512: PkixPublicKey.SignatureAlgorithm
    ECDSA_P256_SHA256: PkixPublicKey.SignatureAlgorithm
    EC_SIGN_P256_SHA256: PkixPublicKey.SignatureAlgorithm
    ECDSA_P384_SHA384: PkixPublicKey.SignatureAlgorithm
    EC_SIGN_P384_SHA384: PkixPublicKey.SignatureAlgorithm
    ECDSA_P521_SHA512: PkixPublicKey.SignatureAlgorithm
    EC_SIGN_P521_SHA512: PkixPublicKey.SignatureAlgorithm
    PUBLIC_KEY_PEM_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    public_key_pem: str
    signature_algorithm: PkixPublicKey.SignatureAlgorithm

    def __init__(self, public_key_pem: _Optional[str]=..., signature_algorithm: _Optional[_Union[PkixPublicKey.SignatureAlgorithm, str]]=...) -> None:
        ...

class AttestorPublicKey(_message.Message):
    __slots__ = ('comment', 'id', 'ascii_armored_pgp_public_key', 'pkix_public_key')
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ASCII_ARMORED_PGP_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PKIX_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    comment: str
    id: str
    ascii_armored_pgp_public_key: str
    pkix_public_key: PkixPublicKey

    def __init__(self, comment: _Optional[str]=..., id: _Optional[str]=..., ascii_armored_pgp_public_key: _Optional[str]=..., pkix_public_key: _Optional[_Union[PkixPublicKey, _Mapping]]=...) -> None:
        ...