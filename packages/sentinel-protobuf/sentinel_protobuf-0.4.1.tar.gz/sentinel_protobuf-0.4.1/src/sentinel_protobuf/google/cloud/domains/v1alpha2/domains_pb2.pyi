from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContactPrivacy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTACT_PRIVACY_UNSPECIFIED: _ClassVar[ContactPrivacy]
    PUBLIC_CONTACT_DATA: _ClassVar[ContactPrivacy]
    PRIVATE_CONTACT_DATA: _ClassVar[ContactPrivacy]
    REDACTED_CONTACT_DATA: _ClassVar[ContactPrivacy]

class DomainNotice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOMAIN_NOTICE_UNSPECIFIED: _ClassVar[DomainNotice]
    HSTS_PRELOADED: _ClassVar[DomainNotice]

class ContactNotice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTACT_NOTICE_UNSPECIFIED: _ClassVar[ContactNotice]
    PUBLIC_CONTACT_DATA_ACKNOWLEDGEMENT: _ClassVar[ContactNotice]

class TransferLockState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_LOCK_STATE_UNSPECIFIED: _ClassVar[TransferLockState]
    UNLOCKED: _ClassVar[TransferLockState]
    LOCKED: _ClassVar[TransferLockState]
CONTACT_PRIVACY_UNSPECIFIED: ContactPrivacy
PUBLIC_CONTACT_DATA: ContactPrivacy
PRIVATE_CONTACT_DATA: ContactPrivacy
REDACTED_CONTACT_DATA: ContactPrivacy
DOMAIN_NOTICE_UNSPECIFIED: DomainNotice
HSTS_PRELOADED: DomainNotice
CONTACT_NOTICE_UNSPECIFIED: ContactNotice
PUBLIC_CONTACT_DATA_ACKNOWLEDGEMENT: ContactNotice
TRANSFER_LOCK_STATE_UNSPECIFIED: TransferLockState
UNLOCKED: TransferLockState
LOCKED: TransferLockState

class Registration(_message.Message):
    __slots__ = ('name', 'domain_name', 'create_time', 'expire_time', 'state', 'issues', 'labels', 'management_settings', 'dns_settings', 'contact_settings', 'pending_contact_settings', 'supported_privacy')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Registration.State]
        REGISTRATION_PENDING: _ClassVar[Registration.State]
        REGISTRATION_FAILED: _ClassVar[Registration.State]
        TRANSFER_PENDING: _ClassVar[Registration.State]
        TRANSFER_FAILED: _ClassVar[Registration.State]
        ACTIVE: _ClassVar[Registration.State]
        SUSPENDED: _ClassVar[Registration.State]
        EXPORTED: _ClassVar[Registration.State]
    STATE_UNSPECIFIED: Registration.State
    REGISTRATION_PENDING: Registration.State
    REGISTRATION_FAILED: Registration.State
    TRANSFER_PENDING: Registration.State
    TRANSFER_FAILED: Registration.State
    ACTIVE: Registration.State
    SUSPENDED: Registration.State
    EXPORTED: Registration.State

    class Issue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISSUE_UNSPECIFIED: _ClassVar[Registration.Issue]
        CONTACT_SUPPORT: _ClassVar[Registration.Issue]
        UNVERIFIED_EMAIL: _ClassVar[Registration.Issue]
    ISSUE_UNSPECIFIED: Registration.Issue
    CONTACT_SUPPORT: Registration.Issue
    UNVERIFIED_EMAIL: Registration.Issue

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DNS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PENDING_CONTACT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain_name: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    state: Registration.State
    issues: _containers.RepeatedScalarFieldContainer[Registration.Issue]
    labels: _containers.ScalarMap[str, str]
    management_settings: ManagementSettings
    dns_settings: DnsSettings
    contact_settings: ContactSettings
    pending_contact_settings: ContactSettings
    supported_privacy: _containers.RepeatedScalarFieldContainer[ContactPrivacy]

    def __init__(self, name: _Optional[str]=..., domain_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Registration.State, str]]=..., issues: _Optional[_Iterable[_Union[Registration.Issue, str]]]=..., labels: _Optional[_Mapping[str, str]]=..., management_settings: _Optional[_Union[ManagementSettings, _Mapping]]=..., dns_settings: _Optional[_Union[DnsSettings, _Mapping]]=..., contact_settings: _Optional[_Union[ContactSettings, _Mapping]]=..., pending_contact_settings: _Optional[_Union[ContactSettings, _Mapping]]=..., supported_privacy: _Optional[_Iterable[_Union[ContactPrivacy, str]]]=...) -> None:
        ...

