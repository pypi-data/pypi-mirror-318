from google.api import resource_pb2 as _resource_pb2
from google.maps.places.v1 import attribution_pb2 as _attribution_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Review(_message.Message):
    __slots__ = ('name', 'relative_publish_time_description', 'text', 'original_text', 'rating', 'author_attribution', 'publish_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PUBLISH_TIME_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    relative_publish_time_description: str
    text: _localized_text_pb2.LocalizedText
    original_text: _localized_text_pb2.LocalizedText
    rating: float
    author_attribution: _attribution_pb2.AuthorAttribution
    publish_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., relative_publish_time_description: _Optional[str]=..., text: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., original_text: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., rating: _Optional[float]=..., author_attribution: _Optional[_Union[_attribution_pb2.AuthorAttribution, _Mapping]]=..., publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...