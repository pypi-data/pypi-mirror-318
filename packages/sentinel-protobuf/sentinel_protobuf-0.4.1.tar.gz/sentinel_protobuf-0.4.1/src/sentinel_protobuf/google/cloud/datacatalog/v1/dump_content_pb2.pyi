from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.datacatalog.v1 import datacatalog_pb2 as _datacatalog_pb2
from google.cloud.datacatalog.v1 import tags_pb2 as _tags_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaggedEntry(_message.Message):
    __slots__ = ("v1_entry", "present_tags", "absent_tags")
    V1_ENTRY_FIELD_NUMBER: _ClassVar[int]
    PRESENT_TAGS_FIELD_NUMBER: _ClassVar[int]
    ABSENT_TAGS_FIELD_NUMBER: _ClassVar[int]
    v1_entry: _datacatalog_pb2.Entry
    present_tags: _containers.RepeatedCompositeFieldContainer[_tags_pb2.Tag]
    absent_tags: _containers.RepeatedCompositeFieldContainer[_tags_pb2.Tag]
    def __init__(self, v1_entry: _Optional[_Union[_datacatalog_pb2.Entry, _Mapping]] = ..., present_tags: _Optional[_Iterable[_Union[_tags_pb2.Tag, _Mapping]]] = ..., absent_tags: _Optional[_Iterable[_Union[_tags_pb2.Tag, _Mapping]]] = ...) -> None: ...

class DumpItem(_message.Message):
    __slots__ = ("tagged_entry",)
    TAGGED_ENTRY_FIELD_NUMBER: _ClassVar[int]
    tagged_entry: TaggedEntry
    def __init__(self, tagged_entry: _Optional[_Union[TaggedEntry, _Mapping]] = ...) -> None: ...
