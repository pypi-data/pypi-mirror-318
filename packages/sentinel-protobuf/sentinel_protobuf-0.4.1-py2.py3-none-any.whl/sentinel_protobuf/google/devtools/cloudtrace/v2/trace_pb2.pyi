from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Span(_message.Message):
    __slots__ = ('name', 'span_id', 'parent_span_id', 'display_name', 'start_time', 'end_time', 'attributes', 'stack_trace', 'time_events', 'links', 'status', 'same_process_as_parent_span', 'child_span_count', 'span_kind')

    class SpanKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPAN_KIND_UNSPECIFIED: _ClassVar[Span.SpanKind]
        INTERNAL: _ClassVar[Span.SpanKind]
        SERVER: _ClassVar[Span.SpanKind]
        CLIENT: _ClassVar[Span.SpanKind]
        PRODUCER: _ClassVar[Span.SpanKind]
        CONSUMER: _ClassVar[Span.SpanKind]
    SPAN_KIND_UNSPECIFIED: Span.SpanKind
    INTERNAL: Span.SpanKind
    SERVER: Span.SpanKind
    CLIENT: Span.SpanKind
    PRODUCER: Span.SpanKind
    CONSUMER: Span.SpanKind

    class Attributes(_message.Message):
        __slots__ = ('attribute_map', 'dropped_attributes_count')

        class AttributeMapEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: AttributeValue

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValue, _Mapping]]=...) -> None:
                ...
        ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
        DROPPED_ATTRIBUTES_COUNT_FIELD_NUMBER: _ClassVar[int]
        attribute_map: _containers.MessageMap[str, AttributeValue]
        dropped_attributes_count: int

        def __init__(self, attribute_map: _Optional[_Mapping[str, AttributeValue]]=..., dropped_attributes_count: _Optional[int]=...) -> None:
            ...

    class TimeEvent(_message.Message):
        __slots__ = ('time', 'annotation', 'message_event')

        class Annotation(_message.Message):
            __slots__ = ('description', 'attributes')
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
            description: TruncatableString
            attributes: Span.Attributes

            def __init__(self, description: _Optional[_Union[TruncatableString, _Mapping]]=..., attributes: _Optional[_Union[Span.Attributes, _Mapping]]=...) -> None:
                ...

        class MessageEvent(_message.Message):
            __slots__ = ('type', 'id', 'uncompressed_size_bytes', 'compressed_size_bytes')

            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNSPECIFIED: _ClassVar[Span.TimeEvent.MessageEvent.Type]
                SENT: _ClassVar[Span.TimeEvent.MessageEvent.Type]
                RECEIVED: _ClassVar[Span.TimeEvent.MessageEvent.Type]
            TYPE_UNSPECIFIED: Span.TimeEvent.MessageEvent.Type
            SENT: Span.TimeEvent.MessageEvent.Type
            RECEIVED: Span.TimeEvent.MessageEvent.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            UNCOMPRESSED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
            COMPRESSED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
            type: Span.TimeEvent.MessageEvent.Type
            id: int
            uncompressed_size_bytes: int
            compressed_size_bytes: int

            def __init__(self, type: _Optional[_Union[Span.TimeEvent.MessageEvent.Type, str]]=..., id: _Optional[int]=..., uncompressed_size_bytes: _Optional[int]=..., compressed_size_bytes: _Optional[int]=...) -> None:
                ...
        TIME_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
        time: _timestamp_pb2.Timestamp
        annotation: Span.TimeEvent.Annotation
        message_event: Span.TimeEvent.MessageEvent

        def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotation: _Optional[_Union[Span.TimeEvent.Annotation, _Mapping]]=..., message_event: _Optional[_Union[Span.TimeEvent.MessageEvent, _Mapping]]=...) -> None:
            ...

    class TimeEvents(_message.Message):
        __slots__ = ('time_event', 'dropped_annotations_count', 'dropped_message_events_count')
        TIME_EVENT_FIELD_NUMBER: _ClassVar[int]
        DROPPED_ANNOTATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        DROPPED_MESSAGE_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        time_event: _containers.RepeatedCompositeFieldContainer[Span.TimeEvent]
        dropped_annotations_count: int
        dropped_message_events_count: int

        def __init__(self, time_event: _Optional[_Iterable[_Union[Span.TimeEvent, _Mapping]]]=..., dropped_annotations_count: _Optional[int]=..., dropped_message_events_count: _Optional[int]=...) -> None:
            ...

    class Link(_message.Message):
        __slots__ = ('trace_id', 'span_id', 'type', 'attributes')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Span.Link.Type]
            CHILD_LINKED_SPAN: _ClassVar[Span.Link.Type]
            PARENT_LINKED_SPAN: _ClassVar[Span.Link.Type]
        TYPE_UNSPECIFIED: Span.Link.Type
        CHILD_LINKED_SPAN: Span.Link.Type
        PARENT_LINKED_SPAN: Span.Link.Type
        TRACE_ID_FIELD_NUMBER: _ClassVar[int]
        SPAN_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        trace_id: str
        span_id: str
        type: Span.Link.Type
        attributes: Span.Attributes

        def __init__(self, trace_id: _Optional[str]=..., span_id: _Optional[str]=..., type: _Optional[_Union[Span.Link.Type, str]]=..., attributes: _Optional[_Union[Span.Attributes, _Mapping]]=...) -> None:
            ...

    class Links(_message.Message):
        __slots__ = ('link', 'dropped_links_count')
        LINK_FIELD_NUMBER: _ClassVar[int]
        DROPPED_LINKS_COUNT_FIELD_NUMBER: _ClassVar[int]
        link: _containers.RepeatedCompositeFieldContainer[Span.Link]
        dropped_links_count: int

        def __init__(self, link: _Optional[_Iterable[_Union[Span.Link, _Mapping]]]=..., dropped_links_count: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    TIME_EVENTS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SAME_PROCESS_AS_PARENT_SPAN_FIELD_NUMBER: _ClassVar[int]
    CHILD_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPAN_KIND_FIELD_NUMBER: _ClassVar[int]
    name: str
    span_id: str
    parent_span_id: str
    display_name: TruncatableString
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    attributes: Span.Attributes
    stack_trace: StackTrace
    time_events: Span.TimeEvents
    links: Span.Links
    status: _status_pb2.Status
    same_process_as_parent_span: _wrappers_pb2.BoolValue
    child_span_count: _wrappers_pb2.Int32Value
    span_kind: Span.SpanKind

    def __init__(self, name: _Optional[str]=..., span_id: _Optional[str]=..., parent_span_id: _Optional[str]=..., display_name: _Optional[_Union[TruncatableString, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., attributes: _Optional[_Union[Span.Attributes, _Mapping]]=..., stack_trace: _Optional[_Union[StackTrace, _Mapping]]=..., time_events: _Optional[_Union[Span.TimeEvents, _Mapping]]=..., links: _Optional[_Union[Span.Links, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., same_process_as_parent_span: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., child_span_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., span_kind: _Optional[_Union[Span.SpanKind, str]]=...) -> None:
        ...

class AttributeValue(_message.Message):
    __slots__ = ('string_value', 'int_value', 'bool_value')
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: TruncatableString
    int_value: int
    bool_value: bool

    def __init__(self, string_value: _Optional[_Union[TruncatableString, _Mapping]]=..., int_value: _Optional[int]=..., bool_value: bool=...) -> None:
        ...

class StackTrace(_message.Message):
    __slots__ = ('stack_frames', 'stack_trace_hash_id')

    class StackFrame(_message.Message):
        __slots__ = ('function_name', 'original_function_name', 'file_name', 'line_number', 'column_number', 'load_module', 'source_version')
        FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        COLUMN_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LOAD_MODULE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
        function_name: TruncatableString
        original_function_name: TruncatableString
        file_name: TruncatableString
        line_number: int
        column_number: int
        load_module: Module
        source_version: TruncatableString

        def __init__(self, function_name: _Optional[_Union[TruncatableString, _Mapping]]=..., original_function_name: _Optional[_Union[TruncatableString, _Mapping]]=..., file_name: _Optional[_Union[TruncatableString, _Mapping]]=..., line_number: _Optional[int]=..., column_number: _Optional[int]=..., load_module: _Optional[_Union[Module, _Mapping]]=..., source_version: _Optional[_Union[TruncatableString, _Mapping]]=...) -> None:
            ...

    class StackFrames(_message.Message):
        __slots__ = ('frame', 'dropped_frames_count')
        FRAME_FIELD_NUMBER: _ClassVar[int]
        DROPPED_FRAMES_COUNT_FIELD_NUMBER: _ClassVar[int]
        frame: _containers.RepeatedCompositeFieldContainer[StackTrace.StackFrame]
        dropped_frames_count: int

        def __init__(self, frame: _Optional[_Iterable[_Union[StackTrace.StackFrame, _Mapping]]]=..., dropped_frames_count: _Optional[int]=...) -> None:
            ...
    STACK_FRAMES_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_HASH_ID_FIELD_NUMBER: _ClassVar[int]
    stack_frames: StackTrace.StackFrames
    stack_trace_hash_id: int

    def __init__(self, stack_frames: _Optional[_Union[StackTrace.StackFrames, _Mapping]]=..., stack_trace_hash_id: _Optional[int]=...) -> None:
        ...

class Module(_message.Message):
    __slots__ = ('module', 'build_id')
    MODULE_FIELD_NUMBER: _ClassVar[int]
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    module: TruncatableString
    build_id: TruncatableString

    def __init__(self, module: _Optional[_Union[TruncatableString, _Mapping]]=..., build_id: _Optional[_Union[TruncatableString, _Mapping]]=...) -> None:
        ...

class TruncatableString(_message.Message):
    __slots__ = ('value', 'truncated_byte_count')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    value: str
    truncated_byte_count: int

    def __init__(self, value: _Optional[str]=..., truncated_byte_count: _Optional[int]=...) -> None:
        ...