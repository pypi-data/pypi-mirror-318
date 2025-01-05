from google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as _static_image_prompt_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticListPrompt(_message.Message):
    __slots__ = ('title', 'subtitle', 'items')

    class ListItem(_message.Message):
        __slots__ = ('key', 'title', 'description', 'image')
        KEY_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        key: str
        title: str
        description: str
        image: _static_image_prompt_pb2.StaticImagePrompt

        def __init__(self, key: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., image: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt, _Mapping]]=...) -> None:
            ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    items: _containers.RepeatedCompositeFieldContainer[StaticListPrompt.ListItem]

    def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., items: _Optional[_Iterable[_Union[StaticListPrompt.ListItem, _Mapping]]]=...) -> None:
        ...