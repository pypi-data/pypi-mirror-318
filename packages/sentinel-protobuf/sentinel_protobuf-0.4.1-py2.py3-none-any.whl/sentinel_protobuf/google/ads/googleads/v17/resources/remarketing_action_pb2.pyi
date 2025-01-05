from google.ads.googleads.v17.common import tag_snippet_pb2 as _tag_snippet_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemarketingAction(_message.Message):
    __slots__ = ("resource_name", "id", "name", "tag_snippets")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    tag_snippets: _containers.RepeatedCompositeFieldContainer[_tag_snippet_pb2.TagSnippet]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., tag_snippets: _Optional[_Iterable[_Union[_tag_snippet_pb2.TagSnippet, _Mapping]]] = ...) -> None: ...
