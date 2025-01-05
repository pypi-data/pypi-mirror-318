from google.actions.sdk.v2.interactionmodel.prompt.content import static_card_prompt_pb2 as _static_card_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_collection_browse_prompt_pb2 as _static_collection_browse_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_collection_prompt_pb2 as _static_collection_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as _static_image_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_list_prompt_pb2 as _static_list_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_media_prompt_pb2 as _static_media_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_table_prompt_pb2 as _static_table_prompt_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticContentPrompt(_message.Message):
    __slots__ = ('card', 'image', 'table', 'media', 'list', 'collection', 'collection_browse')
    CARD_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_BROWSE_FIELD_NUMBER: _ClassVar[int]
    card: _static_card_prompt_pb2.StaticCardPrompt
    image: _static_image_prompt_pb2.StaticImagePrompt
    table: _static_table_prompt_pb2.StaticTablePrompt
    media: _static_media_prompt_pb2.StaticMediaPrompt
    list: _static_list_prompt_pb2.StaticListPrompt
    collection: _static_collection_prompt_pb2.StaticCollectionPrompt
    collection_browse: _static_collection_browse_prompt_pb2.StaticCollectionBrowsePrompt

    def __init__(self, card: _Optional[_Union[_static_card_prompt_pb2.StaticCardPrompt, _Mapping]]=..., image: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt, _Mapping]]=..., table: _Optional[_Union[_static_table_prompt_pb2.StaticTablePrompt, _Mapping]]=..., media: _Optional[_Union[_static_media_prompt_pb2.StaticMediaPrompt, _Mapping]]=..., list: _Optional[_Union[_static_list_prompt_pb2.StaticListPrompt, _Mapping]]=..., collection: _Optional[_Union[_static_collection_prompt_pb2.StaticCollectionPrompt, _Mapping]]=..., collection_browse: _Optional[_Union[_static_collection_browse_prompt_pb2.StaticCollectionBrowsePrompt, _Mapping]]=...) -> None:
        ...