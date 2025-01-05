from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CurrencyConstant(_message.Message):
    __slots__ = ("resource_name", "code", "name", "symbol", "billable_unit_micros")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_UNIT_MICROS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    code: str
    name: str
    symbol: str
    billable_unit_micros: int
    def __init__(self, resource_name: _Optional[str] = ..., code: _Optional[str] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., billable_unit_micros: _Optional[int] = ...) -> None: ...
