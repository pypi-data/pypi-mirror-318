from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import rule_engine_pb2 as _rule_engine_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateRuleSetRequest(_message.Message):
    __slots__ = ('parent', 'rule_set')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rule_set: _rule_engine_pb2.RuleSet

    def __init__(self, parent: _Optional[str]=..., rule_set: _Optional[_Union[_rule_engine_pb2.RuleSet, _Mapping]]=...) -> None:
        ...

class GetRuleSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateRuleSetRequest(_message.Message):
    __slots__ = ('name', 'rule_set')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_FIELD_NUMBER: _ClassVar[int]
    name: str
    rule_set: _rule_engine_pb2.RuleSet

    def __init__(self, name: _Optional[str]=..., rule_set: _Optional[_Union[_rule_engine_pb2.RuleSet, _Mapping]]=...) -> None:
        ...

class DeleteRuleSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRuleSetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRuleSetsResponse(_message.Message):
    __slots__ = ('rule_sets', 'next_page_token')
    RULE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rule_sets: _containers.RepeatedCompositeFieldContainer[_rule_engine_pb2.RuleSet]
    next_page_token: str

    def __init__(self, rule_sets: _Optional[_Iterable[_Union[_rule_engine_pb2.RuleSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...