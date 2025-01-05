from google.api import annotations_pb2 as _annotations_pb2
from google.genomics.v1 import range_pb2 as _range_pb2
from google.genomics.v1 import readalignment_pb2 as _readalignment_pb2
from google.genomics.v1 import readgroupset_pb2 as _readgroupset_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SearchReadGroupSetsRequest(_message.Message):
    __slots__ = ('dataset_ids', 'name', 'page_token', 'page_size')
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    page_token: str
    page_size: int

    def __init__(self, dataset_ids: _Optional[_Iterable[str]]=..., name: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchReadGroupSetsResponse(_message.Message):
    __slots__ = ('read_group_sets', 'next_page_token')
    READ_GROUP_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    read_group_sets: _containers.RepeatedCompositeFieldContainer[_readgroupset_pb2.ReadGroupSet]
    next_page_token: str

    def __init__(self, read_group_sets: _Optional[_Iterable[_Union[_readgroupset_pb2.ReadGroupSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ImportReadGroupSetsRequest(_message.Message):
    __slots__ = ('dataset_id', 'reference_set_id', 'source_uris', 'partition_strategy')

    class PartitionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTITION_STRATEGY_UNSPECIFIED: _ClassVar[ImportReadGroupSetsRequest.PartitionStrategy]
        PER_FILE_PER_SAMPLE: _ClassVar[ImportReadGroupSetsRequest.PartitionStrategy]
        MERGE_ALL: _ClassVar[ImportReadGroupSetsRequest.PartitionStrategy]
    PARTITION_STRATEGY_UNSPECIFIED: ImportReadGroupSetsRequest.PartitionStrategy
    PER_FILE_PER_SAMPLE: ImportReadGroupSetsRequest.PartitionStrategy
    MERGE_ALL: ImportReadGroupSetsRequest.PartitionStrategy
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    reference_set_id: str
    source_uris: _containers.RepeatedScalarFieldContainer[str]
    partition_strategy: ImportReadGroupSetsRequest.PartitionStrategy

    def __init__(self, dataset_id: _Optional[str]=..., reference_set_id: _Optional[str]=..., source_uris: _Optional[_Iterable[str]]=..., partition_strategy: _Optional[_Union[ImportReadGroupSetsRequest.PartitionStrategy, str]]=...) -> None:
        ...

class ImportReadGroupSetsResponse(_message.Message):
    __slots__ = ('read_group_set_ids',)
    READ_GROUP_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    read_group_set_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, read_group_set_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExportReadGroupSetRequest(_message.Message):
    __slots__ = ('project_id', 'export_uri', 'read_group_set_id', 'reference_names')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_URI_FIELD_NUMBER: _ClassVar[int]
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    export_uri: str
    read_group_set_id: str
    reference_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, project_id: _Optional[str]=..., export_uri: _Optional[str]=..., read_group_set_id: _Optional[str]=..., reference_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateReadGroupSetRequest(_message.Message):
    __slots__ = ('read_group_set_id', 'read_group_set', 'update_mask')
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    READ_GROUP_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    read_group_set_id: str
    read_group_set: _readgroupset_pb2.ReadGroupSet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, read_group_set_id: _Optional[str]=..., read_group_set: _Optional[_Union[_readgroupset_pb2.ReadGroupSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteReadGroupSetRequest(_message.Message):
    __slots__ = ('read_group_set_id',)
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    read_group_set_id: str

    def __init__(self, read_group_set_id: _Optional[str]=...) -> None:
        ...

class GetReadGroupSetRequest(_message.Message):
    __slots__ = ('read_group_set_id',)
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    read_group_set_id: str

    def __init__(self, read_group_set_id: _Optional[str]=...) -> None:
        ...

class ListCoverageBucketsRequest(_message.Message):
    __slots__ = ('read_group_set_id', 'reference_name', 'start', 'end', 'target_bucket_width', 'page_token', 'page_size')
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TARGET_BUCKET_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    read_group_set_id: str
    reference_name: str
    start: int
    end: int
    target_bucket_width: int
    page_token: str
    page_size: int

    def __init__(self, read_group_set_id: _Optional[str]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., target_bucket_width: _Optional[int]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class CoverageBucket(_message.Message):
    __slots__ = ('range', 'mean_coverage')
    RANGE_FIELD_NUMBER: _ClassVar[int]
    MEAN_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    range: _range_pb2.Range
    mean_coverage: float

    def __init__(self, range: _Optional[_Union[_range_pb2.Range, _Mapping]]=..., mean_coverage: _Optional[float]=...) -> None:
        ...

class ListCoverageBucketsResponse(_message.Message):
    __slots__ = ('bucket_width', 'coverage_buckets', 'next_page_token')
    BUCKET_WIDTH_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bucket_width: int
    coverage_buckets: _containers.RepeatedCompositeFieldContainer[CoverageBucket]
    next_page_token: str

    def __init__(self, bucket_width: _Optional[int]=..., coverage_buckets: _Optional[_Iterable[_Union[CoverageBucket, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchReadsRequest(_message.Message):
    __slots__ = ('read_group_set_ids', 'read_group_ids', 'reference_name', 'start', 'end', 'page_token', 'page_size')
    READ_GROUP_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    READ_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    read_group_set_ids: _containers.RepeatedScalarFieldContainer[str]
    read_group_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_name: str
    start: int
    end: int
    page_token: str
    page_size: int

    def __init__(self, read_group_set_ids: _Optional[_Iterable[str]]=..., read_group_ids: _Optional[_Iterable[str]]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchReadsResponse(_message.Message):
    __slots__ = ('alignments', 'next_page_token')
    ALIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    alignments: _containers.RepeatedCompositeFieldContainer[_readalignment_pb2.Read]
    next_page_token: str

    def __init__(self, alignments: _Optional[_Iterable[_Union[_readalignment_pb2.Read, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class StreamReadsRequest(_message.Message):
    __slots__ = ('project_id', 'read_group_set_id', 'reference_name', 'start', 'end', 'shard', 'total_shards')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    READ_GROUP_SET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARDS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    read_group_set_id: str
    reference_name: str
    start: int
    end: int
    shard: int
    total_shards: int

    def __init__(self, project_id: _Optional[str]=..., read_group_set_id: _Optional[str]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., shard: _Optional[int]=..., total_shards: _Optional[int]=...) -> None:
        ...

class StreamReadsResponse(_message.Message):
    __slots__ = ('alignments',)
    ALIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    alignments: _containers.RepeatedCompositeFieldContainer[_readalignment_pb2.Read]

    def __init__(self, alignments: _Optional[_Iterable[_Union[_readalignment_pb2.Read, _Mapping]]]=...) -> None:
        ...