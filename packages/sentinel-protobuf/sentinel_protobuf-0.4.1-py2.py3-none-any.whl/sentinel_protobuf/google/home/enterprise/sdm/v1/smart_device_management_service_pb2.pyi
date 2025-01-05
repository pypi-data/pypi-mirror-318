from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.home.enterprise.sdm.v1 import device_pb2 as _device_pb2
from google.home.enterprise.sdm.v1 import site_pb2 as _site_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetDeviceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDevicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListDevicesResponse(_message.Message):
    __slots__ = ('devices', 'next_page_token')
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]
    next_page_token: str

    def __init__(self, devices: _Optional[_Iterable[_Union[_device_pb2.Device, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ExecuteDeviceCommandRequest(_message.Message):
    __slots__ = ('name', 'command', 'params')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    command: str
    params: _struct_pb2.Struct

    def __init__(self, name: _Optional[str]=..., command: _Optional[str]=..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class ExecuteDeviceCommandResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _struct_pb2.Struct

    def __init__(self, results: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class GetStructureRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListStructuresRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListStructuresResponse(_message.Message):
    __slots__ = ('structures', 'next_page_token')
    STRUCTURES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    structures: _containers.RepeatedCompositeFieldContainer[_site_pb2.Structure]
    next_page_token: str

    def __init__(self, structures: _Optional[_Iterable[_Union[_site_pb2.Structure, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRoomRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRoomsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRoomsResponse(_message.Message):
    __slots__ = ('rooms', 'next_page_token')
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[_site_pb2.Room]
    next_page_token: str

    def __init__(self, rooms: _Optional[_Iterable[_Union[_site_pb2.Room, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...