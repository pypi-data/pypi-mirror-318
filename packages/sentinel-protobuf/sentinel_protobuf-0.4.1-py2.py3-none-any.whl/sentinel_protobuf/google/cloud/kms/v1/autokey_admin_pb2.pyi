from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAutokeyConfigRequest(_message.Message):
    __slots__ = ('autokey_config', 'update_mask')
    AUTOKEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    autokey_config: AutokeyConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, autokey_config: _Optional[_Union[AutokeyConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetAutokeyConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class AutokeyConfig(_message.Message):
    __slots__ = ('name', 'key_project', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AutokeyConfig.State]
        ACTIVE: _ClassVar[AutokeyConfig.State]
        KEY_PROJECT_DELETED: _ClassVar[AutokeyConfig.State]
        UNINITIALIZED: _ClassVar[AutokeyConfig.State]
    STATE_UNSPECIFIED: AutokeyConfig.State
    ACTIVE: AutokeyConfig.State
    KEY_PROJECT_DELETED: AutokeyConfig.State
    UNINITIALIZED: AutokeyConfig.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_PROJECT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_project: str
    state: AutokeyConfig.State

    def __init__(self, name: _Optional[str]=..., key_project: _Optional[str]=..., state: _Optional[_Union[AutokeyConfig.State, str]]=...) -> None:
        ...

class ShowEffectiveAutokeyConfigRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ShowEffectiveAutokeyConfigResponse(_message.Message):
    __slots__ = ('key_project',)
    KEY_PROJECT_FIELD_NUMBER: _ClassVar[int]
    key_project: str

    def __init__(self, key_project: _Optional[str]=...) -> None:
        ...