class ManagementSettings(_message.Message):
    __slots__ = ('renewal_method', 'transfer_lock_state')

    class RenewalMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RENEWAL_METHOD_UNSPECIFIED: _ClassVar[ManagementSettings.RenewalMethod]
        AUTOMATIC_RENEWAL: _ClassVar[ManagementSettings.RenewalMethod]
        MANUAL_RENEWAL: _ClassVar[ManagementSettings.RenewalMethod]
    RENEWAL_METHOD_UNSPECIFIED: ManagementSettings.RenewalMethod
    AUTOMATIC_RENEWAL: ManagementSettings.RenewalMethod
    MANUAL_RENEWAL: ManagementSettings.RenewalMethod
    RENEWAL_METHOD_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_LOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    renewal_method: ManagementSettings.RenewalMethod
    transfer_lock_state: TransferLockState

    def __init__(self, renewal_method: _Optional[_Union[ManagementSettings.RenewalMethod, str]]=..., transfer_lock_state: _Optional[_Union[TransferLockState, str]]=...) -> None:
        ...

class DnsSettings(_message.Message):
    __slots__ = ('custom_dns', 'google_domains_dns', 'glue_records')

    class DsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DS_STATE_UNSPECIFIED: _ClassVar[DnsSettings.DsState]
        DS_RECORDS_UNPUBLISHED: _ClassVar[DnsSettings.DsState]
        DS_RECORDS_PUBLISHED: _ClassVar[DnsSettings.DsState]
    DS_STATE_UNSPECIFIED: DnsSettings.DsState
    DS_RECORDS_UNPUBLISHED: DnsSettings.DsState
    DS_RECORDS_PUBLISHED: DnsSettings.DsState

    class CustomDns(_message.Message):
        __slots__ = ('name_servers', 'ds_records')
        NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
        DS_RECORDS_FIELD_NUMBER: _ClassVar[int]
        name_servers: _containers.RepeatedScalarFieldContainer[str]
        ds_records: _containers.RepeatedCompositeFieldContainer[DnsSettings.DsRecord]

        def __init__(self, name_servers: _Optional[_Iterable[str]]=..., ds_records: _Optional[_Iterable[_Union[DnsSettings.DsRecord, _Mapping]]]=...) -> None:
            ...

    class GoogleDomainsDns(_message.Message):
        __slots__ = ('name_servers', 'ds_state', 'ds_records')
        NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
        DS_STATE_FIELD_NUMBER: _ClassVar[int]
        DS_RECORDS_FIELD_NUMBER: _ClassVar[int]
        name_servers: _containers.RepeatedScalarFieldContainer[str]
        ds_state: DnsSettings.DsState
        ds_records: _containers.RepeatedCompositeFieldContainer[DnsSettings.DsRecord]

        def __init__(self, name_servers: _Optional[_Iterable[str]]=..., ds_state: _Optional[_Union[DnsSettings.DsState, str]]=..., ds_records: _Optional[_Iterable[_Union[DnsSettings.DsRecord, _Mapping]]]=...) -> None:
            ...

    class DsRecord(_message.Message):
        __slots__ = ('key_tag', 'algorithm', 'digest_type', 'digest')

        class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ALGORITHM_UNSPECIFIED: _ClassVar[DnsSettings.DsRecord.Algorithm]
            RSAMD5: _ClassVar[DnsSettings.DsRecord.Algorithm]
            DH: _ClassVar[DnsSettings.DsRecord.Algorithm]
            DSA: _ClassVar[DnsSettings.DsRecord.Algorithm]
            ECC: _ClassVar[DnsSettings.DsRecord.Algorithm]
            RSASHA1: _ClassVar[DnsSettings.DsRecord.Algorithm]
            DSANSEC3SHA1: _ClassVar[DnsSettings.DsRecord.Algorithm]
            RSASHA1NSEC3SHA1: _ClassVar[DnsSettings.DsRecord.Algorithm]
            RSASHA256: _ClassVar[DnsSettings.DsRecord.Algorithm]
            RSASHA512: _ClassVar[DnsSettings.DsRecord.Algorithm]
            ECCGOST: _ClassVar[DnsSettings.DsRecord.Algorithm]
            ECDSAP256SHA256: _ClassVar[DnsSettings.DsRecord.Algorithm]
            ECDSAP384SHA384: _ClassVar[DnsSettings.DsRecord.Algorithm]
            ED25519: _ClassVar[DnsSettings.DsRecord.Algorithm]
            ED448: _ClassVar[DnsSettings.DsRecord.Algorithm]
            INDIRECT: _ClassVar[DnsSettings.DsRecord.Algorithm]
            PRIVATEDNS: _ClassVar[DnsSettings.DsRecord.Algorithm]
            PRIVATEOID: _ClassVar[DnsSettings.DsRecord.Algorithm]
        ALGORITHM_UNSPECIFIED: DnsSettings.DsRecord.Algorithm
        RSAMD5: DnsSettings.DsRecord.Algorithm
        DH: DnsSettings.DsRecord.Algorithm
        DSA: DnsSettings.DsRecord.Algorithm
        ECC: DnsSettings.DsRecord.Algorithm
        RSASHA1: DnsSettings.DsRecord.Algorithm
        DSANSEC3SHA1: DnsSettings.DsRecord.Algorithm
        RSASHA1NSEC3SHA1: DnsSettings.DsRecord.Algorithm
        RSASHA256: DnsSettings.DsRecord.Algorithm
        RSASHA512: DnsSettings.DsRecord.Algorithm
        ECCGOST: DnsSettings.DsRecord.Algorithm
        ECDSAP256SHA256: DnsSettings.DsRecord.Algorithm
        ECDSAP384SHA384: DnsSettings.DsRecord.Algorithm
        ED25519: DnsSettings.DsRecord.Algorithm
        ED448: DnsSettings.DsRecord.Algorithm
        INDIRECT: DnsSettings.DsRecord.Algorithm
        PRIVATEDNS: DnsSettings.DsRecord.Algorithm
        PRIVATEOID: DnsSettings.DsRecord.Algorithm

        class DigestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DIGEST_TYPE_UNSPECIFIED: _ClassVar[DnsSettings.DsRecord.DigestType]
            SHA1: _ClassVar[DnsSettings.DsRecord.DigestType]
            SHA256: _ClassVar[DnsSettings.DsRecord.DigestType]
            GOST3411: _ClassVar[DnsSettings.DsRecord.DigestType]
            SHA384: _ClassVar[DnsSettings.DsRecord.DigestType]
        DIGEST_TYPE_UNSPECIFIED: DnsSettings.DsRecord.DigestType
        SHA1: DnsSettings.DsRecord.DigestType
        SHA256: DnsSettings.DsRecord.DigestType
        GOST3411: DnsSettings.DsRecord.DigestType
        SHA384: DnsSettings.DsRecord.DigestType
        KEY_TAG_FIELD_NUMBER: _ClassVar[int]
        ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        DIGEST_TYPE_FIELD_NUMBER: _ClassVar[int]
        DIGEST_FIELD_NUMBER: _ClassVar[int]
        key_tag: int
        algorithm: DnsSettings.DsRecord.Algorithm
        digest_type: DnsSettings.DsRecord.DigestType
        digest: str

        def __init__(self, key_tag: _Optional[int]=..., algorithm: _Optional[_Union[DnsSettings.DsRecord.Algorithm, str]]=..., digest_type: _Optional[_Union[DnsSettings.DsRecord.DigestType, str]]=..., digest: _Optional[str]=...) -> None:
            ...

    class GlueRecord(_message.Message):
        __slots__ = ('host_name', 'ipv4_addresses', 'ipv6_addresses')
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        IPV4_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        IPV6_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        host_name: str
        ipv4_addresses: _containers.RepeatedScalarFieldContainer[str]
        ipv6_addresses: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, host_name: _Optional[str]=..., ipv4_addresses: _Optional[_Iterable[str]]=..., ipv6_addresses: _Optional[_Iterable[str]]=...) -> None:
            ...
    CUSTOM_DNS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DOMAINS_DNS_FIELD_NUMBER: _ClassVar[int]
    GLUE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    custom_dns: DnsSettings.CustomDns
    google_domains_dns: DnsSettings.GoogleDomainsDns
    glue_records: _containers.RepeatedCompositeFieldContainer[DnsSettings.GlueRecord]

    def __init__(self, custom_dns: _Optional[_Union[DnsSettings.CustomDns, _Mapping]]=..., google_domains_dns: _Optional[_Union[DnsSettings.GoogleDomainsDns, _Mapping]]=..., glue_records: _Optional[_Iterable[_Union[DnsSettings.GlueRecord, _Mapping]]]=...) -> None:
        ...

