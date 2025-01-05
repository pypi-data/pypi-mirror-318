from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ('user', 'anonymous', 'impersonation', 'system', 'administrator')
    USER_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    IMPERSONATION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATOR_FIELD_NUMBER: _ClassVar[int]
    user: User
    anonymous: AnonymousUser
    impersonation: Impersonation
    system: SystemEvent
    administrator: Administrator

    def __init__(self, user: _Optional[_Union[User, _Mapping]]=..., anonymous: _Optional[_Union[AnonymousUser, _Mapping]]=..., impersonation: _Optional[_Union[Impersonation, _Mapping]]=..., system: _Optional[_Union[SystemEvent, _Mapping]]=..., administrator: _Optional[_Union[Administrator, _Mapping]]=...) -> None:
        ...

class User(_message.Message):
    __slots__ = ('known_user', 'deleted_user', 'unknown_user')

    class KnownUser(_message.Message):
        __slots__ = ('person_name', 'is_current_user')
        PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_CURRENT_USER_FIELD_NUMBER: _ClassVar[int]
        person_name: str
        is_current_user: bool

        def __init__(self, person_name: _Optional[str]=..., is_current_user: bool=...) -> None:
            ...

    class DeletedUser(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class UnknownUser(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    KNOWN_USER_FIELD_NUMBER: _ClassVar[int]
    DELETED_USER_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USER_FIELD_NUMBER: _ClassVar[int]
    known_user: User.KnownUser
    deleted_user: User.DeletedUser
    unknown_user: User.UnknownUser

    def __init__(self, known_user: _Optional[_Union[User.KnownUser, _Mapping]]=..., deleted_user: _Optional[_Union[User.DeletedUser, _Mapping]]=..., unknown_user: _Optional[_Union[User.UnknownUser, _Mapping]]=...) -> None:
        ...

class AnonymousUser(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Impersonation(_message.Message):
    __slots__ = ('impersonated_user',)
    IMPERSONATED_USER_FIELD_NUMBER: _ClassVar[int]
    impersonated_user: User

    def __init__(self, impersonated_user: _Optional[_Union[User, _Mapping]]=...) -> None:
        ...

class SystemEvent(_message.Message):
    __slots__ = ('type',)

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[SystemEvent.Type]
        USER_DELETION: _ClassVar[SystemEvent.Type]
        TRASH_AUTO_PURGE: _ClassVar[SystemEvent.Type]
    TYPE_UNSPECIFIED: SystemEvent.Type
    USER_DELETION: SystemEvent.Type
    TRASH_AUTO_PURGE: SystemEvent.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SystemEvent.Type

    def __init__(self, type: _Optional[_Union[SystemEvent.Type, str]]=...) -> None:
        ...

class Administrator(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...