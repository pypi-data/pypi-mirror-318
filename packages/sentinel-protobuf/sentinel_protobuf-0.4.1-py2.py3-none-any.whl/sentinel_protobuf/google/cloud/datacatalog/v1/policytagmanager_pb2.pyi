from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.datacatalog.v1 import common_pb2 as _common_pb2
from google.cloud.datacatalog.v1 import timestamps_pb2 as _timestamps_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Taxonomy(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'policy_tag_count', 'taxonomy_timestamps', 'activated_policy_types', 'service')

    class PolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POLICY_TYPE_UNSPECIFIED: _ClassVar[Taxonomy.PolicyType]
        FINE_GRAINED_ACCESS_CONTROL: _ClassVar[Taxonomy.PolicyType]
    POLICY_TYPE_UNSPECIFIED: Taxonomy.PolicyType
    FINE_GRAINED_ACCESS_CONTROL: Taxonomy.PolicyType

    class Service(_message.Message):
        __slots__ = ('name', 'identity')
        NAME_FIELD_NUMBER: _ClassVar[int]
        IDENTITY_FIELD_NUMBER: _ClassVar[int]
        name: _common_pb2.ManagingSystem
        identity: str

        def __init__(self, name: _Optional[_Union[_common_pb2.ManagingSystem, str]]=..., identity: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_POLICY_TYPES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    policy_tag_count: int
    taxonomy_timestamps: _timestamps_pb2.SystemTimestamps
    activated_policy_types: _containers.RepeatedScalarFieldContainer[Taxonomy.PolicyType]
    service: Taxonomy.Service

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., policy_tag_count: _Optional[int]=..., taxonomy_timestamps: _Optional[_Union[_timestamps_pb2.SystemTimestamps, _Mapping]]=..., activated_policy_types: _Optional[_Iterable[_Union[Taxonomy.PolicyType, str]]]=..., service: _Optional[_Union[Taxonomy.Service, _Mapping]]=...) -> None:
        ...

class PolicyTag(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'parent_policy_tag', 'child_policy_tags')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARENT_POLICY_TAG_FIELD_NUMBER: _ClassVar[int]
    CHILD_POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    parent_policy_tag: str
    child_policy_tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., parent_policy_tag: _Optional[str]=..., child_policy_tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateTaxonomyRequest(_message.Message):
    __slots__ = ('parent', 'taxonomy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    taxonomy: Taxonomy

    def __init__(self, parent: _Optional[str]=..., taxonomy: _Optional[_Union[Taxonomy, _Mapping]]=...) -> None:
        ...

class DeleteTaxonomyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateTaxonomyRequest(_message.Message):
    __slots__ = ('taxonomy', 'update_mask')
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    taxonomy: Taxonomy
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, taxonomy: _Optional[_Union[Taxonomy, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTaxonomiesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListTaxonomiesResponse(_message.Message):
    __slots__ = ('taxonomies', 'next_page_token')
    TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    taxonomies: _containers.RepeatedCompositeFieldContainer[Taxonomy]
    next_page_token: str

    def __init__(self, taxonomies: _Optional[_Iterable[_Union[Taxonomy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTaxonomyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePolicyTagRequest(_message.Message):
    __slots__ = ('parent', 'policy_tag')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_TAG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    policy_tag: PolicyTag

    def __init__(self, parent: _Optional[str]=..., policy_tag: _Optional[_Union[PolicyTag, _Mapping]]=...) -> None:
        ...

class DeletePolicyTagRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePolicyTagRequest(_message.Message):
    __slots__ = ('policy_tag', 'update_mask')
    POLICY_TAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    policy_tag: PolicyTag
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, policy_tag: _Optional[_Union[PolicyTag, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListPolicyTagsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPolicyTagsResponse(_message.Message):
    __slots__ = ('policy_tags', 'next_page_token')
    POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policy_tags: _containers.RepeatedCompositeFieldContainer[PolicyTag]
    next_page_token: str

    def __init__(self, policy_tags: _Optional[_Iterable[_Union[PolicyTag, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPolicyTagRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...