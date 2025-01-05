from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BoolArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bool]

    def __init__(self, values: _Optional[_Iterable[bool]]=...) -> None:
        ...

class DoubleArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, values: _Optional[_Iterable[float]]=...) -> None:
        ...

class Int64Array(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, values: _Optional[_Iterable[int]]=...) -> None:
        ...

class StringArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...

class Tensor(_message.Message):
    __slots__ = ('dtype', 'shape', 'bool_val', 'string_val', 'bytes_val', 'float_val', 'double_val', 'int_val', 'int64_val', 'uint_val', 'uint64_val', 'list_val', 'struct_val', 'tensor_val')

    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[Tensor.DataType]
        BOOL: _ClassVar[Tensor.DataType]
        STRING: _ClassVar[Tensor.DataType]
        FLOAT: _ClassVar[Tensor.DataType]
        DOUBLE: _ClassVar[Tensor.DataType]
        INT8: _ClassVar[Tensor.DataType]
        INT16: _ClassVar[Tensor.DataType]
        INT32: _ClassVar[Tensor.DataType]
        INT64: _ClassVar[Tensor.DataType]
        UINT8: _ClassVar[Tensor.DataType]
        UINT16: _ClassVar[Tensor.DataType]
        UINT32: _ClassVar[Tensor.DataType]
        UINT64: _ClassVar[Tensor.DataType]
    DATA_TYPE_UNSPECIFIED: Tensor.DataType
    BOOL: Tensor.DataType
    STRING: Tensor.DataType
    FLOAT: Tensor.DataType
    DOUBLE: Tensor.DataType
    INT8: Tensor.DataType
    INT16: Tensor.DataType
    INT32: Tensor.DataType
    INT64: Tensor.DataType
    UINT8: Tensor.DataType
    UINT16: Tensor.DataType
    UINT32: Tensor.DataType
    UINT64: Tensor.DataType

    class StructValEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Tensor

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Tensor, _Mapping]]=...) -> None:
            ...
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    STRING_VAL_FIELD_NUMBER: _ClassVar[int]
    BYTES_VAL_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VAL_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VAL_FIELD_NUMBER: _ClassVar[int]
    INT_VAL_FIELD_NUMBER: _ClassVar[int]
    INT64_VAL_FIELD_NUMBER: _ClassVar[int]
    UINT_VAL_FIELD_NUMBER: _ClassVar[int]
    UINT64_VAL_FIELD_NUMBER: _ClassVar[int]
    LIST_VAL_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VAL_FIELD_NUMBER: _ClassVar[int]
    TENSOR_VAL_FIELD_NUMBER: _ClassVar[int]
    dtype: Tensor.DataType
    shape: _containers.RepeatedScalarFieldContainer[int]
    bool_val: _containers.RepeatedScalarFieldContainer[bool]
    string_val: _containers.RepeatedScalarFieldContainer[str]
    bytes_val: _containers.RepeatedScalarFieldContainer[bytes]
    float_val: _containers.RepeatedScalarFieldContainer[float]
    double_val: _containers.RepeatedScalarFieldContainer[float]
    int_val: _containers.RepeatedScalarFieldContainer[int]
    int64_val: _containers.RepeatedScalarFieldContainer[int]
    uint_val: _containers.RepeatedScalarFieldContainer[int]
    uint64_val: _containers.RepeatedScalarFieldContainer[int]
    list_val: _containers.RepeatedCompositeFieldContainer[Tensor]
    struct_val: _containers.MessageMap[str, Tensor]
    tensor_val: bytes

    def __init__(self, dtype: _Optional[_Union[Tensor.DataType, str]]=..., shape: _Optional[_Iterable[int]]=..., bool_val: _Optional[_Iterable[bool]]=..., string_val: _Optional[_Iterable[str]]=..., bytes_val: _Optional[_Iterable[bytes]]=..., float_val: _Optional[_Iterable[float]]=..., double_val: _Optional[_Iterable[float]]=..., int_val: _Optional[_Iterable[int]]=..., int64_val: _Optional[_Iterable[int]]=..., uint_val: _Optional[_Iterable[int]]=..., uint64_val: _Optional[_Iterable[int]]=..., list_val: _Optional[_Iterable[_Union[Tensor, _Mapping]]]=..., struct_val: _Optional[_Mapping[str, Tensor]]=..., tensor_val: _Optional[bytes]=...) -> None:
        ...