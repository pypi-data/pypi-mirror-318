from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UptimeCheckRegion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGION_UNSPECIFIED: _ClassVar[UptimeCheckRegion]
    USA: _ClassVar[UptimeCheckRegion]
    EUROPE: _ClassVar[UptimeCheckRegion]
    SOUTH_AMERICA: _ClassVar[UptimeCheckRegion]
    ASIA_PACIFIC: _ClassVar[UptimeCheckRegion]
    USA_OREGON: _ClassVar[UptimeCheckRegion]
    USA_IOWA: _ClassVar[UptimeCheckRegion]
    USA_VIRGINIA: _ClassVar[UptimeCheckRegion]

class GroupResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_TYPE_UNSPECIFIED: _ClassVar[GroupResourceType]
    INSTANCE: _ClassVar[GroupResourceType]
    AWS_ELB_LOAD_BALANCER: _ClassVar[GroupResourceType]
REGION_UNSPECIFIED: UptimeCheckRegion
USA: UptimeCheckRegion
EUROPE: UptimeCheckRegion
SOUTH_AMERICA: UptimeCheckRegion
ASIA_PACIFIC: UptimeCheckRegion
USA_OREGON: UptimeCheckRegion
USA_IOWA: UptimeCheckRegion
USA_VIRGINIA: UptimeCheckRegion
RESOURCE_TYPE_UNSPECIFIED: GroupResourceType
INSTANCE: GroupResourceType
AWS_ELB_LOAD_BALANCER: GroupResourceType

class InternalChecker(_message.Message):
    __slots__ = ('name', 'display_name', 'network', 'gcp_zone', 'peer_project_id', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InternalChecker.State]
        CREATING: _ClassVar[InternalChecker.State]
        RUNNING: _ClassVar[InternalChecker.State]
    UNSPECIFIED: InternalChecker.State
    CREATING: InternalChecker.State
    RUNNING: InternalChecker.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    GCP_ZONE_FIELD_NUMBER: _ClassVar[int]
    PEER_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    network: str
    gcp_zone: str
    peer_project_id: str
    state: InternalChecker.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., network: _Optional[str]=..., gcp_zone: _Optional[str]=..., peer_project_id: _Optional[str]=..., state: _Optional[_Union[InternalChecker.State, str]]=...) -> None:
        ...

class SyntheticMonitorTarget(_message.Message):
    __slots__ = ('cloud_function_v2',)

    class CloudFunctionV2Target(_message.Message):
        __slots__ = ('name', 'cloud_run_revision')
        NAME_FIELD_NUMBER: _ClassVar[int]
        CLOUD_RUN_REVISION_FIELD_NUMBER: _ClassVar[int]
        name: str
        cloud_run_revision: _monitored_resource_pb2.MonitoredResource

        def __init__(self, name: _Optional[str]=..., cloud_run_revision: _Optional[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]=...) -> None:
            ...
    CLOUD_FUNCTION_V2_FIELD_NUMBER: _ClassVar[int]
    cloud_function_v2: SyntheticMonitorTarget.CloudFunctionV2Target

    def __init__(self, cloud_function_v2: _Optional[_Union[SyntheticMonitorTarget.CloudFunctionV2Target, _Mapping]]=...) -> None:
        ...

