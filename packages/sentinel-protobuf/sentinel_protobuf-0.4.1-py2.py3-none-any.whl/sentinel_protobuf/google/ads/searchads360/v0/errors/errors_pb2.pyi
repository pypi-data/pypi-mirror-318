from google.ads.searchads360.v0.common import value_pb2 as _value_pb2
from google.ads.searchads360.v0.errors import authentication_error_pb2 as _authentication_error_pb2
from google.ads.searchads360.v0.errors import authorization_error_pb2 as _authorization_error_pb2
from google.ads.searchads360.v0.errors import custom_column_error_pb2 as _custom_column_error_pb2
from google.ads.searchads360.v0.errors import date_error_pb2 as _date_error_pb2
from google.ads.searchads360.v0.errors import date_range_error_pb2 as _date_range_error_pb2
from google.ads.searchads360.v0.errors import distinct_error_pb2 as _distinct_error_pb2
from google.ads.searchads360.v0.errors import header_error_pb2 as _header_error_pb2
from google.ads.searchads360.v0.errors import internal_error_pb2 as _internal_error_pb2
from google.ads.searchads360.v0.errors import invalid_parameter_error_pb2 as _invalid_parameter_error_pb2
from google.ads.searchads360.v0.errors import query_error_pb2 as _query_error_pb2
from google.ads.searchads360.v0.errors import quota_error_pb2 as _quota_error_pb2
from google.ads.searchads360.v0.errors import request_error_pb2 as _request_error_pb2
from google.ads.searchads360.v0.errors import size_limit_error_pb2 as _size_limit_error_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchAds360Failure(_message.Message):
    __slots__ = ("errors", "request_id")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[SearchAds360Error]
    request_id: str
    def __init__(self, errors: _Optional[_Iterable[_Union[SearchAds360Error, _Mapping]]] = ..., request_id: _Optional[str] = ...) -> None: ...

class SearchAds360Error(_message.Message):
    __slots__ = ("error_code", "message", "trigger", "location", "details")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    error_code: ErrorCode
    message: str
    trigger: _value_pb2.Value
    location: ErrorLocation
    details: ErrorDetails
    def __init__(self, error_code: _Optional[_Union[ErrorCode, _Mapping]] = ..., message: _Optional[str] = ..., trigger: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., location: _Optional[_Union[ErrorLocation, _Mapping]] = ..., details: _Optional[_Union[ErrorDetails, _Mapping]] = ...) -> None: ...

