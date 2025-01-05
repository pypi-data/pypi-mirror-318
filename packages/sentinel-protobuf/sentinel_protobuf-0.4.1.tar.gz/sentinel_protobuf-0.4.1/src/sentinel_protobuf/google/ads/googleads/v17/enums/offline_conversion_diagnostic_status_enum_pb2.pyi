from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineConversionDiagnosticStatusEnum(_message.Message):
    __slots__ = ()

    class OfflineConversionDiagnosticStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus]
        UNKNOWN: _ClassVar[OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus]
        EXCELLENT: _ClassVar[OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus]
        GOOD: _ClassVar[OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus]
        NEEDS_ATTENTION: _ClassVar[OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus]
        NO_RECENT_UPLOAD: _ClassVar[OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus]
    UNSPECIFIED: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    UNKNOWN: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    EXCELLENT: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    GOOD: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    NEEDS_ATTENTION: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    NO_RECENT_UPLOAD: OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus

    def __init__(self) -> None:
        ...