from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataproc.v1 import shared_pb2 as _shared_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ('parent', 'session', 'session_id', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    session: Session
    session_id: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., session: _Optional[_Union[Session, _Mapping]]=..., session_id: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSessionsRequest(_message.Message):
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

class ListSessionsResponse(_message.Message):
    __slots__ = ('sessions', 'next_page_token')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    next_page_token: str

    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class TerminateSessionRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class Session(_message.Message):
    __slots__ = ('name', 'uuid', 'create_time', 'jupyter_session', 'spark_connect_session', 'runtime_info', 'state', 'state_message', 'state_time', 'creator', 'labels', 'runtime_config', 'environment_config', 'user', 'state_history', 'session_template')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Session.State]
        CREATING: _ClassVar[Session.State]
        ACTIVE: _ClassVar[Session.State]
        TERMINATING: _ClassVar[Session.State]
        TERMINATED: _ClassVar[Session.State]
        FAILED: _ClassVar[Session.State]
    STATE_UNSPECIFIED: Session.State
    CREATING: Session.State
    ACTIVE: Session.State
    TERMINATING: Session.State
    TERMINATED: Session.State
    FAILED: Session.State

    class SessionStateHistory(_message.Message):
        __slots__ = ('state', 'state_message', 'state_start_time')
        STATE_FIELD_NUMBER: _ClassVar[int]
        STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
        state: Session.State
        state_message: str
        state_start_time: _timestamp_pb2.Timestamp

        def __init__(self, state: _Optional[_Union[Session.State, str]]=..., state_message: _Optional[str]=..., state_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    JUPYTER_SESSION_FIELD_NUMBER: _ClassVar[int]
    SPARK_CONNECT_SESSION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    STATE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    SESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    create_time: _timestamp_pb2.Timestamp
    jupyter_session: JupyterConfig
    spark_connect_session: SparkConnectConfig
    runtime_info: _shared_pb2.RuntimeInfo
    state: Session.State
    state_message: str
    state_time: _timestamp_pb2.Timestamp
    creator: str
    labels: _containers.ScalarMap[str, str]
    runtime_config: _shared_pb2.RuntimeConfig
    environment_config: _shared_pb2.EnvironmentConfig
    user: str
    state_history: _containers.RepeatedCompositeFieldContainer[Session.SessionStateHistory]
    session_template: str

    def __init__(self, name: _Optional[str]=..., uuid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., jupyter_session: _Optional[_Union[JupyterConfig, _Mapping]]=..., spark_connect_session: _Optional[_Union[SparkConnectConfig, _Mapping]]=..., runtime_info: _Optional[_Union[_shared_pb2.RuntimeInfo, _Mapping]]=..., state: _Optional[_Union[Session.State, str]]=..., state_message: _Optional[str]=..., state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., creator: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., runtime_config: _Optional[_Union[_shared_pb2.RuntimeConfig, _Mapping]]=..., environment_config: _Optional[_Union[_shared_pb2.EnvironmentConfig, _Mapping]]=..., user: _Optional[str]=..., state_history: _Optional[_Iterable[_Union[Session.SessionStateHistory, _Mapping]]]=..., session_template: _Optional[str]=...) -> None:
        ...

class JupyterConfig(_message.Message):
    __slots__ = ('kernel', 'display_name')

    class Kernel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KERNEL_UNSPECIFIED: _ClassVar[JupyterConfig.Kernel]
        PYTHON: _ClassVar[JupyterConfig.Kernel]
        SCALA: _ClassVar[JupyterConfig.Kernel]
    KERNEL_UNSPECIFIED: JupyterConfig.Kernel
    PYTHON: JupyterConfig.Kernel
    SCALA: JupyterConfig.Kernel
    KERNEL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    kernel: JupyterConfig.Kernel
    display_name: str

    def __init__(self, kernel: _Optional[_Union[JupyterConfig.Kernel, str]]=..., display_name: _Optional[str]=...) -> None:
        ...

class SparkConnectConfig(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...