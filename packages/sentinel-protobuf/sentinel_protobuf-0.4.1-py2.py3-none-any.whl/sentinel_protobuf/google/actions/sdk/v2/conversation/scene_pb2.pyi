from google.actions.sdk.v2.conversation.prompt import prompt_pb2 as _prompt_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SlotFillingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[SlotFillingStatus]
    INITIALIZED: _ClassVar[SlotFillingStatus]
    COLLECTING: _ClassVar[SlotFillingStatus]
    FINAL: _ClassVar[SlotFillingStatus]
UNSPECIFIED: SlotFillingStatus
INITIALIZED: SlotFillingStatus
COLLECTING: SlotFillingStatus
FINAL: SlotFillingStatus

class Slot(_message.Message):
    __slots__ = ('mode', 'status', 'value', 'updated', 'prompt')

    class SlotMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[Slot.SlotMode]
        OPTIONAL: _ClassVar[Slot.SlotMode]
        REQUIRED: _ClassVar[Slot.SlotMode]
    MODE_UNSPECIFIED: Slot.SlotMode
    OPTIONAL: Slot.SlotMode
    REQUIRED: Slot.SlotMode

    class SlotStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SLOT_UNSPECIFIED: _ClassVar[Slot.SlotStatus]
        EMPTY: _ClassVar[Slot.SlotStatus]
        INVALID: _ClassVar[Slot.SlotStatus]
        FILLED: _ClassVar[Slot.SlotStatus]
    SLOT_UNSPECIFIED: Slot.SlotStatus
    EMPTY: Slot.SlotStatus
    INVALID: Slot.SlotStatus
    FILLED: Slot.SlotStatus
    MODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    mode: Slot.SlotMode
    status: Slot.SlotStatus
    value: _struct_pb2.Value
    updated: bool
    prompt: _prompt_pb2.Prompt

    def __init__(self, mode: _Optional[_Union[Slot.SlotMode, str]]=..., status: _Optional[_Union[Slot.SlotStatus, str]]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., updated: bool=..., prompt: _Optional[_Union[_prompt_pb2.Prompt, _Mapping]]=...) -> None:
        ...