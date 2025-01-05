from google.api import annotations_pb2 as _annotations_pb2
from google.genomics.v1 import readgroup_pb2 as _readgroup_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReadGroupSet(_message.Message):
    __slots__ = ('id', 'dataset_id', 'reference_set_id', 'name', 'filename', 'read_groups', 'info')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    READ_GROUPS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataset_id: str
    reference_set_id: str
    name: str
    filename: str
    read_groups: _containers.RepeatedCompositeFieldContainer[_readgroup_pb2.ReadGroup]
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, id: _Optional[str]=..., dataset_id: _Optional[str]=..., reference_set_id: _Optional[str]=..., name: _Optional[str]=..., filename: _Optional[str]=..., read_groups: _Optional[_Iterable[_Union[_readgroup_pb2.ReadGroup, _Mapping]]]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...