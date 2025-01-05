from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureView(_message.Message):
    __slots__ = ("big_query_source", "feature_registry_source", "vertex_rag_source", "name", "create_time", "update_time", "etag", "labels", "sync_config", "index_config", "satisfies_pzs", "satisfies_pzi")
    class BigQuerySource(_message.Message):
        __slots__ = ("uri", "entity_id_columns")
        URI_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_COLUMNS_FIELD_NUMBER: _ClassVar[int]
        uri: str
        entity_id_columns: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, uri: _Optional[str] = ..., entity_id_columns: _Optional[_Iterable[str]] = ...) -> None: ...
    class SyncConfig(_message.Message):
        __slots__ = ("cron", "continuous")
        CRON_FIELD_NUMBER: _ClassVar[int]
        CONTINUOUS_FIELD_NUMBER: _ClassVar[int]
        cron: str
        continuous: bool
        def __init__(self, cron: _Optional[str] = ..., continuous: bool = ...) -> None: ...
    class IndexConfig(_message.Message):
        __slots__ = ("tree_ah_config", "brute_force_config", "embedding_column", "filter_columns", "crowding_column", "embedding_dimension", "distance_measure_type")
        class DistanceMeasureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DISTANCE_MEASURE_TYPE_UNSPECIFIED: _ClassVar[FeatureView.IndexConfig.DistanceMeasureType]
            SQUARED_L2_DISTANCE: _ClassVar[FeatureView.IndexConfig.DistanceMeasureType]
            COSINE_DISTANCE: _ClassVar[FeatureView.IndexConfig.DistanceMeasureType]
            DOT_PRODUCT_DISTANCE: _ClassVar[FeatureView.IndexConfig.DistanceMeasureType]
        DISTANCE_MEASURE_TYPE_UNSPECIFIED: FeatureView.IndexConfig.DistanceMeasureType
        SQUARED_L2_DISTANCE: FeatureView.IndexConfig.DistanceMeasureType
        COSINE_DISTANCE: FeatureView.IndexConfig.DistanceMeasureType
        DOT_PRODUCT_DISTANCE: FeatureView.IndexConfig.DistanceMeasureType
        class BruteForceConfig(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TreeAHConfig(_message.Message):
            __slots__ = ("leaf_node_embedding_count",)
            LEAF_NODE_EMBEDDING_COUNT_FIELD_NUMBER: _ClassVar[int]
            leaf_node_embedding_count: int
            def __init__(self, leaf_node_embedding_count: _Optional[int] = ...) -> None: ...
        TREE_AH_CONFIG_FIELD_NUMBER: _ClassVar[int]
        BRUTE_FORCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        EMBEDDING_COLUMN_FIELD_NUMBER: _ClassVar[int]
        FILTER_COLUMNS_FIELD_NUMBER: _ClassVar[int]
        CROWDING_COLUMN_FIELD_NUMBER: _ClassVar[int]
        EMBEDDING_DIMENSION_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_MEASURE_TYPE_FIELD_NUMBER: _ClassVar[int]
        tree_ah_config: FeatureView.IndexConfig.TreeAHConfig
        brute_force_config: FeatureView.IndexConfig.BruteForceConfig
        embedding_column: str
        filter_columns: _containers.RepeatedScalarFieldContainer[str]
        crowding_column: str
        embedding_dimension: int
        distance_measure_type: FeatureView.IndexConfig.DistanceMeasureType
        def __init__(self, tree_ah_config: _Optional[_Union[FeatureView.IndexConfig.TreeAHConfig, _Mapping]] = ..., brute_force_config: _Optional[_Union[FeatureView.IndexConfig.BruteForceConfig, _Mapping]] = ..., embedding_column: _Optional[str] = ..., filter_columns: _Optional[_Iterable[str]] = ..., crowding_column: _Optional[str] = ..., embedding_dimension: _Optional[int] = ..., distance_measure_type: _Optional[_Union[FeatureView.IndexConfig.DistanceMeasureType, str]] = ...) -> None: ...
    class FeatureRegistrySource(_message.Message):
        __slots__ = ("feature_groups", "project_number")
        class FeatureGroup(_message.Message):
            __slots__ = ("feature_group_id", "feature_ids")
            FEATURE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            FEATURE_IDS_FIELD_NUMBER: _ClassVar[int]
            feature_group_id: str
            feature_ids: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, feature_group_id: _Optional[str] = ..., feature_ids: _Optional[_Iterable[str]] = ...) -> None: ...
        FEATURE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        feature_groups: _containers.RepeatedCompositeFieldContainer[FeatureView.FeatureRegistrySource.FeatureGroup]
        project_number: int
        def __init__(self, feature_groups: _Optional[_Iterable[_Union[FeatureView.FeatureRegistrySource.FeatureGroup, _Mapping]]] = ..., project_number: _Optional[int] = ...) -> None: ...
    class VertexRagSource(_message.Message):
        __slots__ = ("uri", "rag_corpus_id")
        URI_FIELD_NUMBER: _ClassVar[int]
        RAG_CORPUS_ID_FIELD_NUMBER: _ClassVar[int]
        uri: str
        rag_corpus_id: int
        def __init__(self, uri: _Optional[str] = ..., rag_corpus_id: _Optional[int] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BIG_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_REGISTRY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERTEX_RAG_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SYNC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    big_query_source: FeatureView.BigQuerySource
    feature_registry_source: FeatureView.FeatureRegistrySource
    vertex_rag_source: FeatureView.VertexRagSource
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]
    sync_config: FeatureView.SyncConfig
    index_config: FeatureView.IndexConfig
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, big_query_source: _Optional[_Union[FeatureView.BigQuerySource, _Mapping]] = ..., feature_registry_source: _Optional[_Union[FeatureView.FeatureRegistrySource, _Mapping]] = ..., vertex_rag_source: _Optional[_Union[FeatureView.VertexRagSource, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., sync_config: _Optional[_Union[FeatureView.SyncConfig, _Mapping]] = ..., index_config: _Optional[_Union[FeatureView.IndexConfig, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...
