from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Process(_message.Message):
    __slots__ = ('name', 'display_name', 'attributes', 'origin')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    attributes: _containers.MessageMap[str, _struct_pb2.Value]
    origin: Origin

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., attributes: _Optional[_Mapping[str, _struct_pb2.Value]]=..., origin: _Optional[_Union[Origin, _Mapping]]=...) -> None:
        ...

class Run(_message.Message):
    __slots__ = ('name', 'display_name', 'attributes', 'start_time', 'end_time', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Run.State]
        STARTED: _ClassVar[Run.State]
        COMPLETED: _ClassVar[Run.State]
        FAILED: _ClassVar[Run.State]
        ABORTED: _ClassVar[Run.State]
    UNKNOWN: Run.State
    STARTED: Run.State
    COMPLETED: Run.State
    FAILED: Run.State
    ABORTED: Run.State

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    attributes: _containers.MessageMap[str, _struct_pb2.Value]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Run.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., attributes: _Optional[_Mapping[str, _struct_pb2.Value]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Run.State, str]]=...) -> None:
        ...

class LineageEvent(_message.Message):
    __slots__ = ('name', 'links', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    links: _containers.RepeatedCompositeFieldContainer[EventLink]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., links: _Optional[_Iterable[_Union[EventLink, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EventLink(_message.Message):
    __slots__ = ('source', 'target')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    source: EntityReference
    target: EntityReference

    def __init__(self, source: _Optional[_Union[EntityReference, _Mapping]]=..., target: _Optional[_Union[EntityReference, _Mapping]]=...) -> None:
        ...

class EntityReference(_message.Message):
    __slots__ = ('fully_qualified_name',)
    FULLY_QUALIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    fully_qualified_name: str

    def __init__(self, fully_qualified_name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('state', 'operation_type', 'resource', 'resource_uuid', 'create_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[OperationMetadata.State]
        PENDING: _ClassVar[OperationMetadata.State]
        RUNNING: _ClassVar[OperationMetadata.State]
        SUCCEEDED: _ClassVar[OperationMetadata.State]
        FAILED: _ClassVar[OperationMetadata.State]
    STATE_UNSPECIFIED: OperationMetadata.State
    PENDING: OperationMetadata.State
    RUNNING: OperationMetadata.State
    SUCCEEDED: OperationMetadata.State
    FAILED: OperationMetadata.State

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[OperationMetadata.Type]
        DELETE: _ClassVar[OperationMetadata.Type]
        CREATE: _ClassVar[OperationMetadata.Type]
    TYPE_UNSPECIFIED: OperationMetadata.Type
    DELETE: OperationMetadata.Type
    CREATE: OperationMetadata.Type
    STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    state: OperationMetadata.State
    operation_type: OperationMetadata.Type
    resource: str
    resource_uuid: str
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[OperationMetadata.State, str]]=..., operation_type: _Optional[_Union[OperationMetadata.Type, str]]=..., resource: _Optional[str]=..., resource_uuid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ProcessOpenLineageRunEventRequest(_message.Message):
    __slots__ = ('parent', 'open_lineage', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPEN_LINEAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    open_lineage: _struct_pb2.Struct
    request_id: str

    def __init__(self, parent: _Optional[str]=..., open_lineage: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ProcessOpenLineageRunEventResponse(_message.Message):
    __slots__ = ('process', 'run', 'lineage_events')
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    LINEAGE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    process: str
    run: str
    lineage_events: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, process: _Optional[str]=..., run: _Optional[str]=..., lineage_events: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateProcessRequest(_message.Message):
    __slots__ = ('parent', 'process', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    process: Process
    request_id: str

    def __init__(self, parent: _Optional[str]=..., process: _Optional[_Union[Process, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateProcessRequest(_message.Message):
    __slots__ = ('process', 'update_mask', 'allow_missing')
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    process: Process
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, process: _Optional[_Union[Process, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class GetProcessRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListProcessesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProcessesResponse(_message.Message):
    __slots__ = ('processes', 'next_page_token')
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    processes: _containers.RepeatedCompositeFieldContainer[Process]
    next_page_token: str

    def __init__(self, processes: _Optional[_Iterable[_Union[Process, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteProcessRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class CreateRunRequest(_message.Message):
    __slots__ = ('parent', 'run', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    run: Run
    request_id: str

    def __init__(self, parent: _Optional[str]=..., run: _Optional[_Union[Run, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateRunRequest(_message.Message):
    __slots__ = ('run', 'update_mask', 'allow_missing')
    RUN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    run: Run
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool

    def __init__(self, run: _Optional[_Union[Run, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class GetRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRunsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRunsResponse(_message.Message):
    __slots__ = ('runs', 'next_page_token')
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[Run]
    next_page_token: str

    def __init__(self, runs: _Optional[_Iterable[_Union[Run, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteRunRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class CreateLineageEventRequest(_message.Message):
    __slots__ = ('parent', 'lineage_event', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LINEAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lineage_event: LineageEvent
    request_id: str

    def __init__(self, parent: _Optional[str]=..., lineage_event: _Optional[_Union[LineageEvent, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetLineageEventRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListLineageEventsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLineageEventsResponse(_message.Message):
    __slots__ = ('lineage_events', 'next_page_token')
    LINEAGE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    lineage_events: _containers.RepeatedCompositeFieldContainer[LineageEvent]
    next_page_token: str

    def __init__(self, lineage_events: _Optional[_Iterable[_Union[LineageEvent, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteLineageEventRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class SearchLinksRequest(_message.Message):
    __slots__ = ('parent', 'source', 'target', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source: EntityReference
    target: EntityReference
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., source: _Optional[_Union[EntityReference, _Mapping]]=..., target: _Optional[_Union[EntityReference, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchLinksResponse(_message.Message):
    __slots__ = ('links', 'next_page_token')
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[Link]
    next_page_token: str

    def __init__(self, links: _Optional[_Iterable[_Union[Link, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Link(_message.Message):
    __slots__ = ('name', 'source', 'target', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source: EntityReference
    target: EntityReference
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., source: _Optional[_Union[EntityReference, _Mapping]]=..., target: _Optional[_Union[EntityReference, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchSearchLinkProcessesRequest(_message.Message):
    __slots__ = ('parent', 'links', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    links: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., links: _Optional[_Iterable[str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class BatchSearchLinkProcessesResponse(_message.Message):
    __slots__ = ('process_links', 'next_page_token')
    PROCESS_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    process_links: _containers.RepeatedCompositeFieldContainer[ProcessLinks]
    next_page_token: str

    def __init__(self, process_links: _Optional[_Iterable[_Union[ProcessLinks, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ProcessLinks(_message.Message):
    __slots__ = ('process', 'links')
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    process: str
    links: _containers.RepeatedCompositeFieldContainer[ProcessLinkInfo]

    def __init__(self, process: _Optional[str]=..., links: _Optional[_Iterable[_Union[ProcessLinkInfo, _Mapping]]]=...) -> None:
        ...

class ProcessLinkInfo(_message.Message):
    __slots__ = ('link', 'start_time', 'end_time')
    LINK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    link: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, link: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Origin(_message.Message):
    __slots__ = ('source_type', 'name')

    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_UNSPECIFIED: _ClassVar[Origin.SourceType]
        CUSTOM: _ClassVar[Origin.SourceType]
        BIGQUERY: _ClassVar[Origin.SourceType]
        DATA_FUSION: _ClassVar[Origin.SourceType]
        COMPOSER: _ClassVar[Origin.SourceType]
        LOOKER_STUDIO: _ClassVar[Origin.SourceType]
        DATAPROC: _ClassVar[Origin.SourceType]
    SOURCE_TYPE_UNSPECIFIED: Origin.SourceType
    CUSTOM: Origin.SourceType
    BIGQUERY: Origin.SourceType
    DATA_FUSION: Origin.SourceType
    COMPOSER: Origin.SourceType
    LOOKER_STUDIO: Origin.SourceType
    DATAPROC: Origin.SourceType
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    source_type: Origin.SourceType
    name: str

    def __init__(self, source_type: _Optional[_Union[Origin.SourceType, str]]=..., name: _Optional[str]=...) -> None:
        ...