class ErrorCode(_message.Message):
    __slots__ = ("request_error", "query_error", "authorization_error", "internal_error", "quota_error", "authentication_error", "date_error", "date_range_error", "distinct_error", "header_error", "size_limit_error", "custom_column_error", "invalid_parameter_error")
    REQUEST_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUERY_ERROR_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUOTA_ERROR_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    DATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_ERROR_FIELD_NUMBER: _ClassVar[int]
    HEADER_ERROR_FIELD_NUMBER: _ClassVar[int]
    SIZE_LIMIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLUMN_ERROR_FIELD_NUMBER: _ClassVar[int]
    INVALID_PARAMETER_ERROR_FIELD_NUMBER: _ClassVar[int]
    request_error: _request_error_pb2.RequestErrorEnum.RequestError
    query_error: _query_error_pb2.QueryErrorEnum.QueryError
    authorization_error: _authorization_error_pb2.AuthorizationErrorEnum.AuthorizationError
    internal_error: _internal_error_pb2.InternalErrorEnum.InternalError
    quota_error: _quota_error_pb2.QuotaErrorEnum.QuotaError
    authentication_error: _authentication_error_pb2.AuthenticationErrorEnum.AuthenticationError
    date_error: _date_error_pb2.DateErrorEnum.DateError
    date_range_error: _date_range_error_pb2.DateRangeErrorEnum.DateRangeError
    distinct_error: _distinct_error_pb2.DistinctErrorEnum.DistinctError
    header_error: _header_error_pb2.HeaderErrorEnum.HeaderError
    size_limit_error: _size_limit_error_pb2.SizeLimitErrorEnum.SizeLimitError
    custom_column_error: _custom_column_error_pb2.CustomColumnErrorEnum.CustomColumnError
    invalid_parameter_error: _invalid_parameter_error_pb2.InvalidParameterErrorEnum.InvalidParameterError
    def __init__(self, request_error: _Optional[_Union[_request_error_pb2.RequestErrorEnum.RequestError, str]] = ..., query_error: _Optional[_Union[_query_error_pb2.QueryErrorEnum.QueryError, str]] = ..., authorization_error: _Optional[_Union[_authorization_error_pb2.AuthorizationErrorEnum.AuthorizationError, str]] = ..., internal_error: _Optional[_Union[_internal_error_pb2.InternalErrorEnum.InternalError, str]] = ..., quota_error: _Optional[_Union[_quota_error_pb2.QuotaErrorEnum.QuotaError, str]] = ..., authentication_error: _Optional[_Union[_authentication_error_pb2.AuthenticationErrorEnum.AuthenticationError, str]] = ..., date_error: _Optional[_Union[_date_error_pb2.DateErrorEnum.DateError, str]] = ..., date_range_error: _Optional[_Union[_date_range_error_pb2.DateRangeErrorEnum.DateRangeError, str]] = ..., distinct_error: _Optional[_Union[_distinct_error_pb2.DistinctErrorEnum.DistinctError, str]] = ..., header_error: _Optional[_Union[_header_error_pb2.HeaderErrorEnum.HeaderError, str]] = ..., size_limit_error: _Optional[_Union[_size_limit_error_pb2.SizeLimitErrorEnum.SizeLimitError, str]] = ..., custom_column_error: _Optional[_Union[_custom_column_error_pb2.CustomColumnErrorEnum.CustomColumnError, str]] = ..., invalid_parameter_error: _Optional[_Union[_invalid_parameter_error_pb2.InvalidParameterErrorEnum.InvalidParameterError, str]] = ...) -> None: ...

class ErrorLocation(_message.Message):
    __slots__ = ("field_path_elements",)
    class FieldPathElement(_message.Message):
        __slots__ = ("field_name", "index")
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        index: int
        def __init__(self, field_name: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...
    FIELD_PATH_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    field_path_elements: _containers.RepeatedCompositeFieldContainer[ErrorLocation.FieldPathElement]
    def __init__(self, field_path_elements: _Optional[_Iterable[_Union[ErrorLocation.FieldPathElement, _Mapping]]] = ...) -> None: ...

class ErrorDetails(_message.Message):
    __slots__ = ("unpublished_error_code", "quota_error_details")
    UNPUBLISHED_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    QUOTA_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    unpublished_error_code: str
    quota_error_details: QuotaErrorDetails
    def __init__(self, unpublished_error_code: _Optional[str] = ..., quota_error_details: _Optional[_Union[QuotaErrorDetails, _Mapping]] = ...) -> None: ...

class QuotaErrorDetails(_message.Message):
    __slots__ = ("rate_scope", "rate_name", "retry_delay")
    class QuotaRateScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[QuotaErrorDetails.QuotaRateScope]
        UNKNOWN: _ClassVar[QuotaErrorDetails.QuotaRateScope]
        ACCOUNT: _ClassVar[QuotaErrorDetails.QuotaRateScope]
        DEVELOPER: _ClassVar[QuotaErrorDetails.QuotaRateScope]
    UNSPECIFIED: QuotaErrorDetails.QuotaRateScope
    UNKNOWN: QuotaErrorDetails.QuotaRateScope
    ACCOUNT: QuotaErrorDetails.QuotaRateScope
    DEVELOPER: QuotaErrorDetails.QuotaRateScope
    RATE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    RATE_NAME_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    rate_scope: QuotaErrorDetails.QuotaRateScope
    rate_name: str
    retry_delay: _duration_pb2.Duration
    def __init__(self, rate_scope: _Optional[_Union[QuotaErrorDetails.QuotaRateScope, str]] = ..., rate_name: _Optional[str] = ..., retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
