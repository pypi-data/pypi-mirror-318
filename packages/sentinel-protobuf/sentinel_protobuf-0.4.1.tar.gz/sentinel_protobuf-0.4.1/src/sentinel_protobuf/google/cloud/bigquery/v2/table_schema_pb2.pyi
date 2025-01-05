from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TableSchema(_message.Message):
    __slots__ = ("fields", "foreign_type_info")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[TableFieldSchema]
    foreign_type_info: ForeignTypeInfo
    def __init__(self, fields: _Optional[_Iterable[_Union[TableFieldSchema, _Mapping]]] = ..., foreign_type_info: _Optional[_Union[ForeignTypeInfo, _Mapping]] = ...) -> None: ...

class ForeignTypeInfo(_message.Message):
    __slots__ = ("type_system",)
    class TypeSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_SYSTEM_UNSPECIFIED: _ClassVar[ForeignTypeInfo.TypeSystem]
        HIVE: _ClassVar[ForeignTypeInfo.TypeSystem]
    TYPE_SYSTEM_UNSPECIFIED: ForeignTypeInfo.TypeSystem
    HIVE: ForeignTypeInfo.TypeSystem
    TYPE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    type_system: ForeignTypeInfo.TypeSystem
    def __init__(self, type_system: _Optional[_Union[ForeignTypeInfo.TypeSystem, str]] = ...) -> None: ...

class DataPolicyOption(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TableFieldSchema(_message.Message):
    __slots__ = ("name", "type", "mode", "fields", "description", "policy_tags", "data_policies", "max_length", "precision", "scale", "rounding_mode", "collation", "default_value_expression", "range_element_type", "foreign_type_definition")
    class RoundingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUNDING_MODE_UNSPECIFIED: _ClassVar[TableFieldSchema.RoundingMode]
        ROUND_HALF_AWAY_FROM_ZERO: _ClassVar[TableFieldSchema.RoundingMode]
        ROUND_HALF_EVEN: _ClassVar[TableFieldSchema.RoundingMode]
    ROUNDING_MODE_UNSPECIFIED: TableFieldSchema.RoundingMode
    ROUND_HALF_AWAY_FROM_ZERO: TableFieldSchema.RoundingMode
    ROUND_HALF_EVEN: TableFieldSchema.RoundingMode
    class PolicyTagList(_message.Message):
        __slots__ = ("names",)
        NAMES_FIELD_NUMBER: _ClassVar[int]
        names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...
    class FieldElementType(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str
        def __init__(self, type: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
    DATA_POLICIES_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ROUNDING_MODE_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    RANGE_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_TYPE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    mode: str
    fields: _containers.RepeatedCompositeFieldContainer[TableFieldSchema]
    description: _wrappers_pb2.StringValue
    policy_tags: TableFieldSchema.PolicyTagList
    data_policies: _containers.RepeatedCompositeFieldContainer[DataPolicyOption]
    max_length: int
    precision: int
    scale: int
    rounding_mode: TableFieldSchema.RoundingMode
    collation: _wrappers_pb2.StringValue
    default_value_expression: _wrappers_pb2.StringValue
    range_element_type: TableFieldSchema.FieldElementType
    foreign_type_definition: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., mode: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[TableFieldSchema, _Mapping]]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., policy_tags: _Optional[_Union[TableFieldSchema.PolicyTagList, _Mapping]] = ..., data_policies: _Optional[_Iterable[_Union[DataPolicyOption, _Mapping]]] = ..., max_length: _Optional[int] = ..., precision: _Optional[int] = ..., scale: _Optional[int] = ..., rounding_mode: _Optional[_Union[TableFieldSchema.RoundingMode, str]] = ..., collation: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., default_value_expression: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., range_element_type: _Optional[_Union[TableFieldSchema.FieldElementType, _Mapping]] = ..., foreign_type_definition: _Optional[str] = ...) -> None: ...
