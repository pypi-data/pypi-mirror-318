from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.spanner.v1 import keys_pb2 as _keys_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Mutation(_message.Message):
    __slots__ = ('insert', 'update', 'insert_or_update', 'replace', 'delete')

    class Write(_message.Message):
        __slots__ = ('table', 'columns', 'values')
        TABLE_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        table: str
        columns: _containers.RepeatedScalarFieldContainer[str]
        values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]

        def __init__(self, table: _Optional[str]=..., columns: _Optional[_Iterable[str]]=..., values: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]]=...) -> None:
            ...

    class Delete(_message.Message):
        __slots__ = ('table', 'key_set')
        TABLE_FIELD_NUMBER: _ClassVar[int]
        KEY_SET_FIELD_NUMBER: _ClassVar[int]
        table: str
        key_set: _keys_pb2.KeySet

        def __init__(self, table: _Optional[str]=..., key_set: _Optional[_Union[_keys_pb2.KeySet, _Mapping]]=...) -> None:
            ...
    INSERT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    INSERT_OR_UPDATE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    insert: Mutation.Write
    update: Mutation.Write
    insert_or_update: Mutation.Write
    replace: Mutation.Write
    delete: Mutation.Delete

    def __init__(self, insert: _Optional[_Union[Mutation.Write, _Mapping]]=..., update: _Optional[_Union[Mutation.Write, _Mapping]]=..., insert_or_update: _Optional[_Union[Mutation.Write, _Mapping]]=..., replace: _Optional[_Union[Mutation.Write, _Mapping]]=..., delete: _Optional[_Union[Mutation.Delete, _Mapping]]=...) -> None:
        ...