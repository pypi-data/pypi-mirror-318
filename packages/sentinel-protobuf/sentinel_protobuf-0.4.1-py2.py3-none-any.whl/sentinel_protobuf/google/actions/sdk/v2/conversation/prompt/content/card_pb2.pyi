from google.actions.sdk.v2.conversation.prompt.content import image_pb2 as _image_pb2
from google.actions.sdk.v2.conversation.prompt.content import link_pb2 as _link_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Card(_message.Message):
    __slots__ = ('title', 'subtitle', 'text', 'image', 'image_fill', 'button')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FILL_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    text: str
    image: _image_pb2.Image
    image_fill: _image_pb2.Image.ImageFill
    button: _link_pb2.Link

    def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., text: _Optional[str]=..., image: _Optional[_Union[_image_pb2.Image, _Mapping]]=..., image_fill: _Optional[_Union[_image_pb2.Image.ImageFill, str]]=..., button: _Optional[_Union[_link_pb2.Link, _Mapping]]=...) -> None:
        ...