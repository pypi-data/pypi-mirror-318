from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ('name', 'meeting_uri', 'meeting_code', 'config', 'active_conference')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEETING_URI_FIELD_NUMBER: _ClassVar[int]
    MEETING_CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONFERENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    meeting_uri: str
    meeting_code: str
    config: SpaceConfig
    active_conference: ActiveConference

    def __init__(self, name: _Optional[str]=..., meeting_uri: _Optional[str]=..., meeting_code: _Optional[str]=..., config: _Optional[_Union[SpaceConfig, _Mapping]]=..., active_conference: _Optional[_Union[ActiveConference, _Mapping]]=...) -> None:
        ...

class ActiveConference(_message.Message):
    __slots__ = ('conference_record',)
    CONFERENCE_RECORD_FIELD_NUMBER: _ClassVar[int]
    conference_record: str

    def __init__(self, conference_record: _Optional[str]=...) -> None:
        ...

class SpaceConfig(_message.Message):
    __slots__ = ('access_type', 'entry_point_access')

    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_TYPE_UNSPECIFIED: _ClassVar[SpaceConfig.AccessType]
        OPEN: _ClassVar[SpaceConfig.AccessType]
        TRUSTED: _ClassVar[SpaceConfig.AccessType]
        RESTRICTED: _ClassVar[SpaceConfig.AccessType]
    ACCESS_TYPE_UNSPECIFIED: SpaceConfig.AccessType
    OPEN: SpaceConfig.AccessType
    TRUSTED: SpaceConfig.AccessType
    RESTRICTED: SpaceConfig.AccessType

    class EntryPointAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTRY_POINT_ACCESS_UNSPECIFIED: _ClassVar[SpaceConfig.EntryPointAccess]
        ALL: _ClassVar[SpaceConfig.EntryPointAccess]
        CREATOR_APP_ONLY: _ClassVar[SpaceConfig.EntryPointAccess]
    ENTRY_POINT_ACCESS_UNSPECIFIED: SpaceConfig.EntryPointAccess
    ALL: SpaceConfig.EntryPointAccess
    CREATOR_APP_ONLY: SpaceConfig.EntryPointAccess
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    access_type: SpaceConfig.AccessType
    entry_point_access: SpaceConfig.EntryPointAccess

    def __init__(self, access_type: _Optional[_Union[SpaceConfig.AccessType, str]]=..., entry_point_access: _Optional[_Union[SpaceConfig.EntryPointAccess, str]]=...) -> None:
        ...

class ConferenceRecord(_message.Message):
    __slots__ = ('name', 'start_time', 'end_time', 'expire_time', 'space')
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    space: str

    def __init__(self, name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., space: _Optional[str]=...) -> None:
        ...

class Participant(_message.Message):
    __slots__ = ('signedin_user', 'anonymous_user', 'phone_user', 'name', 'earliest_start_time', 'latest_end_time')
    SIGNEDIN_USER_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_USER_FIELD_NUMBER: _ClassVar[int]
    PHONE_USER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_END_TIME_FIELD_NUMBER: _ClassVar[int]
    signedin_user: SignedinUser
    anonymous_user: AnonymousUser
    phone_user: PhoneUser
    name: str
    earliest_start_time: _timestamp_pb2.Timestamp
    latest_end_time: _timestamp_pb2.Timestamp

    def __init__(self, signedin_user: _Optional[_Union[SignedinUser, _Mapping]]=..., anonymous_user: _Optional[_Union[AnonymousUser, _Mapping]]=..., phone_user: _Optional[_Union[PhoneUser, _Mapping]]=..., name: _Optional[str]=..., earliest_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., latest_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ParticipantSession(_message.Message):
    __slots__ = ('name', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SignedinUser(_message.Message):
    __slots__ = ('user', 'display_name')
    USER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    display_name: str

    def __init__(self, user: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class AnonymousUser(_message.Message):
    __slots__ = ('display_name',)
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str

    def __init__(self, display_name: _Optional[str]=...) -> None:
        ...

class PhoneUser(_message.Message):
    __slots__ = ('display_name',)
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str

    def __init__(self, display_name: _Optional[str]=...) -> None:
        ...

class Recording(_message.Message):
    __slots__ = ('drive_destination', 'name', 'state', 'start_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Recording.State]
        STARTED: _ClassVar[Recording.State]
        ENDED: _ClassVar[Recording.State]
        FILE_GENERATED: _ClassVar[Recording.State]
    STATE_UNSPECIFIED: Recording.State
    STARTED: Recording.State
    ENDED: Recording.State
    FILE_GENERATED: Recording.State
    DRIVE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    drive_destination: DriveDestination
    name: str
    state: Recording.State
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, drive_destination: _Optional[_Union[DriveDestination, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[Recording.State, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DriveDestination(_message.Message):
    __slots__ = ('file', 'export_uri')
    FILE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_URI_FIELD_NUMBER: _ClassVar[int]
    file: str
    export_uri: str

    def __init__(self, file: _Optional[str]=..., export_uri: _Optional[str]=...) -> None:
        ...

class Transcript(_message.Message):
    __slots__ = ('docs_destination', 'name', 'state', 'start_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Transcript.State]
        STARTED: _ClassVar[Transcript.State]
        ENDED: _ClassVar[Transcript.State]
        FILE_GENERATED: _ClassVar[Transcript.State]
    STATE_UNSPECIFIED: Transcript.State
    STARTED: Transcript.State
    ENDED: Transcript.State
    FILE_GENERATED: Transcript.State
    DOCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    docs_destination: DocsDestination
    name: str
    state: Transcript.State
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, docs_destination: _Optional[_Union[DocsDestination, _Mapping]]=..., name: _Optional[str]=..., state: _Optional[_Union[Transcript.State, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DocsDestination(_message.Message):
    __slots__ = ('document', 'export_uri')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_URI_FIELD_NUMBER: _ClassVar[int]
    document: str
    export_uri: str

    def __init__(self, document: _Optional[str]=..., export_uri: _Optional[str]=...) -> None:
        ...

class TranscriptEntry(_message.Message):
    __slots__ = ('name', 'participant', 'text', 'language_code', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    participant: str
    text: str
    language_code: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., participant: _Optional[str]=..., text: _Optional[str]=..., language_code: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...