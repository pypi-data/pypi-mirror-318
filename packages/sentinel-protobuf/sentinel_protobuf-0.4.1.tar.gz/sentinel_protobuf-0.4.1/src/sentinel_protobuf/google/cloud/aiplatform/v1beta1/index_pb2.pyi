from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import deployed_index_ref_pb2 as _deployed_index_ref_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Index(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'metadata_schema_uri', 'metadata', 'deployed_indexes', 'etag', 'labels', 'create_time', 'update_time', 'index_stats', 'index_update_method', 'encryption_spec', 'satisfies_pzs', 'satisfies_pzi')

    class IndexUpdateMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX_UPDATE_METHOD_UNSPECIFIED: _ClassVar[Index.IndexUpdateMethod]
        BATCH_UPDATE: _ClassVar[Index.IndexUpdateMethod]
        STREAM_UPDATE: _ClassVar[Index.IndexUpdateMethod]
    INDEX_UPDATE_METHOD_UNSPECIFIED: Index.IndexUpdateMethod
    BATCH_UPDATE: Index.IndexUpdateMethod
    STREAM_UPDATE: Index.IndexUpdateMethod

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEXES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_STATS_FIELD_NUMBER: _ClassVar[int]
    INDEX_UPDATE_METHOD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    metadata_schema_uri: str
    metadata: _struct_pb2.Value
    deployed_indexes: _containers.RepeatedCompositeFieldContainer[_deployed_index_ref_pb2.DeployedIndexRef]
    etag: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    index_stats: IndexStats
    index_update_method: Index.IndexUpdateMethod
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., metadata_schema_uri: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., deployed_indexes: _Optional[_Iterable[_Union[_deployed_index_ref_pb2.DeployedIndexRef, _Mapping]]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., index_stats: _Optional[_Union[IndexStats, _Mapping]]=..., index_update_method: _Optional[_Union[Index.IndexUpdateMethod, str]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class IndexDatapoint(_message.Message):
    __slots__ = ('datapoint_id', 'feature_vector', 'sparse_embedding', 'restricts', 'numeric_restricts', 'crowding_tag')

    class SparseEmbedding(_message.Message):
        __slots__ = ('values', 'dimensions')
        VALUES_FIELD_NUMBER: _ClassVar[int]
        DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[float]
        dimensions: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, values: _Optional[_Iterable[float]]=..., dimensions: _Optional[_Iterable[int]]=...) -> None:
            ...

    class Restriction(_message.Message):
        __slots__ = ('namespace', 'allow_list', 'deny_list')
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_LIST_FIELD_NUMBER: _ClassVar[int]
        DENY_LIST_FIELD_NUMBER: _ClassVar[int]
        namespace: str
        allow_list: _containers.RepeatedScalarFieldContainer[str]
        deny_list: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, namespace: _Optional[str]=..., allow_list: _Optional[_Iterable[str]]=..., deny_list: _Optional[_Iterable[str]]=...) -> None:
            ...

    class NumericRestriction(_message.Message):
        __slots__ = ('value_int', 'value_float', 'value_double', 'namespace', 'op')

        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATOR_UNSPECIFIED: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
            LESS: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
            LESS_EQUAL: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
            EQUAL: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
            GREATER_EQUAL: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
            GREATER: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
            NOT_EQUAL: _ClassVar[IndexDatapoint.NumericRestriction.Operator]
        OPERATOR_UNSPECIFIED: IndexDatapoint.NumericRestriction.Operator
        LESS: IndexDatapoint.NumericRestriction.Operator
        LESS_EQUAL: IndexDatapoint.NumericRestriction.Operator
        EQUAL: IndexDatapoint.NumericRestriction.Operator
        GREATER_EQUAL: IndexDatapoint.NumericRestriction.Operator
        GREATER: IndexDatapoint.NumericRestriction.Operator
        NOT_EQUAL: IndexDatapoint.NumericRestriction.Operator
        VALUE_INT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FLOAT_FIELD_NUMBER: _ClassVar[int]
        VALUE_DOUBLE_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        OP_FIELD_NUMBER: _ClassVar[int]
        value_int: int
        value_float: float
        value_double: float
        namespace: str
        op: IndexDatapoint.NumericRestriction.Operator

        def __init__(self, value_int: _Optional[int]=..., value_float: _Optional[float]=..., value_double: _Optional[float]=..., namespace: _Optional[str]=..., op: _Optional[_Union[IndexDatapoint.NumericRestriction.Operator, str]]=...) -> None:
            ...

    class CrowdingTag(_message.Message):
        __slots__ = ('crowding_attribute',)
        CROWDING_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        crowding_attribute: str

        def __init__(self, crowding_attribute: _Optional[str]=...) -> None:
            ...
    DATAPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VECTOR_FIELD_NUMBER: _ClassVar[int]
    SPARSE_EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    RESTRICTS_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_RESTRICTS_FIELD_NUMBER: _ClassVar[int]
    CROWDING_TAG_FIELD_NUMBER: _ClassVar[int]
    datapoint_id: str
    feature_vector: _containers.RepeatedScalarFieldContainer[float]
    sparse_embedding: IndexDatapoint.SparseEmbedding
    restricts: _containers.RepeatedCompositeFieldContainer[IndexDatapoint.Restriction]
    numeric_restricts: _containers.RepeatedCompositeFieldContainer[IndexDatapoint.NumericRestriction]
    crowding_tag: IndexDatapoint.CrowdingTag

    def __init__(self, datapoint_id: _Optional[str]=..., feature_vector: _Optional[_Iterable[float]]=..., sparse_embedding: _Optional[_Union[IndexDatapoint.SparseEmbedding, _Mapping]]=..., restricts: _Optional[_Iterable[_Union[IndexDatapoint.Restriction, _Mapping]]]=..., numeric_restricts: _Optional[_Iterable[_Union[IndexDatapoint.NumericRestriction, _Mapping]]]=..., crowding_tag: _Optional[_Union[IndexDatapoint.CrowdingTag, _Mapping]]=...) -> None:
        ...

class IndexStats(_message.Message):
    __slots__ = ('vectors_count', 'sparse_vectors_count', 'shards_count')
    VECTORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VECTORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARDS_COUNT_FIELD_NUMBER: _ClassVar[int]
    vectors_count: int
    sparse_vectors_count: int
    shards_count: int

    def __init__(self, vectors_count: _Optional[int]=..., sparse_vectors_count: _Optional[int]=..., shards_count: _Optional[int]=...) -> None:
        ...