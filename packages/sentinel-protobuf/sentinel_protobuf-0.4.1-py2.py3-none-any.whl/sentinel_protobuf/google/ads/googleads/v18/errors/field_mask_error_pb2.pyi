from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FieldMaskErrorEnum(_message.Message):
    __slots__ = ()

    class FieldMaskError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FieldMaskErrorEnum.FieldMaskError]
        UNKNOWN: _ClassVar[FieldMaskErrorEnum.FieldMaskError]
        FIELD_MASK_MISSING: _ClassVar[FieldMaskErrorEnum.FieldMaskError]
        FIELD_MASK_NOT_ALLOWED: _ClassVar[FieldMaskErrorEnum.FieldMaskError]
        FIELD_NOT_FOUND: _ClassVar[FieldMaskErrorEnum.FieldMaskError]
        FIELD_HAS_SUBFIELDS: _ClassVar[FieldMaskErrorEnum.FieldMaskError]
    UNSPECIFIED: FieldMaskErrorEnum.FieldMaskError
    UNKNOWN: FieldMaskErrorEnum.FieldMaskError
    FIELD_MASK_MISSING: FieldMaskErrorEnum.FieldMaskError
    FIELD_MASK_NOT_ALLOWED: FieldMaskErrorEnum.FieldMaskError
    FIELD_NOT_FOUND: FieldMaskErrorEnum.FieldMaskError
    FIELD_HAS_SUBFIELDS: FieldMaskErrorEnum.FieldMaskError

    def __init__(self) -> None:
        ...