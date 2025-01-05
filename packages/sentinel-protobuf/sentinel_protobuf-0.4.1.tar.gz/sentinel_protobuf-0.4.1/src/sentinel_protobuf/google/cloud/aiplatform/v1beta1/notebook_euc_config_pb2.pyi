from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class NotebookEucConfig(_message.Message):
    __slots__ = ('euc_disabled', 'bypass_actas_check')
    EUC_DISABLED_FIELD_NUMBER: _ClassVar[int]
    BYPASS_ACTAS_CHECK_FIELD_NUMBER: _ClassVar[int]
    euc_disabled: bool
    bypass_actas_check: bool

    def __init__(self, euc_disabled: bool=..., bypass_actas_check: bool=...) -> None:
        ...