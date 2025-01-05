from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddressMetadata(_message.Message):
    __slots__ = ("business", "po_box", "residential")
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    PO_BOX_FIELD_NUMBER: _ClassVar[int]
    RESIDENTIAL_FIELD_NUMBER: _ClassVar[int]
    business: bool
    po_box: bool
    residential: bool
    def __init__(self, business: bool = ..., po_box: bool = ..., residential: bool = ...) -> None: ...
