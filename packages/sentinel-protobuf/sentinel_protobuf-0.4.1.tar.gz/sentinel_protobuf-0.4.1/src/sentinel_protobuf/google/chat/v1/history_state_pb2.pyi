from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HistoryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HISTORY_STATE_UNSPECIFIED: _ClassVar[HistoryState]
    HISTORY_OFF: _ClassVar[HistoryState]
    HISTORY_ON: _ClassVar[HistoryState]
HISTORY_STATE_UNSPECIFIED: HistoryState
HISTORY_OFF: HistoryState
HISTORY_ON: HistoryState