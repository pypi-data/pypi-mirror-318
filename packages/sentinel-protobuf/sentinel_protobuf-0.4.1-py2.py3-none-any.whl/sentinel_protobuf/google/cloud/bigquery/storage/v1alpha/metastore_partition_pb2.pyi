from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.storage.v1alpha import partition_pb2 as _partition_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateMetastorePartitionRequest(_message.Message):
    __slots__ = ('parent', 'metastore_partition')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METASTORE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metastore_partition: _partition_pb2.MetastorePartition

    def __init__(self, parent: _Optional[str]=..., metastore_partition: _Optional[_Union[_partition_pb2.MetastorePartition, _Mapping]]=...) -> None:
        ...

class BatchCreateMetastorePartitionsRequest(_message.Message):
    __slots__ = ('parent', 'requests', 'skip_existing_partitions')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SKIP_EXISTING_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateMetastorePartitionRequest]
    skip_existing_partitions: bool

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateMetastorePartitionRequest, _Mapping]]]=..., skip_existing_partitions: bool=...) -> None:
        ...

class BatchCreateMetastorePartitionsResponse(_message.Message):
    __slots__ = ('partitions',)
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedCompositeFieldContainer[_partition_pb2.MetastorePartition]

    def __init__(self, partitions: _Optional[_Iterable[_Union[_partition_pb2.MetastorePartition, _Mapping]]]=...) -> None:
        ...

class BatchDeleteMetastorePartitionsRequest(_message.Message):
    __slots__ = ('parent', 'partition_values')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_VALUES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    partition_values: _containers.RepeatedCompositeFieldContainer[_partition_pb2.MetastorePartitionValues]

    def __init__(self, parent: _Optional[str]=..., partition_values: _Optional[_Iterable[_Union[_partition_pb2.MetastorePartitionValues, _Mapping]]]=...) -> None:
        ...

class UpdateMetastorePartitionRequest(_message.Message):
    __slots__ = ('metastore_partition', 'update_mask')
    METASTORE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    metastore_partition: _partition_pb2.MetastorePartition
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, metastore_partition: _Optional[_Union[_partition_pb2.MetastorePartition, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class BatchUpdateMetastorePartitionsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateMetastorePartitionRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateMetastorePartitionRequest, _Mapping]]]=...) -> None:
        ...

class BatchUpdateMetastorePartitionsResponse(_message.Message):
    __slots__ = ('partitions',)
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedCompositeFieldContainer[_partition_pb2.MetastorePartition]

    def __init__(self, partitions: _Optional[_Iterable[_Union[_partition_pb2.MetastorePartition, _Mapping]]]=...) -> None:
        ...

class ListMetastorePartitionsRequest(_message.Message):
    __slots__ = ('parent', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListMetastorePartitionsResponse(_message.Message):
    __slots__ = ('partitions', 'streams')
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    partitions: _partition_pb2.MetastorePartitionList
    streams: _partition_pb2.StreamList

    def __init__(self, partitions: _Optional[_Union[_partition_pb2.MetastorePartitionList, _Mapping]]=..., streams: _Optional[_Union[_partition_pb2.StreamList, _Mapping]]=...) -> None:
        ...

class StreamMetastorePartitionsRequest(_message.Message):
    __slots__ = ('parent', 'metastore_partitions', 'skip_existing_partitions')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METASTORE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SKIP_EXISTING_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metastore_partitions: _containers.RepeatedCompositeFieldContainer[_partition_pb2.MetastorePartition]
    skip_existing_partitions: bool

    def __init__(self, parent: _Optional[str]=..., metastore_partitions: _Optional[_Iterable[_Union[_partition_pb2.MetastorePartition, _Mapping]]]=..., skip_existing_partitions: bool=...) -> None:
        ...

class StreamMetastorePartitionsResponse(_message.Message):
    __slots__ = ('total_partitions_streamed_count', 'total_partitions_inserted_count')
    TOTAL_PARTITIONS_STREAMED_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PARTITIONS_INSERTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_partitions_streamed_count: int
    total_partitions_inserted_count: int

    def __init__(self, total_partitions_streamed_count: _Optional[int]=..., total_partitions_inserted_count: _Optional[int]=...) -> None:
        ...

class BatchSizeTooLargeError(_message.Message):
    __slots__ = ('max_batch_size', 'error_message')
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    max_batch_size: int
    error_message: str

    def __init__(self, max_batch_size: _Optional[int]=..., error_message: _Optional[str]=...) -> None:
        ...