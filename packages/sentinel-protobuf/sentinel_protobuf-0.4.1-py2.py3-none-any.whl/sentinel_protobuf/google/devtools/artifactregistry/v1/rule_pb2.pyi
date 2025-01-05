from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Rule(_message.Message):
    __slots__ = ('name', 'action', 'operation', 'condition', 'package_id')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[Rule.Action]
        ALLOW: _ClassVar[Rule.Action]
        DENY: _ClassVar[Rule.Action]
    ACTION_UNSPECIFIED: Rule.Action
    ALLOW: Rule.Action
    DENY: Rule.Action

    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[Rule.Operation]
        DOWNLOAD: _ClassVar[Rule.Operation]
    OPERATION_UNSPECIFIED: Rule.Operation
    DOWNLOAD: Rule.Operation
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    action: Rule.Action
    operation: Rule.Operation
    condition: _expr_pb2.Expr
    package_id: str

    def __init__(self, name: _Optional[str]=..., action: _Optional[_Union[Rule.Action, str]]=..., operation: _Optional[_Union[Rule.Operation, str]]=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=..., package_id: _Optional[str]=...) -> None:
        ...

class ListRulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRulesResponse(_message.Message):
    __slots__ = ('rules', 'next_page_token')
    RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    next_page_token: str

    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRuleRequest(_message.Message):
    __slots__ = ('parent', 'rule_id', 'rule')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rule_id: str
    rule: Rule

    def __init__(self, parent: _Optional[str]=..., rule_id: _Optional[str]=..., rule: _Optional[_Union[Rule, _Mapping]]=...) -> None:
        ...

class UpdateRuleRequest(_message.Message):
    __slots__ = ('rule', 'update_mask')
    RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...