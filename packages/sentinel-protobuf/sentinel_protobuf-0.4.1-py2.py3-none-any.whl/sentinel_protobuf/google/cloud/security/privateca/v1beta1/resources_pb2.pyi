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

class RevocationReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REVOCATION_REASON_UNSPECIFIED: _ClassVar[RevocationReason]
    KEY_COMPROMISE: _ClassVar[RevocationReason]
    CERTIFICATE_AUTHORITY_COMPROMISE: _ClassVar[RevocationReason]
    AFFILIATION_CHANGED: _ClassVar[RevocationReason]
    SUPERSEDED: _ClassVar[RevocationReason]
    CESSATION_OF_OPERATION: _ClassVar[RevocationReason]
    CERTIFICATE_HOLD: _ClassVar[RevocationReason]
    PRIVILEGE_WITHDRAWN: _ClassVar[RevocationReason]
    ATTRIBUTE_AUTHORITY_COMPROMISE: _ClassVar[RevocationReason]
REVOCATION_REASON_UNSPECIFIED: RevocationReason
KEY_COMPROMISE: RevocationReason
CERTIFICATE_AUTHORITY_COMPROMISE: RevocationReason
AFFILIATION_CHANGED: RevocationReason
SUPERSEDED: RevocationReason
CESSATION_OF_OPERATION: RevocationReason
CERTIFICATE_HOLD: RevocationReason
PRIVILEGE_WITHDRAWN: RevocationReason
ATTRIBUTE_AUTHORITY_COMPROMISE: RevocationReason

