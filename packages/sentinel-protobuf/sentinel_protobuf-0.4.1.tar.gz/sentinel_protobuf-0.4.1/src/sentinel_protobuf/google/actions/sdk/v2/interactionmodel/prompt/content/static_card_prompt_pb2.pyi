from google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as _static_image_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_link_prompt_pb2 as _static_link_prompt_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticCardPrompt(_message.Message):
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
    image: _static_image_prompt_pb2.StaticImagePrompt
    image_fill: _static_image_prompt_pb2.StaticImagePrompt.ImageFill
    button: _static_link_prompt_pb2.StaticLinkPrompt

    def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., text: _Optional[str]=..., image: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt, _Mapping]]=..., image_fill: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt.ImageFill, str]]=..., button: _Optional[_Union[_static_link_prompt_pb2.StaticLinkPrompt, _Mapping]]=...) -> None:
        ...