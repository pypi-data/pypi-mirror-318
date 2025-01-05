from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProtectionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROTECTION_LEVEL_UNSPECIFIED: _ClassVar[ProtectionLevel]
    SOFTWARE: _ClassVar[ProtectionLevel]
    HSM: _ClassVar[ProtectionLevel]
    EXTERNAL: _ClassVar[ProtectionLevel]
    EXTERNAL_VPC: _ClassVar[ProtectionLevel]

class AccessReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REASON_UNSPECIFIED: _ClassVar[AccessReason]
    CUSTOMER_INITIATED_SUPPORT: _ClassVar[AccessReason]
    GOOGLE_INITIATED_SERVICE: _ClassVar[AccessReason]
    THIRD_PARTY_DATA_REQUEST: _ClassVar[AccessReason]
    GOOGLE_INITIATED_REVIEW: _ClassVar[AccessReason]
    CUSTOMER_INITIATED_ACCESS: _ClassVar[AccessReason]
    GOOGLE_INITIATED_SYSTEM_OPERATION: _ClassVar[AccessReason]
    REASON_NOT_EXPECTED: _ClassVar[AccessReason]
    MODIFIED_CUSTOMER_INITIATED_ACCESS: _ClassVar[AccessReason]
    MODIFIED_GOOGLE_INITIATED_SYSTEM_OPERATION: _ClassVar[AccessReason]
    GOOGLE_RESPONSE_TO_PRODUCTION_ALERT: _ClassVar[AccessReason]
    CUSTOMER_AUTHORIZED_WORKFLOW_SERVICING: _ClassVar[AccessReason]
PROTECTION_LEVEL_UNSPECIFIED: ProtectionLevel
SOFTWARE: ProtectionLevel
HSM: ProtectionLevel
EXTERNAL: ProtectionLevel
EXTERNAL_VPC: ProtectionLevel
REASON_UNSPECIFIED: AccessReason
CUSTOMER_INITIATED_SUPPORT: AccessReason
GOOGLE_INITIATED_SERVICE: AccessReason
THIRD_PARTY_DATA_REQUEST: AccessReason
GOOGLE_INITIATED_REVIEW: AccessReason
CUSTOMER_INITIATED_ACCESS: AccessReason
GOOGLE_INITIATED_SYSTEM_OPERATION: AccessReason
REASON_NOT_EXPECTED: AccessReason
MODIFIED_CUSTOMER_INITIATED_ACCESS: AccessReason
MODIFIED_GOOGLE_INITIATED_SYSTEM_OPERATION: AccessReason
GOOGLE_RESPONSE_TO_PRODUCTION_ALERT: AccessReason
CUSTOMER_AUTHORIZED_WORKFLOW_SERVICING: AccessReason