class CertificateAuthority(_message.Message):
    __slots__ = ('name', 'type', 'tier', 'config', 'lifetime', 'key_spec', 'certificate_policy', 'issuing_options', 'subordinate_config', 'state', 'pem_ca_certificates', 'ca_certificate_descriptions', 'gcs_bucket', 'access_urls', 'create_time', 'update_time', 'delete_time', 'labels')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[CertificateAuthority.Type]
        SELF_SIGNED: _ClassVar[CertificateAuthority.Type]
        SUBORDINATE: _ClassVar[CertificateAuthority.Type]
    TYPE_UNSPECIFIED: CertificateAuthority.Type
    SELF_SIGNED: CertificateAuthority.Type
    SUBORDINATE: CertificateAuthority.Type

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[CertificateAuthority.Tier]
        ENTERPRISE: _ClassVar[CertificateAuthority.Tier]
        DEVOPS: _ClassVar[CertificateAuthority.Tier]
    TIER_UNSPECIFIED: CertificateAuthority.Tier
    ENTERPRISE: CertificateAuthority.Tier
    DEVOPS: CertificateAuthority.Tier

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CertificateAuthority.State]
        ENABLED: _ClassVar[CertificateAuthority.State]
        DISABLED: _ClassVar[CertificateAuthority.State]
        PENDING_ACTIVATION: _ClassVar[CertificateAuthority.State]
        PENDING_DELETION: _ClassVar[CertificateAuthority.State]
    STATE_UNSPECIFIED: CertificateAuthority.State
    ENABLED: CertificateAuthority.State
    DISABLED: CertificateAuthority.State
    PENDING_ACTIVATION: CertificateAuthority.State
    PENDING_DELETION: CertificateAuthority.State

    class SignHashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIGN_HASH_ALGORITHM_UNSPECIFIED: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        RSA_PSS_2048_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        RSA_PSS_3072_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        RSA_PSS_4096_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        RSA_PKCS1_2048_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        RSA_PKCS1_3072_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        RSA_PKCS1_4096_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        EC_P256_SHA256: _ClassVar[CertificateAuthority.SignHashAlgorithm]
        EC_P384_SHA384: _ClassVar[CertificateAuthority.SignHashAlgorithm]
    SIGN_HASH_ALGORITHM_UNSPECIFIED: CertificateAuthority.SignHashAlgorithm
    RSA_PSS_2048_SHA256: CertificateAuthority.SignHashAlgorithm
    RSA_PSS_3072_SHA256: CertificateAuthority.SignHashAlgorithm
    RSA_PSS_4096_SHA256: CertificateAuthority.SignHashAlgorithm
    RSA_PKCS1_2048_SHA256: CertificateAuthority.SignHashAlgorithm
    RSA_PKCS1_3072_SHA256: CertificateAuthority.SignHashAlgorithm
    RSA_PKCS1_4096_SHA256: CertificateAuthority.SignHashAlgorithm
    EC_P256_SHA256: CertificateAuthority.SignHashAlgorithm
    EC_P384_SHA384: CertificateAuthority.SignHashAlgorithm

    class IssuingOptions(_message.Message):
        __slots__ = ('include_ca_cert_url', 'include_crl_access_url')
        INCLUDE_CA_CERT_URL_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_CRL_ACCESS_URL_FIELD_NUMBER: _ClassVar[int]
        include_ca_cert_url: bool
        include_crl_access_url: bool

        def __init__(self, include_ca_cert_url: bool=..., include_crl_access_url: bool=...) -> None:
            ...

    class CertificateAuthorityPolicy(_message.Message):
        __slots__ = ('allowed_config_list', 'overwrite_config_values', 'allowed_locations_and_organizations', 'allowed_common_names', 'allowed_sans', 'maximum_lifetime', 'allowed_issuance_modes')

        class AllowedConfigList(_message.Message):
            __slots__ = ('allowed_config_values',)
            ALLOWED_CONFIG_VALUES_FIELD_NUMBER: _ClassVar[int]
            allowed_config_values: _containers.RepeatedCompositeFieldContainer[ReusableConfigWrapper]

            def __init__(self, allowed_config_values: _Optional[_Iterable[_Union[ReusableConfigWrapper, _Mapping]]]=...) -> None:
                ...

        class AllowedSubjectAltNames(_message.Message):
            __slots__ = ('allowed_dns_names', 'allowed_uris', 'allowed_email_addresses', 'allowed_ips', 'allow_globbing_dns_wildcards', 'allow_custom_sans')
            ALLOWED_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
            ALLOWED_URIS_FIELD_NUMBER: _ClassVar[int]
            ALLOWED_EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
            ALLOWED_IPS_FIELD_NUMBER: _ClassVar[int]
            ALLOW_GLOBBING_DNS_WILDCARDS_FIELD_NUMBER: _ClassVar[int]
            ALLOW_CUSTOM_SANS_FIELD_NUMBER: _ClassVar[int]
            allowed_dns_names: _containers.RepeatedScalarFieldContainer[str]
            allowed_uris: _containers.RepeatedScalarFieldContainer[str]
            allowed_email_addresses: _containers.RepeatedScalarFieldContainer[str]
            allowed_ips: _containers.RepeatedScalarFieldContainer[str]
            allow_globbing_dns_wildcards: bool
            allow_custom_sans: bool

            def __init__(self, allowed_dns_names: _Optional[_Iterable[str]]=..., allowed_uris: _Optional[_Iterable[str]]=..., allowed_email_addresses: _Optional[_Iterable[str]]=..., allowed_ips: _Optional[_Iterable[str]]=..., allow_globbing_dns_wildcards: bool=..., allow_custom_sans: bool=...) -> None:
                ...

        class IssuanceModes(_message.Message):
            __slots__ = ('allow_csr_based_issuance', 'allow_config_based_issuance')
            ALLOW_CSR_BASED_ISSUANCE_FIELD_NUMBER: _ClassVar[int]
            ALLOW_CONFIG_BASED_ISSUANCE_FIELD_NUMBER: _ClassVar[int]
            allow_csr_based_issuance: bool
            allow_config_based_issuance: bool

            def __init__(self, allow_csr_based_issuance: bool=..., allow_config_based_issuance: bool=...) -> None:
                ...
        ALLOWED_CONFIG_LIST_FIELD_NUMBER: _ClassVar[int]
        OVERWRITE_CONFIG_VALUES_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_LOCATIONS_AND_ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_COMMON_NAMES_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_SANS_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_LIFETIME_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_ISSUANCE_MODES_FIELD_NUMBER: _ClassVar[int]
        allowed_config_list: CertificateAuthority.CertificateAuthorityPolicy.AllowedConfigList
        overwrite_config_values: ReusableConfigWrapper
        allowed_locations_and_organizations: _containers.RepeatedCompositeFieldContainer[Subject]
        allowed_common_names: _containers.RepeatedScalarFieldContainer[str]
        allowed_sans: CertificateAuthority.CertificateAuthorityPolicy.AllowedSubjectAltNames
        maximum_lifetime: _duration_pb2.Duration
        allowed_issuance_modes: CertificateAuthority.CertificateAuthorityPolicy.IssuanceModes

        def __init__(self, allowed_config_list: _Optional[_Union[CertificateAuthority.CertificateAuthorityPolicy.AllowedConfigList, _Mapping]]=..., overwrite_config_values: _Optional[_Union[ReusableConfigWrapper, _Mapping]]=..., allowed_locations_and_organizations: _Optional[_Iterable[_Union[Subject, _Mapping]]]=..., allowed_common_names: _Optional[_Iterable[str]]=..., allowed_sans: _Optional[_Union[CertificateAuthority.CertificateAuthorityPolicy.AllowedSubjectAltNames, _Mapping]]=..., maximum_lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., allowed_issuance_modes: _Optional[_Union[CertificateAuthority.CertificateAuthorityPolicy.IssuanceModes, _Mapping]]=...) -> None:
            ...

    class AccessUrls(_message.Message):
        __slots__ = ('ca_certificate_access_url', 'crl_access_url')
        CA_CERTIFICATE_ACCESS_URL_FIELD_NUMBER: _ClassVar[int]
        CRL_ACCESS_URL_FIELD_NUMBER: _ClassVar[int]
        ca_certificate_access_url: str
        crl_access_url: str

        def __init__(self, ca_certificate_access_url: _Optional[str]=..., crl_access_url: _Optional[str]=...) -> None:
            ...

    class KeyVersionSpec(_message.Message):
        __slots__ = ('cloud_kms_key_version', 'algorithm')
        CLOUD_KMS_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
        ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        cloud_kms_key_version: str
        algorithm: CertificateAuthority.SignHashAlgorithm

        def __init__(self, cloud_kms_key_version: _Optional[str]=..., algorithm: _Optional[_Union[CertificateAuthority.SignHashAlgorithm, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    ISSUING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SUBORDINATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PEM_CA_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    ACCESS_URLS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: CertificateAuthority.Type
    tier: CertificateAuthority.Tier
    config: CertificateConfig
    lifetime: _duration_pb2.Duration
    key_spec: CertificateAuthority.KeyVersionSpec
    certificate_policy: CertificateAuthority.CertificateAuthorityPolicy
    issuing_options: CertificateAuthority.IssuingOptions
    subordinate_config: SubordinateConfig
    state: CertificateAuthority.State
    pem_ca_certificates: _containers.RepeatedScalarFieldContainer[str]
    ca_certificate_descriptions: _containers.RepeatedCompositeFieldContainer[CertificateDescription]
    gcs_bucket: str
    access_urls: CertificateAuthority.AccessUrls
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[CertificateAuthority.Type, str]]=..., tier: _Optional[_Union[CertificateAuthority.Tier, str]]=..., config: _Optional[_Union[CertificateConfig, _Mapping]]=..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., key_spec: _Optional[_Union[CertificateAuthority.KeyVersionSpec, _Mapping]]=..., certificate_policy: _Optional[_Union[CertificateAuthority.CertificateAuthorityPolicy, _Mapping]]=..., issuing_options: _Optional[_Union[CertificateAuthority.IssuingOptions, _Mapping]]=..., subordinate_config: _Optional[_Union[SubordinateConfig, _Mapping]]=..., state: _Optional[_Union[CertificateAuthority.State, str]]=..., pem_ca_certificates: _Optional[_Iterable[str]]=..., ca_certificate_descriptions: _Optional[_Iterable[_Union[CertificateDescription, _Mapping]]]=..., gcs_bucket: _Optional[str]=..., access_urls: _Optional[_Union[CertificateAuthority.AccessUrls, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CertificateRevocationList(_message.Message):
    __slots__ = ('name', 'sequence_number', 'revoked_certificates', 'pem_crl', 'access_url', 'state', 'create_time', 'update_time', 'labels')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CertificateRevocationList.State]
        ACTIVE: _ClassVar[CertificateRevocationList.State]
        SUPERSEDED: _ClassVar[CertificateRevocationList.State]
    STATE_UNSPECIFIED: CertificateRevocationList.State
    ACTIVE: CertificateRevocationList.State
    SUPERSEDED: CertificateRevocationList.State

    class RevokedCertificate(_message.Message):
        __slots__ = ('certificate', 'hex_serial_number', 'revocation_reason')
        CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        HEX_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        REVOCATION_REASON_FIELD_NUMBER: _ClassVar[int]
        certificate: str
        hex_serial_number: str
        revocation_reason: RevocationReason

        def __init__(self, certificate: _Optional[str]=..., hex_serial_number: _Optional[str]=..., revocation_reason: _Optional[_Union[RevocationReason, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVOKED_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    PEM_CRL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    sequence_number: int
    revoked_certificates: _containers.RepeatedCompositeFieldContainer[CertificateRevocationList.RevokedCertificate]
    pem_crl: str
    access_url: str
    state: CertificateRevocationList.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., sequence_number: _Optional[int]=..., revoked_certificates: _Optional[_Iterable[_Union[CertificateRevocationList.RevokedCertificate, _Mapping]]]=..., pem_crl: _Optional[str]=..., access_url: _Optional[str]=..., state: _Optional[_Union[CertificateRevocationList.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Certificate(_message.Message):
    __slots__ = ('name', 'pem_csr', 'config', 'lifetime', 'revocation_details', 'pem_certificate', 'certificate_description', 'pem_certificate_chain', 'create_time', 'update_time', 'labels')

    class RevocationDetails(_message.Message):
        __slots__ = ('revocation_state', 'revocation_time')
        REVOCATION_STATE_FIELD_NUMBER: _ClassVar[int]
        REVOCATION_TIME_FIELD_NUMBER: _ClassVar[int]
        revocation_state: RevocationReason
        revocation_time: _timestamp_pb2.Timestamp

        def __init__(self, revocation_state: _Optional[_Union[RevocationReason, str]]=..., revocation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEM_CSR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PEM_CERTIFICATE_CHAIN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    pem_csr: str
    config: CertificateConfig
    lifetime: _duration_pb2.Duration
    revocation_details: Certificate.RevocationDetails
    pem_certificate: str
    certificate_description: CertificateDescription
    pem_certificate_chain: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., pem_csr: _Optional[str]=..., config: _Optional[_Union[CertificateConfig, _Mapping]]=..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., revocation_details: _Optional[_Union[Certificate.RevocationDetails, _Mapping]]=..., pem_certificate: _Optional[str]=..., certificate_description: _Optional[_Union[CertificateDescription, _Mapping]]=..., pem_certificate_chain: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ReusableConfig(_message.Message):
    __slots__ = ('name', 'values', 'description', 'create_time', 'update_time', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: ReusableConfigValues
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., values: _Optional[_Union[ReusableConfigValues, _Mapping]]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ReusableConfigValues(_message.Message):
    __slots__ = ('key_usage', 'ca_options', 'policy_ids', 'aia_ocsp_servers', 'additional_extensions')

    class CaOptions(_message.Message):
        __slots__ = ('is_ca', 'max_issuer_path_length')
        IS_CA_FIELD_NUMBER: _ClassVar[int]
        MAX_ISSUER_PATH_LENGTH_FIELD_NUMBER: _ClassVar[int]
        is_ca: _wrappers_pb2.BoolValue
        max_issuer_path_length: _wrappers_pb2.Int32Value

        def __init__(self, is_ca: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., max_issuer_path_length: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
            ...
    KEY_USAGE_FIELD_NUMBER: _ClassVar[int]
    CA_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    POLICY_IDS_FIELD_NUMBER: _ClassVar[int]
    AIA_OCSP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    key_usage: KeyUsage
    ca_options: ReusableConfigValues.CaOptions
    policy_ids: _containers.RepeatedCompositeFieldContainer[ObjectId]
    aia_ocsp_servers: _containers.RepeatedScalarFieldContainer[str]
    additional_extensions: _containers.RepeatedCompositeFieldContainer[X509Extension]

    def __init__(self, key_usage: _Optional[_Union[KeyUsage, _Mapping]]=..., ca_options: _Optional[_Union[ReusableConfigValues.CaOptions, _Mapping]]=..., policy_ids: _Optional[_Iterable[_Union[ObjectId, _Mapping]]]=..., aia_ocsp_servers: _Optional[_Iterable[str]]=..., additional_extensions: _Optional[_Iterable[_Union[X509Extension, _Mapping]]]=...) -> None:
        ...

class ReusableConfigWrapper(_message.Message):
    __slots__ = ('reusable_config', 'reusable_config_values')
    REUSABLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REUSABLE_CONFIG_VALUES_FIELD_NUMBER: _ClassVar[int]
    reusable_config: str
    reusable_config_values: ReusableConfigValues

    def __init__(self, reusable_config: _Optional[str]=..., reusable_config_values: _Optional[_Union[ReusableConfigValues, _Mapping]]=...) -> None:
        ...

class SubordinateConfig(_message.Message):
    __slots__ = ('certificate_authority', 'pem_issuer_chain')

    class SubordinateConfigChain(_message.Message):
        __slots__ = ('pem_certificates',)
        PEM_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        pem_certificates: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, pem_certificates: _Optional[_Iterable[str]]=...) -> None:
            ...
    CERTIFICATE_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    PEM_ISSUER_CHAIN_FIELD_NUMBER: _ClassVar[int]
    certificate_authority: str
    pem_issuer_chain: SubordinateConfig.SubordinateConfigChain

    def __init__(self, certificate_authority: _Optional[str]=..., pem_issuer_chain: _Optional[_Union[SubordinateConfig.SubordinateConfigChain, _Mapping]]=...) -> None:
        ...

class PublicKey(_message.Message):
    __slots__ = ('type', 'key')

    class KeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_TYPE_UNSPECIFIED: _ClassVar[PublicKey.KeyType]
        PEM_RSA_KEY: _ClassVar[PublicKey.KeyType]
        PEM_EC_KEY: _ClassVar[PublicKey.KeyType]
    KEY_TYPE_UNSPECIFIED: PublicKey.KeyType
    PEM_RSA_KEY: PublicKey.KeyType
    PEM_EC_KEY: PublicKey.KeyType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    type: PublicKey.KeyType
    key: bytes

    def __init__(self, type: _Optional[_Union[PublicKey.KeyType, str]]=..., key: _Optional[bytes]=...) -> None:
        ...

class CertificateConfig(_message.Message):
    __slots__ = ('subject_config', 'reusable_config', 'public_key')

    class SubjectConfig(_message.Message):
        __slots__ = ('subject', 'common_name', 'subject_alt_name')
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_ALT_NAME_FIELD_NUMBER: _ClassVar[int]
        subject: Subject
        common_name: str
        subject_alt_name: SubjectAltNames

        def __init__(self, subject: _Optional[_Union[Subject, _Mapping]]=..., common_name: _Optional[str]=..., subject_alt_name: _Optional[_Union[SubjectAltNames, _Mapping]]=...) -> None:
            ...
    SUBJECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REUSABLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    subject_config: CertificateConfig.SubjectConfig
    reusable_config: ReusableConfigWrapper
    public_key: PublicKey

    def __init__(self, subject_config: _Optional[_Union[CertificateConfig.SubjectConfig, _Mapping]]=..., reusable_config: _Optional[_Union[ReusableConfigWrapper, _Mapping]]=..., public_key: _Optional[_Union[PublicKey, _Mapping]]=...) -> None:
        ...

class CertificateDescription(_message.Message):
    __slots__ = ('subject_description', 'config_values', 'public_key', 'subject_key_id', 'authority_key_id', 'crl_distribution_points', 'aia_issuing_certificate_urls', 'cert_fingerprint')

    class SubjectDescription(_message.Message):
        __slots__ = ('subject', 'common_name', 'subject_alt_name', 'hex_serial_number', 'lifetime', 'not_before_time', 'not_after_time')
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_ALT_NAME_FIELD_NUMBER: _ClassVar[int]
        HEX_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LIFETIME_FIELD_NUMBER: _ClassVar[int]
        NOT_BEFORE_TIME_FIELD_NUMBER: _ClassVar[int]
        NOT_AFTER_TIME_FIELD_NUMBER: _ClassVar[int]
        subject: Subject
        common_name: str
        subject_alt_name: SubjectAltNames
        hex_serial_number: str
        lifetime: _duration_pb2.Duration
        not_before_time: _timestamp_pb2.Timestamp
        not_after_time: _timestamp_pb2.Timestamp

        def __init__(self, subject: _Optional[_Union[Subject, _Mapping]]=..., common_name: _Optional[str]=..., subject_alt_name: _Optional[_Union[SubjectAltNames, _Mapping]]=..., hex_serial_number: _Optional[str]=..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., not_before_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., not_after_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class KeyId(_message.Message):
        __slots__ = ('key_id',)
        KEY_ID_FIELD_NUMBER: _ClassVar[int]
        key_id: str

        def __init__(self, key_id: _Optional[str]=...) -> None:
            ...

    class CertificateFingerprint(_message.Message):
        __slots__ = ('sha256_hash',)
        SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
        sha256_hash: str

        def __init__(self, sha256_hash: _Optional[str]=...) -> None:
            ...
    SUBJECT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUES_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CRL_DISTRIBUTION_POINTS_FIELD_NUMBER: _ClassVar[int]
    AIA_ISSUING_CERTIFICATE_URLS_FIELD_NUMBER: _ClassVar[int]
    CERT_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    subject_description: CertificateDescription.SubjectDescription
    config_values: ReusableConfigValues
    public_key: PublicKey
    subject_key_id: CertificateDescription.KeyId
    authority_key_id: CertificateDescription.KeyId
    crl_distribution_points: _containers.RepeatedScalarFieldContainer[str]
    aia_issuing_certificate_urls: _containers.RepeatedScalarFieldContainer[str]
    cert_fingerprint: CertificateDescription.CertificateFingerprint

    def __init__(self, subject_description: _Optional[_Union[CertificateDescription.SubjectDescription, _Mapping]]=..., config_values: _Optional[_Union[ReusableConfigValues, _Mapping]]=..., public_key: _Optional[_Union[PublicKey, _Mapping]]=..., subject_key_id: _Optional[_Union[CertificateDescription.KeyId, _Mapping]]=..., authority_key_id: _Optional[_Union[CertificateDescription.KeyId, _Mapping]]=..., crl_distribution_points: _Optional[_Iterable[str]]=..., aia_issuing_certificate_urls: _Optional[_Iterable[str]]=..., cert_fingerprint: _Optional[_Union[CertificateDescription.CertificateFingerprint, _Mapping]]=...) -> None:
        ...

class ObjectId(_message.Message):
    __slots__ = ('object_id_path',)
    OBJECT_ID_PATH_FIELD_NUMBER: _ClassVar[int]
    object_id_path: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, object_id_path: _Optional[_Iterable[int]]=...) -> None:
        ...

class X509Extension(_message.Message):
    __slots__ = ('object_id', 'critical', 'value')
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    object_id: ObjectId
    critical: bool
    value: bytes

    def __init__(self, object_id: _Optional[_Union[ObjectId, _Mapping]]=..., critical: bool=..., value: _Optional[bytes]=...) -> None:
        ...

class KeyUsage(_message.Message):
    __slots__ = ('base_key_usage', 'extended_key_usage', 'unknown_extended_key_usages')

    class KeyUsageOptions(_message.Message):
        __slots__ = ('digital_signature', 'content_commitment', 'key_encipherment', 'data_encipherment', 'key_agreement', 'cert_sign', 'crl_sign', 'encipher_only', 'decipher_only')
        DIGITAL_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
        KEY_ENCIPHERMENT_FIELD_NUMBER: _ClassVar[int]
        DATA_ENCIPHERMENT_FIELD_NUMBER: _ClassVar[int]
        KEY_AGREEMENT_FIELD_NUMBER: _ClassVar[int]
        CERT_SIGN_FIELD_NUMBER: _ClassVar[int]
        CRL_SIGN_FIELD_NUMBER: _ClassVar[int]
        ENCIPHER_ONLY_FIELD_NUMBER: _ClassVar[int]
        DECIPHER_ONLY_FIELD_NUMBER: _ClassVar[int]
        digital_signature: bool
        content_commitment: bool
        key_encipherment: bool
        data_encipherment: bool
        key_agreement: bool
        cert_sign: bool
        crl_sign: bool
        encipher_only: bool
        decipher_only: bool

        def __init__(self, digital_signature: bool=..., content_commitment: bool=..., key_encipherment: bool=..., data_encipherment: bool=..., key_agreement: bool=..., cert_sign: bool=..., crl_sign: bool=..., encipher_only: bool=..., decipher_only: bool=...) -> None:
            ...

    class ExtendedKeyUsageOptions(_message.Message):
        __slots__ = ('server_auth', 'client_auth', 'code_signing', 'email_protection', 'time_stamping', 'ocsp_signing')
        SERVER_AUTH_FIELD_NUMBER: _ClassVar[int]
        CLIENT_AUTH_FIELD_NUMBER: _ClassVar[int]
        CODE_SIGNING_FIELD_NUMBER: _ClassVar[int]
        EMAIL_PROTECTION_FIELD_NUMBER: _ClassVar[int]
        TIME_STAMPING_FIELD_NUMBER: _ClassVar[int]
        OCSP_SIGNING_FIELD_NUMBER: _ClassVar[int]
        server_auth: bool
        client_auth: bool
        code_signing: bool
        email_protection: bool
        time_stamping: bool
        ocsp_signing: bool

        def __init__(self, server_auth: bool=..., client_auth: bool=..., code_signing: bool=..., email_protection: bool=..., time_stamping: bool=..., ocsp_signing: bool=...) -> None:
            ...
    BASE_KEY_USAGE_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_KEY_USAGE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTENDED_KEY_USAGES_FIELD_NUMBER: _ClassVar[int]
    base_key_usage: KeyUsage.KeyUsageOptions
    extended_key_usage: KeyUsage.ExtendedKeyUsageOptions
    unknown_extended_key_usages: _containers.RepeatedCompositeFieldContainer[ObjectId]

    def __init__(self, base_key_usage: _Optional[_Union[KeyUsage.KeyUsageOptions, _Mapping]]=..., extended_key_usage: _Optional[_Union[KeyUsage.ExtendedKeyUsageOptions, _Mapping]]=..., unknown_extended_key_usages: _Optional[_Iterable[_Union[ObjectId, _Mapping]]]=...) -> None:
        ...

class Subject(_message.Message):
    __slots__ = ('country_code', 'organization', 'organizational_unit', 'locality', 'province', 'street_address', 'postal_code')
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    organization: str
    organizational_unit: str
    locality: str
    province: str
    street_address: str
    postal_code: str

    def __init__(self, country_code: _Optional[str]=..., organization: _Optional[str]=..., organizational_unit: _Optional[str]=..., locality: _Optional[str]=..., province: _Optional[str]=..., street_address: _Optional[str]=..., postal_code: _Optional[str]=...) -> None:
        ...

class SubjectAltNames(_message.Message):
    __slots__ = ('dns_names', 'uris', 'email_addresses', 'ip_addresses', 'custom_sans')
    DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
    URIS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SANS_FIELD_NUMBER: _ClassVar[int]
    dns_names: _containers.RepeatedScalarFieldContainer[str]
    uris: _containers.RepeatedScalarFieldContainer[str]
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    custom_sans: _containers.RepeatedCompositeFieldContainer[X509Extension]

    def __init__(self, dns_names: _Optional[_Iterable[str]]=..., uris: _Optional[_Iterable[str]]=..., email_addresses: _Optional[_Iterable[str]]=..., ip_addresses: _Optional[_Iterable[str]]=..., custom_sans: _Optional[_Iterable[_Union[X509Extension, _Mapping]]]=...) -> None:
        ...