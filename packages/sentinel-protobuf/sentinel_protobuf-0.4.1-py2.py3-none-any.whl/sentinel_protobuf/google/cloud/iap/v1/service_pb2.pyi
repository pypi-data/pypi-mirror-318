from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTunnelDestGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTunnelDestGroupsResponse(_message.Message):
    __slots__ = ("tunnel_dest_groups", "next_page_token")
    TUNNEL_DEST_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tunnel_dest_groups: _containers.RepeatedCompositeFieldContainer[TunnelDestGroup]
    next_page_token: str
    def __init__(self, tunnel_dest_groups: _Optional[_Iterable[_Union[TunnelDestGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateTunnelDestGroupRequest(_message.Message):
    __slots__ = ("parent", "tunnel_dest_group", "tunnel_dest_group_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_DEST_GROUP_FIELD_NUMBER: _ClassVar[int]
    TUNNEL_DEST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tunnel_dest_group: TunnelDestGroup
    tunnel_dest_group_id: str
    def __init__(self, parent: _Optional[str] = ..., tunnel_dest_group: _Optional[_Union[TunnelDestGroup, _Mapping]] = ..., tunnel_dest_group_id: _Optional[str] = ...) -> None: ...

class GetTunnelDestGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteTunnelDestGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateTunnelDestGroupRequest(_message.Message):
    __slots__ = ("tunnel_dest_group", "update_mask")
    TUNNEL_DEST_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tunnel_dest_group: TunnelDestGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tunnel_dest_group: _Optional[_Union[TunnelDestGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class TunnelDestGroup(_message.Message):
    __slots__ = ("name", "cidrs", "fqdns")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CIDRS_FIELD_NUMBER: _ClassVar[int]
    FQDNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    cidrs: _containers.RepeatedScalarFieldContainer[str]
    fqdns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., cidrs: _Optional[_Iterable[str]] = ..., fqdns: _Optional[_Iterable[str]] = ...) -> None: ...

class GetIapSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateIapSettingsRequest(_message.Message):
    __slots__ = ("iap_settings", "update_mask")
    IAP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    iap_settings: IapSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, iap_settings: _Optional[_Union[IapSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class IapSettings(_message.Message):
    __slots__ = ("name", "access_settings", "application_settings")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    access_settings: AccessSettings
    application_settings: ApplicationSettings
    def __init__(self, name: _Optional[str] = ..., access_settings: _Optional[_Union[AccessSettings, _Mapping]] = ..., application_settings: _Optional[_Union[ApplicationSettings, _Mapping]] = ...) -> None: ...

class AccessSettings(_message.Message):
    __slots__ = ("gcip_settings", "cors_settings", "oauth_settings", "reauth_settings", "allowed_domains_settings")
    GCIP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CORS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REAUTH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DOMAINS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    gcip_settings: GcipSettings
    cors_settings: CorsSettings
    oauth_settings: OAuthSettings
    reauth_settings: ReauthSettings
    allowed_domains_settings: AllowedDomainsSettings
    def __init__(self, gcip_settings: _Optional[_Union[GcipSettings, _Mapping]] = ..., cors_settings: _Optional[_Union[CorsSettings, _Mapping]] = ..., oauth_settings: _Optional[_Union[OAuthSettings, _Mapping]] = ..., reauth_settings: _Optional[_Union[ReauthSettings, _Mapping]] = ..., allowed_domains_settings: _Optional[_Union[AllowedDomainsSettings, _Mapping]] = ...) -> None: ...

class GcipSettings(_message.Message):
    __slots__ = ("tenant_ids", "login_page_uri")
    TENANT_IDS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_PAGE_URI_FIELD_NUMBER: _ClassVar[int]
    tenant_ids: _containers.RepeatedScalarFieldContainer[str]
    login_page_uri: _wrappers_pb2.StringValue
    def __init__(self, tenant_ids: _Optional[_Iterable[str]] = ..., login_page_uri: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class CorsSettings(_message.Message):
    __slots__ = ("allow_http_options",)
    ALLOW_HTTP_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    allow_http_options: _wrappers_pb2.BoolValue
    def __init__(self, allow_http_options: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class OAuthSettings(_message.Message):
    __slots__ = ("login_hint", "programmatic_clients")
    LOGIN_HINT_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMATIC_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    login_hint: _wrappers_pb2.StringValue
    programmatic_clients: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, login_hint: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., programmatic_clients: _Optional[_Iterable[str]] = ...) -> None: ...

class ReauthSettings(_message.Message):
    __slots__ = ("method", "max_age", "policy_type")
    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_UNSPECIFIED: _ClassVar[ReauthSettings.Method]
        LOGIN: _ClassVar[ReauthSettings.Method]
        PASSWORD: _ClassVar[ReauthSettings.Method]
        SECURE_KEY: _ClassVar[ReauthSettings.Method]
        ENROLLED_SECOND_FACTORS: _ClassVar[ReauthSettings.Method]
    METHOD_UNSPECIFIED: ReauthSettings.Method
    LOGIN: ReauthSettings.Method
    PASSWORD: ReauthSettings.Method
    SECURE_KEY: ReauthSettings.Method
    ENROLLED_SECOND_FACTORS: ReauthSettings.Method
    class PolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POLICY_TYPE_UNSPECIFIED: _ClassVar[ReauthSettings.PolicyType]
        MINIMUM: _ClassVar[ReauthSettings.PolicyType]
        DEFAULT: _ClassVar[ReauthSettings.PolicyType]
    POLICY_TYPE_UNSPECIFIED: ReauthSettings.PolicyType
    MINIMUM: ReauthSettings.PolicyType
    DEFAULT: ReauthSettings.PolicyType
    METHOD_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    method: ReauthSettings.Method
    max_age: _duration_pb2.Duration
    policy_type: ReauthSettings.PolicyType
    def __init__(self, method: _Optional[_Union[ReauthSettings.Method, str]] = ..., max_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., policy_type: _Optional[_Union[ReauthSettings.PolicyType, str]] = ...) -> None: ...

class AllowedDomainsSettings(_message.Message):
    __slots__ = ("enable", "domains")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enable: bool = ..., domains: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplicationSettings(_message.Message):
    __slots__ = ("csm_settings", "access_denied_page_settings", "cookie_domain", "attribute_propagation_settings")
    CSM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DENIED_PAGE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_PROPAGATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    csm_settings: CsmSettings
    access_denied_page_settings: AccessDeniedPageSettings
    cookie_domain: _wrappers_pb2.StringValue
    attribute_propagation_settings: AttributePropagationSettings
    def __init__(self, csm_settings: _Optional[_Union[CsmSettings, _Mapping]] = ..., access_denied_page_settings: _Optional[_Union[AccessDeniedPageSettings, _Mapping]] = ..., cookie_domain: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., attribute_propagation_settings: _Optional[_Union[AttributePropagationSettings, _Mapping]] = ...) -> None: ...

class CsmSettings(_message.Message):
    __slots__ = ("rctoken_aud",)
    RCTOKEN_AUD_FIELD_NUMBER: _ClassVar[int]
    rctoken_aud: _wrappers_pb2.StringValue
    def __init__(self, rctoken_aud: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class AccessDeniedPageSettings(_message.Message):
    __slots__ = ("access_denied_page_uri", "generate_troubleshooting_uri", "remediation_token_generation_enabled")
    ACCESS_DENIED_PAGE_URI_FIELD_NUMBER: _ClassVar[int]
    GENERATE_TROUBLESHOOTING_URI_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_TOKEN_GENERATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    access_denied_page_uri: _wrappers_pb2.StringValue
    generate_troubleshooting_uri: _wrappers_pb2.BoolValue
    remediation_token_generation_enabled: _wrappers_pb2.BoolValue
    def __init__(self, access_denied_page_uri: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., generate_troubleshooting_uri: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., remediation_token_generation_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class AttributePropagationSettings(_message.Message):
    __slots__ = ("expression", "output_credentials", "enable")
    class OutputCredentials(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTPUT_CREDENTIALS_UNSPECIFIED: _ClassVar[AttributePropagationSettings.OutputCredentials]
        HEADER: _ClassVar[AttributePropagationSettings.OutputCredentials]
        JWT: _ClassVar[AttributePropagationSettings.OutputCredentials]
        RCTOKEN: _ClassVar[AttributePropagationSettings.OutputCredentials]
    OUTPUT_CREDENTIALS_UNSPECIFIED: AttributePropagationSettings.OutputCredentials
    HEADER: AttributePropagationSettings.OutputCredentials
    JWT: AttributePropagationSettings.OutputCredentials
    RCTOKEN: AttributePropagationSettings.OutputCredentials
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    expression: str
    output_credentials: _containers.RepeatedScalarFieldContainer[AttributePropagationSettings.OutputCredentials]
    enable: bool
    def __init__(self, expression: _Optional[str] = ..., output_credentials: _Optional[_Iterable[_Union[AttributePropagationSettings.OutputCredentials, str]]] = ..., enable: bool = ...) -> None: ...

class ListBrandsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListBrandsResponse(_message.Message):
    __slots__ = ("brands",)
    BRANDS_FIELD_NUMBER: _ClassVar[int]
    brands: _containers.RepeatedCompositeFieldContainer[Brand]
    def __init__(self, brands: _Optional[_Iterable[_Union[Brand, _Mapping]]] = ...) -> None: ...

class CreateBrandRequest(_message.Message):
    __slots__ = ("parent", "brand")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    parent: str
    brand: Brand
    def __init__(self, parent: _Optional[str] = ..., brand: _Optional[_Union[Brand, _Mapping]] = ...) -> None: ...

class GetBrandRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListIdentityAwareProxyClientsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListIdentityAwareProxyClientsResponse(_message.Message):
    __slots__ = ("identity_aware_proxy_clients", "next_page_token")
    IDENTITY_AWARE_PROXY_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identity_aware_proxy_clients: _containers.RepeatedCompositeFieldContainer[IdentityAwareProxyClient]
    next_page_token: str
    def __init__(self, identity_aware_proxy_clients: _Optional[_Iterable[_Union[IdentityAwareProxyClient, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateIdentityAwareProxyClientRequest(_message.Message):
    __slots__ = ("parent", "identity_aware_proxy_client")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_AWARE_PROXY_CLIENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    identity_aware_proxy_client: IdentityAwareProxyClient
    def __init__(self, parent: _Optional[str] = ..., identity_aware_proxy_client: _Optional[_Union[IdentityAwareProxyClient, _Mapping]] = ...) -> None: ...

class GetIdentityAwareProxyClientRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResetIdentityAwareProxyClientSecretRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteIdentityAwareProxyClientRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Brand(_message.Message):
    __slots__ = ("name", "support_email", "application_title", "org_internal_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_TITLE_FIELD_NUMBER: _ClassVar[int]
    ORG_INTERNAL_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    support_email: str
    application_title: str
    org_internal_only: bool
    def __init__(self, name: _Optional[str] = ..., support_email: _Optional[str] = ..., application_title: _Optional[str] = ..., org_internal_only: bool = ...) -> None: ...

class IdentityAwareProxyClient(_message.Message):
    __slots__ = ("name", "secret", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    secret: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., secret: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...
