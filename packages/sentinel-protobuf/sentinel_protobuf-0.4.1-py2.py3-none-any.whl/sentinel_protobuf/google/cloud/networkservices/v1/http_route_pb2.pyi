from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HttpRoute(_message.Message):
    __slots__ = ('name', 'self_link', 'description', 'create_time', 'update_time', 'hostnames', 'meshes', 'gateways', 'labels', 'rules')

    class HeaderMatch(_message.Message):
        __slots__ = ('exact_match', 'regex_match', 'prefix_match', 'present_match', 'suffix_match', 'range_match', 'header', 'invert_match')

        class IntegerRange(_message.Message):
            __slots__ = ('start', 'end')
            START_FIELD_NUMBER: _ClassVar[int]
            END_FIELD_NUMBER: _ClassVar[int]
            start: int
            end: int

            def __init__(self, start: _Optional[int]=..., end: _Optional[int]=...) -> None:
                ...
        EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
        REGEX_MATCH_FIELD_NUMBER: _ClassVar[int]
        PREFIX_MATCH_FIELD_NUMBER: _ClassVar[int]
        PRESENT_MATCH_FIELD_NUMBER: _ClassVar[int]
        SUFFIX_MATCH_FIELD_NUMBER: _ClassVar[int]
        RANGE_MATCH_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        INVERT_MATCH_FIELD_NUMBER: _ClassVar[int]
        exact_match: str
        regex_match: str
        prefix_match: str
        present_match: bool
        suffix_match: str
        range_match: HttpRoute.HeaderMatch.IntegerRange
        header: str
        invert_match: bool

        def __init__(self, exact_match: _Optional[str]=..., regex_match: _Optional[str]=..., prefix_match: _Optional[str]=..., present_match: bool=..., suffix_match: _Optional[str]=..., range_match: _Optional[_Union[HttpRoute.HeaderMatch.IntegerRange, _Mapping]]=..., header: _Optional[str]=..., invert_match: bool=...) -> None:
            ...

    class QueryParameterMatch(_message.Message):
        __slots__ = ('exact_match', 'regex_match', 'present_match', 'query_parameter')
        EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
        REGEX_MATCH_FIELD_NUMBER: _ClassVar[int]
        PRESENT_MATCH_FIELD_NUMBER: _ClassVar[int]
        QUERY_PARAMETER_FIELD_NUMBER: _ClassVar[int]
        exact_match: str
        regex_match: str
        present_match: bool
        query_parameter: str

        def __init__(self, exact_match: _Optional[str]=..., regex_match: _Optional[str]=..., present_match: bool=..., query_parameter: _Optional[str]=...) -> None:
            ...

    class RouteMatch(_message.Message):
        __slots__ = ('full_path_match', 'prefix_match', 'regex_match', 'ignore_case', 'headers', 'query_parameters')
        FULL_PATH_MATCH_FIELD_NUMBER: _ClassVar[int]
        PREFIX_MATCH_FIELD_NUMBER: _ClassVar[int]
        REGEX_MATCH_FIELD_NUMBER: _ClassVar[int]
        IGNORE_CASE_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        QUERY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        full_path_match: str
        prefix_match: str
        regex_match: str
        ignore_case: bool
        headers: _containers.RepeatedCompositeFieldContainer[HttpRoute.HeaderMatch]
        query_parameters: _containers.RepeatedCompositeFieldContainer[HttpRoute.QueryParameterMatch]

        def __init__(self, full_path_match: _Optional[str]=..., prefix_match: _Optional[str]=..., regex_match: _Optional[str]=..., ignore_case: bool=..., headers: _Optional[_Iterable[_Union[HttpRoute.HeaderMatch, _Mapping]]]=..., query_parameters: _Optional[_Iterable[_Union[HttpRoute.QueryParameterMatch, _Mapping]]]=...) -> None:
            ...

    class Destination(_message.Message):
        __slots__ = ('service_name', 'weight')
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        weight: int

        def __init__(self, service_name: _Optional[str]=..., weight: _Optional[int]=...) -> None:
            ...

    class Redirect(_message.Message):
        __slots__ = ('host_redirect', 'path_redirect', 'prefix_rewrite', 'response_code', 'https_redirect', 'strip_query', 'port_redirect')

        class ResponseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESPONSE_CODE_UNSPECIFIED: _ClassVar[HttpRoute.Redirect.ResponseCode]
            MOVED_PERMANENTLY_DEFAULT: _ClassVar[HttpRoute.Redirect.ResponseCode]
            FOUND: _ClassVar[HttpRoute.Redirect.ResponseCode]
            SEE_OTHER: _ClassVar[HttpRoute.Redirect.ResponseCode]
            TEMPORARY_REDIRECT: _ClassVar[HttpRoute.Redirect.ResponseCode]
            PERMANENT_REDIRECT: _ClassVar[HttpRoute.Redirect.ResponseCode]
        RESPONSE_CODE_UNSPECIFIED: HttpRoute.Redirect.ResponseCode
        MOVED_PERMANENTLY_DEFAULT: HttpRoute.Redirect.ResponseCode
        FOUND: HttpRoute.Redirect.ResponseCode
        SEE_OTHER: HttpRoute.Redirect.ResponseCode
        TEMPORARY_REDIRECT: HttpRoute.Redirect.ResponseCode
        PERMANENT_REDIRECT: HttpRoute.Redirect.ResponseCode
        HOST_REDIRECT_FIELD_NUMBER: _ClassVar[int]
        PATH_REDIRECT_FIELD_NUMBER: _ClassVar[int]
        PREFIX_REWRITE_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
        HTTPS_REDIRECT_FIELD_NUMBER: _ClassVar[int]
        STRIP_QUERY_FIELD_NUMBER: _ClassVar[int]
        PORT_REDIRECT_FIELD_NUMBER: _ClassVar[int]
        host_redirect: str
        path_redirect: str
        prefix_rewrite: str
        response_code: HttpRoute.Redirect.ResponseCode
        https_redirect: bool
        strip_query: bool
        port_redirect: int

        def __init__(self, host_redirect: _Optional[str]=..., path_redirect: _Optional[str]=..., prefix_rewrite: _Optional[str]=..., response_code: _Optional[_Union[HttpRoute.Redirect.ResponseCode, str]]=..., https_redirect: bool=..., strip_query: bool=..., port_redirect: _Optional[int]=...) -> None:
            ...

    class FaultInjectionPolicy(_message.Message):
        __slots__ = ('delay', 'abort')

        class Delay(_message.Message):
            __slots__ = ('fixed_delay', 'percentage')
            FIXED_DELAY_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            fixed_delay: _duration_pb2.Duration
            percentage: int

            def __init__(self, fixed_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., percentage: _Optional[int]=...) -> None:
                ...

        class Abort(_message.Message):
            __slots__ = ('http_status', 'percentage')
            HTTP_STATUS_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            http_status: int
            percentage: int

            def __init__(self, http_status: _Optional[int]=..., percentage: _Optional[int]=...) -> None:
                ...
        DELAY_FIELD_NUMBER: _ClassVar[int]
        ABORT_FIELD_NUMBER: _ClassVar[int]
        delay: HttpRoute.FaultInjectionPolicy.Delay
        abort: HttpRoute.FaultInjectionPolicy.Abort

        def __init__(self, delay: _Optional[_Union[HttpRoute.FaultInjectionPolicy.Delay, _Mapping]]=..., abort: _Optional[_Union[HttpRoute.FaultInjectionPolicy.Abort, _Mapping]]=...) -> None:
            ...

    class HeaderModifier(_message.Message):
        __slots__ = ('set', 'add', 'remove')

        class SetEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...

        class AddEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        SET_FIELD_NUMBER: _ClassVar[int]
        ADD_FIELD_NUMBER: _ClassVar[int]
        REMOVE_FIELD_NUMBER: _ClassVar[int]
        set: _containers.ScalarMap[str, str]
        add: _containers.ScalarMap[str, str]
        remove: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, set: _Optional[_Mapping[str, str]]=..., add: _Optional[_Mapping[str, str]]=..., remove: _Optional[_Iterable[str]]=...) -> None:
            ...

    class URLRewrite(_message.Message):
        __slots__ = ('path_prefix_rewrite', 'host_rewrite')
        PATH_PREFIX_REWRITE_FIELD_NUMBER: _ClassVar[int]
        HOST_REWRITE_FIELD_NUMBER: _ClassVar[int]
        path_prefix_rewrite: str
        host_rewrite: str

        def __init__(self, path_prefix_rewrite: _Optional[str]=..., host_rewrite: _Optional[str]=...) -> None:
            ...

    class RetryPolicy(_message.Message):
        __slots__ = ('retry_conditions', 'num_retries', 'per_try_timeout')
        RETRY_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
        PER_TRY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        retry_conditions: _containers.RepeatedScalarFieldContainer[str]
        num_retries: int
        per_try_timeout: _duration_pb2.Duration

        def __init__(self, retry_conditions: _Optional[_Iterable[str]]=..., num_retries: _Optional[int]=..., per_try_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class RequestMirrorPolicy(_message.Message):
        __slots__ = ('destination',)
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        destination: HttpRoute.Destination

        def __init__(self, destination: _Optional[_Union[HttpRoute.Destination, _Mapping]]=...) -> None:
            ...

    class CorsPolicy(_message.Message):
        __slots__ = ('allow_origins', 'allow_origin_regexes', 'allow_methods', 'allow_headers', 'expose_headers', 'max_age', 'allow_credentials', 'disabled')
        ALLOW_ORIGINS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ORIGIN_REGEXES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_METHODS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_HEADERS_FIELD_NUMBER: _ClassVar[int]
        EXPOSE_HEADERS_FIELD_NUMBER: _ClassVar[int]
        MAX_AGE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        allow_origins: _containers.RepeatedScalarFieldContainer[str]
        allow_origin_regexes: _containers.RepeatedScalarFieldContainer[str]
        allow_methods: _containers.RepeatedScalarFieldContainer[str]
        allow_headers: _containers.RepeatedScalarFieldContainer[str]
        expose_headers: _containers.RepeatedScalarFieldContainer[str]
        max_age: str
        allow_credentials: bool
        disabled: bool

        def __init__(self, allow_origins: _Optional[_Iterable[str]]=..., allow_origin_regexes: _Optional[_Iterable[str]]=..., allow_methods: _Optional[_Iterable[str]]=..., allow_headers: _Optional[_Iterable[str]]=..., expose_headers: _Optional[_Iterable[str]]=..., max_age: _Optional[str]=..., allow_credentials: bool=..., disabled: bool=...) -> None:
            ...

    class RouteAction(_message.Message):
        __slots__ = ('destinations', 'redirect', 'fault_injection_policy', 'request_header_modifier', 'response_header_modifier', 'url_rewrite', 'timeout', 'retry_policy', 'request_mirror_policy', 'cors_policy')
        DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_FIELD_NUMBER: _ClassVar[int]
        FAULT_INJECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
        REQUEST_HEADER_MODIFIER_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_HEADER_MODIFIER_FIELD_NUMBER: _ClassVar[int]
        URL_REWRITE_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
        REQUEST_MIRROR_POLICY_FIELD_NUMBER: _ClassVar[int]
        CORS_POLICY_FIELD_NUMBER: _ClassVar[int]
        destinations: _containers.RepeatedCompositeFieldContainer[HttpRoute.Destination]
        redirect: HttpRoute.Redirect
        fault_injection_policy: HttpRoute.FaultInjectionPolicy
        request_header_modifier: HttpRoute.HeaderModifier
        response_header_modifier: HttpRoute.HeaderModifier
        url_rewrite: HttpRoute.URLRewrite
        timeout: _duration_pb2.Duration
        retry_policy: HttpRoute.RetryPolicy
        request_mirror_policy: HttpRoute.RequestMirrorPolicy
        cors_policy: HttpRoute.CorsPolicy

        def __init__(self, destinations: _Optional[_Iterable[_Union[HttpRoute.Destination, _Mapping]]]=..., redirect: _Optional[_Union[HttpRoute.Redirect, _Mapping]]=..., fault_injection_policy: _Optional[_Union[HttpRoute.FaultInjectionPolicy, _Mapping]]=..., request_header_modifier: _Optional[_Union[HttpRoute.HeaderModifier, _Mapping]]=..., response_header_modifier: _Optional[_Union[HttpRoute.HeaderModifier, _Mapping]]=..., url_rewrite: _Optional[_Union[HttpRoute.URLRewrite, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., retry_policy: _Optional[_Union[HttpRoute.RetryPolicy, _Mapping]]=..., request_mirror_policy: _Optional[_Union[HttpRoute.RequestMirrorPolicy, _Mapping]]=..., cors_policy: _Optional[_Union[HttpRoute.CorsPolicy, _Mapping]]=...) -> None:
            ...

    class RouteRule(_message.Message):
        __slots__ = ('matches', 'action')
        MATCHES_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        matches: _containers.RepeatedCompositeFieldContainer[HttpRoute.RouteMatch]
        action: HttpRoute.RouteAction

        def __init__(self, matches: _Optional[_Iterable[_Union[HttpRoute.RouteMatch, _Mapping]]]=..., action: _Optional[_Union[HttpRoute.RouteAction, _Mapping]]=...) -> None:
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
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAMES_FIELD_NUMBER: _ClassVar[int]
    MESHES_FIELD_NUMBER: _ClassVar[int]
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    self_link: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    hostnames: _containers.RepeatedScalarFieldContainer[str]
    meshes: _containers.RepeatedScalarFieldContainer[str]
    gateways: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.ScalarMap[str, str]
    rules: _containers.RepeatedCompositeFieldContainer[HttpRoute.RouteRule]

    def __init__(self, name: _Optional[str]=..., self_link: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., hostnames: _Optional[_Iterable[str]]=..., meshes: _Optional[_Iterable[str]]=..., gateways: _Optional[_Iterable[str]]=..., labels: _Optional[_Mapping[str, str]]=..., rules: _Optional[_Iterable[_Union[HttpRoute.RouteRule, _Mapping]]]=...) -> None:
        ...

class ListHttpRoutesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListHttpRoutesResponse(_message.Message):
    __slots__ = ('http_routes', 'next_page_token')
    HTTP_ROUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    http_routes: _containers.RepeatedCompositeFieldContainer[HttpRoute]
    next_page_token: str

    def __init__(self, http_routes: _Optional[_Iterable[_Union[HttpRoute, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetHttpRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateHttpRouteRequest(_message.Message):
    __slots__ = ('parent', 'http_route_id', 'http_route')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HTTP_ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    HTTP_ROUTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    http_route_id: str
    http_route: HttpRoute

    def __init__(self, parent: _Optional[str]=..., http_route_id: _Optional[str]=..., http_route: _Optional[_Union[HttpRoute, _Mapping]]=...) -> None:
        ...

class UpdateHttpRouteRequest(_message.Message):
    __slots__ = ('update_mask', 'http_route')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    HTTP_ROUTE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    http_route: HttpRoute

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., http_route: _Optional[_Union[HttpRoute, _Mapping]]=...) -> None:
        ...

class DeleteHttpRouteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...