class KeyRing(_message.Message):
    __slots__ = ('name', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CryptoKey(_message.Message):
    __slots__ = ('name', 'primary', 'purpose', 'create_time', 'next_rotation_time', 'rotation_period', 'version_template', 'labels', 'import_only', 'destroy_scheduled_duration', 'crypto_key_backend', 'key_access_justifications_policy')

    class CryptoKeyPurpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CRYPTO_KEY_PURPOSE_UNSPECIFIED: _ClassVar[CryptoKey.CryptoKeyPurpose]
        ENCRYPT_DECRYPT: _ClassVar[CryptoKey.CryptoKeyPurpose]
        ASYMMETRIC_SIGN: _ClassVar[CryptoKey.CryptoKeyPurpose]
        ASYMMETRIC_DECRYPT: _ClassVar[CryptoKey.CryptoKeyPurpose]
        RAW_ENCRYPT_DECRYPT: _ClassVar[CryptoKey.CryptoKeyPurpose]
        MAC: _ClassVar[CryptoKey.CryptoKeyPurpose]
    CRYPTO_KEY_PURPOSE_UNSPECIFIED: CryptoKey.CryptoKeyPurpose
    ENCRYPT_DECRYPT: CryptoKey.CryptoKeyPurpose
    ASYMMETRIC_SIGN: CryptoKey.CryptoKeyPurpose
    ASYMMETRIC_DECRYPT: CryptoKey.CryptoKeyPurpose
    RAW_ENCRYPT_DECRYPT: CryptoKey.CryptoKeyPurpose
    MAC: CryptoKey.CryptoKeyPurpose

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_ROTATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ROTATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    VERSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ONLY_FIELD_NUMBER: _ClassVar[int]
    DESTROY_SCHEDULED_DURATION_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_BACKEND_FIELD_NUMBER: _ClassVar[int]
    KEY_ACCESS_JUSTIFICATIONS_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    primary: CryptoKeyVersion
    purpose: CryptoKey.CryptoKeyPurpose
    create_time: _timestamp_pb2.Timestamp
    next_rotation_time: _timestamp_pb2.Timestamp
    rotation_period: _duration_pb2.Duration
    version_template: CryptoKeyVersionTemplate
    labels: _containers.ScalarMap[str, str]
    import_only: bool
    destroy_scheduled_duration: _duration_pb2.Duration
    crypto_key_backend: str
    key_access_justifications_policy: KeyAccessJustificationsPolicy

    def __init__(self, name: _Optional[str]=..., primary: _Optional[_Union[CryptoKeyVersion, _Mapping]]=..., purpose: _Optional[_Union[CryptoKey.CryptoKeyPurpose, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_rotation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rotation_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., version_template: _Optional[_Union[CryptoKeyVersionTemplate, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., import_only: bool=..., destroy_scheduled_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., crypto_key_backend: _Optional[str]=..., key_access_justifications_policy: _Optional[_Union[KeyAccessJustificationsPolicy, _Mapping]]=...) -> None:
        ...

class CryptoKeyVersionTemplate(_message.Message):
    __slots__ = ('protection_level', 'algorithm')
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    protection_level: ProtectionLevel
    algorithm: CryptoKeyVersion.CryptoKeyVersionAlgorithm

    def __init__(self, protection_level: _Optional[_Union[ProtectionLevel, str]]=..., algorithm: _Optional[_Union[CryptoKeyVersion.CryptoKeyVersionAlgorithm, str]]=...) -> None:
        ...

class KeyOperationAttestation(_message.Message):
    __slots__ = ('format', 'content', 'cert_chains')

    class AttestationFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ATTESTATION_FORMAT_UNSPECIFIED: _ClassVar[KeyOperationAttestation.AttestationFormat]
        CAVIUM_V1_COMPRESSED: _ClassVar[KeyOperationAttestation.AttestationFormat]
        CAVIUM_V2_COMPRESSED: _ClassVar[KeyOperationAttestation.AttestationFormat]
    ATTESTATION_FORMAT_UNSPECIFIED: KeyOperationAttestation.AttestationFormat
    CAVIUM_V1_COMPRESSED: KeyOperationAttestation.AttestationFormat
    CAVIUM_V2_COMPRESSED: KeyOperationAttestation.AttestationFormat

    class CertificateChains(_message.Message):
        __slots__ = ('cavium_certs', 'google_card_certs', 'google_partition_certs')
        CAVIUM_CERTS_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_CARD_CERTS_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_PARTITION_CERTS_FIELD_NUMBER: _ClassVar[int]
        cavium_certs: _containers.RepeatedScalarFieldContainer[str]
        google_card_certs: _containers.RepeatedScalarFieldContainer[str]
        google_partition_certs: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, cavium_certs: _Optional[_Iterable[str]]=..., google_card_certs: _Optional[_Iterable[str]]=..., google_partition_certs: _Optional[_Iterable[str]]=...) -> None:
            ...
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CERT_CHAINS_FIELD_NUMBER: _ClassVar[int]
    format: KeyOperationAttestation.AttestationFormat
    content: bytes
    cert_chains: KeyOperationAttestation.CertificateChains

    def __init__(self, format: _Optional[_Union[KeyOperationAttestation.AttestationFormat, str]]=..., content: _Optional[bytes]=..., cert_chains: _Optional[_Union[KeyOperationAttestation.CertificateChains, _Mapping]]=...) -> None:
        ...

class CryptoKeyVersion(_message.Message):
    __slots__ = ('name', 'state', 'protection_level', 'algorithm', 'attestation', 'create_time', 'generate_time', 'destroy_time', 'destroy_event_time', 'import_job', 'import_time', 'import_failure_reason', 'generation_failure_reason', 'external_destruction_failure_reason', 'external_protection_level_options', 'reimport_eligible')

    class CryptoKeyVersionAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        GOOGLE_SYMMETRIC_ENCRYPTION: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        AES_128_GCM: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        AES_256_GCM: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        AES_128_CBC: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        AES_256_CBC: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        AES_128_CTR: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        AES_256_CTR: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PSS_2048_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PSS_3072_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PSS_4096_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PSS_4096_SHA512: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PKCS1_2048_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PKCS1_3072_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PKCS1_4096_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_PKCS1_4096_SHA512: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_RAW_PKCS1_2048: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_RAW_PKCS1_3072: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_SIGN_RAW_PKCS1_4096: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_2048_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_3072_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_4096_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_4096_SHA512: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_2048_SHA1: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_3072_SHA1: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        RSA_DECRYPT_OAEP_4096_SHA1: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        EC_SIGN_P256_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        EC_SIGN_P384_SHA384: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        EC_SIGN_SECP256K1_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        EC_SIGN_ED25519: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        HMAC_SHA256: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        HMAC_SHA1: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        HMAC_SHA384: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        HMAC_SHA512: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        HMAC_SHA224: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        EXTERNAL_SYMMETRIC_ENCRYPTION: _ClassVar[CryptoKeyVersion.CryptoKeyVersionAlgorithm]
    CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    GOOGLE_SYMMETRIC_ENCRYPTION: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    AES_128_GCM: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    AES_256_GCM: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    AES_128_CBC: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    AES_256_CBC: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    AES_128_CTR: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    AES_256_CTR: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PSS_2048_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PSS_3072_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PSS_4096_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PSS_4096_SHA512: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PKCS1_2048_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PKCS1_3072_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PKCS1_4096_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_PKCS1_4096_SHA512: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_RAW_PKCS1_2048: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_RAW_PKCS1_3072: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_SIGN_RAW_PKCS1_4096: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_2048_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_3072_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_4096_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_4096_SHA512: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_2048_SHA1: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_3072_SHA1: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    RSA_DECRYPT_OAEP_4096_SHA1: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    EC_SIGN_P256_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    EC_SIGN_P384_SHA384: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    EC_SIGN_SECP256K1_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    EC_SIGN_ED25519: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    HMAC_SHA256: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    HMAC_SHA1: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    HMAC_SHA384: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    HMAC_SHA512: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    HMAC_SHA224: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    EXTERNAL_SYMMETRIC_ENCRYPTION: CryptoKeyVersion.CryptoKeyVersionAlgorithm

    class CryptoKeyVersionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CRYPTO_KEY_VERSION_STATE_UNSPECIFIED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        PENDING_GENERATION: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        ENABLED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        DISABLED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        DESTROYED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        DESTROY_SCHEDULED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        PENDING_IMPORT: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        IMPORT_FAILED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        GENERATION_FAILED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        PENDING_EXTERNAL_DESTRUCTION: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
        EXTERNAL_DESTRUCTION_FAILED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionState]
    CRYPTO_KEY_VERSION_STATE_UNSPECIFIED: CryptoKeyVersion.CryptoKeyVersionState
    PENDING_GENERATION: CryptoKeyVersion.CryptoKeyVersionState
    ENABLED: CryptoKeyVersion.CryptoKeyVersionState
    DISABLED: CryptoKeyVersion.CryptoKeyVersionState
    DESTROYED: CryptoKeyVersion.CryptoKeyVersionState
    DESTROY_SCHEDULED: CryptoKeyVersion.CryptoKeyVersionState
    PENDING_IMPORT: CryptoKeyVersion.CryptoKeyVersionState
    IMPORT_FAILED: CryptoKeyVersion.CryptoKeyVersionState
    GENERATION_FAILED: CryptoKeyVersion.CryptoKeyVersionState
    PENDING_EXTERNAL_DESTRUCTION: CryptoKeyVersion.CryptoKeyVersionState
    EXTERNAL_DESTRUCTION_FAILED: CryptoKeyVersion.CryptoKeyVersionState

    class CryptoKeyVersionView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CRYPTO_KEY_VERSION_VIEW_UNSPECIFIED: _ClassVar[CryptoKeyVersion.CryptoKeyVersionView]
        FULL: _ClassVar[CryptoKeyVersion.CryptoKeyVersionView]
    CRYPTO_KEY_VERSION_VIEW_UNSPECIFIED: CryptoKeyVersion.CryptoKeyVersionView
    FULL: CryptoKeyVersion.CryptoKeyVersionView
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GENERATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESTROY_TIME_FIELD_NUMBER: _ClassVar[int]
    DESTROY_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TIME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DESTRUCTION_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PROTECTION_LEVEL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REIMPORT_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: CryptoKeyVersion.CryptoKeyVersionState
    protection_level: ProtectionLevel
    algorithm: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    attestation: KeyOperationAttestation
    create_time: _timestamp_pb2.Timestamp
    generate_time: _timestamp_pb2.Timestamp
    destroy_time: _timestamp_pb2.Timestamp
    destroy_event_time: _timestamp_pb2.Timestamp
    import_job: str
    import_time: _timestamp_pb2.Timestamp
    import_failure_reason: str
    generation_failure_reason: str
    external_destruction_failure_reason: str
    external_protection_level_options: ExternalProtectionLevelOptions
    reimport_eligible: bool

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[CryptoKeyVersion.CryptoKeyVersionState, str]]=..., protection_level: _Optional[_Union[ProtectionLevel, str]]=..., algorithm: _Optional[_Union[CryptoKeyVersion.CryptoKeyVersionAlgorithm, str]]=..., attestation: _Optional[_Union[KeyOperationAttestation, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., generate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., destroy_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., destroy_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., import_job: _Optional[str]=..., import_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., import_failure_reason: _Optional[str]=..., generation_failure_reason: _Optional[str]=..., external_destruction_failure_reason: _Optional[str]=..., external_protection_level_options: _Optional[_Union[ExternalProtectionLevelOptions, _Mapping]]=..., reimport_eligible: bool=...) -> None:
        ...

class PublicKey(_message.Message):
    __slots__ = ('pem', 'algorithm', 'pem_crc32c', 'name', 'protection_level')
    PEM_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PEM_CRC32C_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    pem: str
    algorithm: CryptoKeyVersion.CryptoKeyVersionAlgorithm
    pem_crc32c: _wrappers_pb2.Int64Value
    name: str
    protection_level: ProtectionLevel

    def __init__(self, pem: _Optional[str]=..., algorithm: _Optional[_Union[CryptoKeyVersion.CryptoKeyVersionAlgorithm, str]]=..., pem_crc32c: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., name: _Optional[str]=..., protection_level: _Optional[_Union[ProtectionLevel, str]]=...) -> None:
        ...

class ImportJob(_message.Message):
    __slots__ = ('name', 'import_method', 'protection_level', 'create_time', 'generate_time', 'expire_time', 'expire_event_time', 'state', 'public_key', 'attestation')

    class ImportMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPORT_METHOD_UNSPECIFIED: _ClassVar[ImportJob.ImportMethod]
        RSA_OAEP_3072_SHA1_AES_256: _ClassVar[ImportJob.ImportMethod]
        RSA_OAEP_4096_SHA1_AES_256: _ClassVar[ImportJob.ImportMethod]
        RSA_OAEP_3072_SHA256_AES_256: _ClassVar[ImportJob.ImportMethod]
        RSA_OAEP_4096_SHA256_AES_256: _ClassVar[ImportJob.ImportMethod]
        RSA_OAEP_3072_SHA256: _ClassVar[ImportJob.ImportMethod]
        RSA_OAEP_4096_SHA256: _ClassVar[ImportJob.ImportMethod]
    IMPORT_METHOD_UNSPECIFIED: ImportJob.ImportMethod
    RSA_OAEP_3072_SHA1_AES_256: ImportJob.ImportMethod
    RSA_OAEP_4096_SHA1_AES_256: ImportJob.ImportMethod
    RSA_OAEP_3072_SHA256_AES_256: ImportJob.ImportMethod
    RSA_OAEP_4096_SHA256_AES_256: ImportJob.ImportMethod
    RSA_OAEP_3072_SHA256: ImportJob.ImportMethod
    RSA_OAEP_4096_SHA256: ImportJob.ImportMethod

    class ImportJobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPORT_JOB_STATE_UNSPECIFIED: _ClassVar[ImportJob.ImportJobState]
        PENDING_GENERATION: _ClassVar[ImportJob.ImportJobState]
        ACTIVE: _ClassVar[ImportJob.ImportJobState]
        EXPIRED: _ClassVar[ImportJob.ImportJobState]
    IMPORT_JOB_STATE_UNSPECIFIED: ImportJob.ImportJobState
    PENDING_GENERATION: ImportJob.ImportJobState
    ACTIVE: ImportJob.ImportJobState
    EXPIRED: ImportJob.ImportJobState

    class WrappingPublicKey(_message.Message):
        __slots__ = ('pem',)
        PEM_FIELD_NUMBER: _ClassVar[int]
        pem: str

        def __init__(self, pem: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_METHOD_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GENERATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    import_method: ImportJob.ImportMethod
    protection_level: ProtectionLevel
    create_time: _timestamp_pb2.Timestamp
    generate_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    expire_event_time: _timestamp_pb2.Timestamp
    state: ImportJob.ImportJobState
    public_key: ImportJob.WrappingPublicKey
    attestation: KeyOperationAttestation

    def __init__(self, name: _Optional[str]=..., import_method: _Optional[_Union[ImportJob.ImportMethod, str]]=..., protection_level: _Optional[_Union[ProtectionLevel, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., generate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ImportJob.ImportJobState, str]]=..., public_key: _Optional[_Union[ImportJob.WrappingPublicKey, _Mapping]]=..., attestation: _Optional[_Union[KeyOperationAttestation, _Mapping]]=...) -> None:
        ...

class ExternalProtectionLevelOptions(_message.Message):
    __slots__ = ('external_key_uri', 'ekm_connection_key_path')
    EXTERNAL_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    EKM_CONNECTION_KEY_PATH_FIELD_NUMBER: _ClassVar[int]
    external_key_uri: str
    ekm_connection_key_path: str

    def __init__(self, external_key_uri: _Optional[str]=..., ekm_connection_key_path: _Optional[str]=...) -> None:
        ...

class KeyAccessJustificationsPolicy(_message.Message):
    __slots__ = ('allowed_access_reasons',)
    ALLOWED_ACCESS_REASONS_FIELD_NUMBER: _ClassVar[int]
    allowed_access_reasons: _containers.RepeatedScalarFieldContainer[AccessReason]

    def __init__(self, allowed_access_reasons: _Optional[_Iterable[_Union[AccessReason, str]]]=...) -> None:
        ...