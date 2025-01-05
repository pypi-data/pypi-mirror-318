from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Barcode(_message.Message):
    __slots__ = ('format', 'value_format', 'raw_value')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    format: str
    value_format: str
    raw_value: str

    def __init__(self, format: _Optional[str]=..., value_format: _Optional[str]=..., raw_value: _Optional[str]=...) -> None:
        ...