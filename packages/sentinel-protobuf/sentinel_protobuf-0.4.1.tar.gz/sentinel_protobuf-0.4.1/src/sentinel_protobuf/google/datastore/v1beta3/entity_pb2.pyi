from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PartitionId(_message.Message):
    __slots__ = ('project_id', 'namespace_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    namespace_id: str

    def __init__(self, project_id: _Optional[str]=..., namespace_id: _Optional[str]=...) -> None:
        ...

class Key(_message.Message):
    __slots__ = ('partition_id', 'path')

    class PathElement(_message.Message):
        __slots__ = ('kind', 'id', 'name')
        KIND_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        kind: str
        id: int
        name: str

        def __init__(self, kind: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=...) -> None:
            ...
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    partition_id: PartitionId
    path: _containers.RepeatedCompositeFieldContainer[Key.PathElement]

    def __init__(self, partition_id: _Optional[_Union[PartitionId, _Mapping]]=..., path: _Optional[_Iterable[_Union[Key.PathElement, _Mapping]]]=...) -> None:
        ...

class ArrayValue(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Value]

    def __init__(self, values: _Optional[_Iterable[_Union[Value, _Mapping]]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('null_value', 'boolean_value', 'integer_value', 'double_value', 'timestamp_value', 'key_value', 'string_value', 'blob_value', 'geo_point_value', 'entity_value', 'array_value', 'meaning', 'exclude_from_indexes')
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BLOB_VALUE_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    MEANING_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FROM_INDEXES_FIELD_NUMBER: _ClassVar[int]
    null_value: _struct_pb2.NullValue
    boolean_value: bool
    integer_value: int
    double_value: float
    timestamp_value: _timestamp_pb2.Timestamp
    key_value: Key
    string_value: str
    blob_value: bytes
    geo_point_value: _latlng_pb2.LatLng
    entity_value: Entity
    array_value: ArrayValue
    meaning: int
    exclude_from_indexes: bool

    def __init__(self, null_value: _Optional[_Union[_struct_pb2.NullValue, str]]=..., boolean_value: bool=..., integer_value: _Optional[int]=..., double_value: _Optional[float]=..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., key_value: _Optional[_Union[Key, _Mapping]]=..., string_value: _Optional[str]=..., blob_value: _Optional[bytes]=..., geo_point_value: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., entity_value: _Optional[_Union[Entity, _Mapping]]=..., array_value: _Optional[_Union[ArrayValue, _Mapping]]=..., meaning: _Optional[int]=..., exclude_from_indexes: bool=...) -> None:
        ...

class Entity(_message.Message):
    __slots__ = ('key', 'properties')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Value, _Mapping]]=...) -> None:
            ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    key: Key
    properties: _containers.MessageMap[str, Value]

    def __init__(self, key: _Optional[_Union[Key, _Mapping]]=..., properties: _Optional[_Mapping[str, Value]]=...) -> None:
        ...