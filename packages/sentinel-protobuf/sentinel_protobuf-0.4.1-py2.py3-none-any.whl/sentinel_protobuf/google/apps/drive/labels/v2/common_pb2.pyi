from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.type import color_pb2 as _color_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Lifecycle(_message.Message):
    __slots__ = ('state', 'has_unpublished_changes', 'disabled_policy')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Lifecycle.State]
        UNPUBLISHED_DRAFT: _ClassVar[Lifecycle.State]
        PUBLISHED: _ClassVar[Lifecycle.State]
        DISABLED: _ClassVar[Lifecycle.State]
        DELETED: _ClassVar[Lifecycle.State]
    STATE_UNSPECIFIED: Lifecycle.State
    UNPUBLISHED_DRAFT: Lifecycle.State
    PUBLISHED: Lifecycle.State
    DISABLED: Lifecycle.State
    DELETED: Lifecycle.State

    class DisabledPolicy(_message.Message):
        __slots__ = ('hide_in_search', 'show_in_apply')
        HIDE_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
        SHOW_IN_APPLY_FIELD_NUMBER: _ClassVar[int]
        hide_in_search: bool
        show_in_apply: bool

        def __init__(self, hide_in_search: bool=..., show_in_apply: bool=...) -> None:
            ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    HAS_UNPUBLISHED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    DISABLED_POLICY_FIELD_NUMBER: _ClassVar[int]
    state: Lifecycle.State
    has_unpublished_changes: bool
    disabled_policy: Lifecycle.DisabledPolicy

    def __init__(self, state: _Optional[_Union[Lifecycle.State, str]]=..., has_unpublished_changes: bool=..., disabled_policy: _Optional[_Union[Lifecycle.DisabledPolicy, _Mapping]]=...) -> None:
        ...

class UserInfo(_message.Message):
    __slots__ = ('person',)
    PERSON_FIELD_NUMBER: _ClassVar[int]
    person: str

    def __init__(self, person: _Optional[str]=...) -> None:
        ...

class BadgeConfig(_message.Message):
    __slots__ = ('color', 'priority_override')
    COLOR_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    color: _color_pb2.Color
    priority_override: int

    def __init__(self, color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., priority_override: _Optional[int]=...) -> None:
        ...

class BadgeColors(_message.Message):
    __slots__ = ('background_color', 'foreground_color', 'solo_color')
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    FOREGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    SOLO_COLOR_FIELD_NUMBER: _ClassVar[int]
    background_color: _color_pb2.Color
    foreground_color: _color_pb2.Color
    solo_color: _color_pb2.Color

    def __init__(self, background_color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., foreground_color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., solo_color: _Optional[_Union[_color_pb2.Color, _Mapping]]=...) -> None:
        ...

class LockStatus(_message.Message):
    __slots__ = ('locked',)
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    locked: bool

    def __init__(self, locked: bool=...) -> None:
        ...