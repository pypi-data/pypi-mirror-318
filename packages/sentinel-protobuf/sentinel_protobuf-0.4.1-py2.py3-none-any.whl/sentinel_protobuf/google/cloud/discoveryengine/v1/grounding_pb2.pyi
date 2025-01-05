from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GroundingFact(_message.Message):
    __slots__ = ('fact_text', 'attributes')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    FACT_TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    fact_text: str
    attributes: _containers.ScalarMap[str, str]

    def __init__(self, fact_text: _Optional[str]=..., attributes: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class FactChunk(_message.Message):
    __slots__ = ('chunk_text', 'source', 'index', 'source_metadata')

    class SourceMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CHUNK_TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SOURCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    chunk_text: str
    source: str
    index: int
    source_metadata: _containers.ScalarMap[str, str]

    def __init__(self, chunk_text: _Optional[str]=..., source: _Optional[str]=..., index: _Optional[int]=..., source_metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...