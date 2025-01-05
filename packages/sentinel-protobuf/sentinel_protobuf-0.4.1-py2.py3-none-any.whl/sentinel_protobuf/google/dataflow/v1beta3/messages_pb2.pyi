from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobMessageImportance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_MESSAGE_IMPORTANCE_UNKNOWN: _ClassVar[JobMessageImportance]
    JOB_MESSAGE_DEBUG: _ClassVar[JobMessageImportance]
    JOB_MESSAGE_DETAILED: _ClassVar[JobMessageImportance]
    JOB_MESSAGE_BASIC: _ClassVar[JobMessageImportance]
    JOB_MESSAGE_WARNING: _ClassVar[JobMessageImportance]
    JOB_MESSAGE_ERROR: _ClassVar[JobMessageImportance]
JOB_MESSAGE_IMPORTANCE_UNKNOWN: JobMessageImportance
JOB_MESSAGE_DEBUG: JobMessageImportance
JOB_MESSAGE_DETAILED: JobMessageImportance
JOB_MESSAGE_BASIC: JobMessageImportance
JOB_MESSAGE_WARNING: JobMessageImportance
JOB_MESSAGE_ERROR: JobMessageImportance

class JobMessage(_message.Message):
    __slots__ = ('id', 'time', 'message_text', 'message_importance')
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    time: _timestamp_pb2.Timestamp
    message_text: str
    message_importance: JobMessageImportance

    def __init__(self, id: _Optional[str]=..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message_text: _Optional[str]=..., message_importance: _Optional[_Union[JobMessageImportance, str]]=...) -> None:
        ...

class StructuredMessage(_message.Message):
    __slots__ = ('message_text', 'message_key', 'parameters')

    class Parameter(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    MESSAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    message_text: str
    message_key: str
    parameters: _containers.RepeatedCompositeFieldContainer[StructuredMessage.Parameter]

    def __init__(self, message_text: _Optional[str]=..., message_key: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[StructuredMessage.Parameter, _Mapping]]]=...) -> None:
        ...

class AutoscalingEvent(_message.Message):
    __slots__ = ('current_num_workers', 'target_num_workers', 'event_type', 'description', 'time', 'worker_pool')

    class AutoscalingEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[AutoscalingEvent.AutoscalingEventType]
        TARGET_NUM_WORKERS_CHANGED: _ClassVar[AutoscalingEvent.AutoscalingEventType]
        CURRENT_NUM_WORKERS_CHANGED: _ClassVar[AutoscalingEvent.AutoscalingEventType]
        ACTUATION_FAILURE: _ClassVar[AutoscalingEvent.AutoscalingEventType]
        NO_CHANGE: _ClassVar[AutoscalingEvent.AutoscalingEventType]
    TYPE_UNKNOWN: AutoscalingEvent.AutoscalingEventType
    TARGET_NUM_WORKERS_CHANGED: AutoscalingEvent.AutoscalingEventType
    CURRENT_NUM_WORKERS_CHANGED: AutoscalingEvent.AutoscalingEventType
    ACTUATION_FAILURE: AutoscalingEvent.AutoscalingEventType
    NO_CHANGE: AutoscalingEvent.AutoscalingEventType
    CURRENT_NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    current_num_workers: int
    target_num_workers: int
    event_type: AutoscalingEvent.AutoscalingEventType
    description: StructuredMessage
    time: _timestamp_pb2.Timestamp
    worker_pool: str

    def __init__(self, current_num_workers: _Optional[int]=..., target_num_workers: _Optional[int]=..., event_type: _Optional[_Union[AutoscalingEvent.AutoscalingEventType, str]]=..., description: _Optional[_Union[StructuredMessage, _Mapping]]=..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., worker_pool: _Optional[str]=...) -> None:
        ...

class ListJobMessagesRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'minimum_importance', 'page_size', 'page_token', 'start_time', 'end_time', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    minimum_importance: JobMessageImportance
    page_size: int
    page_token: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., minimum_importance: _Optional[_Union[JobMessageImportance, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class ListJobMessagesResponse(_message.Message):
    __slots__ = ('job_messages', 'next_page_token', 'autoscaling_events')
    JOB_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_EVENTS_FIELD_NUMBER: _ClassVar[int]
    job_messages: _containers.RepeatedCompositeFieldContainer[JobMessage]
    next_page_token: str
    autoscaling_events: _containers.RepeatedCompositeFieldContainer[AutoscalingEvent]

    def __init__(self, job_messages: _Optional[_Iterable[_Union[JobMessage, _Mapping]]]=..., next_page_token: _Optional[str]=..., autoscaling_events: _Optional[_Iterable[_Union[AutoscalingEvent, _Mapping]]]=...) -> None:
        ...