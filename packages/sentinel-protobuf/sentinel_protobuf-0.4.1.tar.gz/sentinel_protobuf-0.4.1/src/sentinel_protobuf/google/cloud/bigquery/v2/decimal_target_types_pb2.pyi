from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DecimalTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECIMAL_TARGET_TYPE_UNSPECIFIED: _ClassVar[DecimalTargetType]
    NUMERIC: _ClassVar[DecimalTargetType]
    BIGNUMERIC: _ClassVar[DecimalTargetType]
    STRING: _ClassVar[DecimalTargetType]
DECIMAL_TARGET_TYPE_UNSPECIFIED: DecimalTargetType
NUMERIC: DecimalTargetType
BIGNUMERIC: DecimalTargetType
STRING: DecimalTargetType