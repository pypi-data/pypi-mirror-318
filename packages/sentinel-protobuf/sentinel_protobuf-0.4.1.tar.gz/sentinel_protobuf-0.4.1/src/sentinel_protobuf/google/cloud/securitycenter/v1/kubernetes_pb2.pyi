from google.cloud.securitycenter.v1 import container_pb2 as _container_pb2
from google.cloud.securitycenter.v1 import label_pb2 as _label_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Kubernetes(_message.Message):
    __slots__ = ('pods', 'nodes', 'node_pools', 'roles', 'bindings', 'access_reviews', 'objects')

    class Pod(_message.Message):
        __slots__ = ('ns', 'name', 'labels', 'containers')
        NS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        CONTAINERS_FIELD_NUMBER: _ClassVar[int]
        ns: str
        name: str
        labels: _containers.RepeatedCompositeFieldContainer[_label_pb2.Label]
        containers: _containers.RepeatedCompositeFieldContainer[_container_pb2.Container]

        def __init__(self, ns: _Optional[str]=..., name: _Optional[str]=..., labels: _Optional[_Iterable[_Union[_label_pb2.Label, _Mapping]]]=..., containers: _Optional[_Iterable[_Union[_container_pb2.Container, _Mapping]]]=...) -> None:
            ...

    class Node(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...

    class NodePool(_message.Message):
        __slots__ = ('name', 'nodes')
        NAME_FIELD_NUMBER: _ClassVar[int]
        NODES_FIELD_NUMBER: _ClassVar[int]
        name: str
        nodes: _containers.RepeatedCompositeFieldContainer[Kubernetes.Node]

        def __init__(self, name: _Optional[str]=..., nodes: _Optional[_Iterable[_Union[Kubernetes.Node, _Mapping]]]=...) -> None:
            ...

    class Role(_message.Message):
        __slots__ = ('kind', 'ns', 'name')

        class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            KIND_UNSPECIFIED: _ClassVar[Kubernetes.Role.Kind]
            ROLE: _ClassVar[Kubernetes.Role.Kind]
            CLUSTER_ROLE: _ClassVar[Kubernetes.Role.Kind]
        KIND_UNSPECIFIED: Kubernetes.Role.Kind
        ROLE: Kubernetes.Role.Kind
        CLUSTER_ROLE: Kubernetes.Role.Kind
        KIND_FIELD_NUMBER: _ClassVar[int]
        NS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        kind: Kubernetes.Role.Kind
        ns: str
        name: str

        def __init__(self, kind: _Optional[_Union[Kubernetes.Role.Kind, str]]=..., ns: _Optional[str]=..., name: _Optional[str]=...) -> None:
            ...

    class Binding(_message.Message):
        __slots__ = ('ns', 'name', 'role', 'subjects')
        NS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        SUBJECTS_FIELD_NUMBER: _ClassVar[int]
        ns: str
        name: str
        role: Kubernetes.Role
        subjects: _containers.RepeatedCompositeFieldContainer[Kubernetes.Subject]

        def __init__(self, ns: _Optional[str]=..., name: _Optional[str]=..., role: _Optional[_Union[Kubernetes.Role, _Mapping]]=..., subjects: _Optional[_Iterable[_Union[Kubernetes.Subject, _Mapping]]]=...) -> None:
            ...

    class Subject(_message.Message):
        __slots__ = ('kind', 'ns', 'name')

        class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUTH_TYPE_UNSPECIFIED: _ClassVar[Kubernetes.Subject.AuthType]
            USER: _ClassVar[Kubernetes.Subject.AuthType]
            SERVICEACCOUNT: _ClassVar[Kubernetes.Subject.AuthType]
            GROUP: _ClassVar[Kubernetes.Subject.AuthType]
        AUTH_TYPE_UNSPECIFIED: Kubernetes.Subject.AuthType
        USER: Kubernetes.Subject.AuthType
        SERVICEACCOUNT: Kubernetes.Subject.AuthType
        GROUP: Kubernetes.Subject.AuthType
        KIND_FIELD_NUMBER: _ClassVar[int]
        NS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        kind: Kubernetes.Subject.AuthType
        ns: str
        name: str

        def __init__(self, kind: _Optional[_Union[Kubernetes.Subject.AuthType, str]]=..., ns: _Optional[str]=..., name: _Optional[str]=...) -> None:
            ...

    class AccessReview(_message.Message):
        __slots__ = ('group', 'ns', 'name', 'resource', 'subresource', 'verb', 'version')
        GROUP_FIELD_NUMBER: _ClassVar[int]
        NS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        SUBRESOURCE_FIELD_NUMBER: _ClassVar[int]
        VERB_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        group: str
        ns: str
        name: str
        resource: str
        subresource: str
        verb: str
        version: str

        def __init__(self, group: _Optional[str]=..., ns: _Optional[str]=..., name: _Optional[str]=..., resource: _Optional[str]=..., subresource: _Optional[str]=..., verb: _Optional[str]=..., version: _Optional[str]=...) -> None:
            ...

    class Object(_message.Message):
        __slots__ = ('group', 'kind', 'ns', 'name', 'containers')
        GROUP_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        NS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINERS_FIELD_NUMBER: _ClassVar[int]
        group: str
        kind: str
        ns: str
        name: str
        containers: _containers.RepeatedCompositeFieldContainer[_container_pb2.Container]

        def __init__(self, group: _Optional[str]=..., kind: _Optional[str]=..., ns: _Optional[str]=..., name: _Optional[str]=..., containers: _Optional[_Iterable[_Union[_container_pb2.Container, _Mapping]]]=...) -> None:
            ...
    PODS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    pods: _containers.RepeatedCompositeFieldContainer[Kubernetes.Pod]
    nodes: _containers.RepeatedCompositeFieldContainer[Kubernetes.Node]
    node_pools: _containers.RepeatedCompositeFieldContainer[Kubernetes.NodePool]
    roles: _containers.RepeatedCompositeFieldContainer[Kubernetes.Role]
    bindings: _containers.RepeatedCompositeFieldContainer[Kubernetes.Binding]
    access_reviews: _containers.RepeatedCompositeFieldContainer[Kubernetes.AccessReview]
    objects: _containers.RepeatedCompositeFieldContainer[Kubernetes.Object]

    def __init__(self, pods: _Optional[_Iterable[_Union[Kubernetes.Pod, _Mapping]]]=..., nodes: _Optional[_Iterable[_Union[Kubernetes.Node, _Mapping]]]=..., node_pools: _Optional[_Iterable[_Union[Kubernetes.NodePool, _Mapping]]]=..., roles: _Optional[_Iterable[_Union[Kubernetes.Role, _Mapping]]]=..., bindings: _Optional[_Iterable[_Union[Kubernetes.Binding, _Mapping]]]=..., access_reviews: _Optional[_Iterable[_Union[Kubernetes.AccessReview, _Mapping]]]=..., objects: _Optional[_Iterable[_Union[Kubernetes.Object, _Mapping]]]=...) -> None:
        ...