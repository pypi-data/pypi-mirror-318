from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.support.v2 import comment_pb2 as _comment_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListCommentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCommentsResponse(_message.Message):
    __slots__ = ('comments', 'next_page_token')
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_comment_pb2.Comment]
    next_page_token: str

    def __init__(self, comments: _Optional[_Iterable[_Union[_comment_pb2.Comment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateCommentRequest(_message.Message):
    __slots__ = ('parent', 'comment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    comment: _comment_pb2.Comment

    def __init__(self, parent: _Optional[str]=..., comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]]=...) -> None:
        ...