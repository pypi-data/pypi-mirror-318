from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.meet.v2 import resource_pb2 as _resource_pb2_1
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceRequest(_message.Message):
    __slots__ = ('space',)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _resource_pb2_1.Space

    def __init__(self, space: _Optional[_Union[_resource_pb2_1.Space, _Mapping]]=...) -> None:
        ...

class GetSpaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSpaceRequest(_message.Message):
    __slots__ = ('space', 'update_mask')
    SPACE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    space: _resource_pb2_1.Space
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, space: _Optional[_Union[_resource_pb2_1.Space, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class EndActiveConferenceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetConferenceRecordRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConferenceRecordsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'filter')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListConferenceRecordsResponse(_message.Message):
    __slots__ = ('conference_records', 'next_page_token')
    CONFERENCE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conference_records: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.ConferenceRecord]
    next_page_token: str

    def __init__(self, conference_records: _Optional[_Iterable[_Union[_resource_pb2_1.ConferenceRecord, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetParticipantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListParticipantsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListParticipantsResponse(_message.Message):
    __slots__ = ('participants', 'next_page_token', 'total_size')
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.Participant]
    next_page_token: str
    total_size: int

    def __init__(self, participants: _Optional[_Iterable[_Union[_resource_pb2_1.Participant, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetParticipantSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListParticipantSessionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListParticipantSessionsResponse(_message.Message):
    __slots__ = ('participant_sessions', 'next_page_token')
    PARTICIPANT_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    participant_sessions: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.ParticipantSession]
    next_page_token: str

    def __init__(self, participant_sessions: _Optional[_Iterable[_Union[_resource_pb2_1.ParticipantSession, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRecordingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRecordingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRecordingsResponse(_message.Message):
    __slots__ = ('recordings', 'next_page_token')
    RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    recordings: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.Recording]
    next_page_token: str

    def __init__(self, recordings: _Optional[_Iterable[_Union[_resource_pb2_1.Recording, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTranscriptRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTranscriptsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTranscriptsResponse(_message.Message):
    __slots__ = ('transcripts', 'next_page_token')
    TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transcripts: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.Transcript]
    next_page_token: str

    def __init__(self, transcripts: _Optional[_Iterable[_Union[_resource_pb2_1.Transcript, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTranscriptEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTranscriptEntriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTranscriptEntriesResponse(_message.Message):
    __slots__ = ('transcript_entries', 'next_page_token')
    TRANSCRIPT_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transcript_entries: _containers.RepeatedCompositeFieldContainer[_resource_pb2_1.TranscriptEntry]
    next_page_token: str

    def __init__(self, transcript_entries: _Optional[_Iterable[_Union[_resource_pb2_1.TranscriptEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...