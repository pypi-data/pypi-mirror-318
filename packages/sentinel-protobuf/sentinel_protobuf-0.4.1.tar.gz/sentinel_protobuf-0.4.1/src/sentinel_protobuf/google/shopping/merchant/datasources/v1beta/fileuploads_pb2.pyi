from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileUpload(_message.Message):
    __slots__ = ('name', 'data_source_id', 'processing_state', 'issues', 'items_total', 'items_created', 'items_updated', 'upload_time')

    class ProcessingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROCESSING_STATE_UNSPECIFIED: _ClassVar[FileUpload.ProcessingState]
        FAILED: _ClassVar[FileUpload.ProcessingState]
        IN_PROGRESS: _ClassVar[FileUpload.ProcessingState]
        SUCCEEDED: _ClassVar[FileUpload.ProcessingState]
    PROCESSING_STATE_UNSPECIFIED: FileUpload.ProcessingState
    FAILED: FileUpload.ProcessingState
    IN_PROGRESS: FileUpload.ProcessingState
    SUCCEEDED: FileUpload.ProcessingState

    class Issue(_message.Message):
        __slots__ = ('title', 'description', 'code', 'count', 'severity', 'documentation_uri')

        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[FileUpload.Issue.Severity]
            WARNING: _ClassVar[FileUpload.Issue.Severity]
            ERROR: _ClassVar[FileUpload.Issue.Severity]
        SEVERITY_UNSPECIFIED: FileUpload.Issue.Severity
        WARNING: FileUpload.Issue.Severity
        ERROR: FileUpload.Issue.Severity
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_URI_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        code: str
        count: int
        severity: FileUpload.Issue.Severity
        documentation_uri: str

        def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., code: _Optional[str]=..., count: _Optional[int]=..., severity: _Optional[_Union[FileUpload.Issue.Severity, str]]=..., documentation_uri: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_STATE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_CREATED_FIELD_NUMBER: _ClassVar[int]
    ITEMS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_source_id: int
    processing_state: FileUpload.ProcessingState
    issues: _containers.RepeatedCompositeFieldContainer[FileUpload.Issue]
    items_total: int
    items_created: int
    items_updated: int
    upload_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., data_source_id: _Optional[int]=..., processing_state: _Optional[_Union[FileUpload.ProcessingState, str]]=..., issues: _Optional[_Iterable[_Union[FileUpload.Issue, _Mapping]]]=..., items_total: _Optional[int]=..., items_created: _Optional[int]=..., items_updated: _Optional[int]=..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetFileUploadRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...