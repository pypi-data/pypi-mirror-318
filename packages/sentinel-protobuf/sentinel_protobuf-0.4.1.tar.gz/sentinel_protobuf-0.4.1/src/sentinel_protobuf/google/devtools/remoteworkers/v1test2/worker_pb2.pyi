from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Worker(_message.Message):
    __slots__ = ('devices', 'properties', 'configs')

    class Property(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class Config(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    properties: _containers.RepeatedCompositeFieldContainer[Worker.Property]
    configs: _containers.RepeatedCompositeFieldContainer[Worker.Config]

    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]]=..., properties: _Optional[_Iterable[_Union[Worker.Property, _Mapping]]]=..., configs: _Optional[_Iterable[_Union[Worker.Config, _Mapping]]]=...) -> None:
        ...

class Device(_message.Message):
    __slots__ = ('handle', 'properties')

    class Property(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    handle: str
    properties: _containers.RepeatedCompositeFieldContainer[Device.Property]

    def __init__(self, handle: _Optional[str]=..., properties: _Optional[_Iterable[_Union[Device.Property, _Mapping]]]=...) -> None:
        ...