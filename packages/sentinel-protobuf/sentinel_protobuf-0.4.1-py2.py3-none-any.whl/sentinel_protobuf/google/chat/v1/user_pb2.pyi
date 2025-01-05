from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ('name', 'display_name', 'domain_id', 'type', 'is_anonymous')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[User.Type]
        HUMAN: _ClassVar[User.Type]
        BOT: _ClassVar[User.Type]
    TYPE_UNSPECIFIED: User.Type
    HUMAN: User.Type
    BOT: User.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    domain_id: str
    type: User.Type
    is_anonymous: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., domain_id: _Optional[str]=..., type: _Optional[_Union[User.Type, str]]=..., is_anonymous: bool=...) -> None:
        ...