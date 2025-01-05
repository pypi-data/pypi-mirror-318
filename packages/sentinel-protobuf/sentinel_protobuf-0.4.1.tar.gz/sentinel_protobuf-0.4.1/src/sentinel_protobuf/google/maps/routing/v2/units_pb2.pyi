from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class Units(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNITS_UNSPECIFIED: _ClassVar[Units]
    METRIC: _ClassVar[Units]
    IMPERIAL: _ClassVar[Units]
UNITS_UNSPECIFIED: Units
METRIC: Units
IMPERIAL: Units