from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FirewallRule(_message.Message):
    __slots__ = ('priority', 'action', 'source_range', 'description')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_ACTION: _ClassVar[FirewallRule.Action]
        ALLOW: _ClassVar[FirewallRule.Action]
        DENY: _ClassVar[FirewallRule.Action]
    UNSPECIFIED_ACTION: FirewallRule.Action
    ALLOW: FirewallRule.Action
    DENY: FirewallRule.Action
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    priority: int
    action: FirewallRule.Action
    source_range: str
    description: str

    def __init__(self, priority: _Optional[int]=..., action: _Optional[_Union[FirewallRule.Action, str]]=..., source_range: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...