from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SpecialistPool(_message.Message):
    __slots__ = ('name', 'display_name', 'specialist_managers_count', 'specialist_manager_emails', 'pending_data_labeling_jobs', 'specialist_worker_emails')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIALIST_MANAGERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPECIALIST_MANAGER_EMAILS_FIELD_NUMBER: _ClassVar[int]
    PENDING_DATA_LABELING_JOBS_FIELD_NUMBER: _ClassVar[int]
    SPECIALIST_WORKER_EMAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    specialist_managers_count: int
    specialist_manager_emails: _containers.RepeatedScalarFieldContainer[str]
    pending_data_labeling_jobs: _containers.RepeatedScalarFieldContainer[str]
    specialist_worker_emails: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., specialist_managers_count: _Optional[int]=..., specialist_manager_emails: _Optional[_Iterable[str]]=..., pending_data_labeling_jobs: _Optional[_Iterable[str]]=..., specialist_worker_emails: _Optional[_Iterable[str]]=...) -> None:
        ...