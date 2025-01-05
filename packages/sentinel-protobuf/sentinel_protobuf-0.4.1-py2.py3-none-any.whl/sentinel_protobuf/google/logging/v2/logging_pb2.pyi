from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.api import resource_pb2 as _resource_pb2
from google.logging.v2 import log_entry_pb2 as _log_entry_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeleteLogRequest(_message.Message):
    __slots__ = ('log_name',)
    LOG_NAME_FIELD_NUMBER: _ClassVar[int]
    log_name: str

    def __init__(self, log_name: _Optional[str]=...) -> None:
        ...

class WriteLogEntriesRequest(_message.Message):
    __slots__ = ('log_name', 'resource', 'labels', 'entries', 'partial_success', 'dry_run')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    LOG_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    log_name: str
    resource: _monitored_resource_pb2.MonitoredResource
    labels: _containers.ScalarMap[str, str]
    entries: _containers.RepeatedCompositeFieldContainer[_log_entry_pb2.LogEntry]
    partial_success: bool
    dry_run: bool

    def __init__(self, log_name: _Optional[str]=..., resource: _Optional[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., entries: _Optional[_Iterable[_Union[_log_entry_pb2.LogEntry, _Mapping]]]=..., partial_success: bool=..., dry_run: bool=...) -> None:
        ...

class WriteLogEntriesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WriteLogEntriesPartialErrors(_message.Message):
    __slots__ = ('log_entry_errors',)

    class LogEntryErrorsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _status_pb2.Status

        def __init__(self, key: _Optional[int]=..., value: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    LOG_ENTRY_ERRORS_FIELD_NUMBER: _ClassVar[int]
    log_entry_errors: _containers.MessageMap[int, _status_pb2.Status]

    def __init__(self, log_entry_errors: _Optional[_Mapping[int, _status_pb2.Status]]=...) -> None:
        ...

class ListLogEntriesRequest(_message.Message):
    __slots__ = ('resource_names', 'filter', 'order_by', 'page_size', 'page_token')
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_names: _containers.RepeatedScalarFieldContainer[str]
    filter: str
    order_by: str
    page_size: int
    page_token: str

    def __init__(self, resource_names: _Optional[_Iterable[str]]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLogEntriesResponse(_message.Message):
    __slots__ = ('entries', 'next_page_token')
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_log_entry_pb2.LogEntry]
    next_page_token: str

    def __init__(self, entries: _Optional[_Iterable[_Union[_log_entry_pb2.LogEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListMonitoredResourceDescriptorsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMonitoredResourceDescriptorsResponse(_message.Message):
    __slots__ = ('resource_descriptors', 'next_page_token')
    RESOURCE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_descriptors: _containers.RepeatedCompositeFieldContainer[_monitored_resource_pb2.MonitoredResourceDescriptor]
    next_page_token: str

    def __init__(self, resource_descriptors: _Optional[_Iterable[_Union[_monitored_resource_pb2.MonitoredResourceDescriptor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListLogsRequest(_message.Message):
    __slots__ = ('parent', 'resource_names', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    resource_names: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., resource_names: _Optional[_Iterable[str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLogsResponse(_message.Message):
    __slots__ = ('log_names', 'next_page_token')
    LOG_NAMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    log_names: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, log_names: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class TailLogEntriesRequest(_message.Message):
    __slots__ = ('resource_names', 'filter', 'buffer_window')
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    BUFFER_WINDOW_FIELD_NUMBER: _ClassVar[int]
    resource_names: _containers.RepeatedScalarFieldContainer[str]
    filter: str
    buffer_window: _duration_pb2.Duration

    def __init__(self, resource_names: _Optional[_Iterable[str]]=..., filter: _Optional[str]=..., buffer_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class TailLogEntriesResponse(_message.Message):
    __slots__ = ('entries', 'suppression_info')

    class SuppressionInfo(_message.Message):
        __slots__ = ('reason', 'suppressed_count')

        class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            REASON_UNSPECIFIED: _ClassVar[TailLogEntriesResponse.SuppressionInfo.Reason]
            RATE_LIMIT: _ClassVar[TailLogEntriesResponse.SuppressionInfo.Reason]
            NOT_CONSUMED: _ClassVar[TailLogEntriesResponse.SuppressionInfo.Reason]
        REASON_UNSPECIFIED: TailLogEntriesResponse.SuppressionInfo.Reason
        RATE_LIMIT: TailLogEntriesResponse.SuppressionInfo.Reason
        NOT_CONSUMED: TailLogEntriesResponse.SuppressionInfo.Reason
        REASON_FIELD_NUMBER: _ClassVar[int]
        SUPPRESSED_COUNT_FIELD_NUMBER: _ClassVar[int]
        reason: TailLogEntriesResponse.SuppressionInfo.Reason
        suppressed_count: int

        def __init__(self, reason: _Optional[_Union[TailLogEntriesResponse.SuppressionInfo.Reason, str]]=..., suppressed_count: _Optional[int]=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_log_entry_pb2.LogEntry]
    suppression_info: _containers.RepeatedCompositeFieldContainer[TailLogEntriesResponse.SuppressionInfo]

    def __init__(self, entries: _Optional[_Iterable[_Union[_log_entry_pb2.LogEntry, _Mapping]]]=..., suppression_info: _Optional[_Iterable[_Union[TailLogEntriesResponse.SuppressionInfo, _Mapping]]]=...) -> None:
        ...