class ContactSettings(_message.Message):
    __slots__ = ('privacy', 'registrant_contact', 'admin_contact', 'technical_contact')

    class Contact(_message.Message):
        __slots__ = ('postal_address', 'email', 'phone_number', 'fax_number')
        POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        FAX_NUMBER_FIELD_NUMBER: _ClassVar[int]
        postal_address: _postal_address_pb2.PostalAddress
        email: str
        phone_number: str
        fax_number: str

        def __init__(self, postal_address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]]=..., email: _Optional[str]=..., phone_number: _Optional[str]=..., fax_number: _Optional[str]=...) -> None:
            ...
    PRIVACY_FIELD_NUMBER: _ClassVar[int]
    REGISTRANT_CONTACT_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CONTACT_FIELD_NUMBER: _ClassVar[int]
    TECHNICAL_CONTACT_FIELD_NUMBER: _ClassVar[int]
    privacy: ContactPrivacy
    registrant_contact: ContactSettings.Contact
    admin_contact: ContactSettings.Contact
    technical_contact: ContactSettings.Contact

    def __init__(self, privacy: _Optional[_Union[ContactPrivacy, str]]=..., registrant_contact: _Optional[_Union[ContactSettings.Contact, _Mapping]]=..., admin_contact: _Optional[_Union[ContactSettings.Contact, _Mapping]]=..., technical_contact: _Optional[_Union[ContactSettings.Contact, _Mapping]]=...) -> None:
        ...

