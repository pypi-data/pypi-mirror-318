from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CallConversionReportingStateEnum(_message.Message):
    __slots__ = ()

    class CallConversionReportingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CallConversionReportingStateEnum.CallConversionReportingState]
        UNKNOWN: _ClassVar[CallConversionReportingStateEnum.CallConversionReportingState]
        DISABLED: _ClassVar[CallConversionReportingStateEnum.CallConversionReportingState]
        USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION: _ClassVar[CallConversionReportingStateEnum.CallConversionReportingState]
        USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION: _ClassVar[CallConversionReportingStateEnum.CallConversionReportingState]
    UNSPECIFIED: CallConversionReportingStateEnum.CallConversionReportingState
    UNKNOWN: CallConversionReportingStateEnum.CallConversionReportingState
    DISABLED: CallConversionReportingStateEnum.CallConversionReportingState
    USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION: CallConversionReportingStateEnum.CallConversionReportingState
    USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION: CallConversionReportingStateEnum.CallConversionReportingState

    def __init__(self) -> None:
        ...