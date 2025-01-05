from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_EVENT_TYPE_UNSPECIFIED: _ClassVar[OperationEventType]
    OPERATION_EVENT_CREATE_CONTENT_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_CREATE_CONTENT_ENDED: _ClassVar[OperationEventType]
    OPERATION_EVENT_BUILD_CONTENT_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_BUILD_CONTENT_ENDED: _ClassVar[OperationEventType]
    OPERATION_EVENT_UPDATE_CONTENT_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_UPDATE_CONTENT_ENDED: _ClassVar[OperationEventType]
    OPERATION_EVENT_DELETE_CONTENT_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_DELETE_CONTENT_ENDED: _ClassVar[OperationEventType]
    OPERATION_EVENT_CREATE_INSTANCE_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_CREATE_INSTANCE_ENDED: _ClassVar[OperationEventType]
    OPERATION_EVENT_UPDATE_INSTANCE_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_UPDATE_INSTANCE_ENDED: _ClassVar[OperationEventType]
    OPERATION_EVENT_DELETE_INSTANCE_STARTED: _ClassVar[OperationEventType]
    OPERATION_EVENT_DELETE_INSTANCE_ENDED: _ClassVar[OperationEventType]

class SessionEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_EVENT_TYPE_UNSPECIFIED: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_SHUTTING_DOWN: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_READY: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_BINARY_STARTED: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_READ_POD_IMAGE_NAMES: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_CONNECTED_TO_GAME: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_CONNECTED_TO_CLIENT: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_DISCONNECTED_FROM_CLIENT: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_RECEIVED_CREATE_SESSION_REQUEST: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_GAME_MESSAGE_STREAM_CLOSED: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_GAME_FRAME_STREAM_CLOSED: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_GAME_MESSAGE_STREAM_ERROR: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_GAME_AUDIO_STREAM_ERROR: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_GAME_AUDIO_STREAM_CLOSED: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_GAME_FRAME_STREAM_ERROR: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_GAME_DISCONNECTING_AFTER_PAUSED_TOO_LONG: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_RECEIVED_EXPERIMENT_CONFIGURATION: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_GAME_CONNECTED_TO_LOGGING_SERVICE: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_DETERMINED_SESSION_OPTIONS: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_STREAMER_KILLED_IN_MIDDLE_OF_SESSION: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_GAME_UPDATED_FRAME_PIPELINE: _ClassVar[SessionEventType]
    SESSION_EVENT_SERVER_ERROR: _ClassVar[SessionEventType]
OPERATION_EVENT_TYPE_UNSPECIFIED: OperationEventType
OPERATION_EVENT_CREATE_CONTENT_STARTED: OperationEventType
OPERATION_EVENT_CREATE_CONTENT_ENDED: OperationEventType
OPERATION_EVENT_BUILD_CONTENT_STARTED: OperationEventType
OPERATION_EVENT_BUILD_CONTENT_ENDED: OperationEventType
OPERATION_EVENT_UPDATE_CONTENT_STARTED: OperationEventType
OPERATION_EVENT_UPDATE_CONTENT_ENDED: OperationEventType
OPERATION_EVENT_DELETE_CONTENT_STARTED: OperationEventType
OPERATION_EVENT_DELETE_CONTENT_ENDED: OperationEventType
OPERATION_EVENT_CREATE_INSTANCE_STARTED: OperationEventType
OPERATION_EVENT_CREATE_INSTANCE_ENDED: OperationEventType
OPERATION_EVENT_UPDATE_INSTANCE_STARTED: OperationEventType
OPERATION_EVENT_UPDATE_INSTANCE_ENDED: OperationEventType
OPERATION_EVENT_DELETE_INSTANCE_STARTED: OperationEventType
OPERATION_EVENT_DELETE_INSTANCE_ENDED: OperationEventType
SESSION_EVENT_TYPE_UNSPECIFIED: SessionEventType
SESSION_EVENT_SERVER_STREAMER_SHUTTING_DOWN: SessionEventType
SESSION_EVENT_SERVER_STREAMER_READY: SessionEventType
SESSION_EVENT_SERVER_STREAMER_BINARY_STARTED: SessionEventType
SESSION_EVENT_SERVER_STREAMER_READ_POD_IMAGE_NAMES: SessionEventType
SESSION_EVENT_SERVER_STREAMER_CONNECTED_TO_GAME: SessionEventType
SESSION_EVENT_SERVER_STREAMER_CONNECTED_TO_CLIENT: SessionEventType
SESSION_EVENT_SERVER_STREAMER_DISCONNECTED_FROM_CLIENT: SessionEventType
SESSION_EVENT_SERVER_STREAMER_RECEIVED_CREATE_SESSION_REQUEST: SessionEventType
SESSION_EVENT_SERVER_STREAMER_GAME_MESSAGE_STREAM_CLOSED: SessionEventType
SESSION_EVENT_SERVER_STREAMER_GAME_FRAME_STREAM_CLOSED: SessionEventType
SESSION_EVENT_SERVER_STREAMER_GAME_MESSAGE_STREAM_ERROR: SessionEventType
SESSION_EVENT_SERVER_STREAMER_GAME_AUDIO_STREAM_ERROR: SessionEventType
SESSION_EVENT_SERVER_STREAMER_GAME_AUDIO_STREAM_CLOSED: SessionEventType
SESSION_EVENT_SERVER_STREAMER_GAME_FRAME_STREAM_ERROR: SessionEventType
SESSION_EVENT_SERVER_GAME_DISCONNECTING_AFTER_PAUSED_TOO_LONG: SessionEventType
SESSION_EVENT_SERVER_STREAMER_RECEIVED_EXPERIMENT_CONFIGURATION: SessionEventType
SESSION_EVENT_SERVER_GAME_CONNECTED_TO_LOGGING_SERVICE: SessionEventType
SESSION_EVENT_SERVER_STREAMER_DETERMINED_SESSION_OPTIONS: SessionEventType
SESSION_EVENT_SERVER_STREAMER_KILLED_IN_MIDDLE_OF_SESSION: SessionEventType
SESSION_EVENT_SERVER_GAME_UPDATED_FRAME_PIPELINE: SessionEventType
SESSION_EVENT_SERVER_ERROR: SessionEventType

class OperationEventLog(_message.Message):
    __slots__ = ('event_type', 'event_time', 'operation', 'operation_artifacts')
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    event_type: OperationEventType
    event_time: _timestamp_pb2.Timestamp
    operation: str
    operation_artifacts: _containers.RepeatedCompositeFieldContainer[OperationArtifact]

    def __init__(self, event_type: _Optional[_Union[OperationEventType, str]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operation: _Optional[str]=..., operation_artifacts: _Optional[_Iterable[_Union[OperationArtifact, _Mapping]]]=...) -> None:
        ...

class OperationArtifact(_message.Message):
    __slots__ = ('artifact_type', 'artifact_uri')
    ARTIFACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    artifact_type: str
    artifact_uri: str

    def __init__(self, artifact_type: _Optional[str]=..., artifact_uri: _Optional[str]=...) -> None:
        ...

class SessionEventLog(_message.Message):
    __slots__ = ('event_type', 'event_time', 'session_id')
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    event_type: SessionEventType
    event_time: _timestamp_pb2.Timestamp
    session_id: str

    def __init__(self, event_type: _Optional[_Union[SessionEventType, str]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., session_id: _Optional[str]=...) -> None:
        ...