class SearchDomainsRequest(_message.Message):
    __slots__ = ('query', 'location')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    query: str
    location: str

    def __init__(self, query: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class SearchDomainsResponse(_message.Message):
    __slots__ = ('register_parameters',)
    REGISTER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    register_parameters: _containers.RepeatedCompositeFieldContainer[RegisterParameters]

    def __init__(self, register_parameters: _Optional[_Iterable[_Union[RegisterParameters, _Mapping]]]=...) -> None:
        ...

class RetrieveRegisterParametersRequest(_message.Message):
    __slots__ = ('domain_name', 'location')
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    location: str

    def __init__(self, domain_name: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class RetrieveRegisterParametersResponse(_message.Message):
    __slots__ = ('register_parameters',)
    REGISTER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    register_parameters: RegisterParameters

    def __init__(self, register_parameters: _Optional[_Union[RegisterParameters, _Mapping]]=...) -> None:
        ...

class RegisterDomainRequest(_message.Message):
    __slots__ = ('parent', 'registration', 'domain_notices', 'contact_notices', 'yearly_price', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NOTICES_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NOTICES_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    registration: Registration
    domain_notices: _containers.RepeatedScalarFieldContainer[DomainNotice]
    contact_notices: _containers.RepeatedScalarFieldContainer[ContactNotice]
    yearly_price: _money_pb2.Money
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., registration: _Optional[_Union[Registration, _Mapping]]=..., domain_notices: _Optional[_Iterable[_Union[DomainNotice, str]]]=..., contact_notices: _Optional[_Iterable[_Union[ContactNotice, str]]]=..., yearly_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class RetrieveTransferParametersRequest(_message.Message):
    __slots__ = ('domain_name', 'location')
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    location: str

    def __init__(self, domain_name: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class RetrieveTransferParametersResponse(_message.Message):
    __slots__ = ('transfer_parameters',)
    TRANSFER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    transfer_parameters: TransferParameters

    def __init__(self, transfer_parameters: _Optional[_Union[TransferParameters, _Mapping]]=...) -> None:
        ...

class TransferDomainRequest(_message.Message):
    __slots__ = ('parent', 'registration', 'contact_notices', 'yearly_price', 'authorization_code', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NOTICES_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    registration: Registration
    contact_notices: _containers.RepeatedScalarFieldContainer[ContactNotice]
    yearly_price: _money_pb2.Money
    authorization_code: AuthorizationCode
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., registration: _Optional[_Union[Registration, _Mapping]]=..., contact_notices: _Optional[_Iterable[_Union[ContactNotice, str]]]=..., yearly_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., authorization_code: _Optional[_Union[AuthorizationCode, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class ListRegistrationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRegistrationsResponse(_message.Message):
    __slots__ = ('registrations', 'next_page_token')
    REGISTRATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    registrations: _containers.RepeatedCompositeFieldContainer[Registration]
    next_page_token: str

    def __init__(self, registrations: _Optional[_Iterable[_Union[Registration, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRegistrationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateRegistrationRequest(_message.Message):
    __slots__ = ('registration', 'update_mask')
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    registration: Registration
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, registration: _Optional[_Union[Registration, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ConfigureManagementSettingsRequest(_message.Message):
    __slots__ = ('registration', 'management_settings', 'update_mask')
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    registration: str
    management_settings: ManagementSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, registration: _Optional[str]=..., management_settings: _Optional[_Union[ManagementSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ConfigureDnsSettingsRequest(_message.Message):
    __slots__ = ('registration', 'dns_settings', 'update_mask', 'validate_only')
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    DNS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    registration: str
    dns_settings: DnsSettings
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, registration: _Optional[str]=..., dns_settings: _Optional[_Union[DnsSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class ConfigureContactSettingsRequest(_message.Message):
    __slots__ = ('registration', 'contact_settings', 'update_mask', 'contact_notices', 'validate_only')
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    CONTACT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NOTICES_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    registration: str
    contact_settings: ContactSettings
    update_mask: _field_mask_pb2.FieldMask
    contact_notices: _containers.RepeatedScalarFieldContainer[ContactNotice]
    validate_only: bool

    def __init__(self, registration: _Optional[str]=..., contact_settings: _Optional[_Union[ContactSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., contact_notices: _Optional[_Iterable[_Union[ContactNotice, str]]]=..., validate_only: bool=...) -> None:
        ...

class ExportRegistrationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteRegistrationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RetrieveAuthorizationCodeRequest(_message.Message):
    __slots__ = ('registration',)
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    registration: str

    def __init__(self, registration: _Optional[str]=...) -> None:
        ...

class ResetAuthorizationCodeRequest(_message.Message):
    __slots__ = ('registration',)
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    registration: str

    def __init__(self, registration: _Optional[str]=...) -> None:
        ...

class RegisterParameters(_message.Message):
    __slots__ = ('domain_name', 'availability', 'supported_privacy', 'domain_notices', 'yearly_price')

    class Availability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AVAILABILITY_UNSPECIFIED: _ClassVar[RegisterParameters.Availability]
        AVAILABLE: _ClassVar[RegisterParameters.Availability]
        UNAVAILABLE: _ClassVar[RegisterParameters.Availability]
        UNSUPPORTED: _ClassVar[RegisterParameters.Availability]
        UNKNOWN: _ClassVar[RegisterParameters.Availability]
    AVAILABILITY_UNSPECIFIED: RegisterParameters.Availability
    AVAILABLE: RegisterParameters.Availability
    UNAVAILABLE: RegisterParameters.Availability
    UNSUPPORTED: RegisterParameters.Availability
    UNKNOWN: RegisterParameters.Availability
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NOTICES_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    availability: RegisterParameters.Availability
    supported_privacy: _containers.RepeatedScalarFieldContainer[ContactPrivacy]
    domain_notices: _containers.RepeatedScalarFieldContainer[DomainNotice]
    yearly_price: _money_pb2.Money

    def __init__(self, domain_name: _Optional[str]=..., availability: _Optional[_Union[RegisterParameters.Availability, str]]=..., supported_privacy: _Optional[_Iterable[_Union[ContactPrivacy, str]]]=..., domain_notices: _Optional[_Iterable[_Union[DomainNotice, str]]]=..., yearly_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
        ...

class TransferParameters(_message.Message):
    __slots__ = ('domain_name', 'current_registrar', 'name_servers', 'transfer_lock_state', 'supported_privacy', 'yearly_price')
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REGISTRAR_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_LOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    current_registrar: str
    name_servers: _containers.RepeatedScalarFieldContainer[str]
    transfer_lock_state: TransferLockState
    supported_privacy: _containers.RepeatedScalarFieldContainer[ContactPrivacy]
    yearly_price: _money_pb2.Money

    def __init__(self, domain_name: _Optional[str]=..., current_registrar: _Optional[str]=..., name_servers: _Optional[_Iterable[str]]=..., transfer_lock_state: _Optional[_Union[TransferLockState, str]]=..., supported_privacy: _Optional[_Iterable[_Union[ContactPrivacy, str]]]=..., yearly_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
        ...

class AuthorizationCode(_message.Message):
    __slots__ = ('code',)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str

    def __init__(self, code: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_detail', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_detail: _Optional[str]=..., api_version: _Optional[str]=...) -> None:
        ...