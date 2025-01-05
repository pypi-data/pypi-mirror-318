from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Constraint(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'constraint_default', 'list_constraint', 'boolean_constraint', 'supports_dry_run')

    class ConstraintDefault(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONSTRAINT_DEFAULT_UNSPECIFIED: _ClassVar[Constraint.ConstraintDefault]
        ALLOW: _ClassVar[Constraint.ConstraintDefault]
        DENY: _ClassVar[Constraint.ConstraintDefault]
    CONSTRAINT_DEFAULT_UNSPECIFIED: Constraint.ConstraintDefault
    ALLOW: Constraint.ConstraintDefault
    DENY: Constraint.ConstraintDefault

    class ListConstraint(_message.Message):
        __slots__ = ('supports_in', 'supports_under')
        SUPPORTS_IN_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_UNDER_FIELD_NUMBER: _ClassVar[int]
        supports_in: bool
        supports_under: bool

        def __init__(self, supports_in: bool=..., supports_under: bool=...) -> None:
            ...

    class BooleanConstraint(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    LIST_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    constraint_default: Constraint.ConstraintDefault
    list_constraint: Constraint.ListConstraint
    boolean_constraint: Constraint.BooleanConstraint
    supports_dry_run: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., constraint_default: _Optional[_Union[Constraint.ConstraintDefault, str]]=..., list_constraint: _Optional[_Union[Constraint.ListConstraint, _Mapping]]=..., boolean_constraint: _Optional[_Union[Constraint.BooleanConstraint, _Mapping]]=..., supports_dry_run: bool=...) -> None:
        ...

class CustomConstraint(_message.Message):
    __slots__ = ('name', 'resource_types', 'method_types', 'condition', 'action_type', 'display_name', 'description', 'update_time')

    class MethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_TYPE_UNSPECIFIED: _ClassVar[CustomConstraint.MethodType]
        CREATE: _ClassVar[CustomConstraint.MethodType]
        UPDATE: _ClassVar[CustomConstraint.MethodType]
        DELETE: _ClassVar[CustomConstraint.MethodType]
        REMOVE_GRANT: _ClassVar[CustomConstraint.MethodType]
        GOVERN_TAGS: _ClassVar[CustomConstraint.MethodType]
    METHOD_TYPE_UNSPECIFIED: CustomConstraint.MethodType
    CREATE: CustomConstraint.MethodType
    UPDATE: CustomConstraint.MethodType
    DELETE: CustomConstraint.MethodType
    REMOVE_GRANT: CustomConstraint.MethodType
    GOVERN_TAGS: CustomConstraint.MethodType

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