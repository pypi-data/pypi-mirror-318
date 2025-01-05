from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WebDetection(_message.Message):
    __slots__ = ('web_entities', 'full_matching_images', 'partial_matching_images', 'pages_with_matching_images', 'visually_similar_images', 'best_guess_labels')

    class WebEntity(_message.Message):
        __slots__ = ('entity_id', 'score', 'description')
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        entity_id: str
        score: float
        description: str

        def __init__(self, entity_id: _Optional[str]=..., score: _Optional[float]=..., description: _Optional[str]=...) -> None:
            ...

    class WebImage(_message.Message):
        __slots__ = ('url', 'score')
        URL_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        url: str
        score: float

        def __init__(self, url: _Optional[str]=..., score: _Optional[float]=...) -> None:
            ...

    class WebPage(_message.Message):
        __slots__ = ('url', 'score', 'page_title', 'full_matching_images', 'partial_matching_images')
        URL_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
        FULL_MATCHING_IMAGES_FIELD_NUMBER: _ClassVar[int]
        PARTIAL_MATCHING_IMAGES_FIELD_NUMBER: _ClassVar[int]
        url: str
        score: float
        page_title: str
        full_matching_images: _containers.RepeatedCompositeFieldContainer[WebDetection.WebImage]
        partial_matching_images: _containers.RepeatedCompositeFieldContainer[WebDetection.WebImage]

        def __init__(self, url: _Optional[str]=..., score: _Optional[float]=..., page_title: _Optional[str]=..., full_matching_images: _Optional[_Iterable[_Union[WebDetection.WebImage, _Mapping]]]=..., partial_matching_images: _Optional[_Iterable[_Union[WebDetection.WebImage, _Mapping]]]=...) -> None:
            ...

    class WebLabel(_message.Message):
        __slots__ = ('label', 'language_code')
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        label: str
        language_code: str

        def __init__(self, label: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
            ...
    WEB_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    FULL_MATCHING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_MATCHING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    PAGES_WITH_MATCHING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    VISUALLY_SIMILAR_IMAGES_FIELD_NUMBER: _ClassVar[int]
    BEST_GUESS_LABELS_FIELD_NUMBER: _ClassVar[int]
    web_entities: _containers.RepeatedCompositeFieldContainer[WebDetection.WebEntity]
    full_matching_images: _containers.RepeatedCompositeFieldContainer[WebDetection.WebImage]
    partial_matching_images: _containers.RepeatedCompositeFieldContainer[WebDetection.WebImage]
    pages_with_matching_images: _containers.RepeatedCompositeFieldContainer[WebDetection.WebPage]
    visually_similar_images: _containers.RepeatedCompositeFieldContainer[WebDetection.WebImage]
    best_guess_labels: _containers.RepeatedCompositeFieldContainer[WebDetection.WebLabel]

    def __init__(self, web_entities: _Optional[_Iterable[_Union[WebDetection.WebEntity, _Mapping]]]=..., full_matching_images: _Optional[_Iterable[_Union[WebDetection.WebImage, _Mapping]]]=..., partial_matching_images: _Optional[_Iterable[_Union[WebDetection.WebImage, _Mapping]]]=..., pages_with_matching_images: _Optional[_Iterable[_Union[WebDetection.WebPage, _Mapping]]]=..., visually_similar_images: _Optional[_Iterable[_Union[WebDetection.WebImage, _Mapping]]]=..., best_guess_labels: _Optional[_Iterable[_Union[WebDetection.WebLabel, _Mapping]]]=...) -> None:
        ...