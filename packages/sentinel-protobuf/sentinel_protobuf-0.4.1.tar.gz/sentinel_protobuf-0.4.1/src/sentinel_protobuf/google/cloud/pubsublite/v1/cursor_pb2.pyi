from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.pubsublite.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InitialCommitCursorRequest(_message.Message):
    __slots__ = ('subscription', 'partition')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    partition: int

    def __init__(self, subscription: _Optional[str]=..., partition: _Optional[int]=...) -> None:
        ...

class InitialCommitCursorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SequencedCommitCursorRequest(_message.Message):
    __slots__ = ('cursor',)
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    cursor: _common_pb2.Cursor

    def __init__(self, cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class SequencedCommitCursorResponse(_message.Message):
    __slots__ = ('acknowledged_commits',)
    ACKNOWLEDGED_COMMITS_FIELD_NUMBER: _ClassVar[int]
    acknowledged_commits: int

    def __init__(self, acknowledged_commits: _Optional[int]=...) -> None:
        ...

class StreamingCommitCursorRequest(_message.Message):
    __slots__ = ('initial', 'commit')
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    initial: InitialCommitCursorRequest
    commit: SequencedCommitCursorRequest

    def __init__(self, initial: _Optional[_Union[InitialCommitCursorRequest, _Mapping]]=..., commit: _Optional[_Union[SequencedCommitCursorRequest, _Mapping]]=...) -> None:
        ...

class StreamingCommitCursorResponse(_message.Message):
    __slots__ = ('initial', 'commit')
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    initial: InitialCommitCursorResponse
    commit: SequencedCommitCursorResponse

    def __init__(self, initial: _Optional[_Union[InitialCommitCursorResponse, _Mapping]]=..., commit: _Optional[_Union[SequencedCommitCursorResponse, _Mapping]]=...) -> None:
        ...

class CommitCursorRequest(_message.Message):
    __slots__ = ('subscription', 'partition', 'cursor')
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    subscription: str
    partition: int
    cursor: _common_pb2.Cursor

    def __init__(self, subscription: _Optional[str]=..., partition: _Optional[int]=..., cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class CommitCursorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListPartitionCursorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class PartitionCursor(_message.Message):
    __slots__ = ('partition', 'cursor')
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    partition: int
    cursor: _common_pb2.Cursor

    def __init__(self, partition: _Optional[int]=..., cursor: _Optional[_Union[_common_pb2.Cursor, _Mapping]]=...) -> None:
        ...

class ListPartitionCursorsResponse(_message.Message):
    __slots__ = ('partition_cursors', 'next_page_token')
    PARTITION_CURSORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    partition_cursors: _containers.RepeatedCompositeFieldContainer[PartitionCursor]
    next_page_token: str

    def __init__(self, partition_cursors: _Optional[_Iterable[_Union[PartitionCursor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...