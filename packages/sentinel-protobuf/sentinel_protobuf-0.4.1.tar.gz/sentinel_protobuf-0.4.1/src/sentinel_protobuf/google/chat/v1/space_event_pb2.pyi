from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.chat.v1 import event_payload_pb2 as _event_payload_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceEvent(_message.Message):
    __slots__ = ("name", "event_time", "event_type", "message_created_event_data", "message_updated_event_data", "message_deleted_event_data", "message_batch_created_event_data", "message_batch_updated_event_data", "message_batch_deleted_event_data", "space_updated_event_data", "space_batch_updated_event_data", "membership_created_event_data", "membership_updated_event_data", "membership_deleted_event_data", "membership_batch_created_event_data", "membership_batch_updated_event_data", "membership_batch_deleted_event_data", "reaction_created_event_data", "reaction_deleted_event_data", "reaction_batch_created_event_data", "reaction_batch_deleted_event_data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CREATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UPDATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DELETED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BATCH_CREATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BATCH_UPDATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BATCH_DELETED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    SPACE_UPDATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    SPACE_BATCH_UPDATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_CREATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_UPDATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_DELETED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_BATCH_CREATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_BATCH_UPDATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_BATCH_DELETED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    REACTION_CREATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    REACTION_DELETED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    REACTION_BATCH_CREATED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    REACTION_BATCH_DELETED_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    event_time: _timestamp_pb2.Timestamp
    event_type: str
    message_created_event_data: _event_payload_pb2.MessageCreatedEventData
    message_updated_event_data: _event_payload_pb2.MessageUpdatedEventData
    message_deleted_event_data: _event_payload_pb2.MessageDeletedEventData
    message_batch_created_event_data: _event_payload_pb2.MessageBatchCreatedEventData
    message_batch_updated_event_data: _event_payload_pb2.MessageBatchUpdatedEventData
    message_batch_deleted_event_data: _event_payload_pb2.MessageBatchDeletedEventData
    space_updated_event_data: _event_payload_pb2.SpaceUpdatedEventData
    space_batch_updated_event_data: _event_payload_pb2.SpaceBatchUpdatedEventData
    membership_created_event_data: _event_payload_pb2.MembershipCreatedEventData
    membership_updated_event_data: _event_payload_pb2.MembershipUpdatedEventData
    membership_deleted_event_data: _event_payload_pb2.MembershipDeletedEventData
    membership_batch_created_event_data: _event_payload_pb2.MembershipBatchCreatedEventData
    membership_batch_updated_event_data: _event_payload_pb2.MembershipBatchUpdatedEventData
    membership_batch_deleted_event_data: _event_payload_pb2.MembershipBatchDeletedEventData
    reaction_created_event_data: _event_payload_pb2.ReactionCreatedEventData
    reaction_deleted_event_data: _event_payload_pb2.ReactionDeletedEventData
    reaction_batch_created_event_data: _event_payload_pb2.ReactionBatchCreatedEventData
    reaction_batch_deleted_event_data: _event_payload_pb2.ReactionBatchDeletedEventData
    def __init__(self, name: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event_type: _Optional[str] = ..., message_created_event_data: _Optional[_Union[_event_payload_pb2.MessageCreatedEventData, _Mapping]] = ..., message_updated_event_data: _Optional[_Union[_event_payload_pb2.MessageUpdatedEventData, _Mapping]] = ..., message_deleted_event_data: _Optional[_Union[_event_payload_pb2.MessageDeletedEventData, _Mapping]] = ..., message_batch_created_event_data: _Optional[_Union[_event_payload_pb2.MessageBatchCreatedEventData, _Mapping]] = ..., message_batch_updated_event_data: _Optional[_Union[_event_payload_pb2.MessageBatchUpdatedEventData, _Mapping]] = ..., message_batch_deleted_event_data: _Optional[_Union[_event_payload_pb2.MessageBatchDeletedEventData, _Mapping]] = ..., space_updated_event_data: _Optional[_Union[_event_payload_pb2.SpaceUpdatedEventData, _Mapping]] = ..., space_batch_updated_event_data: _Optional[_Union[_event_payload_pb2.SpaceBatchUpdatedEventData, _Mapping]] = ..., membership_created_event_data: _Optional[_Union[_event_payload_pb2.MembershipCreatedEventData, _Mapping]] = ..., membership_updated_event_data: _Optional[_Union[_event_payload_pb2.MembershipUpdatedEventData, _Mapping]] = ..., membership_deleted_event_data: _Optional[_Union[_event_payload_pb2.MembershipDeletedEventData, _Mapping]] = ..., membership_batch_created_event_data: _Optional[_Union[_event_payload_pb2.MembershipBatchCreatedEventData, _Mapping]] = ..., membership_batch_updated_event_data: _Optional[_Union[_event_payload_pb2.MembershipBatchUpdatedEventData, _Mapping]] = ..., membership_batch_deleted_event_data: _Optional[_Union[_event_payload_pb2.MembershipBatchDeletedEventData, _Mapping]] = ..., reaction_created_event_data: _Optional[_Union[_event_payload_pb2.ReactionCreatedEventData, _Mapping]] = ..., reaction_deleted_event_data: _Optional[_Union[_event_payload_pb2.ReactionDeletedEventData, _Mapping]] = ..., reaction_batch_created_event_data: _Optional[_Union[_event_payload_pb2.ReactionBatchCreatedEventData, _Mapping]] = ..., reaction_batch_deleted_event_data: _Optional[_Union[_event_payload_pb2.ReactionBatchDeletedEventData, _Mapping]] = ...) -> None: ...

class GetSpaceEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSpaceEventsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListSpaceEventsResponse(_message.Message):
    __slots__ = ("space_events", "next_page_token")
    SPACE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    space_events: _containers.RepeatedCompositeFieldContainer[SpaceEvent]
    next_page_token: str
    def __init__(self, space_events: _Optional[_Iterable[_Union[SpaceEvent, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
