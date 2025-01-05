from google.actions.sdk.v2.interactionmodel.type import entity_display_pb2 as _entity_display_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FreeTextType(_message.Message):
    __slots__ = ('display',)
    DISPLAY_FIELD_NUMBER: _ClassVar[int]
    display: _entity_display_pb2.EntityDisplay

    def __init__(self, display: _Optional[_Union[_entity_display_pb2.EntityDisplay, _Mapping]]=...) -> None:
        ...