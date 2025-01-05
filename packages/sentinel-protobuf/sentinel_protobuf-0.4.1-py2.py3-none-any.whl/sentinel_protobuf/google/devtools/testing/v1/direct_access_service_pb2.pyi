from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.testing.v1 import adb_service_pb2 as _adb_service_pb2
from google.devtools.testing.v1 import test_execution_pb2 as _test_execution_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDeviceSessionRequest(_message.Message):
    __slots__ = ('parent', 'device_session')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    device_session: DeviceSession

    def __init__(self, parent: _Optional[str]=..., device_session: _Optional[_Union[DeviceSession, _Mapping]]=...) -> None:
        ...

class ListDeviceSessionsRequest(_message.Message):
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

class ListDeviceSessionsResponse(_message.Message):
    __slots__ = ('device_sessions', 'next_page_token')
    DEVICE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    device_sessions: _containers.RepeatedCompositeFieldContainer[DeviceSession]
    next_page_token: str

    def __init__(self, device_sessions: _Optional[_Iterable[_Union[DeviceSession, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDeviceSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelDeviceSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDeviceSessionRequest(_message.Message):
    __slots__ = ('device_session', 'update_mask')
    DEVICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    device_session: DeviceSession
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, device_session: _Optional[_Union[DeviceSession, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeviceSession(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'state_histories', 'ttl', 'expire_time', 'inactivity_timeout', 'create_time', 'active_start_time', 'android_device')

    class SessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SESSION_STATE_UNSPECIFIED: _ClassVar[DeviceSession.SessionState]
        REQUESTED: _ClassVar[DeviceSession.SessionState]
        PENDING: _ClassVar[DeviceSession.SessionState]
        ACTIVE: _ClassVar[DeviceSession.SessionState]
        EXPIRED: _ClassVar[DeviceSession.SessionState]
        FINISHED: _ClassVar[DeviceSession.SessionState]
        UNAVAILABLE: _ClassVar[DeviceSession.SessionState]
        ERROR: _ClassVar[DeviceSession.SessionState]
    SESSION_STATE_UNSPECIFIED: DeviceSession.SessionState
    REQUESTED: DeviceSession.SessionState
    PENDING: DeviceSession.SessionState
    ACTIVE: DeviceSession.SessionState
    EXPIRED: DeviceSession.SessionState
    FINISHED: DeviceSession.SessionState
    UNAVAILABLE: DeviceSession.SessionState
    ERROR: DeviceSession.SessionState

    class SessionStateEvent(_message.Message):
        __slots__ = ('session_state', 'event_time', 'state_message')
        SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
        EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
        STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        session_state: DeviceSession.SessionState
        event_time: _timestamp_pb2.Timestamp
        state_message: str

        def __init__(self, session_state: _Optional[_Union[DeviceSession.SessionState, str]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state_message: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    INACTIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    ANDROID_DEVICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: DeviceSession.SessionState
    state_histories: _containers.RepeatedCompositeFieldContainer[DeviceSession.SessionStateEvent]
    ttl: _duration_pb2.Duration
    expire_time: _timestamp_pb2.Timestamp
    inactivity_timeout: _duration_pb2.Duration
    create_time: _timestamp_pb2.Timestamp
    active_start_time: _timestamp_pb2.Timestamp
    android_device: _test_execution_pb2.AndroidDevice

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[DeviceSession.SessionState, str]]=..., state_histories: _Optional[_Iterable[_Union[DeviceSession.SessionStateEvent, _Mapping]]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., inactivity_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., active_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., android_device: _Optional[_Union[_test_execution_pb2.AndroidDevice, _Mapping]]=...) -> None:
        ...