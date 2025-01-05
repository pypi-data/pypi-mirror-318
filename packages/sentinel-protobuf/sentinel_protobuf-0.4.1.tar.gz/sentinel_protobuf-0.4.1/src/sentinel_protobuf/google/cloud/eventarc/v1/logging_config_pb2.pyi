from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoggingConfig(_message.Message):
    __slots__ = ('log_severity',)

    class LogSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_SEVERITY_UNSPECIFIED: _ClassVar[LoggingConfig.LogSeverity]
        NONE: _ClassVar[LoggingConfig.LogSeverity]
        DEBUG: _ClassVar[LoggingConfig.LogSeverity]
        INFO: _ClassVar[LoggingConfig.LogSeverity]
        NOTICE: _ClassVar[LoggingConfig.LogSeverity]
        WARNING: _ClassVar[LoggingConfig.LogSeverity]
        ERROR: _ClassVar[LoggingConfig.LogSeverity]
        CRITICAL: _ClassVar[LoggingConfig.LogSeverity]
        ALERT: _ClassVar[LoggingConfig.LogSeverity]
        EMERGENCY: _ClassVar[LoggingConfig.LogSeverity]
    LOG_SEVERITY_UNSPECIFIED: LoggingConfig.LogSeverity
    NONE: LoggingConfig.LogSeverity
    DEBUG: LoggingConfig.LogSeverity
    INFO: LoggingConfig.LogSeverity
    NOTICE: LoggingConfig.LogSeverity
    WARNING: LoggingConfig.LogSeverity
    ERROR: LoggingConfig.LogSeverity
    CRITICAL: LoggingConfig.LogSeverity
    ALERT: LoggingConfig.LogSeverity
    EMERGENCY: LoggingConfig.LogSeverity
    LOG_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    log_severity: LoggingConfig.LogSeverity

    def __init__(self, log_severity: _Optional[_Union[LoggingConfig.LogSeverity, str]]=...) -> None:
        ...