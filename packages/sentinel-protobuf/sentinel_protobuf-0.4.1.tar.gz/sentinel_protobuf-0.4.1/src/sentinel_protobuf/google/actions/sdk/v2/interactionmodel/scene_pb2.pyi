from google.actions.sdk.v2.interactionmodel import conditional_event_pb2 as _conditional_event_pb2
from google.actions.sdk.v2.interactionmodel import event_handler_pb2 as _event_handler_pb2
from google.actions.sdk.v2.interactionmodel import intent_event_pb2 as _intent_event_pb2
from google.actions.sdk.v2.interactionmodel import slot_pb2 as _slot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Scene(_message.Message):
    __slots__ = ('on_enter', 'intent_events', 'conditional_events', 'slots', 'on_slot_updated')
    ON_ENTER_FIELD_NUMBER: _ClassVar[int]
    INTENT_EVENTS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    ON_SLOT_UPDATED_FIELD_NUMBER: _ClassVar[int]
    on_enter: _event_handler_pb2.EventHandler
    intent_events: _containers.RepeatedCompositeFieldContainer[_intent_event_pb2.IntentEvent]
    conditional_events: _containers.RepeatedCompositeFieldContainer[_conditional_event_pb2.ConditionalEvent]
    slots: _containers.RepeatedCompositeFieldContainer[_slot_pb2.Slot]
    on_slot_updated: _event_handler_pb2.EventHandler

    def __init__(self, on_enter: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., intent_events: _Optional[_Iterable[_Union[_intent_event_pb2.IntentEvent, _Mapping]]]=..., conditional_events: _Optional[_Iterable[_Union[_conditional_event_pb2.ConditionalEvent, _Mapping]]]=..., slots: _Optional[_Iterable[_Union[_slot_pb2.Slot, _Mapping]]]=..., on_slot_updated: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=...) -> None:
        ...