from google.maps.places.v1 import photo_pb2 as _photo_pb2
from google.maps.places.v1 import review_pb2 as _review_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContextualContent(_message.Message):
    __slots__ = ('reviews', 'photos', 'justifications')

    class Justification(_message.Message):
        __slots__ = ('review_justification', 'business_availability_attributes_justification')

        class ReviewJustification(_message.Message):
            __slots__ = ('highlighted_text', 'review')

            class HighlightedText(_message.Message):
                __slots__ = ('text', 'highlighted_text_ranges')

                class HighlightedTextRange(_message.Message):
                    __slots__ = ('start_index', 'end_index')
                    START_INDEX_FIELD_NUMBER: _ClassVar[int]
                    END_INDEX_FIELD_NUMBER: _ClassVar[int]
                    start_index: int
                    end_index: int

                    def __init__(self, start_index: _Optional[int]=..., end_index: _Optional[int]=...) -> None:
                        ...
                TEXT_FIELD_NUMBER: _ClassVar[int]
                HIGHLIGHTED_TEXT_RANGES_FIELD_NUMBER: _ClassVar[int]
                text: str
                highlighted_text_ranges: _containers.RepeatedCompositeFieldContainer[ContextualContent.Justification.ReviewJustification.HighlightedText.HighlightedTextRange]

                def __init__(self, text: _Optional[str]=..., highlighted_text_ranges: _Optional[_Iterable[_Union[ContextualContent.Justification.ReviewJustification.HighlightedText.HighlightedTextRange, _Mapping]]]=...) -> None:
                    ...
            HIGHLIGHTED_TEXT_FIELD_NUMBER: _ClassVar[int]
            REVIEW_FIELD_NUMBER: _ClassVar[int]
            highlighted_text: ContextualContent.Justification.ReviewJustification.HighlightedText
            review: _review_pb2.Review

            def __init__(self, highlighted_text: _Optional[_Union[ContextualContent.Justification.ReviewJustification.HighlightedText, _Mapping]]=..., review: _Optional[_Union[_review_pb2.Review, _Mapping]]=...) -> None:
                ...

        class BusinessAvailabilityAttributesJustification(_message.Message):
            __slots__ = ('takeout', 'delivery', 'dine_in')
            TAKEOUT_FIELD_NUMBER: _ClassVar[int]
            DELIVERY_FIELD_NUMBER: _ClassVar[int]
            DINE_IN_FIELD_NUMBER: _ClassVar[int]
            takeout: bool
            delivery: bool
            dine_in: bool

            def __init__(self, takeout: bool=..., delivery: bool=..., dine_in: bool=...) -> None:
                ...
        REVIEW_JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
        BUSINESS_AVAILABILITY_ATTRIBUTES_JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
        review_justification: ContextualContent.Justification.ReviewJustification
        business_availability_attributes_justification: ContextualContent.Justification.BusinessAvailabilityAttributesJustification

        def __init__(self, review_justification: _Optional[_Union[ContextualContent.Justification.ReviewJustification, _Mapping]]=..., business_availability_attributes_justification: _Optional[_Union[ContextualContent.Justification.BusinessAvailabilityAttributesJustification, _Mapping]]=...) -> None:
            ...
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    JUSTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    reviews: _containers.RepeatedCompositeFieldContainer[_review_pb2.Review]
    photos: _containers.RepeatedCompositeFieldContainer[_photo_pb2.Photo]
    justifications: _containers.RepeatedCompositeFieldContainer[ContextualContent.Justification]

    def __init__(self, reviews: _Optional[_Iterable[_Union[_review_pb2.Review, _Mapping]]]=..., photos: _Optional[_Iterable[_Union[_photo_pb2.Photo, _Mapping]]]=..., justifications: _Optional[_Iterable[_Union[ContextualContent.Justification, _Mapping]]]=...) -> None:
        ...