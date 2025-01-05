from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IamBinding(_message.Message):
    __slots__ = ('action', 'role', 'member')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[IamBinding.Action]
        ADD: _ClassVar[IamBinding.Action]
        REMOVE: _ClassVar[IamBinding.Action]
    ACTION_UNSPECIFIED: IamBinding.Action
    ADD: IamBinding.Action
    REMOVE: IamBinding.Action
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    action: IamBinding.Action
    role: str
    member: str

    def __init__(self, action: _Optional[_Union[IamBinding.Action, str]]=..., role: _Optional[str]=..., member: _Optional[str]=...) -> None:
        ...