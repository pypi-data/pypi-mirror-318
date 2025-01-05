from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import billing_accounts_pb2 as _billing_accounts_pb2
from google.cloud.channel.v1 import channel_partner_links_pb2 as _channel_partner_links_pb2
from google.cloud.channel.v1 import common_pb2 as _common_pb2
from google.cloud.channel.v1 import customers_pb2 as _customers_pb2
from google.cloud.channel.v1 import entitlement_changes_pb2 as _entitlement_changes_pb2
from google.cloud.channel.v1 import entitlements_pb2 as _entitlements_pb2
from google.cloud.channel.v1 import offers_pb2 as _offers_pb2
from google.cloud.channel.v1 import operations_pb2 as _operations_pb2
from google.cloud.channel.v1 import products_pb2 as _products_pb2
from google.cloud.channel.v1 import repricing_pb2 as _repricing_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CheckCloudIdentityAccountsExistRequest(_message.Message):
    __slots__ = ('parent', 'domain', 'primary_admin_email')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ADMIN_EMAIL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    domain: str
    primary_admin_email: str

    def __init__(self, parent: _Optional[str]=..., domain: _Optional[str]=..., primary_admin_email: _Optional[str]=...) -> None:
        ...

class CloudIdentityCustomerAccount(_message.Message):
    __slots__ = ('existing', 'owned', 'customer_name', 'customer_cloud_identity_id', 'customer_type', 'channel_partner_cloud_identity_id')
    EXISTING_FIELD_NUMBER: _ClassVar[int]
    OWNED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    existing: bool
    owned: bool
    customer_name: str
    customer_cloud_identity_id: str
    customer_type: _common_pb2.CloudIdentityInfo.CustomerType
    channel_partner_cloud_identity_id: str

    def __init__(self, existing: bool=..., owned: bool=..., customer_name: _Optional[str]=..., customer_cloud_identity_id: _Optional[str]=..., customer_type: _Optional[_Union[_common_pb2.CloudIdentityInfo.CustomerType, str]]=..., channel_partner_cloud_identity_id: _Optional[str]=...) -> None:
        ...

class CheckCloudIdentityAccountsExistResponse(_message.Message):
    __slots__ = ('cloud_identity_accounts',)
    CLOUD_IDENTITY_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    cloud_identity_accounts: _containers.RepeatedCompositeFieldContainer[CloudIdentityCustomerAccount]

    def __init__(self, cloud_identity_accounts: _Optional[_Iterable[_Union[CloudIdentityCustomerAccount, _Mapping]]]=...) -> None:
        ...

class ListCustomersRequest(_message.Message):
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

