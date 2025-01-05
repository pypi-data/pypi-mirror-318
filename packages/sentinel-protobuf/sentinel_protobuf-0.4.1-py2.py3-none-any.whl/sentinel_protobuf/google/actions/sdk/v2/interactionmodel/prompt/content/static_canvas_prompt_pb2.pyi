from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticCanvasPrompt(_message.Message):
    __slots__ = ('url', 'data', 'suppress_mic', 'send_state_data_to_canvas_app', 'enable_full_screen')
    URL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_MIC_FIELD_NUMBER: _ClassVar[int]
    SEND_STATE_DATA_TO_CANVAS_APP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FULL_SCREEN_FIELD_NUMBER: _ClassVar[int]
    url: str
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    suppress_mic: bool
    send_state_data_to_canvas_app: bool
    enable_full_screen: bool

    def __init__(self, url: _Optional[str]=..., data: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., suppress_mic: bool=..., send_state_data_to_canvas_app: bool=..., enable_full_screen: bool=...) -> None:
        ...