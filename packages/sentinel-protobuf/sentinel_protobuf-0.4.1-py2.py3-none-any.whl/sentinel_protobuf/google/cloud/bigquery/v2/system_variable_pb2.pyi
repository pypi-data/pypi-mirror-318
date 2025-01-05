from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import standard_sql_pb2 as _standard_sql_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SystemVariables(_message.Message):
    __slots__ = ('types', 'values')

    class TypesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _standard_sql_pb2.StandardSqlDataType

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_standard_sql_pb2.StandardSqlDataType, _Mapping]]=...) -> None:
            ...
    TYPES_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    types: _containers.MessageMap[str, _standard_sql_pb2.StandardSqlDataType]
    values: _struct_pb2.Struct

    def __init__(self, types: _Optional[_Mapping[str, _standard_sql_pb2.StandardSqlDataType]]=..., values: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...