from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EntityDisplay(_message.Message):
    __slots__ = ('icon_title', 'icon_url')
    ICON_TITLE_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    icon_title: str
    icon_url: str

    def __init__(self, icon_title: _Optional[str]=..., icon_url: _Optional[str]=...) -> None:
        ...