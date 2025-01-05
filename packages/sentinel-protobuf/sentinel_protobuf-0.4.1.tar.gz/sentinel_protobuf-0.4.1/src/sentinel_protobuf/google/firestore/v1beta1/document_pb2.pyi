from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ('name', 'fields', 'create_time', 'update_time')

    class FieldsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    fields: _containers.MessageMap[str, Value]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., fields: _Optional[_Mapping[str, Value]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('null_value', 'boolean_value', 'integer_value', 'double_value', 'timestamp_value', 'string_value', 'bytes_value', 'reference_value', 'geo_point_value', 'array_value', 'map_value')
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    GEO_POINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    null_value: _struct_pb2.NullValue
    boolean_value: bool
    integer_value: int
    double_value: float
    timestamp_value: _timestamp_pb2.Timestamp
    string_value: str
    bytes_value: bytes
    reference_value: str
    geo_point_value: _latlng_pb2.LatLng
    array_value: ArrayValue
    map_value: MapValue

    def __init__(self, null_value: _Optional[_Union[_struct_pb2.NullValue, str]]=..., boolean_value: bool=..., integer_value: _Optional[int]=..., double_value: _Optional[float]=..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., string_value: _Optional[str]=..., bytes_value: _Optional[bytes]=..., reference_value: _Optional[str]=..., geo_point_value: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., array_value: _Optional[_Union[ArrayValue, _Mapping]]=..., map_value: _Optional[_Union[MapValue, _Mapping]]=...) -> None:
        ...

class ArrayValue(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Value]

    def __init__(self, values: _Optional[_Iterable[_Union[Value, _Mapping]]]=...) -> None:
        ...

class MapValue(_message.Message):
    __slots__ = ('fields',)

    class FieldsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Value, _Mapping]]=...) -> None:
            ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Value]

    def __init__(self, fields: _Optional[_Mapping[str, Value]]=...) -> None:
        ...