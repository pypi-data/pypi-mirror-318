from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RequestErrorEnum(_message.Message):
    __slots__ = ()

    class RequestError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[RequestErrorEnum.RequestError]
        UNKNOWN: _ClassVar[RequestErrorEnum.RequestError]
        RESOURCE_NAME_MISSING: _ClassVar[RequestErrorEnum.RequestError]
        RESOURCE_NAME_MALFORMED: _ClassVar[RequestErrorEnum.RequestError]
        BAD_RESOURCE_ID: _ClassVar[RequestErrorEnum.RequestError]
        INVALID_CUSTOMER_ID: _ClassVar[RequestErrorEnum.RequestError]
        OPERATION_REQUIRED: _ClassVar[RequestErrorEnum.RequestError]
        RESOURCE_NOT_FOUND: _ClassVar[RequestErrorEnum.RequestError]
        INVALID_PAGE_TOKEN: _ClassVar[RequestErrorEnum.RequestError]
        EXPIRED_PAGE_TOKEN: _ClassVar[RequestErrorEnum.RequestError]
        INVALID_PAGE_SIZE: _ClassVar[RequestErrorEnum.RequestError]
        PAGE_SIZE_NOT_SUPPORTED: _ClassVar[RequestErrorEnum.RequestError]
        REQUIRED_FIELD_MISSING: _ClassVar[RequestErrorEnum.RequestError]
        IMMUTABLE_FIELD: _ClassVar[RequestErrorEnum.RequestError]
        TOO_MANY_MUTATE_OPERATIONS: _ClassVar[RequestErrorEnum.RequestError]
        CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT: _ClassVar[RequestErrorEnum.RequestError]
        CANNOT_MODIFY_FOREIGN_FIELD: _ClassVar[RequestErrorEnum.RequestError]
        INVALID_ENUM_VALUE: _ClassVar[RequestErrorEnum.RequestError]
        DEVELOPER_TOKEN_PARAMETER_MISSING: _ClassVar[RequestErrorEnum.RequestError]
        LOGIN_CUSTOMER_ID_PARAMETER_MISSING: _ClassVar[RequestErrorEnum.RequestError]
        VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN: _ClassVar[RequestErrorEnum.RequestError]
        CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS: _ClassVar[RequestErrorEnum.RequestError]
        CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS: _ClassVar[RequestErrorEnum.RequestError]
        INCONSISTENT_RETURN_SUMMARY_ROW_VALUE: _ClassVar[RequestErrorEnum.RequestError]
        TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED: _ClassVar[RequestErrorEnum.RequestError]
        RPC_DEADLINE_TOO_SHORT: _ClassVar[RequestErrorEnum.RequestError]
        UNSUPPORTED_VERSION: _ClassVar[RequestErrorEnum.RequestError]
        CLOUD_PROJECT_NOT_FOUND: _ClassVar[RequestErrorEnum.RequestError]
    UNSPECIFIED: RequestErrorEnum.RequestError
    UNKNOWN: RequestErrorEnum.RequestError
    RESOURCE_NAME_MISSING: RequestErrorEnum.RequestError
    RESOURCE_NAME_MALFORMED: RequestErrorEnum.RequestError
    BAD_RESOURCE_ID: RequestErrorEnum.RequestError
    INVALID_CUSTOMER_ID: RequestErrorEnum.RequestError
    OPERATION_REQUIRED: RequestErrorEnum.RequestError
    RESOURCE_NOT_FOUND: RequestErrorEnum.RequestError
    INVALID_PAGE_TOKEN: RequestErrorEnum.RequestError
    EXPIRED_PAGE_TOKEN: RequestErrorEnum.RequestError
    INVALID_PAGE_SIZE: RequestErrorEnum.RequestError
    PAGE_SIZE_NOT_SUPPORTED: RequestErrorEnum.RequestError
    REQUIRED_FIELD_MISSING: RequestErrorEnum.RequestError
    IMMUTABLE_FIELD: RequestErrorEnum.RequestError
    TOO_MANY_MUTATE_OPERATIONS: RequestErrorEnum.RequestError
    CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT: RequestErrorEnum.RequestError
    CANNOT_MODIFY_FOREIGN_FIELD: RequestErrorEnum.RequestError
    INVALID_ENUM_VALUE: RequestErrorEnum.RequestError
    DEVELOPER_TOKEN_PARAMETER_MISSING: RequestErrorEnum.RequestError
    LOGIN_CUSTOMER_ID_PARAMETER_MISSING: RequestErrorEnum.RequestError
    VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN: RequestErrorEnum.RequestError
    CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS: RequestErrorEnum.RequestError
    CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS: RequestErrorEnum.RequestError
    INCONSISTENT_RETURN_SUMMARY_ROW_VALUE: RequestErrorEnum.RequestError
    TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED: RequestErrorEnum.RequestError
    RPC_DEADLINE_TOO_SHORT: RequestErrorEnum.RequestError
    UNSUPPORTED_VERSION: RequestErrorEnum.RequestError
    CLOUD_PROJECT_NOT_FOUND: RequestErrorEnum.RequestError

    def __init__(self) -> None:
        ...