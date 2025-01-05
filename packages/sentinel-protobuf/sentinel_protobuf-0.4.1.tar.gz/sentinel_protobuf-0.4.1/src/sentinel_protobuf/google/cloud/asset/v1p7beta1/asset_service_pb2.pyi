from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_UNSPECIFIED: _ClassVar[ContentType]
    RESOURCE: _ClassVar[ContentType]
    IAM_POLICY: _ClassVar[ContentType]
    ORG_POLICY: _ClassVar[ContentType]
    ACCESS_POLICY: _ClassVar[ContentType]
    RELATIONSHIP: _ClassVar[ContentType]
CONTENT_TYPE_UNSPECIFIED: ContentType
RESOURCE: ContentType
IAM_POLICY: ContentType
ORG_POLICY: ContentType
ACCESS_POLICY: ContentType
RELATIONSHIP: ContentType

class ExportAssetsRequest(_message.Message):
    __slots__ = ('parent', 'read_time', 'asset_types', 'content_type', 'output_config', 'relationship_types')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_time: _timestamp_pb2.Timestamp
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    output_config: OutputConfig
    relationship_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., asset_types: _Optional[_Iterable[str]]=..., content_type: _Optional[_Union[ContentType, str]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=..., relationship_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExportAssetsResponse(_message.Message):
    __slots__ = ('read_time', 'output_config', 'output_result')
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    read_time: _timestamp_pb2.Timestamp
    output_config: OutputConfig
    output_result: OutputResult

    def __init__(self, read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=..., output_result: _Optional[_Union[OutputResult, _Mapping]]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'bigquery_destination')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    bigquery_destination: BigQueryDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., bigquery_destination: _Optional[_Union[BigQueryDestination, _Mapping]]=...) -> None:
        ...

class OutputResult(_message.Message):
    __slots__ = ('gcs_result',)
    GCS_RESULT_FIELD_NUMBER: _ClassVar[int]
    gcs_result: GcsOutputResult

    def __init__(self, gcs_result: _Optional[_Union[GcsOutputResult, _Mapping]]=...) -> None:
        ...

class GcsOutputResult(_message.Message):
    __slots__ = ('uris',)
    URIS_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('uri', 'uri_prefix')
    URI_FIELD_NUMBER: _ClassVar[int]
    URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    uri: str
    uri_prefix: str

    def __init__(self, uri: _Optional[str]=..., uri_prefix: _Optional[str]=...) -> None:
        ...

class BigQueryDestination(_message.Message):
    __slots__ = ('dataset', 'table', 'force', 'partition_spec', 'separate_tables_per_asset_type')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SEPARATE_TABLES_PER_ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    table: str
    force: bool
    partition_spec: PartitionSpec
    separate_tables_per_asset_type: bool

    def __init__(self, dataset: _Optional[str]=..., table: _Optional[str]=..., force: bool=..., partition_spec: _Optional[_Union[PartitionSpec, _Mapping]]=..., separate_tables_per_asset_type: bool=...) -> None:
        ...

class PartitionSpec(_message.Message):
    __slots__ = ('partition_key',)

    class PartitionKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTITION_KEY_UNSPECIFIED: _ClassVar[PartitionSpec.PartitionKey]
        READ_TIME: _ClassVar[PartitionSpec.PartitionKey]
        REQUEST_TIME: _ClassVar[PartitionSpec.PartitionKey]
    PARTITION_KEY_UNSPECIFIED: PartitionSpec.PartitionKey
    READ_TIME: PartitionSpec.PartitionKey
    REQUEST_TIME: PartitionSpec.PartitionKey
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    partition_key: PartitionSpec.PartitionKey

    def __init__(self, partition_key: _Optional[_Union[PartitionSpec.PartitionKey, str]]=...) -> None:
        ...