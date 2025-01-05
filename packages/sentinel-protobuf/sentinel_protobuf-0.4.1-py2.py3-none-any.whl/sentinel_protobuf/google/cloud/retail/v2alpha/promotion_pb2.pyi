from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Promotion(_message.Message):
    __slots__ = ('promotion_id',)
    PROMOTION_ID_FIELD_NUMBER: _ClassVar[int]
    promotion_id: str

    def __init__(self, promotion_id: _Optional[str]=...) -> None:
        ...