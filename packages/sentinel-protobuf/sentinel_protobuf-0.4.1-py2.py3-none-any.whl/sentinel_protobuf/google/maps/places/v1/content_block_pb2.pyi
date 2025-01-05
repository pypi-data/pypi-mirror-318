from google.maps.places.v1 import reference_pb2 as _reference_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContentBlock(_message.Message):
    __slots__ = ('topic', 'content', 'references')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    topic: str
    content: _localized_text_pb2.LocalizedText
    references: _reference_pb2.References

    def __init__(self, topic: _Optional[str]=..., content: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., references: _Optional[_Union[_reference_pb2.References, _Mapping]]=...) -> None:
        ...