from google.actions.sdk.v2.conversation.prompt.content import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Collection(_message.Message):
    __slots__ = ('title', 'subtitle', 'items', 'image_fill')

    class CollectionItem(_message.Message):
        __slots__ = ('key',)
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: str

        def __init__(self, key: _Optional[str]=...) -> None:
            ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FILL_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    items: _containers.RepeatedCompositeFieldContainer[Collection.CollectionItem]
    image_fill: _image_pb2.Image.ImageFill

    def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., items: _Optional[_Iterable[_Union[Collection.CollectionItem, _Mapping]]]=..., image_fill: _Optional[_Union[_image_pb2.Image.ImageFill, str]]=...) -> None:
        ...