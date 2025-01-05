from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.certificatemanager.v1 import certificate_issuance_config_pb2 as _certificate_issuance_config_pb2
from google.cloud.certificatemanager.v1 import trust_config_pb2 as _trust_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVING_STATE_UNSPECIFIED: _ClassVar[ServingState]
    ACTIVE: _ClassVar[ServingState]
    PENDING: _ClassVar[ServingState]
SERVING_STATE_UNSPECIFIED: ServingState
ACTIVE: ServingState
PENDING: ServingState

class ListCertificatesRequest(_message.Message):
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

class ListCertificatesResponse(_message.Message):
    __slots__ = ('certificates', 'next_page_token', 'unreachable')
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificates: _containers.RepeatedCompositeFieldContainer[Certificate]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, certificates: _Optional[_Iterable[_Union[Certificate, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCertificateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCertificateRequest(_message.Message):
    __slots__ = ('parent', 'certificate_id', 'certificate')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_id: str
    certificate: Certificate

    def __init__(self, parent: _Optional[str]=..., certificate_id: _Optional[str]=..., certificate: _Optional[_Union[Certificate, _Mapping]]=...) -> None:
        ...

class UpdateCertificateRequest(_message.Message):
    __slots__ = ('certificate', 'update_mask')
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    certificate: Certificate
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, certificate: _Optional[_Union[Certificate, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCertificateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCertificateMapsRequest(_message.Message):
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

class ListCertificateMapsResponse(_message.Message):
    __slots__ = ('certificate_maps', 'next_page_token', 'unreachable')
    CERTIFICATE_MAPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificate_maps: _containers.RepeatedCompositeFieldContainer[CertificateMap]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, certificate_maps: _Optional[_Iterable[_Union[CertificateMap, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCertificateMapRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCertificateMapRequest(_message.Message):
    __slots__ = ('parent', 'certificate_map_id', 'certificate_map')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_MAP_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_MAP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_map_id: str
    certificate_map: CertificateMap

    def __init__(self, parent: _Optional[str]=..., certificate_map_id: _Optional[str]=..., certificate_map: _Optional[_Union[CertificateMap, _Mapping]]=...) -> None:
        ...

class UpdateCertificateMapRequest(_message.Message):
    __slots__ = ('certificate_map', 'update_mask')
    CERTIFICATE_MAP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    certificate_map: CertificateMap
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, certificate_map: _Optional[_Union[CertificateMap, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCertificateMapRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCertificateMapEntriesRequest(_message.Message):
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

class ListCertificateMapEntriesResponse(_message.Message):
    __slots__ = ('certificate_map_entries', 'next_page_token', 'unreachable')
    CERTIFICATE_MAP_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    certificate_map_entries: _containers.RepeatedCompositeFieldContainer[CertificateMapEntry]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, certificate_map_entries: _Optional[_Iterable[_Union[CertificateMapEntry, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCertificateMapEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCertificateMapEntryRequest(_message.Message):
    __slots__ = ('parent', 'certificate_map_entry_id', 'certificate_map_entry')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_MAP_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_MAP_ENTRY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    certificate_map_entry_id: str
    certificate_map_entry: CertificateMapEntry

    def __init__(self, parent: _Optional[str]=..., certificate_map_entry_id: _Optional[str]=..., certificate_map_entry: _Optional[_Union[CertificateMapEntry, _Mapping]]=...) -> None:
        ...

class UpdateCertificateMapEntryRequest(_message.Message):
    __slots__ = ('certificate_map_entry', 'update_mask')
    CERTIFICATE_MAP_ENTRY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    certificate_map_entry: CertificateMapEntry
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, certificate_map_entry: _Optional[_Union[CertificateMapEntry, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCertificateMapEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDnsAuthorizationsRequest(_message.Message):
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

class ListDnsAuthorizationsResponse(_message.Message):
    __slots__ = ('dns_authorizations', 'next_page_token', 'unreachable')
    DNS_AUTHORIZATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    dns_authorizations: _containers.RepeatedCompositeFieldContainer[DnsAuthorization]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, dns_authorizations: _Optional[_Iterable[_Union[DnsAuthorization, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDnsAuthorizationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDnsAuthorizationRequest(_message.Message):
    __slots__ = ('parent', 'dns_authorization_id', 'dns_authorization')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DNS_AUTHORIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DNS_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dns_authorization_id: str
    dns_authorization: DnsAuthorization

    def __init__(self, parent: _Optional[str]=..., dns_authorization_id: _Optional[str]=..., dns_authorization: _Optional[_Union[DnsAuthorization, _Mapping]]=...) -> None:
        ...

class UpdateDnsAuthorizationRequest(_message.Message):
    __slots__ = ('dns_authorization', 'update_mask')
    DNS_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dns_authorization: DnsAuthorization
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dns_authorization: _Optional[_Union[DnsAuthorization, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDnsAuthorizationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
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

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class Certificate(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'self_managed', 'managed', 'san_dnsnames', 'pem_certificate', 'expire_time', 'scope')

    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[Certificate.Scope]
        EDGE_CACHE: _ClassVar[Certificate.Scope]
        ALL_REGIONS: _ClassVar[Certificate.Scope]
    DEFAULT: Certificate.Scope
    EDGE_CACHE: Certificate.Scope
    ALL_REGIONS: Certificate.Scope

    class SelfManagedCertificate(_message.Message):
        __slots__ = ('pem_certificate', 'pem_private_key')
        PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        PEM_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        pem_certificate: str
        pem_private_key: str

        def __init__(self, pem_certificate: _Optional[str]=..., pem_private_key: _Optional[str]=...) -> None:
            ...

    class ManagedCertificate(_message.Message):
        __slots__ = ('domains', 'dns_authorizations', 'issuance_config', 'state', 'provisioning_issue', 'authorization_attempt_info')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Certificate.ManagedCertificate.State]
            PROVISIONING: _ClassVar[Certificate.ManagedCertificate.State]
            FAILED: _ClassVar[Certificate.ManagedCertificate.State]
            ACTIVE: _ClassVar[Certificate.ManagedCertificate.State]
        STATE_UNSPECIFIED: Certificate.ManagedCertificate.State
        PROVISIONING: Certificate.ManagedCertificate.State
        FAILED: Certificate.ManagedCertificate.State
        ACTIVE: Certificate.ManagedCertificate.State

        class ProvisioningIssue(_message.Message):
            __slots__ = ('reason', 'details')

            class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                REASON_UNSPECIFIED: _ClassVar[Certificate.ManagedCertificate.ProvisioningIssue.Reason]
                AUTHORIZATION_ISSUE: _ClassVar[Certificate.ManagedCertificate.ProvisioningIssue.Reason]
                RATE_LIMITED: _ClassVar[Certificate.ManagedCertificate.ProvisioningIssue.Reason]
            REASON_UNSPECIFIED: Certificate.ManagedCertificate.ProvisioningIssue.Reason
            AUTHORIZATION_ISSUE: Certificate.ManagedCertificate.ProvisioningIssue.Reason
            RATE_LIMITED: Certificate.ManagedCertificate.ProvisioningIssue.Reason
            REASON_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            reason: Certificate.ManagedCertificate.ProvisioningIssue.Reason
            details: str

            def __init__(self, reason: _Optional[_Union[Certificate.ManagedCertificate.ProvisioningIssue.Reason, str]]=..., details: _Optional[str]=...) -> None:
                ...

        class AuthorizationAttemptInfo(_message.Message):
            __slots__ = ('domain', 'state', 'failure_reason', 'details')

            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.State]
                AUTHORIZING: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.State]
                AUTHORIZED: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.State]
                FAILED: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.State]
            STATE_UNSPECIFIED: Certificate.ManagedCertificate.AuthorizationAttemptInfo.State
            AUTHORIZING: Certificate.ManagedCertificate.AuthorizationAttemptInfo.State
            AUTHORIZED: Certificate.ManagedCertificate.AuthorizationAttemptInfo.State
            FAILED: Certificate.ManagedCertificate.AuthorizationAttemptInfo.State

            class FailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FAILURE_REASON_UNSPECIFIED: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason]
                CONFIG: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason]
                CAA: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason]
                RATE_LIMITED: _ClassVar[Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason]
            FAILURE_REASON_UNSPECIFIED: Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason
            CONFIG: Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason
            CAA: Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason
            RATE_LIMITED: Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason
            DOMAIN_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            domain: str
            state: Certificate.ManagedCertificate.AuthorizationAttemptInfo.State
            failure_reason: Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason
            details: str

            def __init__(self, domain: _Optional[str]=..., state: _Optional[_Union[Certificate.ManagedCertificate.AuthorizationAttemptInfo.State, str]]=..., failure_reason: _Optional[_Union[Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason, str]]=..., details: _Optional[str]=...) -> None:
                ...
        DOMAINS_FIELD_NUMBER: _ClassVar[int]
        DNS_AUTHORIZATIONS_FIELD_NUMBER: _ClassVar[int]
        ISSUANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        PROVISIONING_ISSUE_FIELD_NUMBER: _ClassVar[int]
        AUTHORIZATION_ATTEMPT_INFO_FIELD_NUMBER: _ClassVar[int]
        domains: _containers.RepeatedScalarFieldContainer[str]
        dns_authorizations: _containers.RepeatedScalarFieldContainer[str]
        issuance_config: str
        state: Certificate.ManagedCertificate.State
        provisioning_issue: Certificate.ManagedCertificate.ProvisioningIssue
        authorization_attempt_info: _containers.RepeatedCompositeFieldContainer[Certificate.ManagedCertificate.AuthorizationAttemptInfo]

        def __init__(self, domains: _Optional[_Iterable[str]]=..., dns_authorizations: _Optional[_Iterable[str]]=..., issuance_config: _Optional[str]=..., state: _Optional[_Union[Certificate.ManagedCertificate.State, str]]=..., provisioning_issue: _Optional[_Union[Certificate.ManagedCertificate.ProvisioningIssue, _Mapping]]=..., authorization_attempt_info: _Optional[_Iterable[_Union[Certificate.ManagedCertificate.AuthorizationAttemptInfo, _Mapping]]]=...) -> None:
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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SELF_MANAGED_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FIELD_NUMBER: _ClassVar[int]
    SAN_DNSNAMES_FIELD_NUMBER: _ClassVar[int]
    PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    self_managed: Certificate.SelfManagedCertificate
    managed: Certificate.ManagedCertificate
    san_dnsnames: _containers.RepeatedScalarFieldContainer[str]
    pem_certificate: str
    expire_time: _timestamp_pb2.Timestamp
    scope: Certificate.Scope

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., self_managed: _Optional[_Union[Certificate.SelfManagedCertificate, _Mapping]]=..., managed: _Optional[_Union[Certificate.ManagedCertificate, _Mapping]]=..., san_dnsnames: _Optional[_Iterable[str]]=..., pem_certificate: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., scope: _Optional[_Union[Certificate.Scope, str]]=...) -> None:
        ...

class CertificateMap(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'gclb_targets')

    class GclbTarget(_message.Message):
        __slots__ = ('target_https_proxy', 'target_ssl_proxy', 'ip_configs')

        class IpConfig(_message.Message):
            __slots__ = ('ip_address', 'ports')
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PORTS_FIELD_NUMBER: _ClassVar[int]
            ip_address: str
            ports: _containers.RepeatedScalarFieldContainer[int]

            def __init__(self, ip_address: _Optional[str]=..., ports: _Optional[_Iterable[int]]=...) -> None:
                ...
        TARGET_HTTPS_PROXY_FIELD_NUMBER: _ClassVar[int]
        TARGET_SSL_PROXY_FIELD_NUMBER: _ClassVar[int]
        IP_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        target_https_proxy: str
        target_ssl_proxy: str
        ip_configs: _containers.RepeatedCompositeFieldContainer[CertificateMap.GclbTarget.IpConfig]

        def __init__(self, target_https_proxy: _Optional[str]=..., target_ssl_proxy: _Optional[str]=..., ip_configs: _Optional[_Iterable[_Union[CertificateMap.GclbTarget.IpConfig, _Mapping]]]=...) -> None:
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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    GCLB_TARGETS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    gclb_targets: _containers.RepeatedCompositeFieldContainer[CertificateMap.GclbTarget]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., gclb_targets: _Optional[_Iterable[_Union[CertificateMap.GclbTarget, _Mapping]]]=...) -> None:
        ...

class CertificateMapEntry(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'hostname', 'matcher', 'certificates', 'state')

    class Matcher(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCHER_UNSPECIFIED: _ClassVar[CertificateMapEntry.Matcher]
        PRIMARY: _ClassVar[CertificateMapEntry.Matcher]
    MATCHER_UNSPECIFIED: CertificateMapEntry.Matcher
    PRIMARY: CertificateMapEntry.Matcher

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    MATCHER_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    hostname: str
    matcher: CertificateMapEntry.Matcher
    certificates: _containers.RepeatedScalarFieldContainer[str]
    state: ServingState

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., hostname: _Optional[str]=..., matcher: _Optional[_Union[CertificateMapEntry.Matcher, str]]=..., certificates: _Optional[_Iterable[str]]=..., state: _Optional[_Union[ServingState, str]]=...) -> None:
        ...

class DnsAuthorization(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'domain', 'dns_resource_record', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[DnsAuthorization.Type]
        FIXED_RECORD: _ClassVar[DnsAuthorization.Type]
        PER_PROJECT_RECORD: _ClassVar[DnsAuthorization.Type]
    TYPE_UNSPECIFIED: DnsAuthorization.Type
    FIXED_RECORD: DnsAuthorization.Type
    PER_PROJECT_RECORD: DnsAuthorization.Type

    class DnsResourceRecord(_message.Message):
        __slots__ = ('name', 'type', 'data')
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str
        data: str

        def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., data: _Optional[str]=...) -> None:
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
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DNS_RESOURCE_RECORD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    domain: str
    dns_resource_record: DnsAuthorization.DnsResourceRecord
    type: DnsAuthorization.Type

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., domain: _Optional[str]=..., dns_resource_record: _Optional[_Union[DnsAuthorization.DnsResourceRecord, _Mapping]]=..., type: _Optional[_Union[DnsAuthorization.Type, str]]=...) -> None:
        ...