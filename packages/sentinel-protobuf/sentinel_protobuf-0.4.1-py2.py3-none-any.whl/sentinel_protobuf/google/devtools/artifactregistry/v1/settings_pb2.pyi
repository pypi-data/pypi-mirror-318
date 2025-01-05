from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProjectSettings(_message.Message):
    __slots__ = ('name', 'legacy_redirection_state', 'pull_percent')

    class RedirectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REDIRECTION_STATE_UNSPECIFIED: _ClassVar[ProjectSettings.RedirectionState]
        REDIRECTION_FROM_GCR_IO_DISABLED: _ClassVar[ProjectSettings.RedirectionState]
        REDIRECTION_FROM_GCR_IO_ENABLED: _ClassVar[ProjectSettings.RedirectionState]
        REDIRECTION_FROM_GCR_IO_FINALIZED: _ClassVar[ProjectSettings.RedirectionState]
        REDIRECTION_FROM_GCR_IO_ENABLED_AND_COPYING: _ClassVar[ProjectSettings.RedirectionState]
        REDIRECTION_FROM_GCR_IO_PARTIAL_AND_COPYING: _ClassVar[ProjectSettings.RedirectionState]
    REDIRECTION_STATE_UNSPECIFIED: ProjectSettings.RedirectionState
    REDIRECTION_FROM_GCR_IO_DISABLED: ProjectSettings.RedirectionState
    REDIRECTION_FROM_GCR_IO_ENABLED: ProjectSettings.RedirectionState
    REDIRECTION_FROM_GCR_IO_FINALIZED: ProjectSettings.RedirectionState
    REDIRECTION_FROM_GCR_IO_ENABLED_AND_COPYING: ProjectSettings.RedirectionState
    REDIRECTION_FROM_GCR_IO_PARTIAL_AND_COPYING: ProjectSettings.RedirectionState
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEGACY_REDIRECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    PULL_PERCENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    legacy_redirection_state: ProjectSettings.RedirectionState
    pull_percent: int

    def __init__(self, name: _Optional[str]=..., legacy_redirection_state: _Optional[_Union[ProjectSettings.RedirectionState, str]]=..., pull_percent: _Optional[int]=...) -> None:
        ...

class GetProjectSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateProjectSettingsRequest(_message.Message):
    __slots__ = ('project_settings', 'update_mask')
    PROJECT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project_settings: ProjectSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, project_settings: _Optional[_Union[ProjectSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...