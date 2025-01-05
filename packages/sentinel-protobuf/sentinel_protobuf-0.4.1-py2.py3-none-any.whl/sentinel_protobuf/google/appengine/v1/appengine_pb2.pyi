from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.appengine.v1 import application_pb2 as _application_pb2
from google.appengine.v1 import certificate_pb2 as _certificate_pb2
from google.appengine.v1 import domain_pb2 as _domain_pb2
from google.appengine.v1 import domain_mapping_pb2 as _domain_mapping_pb2
from google.appengine.v1 import firewall_pb2 as _firewall_pb2
from google.appengine.v1 import instance_pb2 as _instance_pb2
from google.appengine.v1 import service_pb2 as _service_pb2
from google.appengine.v1 import version_pb2 as _version_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VersionView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASIC: _ClassVar[VersionView]
    FULL: _ClassVar[VersionView]

class AuthorizedCertificateView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASIC_CERTIFICATE: _ClassVar[AuthorizedCertificateView]
    FULL_CERTIFICATE: _ClassVar[AuthorizedCertificateView]

class DomainOverrideStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY: _ClassVar[DomainOverrideStrategy]
    STRICT: _ClassVar[DomainOverrideStrategy]
    OVERRIDE: _ClassVar[DomainOverrideStrategy]
BASIC: VersionView
FULL: VersionView
BASIC_CERTIFICATE: AuthorizedCertificateView
FULL_CERTIFICATE: AuthorizedCertificateView
UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY: DomainOverrideStrategy
STRICT: DomainOverrideStrategy
OVERRIDE: DomainOverrideStrategy

class GetApplicationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ('application',)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application

    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]]=...) -> None:
        ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ('name', 'application', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    application: _application_pb2.Application
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., application: _Optional[_Union[_application_pb2.Application, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RepairApplicationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServicesResponse(_message.Message):
    __slots__ = ('services', 'next_page_token')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    next_page_token: str

    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ('name', 'service', 'update_mask', 'migrate_traffic')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    name: str
    service: _service_pb2.Service
    update_mask: _field_mask_pb2.FieldMask
    migrate_traffic: bool

    def __init__(self, name: _Optional[str]=..., service: _Optional[_Union[_service_pb2.Service, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., migrate_traffic: bool=...) -> None:
        ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: VersionView
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[VersionView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVersionsResponse(_message.Message):
    __slots__ = ('versions', 'next_page_token')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[_version_pb2.Version]
    next_page_token: str

    def __init__(self, versions: _Optional[_Iterable[_Union[_version_pb2.Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVersionRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: VersionView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[VersionView, str]]=...) -> None:
        ...

class CreateVersionRequest(_message.Message):
    __slots__ = ('parent', 'version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    version: _version_pb2.Version

    def __init__(self, parent: _Optional[str]=..., version: _Optional[_Union[_version_pb2.Version, _Mapping]]=...) -> None:
        ...

class UpdateVersionRequest(_message.Message):
    __slots__ = ('name', 'version', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: _version_pb2.Version
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., version: _Optional[_Union[_version_pb2.Version, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[_instance_pb2.Instance]
    next_page_token: str

    def __init__(self, instances: _Optional[_Iterable[_Union[_instance_pb2.Instance, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DebugInstanceRequest(_message.Message):
    __slots__ = ('name', 'ssh_key')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    ssh_key: str

    def __init__(self, name: _Optional[str]=..., ssh_key: _Optional[str]=...) -> None:
        ...

class ListIngressRulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'matching_address')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MATCHING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    matching_address: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., matching_address: _Optional[str]=...) -> None:
        ...

class ListIngressRulesResponse(_message.Message):
    __slots__ = ('ingress_rules', 'next_page_token')
    INGRESS_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ingress_rules: _containers.RepeatedCompositeFieldContainer[_firewall_pb2.FirewallRule]
    next_page_token: str

    def __init__(self, ingress_rules: _Optional[_Iterable[_Union[_firewall_pb2.FirewallRule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchUpdateIngressRulesRequest(_message.Message):
    __slots__ = ('name', 'ingress_rules')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INGRESS_RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    ingress_rules: _containers.RepeatedCompositeFieldContainer[_firewall_pb2.FirewallRule]

    def __init__(self, name: _Optional[str]=..., ingress_rules: _Optional[_Iterable[_Union[_firewall_pb2.FirewallRule, _Mapping]]]=...) -> None:
        ...

class BatchUpdateIngressRulesResponse(_message.Message):
    __slots__ = ('ingress_rules',)
    INGRESS_RULES_FIELD_NUMBER: _ClassVar[int]
    ingress_rules: _containers.RepeatedCompositeFieldContainer[_firewall_pb2.FirewallRule]

    def __init__(self, ingress_rules: _Optional[_Iterable[_Union[_firewall_pb2.FirewallRule, _Mapping]]]=...) -> None:
        ...

class CreateIngressRuleRequest(_message.Message):
    __slots__ = ('parent', 'rule')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rule: _firewall_pb2.FirewallRule

    def __init__(self, parent: _Optional[str]=..., rule: _Optional[_Union[_firewall_pb2.FirewallRule, _Mapping]]=...) -> None:
        ...

class GetIngressRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateIngressRuleRequest(_message.Message):
    __slots__ = ('name', 'rule', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    rule: _firewall_pb2.FirewallRule
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., rule: _Optional[_Union[_firewall_pb2.FirewallRule, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteIngressRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAuthorizedDomainsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAuthorizedDomainsResponse(_message.Message):
    __slots__ = ('domains', 'next_page_token')
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    domains: _containers.RepeatedCompositeFieldContainer[_domain_pb2.AuthorizedDomain]
    next_page_token: str

    def __init__(self, domains: _Optional[_Iterable[_Union[_domain_pb2.AuthorizedDomain, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListAuthorizedCertificatesRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: AuthorizedCertificateView
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[AuthorizedCertificateView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAuthorizedCertificatesResponse(_message.Message):
    __slots__ = ('certificates', 'next_page_token')
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    certificates: _containers.RepeatedCompositeFieldContainer[_certificate_pb2.AuthorizedCertificate]
    next_page_token: str

    def __init__(self, certificates: _Optional[_Iterable[_Union[_certificate_pb2.AuthorizedCertificate, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetAuthorizedCertificateRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: AuthorizedCertificateView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[AuthorizedCertificateView, str]]=...) -> None:
        ...

class CreateAuthorizedCertificateRequest(_message.Message):
    __slots__ = ('parent', 'certificate')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate: _certificate_pb2.AuthorizedCertificate

    def __init__(self, parent: _Optional[str]=..., certificate: _Optional[_Union[_certificate_pb2.AuthorizedCertificate, _Mapping]]=...) -> None:
        ...

class UpdateAuthorizedCertificateRequest(_message.Message):
    __slots__ = ('name', 'certificate', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    certificate: _certificate_pb2.AuthorizedCertificate
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., certificate: _Optional[_Union[_certificate_pb2.AuthorizedCertificate, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAuthorizedCertificateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDomainMappingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDomainMappingsResponse(_message.Message):
    __slots__ = ('domain_mappings', 'next_page_token')
    DOMAIN_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    domain_mappings: _containers.RepeatedCompositeFieldContainer[_domain_mapping_pb2.DomainMapping]
    next_page_token: str

    def __init__(self, domain_mappings: _Optional[_Iterable[_Union[_domain_mapping_pb2.DomainMapping, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDomainMappingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDomainMappingRequest(_message.Message):
    __slots__ = ('parent', 'domain_mapping', 'override_strategy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MAPPING_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    domain_mapping: _domain_mapping_pb2.DomainMapping
    override_strategy: DomainOverrideStrategy

    def __init__(self, parent: _Optional[str]=..., domain_mapping: _Optional[_Union[_domain_mapping_pb2.DomainMapping, _Mapping]]=..., override_strategy: _Optional[_Union[DomainOverrideStrategy, str]]=...) -> None:
        ...

class UpdateDomainMappingRequest(_message.Message):
    __slots__ = ('name', 'domain_mapping', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MAPPING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain_mapping: _domain_mapping_pb2.DomainMapping
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., domain_mapping: _Optional[_Union[_domain_mapping_pb2.DomainMapping, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDomainMappingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...