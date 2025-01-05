from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListCertificateIssuanceConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCertificateIssuanceConfigsResponse(_message.Message):
    __slots__ = ('certificate_issuance_configs', 'next_page_token', 'unreachable')
    CERTIFICATE_ISSUANCE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificate_issuance_configs: _containers.RepeatedCompositeFieldContainer[CertificateIssuanceConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, certificate_issuance_configs: _Optional[_Iterable[_Union[CertificateIssuanceConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCertificateIssuanceConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCertificateIssuanceConfigRequest(_message.Message):
    __slots__ = ('parent', 'certificate_issuance_config_id', 'certificate_issuance_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_ISSUANCE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_ISSUANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_issuance_config_id: str
    certificate_issuance_config: CertificateIssuanceConfig

    def __init__(self, parent: _Optional[str]=..., certificate_issuance_config_id: _Optional[str]=..., certificate_issuance_config: _Optional[_Union[CertificateIssuanceConfig, _Mapping]]=...) -> None:
        ...

class DeleteCertificateIssuanceConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CertificateIssuanceConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'certificate_authority_config', 'lifetime', 'rotation_window_percentage', 'key_algorithm')

    class KeyAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_ALGORITHM_UNSPECIFIED: _ClassVar[CertificateIssuanceConfig.KeyAlgorithm]
        RSA_2048: _ClassVar[CertificateIssuanceConfig.KeyAlgorithm]
        ECDSA_P256: _ClassVar[CertificateIssuanceConfig.KeyAlgorithm]
    KEY_ALGORITHM_UNSPECIFIED: CertificateIssuanceConfig.KeyAlgorithm
    RSA_2048: CertificateIssuanceConfig.KeyAlgorithm
    ECDSA_P256: CertificateIssuanceConfig.KeyAlgorithm

    class CertificateAuthorityConfig(_message.Message):
        __slots__ = ('certificate_authority_service_config',)

        class CertificateAuthorityServiceConfig(_message.Message):
            __slots__ = ('ca_pool',)
            CA_POOL_FIELD_NUMBER: _ClassVar[int]
            ca_pool: str

            def __init__(self, ca_pool: _Optional[str]=...) -> None:
                ...
        CERTIFICATE_AUTHORITY_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        certificate_authority_service_config: CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig

        def __init__(self, certificate_authority_service_config: _Optional[_Union[CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig, _Mapping]]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_AUTHORITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    ROTATION_WINDOW_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    certificate_authority_config: CertificateIssuanceConfig.CertificateAuthorityConfig
    lifetime: _duration_pb2.Duration
    rotation_window_percentage: int
    key_algorithm: CertificateIssuanceConfig.KeyAlgorithm

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., certificate_authority_config: _Optional[_Union[CertificateIssuanceConfig.CertificateAuthorityConfig, _Mapping]]=..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., rotation_window_percentage: _Optional[int]=..., key_algorithm: _Optional[_Union[CertificateIssuanceConfig.KeyAlgorithm, str]]=...) -> None:
        ...