from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LogEntry(_message.Message):
    __slots__ = ('cloud_logging_entry',)
    CLOUD_LOGGING_ENTRY_FIELD_NUMBER: _ClassVar[int]
    cloud_logging_entry: CloudLoggingEntry

    def __init__(self, cloud_logging_entry: _Optional[_Union[CloudLoggingEntry, _Mapping]]=...) -> None:
        ...

class CloudLoggingEntry(_message.Message):
    __slots__ = ('insert_id', 'log_id', 'resource_container', 'timestamp')
    INSERT_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    insert_id: str
    log_id: str
    resource_container: str
    timestamp: _timestamp_pb2.Timestamp

    def __init__(self, insert_id: _Optional[str]=..., log_id: _Optional[str]=..., resource_container: _Optional[str]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...