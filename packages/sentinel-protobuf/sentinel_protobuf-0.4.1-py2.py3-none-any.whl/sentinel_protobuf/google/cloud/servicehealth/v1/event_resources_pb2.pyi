from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_VIEW_UNSPECIFIED: _ClassVar[EventView]
    EVENT_VIEW_BASIC: _ClassVar[EventView]
    EVENT_VIEW_FULL: _ClassVar[EventView]

class OrganizationEventView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORGANIZATION_EVENT_VIEW_UNSPECIFIED: _ClassVar[OrganizationEventView]
    ORGANIZATION_EVENT_VIEW_BASIC: _ClassVar[OrganizationEventView]
    ORGANIZATION_EVENT_VIEW_FULL: _ClassVar[OrganizationEventView]
EVENT_VIEW_UNSPECIFIED: EventView
EVENT_VIEW_BASIC: EventView
EVENT_VIEW_FULL: EventView
ORGANIZATION_EVENT_VIEW_UNSPECIFIED: OrganizationEventView
ORGANIZATION_EVENT_VIEW_BASIC: OrganizationEventView
ORGANIZATION_EVENT_VIEW_FULL: OrganizationEventView

class Event(_message.Message):
    __slots__ = ('name', 'title', 'description', 'category', 'detailed_category', 'state', 'detailed_state', 'event_impacts', 'relevance', 'updates', 'parent_event', 'update_time', 'start_time', 'end_time', 'next_update_time')

    class EventCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_CATEGORY_UNSPECIFIED: _ClassVar[Event.EventCategory]
        INCIDENT: _ClassVar[Event.EventCategory]
    EVENT_CATEGORY_UNSPECIFIED: Event.EventCategory
    INCIDENT: Event.EventCategory

    class DetailedCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETAILED_CATEGORY_UNSPECIFIED: _ClassVar[Event.DetailedCategory]
        CONFIRMED_INCIDENT: _ClassVar[Event.DetailedCategory]
        EMERGING_INCIDENT: _ClassVar[Event.DetailedCategory]
    DETAILED_CATEGORY_UNSPECIFIED: Event.DetailedCategory
    CONFIRMED_INCIDENT: Event.DetailedCategory
    EMERGING_INCIDENT: Event.DetailedCategory

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Event.State]
        ACTIVE: _ClassVar[Event.State]
        CLOSED: _ClassVar[Event.State]
    STATE_UNSPECIFIED: Event.State
    ACTIVE: Event.State
    CLOSED: Event.State

    class DetailedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETAILED_STATE_UNSPECIFIED: _ClassVar[Event.DetailedState]
        EMERGING: _ClassVar[Event.DetailedState]
        CONFIRMED: _ClassVar[Event.DetailedState]
        RESOLVED: _ClassVar[Event.DetailedState]
        MERGED: _ClassVar[Event.DetailedState]
        AUTO_CLOSED: _ClassVar[Event.DetailedState]
        FALSE_POSITIVE: _ClassVar[Event.DetailedState]
    DETAILED_STATE_UNSPECIFIED: Event.DetailedState
    EMERGING: Event.DetailedState
    CONFIRMED: Event.DetailedState
    RESOLVED: Event.DetailedState
    MERGED: Event.DetailedState
    AUTO_CLOSED: Event.DetailedState
    FALSE_POSITIVE: Event.DetailedState

    class Relevance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELEVANCE_UNSPECIFIED: _ClassVar[Event.Relevance]
        UNKNOWN: _ClassVar[Event.Relevance]
        NOT_IMPACTED: _ClassVar[Event.Relevance]
        PARTIALLY_RELATED: _ClassVar[Event.Relevance]
        RELATED: _ClassVar[Event.Relevance]
        IMPACTED: _ClassVar[Event.Relevance]
    RELEVANCE_UNSPECIFIED: Event.Relevance
    UNKNOWN: Event.Relevance
    NOT_IMPACTED: Event.Relevance
    PARTIALLY_RELATED: Event.Relevance
    RELATED: Event.Relevance
    IMPACTED: Event.Relevance
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DETAILED_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_STATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_IMPACTS_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    PARENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    category: Event.EventCategory
    detailed_category: Event.DetailedCategory
    state: Event.State
    detailed_state: Event.DetailedState
    event_impacts: _containers.RepeatedCompositeFieldContainer[EventImpact]
    relevance: Event.Relevance
    updates: _containers.RepeatedCompositeFieldContainer[EventUpdate]
    parent_event: str
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    next_update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., category: _Optional[_Union[Event.EventCategory, str]]=..., detailed_category: _Optional[_Union[Event.DetailedCategory, str]]=..., state: _Optional[_Union[Event.State, str]]=..., detailed_state: _Optional[_Union[Event.DetailedState, str]]=..., event_impacts: _Optional[_Iterable[_Union[EventImpact, _Mapping]]]=..., relevance: _Optional[_Union[Event.Relevance, str]]=..., updates: _Optional[_Iterable[_Union[EventUpdate, _Mapping]]]=..., parent_event: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class OrganizationEvent(_message.Message):
    __slots__ = ('name', 'title', 'description', 'category', 'detailed_category', 'state', 'detailed_state', 'event_impacts', 'updates', 'parent_event', 'update_time', 'start_time', 'end_time', 'next_update_time')

    class EventCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_CATEGORY_UNSPECIFIED: _ClassVar[OrganizationEvent.EventCategory]
        INCIDENT: _ClassVar[OrganizationEvent.EventCategory]
    EVENT_CATEGORY_UNSPECIFIED: OrganizationEvent.EventCategory
    INCIDENT: OrganizationEvent.EventCategory

    class DetailedCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETAILED_CATEGORY_UNSPECIFIED: _ClassVar[OrganizationEvent.DetailedCategory]
        CONFIRMED_INCIDENT: _ClassVar[OrganizationEvent.DetailedCategory]
        EMERGING_INCIDENT: _ClassVar[OrganizationEvent.DetailedCategory]
    DETAILED_CATEGORY_UNSPECIFIED: OrganizationEvent.DetailedCategory
    CONFIRMED_INCIDENT: OrganizationEvent.DetailedCategory
    EMERGING_INCIDENT: OrganizationEvent.DetailedCategory

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[OrganizationEvent.State]
        ACTIVE: _ClassVar[OrganizationEvent.State]
        CLOSED: _ClassVar[OrganizationEvent.State]
    STATE_UNSPECIFIED: OrganizationEvent.State
    ACTIVE: OrganizationEvent.State
    CLOSED: OrganizationEvent.State

    class DetailedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETAILED_STATE_UNSPECIFIED: _ClassVar[OrganizationEvent.DetailedState]
        EMERGING: _ClassVar[OrganizationEvent.DetailedState]
        CONFIRMED: _ClassVar[OrganizationEvent.DetailedState]
        RESOLVED: _ClassVar[OrganizationEvent.DetailedState]
        MERGED: _ClassVar[OrganizationEvent.DetailedState]
        AUTO_CLOSED: _ClassVar[OrganizationEvent.DetailedState]
        FALSE_POSITIVE: _ClassVar[OrganizationEvent.DetailedState]
    DETAILED_STATE_UNSPECIFIED: OrganizationEvent.DetailedState
    EMERGING: OrganizationEvent.DetailedState
    CONFIRMED: OrganizationEvent.DetailedState
    RESOLVED: OrganizationEvent.DetailedState
    MERGED: OrganizationEvent.DetailedState
    AUTO_CLOSED: OrganizationEvent.DetailedState
    FALSE_POSITIVE: OrganizationEvent.DetailedState
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DETAILED_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_STATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_IMPACTS_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    PARENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    description: str
    category: OrganizationEvent.EventCategory
    detailed_category: OrganizationEvent.DetailedCategory
    state: OrganizationEvent.State
    detailed_state: OrganizationEvent.DetailedState
    event_impacts: _containers.RepeatedCompositeFieldContainer[EventImpact]
    updates: _containers.RepeatedCompositeFieldContainer[EventUpdate]
    parent_event: str
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    next_update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., category: _Optional[_Union[OrganizationEvent.EventCategory, str]]=..., detailed_category: _Optional[_Union[OrganizationEvent.DetailedCategory, str]]=..., state: _Optional[_Union[OrganizationEvent.State, str]]=..., detailed_state: _Optional[_Union[OrganizationEvent.DetailedState, str]]=..., event_impacts: _Optional[_Iterable[_Union[EventImpact, _Mapping]]]=..., updates: _Optional[_Iterable[_Union[EventUpdate, _Mapping]]]=..., parent_event: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EventUpdate(_message.Message):
    __slots__ = ('update_time', 'title', 'description', 'symptom', 'workaround')
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYMPTOM_FIELD_NUMBER: _ClassVar[int]
    WORKAROUND_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    title: str
    description: str
    symptom: str
    workaround: str

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., title: _Optional[str]=..., description: _Optional[str]=..., symptom: _Optional[str]=..., workaround: _Optional[str]=...) -> None:
        ...

