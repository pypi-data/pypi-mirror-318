from google.type import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationSpecColor(_message.Message):
    __slots__ = ('color', 'display_name', 'id')
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    color: _color_pb2.Color
    display_name: str
    id: str

    def __init__(self, color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., display_name: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...