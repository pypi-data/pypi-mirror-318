from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Configuration(_message.Message):
    __slots__ = ('name', 'id', 'status_attributes', 'configuration_attributes', 'properties', 'display_name')

    class Id(_message.Message):
        __slots__ = ('invocation_id', 'configuration_id')
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
        invocation_id: str
        configuration_id: str

        def __init__(self, invocation_id: _Optional[str]=..., configuration_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: Configuration.Id
    status_attributes: _common_pb2.StatusAttributes
    configuration_attributes: ConfigurationAttributes
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    display_name: str

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[Configuration.Id, _Mapping]]=..., status_attributes: _Optional[_Union[_common_pb2.StatusAttributes, _Mapping]]=..., configuration_attributes: _Optional[_Union[ConfigurationAttributes, _Mapping]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., display_name: _Optional[str]=...) -> None:
        ...

class ConfigurationAttributes(_message.Message):
    __slots__ = ('cpu',)
    CPU_FIELD_NUMBER: _ClassVar[int]
    cpu: str

    def __init__(self, cpu: _Optional[str]=...) -> None:
        ...