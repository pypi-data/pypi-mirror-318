from google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as _static_image_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_link_prompt_pb2 as _static_link_prompt_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticCollectionBrowsePrompt(_message.Message):
    __slots__ = ('items', 'image_fill')

    class CollectionBrowseItem(_message.Message):
        __slots__ = ('title', 'description', 'footer', 'image', 'open_uri_action')
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        OPEN_URI_ACTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        footer: str
        image: _static_image_prompt_pb2.StaticImagePrompt
        open_uri_action: _static_link_prompt_pb2.OpenUrl

        def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., footer: _Optional[str]=..., image: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt, _Mapping]]=..., open_uri_action: _Optional[_Union[_static_link_prompt_pb2.OpenUrl, _Mapping]]=...) -> None:
            ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FILL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[StaticCollectionBrowsePrompt.CollectionBrowseItem]
    image_fill: _static_image_prompt_pb2.StaticImagePrompt.ImageFill

    def __init__(self, items: _Optional[_Iterable[_Union[StaticCollectionBrowsePrompt.CollectionBrowseItem, _Mapping]]]=..., image_fill: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt.ImageFill, str]]=...) -> None:
        ...