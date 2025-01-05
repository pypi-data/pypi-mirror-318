from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CitationMetadata(_message.Message):
    __slots__ = ("citation_sources",)
    CITATION_SOURCES_FIELD_NUMBER: _ClassVar[int]
    citation_sources: _containers.RepeatedCompositeFieldContainer[CitationSource]
    def __init__(self, citation_sources: _Optional[_Iterable[_Union[CitationSource, _Mapping]]] = ...) -> None: ...

class CitationSource(_message.Message):
    __slots__ = ("start_index", "end_index", "uri", "license")
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_INDEX_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    start_index: int
    end_index: int
    uri: str
    license: str
    def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., uri: _Optional[str] = ..., license: _Optional[str] = ...) -> None: ...
