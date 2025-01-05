from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Trace(_message.Message):
    __slots__ = ('project_id', 'trace_id', 'spans')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    trace_id: str
    spans: _containers.RepeatedCompositeFieldContainer[TraceSpan]

    def __init__(self, project_id: _Optional[str]=..., trace_id: _Optional[str]=..., spans: _Optional[_Iterable[_Union[TraceSpan, _Mapping]]]=...) -> None:
        ...

class Traces(_message.Message):
    __slots__ = ('traces',)
    TRACES_FIELD_NUMBER: _ClassVar[int]
    traces: _containers.RepeatedCompositeFieldContainer[Trace]

    def __init__(self, traces: _Optional[_Iterable[_Union[Trace, _Mapping]]]=...) -> None:
        ...

class TraceSpan(_message.Message):
    __slots__ = ('span_id', 'kind', 'name', 'start_time', 'end_time', 'parent_span_id', 'labels')

    class SpanKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPAN_KIND_UNSPECIFIED: _ClassVar[TraceSpan.SpanKind]
        RPC_SERVER: _ClassVar[TraceSpan.SpanKind]
        RPC_CLIENT: _ClassVar[TraceSpan.SpanKind]
    SPAN_KIND_UNSPECIFIED: TraceSpan.SpanKind
    RPC_SERVER: TraceSpan.SpanKind
    RPC_CLIENT: TraceSpan.SpanKind

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    span_id: int
    kind: TraceSpan.SpanKind
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    parent_span_id: int
    labels: _containers.ScalarMap[str, str]

    def __init__(self, span_id: _Optional[int]=..., kind: _Optional[_Union[TraceSpan.SpanKind, str]]=..., name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., parent_span_id: _Optional[int]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListTracesRequest(_message.Message):
    __slots__ = ('project_id', 'view', 'page_size', 'page_token', 'start_time', 'end_time', 'filter', 'order_by')

    class ViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIEW_TYPE_UNSPECIFIED: _ClassVar[ListTracesRequest.ViewType]
        MINIMAL: _ClassVar[ListTracesRequest.ViewType]
        ROOTSPAN: _ClassVar[ListTracesRequest.ViewType]
        COMPLETE: _ClassVar[ListTracesRequest.ViewType]
    VIEW_TYPE_UNSPECIFIED: ListTracesRequest.ViewType
    MINIMAL: ListTracesRequest.ViewType
    ROOTSPAN: ListTracesRequest.ViewType
    COMPLETE: ListTracesRequest.ViewType
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    view: ListTracesRequest.ViewType
    page_size: int
    page_token: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    filter: str
    order_by: str

    def __init__(self, project_id: _Optional[str]=..., view: _Optional[_Union[ListTracesRequest.ViewType, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListTracesResponse(_message.Message):
    __slots__ = ('traces', 'next_page_token')
    TRACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    traces: _containers.RepeatedCompositeFieldContainer[Trace]
    next_page_token: str

    def __init__(self, traces: _Optional[_Iterable[_Union[Trace, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTraceRequest(_message.Message):
    __slots__ = ('project_id', 'trace_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    trace_id: str

    def __init__(self, project_id: _Optional[str]=..., trace_id: _Optional[str]=...) -> None:
        ...

class PatchTracesRequest(_message.Message):
    __slots__ = ('project_id', 'traces')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRACES_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    traces: Traces

    def __init__(self, project_id: _Optional[str]=..., traces: _Optional[_Union[Traces, _Mapping]]=...) -> None:
        ...