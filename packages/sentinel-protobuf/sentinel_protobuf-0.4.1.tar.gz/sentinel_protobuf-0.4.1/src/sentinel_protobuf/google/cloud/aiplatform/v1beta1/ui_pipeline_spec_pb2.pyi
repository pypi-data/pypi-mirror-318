from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import value_pb2 as _value_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ArtifactTypeSchema(_message.Message):
    __slots__ = ('schema_title', 'schema_uri', 'instance_schema', 'schema_version')
    SCHEMA_TITLE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    schema_title: str
    schema_uri: str
    instance_schema: str
    schema_version: str

    def __init__(self, schema_title: _Optional[str]=..., schema_uri: _Optional[str]=..., instance_schema: _Optional[str]=..., schema_version: _Optional[str]=...) -> None:
        ...

class RuntimeArtifact(_message.Message):
    __slots__ = ('name', 'type', 'uri', 'properties', 'custom_properties', 'metadata')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _value_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_value_pb2.Value, _Mapping]]=...) -> None:
            ...

    class CustomPropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _value_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_value_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: ArtifactTypeSchema
    uri: str
    properties: _containers.MessageMap[str, _value_pb2.Value]
    custom_properties: _containers.MessageMap[str, _value_pb2.Value]
    metadata: _struct_pb2.Struct

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[ArtifactTypeSchema, _Mapping]]=..., uri: _Optional[str]=..., properties: _Optional[_Mapping[str, _value_pb2.Value]]=..., custom_properties: _Optional[_Mapping[str, _value_pb2.Value]]=..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...