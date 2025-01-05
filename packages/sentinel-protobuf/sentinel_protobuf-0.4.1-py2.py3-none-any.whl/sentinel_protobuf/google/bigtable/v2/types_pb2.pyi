from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Type(_message.Message):
    __slots__ = ('bytes_type', 'string_type', 'int64_type', 'float32_type', 'float64_type', 'bool_type', 'timestamp_type', 'date_type', 'aggregate_type', 'struct_type', 'array_type', 'map_type')

    class Bytes(_message.Message):
        __slots__ = ('encoding',)

        class Encoding(_message.Message):
            __slots__ = ('raw',)

            class Raw(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...
            RAW_FIELD_NUMBER: _ClassVar[int]
            raw: Type.Bytes.Encoding.Raw

            def __init__(self, raw: _Optional[_Union[Type.Bytes.Encoding.Raw, _Mapping]]=...) -> None:
                ...
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        encoding: Type.Bytes.Encoding

        def __init__(self, encoding: _Optional[_Union[Type.Bytes.Encoding, _Mapping]]=...) -> None:
            ...

    class String(_message.Message):
        __slots__ = ('encoding',)

        class Encoding(_message.Message):
            __slots__ = ('utf8_raw', 'utf8_bytes')

            class Utf8Raw(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...

            class Utf8Bytes(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...
            UTF8_RAW_FIELD_NUMBER: _ClassVar[int]
            UTF8_BYTES_FIELD_NUMBER: _ClassVar[int]
            utf8_raw: Type.String.Encoding.Utf8Raw
            utf8_bytes: Type.String.Encoding.Utf8Bytes

            def __init__(self, utf8_raw: _Optional[_Union[Type.String.Encoding.Utf8Raw, _Mapping]]=..., utf8_bytes: _Optional[_Union[Type.String.Encoding.Utf8Bytes, _Mapping]]=...) -> None:
                ...
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        encoding: Type.String.Encoding

        def __init__(self, encoding: _Optional[_Union[Type.String.Encoding, _Mapping]]=...) -> None:
            ...

    class Int64(_message.Message):
        __slots__ = ('encoding',)

        class Encoding(_message.Message):
            __slots__ = ('big_endian_bytes',)

            class BigEndianBytes(_message.Message):
                __slots__ = ('bytes_type',)
                BYTES_TYPE_FIELD_NUMBER: _ClassVar[int]
                bytes_type: Type.Bytes

                def __init__(self, bytes_type: _Optional[_Union[Type.Bytes, _Mapping]]=...) -> None:
                    ...
            BIG_ENDIAN_BYTES_FIELD_NUMBER: _ClassVar[int]
            big_endian_bytes: Type.Int64.Encoding.BigEndianBytes

            def __init__(self, big_endian_bytes: _Optional[_Union[Type.Int64.Encoding.BigEndianBytes, _Mapping]]=...) -> None:
                ...
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        encoding: Type.Int64.Encoding

        def __init__(self, encoding: _Optional[_Union[Type.Int64.Encoding, _Mapping]]=...) -> None:
            ...

    class Bool(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Float32(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Float64(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Timestamp(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Date(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Struct(_message.Message):
        __slots__ = ('fields',)

        class Field(_message.Message):
            __slots__ = ('field_name', 'type')
            FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            field_name: str
            type: Type

            def __init__(self, field_name: _Optional[str]=..., type: _Optional[_Union[Type, _Mapping]]=...) -> None:
                ...
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedCompositeFieldContainer[Type.Struct.Field]

        def __init__(self, fields: _Optional[_Iterable[_Union[Type.Struct.Field, _Mapping]]]=...) -> None:
            ...

    class Array(_message.Message):
        __slots__ = ('element_type',)
        ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        element_type: Type

        def __init__(self, element_type: _Optional[_Union[Type, _Mapping]]=...) -> None:
            ...

    class Map(_message.Message):
        __slots__ = ('key_type', 'value_type')
        KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        key_type: Type
        value_type: Type

        def __init__(self, key_type: _Optional[_Union[Type, _Mapping]]=..., value_type: _Optional[_Union[Type, _Mapping]]=...) -> None:
            ...

    class Aggregate(_message.Message):
        __slots__ = ('input_type', 'state_type', 'sum', 'hllpp_unique_count', 'max', 'min')

        class Sum(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class Max(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class Min(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class HyperLogLogPlusPlusUniqueCount(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
        STATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SUM_FIELD_NUMBER: _ClassVar[int]
        HLLPP_UNIQUE_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        input_type: Type
        state_type: Type
        sum: Type.Aggregate.Sum
        hllpp_unique_count: Type.Aggregate.HyperLogLogPlusPlusUniqueCount
        max: Type.Aggregate.Max
        min: Type.Aggregate.Min

        def __init__(self, input_type: _Optional[_Union[Type, _Mapping]]=..., state_type: _Optional[_Union[Type, _Mapping]]=..., sum: _Optional[_Union[Type.Aggregate.Sum, _Mapping]]=..., hllpp_unique_count: _Optional[_Union[Type.Aggregate.HyperLogLogPlusPlusUniqueCount, _Mapping]]=..., max: _Optional[_Union[Type.Aggregate.Max, _Mapping]]=..., min: _Optional[_Union[Type.Aggregate.Min, _Mapping]]=...) -> None:
            ...
    BYTES_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRING_TYPE_FIELD_NUMBER: _ClassVar[int]
    INT64_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT32_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT64_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    bytes_type: Type.Bytes
    string_type: Type.String
    int64_type: Type.Int64
    float32_type: Type.Float32
    float64_type: Type.Float64
    bool_type: Type.Bool
    timestamp_type: Type.Timestamp
    date_type: Type.Date
    aggregate_type: Type.Aggregate
    struct_type: Type.Struct
    array_type: Type.Array
    map_type: Type.Map

    def __init__(self, bytes_type: _Optional[_Union[Type.Bytes, _Mapping]]=..., string_type: _Optional[_Union[Type.String, _Mapping]]=..., int64_type: _Optional[_Union[Type.Int64, _Mapping]]=..., float32_type: _Optional[_Union[Type.Float32, _Mapping]]=..., float64_type: _Optional[_Union[Type.Float64, _Mapping]]=..., bool_type: _Optional[_Union[Type.Bool, _Mapping]]=..., timestamp_type: _Optional[_Union[Type.Timestamp, _Mapping]]=..., date_type: _Optional[_Union[Type.Date, _Mapping]]=..., aggregate_type: _Optional[_Union[Type.Aggregate, _Mapping]]=..., struct_type: _Optional[_Union[Type.Struct, _Mapping]]=..., array_type: _Optional[_Union[Type.Array, _Mapping]]=..., map_type: _Optional[_Union[Type.Map, _Mapping]]=...) -> None:
        ...