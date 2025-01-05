
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ['golang_bindings', 'modules']
    GOLANG_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    golang_bindings: _containers.RepeatedCompositeFieldContainer[GolangBinding]
    modules: _containers.RepeatedCompositeFieldContainer[ModuleConfig]

    def __init__(self, modules: _Optional[_Iterable[_Union[(ModuleConfig, _Mapping)]]]=..., golang_bindings: _Optional[_Iterable[_Union[(GolangBinding, _Mapping)]]]=...) -> None:
        ...

class GolangBinding(_message.Message):
    __slots__ = ['implementation', 'interface_type']
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    implementation: str
    interface_type: str

    def __init__(self, interface_type: _Optional[str]=..., implementation: _Optional[str]=...) -> None:
        ...

class ModuleConfig(_message.Message):
    __slots__ = ['config', 'golang_bindings', 'name']
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    GOLANG_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    config: _any_pb2.Any
    golang_bindings: _containers.RepeatedCompositeFieldContainer[GolangBinding]
    name: str

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[(_any_pb2.Any, _Mapping)]]=..., golang_bindings: _Optional[_Iterable[_Union[(GolangBinding, _Mapping)]]]=...) -> None:
        ...
