from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DestinationConfig(_message.Message):
    __slots__ = ('key', 'destinations')
    KEY_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    key: str
    destinations: _containers.RepeatedCompositeFieldContainer[Destination]

    def __init__(self, key: _Optional[str]=..., destinations: _Optional[_Iterable[_Union[Destination, _Mapping]]]=...) -> None:
        ...

class Destination(_message.Message):
    __slots__ = ('service_attachment', 'host', 'port')
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    service_attachment: str
    host: str
    port: int

    def __init__(self, service_attachment: _Optional[str]=..., host: _Optional[str]=..., port: _Optional[int]=...) -> None:
        ...