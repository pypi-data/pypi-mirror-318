from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.security.privateca.v1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCertificateRequest(_message.Message):
    __slots__ = ("parent", "certificate_id", "certificate", "request_id", "validate_only", "issuing_certificate_authority_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ISSUING_CERTIFICATE_AUTHORITY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_id: str
    certificate: _resources_pb2.Certificate
    request_id: str
    validate_only: bool
    issuing_certificate_authority_id: str
    def __init__(self, parent: _Optional[str] = ..., certificate_id: _Optional[str] = ..., certificate: _Optional[_Union[_resources_pb2.Certificate, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., issuing_certificate_authority_id: _Optional[str] = ...) -> None: ...

class GetCertificateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCertificatesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListCertificatesResponse(_message.Message):
    __slots__ = ("certificates", "next_page_token", "unreachable")
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificates: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Certificate]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, certificates: _Optional[_Iterable[_Union[_resources_pb2.Certificate, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class RevokeCertificateRequest(_message.Message):
    __slots__ = ("name", "reason", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: _resources_pb2.RevocationReason
    request_id: str
    def __init__(self, name: _Optional[str] = ..., reason: _Optional[_Union[_resources_pb2.RevocationReason, str]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateCertificateRequest(_message.Message):
    __slots__ = ("certificate", "update_mask", "request_id")
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    certificate: _resources_pb2.Certificate
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, certificate: _Optional[_Union[_resources_pb2.Certificate, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ActivateCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name", "pem_ca_certificate", "subordinate_config", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEM_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    SUBORDINATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    pem_ca_certificate: str
    subordinate_config: _resources_pb2.SubordinateConfig
    request_id: str
    def __init__(self, name: _Optional[str] = ..., pem_ca_certificate: _Optional[str] = ..., subordinate_config: _Optional[_Union[_resources_pb2.SubordinateConfig, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateCertificateAuthorityRequest(_message.Message):
    __slots__ = ("parent", "certificate_authority_id", "certificate_authority", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_AUTHORITY_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_authority_id: str
    certificate_authority: _resources_pb2.CertificateAuthority
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., certificate_authority_id: _Optional[str] = ..., certificate_authority: _Optional[_Union[_resources_pb2.CertificateAuthority, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DisableCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name", "request_id", "ignore_dependent_resources")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DEPENDENT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    ignore_dependent_resources: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., ignore_dependent_resources: bool = ...) -> None: ...

class EnableCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class FetchCertificateAuthorityCsrRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class FetchCertificateAuthorityCsrResponse(_message.Message):
    __slots__ = ("pem_csr",)
    PEM_CSR_FIELD_NUMBER: _ClassVar[int]
    pem_csr: str
    def __init__(self, pem_csr: _Optional[str] = ...) -> None: ...

class GetCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCertificateAuthoritiesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListCertificateAuthoritiesResponse(_message.Message):
    __slots__ = ("certificate_authorities", "next_page_token", "unreachable")
    CERTIFICATE_AUTHORITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificate_authorities: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CertificateAuthority]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, certificate_authorities: _Optional[_Iterable[_Union[_resources_pb2.CertificateAuthority, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UndeleteCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name", "request_id", "ignore_active_certificates", "skip_grace_period", "ignore_dependent_resources")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ACTIVE_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    SKIP_GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DEPENDENT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    ignore_active_certificates: bool
    skip_grace_period: bool
    ignore_dependent_resources: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., ignore_active_certificates: bool = ..., skip_grace_period: bool = ..., ignore_dependent_resources: bool = ...) -> None: ...

class UpdateCertificateAuthorityRequest(_message.Message):
    __slots__ = ("certificate_authority", "update_mask", "request_id")
    CERTIFICATE_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_authority: _resources_pb2.CertificateAuthority
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, certificate_authority: _Optional[_Union[_resources_pb2.CertificateAuthority, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateCaPoolRequest(_message.Message):
    __slots__ = ("parent", "ca_pool_id", "ca_pool", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CA_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    CA_POOL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ca_pool_id: str
    ca_pool: _resources_pb2.CaPool
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., ca_pool_id: _Optional[str] = ..., ca_pool: _Optional[_Union[_resources_pb2.CaPool, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateCaPoolRequest(_message.Message):
    __slots__ = ("ca_pool", "update_mask", "request_id")
    CA_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ca_pool: _resources_pb2.CaPool
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, ca_pool: _Optional[_Union[_resources_pb2.CaPool, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteCaPoolRequest(_message.Message):
    __slots__ = ("name", "request_id", "ignore_dependent_resources")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DEPENDENT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    ignore_dependent_resources: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., ignore_dependent_resources: bool = ...) -> None: ...

class FetchCaCertsRequest(_message.Message):
    __slots__ = ("ca_pool", "request_id")
    CA_POOL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ca_pool: str
    request_id: str
    def __init__(self, ca_pool: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class FetchCaCertsResponse(_message.Message):
    __slots__ = ("ca_certs",)
    class CertChain(_message.Message):
        __slots__ = ("certificates",)
        CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        certificates: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, certificates: _Optional[_Iterable[str]] = ...) -> None: ...
    CA_CERTS_FIELD_NUMBER: _ClassVar[int]
    ca_certs: _containers.RepeatedCompositeFieldContainer[FetchCaCertsResponse.CertChain]
    def __init__(self, ca_certs: _Optional[_Iterable[_Union[FetchCaCertsResponse.CertChain, _Mapping]]] = ...) -> None: ...

class GetCaPoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCaPoolsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListCaPoolsResponse(_message.Message):
    __slots__ = ("ca_pools", "next_page_token", "unreachable")
    CA_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    ca_pools: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CaPool]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ca_pools: _Optional[_Iterable[_Union[_resources_pb2.CaPool, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCertificateRevocationListRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCertificateRevocationListsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListCertificateRevocationListsResponse(_message.Message):
    __slots__ = ("certificate_revocation_lists", "next_page_token", "unreachable")
    CERTIFICATE_REVOCATION_LISTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificate_revocation_lists: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CertificateRevocationList]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, certificate_revocation_lists: _Optional[_Iterable[_Union[_resources_pb2.CertificateRevocationList, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateCertificateRevocationListRequest(_message.Message):
    __slots__ = ("certificate_revocation_list", "update_mask", "request_id")
    CERTIFICATE_REVOCATION_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_revocation_list: _resources_pb2.CertificateRevocationList
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, certificate_revocation_list: _Optional[_Union[_resources_pb2.CertificateRevocationList, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateCertificateTemplateRequest(_message.Message):
    __slots__ = ("parent", "certificate_template_id", "certificate_template", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_template_id: str
    certificate_template: _resources_pb2.CertificateTemplate
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., certificate_template_id: _Optional[str] = ..., certificate_template: _Optional[_Union[_resources_pb2.CertificateTemplate, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteCertificateTemplateRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetCertificateTemplateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCertificateTemplatesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListCertificateTemplatesResponse(_message.Message):
    __slots__ = ("certificate_templates", "next_page_token", "unreachable")
    CERTIFICATE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificate_templates: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CertificateTemplate]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, certificate_templates: _Optional[_Iterable[_Union[_resources_pb2.CertificateTemplate, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateCertificateTemplateRequest(_message.Message):
    __slots__ = ("certificate_template", "update_mask", "request_id")
    CERTIFICATE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_template: _resources_pb2.CertificateTemplate
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, certificate_template: _Optional[_Union[_resources_pb2.CertificateTemplate, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...
