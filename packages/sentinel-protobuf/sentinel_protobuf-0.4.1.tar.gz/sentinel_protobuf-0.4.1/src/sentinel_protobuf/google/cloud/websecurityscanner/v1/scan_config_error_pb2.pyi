from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScanConfigError(_message.Message):
    __slots__ = ('code', 'field_name')

    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[ScanConfigError.Code]
        OK: _ClassVar[ScanConfigError.Code]
        INTERNAL_ERROR: _ClassVar[ScanConfigError.Code]
        APPENGINE_API_BACKEND_ERROR: _ClassVar[ScanConfigError.Code]
        APPENGINE_API_NOT_ACCESSIBLE: _ClassVar[ScanConfigError.Code]
        APPENGINE_DEFAULT_HOST_MISSING: _ClassVar[ScanConfigError.Code]
        CANNOT_USE_GOOGLE_COM_ACCOUNT: _ClassVar[ScanConfigError.Code]
        CANNOT_USE_OWNER_ACCOUNT: _ClassVar[ScanConfigError.Code]
        COMPUTE_API_BACKEND_ERROR: _ClassVar[ScanConfigError.Code]
        COMPUTE_API_NOT_ACCESSIBLE: _ClassVar[ScanConfigError.Code]
        CUSTOM_LOGIN_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT: _ClassVar[ScanConfigError.Code]
        CUSTOM_LOGIN_URL_MALFORMED: _ClassVar[ScanConfigError.Code]
        CUSTOM_LOGIN_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS: _ClassVar[ScanConfigError.Code]
        CUSTOM_LOGIN_URL_MAPPED_TO_UNRESERVED_ADDRESS: _ClassVar[ScanConfigError.Code]
        CUSTOM_LOGIN_URL_HAS_NON_ROUTABLE_IP_ADDRESS: _ClassVar[ScanConfigError.Code]
        CUSTOM_LOGIN_URL_HAS_UNRESERVED_IP_ADDRESS: _ClassVar[ScanConfigError.Code]
        DUPLICATE_SCAN_NAME: _ClassVar[ScanConfigError.Code]
        INVALID_FIELD_VALUE: _ClassVar[ScanConfigError.Code]
        FAILED_TO_AUTHENTICATE_TO_TARGET: _ClassVar[ScanConfigError.Code]
        FINDING_TYPE_UNSPECIFIED: _ClassVar[ScanConfigError.Code]
        FORBIDDEN_TO_SCAN_COMPUTE: _ClassVar[ScanConfigError.Code]
        FORBIDDEN_UPDATE_TO_MANAGED_SCAN: _ClassVar[ScanConfigError.Code]
        MALFORMED_FILTER: _ClassVar[ScanConfigError.Code]
        MALFORMED_RESOURCE_NAME: _ClassVar[ScanConfigError.Code]
        PROJECT_INACTIVE: _ClassVar[ScanConfigError.Code]
        REQUIRED_FIELD: _ClassVar[ScanConfigError.Code]
        RESOURCE_NAME_INCONSISTENT: _ClassVar[ScanConfigError.Code]
        SCAN_ALREADY_RUNNING: _ClassVar[ScanConfigError.Code]
        SCAN_NOT_RUNNING: _ClassVar[ScanConfigError.Code]
        SEED_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT: _ClassVar[ScanConfigError.Code]
        SEED_URL_MALFORMED: _ClassVar[ScanConfigError.Code]
        SEED_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS: _ClassVar[ScanConfigError.Code]
        SEED_URL_MAPPED_TO_UNRESERVED_ADDRESS: _ClassVar[ScanConfigError.Code]
        SEED_URL_HAS_NON_ROUTABLE_IP_ADDRESS: _ClassVar[ScanConfigError.Code]
        SEED_URL_HAS_UNRESERVED_IP_ADDRESS: _ClassVar[ScanConfigError.Code]
        SERVICE_ACCOUNT_NOT_CONFIGURED: _ClassVar[ScanConfigError.Code]
        TOO_MANY_SCANS: _ClassVar[ScanConfigError.Code]
        UNABLE_TO_RESOLVE_PROJECT_INFO: _ClassVar[ScanConfigError.Code]
        UNSUPPORTED_BLACKLIST_PATTERN_FORMAT: _ClassVar[ScanConfigError.Code]
        UNSUPPORTED_FILTER: _ClassVar[ScanConfigError.Code]
        UNSUPPORTED_FINDING_TYPE: _ClassVar[ScanConfigError.Code]
        UNSUPPORTED_URL_SCHEME: _ClassVar[ScanConfigError.Code]
    CODE_UNSPECIFIED: ScanConfigError.Code
    OK: ScanConfigError.Code
    INTERNAL_ERROR: ScanConfigError.Code
    APPENGINE_API_BACKEND_ERROR: ScanConfigError.Code
    APPENGINE_API_NOT_ACCESSIBLE: ScanConfigError.Code
    APPENGINE_DEFAULT_HOST_MISSING: ScanConfigError.Code
    CANNOT_USE_GOOGLE_COM_ACCOUNT: ScanConfigError.Code
    CANNOT_USE_OWNER_ACCOUNT: ScanConfigError.Code
    COMPUTE_API_BACKEND_ERROR: ScanConfigError.Code
    COMPUTE_API_NOT_ACCESSIBLE: ScanConfigError.Code
    CUSTOM_LOGIN_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT: ScanConfigError.Code
    CUSTOM_LOGIN_URL_MALFORMED: ScanConfigError.Code
    CUSTOM_LOGIN_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS: ScanConfigError.Code
    CUSTOM_LOGIN_URL_MAPPED_TO_UNRESERVED_ADDRESS: ScanConfigError.Code
    CUSTOM_LOGIN_URL_HAS_NON_ROUTABLE_IP_ADDRESS: ScanConfigError.Code
    CUSTOM_LOGIN_URL_HAS_UNRESERVED_IP_ADDRESS: ScanConfigError.Code
    DUPLICATE_SCAN_NAME: ScanConfigError.Code
    INVALID_FIELD_VALUE: ScanConfigError.Code
    FAILED_TO_AUTHENTICATE_TO_TARGET: ScanConfigError.Code
    FINDING_TYPE_UNSPECIFIED: ScanConfigError.Code
    FORBIDDEN_TO_SCAN_COMPUTE: ScanConfigError.Code
    FORBIDDEN_UPDATE_TO_MANAGED_SCAN: ScanConfigError.Code
    MALFORMED_FILTER: ScanConfigError.Code
    MALFORMED_RESOURCE_NAME: ScanConfigError.Code
    PROJECT_INACTIVE: ScanConfigError.Code
    REQUIRED_FIELD: ScanConfigError.Code
    RESOURCE_NAME_INCONSISTENT: ScanConfigError.Code
    SCAN_ALREADY_RUNNING: ScanConfigError.Code
    SCAN_NOT_RUNNING: ScanConfigError.Code
    SEED_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT: ScanConfigError.Code
    SEED_URL_MALFORMED: ScanConfigError.Code
    SEED_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS: ScanConfigError.Code
    SEED_URL_MAPPED_TO_UNRESERVED_ADDRESS: ScanConfigError.Code
    SEED_URL_HAS_NON_ROUTABLE_IP_ADDRESS: ScanConfigError.Code
    SEED_URL_HAS_UNRESERVED_IP_ADDRESS: ScanConfigError.Code
    SERVICE_ACCOUNT_NOT_CONFIGURED: ScanConfigError.Code
    TOO_MANY_SCANS: ScanConfigError.Code
    UNABLE_TO_RESOLVE_PROJECT_INFO: ScanConfigError.Code
    UNSUPPORTED_BLACKLIST_PATTERN_FORMAT: ScanConfigError.Code
    UNSUPPORTED_FILTER: ScanConfigError.Code
    UNSUPPORTED_FINDING_TYPE: ScanConfigError.Code
    UNSUPPORTED_URL_SCHEME: ScanConfigError.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    code: ScanConfigError.Code
    field_name: str

    def __init__(self, code: _Optional[_Union[ScanConfigError.Code, str]]=..., field_name: _Optional[str]=...) -> None:
        ...