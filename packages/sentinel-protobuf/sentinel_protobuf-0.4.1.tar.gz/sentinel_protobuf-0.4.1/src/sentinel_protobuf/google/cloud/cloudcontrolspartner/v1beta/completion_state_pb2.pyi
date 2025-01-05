from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CompletionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPLETION_STATE_UNSPECIFIED: _ClassVar[CompletionState]
    PENDING: _ClassVar[CompletionState]
    SUCCEEDED: _ClassVar[CompletionState]
    FAILED: _ClassVar[CompletionState]
    NOT_APPLICABLE: _ClassVar[CompletionState]
COMPLETION_STATE_UNSPECIFIED: CompletionState
PENDING: CompletionState
SUCCEEDED: CompletionState
FAILED: CompletionState
NOT_APPLICABLE: CompletionState