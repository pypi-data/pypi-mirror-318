from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyRule(_message.Message):
    __slots__ = ('values', 'allow_all', 'deny_all', 'enforce', 'condition')

    class StringValues(_message.Message):
        __slots__ = ('allowed_values', 'denied_values')
        ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
        DENIED_VALUES_FIELD_NUMBER: _ClassVar[int]
        allowed_values: _containers.RepeatedScalarFieldContainer[str]
        denied_values: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, allowed_values: _Optional[_Iterable[str]]=..., denied_values: _Optional[_Iterable[str]]=...) -> None:
            ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_FIELD_NUMBER: _ClassVar[int]
    DENY_ALL_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    values: PolicyRule.StringValues
    allow_all: bool
    deny_all: bool
    enforce: bool
    condition: _expr_pb2.Expr

    def __init__(self, values: _Optional[_Union[PolicyRule.StringValues, _Mapping]]=..., allow_all: bool=..., deny_all: bool=..., enforce: bool=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=...) -> None:
        ...

class CustomConstraint(_message.Message):
    __slots__ = ('name', 'resource_types', 'method_types', 'condition', 'action_type', 'display_name', 'description', 'update_time')

    class MethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_TYPE_UNSPECIFIED: _ClassVar[CustomConstraint.MethodType]
        CREATE: _ClassVar[CustomConstraint.MethodType]
        UPDATE: _ClassVar[CustomConstraint.MethodType]
        DELETE: _ClassVar[CustomConstraint.MethodType]
    METHOD_TYPE_UNSPECIFIED: CustomConstraint.MethodType
    CREATE: CustomConstraint.MethodType
    UPDATE: CustomConstraint.MethodType
    DELETE: CustomConstraint.MethodType

    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[CustomConstraint.ActionType]
        ALLOW: _ClassVar[CustomConstraint.ActionType]
        DENY: _ClassVar[CustomConstraint.ActionType]
    ACTION_TYPE_UNSPECIFIED: CustomConstraint.ActionType
    ALLOW: CustomConstraint.ActionType
    DENY: CustomConstraint.ActionType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    METHOD_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource_types: _containers.RepeatedScalarFieldContainer[str]
    method_types: _containers.RepeatedScalarFieldContainer[CustomConstraint.MethodType]
    condition: str
    action_type: CustomConstraint.ActionType
    display_name: str
    description: str
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., resource_types: _Optional[_Iterable[str]]=..., method_types: _Optional[_Iterable[_Union[CustomConstraint.MethodType, str]]]=..., condition: _Optional[str]=..., action_type: _Optional[_Union[CustomConstraint.ActionType, str]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...