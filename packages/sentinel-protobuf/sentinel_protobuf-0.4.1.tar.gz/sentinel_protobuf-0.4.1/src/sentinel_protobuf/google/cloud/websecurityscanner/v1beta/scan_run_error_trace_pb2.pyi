from google.cloud.websecurityscanner.v1beta import scan_config_error_pb2 as _scan_config_error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScanRunErrorTrace(_message.Message):
    __slots__ = ('code', 'scan_config_error', 'most_common_http_error_code')

    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[ScanRunErrorTrace.Code]
        INTERNAL_ERROR: _ClassVar[ScanRunErrorTrace.Code]
        SCAN_CONFIG_ISSUE: _ClassVar[ScanRunErrorTrace.Code]
        AUTHENTICATION_CONFIG_ISSUE: _ClassVar[ScanRunErrorTrace.Code]
        TIMED_OUT_WHILE_SCANNING: _ClassVar[ScanRunErrorTrace.Code]
        TOO_MANY_REDIRECTS: _ClassVar[ScanRunErrorTrace.Code]
        TOO_MANY_HTTP_ERRORS: _ClassVar[ScanRunErrorTrace.Code]
    CODE_UNSPECIFIED: ScanRunErrorTrace.Code
    INTERNAL_ERROR: ScanRunErrorTrace.Code
    SCAN_CONFIG_ISSUE: ScanRunErrorTrace.Code
    AUTHENTICATION_CONFIG_ISSUE: ScanRunErrorTrace.Code
    TIMED_OUT_WHILE_SCANNING: ScanRunErrorTrace.Code
    TOO_MANY_REDIRECTS: ScanRunErrorTrace.Code
    TOO_MANY_HTTP_ERRORS: ScanRunErrorTrace.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    SCAN_CONFIG_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOST_COMMON_HTTP_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    code: ScanRunErrorTrace.Code
    scan_config_error: _scan_config_error_pb2.ScanConfigError
    most_common_http_error_code: int

    def __init__(self, code: _Optional[_Union[ScanRunErrorTrace.Code, str]]=..., scan_config_error: _Optional[_Union[_scan_config_error_pb2.ScanConfigError, _Mapping]]=..., most_common_http_error_code: _Optional[int]=...) -> None:
        ...