class Location(_message.Message):
    __slots__ = ('location_name',)
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    location_name: str

    def __init__(self, location_name: _Optional[str]=...) -> None:
        ...

class Product(_message.Message):
    __slots__ = ('product_name', 'id')
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    id: str

    def __init__(self, product_name: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...

class EventImpact(_message.Message):
    __slots__ = ('product', 'location')
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    product: Product
    location: Location

    def __init__(self, product: _Optional[_Union[Product, _Mapping]]=..., location: _Optional[_Union[Location, _Mapping]]=...) -> None:
        ...

class OrganizationImpact(_message.Message):
    __slots__ = ('name', 'events', 'asset', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    events: _containers.RepeatedScalarFieldContainer[str]
    asset: Asset
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., events: _Optional[_Iterable[str]]=..., asset: _Optional[_Union[Asset, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Asset(_message.Message):
    __slots__ = ('asset_name', 'asset_type')
    ASSET_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    asset_name: str
    asset_type: str

    def __init__(self, asset_name: _Optional[str]=..., asset_type: _Optional[str]=...) -> None:
        ...

class ListEventsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    view: EventView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., view: _Optional[_Union[EventView, str]]=...) -> None:
        ...

class ListEventsResponse(_message.Message):
    __slots__ = ('events', 'next_page_token', 'unreachable')
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEventRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOrganizationEventsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    view: OrganizationEventView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., view: _Optional[_Union[OrganizationEventView, str]]=...) -> None:
        ...

class ListOrganizationEventsResponse(_message.Message):
    __slots__ = ('organization_events', 'next_page_token', 'unreachable')
    ORGANIZATION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    organization_events: _containers.RepeatedCompositeFieldContainer[OrganizationEvent]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, organization_events: _Optional[_Iterable[_Union[OrganizationEvent, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOrganizationEventRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOrganizationImpactsRequest(_message.Message):
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

class ListOrganizationImpactsResponse(_message.Message):
    __slots__ = ('organization_impacts', 'next_page_token', 'unreachable')
    ORGANIZATION_IMPACTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    organization_impacts: _containers.RepeatedCompositeFieldContainer[OrganizationImpact]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, organization_impacts: _Optional[_Iterable[_Union[OrganizationImpact, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOrganizationImpactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...