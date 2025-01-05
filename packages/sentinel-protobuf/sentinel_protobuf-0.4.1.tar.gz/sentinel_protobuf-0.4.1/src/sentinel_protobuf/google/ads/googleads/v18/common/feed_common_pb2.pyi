from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Money(_message.Message):
    __slots__ = ("currency_code", "amount_micros")
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    amount_micros: int
    def __init__(self, currency_code: _Optional[str] = ..., amount_micros: _Optional[int] = ...) -> None: ...
