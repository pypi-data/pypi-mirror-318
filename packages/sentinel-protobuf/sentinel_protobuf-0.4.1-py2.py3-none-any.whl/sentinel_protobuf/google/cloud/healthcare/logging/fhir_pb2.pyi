from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImportFhirLogEntry(_message.Message):
    __slots__ = ('source', 'resource_id', 'error')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    source: str
    resource_id: str
    error: _status_pb2.Status

    def __init__(self, source: _Optional[str]=..., resource_id: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ExportFhirLogEntry(_message.Message):
    __slots__ = ('destination', 'resource_name', 'error')
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    destination: str
    resource_name: str
    error: _status_pb2.Status

    def __init__(self, destination: _Optional[str]=..., resource_name: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class FhirConfigureSearchLogEntry(_message.Message):
    __slots__ = ('resource_id', 'error')
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    error: _status_pb2.Status

    def __init__(self, resource_id: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class FhirNotificationLogEntry(_message.Message):
    __slots__ = ('resource_name', 'pubsub_topic', 'error')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    pubsub_topic: str
    error: _status_pb2.Status

    def __init__(self, resource_name: _Optional[str]=..., pubsub_topic: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class FhirStreamLogEntry(_message.Message):
    __slots__ = ('resource_name', 'destination', 'error')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    destination: str
    error: _status_pb2.Status

    def __init__(self, resource_name: _Optional[str]=..., destination: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class FhirDeidentifyStreamToStoreLogEntry(_message.Message):
    __slots__ = ('resource_name', 'destination', 'error')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    destination: str
    error: _status_pb2.Status

    def __init__(self, resource_name: _Optional[str]=..., destination: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...