from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.datacatalog.v1beta1 import policytagmanager_pb2 as _policytagmanager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SerializedTaxonomy(_message.Message):
    __slots__ = ('display_name', 'description', 'policy_tags', 'activated_policy_types')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_POLICY_TYPES_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    policy_tags: _containers.RepeatedCompositeFieldContainer[SerializedPolicyTag]
    activated_policy_types: _containers.RepeatedScalarFieldContainer[_policytagmanager_pb2.Taxonomy.PolicyType]

    def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., policy_tags: _Optional[_Iterable[_Union[SerializedPolicyTag, _Mapping]]]=..., activated_policy_types: _Optional[_Iterable[_Union[_policytagmanager_pb2.Taxonomy.PolicyType, str]]]=...) -> None:
        ...

class SerializedPolicyTag(_message.Message):
    __slots__ = ('policy_tag', 'display_name', 'description', 'child_policy_tags')
    POLICY_TAG_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHILD_POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
    policy_tag: str
    display_name: str
    description: str
    child_policy_tags: _containers.RepeatedCompositeFieldContainer[SerializedPolicyTag]

    def __init__(self, policy_tag: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., child_policy_tags: _Optional[_Iterable[_Union[SerializedPolicyTag, _Mapping]]]=...) -> None:
        ...

class ImportTaxonomiesRequest(_message.Message):
    __slots__ = ('parent', 'inline_source')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    inline_source: InlineSource

    def __init__(self, parent: _Optional[str]=..., inline_source: _Optional[_Union[InlineSource, _Mapping]]=...) -> None:
        ...

class InlineSource(_message.Message):
    __slots__ = ('taxonomies',)
    TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    taxonomies: _containers.RepeatedCompositeFieldContainer[SerializedTaxonomy]

    def __init__(self, taxonomies: _Optional[_Iterable[_Union[SerializedTaxonomy, _Mapping]]]=...) -> None:
        ...

class ImportTaxonomiesResponse(_message.Message):
    __slots__ = ('taxonomies',)
    TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    taxonomies: _containers.RepeatedCompositeFieldContainer[_policytagmanager_pb2.Taxonomy]

    def __init__(self, taxonomies: _Optional[_Iterable[_Union[_policytagmanager_pb2.Taxonomy, _Mapping]]]=...) -> None:
        ...

class ExportTaxonomiesRequest(_message.Message):
    __slots__ = ('parent', 'taxonomies', 'serialized_taxonomies')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    taxonomies: _containers.RepeatedScalarFieldContainer[str]
    serialized_taxonomies: bool

    def __init__(self, parent: _Optional[str]=..., taxonomies: _Optional[_Iterable[str]]=..., serialized_taxonomies: bool=...) -> None:
        ...

class ExportTaxonomiesResponse(_message.Message):
    __slots__ = ('taxonomies',)
    TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    taxonomies: _containers.RepeatedCompositeFieldContainer[SerializedTaxonomy]

    def __init__(self, taxonomies: _Optional[_Iterable[_Union[SerializedTaxonomy, _Mapping]]]=...) -> None:
        ...