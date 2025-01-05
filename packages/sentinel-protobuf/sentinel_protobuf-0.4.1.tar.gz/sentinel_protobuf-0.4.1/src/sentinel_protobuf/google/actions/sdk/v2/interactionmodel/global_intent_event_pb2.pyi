from google.actions.sdk.v2.interactionmodel import event_handler_pb2 as _event_handler_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GlobalIntentEvent(_message.Message):
    __slots__ = ('transition_to_scene', 'handler')
    TRANSITION_TO_SCENE_FIELD_NUMBER: _ClassVar[int]
    HANDLER_FIELD_NUMBER: _ClassVar[int]
    transition_to_scene: str
    handler: _event_handler_pb2.EventHandler

    def __init__(self, transition_to_scene: _Optional[str]=..., handler: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=...) -> None:
        ...