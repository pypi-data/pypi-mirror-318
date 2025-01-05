from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RealTimeBiddingSetting(_message.Message):
    __slots__ = ("opt_in",)
    OPT_IN_FIELD_NUMBER: _ClassVar[int]
    opt_in: bool
    def __init__(self, opt_in: bool = ...) -> None: ...
