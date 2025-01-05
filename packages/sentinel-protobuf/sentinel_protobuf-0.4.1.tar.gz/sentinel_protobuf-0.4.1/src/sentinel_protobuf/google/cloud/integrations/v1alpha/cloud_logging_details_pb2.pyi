from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudLoggingDetails(_message.Message):
    __slots__ = ("cloud_logging_severity", "enable_cloud_logging")
    class CloudLoggingSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLOUD_LOGGING_SEVERITY_UNSPECIFIED: _ClassVar[CloudLoggingDetails.CloudLoggingSeverity]
        INFO: _ClassVar[CloudLoggingDetails.CloudLoggingSeverity]
        ERROR: _ClassVar[CloudLoggingDetails.CloudLoggingSeverity]
        WARNING: _ClassVar[CloudLoggingDetails.CloudLoggingSeverity]
    CLOUD_LOGGING_SEVERITY_UNSPECIFIED: CloudLoggingDetails.CloudLoggingSeverity
    INFO: CloudLoggingDetails.CloudLoggingSeverity
    ERROR: CloudLoggingDetails.CloudLoggingSeverity
    WARNING: CloudLoggingDetails.CloudLoggingSeverity
    CLOUD_LOGGING_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CLOUD_LOGGING_FIELD_NUMBER: _ClassVar[int]
    cloud_logging_severity: CloudLoggingDetails.CloudLoggingSeverity
    enable_cloud_logging: bool
    def __init__(self, cloud_logging_severity: _Optional[_Union[CloudLoggingDetails.CloudLoggingSeverity, str]] = ..., enable_cloud_logging: bool = ...) -> None: ...
