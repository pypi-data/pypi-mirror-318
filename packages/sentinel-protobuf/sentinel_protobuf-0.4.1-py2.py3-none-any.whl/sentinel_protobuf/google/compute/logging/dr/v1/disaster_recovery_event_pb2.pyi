from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisasterRecoveryEvent(_message.Message):
    __slots__ = ("severity", "details")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[DisasterRecoveryEvent.Severity]
        ACTION_REQUIRED: _ClassVar[DisasterRecoveryEvent.Severity]
        ACTION_SUGGESTED: _ClassVar[DisasterRecoveryEvent.Severity]
        NOTICE: _ClassVar[DisasterRecoveryEvent.Severity]
    SEVERITY_UNSPECIFIED: DisasterRecoveryEvent.Severity
    ACTION_REQUIRED: DisasterRecoveryEvent.Severity
    ACTION_SUGGESTED: DisasterRecoveryEvent.Severity
    NOTICE: DisasterRecoveryEvent.Severity
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    severity: DisasterRecoveryEvent.Severity
    details: str
    def __init__(self, severity: _Optional[_Union[DisasterRecoveryEvent.Severity, str]] = ..., details: _Optional[str] = ...) -> None: ...
