from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlFlagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_FLAG_TYPE_UNSPECIFIED: _ClassVar[SqlFlagType]
    BOOLEAN: _ClassVar[SqlFlagType]
    STRING: _ClassVar[SqlFlagType]
    INTEGER: _ClassVar[SqlFlagType]
    NONE: _ClassVar[SqlFlagType]
    MYSQL_TIMEZONE_OFFSET: _ClassVar[SqlFlagType]
    FLOAT: _ClassVar[SqlFlagType]
    REPEATED_STRING: _ClassVar[SqlFlagType]
SQL_FLAG_TYPE_UNSPECIFIED: SqlFlagType
BOOLEAN: SqlFlagType
STRING: SqlFlagType
INTEGER: SqlFlagType
NONE: SqlFlagType
MYSQL_TIMEZONE_OFFSET: SqlFlagType
FLOAT: SqlFlagType
REPEATED_STRING: SqlFlagType

class SqlFlagsListRequest(_message.Message):
    __slots__ = ("database_version",)
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    database_version: str
    def __init__(self, database_version: _Optional[str] = ...) -> None: ...

class FlagsListResponse(_message.Message):
    __slots__ = ("kind", "items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[Flag]
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Flag, _Mapping]]] = ...) -> None: ...

class Flag(_message.Message):
    __slots__ = ("name", "type", "applies_to", "allowed_string_values", "min_value", "max_value", "requires_restart", "kind", "in_beta", "allowed_int_values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLIES_TO_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_RESTART_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    IN_BETA_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_INT_VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: SqlFlagType
    applies_to: _containers.RepeatedScalarFieldContainer[_cloud_sql_resources_pb2.SqlDatabaseVersion]
    allowed_string_values: _containers.RepeatedScalarFieldContainer[str]
    min_value: _wrappers_pb2.Int64Value
    max_value: _wrappers_pb2.Int64Value
    requires_restart: _wrappers_pb2.BoolValue
    kind: str
    in_beta: _wrappers_pb2.BoolValue
    allowed_int_values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[SqlFlagType, str]] = ..., applies_to: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.SqlDatabaseVersion, str]]] = ..., allowed_string_values: _Optional[_Iterable[str]] = ..., min_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., requires_restart: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., kind: _Optional[str] = ..., in_beta: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., allowed_int_values: _Optional[_Iterable[int]] = ...) -> None: ...
