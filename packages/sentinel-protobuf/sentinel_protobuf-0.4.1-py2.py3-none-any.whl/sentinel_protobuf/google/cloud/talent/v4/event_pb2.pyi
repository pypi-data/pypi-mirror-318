from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ClientEvent(_message.Message):
    __slots__ = ('request_id', 'event_id', 'create_time', 'job_event', 'event_notes')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_EVENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_NOTES_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    event_id: str
    create_time: _timestamp_pb2.Timestamp
    job_event: JobEvent
    event_notes: str

    def __init__(self, request_id: _Optional[str]=..., event_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., job_event: _Optional[_Union[JobEvent, _Mapping]]=..., event_notes: _Optional[str]=...) -> None:
        ...

class JobEvent(_message.Message):
    __slots__ = ('type', 'jobs')

    class JobEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_EVENT_TYPE_UNSPECIFIED: _ClassVar[JobEvent.JobEventType]
        IMPRESSION: _ClassVar[JobEvent.JobEventType]
        VIEW: _ClassVar[JobEvent.JobEventType]
        VIEW_REDIRECT: _ClassVar[JobEvent.JobEventType]
        APPLICATION_START: _ClassVar[JobEvent.JobEventType]
        APPLICATION_FINISH: _ClassVar[JobEvent.JobEventType]
        APPLICATION_QUICK_SUBMISSION: _ClassVar[JobEvent.JobEventType]
        APPLICATION_REDIRECT: _ClassVar[JobEvent.JobEventType]
        APPLICATION_START_FROM_SEARCH: _ClassVar[JobEvent.JobEventType]
        APPLICATION_REDIRECT_FROM_SEARCH: _ClassVar[JobEvent.JobEventType]
        APPLICATION_COMPANY_SUBMIT: _ClassVar[JobEvent.JobEventType]
        BOOKMARK: _ClassVar[JobEvent.JobEventType]
        NOTIFICATION: _ClassVar[JobEvent.JobEventType]
        HIRED: _ClassVar[JobEvent.JobEventType]
        SENT_CV: _ClassVar[JobEvent.JobEventType]
        INTERVIEW_GRANTED: _ClassVar[JobEvent.JobEventType]
    JOB_EVENT_TYPE_UNSPECIFIED: JobEvent.JobEventType
    IMPRESSION: JobEvent.JobEventType
    VIEW: JobEvent.JobEventType
    VIEW_REDIRECT: JobEvent.JobEventType
    APPLICATION_START: JobEvent.JobEventType
    APPLICATION_FINISH: JobEvent.JobEventType
    APPLICATION_QUICK_SUBMISSION: JobEvent.JobEventType
    APPLICATION_REDIRECT: JobEvent.JobEventType
    APPLICATION_START_FROM_SEARCH: JobEvent.JobEventType
    APPLICATION_REDIRECT_FROM_SEARCH: JobEvent.JobEventType
    APPLICATION_COMPANY_SUBMIT: JobEvent.JobEventType
    BOOKMARK: JobEvent.JobEventType
    NOTIFICATION: JobEvent.JobEventType
    HIRED: JobEvent.JobEventType
    SENT_CV: JobEvent.JobEventType
    INTERVIEW_GRANTED: JobEvent.JobEventType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    type: JobEvent.JobEventType
    jobs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, type: _Optional[_Union[JobEvent.JobEventType, str]]=..., jobs: _Optional[_Iterable[str]]=...) -> None:
        ...