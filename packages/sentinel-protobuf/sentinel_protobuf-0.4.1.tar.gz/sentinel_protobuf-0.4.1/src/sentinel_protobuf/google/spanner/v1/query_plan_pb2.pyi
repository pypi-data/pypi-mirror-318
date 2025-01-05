from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PlanNode(_message.Message):
    __slots__ = ('index', 'kind', 'display_name', 'child_links', 'short_representation', 'metadata', 'execution_stats')

    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[PlanNode.Kind]
        RELATIONAL: _ClassVar[PlanNode.Kind]
        SCALAR: _ClassVar[PlanNode.Kind]
    KIND_UNSPECIFIED: PlanNode.Kind
    RELATIONAL: PlanNode.Kind
    SCALAR: PlanNode.Kind

    class ChildLink(_message.Message):
        __slots__ = ('child_index', 'type', 'variable')
        CHILD_INDEX_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VARIABLE_FIELD_NUMBER: _ClassVar[int]
        child_index: int
        type: str
        variable: str

        def __init__(self, child_index: _Optional[int]=..., type: _Optional[str]=..., variable: _Optional[str]=...) -> None:
            ...

    class ShortRepresentation(_message.Message):
        __slots__ = ('description', 'subqueries')

        class SubqueriesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int

            def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
                ...
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SUBQUERIES_FIELD_NUMBER: _ClassVar[int]
        description: str
        subqueries: _containers.ScalarMap[str, int]

        def __init__(self, description: _Optional[str]=..., subqueries: _Optional[_Mapping[str, int]]=...) -> None:
            ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHILD_LINKS_FIELD_NUMBER: _ClassVar[int]
    SHORT_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATS_FIELD_NUMBER: _ClassVar[int]
    index: int
    kind: PlanNode.Kind
    display_name: str
    child_links: _containers.RepeatedCompositeFieldContainer[PlanNode.ChildLink]
    short_representation: PlanNode.ShortRepresentation
    metadata: _struct_pb2.Struct
    execution_stats: _struct_pb2.Struct

    def __init__(self, index: _Optional[int]=..., kind: _Optional[_Union[PlanNode.Kind, str]]=..., display_name: _Optional[str]=..., child_links: _Optional[_Iterable[_Union[PlanNode.ChildLink, _Mapping]]]=..., short_representation: _Optional[_Union[PlanNode.ShortRepresentation, _Mapping]]=..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., execution_stats: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class QueryPlan(_message.Message):
    __slots__ = ('plan_nodes',)
    PLAN_NODES_FIELD_NUMBER: _ClassVar[int]
    plan_nodes: _containers.RepeatedCompositeFieldContainer[PlanNode]

    def __init__(self, plan_nodes: _Optional[_Iterable[_Union[PlanNode, _Mapping]]]=...) -> None:
        ...