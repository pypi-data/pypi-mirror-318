from google.ads.admanager.v1 import taxonomy_type_enum_pb2 as _taxonomy_type_enum_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TaxonomyCategory(_message.Message):
    __slots__ = ('name', 'taxonomy_category_id', 'display_name', 'grouping_only', 'parent_taxonomy_category_id', 'taxonomy_type', 'ancestor_names', 'ancestor_taxonomy_category_ids')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPING_ONLY_FIELD_NUMBER: _ClassVar[int]
    PARENT_TAXONOMY_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_NAMES_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_TAXONOMY_CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    taxonomy_category_id: int
    display_name: str
    grouping_only: bool
    parent_taxonomy_category_id: int
    taxonomy_type: _taxonomy_type_enum_pb2.TaxonomyTypeEnum.TaxonomyType
    ancestor_names: _containers.RepeatedScalarFieldContainer[str]
    ancestor_taxonomy_category_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, name: _Optional[str]=..., taxonomy_category_id: _Optional[int]=..., display_name: _Optional[str]=..., grouping_only: bool=..., parent_taxonomy_category_id: _Optional[int]=..., taxonomy_type: _Optional[_Union[_taxonomy_type_enum_pb2.TaxonomyTypeEnum.TaxonomyType, str]]=..., ancestor_names: _Optional[_Iterable[str]]=..., ancestor_taxonomy_category_ids: _Optional[_Iterable[int]]=...) -> None:
        ...