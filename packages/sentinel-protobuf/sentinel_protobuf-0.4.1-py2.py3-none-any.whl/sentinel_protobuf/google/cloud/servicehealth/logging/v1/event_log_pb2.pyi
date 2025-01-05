from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventLog(_message.Message):
    __slots__ = ('title', 'description', 'category', 'state', 'detailed_state', 'impacted_products', 'impacted_locations', 'relevance', 'parent_event', 'update_time', 'start_time', 'end_time', 'next_update_time')

    class EventCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_CATEGORY_UNSPECIFIED: _ClassVar[EventLog.EventCategory]
        INCIDENT: _ClassVar[EventLog.EventCategory]
    EVENT_CATEGORY_UNSPECIFIED: EventLog.EventCategory
    INCIDENT: EventLog.EventCategory

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[EventLog.State]
        ACTIVE: _ClassVar[EventLog.State]
        CLOSED: _ClassVar[EventLog.State]
    STATE_UNSPECIFIED: EventLog.State
    ACTIVE: EventLog.State
    CLOSED: EventLog.State

    class DetailedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETAILED_STATE_UNSPECIFIED: _ClassVar[EventLog.DetailedState]
        EMERGING: _ClassVar[EventLog.DetailedState]
        CONFIRMED: _ClassVar[EventLog.DetailedState]
        RESOLVED: _ClassVar[EventLog.DetailedState]
        MERGED: _ClassVar[EventLog.DetailedState]
    DETAILED_STATE_UNSPECIFIED: EventLog.DetailedState
    EMERGING: EventLog.DetailedState
    CONFIRMED: EventLog.DetailedState
    RESOLVED: EventLog.DetailedState
    MERGED: EventLog.DetailedState

    class Relevance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELEVANCE_UNSPECIFIED: _ClassVar[EventLog.Relevance]
        UNKNOWN: _ClassVar[EventLog.Relevance]
        NOT_IMPACTED: _ClassVar[EventLog.Relevance]
        PARTIALLY_RELATED: _ClassVar[EventLog.Relevance]
        RELATED: _ClassVar[EventLog.Relevance]
        IMPACTED: _ClassVar[EventLog.Relevance]
    RELEVANCE_UNSPECIFIED: EventLog.Relevance
    UNKNOWN: EventLog.Relevance
    NOT_IMPACTED: EventLog.Relevance
    PARTIALLY_RELATED: EventLog.Relevance
    RELATED: EventLog.Relevance
    IMPACTED: EventLog.Relevance
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_STATE_FIELD_NUMBER: _ClassVar[int]
    IMPACTED_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    IMPACTED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    category: EventLog.EventCategory
    state: EventLog.State
    detailed_state: EventLog.DetailedState
    impacted_products: str
    impacted_locations: str
    relevance: EventLog.Relevance
    parent_event: str
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    next_update_time: _timestamp_pb2.Timestamp

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., category: _Optional[_Union[EventLog.EventCategory, str]]=..., state: _Optional[_Union[EventLog.State, str]]=..., detailed_state: _Optional[_Union[EventLog.DetailedState, str]]=..., impacted_products: _Optional[str]=..., impacted_locations: _Optional[str]=..., relevance: _Optional[_Union[EventLog.Relevance, str]]=..., parent_event: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...