class ListCustomersResponse(_message.Message):
    __slots__ = ('customers', 'next_page_token')
    CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    customers: _containers.RepeatedCompositeFieldContainer[_customers_pb2.Customer]
    next_page_token: str

    def __init__(self, customers: _Optional[_Iterable[_Union[_customers_pb2.Customer, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetCustomerRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCustomerRequest(_message.Message):
    __slots__ = ('parent', 'customer')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    customer: _customers_pb2.Customer

    def __init__(self, parent: _Optional[str]=..., customer: _Optional[_Union[_customers_pb2.Customer, _Mapping]]=...) -> None:
        ...

class UpdateCustomerRequest(_message.Message):
    __slots__ = ('customer', 'update_mask')
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    customer: _customers_pb2.Customer
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, customer: _Optional[_Union[_customers_pb2.Customer, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCustomerRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportCustomerRequest(_message.Message):
    __slots__ = ('domain', 'cloud_identity_id', 'primary_admin_email', 'parent', 'auth_token', 'overwrite_if_exists', 'channel_partner_id', 'customer')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ADMIN_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    cloud_identity_id: str
    primary_admin_email: str
    parent: str
    auth_token: str
    overwrite_if_exists: bool
    channel_partner_id: str
    customer: str

    def __init__(self, domain: _Optional[str]=..., cloud_identity_id: _Optional[str]=..., primary_admin_email: _Optional[str]=..., parent: _Optional[str]=..., auth_token: _Optional[str]=..., overwrite_if_exists: bool=..., channel_partner_id: _Optional[str]=..., customer: _Optional[str]=...) -> None:
        ...

class ProvisionCloudIdentityRequest(_message.Message):
    __slots__ = ('customer', 'cloud_identity_info', 'user', 'validate_only')
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_IDENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer: str
    cloud_identity_info: _common_pb2.CloudIdentityInfo
    user: _common_pb2.AdminUser
    validate_only: bool

    def __init__(self, customer: _Optional[str]=..., cloud_identity_info: _Optional[_Union[_common_pb2.CloudIdentityInfo, _Mapping]]=..., user: _Optional[_Union[_common_pb2.AdminUser, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class ListEntitlementsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEntitlementsResponse(_message.Message):
    __slots__ = ('entitlements', 'next_page_token')
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Entitlement]
    next_page_token: str

    def __init__(self, entitlements: _Optional[_Iterable[_Union[_entitlements_pb2.Entitlement, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListTransferableSkusRequest(_message.Message):
    __slots__ = ('cloud_identity_id', 'customer_name', 'parent', 'page_size', 'page_token', 'auth_token', 'language_code')
    CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    cloud_identity_id: str
    customer_name: str
    parent: str
    page_size: int
    page_token: str
    auth_token: str
    language_code: str

    def __init__(self, cloud_identity_id: _Optional[str]=..., customer_name: _Optional[str]=..., parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., auth_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListTransferableSkusResponse(_message.Message):
    __slots__ = ('transferable_skus', 'next_page_token')
    TRANSFERABLE_SKUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transferable_skus: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.TransferableSku]
    next_page_token: str

    def __init__(self, transferable_skus: _Optional[_Iterable[_Union[_entitlements_pb2.TransferableSku, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListTransferableOffersRequest(_message.Message):
    __slots__ = ('cloud_identity_id', 'customer_name', 'parent', 'page_size', 'page_token', 'sku', 'language_code', 'billing_account')
    CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    cloud_identity_id: str
    customer_name: str
    parent: str
    page_size: int
    page_token: str
    sku: str
    language_code: str
    billing_account: str

    def __init__(self, cloud_identity_id: _Optional[str]=..., customer_name: _Optional[str]=..., parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., sku: _Optional[str]=..., language_code: _Optional[str]=..., billing_account: _Optional[str]=...) -> None:
        ...

class ListTransferableOffersResponse(_message.Message):
    __slots__ = ('transferable_offers', 'next_page_token')
    TRANSFERABLE_OFFERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transferable_offers: _containers.RepeatedCompositeFieldContainer[TransferableOffer]
    next_page_token: str

    def __init__(self, transferable_offers: _Optional[_Iterable[_Union[TransferableOffer, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class TransferableOffer(_message.Message):
    __slots__ = ('offer',)
    OFFER_FIELD_NUMBER: _ClassVar[int]
    offer: _offers_pb2.Offer

    def __init__(self, offer: _Optional[_Union[_offers_pb2.Offer, _Mapping]]=...) -> None:
        ...

class GetEntitlementRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListChannelPartnerLinksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: _channel_partner_links_pb2.ChannelPartnerLinkView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[_channel_partner_links_pb2.ChannelPartnerLinkView, str]]=...) -> None:
        ...

class ListChannelPartnerLinksResponse(_message.Message):
    __slots__ = ('channel_partner_links', 'next_page_token')
    CHANNEL_PARTNER_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    channel_partner_links: _containers.RepeatedCompositeFieldContainer[_channel_partner_links_pb2.ChannelPartnerLink]
    next_page_token: str

    def __init__(self, channel_partner_links: _Optional[_Iterable[_Union[_channel_partner_links_pb2.ChannelPartnerLink, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetChannelPartnerLinkRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _channel_partner_links_pb2.ChannelPartnerLinkView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[_channel_partner_links_pb2.ChannelPartnerLinkView, str]]=...) -> None:
        ...

class CreateChannelPartnerLinkRequest(_message.Message):
    __slots__ = ('parent', 'channel_partner_link')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    channel_partner_link: _channel_partner_links_pb2.ChannelPartnerLink

    def __init__(self, parent: _Optional[str]=..., channel_partner_link: _Optional[_Union[_channel_partner_links_pb2.ChannelPartnerLink, _Mapping]]=...) -> None:
        ...

class UpdateChannelPartnerLinkRequest(_message.Message):
    __slots__ = ('name', 'channel_partner_link', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    channel_partner_link: _channel_partner_links_pb2.ChannelPartnerLink
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., channel_partner_link: _Optional[_Union[_channel_partner_links_pb2.ChannelPartnerLink, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetCustomerRepricingConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCustomerRepricingConfigsRequest(_message.Message):
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

class ListCustomerRepricingConfigsResponse(_message.Message):
    __slots__ = ('customer_repricing_configs', 'next_page_token')
    CUSTOMER_REPRICING_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    customer_repricing_configs: _containers.RepeatedCompositeFieldContainer[_repricing_pb2.CustomerRepricingConfig]
    next_page_token: str

    def __init__(self, customer_repricing_configs: _Optional[_Iterable[_Union[_repricing_pb2.CustomerRepricingConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateCustomerRepricingConfigRequest(_message.Message):
    __slots__ = ('parent', 'customer_repricing_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_REPRICING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    customer_repricing_config: _repricing_pb2.CustomerRepricingConfig

    def __init__(self, parent: _Optional[str]=..., customer_repricing_config: _Optional[_Union[_repricing_pb2.CustomerRepricingConfig, _Mapping]]=...) -> None:
        ...

class UpdateCustomerRepricingConfigRequest(_message.Message):
    __slots__ = ('customer_repricing_config',)
    CUSTOMER_REPRICING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    customer_repricing_config: _repricing_pb2.CustomerRepricingConfig

    def __init__(self, customer_repricing_config: _Optional[_Union[_repricing_pb2.CustomerRepricingConfig, _Mapping]]=...) -> None:
        ...

class DeleteCustomerRepricingConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetChannelPartnerRepricingConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListChannelPartnerRepricingConfigsRequest(_message.Message):
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

class ListChannelPartnerRepricingConfigsResponse(_message.Message):
    __slots__ = ('channel_partner_repricing_configs', 'next_page_token')
    CHANNEL_PARTNER_REPRICING_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    channel_partner_repricing_configs: _containers.RepeatedCompositeFieldContainer[_repricing_pb2.ChannelPartnerRepricingConfig]
    next_page_token: str

    def __init__(self, channel_partner_repricing_configs: _Optional[_Iterable[_Union[_repricing_pb2.ChannelPartnerRepricingConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateChannelPartnerRepricingConfigRequest(_message.Message):
    __slots__ = ('parent', 'channel_partner_repricing_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_REPRICING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    channel_partner_repricing_config: _repricing_pb2.ChannelPartnerRepricingConfig

    def __init__(self, parent: _Optional[str]=..., channel_partner_repricing_config: _Optional[_Union[_repricing_pb2.ChannelPartnerRepricingConfig, _Mapping]]=...) -> None:
        ...

class UpdateChannelPartnerRepricingConfigRequest(_message.Message):
    __slots__ = ('channel_partner_repricing_config',)
    CHANNEL_PARTNER_REPRICING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    channel_partner_repricing_config: _repricing_pb2.ChannelPartnerRepricingConfig

    def __init__(self, channel_partner_repricing_config: _Optional[_Union[_repricing_pb2.ChannelPartnerRepricingConfig, _Mapping]]=...) -> None:
        ...

class DeleteChannelPartnerRepricingConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSkuGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSkuGroupBillableSkusRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSkuGroupsResponse(_message.Message):
    __slots__ = ('sku_groups', 'next_page_token')
    SKU_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sku_groups: _containers.RepeatedCompositeFieldContainer[SkuGroup]
    next_page_token: str

    def __init__(self, sku_groups: _Optional[_Iterable[_Union[SkuGroup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListSkuGroupBillableSkusResponse(_message.Message):
    __slots__ = ('billable_skus', 'next_page_token')
    BILLABLE_SKUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    billable_skus: _containers.RepeatedCompositeFieldContainer[BillableSku]
    next_page_token: str

    def __init__(self, billable_skus: _Optional[_Iterable[_Union[BillableSku, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SkuGroup(_message.Message):
    __slots__ = ('name', 'display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class BillableSku(_message.Message):
    __slots__ = ('sku', 'sku_display_name', 'service', 'service_display_name')
    SKU_FIELD_NUMBER: _ClassVar[int]
    SKU_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    sku: str
    sku_display_name: str
    service: str
    service_display_name: str

    def __init__(self, sku: _Optional[str]=..., sku_display_name: _Optional[str]=..., service: _Optional[str]=..., service_display_name: _Optional[str]=...) -> None:
        ...

class CreateEntitlementRequest(_message.Message):
    __slots__ = ('parent', 'entitlement', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entitlement: _entitlements_pb2.Entitlement
    request_id: str

    def __init__(self, parent: _Optional[str]=..., entitlement: _Optional[_Union[_entitlements_pb2.Entitlement, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class TransferEntitlementsRequest(_message.Message):
    __slots__ = ('parent', 'entitlements', 'auth_token', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entitlements: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Entitlement]
    auth_token: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., entitlements: _Optional[_Iterable[_Union[_entitlements_pb2.Entitlement, _Mapping]]]=..., auth_token: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class TransferEntitlementsResponse(_message.Message):
    __slots__ = ('entitlements',)
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Entitlement]

    def __init__(self, entitlements: _Optional[_Iterable[_Union[_entitlements_pb2.Entitlement, _Mapping]]]=...) -> None:
        ...

class TransferEntitlementsToGoogleRequest(_message.Message):
    __slots__ = ('parent', 'entitlements', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entitlements: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Entitlement]
    request_id: str

    def __init__(self, parent: _Optional[str]=..., entitlements: _Optional[_Iterable[_Union[_entitlements_pb2.Entitlement, _Mapping]]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ChangeParametersRequest(_message.Message):
    __slots__ = ('name', 'parameters', 'request_id', 'purchase_order_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameters: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Parameter]
    request_id: str
    purchase_order_id: str

    def __init__(self, name: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[_entitlements_pb2.Parameter, _Mapping]]]=..., request_id: _Optional[str]=..., purchase_order_id: _Optional[str]=...) -> None:
        ...

class ChangeRenewalSettingsRequest(_message.Message):
    __slots__ = ('name', 'renewal_settings', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    renewal_settings: _entitlements_pb2.RenewalSettings
    request_id: str

    def __init__(self, name: _Optional[str]=..., renewal_settings: _Optional[_Union[_entitlements_pb2.RenewalSettings, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ChangeOfferRequest(_message.Message):
    __slots__ = ('name', 'offer', 'parameters', 'purchase_order_id', 'request_id', 'billing_account')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offer: str
    parameters: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Parameter]
    purchase_order_id: str
    request_id: str
    billing_account: str

    def __init__(self, name: _Optional[str]=..., offer: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[_entitlements_pb2.Parameter, _Mapping]]]=..., purchase_order_id: _Optional[str]=..., request_id: _Optional[str]=..., billing_account: _Optional[str]=...) -> None:
        ...

class StartPaidServiceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class CancelEntitlementRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class SuspendEntitlementRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ActivateEntitlementRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class LookupOfferRequest(_message.Message):
    __slots__ = ('entitlement',)
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    entitlement: str

    def __init__(self, entitlement: _Optional[str]=...) -> None:
        ...

class ListProductsRequest(_message.Message):
    __slots__ = ('account', 'page_size', 'page_token', 'language_code')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    account: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, account: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListProductsResponse(_message.Message):
    __slots__ = ('products', 'next_page_token')
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[_products_pb2.Product]
    next_page_token: str

    def __init__(self, products: _Optional[_Iterable[_Union[_products_pb2.Product, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListSkusRequest(_message.Message):
    __slots__ = ('parent', 'account', 'page_size', 'page_token', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    account: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, parent: _Optional[str]=..., account: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListSkusResponse(_message.Message):
    __slots__ = ('skus', 'next_page_token')
    SKUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    skus: _containers.RepeatedCompositeFieldContainer[_products_pb2.Sku]
    next_page_token: str

    def __init__(self, skus: _Optional[_Iterable[_Union[_products_pb2.Sku, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListOffersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'language_code', 'show_future_offers')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SHOW_FUTURE_OFFERS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    language_code: str
    show_future_offers: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., language_code: _Optional[str]=..., show_future_offers: bool=...) -> None:
        ...

class ListOffersResponse(_message.Message):
    __slots__ = ('offers', 'next_page_token')
    OFFERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    offers: _containers.RepeatedCompositeFieldContainer[_offers_pb2.Offer]
    next_page_token: str

    def __init__(self, offers: _Optional[_Iterable[_Union[_offers_pb2.Offer, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListPurchasableSkusRequest(_message.Message):
    __slots__ = ('create_entitlement_purchase', 'change_offer_purchase', 'customer', 'page_size', 'page_token', 'language_code')

    class CreateEntitlementPurchase(_message.Message):
        __slots__ = ('product',)
        PRODUCT_FIELD_NUMBER: _ClassVar[int]
        product: str

        def __init__(self, product: _Optional[str]=...) -> None:
            ...

    class ChangeOfferPurchase(_message.Message):
        __slots__ = ('entitlement', 'change_type')

        class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CHANGE_TYPE_UNSPECIFIED: _ClassVar[ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType]
            UPGRADE: _ClassVar[ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType]
            DOWNGRADE: _ClassVar[ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType]
        CHANGE_TYPE_UNSPECIFIED: ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType
        UPGRADE: ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType
        DOWNGRADE: ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType
        ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
        CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        entitlement: str
        change_type: ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType

        def __init__(self, entitlement: _Optional[str]=..., change_type: _Optional[_Union[ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType, str]]=...) -> None:
            ...
    CREATE_ENTITLEMENT_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OFFER_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    create_entitlement_purchase: ListPurchasableSkusRequest.CreateEntitlementPurchase
    change_offer_purchase: ListPurchasableSkusRequest.ChangeOfferPurchase
    customer: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, create_entitlement_purchase: _Optional[_Union[ListPurchasableSkusRequest.CreateEntitlementPurchase, _Mapping]]=..., change_offer_purchase: _Optional[_Union[ListPurchasableSkusRequest.ChangeOfferPurchase, _Mapping]]=..., customer: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListPurchasableSkusResponse(_message.Message):
    __slots__ = ('purchasable_skus', 'next_page_token')
    PURCHASABLE_SKUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    purchasable_skus: _containers.RepeatedCompositeFieldContainer[PurchasableSku]
    next_page_token: str

    def __init__(self, purchasable_skus: _Optional[_Iterable[_Union[PurchasableSku, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class PurchasableSku(_message.Message):
    __slots__ = ('sku',)
    SKU_FIELD_NUMBER: _ClassVar[int]
    sku: _products_pb2.Sku

    def __init__(self, sku: _Optional[_Union[_products_pb2.Sku, _Mapping]]=...) -> None:
        ...

class ListPurchasableOffersRequest(_message.Message):
    __slots__ = ('create_entitlement_purchase', 'change_offer_purchase', 'customer', 'page_size', 'page_token', 'language_code')

    class CreateEntitlementPurchase(_message.Message):
        __slots__ = ('sku', 'billing_account')
        SKU_FIELD_NUMBER: _ClassVar[int]
        BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        sku: str
        billing_account: str

        def __init__(self, sku: _Optional[str]=..., billing_account: _Optional[str]=...) -> None:
            ...

    class ChangeOfferPurchase(_message.Message):
        __slots__ = ('entitlement', 'new_sku', 'billing_account')
        ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
        NEW_SKU_FIELD_NUMBER: _ClassVar[int]
        BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        entitlement: str
        new_sku: str
        billing_account: str

        def __init__(self, entitlement: _Optional[str]=..., new_sku: _Optional[str]=..., billing_account: _Optional[str]=...) -> None:
            ...
    CREATE_ENTITLEMENT_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OFFER_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    create_entitlement_purchase: ListPurchasableOffersRequest.CreateEntitlementPurchase
    change_offer_purchase: ListPurchasableOffersRequest.ChangeOfferPurchase
    customer: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, create_entitlement_purchase: _Optional[_Union[ListPurchasableOffersRequest.CreateEntitlementPurchase, _Mapping]]=..., change_offer_purchase: _Optional[_Union[ListPurchasableOffersRequest.ChangeOfferPurchase, _Mapping]]=..., customer: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListPurchasableOffersResponse(_message.Message):
    __slots__ = ('purchasable_offers', 'next_page_token')
    PURCHASABLE_OFFERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    purchasable_offers: _containers.RepeatedCompositeFieldContainer[PurchasableOffer]
    next_page_token: str

    def __init__(self, purchasable_offers: _Optional[_Iterable[_Union[PurchasableOffer, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class PurchasableOffer(_message.Message):
    __slots__ = ('offer',)
    OFFER_FIELD_NUMBER: _ClassVar[int]
    offer: _offers_pb2.Offer

    def __init__(self, offer: _Optional[_Union[_offers_pb2.Offer, _Mapping]]=...) -> None:
        ...

class QueryEligibleBillingAccountsRequest(_message.Message):
    __slots__ = ('customer', 'skus')
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    SKUS_FIELD_NUMBER: _ClassVar[int]
    customer: str
    skus: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, customer: _Optional[str]=..., skus: _Optional[_Iterable[str]]=...) -> None:
        ...

class QueryEligibleBillingAccountsResponse(_message.Message):
    __slots__ = ('sku_purchase_groups',)
    SKU_PURCHASE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    sku_purchase_groups: _containers.RepeatedCompositeFieldContainer[SkuPurchaseGroup]

    def __init__(self, sku_purchase_groups: _Optional[_Iterable[_Union[SkuPurchaseGroup, _Mapping]]]=...) -> None:
        ...

class SkuPurchaseGroup(_message.Message):
    __slots__ = ('skus', 'billing_account_purchase_infos')
    SKUS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_PURCHASE_INFOS_FIELD_NUMBER: _ClassVar[int]
    skus: _containers.RepeatedScalarFieldContainer[str]
    billing_account_purchase_infos: _containers.RepeatedCompositeFieldContainer[BillingAccountPurchaseInfo]

    def __init__(self, skus: _Optional[_Iterable[str]]=..., billing_account_purchase_infos: _Optional[_Iterable[_Union[BillingAccountPurchaseInfo, _Mapping]]]=...) -> None:
        ...

class BillingAccountPurchaseInfo(_message.Message):
    __slots__ = ('billing_account',)
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    billing_account: _billing_accounts_pb2.BillingAccount

    def __init__(self, billing_account: _Optional[_Union[_billing_accounts_pb2.BillingAccount, _Mapping]]=...) -> None:
        ...

class RegisterSubscriberRequest(_message.Message):
    __slots__ = ('account', 'service_account')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: str
    service_account: str

    def __init__(self, account: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class RegisterSubscriberResponse(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str

    def __init__(self, topic: _Optional[str]=...) -> None:
        ...

class UnregisterSubscriberRequest(_message.Message):
    __slots__ = ('account', 'service_account')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: str
    service_account: str

    def __init__(self, account: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class UnregisterSubscriberResponse(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str

    def __init__(self, topic: _Optional[str]=...) -> None:
        ...

class ListSubscribersRequest(_message.Message):
    __slots__ = ('account', 'page_size', 'page_token')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account: str
    page_size: int
    page_token: str

    def __init__(self, account: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSubscribersResponse(_message.Message):
    __slots__ = ('topic', 'service_accounts', 'next_page_token')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topic: str
    service_accounts: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, topic: _Optional[str]=..., service_accounts: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListEntitlementChangesRequest(_message.Message):
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

class ListEntitlementChangesResponse(_message.Message):
    __slots__ = ('entitlement_changes', 'next_page_token')
    ENTITLEMENT_CHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entitlement_changes: _containers.RepeatedCompositeFieldContainer[_entitlement_changes_pb2.EntitlementChange]
    next_page_token: str

    def __init__(self, entitlement_changes: _Optional[_Iterable[_Union[_entitlement_changes_pb2.EntitlementChange, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...