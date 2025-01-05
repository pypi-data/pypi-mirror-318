from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImportDicomLogEntry(_message.Message):
    __slots__ = ('source', 'error')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    source: str
    error: _status_pb2.Status

    def __init__(self, source: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ExportDicomLogEntry(_message.Message):
    __slots__ = ('resource_name', 'error')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    error: _status_pb2.Status

    def __init__(self, resource_name: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class DicomNotificationLogEntry(_message.Message):
    __slots__ = ('resource_name', 'pubsub_topic', 'error')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    pubsub_topic: str
    error: _status_pb2.Status

    def __init__(self, resource_name: _Optional[str]=..., pubsub_topic: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class DicomStreamLogEntry(_message.Message):
    __slots__ = ('resource_name', 'destination', 'error')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    destination: str
    error: _status_pb2.Status

    def __init__(self, resource_name: _Optional[str]=..., destination: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...