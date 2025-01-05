from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ('name', 'version_state', 'creator', 'update_time')

    class VersionState(_message.Message):
        __slots__ = ('state', 'message')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Version.VersionState.State]
            CREATION_IN_PROGRESS: _ClassVar[Version.VersionState.State]
            CREATION_FAILED: _ClassVar[Version.VersionState.State]
            CREATED: _ClassVar[Version.VersionState.State]
            REVIEW_IN_PROGRESS: _ClassVar[Version.VersionState.State]
            APPROVED: _ClassVar[Version.VersionState.State]
            CONDITIONALLY_APPROVED: _ClassVar[Version.VersionState.State]
            DENIED: _ClassVar[Version.VersionState.State]
            UNDER_TAKEDOWN: _ClassVar[Version.VersionState.State]
            DELETED: _ClassVar[Version.VersionState.State]
        STATE_UNSPECIFIED: Version.VersionState.State
        CREATION_IN_PROGRESS: Version.VersionState.State
        CREATION_FAILED: Version.VersionState.State
        CREATED: Version.VersionState.State
        REVIEW_IN_PROGRESS: Version.VersionState.State
        APPROVED: Version.VersionState.State
        CONDITIONALLY_APPROVED: Version.VersionState.State
        DENIED: Version.VersionState.State
        UNDER_TAKEDOWN: Version.VersionState.State
        DELETED: Version.VersionState.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        state: Version.VersionState.State
        message: str

        def __init__(self, state: _Optional[_Union[Version.VersionState.State, str]]=..., message: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_state: Version.VersionState
    creator: str
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., version_state: _Optional[_Union[Version.VersionState, _Mapping]]=..., creator: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...