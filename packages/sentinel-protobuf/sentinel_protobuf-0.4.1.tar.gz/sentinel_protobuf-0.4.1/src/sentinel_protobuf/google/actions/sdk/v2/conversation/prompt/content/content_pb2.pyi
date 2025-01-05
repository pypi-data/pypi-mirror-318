from google.actions.sdk.v2.conversation.prompt.content import canvas_pb2 as _canvas_pb2
from google.actions.sdk.v2.conversation.prompt.content import card_pb2 as _card_pb2
from google.actions.sdk.v2.conversation.prompt.content import collection_pb2 as _collection_pb2
from google.actions.sdk.v2.conversation.prompt.content import image_pb2 as _image_pb2
from google.actions.sdk.v2.conversation.prompt.content import list_pb2 as _list_pb2
from google.actions.sdk.v2.conversation.prompt.content import media_pb2 as _media_pb2
from google.actions.sdk.v2.conversation.prompt.content import table_pb2 as _table_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Content(_message.Message):
    __slots__ = ('card', 'image', 'table', 'media', 'canvas', 'collection', 'list')
    CARD_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    card: _card_pb2.Card
    image: _image_pb2.Image
    table: _table_pb2.Table
    media: _media_pb2.Media
    canvas: _canvas_pb2.Canvas
    collection: _collection_pb2.Collection
    list: _list_pb2.List

    def __init__(self, card: _Optional[_Union[_card_pb2.Card, _Mapping]]=..., image: _Optional[_Union[_image_pb2.Image, _Mapping]]=..., table: _Optional[_Union[_table_pb2.Table, _Mapping]]=..., media: _Optional[_Union[_media_pb2.Media, _Mapping]]=..., canvas: _Optional[_Union[_canvas_pb2.Canvas, _Mapping]]=..., collection: _Optional[_Union[_collection_pb2.Collection, _Mapping]]=..., list: _Optional[_Union[_list_pb2.List, _Mapping]]=...) -> None:
        ...