class UptimeCheckConfig(_message.Message):
    __slots__ = ('name', 'display_name', 'monitored_resource', 'resource_group', 'synthetic_monitor', 'http_check', 'tcp_check', 'period', 'timeout', 'content_matchers', 'checker_type', 'selected_regions', 'is_internal', 'internal_checkers', 'user_labels')

    class CheckerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHECKER_TYPE_UNSPECIFIED: _ClassVar[UptimeCheckConfig.CheckerType]
        STATIC_IP_CHECKERS: _ClassVar[UptimeCheckConfig.CheckerType]
        VPC_CHECKERS: _ClassVar[UptimeCheckConfig.CheckerType]
    CHECKER_TYPE_UNSPECIFIED: UptimeCheckConfig.CheckerType
    STATIC_IP_CHECKERS: UptimeCheckConfig.CheckerType
    VPC_CHECKERS: UptimeCheckConfig.CheckerType

    class ResourceGroup(_message.Message):
        __slots__ = ('group_id', 'resource_type')
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        resource_type: GroupResourceType

        def __init__(self, group_id: _Optional[str]=..., resource_type: _Optional[_Union[GroupResourceType, str]]=...) -> None:
            ...

    class PingConfig(_message.Message):
        __slots__ = ('pings_count',)
        PINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
        pings_count: int

        def __init__(self, pings_count: _Optional[int]=...) -> None:
            ...

    class HttpCheck(_message.Message):
        __slots__ = ('request_method', 'use_ssl', 'path', 'port', 'auth_info', 'mask_headers', 'headers', 'content_type', 'custom_content_type', 'validate_ssl', 'body', 'accepted_response_status_codes', 'ping_config', 'service_agent_authentication')

        class RequestMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD_UNSPECIFIED: _ClassVar[UptimeCheckConfig.HttpCheck.RequestMethod]
            GET: _ClassVar[UptimeCheckConfig.HttpCheck.RequestMethod]
            POST: _ClassVar[UptimeCheckConfig.HttpCheck.RequestMethod]
        METHOD_UNSPECIFIED: UptimeCheckConfig.HttpCheck.RequestMethod
        GET: UptimeCheckConfig.HttpCheck.RequestMethod
        POST: UptimeCheckConfig.HttpCheck.RequestMethod

        class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[UptimeCheckConfig.HttpCheck.ContentType]
            URL_ENCODED: _ClassVar[UptimeCheckConfig.HttpCheck.ContentType]
            USER_PROVIDED: _ClassVar[UptimeCheckConfig.HttpCheck.ContentType]
        TYPE_UNSPECIFIED: UptimeCheckConfig.HttpCheck.ContentType
        URL_ENCODED: UptimeCheckConfig.HttpCheck.ContentType
        USER_PROVIDED: UptimeCheckConfig.HttpCheck.ContentType

        class BasicAuthentication(_message.Message):
            __slots__ = ('username', 'password')
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            username: str
            password: str

            def __init__(self, username: _Optional[str]=..., password: _Optional[str]=...) -> None:
                ...

        class ResponseStatusCode(_message.Message):
            __slots__ = ('status_value', 'status_class')

            class StatusClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATUS_CLASS_UNSPECIFIED: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
                STATUS_CLASS_1XX: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
                STATUS_CLASS_2XX: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
                STATUS_CLASS_3XX: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
                STATUS_CLASS_4XX: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
                STATUS_CLASS_5XX: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
                STATUS_CLASS_ANY: _ClassVar[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass]
            STATUS_CLASS_UNSPECIFIED: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_CLASS_1XX: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_CLASS_2XX: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_CLASS_3XX: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_CLASS_4XX: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_CLASS_5XX: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_CLASS_ANY: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass
            STATUS_VALUE_FIELD_NUMBER: _ClassVar[int]
            STATUS_CLASS_FIELD_NUMBER: _ClassVar[int]
            status_value: int
            status_class: UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass

            def __init__(self, status_value: _Optional[int]=..., status_class: _Optional[_Union[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass, str]]=...) -> None:
                ...

        class ServiceAgentAuthentication(_message.Message):
            __slots__ = ('type',)

            class ServiceAgentAuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SERVICE_AGENT_AUTHENTICATION_TYPE_UNSPECIFIED: _ClassVar[UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType]
                OIDC_TOKEN: _ClassVar[UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType]
            SERVICE_AGENT_AUTHENTICATION_TYPE_UNSPECIFIED: UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType
            OIDC_TOKEN: UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType

            def __init__(self, type: _Optional[_Union[UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType, str]]=...) -> None:
                ...

        class HeadersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
        USE_SSL_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        AUTH_INFO_FIELD_NUMBER: _ClassVar[int]
        MASK_HEADERS_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALIDATE_SSL_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        ACCEPTED_RESPONSE_STATUS_CODES_FIELD_NUMBER: _ClassVar[int]
        PING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_AGENT_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
        request_method: UptimeCheckConfig.HttpCheck.RequestMethod
        use_ssl: bool
        path: str
        port: int
        auth_info: UptimeCheckConfig.HttpCheck.BasicAuthentication
        mask_headers: bool
        headers: _containers.ScalarMap[str, str]
        content_type: UptimeCheckConfig.HttpCheck.ContentType
        custom_content_type: str
        validate_ssl: bool
        body: bytes
        accepted_response_status_codes: _containers.RepeatedCompositeFieldContainer[UptimeCheckConfig.HttpCheck.ResponseStatusCode]
        ping_config: UptimeCheckConfig.PingConfig
        service_agent_authentication: UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication

        def __init__(self, request_method: _Optional[_Union[UptimeCheckConfig.HttpCheck.RequestMethod, str]]=..., use_ssl: bool=..., path: _Optional[str]=..., port: _Optional[int]=..., auth_info: _Optional[_Union[UptimeCheckConfig.HttpCheck.BasicAuthentication, _Mapping]]=..., mask_headers: bool=..., headers: _Optional[_Mapping[str, str]]=..., content_type: _Optional[_Union[UptimeCheckConfig.HttpCheck.ContentType, str]]=..., custom_content_type: _Optional[str]=..., validate_ssl: bool=..., body: _Optional[bytes]=..., accepted_response_status_codes: _Optional[_Iterable[_Union[UptimeCheckConfig.HttpCheck.ResponseStatusCode, _Mapping]]]=..., ping_config: _Optional[_Union[UptimeCheckConfig.PingConfig, _Mapping]]=..., service_agent_authentication: _Optional[_Union[UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication, _Mapping]]=...) -> None:
            ...

    class TcpCheck(_message.Message):
        __slots__ = ('port', 'ping_config')
        PORT_FIELD_NUMBER: _ClassVar[int]
        PING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        port: int
        ping_config: UptimeCheckConfig.PingConfig

        def __init__(self, port: _Optional[int]=..., ping_config: _Optional[_Union[UptimeCheckConfig.PingConfig, _Mapping]]=...) -> None:
            ...

    class ContentMatcher(_message.Message):
        __slots__ = ('content', 'matcher', 'json_path_matcher')

        class ContentMatcherOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_MATCHER_OPTION_UNSPECIFIED: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
            CONTAINS_STRING: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
            NOT_CONTAINS_STRING: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
            MATCHES_REGEX: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
            NOT_MATCHES_REGEX: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
            MATCHES_JSON_PATH: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
            NOT_MATCHES_JSON_PATH: _ClassVar[UptimeCheckConfig.ContentMatcher.ContentMatcherOption]
        CONTENT_MATCHER_OPTION_UNSPECIFIED: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        CONTAINS_STRING: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        NOT_CONTAINS_STRING: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        MATCHES_REGEX: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        NOT_MATCHES_REGEX: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        MATCHES_JSON_PATH: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        NOT_MATCHES_JSON_PATH: UptimeCheckConfig.ContentMatcher.ContentMatcherOption

        class JsonPathMatcher(_message.Message):
            __slots__ = ('json_path', 'json_matcher')

            class JsonPathMatcherOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                JSON_PATH_MATCHER_OPTION_UNSPECIFIED: _ClassVar[UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption]
                EXACT_MATCH: _ClassVar[UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption]
                REGEX_MATCH: _ClassVar[UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption]
            JSON_PATH_MATCHER_OPTION_UNSPECIFIED: UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption
            EXACT_MATCH: UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption
            REGEX_MATCH: UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption
            JSON_PATH_FIELD_NUMBER: _ClassVar[int]
            JSON_MATCHER_FIELD_NUMBER: _ClassVar[int]
            json_path: str
            json_matcher: UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption

            def __init__(self, json_path: _Optional[str]=..., json_matcher: _Optional[_Union[UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption, str]]=...) -> None:
                ...
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        MATCHER_FIELD_NUMBER: _ClassVar[int]
        JSON_PATH_MATCHER_FIELD_NUMBER: _ClassVar[int]
        content: str
        matcher: UptimeCheckConfig.ContentMatcher.ContentMatcherOption
        json_path_matcher: UptimeCheckConfig.ContentMatcher.JsonPathMatcher

        def __init__(self, content: _Optional[str]=..., matcher: _Optional[_Union[UptimeCheckConfig.ContentMatcher.ContentMatcherOption, str]]=..., json_path_matcher: _Optional[_Union[UptimeCheckConfig.ContentMatcher.JsonPathMatcher, _Mapping]]=...) -> None:
            ...

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MONITORED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_MONITOR_FIELD_NUMBER: _ClassVar[int]
    HTTP_CHECK_FIELD_NUMBER: _ClassVar[int]
    TCP_CHECK_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    CHECKER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_CHECKERS_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    monitored_resource: _monitored_resource_pb2.MonitoredResource
    resource_group: UptimeCheckConfig.ResourceGroup
    synthetic_monitor: SyntheticMonitorTarget
    http_check: UptimeCheckConfig.HttpCheck
    tcp_check: UptimeCheckConfig.TcpCheck
    period: _duration_pb2.Duration
    timeout: _duration_pb2.Duration
    content_matchers: _containers.RepeatedCompositeFieldContainer[UptimeCheckConfig.ContentMatcher]
    checker_type: UptimeCheckConfig.CheckerType
    selected_regions: _containers.RepeatedScalarFieldContainer[UptimeCheckRegion]
    is_internal: bool
    internal_checkers: _containers.RepeatedCompositeFieldContainer[InternalChecker]
    user_labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., monitored_resource: _Optional[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]=..., resource_group: _Optional[_Union[UptimeCheckConfig.ResourceGroup, _Mapping]]=..., synthetic_monitor: _Optional[_Union[SyntheticMonitorTarget, _Mapping]]=..., http_check: _Optional[_Union[UptimeCheckConfig.HttpCheck, _Mapping]]=..., tcp_check: _Optional[_Union[UptimeCheckConfig.TcpCheck, _Mapping]]=..., period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., content_matchers: _Optional[_Iterable[_Union[UptimeCheckConfig.ContentMatcher, _Mapping]]]=..., checker_type: _Optional[_Union[UptimeCheckConfig.CheckerType, str]]=..., selected_regions: _Optional[_Iterable[_Union[UptimeCheckRegion, str]]]=..., is_internal: bool=..., internal_checkers: _Optional[_Iterable[_Union[InternalChecker, _Mapping]]]=..., user_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class UptimeCheckIp(_message.Message):
    __slots__ = ('region', 'location', 'ip_address')
    REGION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    region: UptimeCheckRegion
    location: str
    ip_address: str

    def __init__(self, region: _Optional[_Union[UptimeCheckRegion, str]]=..., location: _Optional[str]=..., ip_address: _Optional[str]=...) -> None:
        ...