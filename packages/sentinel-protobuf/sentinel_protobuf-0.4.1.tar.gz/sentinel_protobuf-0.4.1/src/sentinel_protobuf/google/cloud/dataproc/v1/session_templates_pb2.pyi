from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataproc.v1 import sessions_pb2 as _sessions_pb2
from google.cloud.dataproc.v1 import shared_pb2 as _shared_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionTemplateRequest(_message.Message):
    __slots__ = ('parent', 'session_template')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    session_template: SessionTemplate

    def __init__(self, parent: _Optional[str]=..., session_template: _Optional[_Union[SessionTemplate, _Mapping]]=...) -> None:
        ...

class UpdateSessionTemplateRequest(_message.Message):
    __slots__ = ('session_template',)
    SESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    session_template: SessionTemplate

    def __init__(self, session_template: _Optional[_Union[SessionTemplate, _Mapping]]=...) -> None:
        ...

class GetSessionTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSessionTemplatesRequest(_message.Message):
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

class ListSessionTemplatesResponse(_message.Message):
    __slots__ = ('session_templates', 'next_page_token')
    SESSION_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    session_templates: _containers.RepeatedCompositeFieldContainer[SessionTemplate]
    next_page_token: str

    def __init__(self, session_templates: _Optional[_Iterable[_Union[SessionTemplate, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteSessionTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SessionTemplate(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'jupyter_session', 'spark_connect_session', 'creator', 'labels', 'runtime_config', 'environment_config', 'update_time', 'uuid')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    JUPYTER_SESSION_FIELD_NUMBER: _ClassVar[int]
    SPARK_CONNECT_SESSION_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    jupyter_session: _sessions_pb2.JupyterConfig
    spark_connect_session: _sessions_pb2.SparkConnectConfig
    creator: str
    labels: _containers.ScalarMap[str, str]
    runtime_config: _shared_pb2.RuntimeConfig
    environment_config: _shared_pb2.EnvironmentConfig
    update_time: _timestamp_pb2.Timestamp
    uuid: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., jupyter_session: _Optional[_Union[_sessions_pb2.JupyterConfig, _Mapping]]=..., spark_connect_session: _Optional[_Union[_sessions_pb2.SparkConnectConfig, _Mapping]]=..., creator: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., runtime_config: _Optional[_Union[_shared_pb2.RuntimeConfig, _Mapping]]=..., environment_config: _Optional[_Union[_shared_pb2.EnvironmentConfig, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., uuid: _Optional[str]=...) -> None:
        ...