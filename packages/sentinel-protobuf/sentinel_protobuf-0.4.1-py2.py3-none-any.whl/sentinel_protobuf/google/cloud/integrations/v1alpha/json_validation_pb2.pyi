from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class JsonValidationOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON_VALIDATION_OPTION_UNSPECIFIED: _ClassVar[JsonValidationOption]
    SKIP: _ClassVar[JsonValidationOption]
    PRE_EXECUTION: _ClassVar[JsonValidationOption]
    POST_EXECUTION: _ClassVar[JsonValidationOption]
    PRE_POST_EXECUTION: _ClassVar[JsonValidationOption]
JSON_VALIDATION_OPTION_UNSPECIFIED: JsonValidationOption
SKIP: JsonValidationOption
PRE_EXECUTION: JsonValidationOption
POST_EXECUTION: JsonValidationOption
PRE_POST_EXECUTION: JsonValidationOption