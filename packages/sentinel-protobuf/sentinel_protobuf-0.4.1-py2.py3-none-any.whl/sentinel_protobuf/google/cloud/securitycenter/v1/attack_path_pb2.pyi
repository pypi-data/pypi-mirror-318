from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AttackPath(_message.Message):
    __slots__ = ('name', 'path_nodes', 'edges')

    class AttackPathNode(_message.Message):
        __slots__ = ('resource', 'resource_type', 'display_name', 'associated_findings', 'uuid', 'attack_steps')

        class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NODE_TYPE_UNSPECIFIED: _ClassVar[AttackPath.AttackPathNode.NodeType]
            NODE_TYPE_AND: _ClassVar[AttackPath.AttackPathNode.NodeType]
            NODE_TYPE_OR: _ClassVar[AttackPath.AttackPathNode.NodeType]
            NODE_TYPE_DEFENSE: _ClassVar[AttackPath.AttackPathNode.NodeType]
            NODE_TYPE_ATTACKER: _ClassVar[AttackPath.AttackPathNode.NodeType]
        NODE_TYPE_UNSPECIFIED: AttackPath.AttackPathNode.NodeType
        NODE_TYPE_AND: AttackPath.AttackPathNode.NodeType
        NODE_TYPE_OR: AttackPath.AttackPathNode.NodeType
        NODE_TYPE_DEFENSE: AttackPath.AttackPathNode.NodeType
        NODE_TYPE_ATTACKER: AttackPath.AttackPathNode.NodeType

        class PathNodeAssociatedFinding(_message.Message):
            __slots__ = ('canonical_finding', 'finding_category', 'name')
            CANONICAL_FINDING_FIELD_NUMBER: _ClassVar[int]
            FINDING_CATEGORY_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            canonical_finding: str
            finding_category: str
            name: str

            def __init__(self, canonical_finding: _Optional[str]=..., finding_category: _Optional[str]=..., name: _Optional[str]=...) -> None:
                ...

        class AttackStepNode(_message.Message):
            __slots__ = ('uuid', 'type', 'display_name', 'labels', 'description')

            class LabelsEntry(_message.Message):
                __slots__ = ('key', 'value')
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str

                def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                    ...
            UUID_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            LABELS_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            uuid: str
            type: AttackPath.AttackPathNode.NodeType
            display_name: str
            labels: _containers.ScalarMap[str, str]
            description: str

            def __init__(self, uuid: _Optional[str]=..., type: _Optional[_Union[AttackPath.AttackPathNode.NodeType, str]]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=...) -> None:
                ...
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ASSOCIATED_FINDINGS_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        ATTACK_STEPS_FIELD_NUMBER: _ClassVar[int]
        resource: str
        resource_type: str
        display_name: str
        associated_findings: _containers.RepeatedCompositeFieldContainer[AttackPath.AttackPathNode.PathNodeAssociatedFinding]
        uuid: str
        attack_steps: _containers.RepeatedCompositeFieldContainer[AttackPath.AttackPathNode.AttackStepNode]

        def __init__(self, resource: _Optional[str]=..., resource_type: _Optional[str]=..., display_name: _Optional[str]=..., associated_findings: _Optional[_Iterable[_Union[AttackPath.AttackPathNode.PathNodeAssociatedFinding, _Mapping]]]=..., uuid: _Optional[str]=..., attack_steps: _Optional[_Iterable[_Union[AttackPath.AttackPathNode.AttackStepNode, _Mapping]]]=...) -> None:
            ...

    class AttackPathEdge(_message.Message):
        __slots__ = ('source', 'destination')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        source: str
        destination: str

        def __init__(self, source: _Optional[str]=..., destination: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    path_nodes: _containers.RepeatedCompositeFieldContainer[AttackPath.AttackPathNode]
    edges: _containers.RepeatedCompositeFieldContainer[AttackPath.AttackPathEdge]

    def __init__(self, name: _Optional[str]=..., path_nodes: _Optional[_Iterable[_Union[AttackPath.AttackPathNode, _Mapping]]]=..., edges: _Optional[_Iterable[_Union[AttackPath.AttackPathEdge, _Mapping]]]=...) -> None:
        ...