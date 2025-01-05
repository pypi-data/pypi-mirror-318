from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ScanRunWarningTrace(_message.Message):
    __slots__ = ('code',)

    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[ScanRunWarningTrace.Code]
        INSUFFICIENT_CRAWL_RESULTS: _ClassVar[ScanRunWarningTrace.Code]
        TOO_MANY_CRAWL_RESULTS: _ClassVar[ScanRunWarningTrace.Code]
        TOO_MANY_FUZZ_TASKS: _ClassVar[ScanRunWarningTrace.Code]
        BLOCKED_BY_IAP: _ClassVar[ScanRunWarningTrace.Code]
        NO_STARTING_URL_FOUND_FOR_MANAGED_SCAN: _ClassVar[ScanRunWarningTrace.Code]
    CODE_UNSPECIFIED: ScanRunWarningTrace.Code
    INSUFFICIENT_CRAWL_RESULTS: ScanRunWarningTrace.Code
    TOO_MANY_CRAWL_RESULTS: ScanRunWarningTrace.Code
    TOO_MANY_FUZZ_TASKS: ScanRunWarningTrace.Code
    BLOCKED_BY_IAP: ScanRunWarningTrace.Code
    NO_STARTING_URL_FOUND_FOR_MANAGED_SCAN: ScanRunWarningTrace.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: ScanRunWarningTrace.Code

    def __init__(self, code: _Optional[_Union[ScanRunWarningTrace.Code, str]]=...) -> None:
        ...