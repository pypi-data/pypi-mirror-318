from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import featurestore_online_service_pb2 as _featurestore_online_service_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureViewDataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED: _ClassVar[FeatureViewDataFormat]
    KEY_VALUE: _ClassVar[FeatureViewDataFormat]
    PROTO_STRUCT: _ClassVar[FeatureViewDataFormat]
FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED: FeatureViewDataFormat
KEY_VALUE: FeatureViewDataFormat
PROTO_STRUCT: FeatureViewDataFormat

class FeatureViewDataKey(_message.Message):
    __slots__ = ("key", "composite_key")
    class CompositeKey(_message.Message):
        __slots__ = ("parts",)
        PARTS_FIELD_NUMBER: _ClassVar[int]
        parts: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, parts: _Optional[_Iterable[str]] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    COMPOSITE_KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    composite_key: FeatureViewDataKey.CompositeKey
    def __init__(self, key: _Optional[str] = ..., composite_key: _Optional[_Union[FeatureViewDataKey.CompositeKey, _Mapping]] = ...) -> None: ...

class FetchFeatureValuesRequest(_message.Message):
    __slots__ = ("id", "feature_view", "data_key", "data_format", "format")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[FetchFeatureValuesRequest.Format]
        KEY_VALUE: _ClassVar[FetchFeatureValuesRequest.Format]
        PROTO_STRUCT: _ClassVar[FetchFeatureValuesRequest.Format]
    FORMAT_UNSPECIFIED: FetchFeatureValuesRequest.Format
    KEY_VALUE: FetchFeatureValuesRequest.Format
    PROTO_STRUCT: FetchFeatureValuesRequest.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    DATA_KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    feature_view: str
    data_key: FeatureViewDataKey
    data_format: FeatureViewDataFormat
    format: FetchFeatureValuesRequest.Format
    def __init__(self, id: _Optional[str] = ..., feature_view: _Optional[str] = ..., data_key: _Optional[_Union[FeatureViewDataKey, _Mapping]] = ..., data_format: _Optional[_Union[FeatureViewDataFormat, str]] = ..., format: _Optional[_Union[FetchFeatureValuesRequest.Format, str]] = ...) -> None: ...

class FetchFeatureValuesResponse(_message.Message):
    __slots__ = ("key_values", "proto_struct", "data_key")
    class FeatureNameValuePairList(_message.Message):
        __slots__ = ("features",)
        class FeatureNameValuePair(_message.Message):
            __slots__ = ("value", "name")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            value: _featurestore_online_service_pb2.FeatureValue
            name: str
            def __init__(self, value: _Optional[_Union[_featurestore_online_service_pb2.FeatureValue, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        features: _containers.RepeatedCompositeFieldContainer[FetchFeatureValuesResponse.FeatureNameValuePairList.FeatureNameValuePair]
        def __init__(self, features: _Optional[_Iterable[_Union[FetchFeatureValuesResponse.FeatureNameValuePairList.FeatureNameValuePair, _Mapping]]] = ...) -> None: ...
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    PROTO_STRUCT_FIELD_NUMBER: _ClassVar[int]
    DATA_KEY_FIELD_NUMBER: _ClassVar[int]
    key_values: FetchFeatureValuesResponse.FeatureNameValuePairList
    proto_struct: _struct_pb2.Struct
    data_key: FeatureViewDataKey
    def __init__(self, key_values: _Optional[_Union[FetchFeatureValuesResponse.FeatureNameValuePairList, _Mapping]] = ..., proto_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., data_key: _Optional[_Union[FeatureViewDataKey, _Mapping]] = ...) -> None: ...

class StreamingFetchFeatureValuesRequest(_message.Message):
    __slots__ = ("feature_view", "data_keys", "data_format")
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    DATA_KEYS_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    feature_view: str
    data_keys: _containers.RepeatedCompositeFieldContainer[FeatureViewDataKey]
    data_format: FeatureViewDataFormat
    def __init__(self, feature_view: _Optional[str] = ..., data_keys: _Optional[_Iterable[_Union[FeatureViewDataKey, _Mapping]]] = ..., data_format: _Optional[_Union[FeatureViewDataFormat, str]] = ...) -> None: ...

class StreamingFetchFeatureValuesResponse(_message.Message):
    __slots__ = ("status", "data", "data_keys_with_error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_KEYS_WITH_ERROR_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    data: _containers.RepeatedCompositeFieldContainer[FetchFeatureValuesResponse]
    data_keys_with_error: _containers.RepeatedCompositeFieldContainer[FeatureViewDataKey]
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., data: _Optional[_Iterable[_Union[FetchFeatureValuesResponse, _Mapping]]] = ..., data_keys_with_error: _Optional[_Iterable[_Union[FeatureViewDataKey, _Mapping]]] = ...) -> None: ...

class NearestNeighborQuery(_message.Message):
    __slots__ = ("entity_id", "embedding", "neighbor_count", "string_filters", "numeric_filters", "per_crowding_attribute_neighbor_count", "parameters")
    class Embedding(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...
    class StringFilter(_message.Message):
        __slots__ = ("name", "allow_tokens", "deny_tokens")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ALLOW_TOKENS_FIELD_NUMBER: _ClassVar[int]
        DENY_TOKENS_FIELD_NUMBER: _ClassVar[int]
        name: str
        allow_tokens: _containers.RepeatedScalarFieldContainer[str]
        deny_tokens: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., allow_tokens: _Optional[_Iterable[str]] = ..., deny_tokens: _Optional[_Iterable[str]] = ...) -> None: ...
    class NumericFilter(_message.Message):
        __slots__ = ("value_int", "value_float", "value_double", "name", "op")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATOR_UNSPECIFIED: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
            LESS: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
            LESS_EQUAL: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
            EQUAL: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
            GREATER_EQUAL: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
            GREATER: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
            NOT_EQUAL: _ClassVar[NearestNeighborQuery.NumericFilter.Operator]
        OPERATOR_UNSPECIFIED: NearestNeighborQuery.NumericFilter.Operator
        LESS: NearestNeighborQuery.NumericFilter.Operator
        LESS_EQUAL: NearestNeighborQuery.NumericFilter.Operator
        EQUAL: NearestNeighborQuery.NumericFilter.Operator
        GREATER_EQUAL: NearestNeighborQuery.NumericFilter.Operator
        GREATER: NearestNeighborQuery.NumericFilter.Operator
        NOT_EQUAL: NearestNeighborQuery.NumericFilter.Operator
        VALUE_INT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FLOAT_FIELD_NUMBER: _ClassVar[int]
        VALUE_DOUBLE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OP_FIELD_NUMBER: _ClassVar[int]
        value_int: int
        value_float: float
        value_double: float
        name: str
        op: NearestNeighborQuery.NumericFilter.Operator
        def __init__(self, value_int: _Optional[int] = ..., value_float: _Optional[float] = ..., value_double: _Optional[float] = ..., name: _Optional[str] = ..., op: _Optional[_Union[NearestNeighborQuery.NumericFilter.Operator, str]] = ...) -> None: ...
    class Parameters(_message.Message):
        __slots__ = ("approximate_neighbor_candidates", "leaf_nodes_search_fraction")
        APPROXIMATE_NEIGHBOR_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        LEAF_NODES_SEARCH_FRACTION_FIELD_NUMBER: _ClassVar[int]
        approximate_neighbor_candidates: int
        leaf_nodes_search_fraction: float
        def __init__(self, approximate_neighbor_candidates: _Optional[int] = ..., leaf_nodes_search_fraction: _Optional[float] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTERS_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PER_CROWDING_ATTRIBUTE_NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    embedding: NearestNeighborQuery.Embedding
    neighbor_count: int
    string_filters: _containers.RepeatedCompositeFieldContainer[NearestNeighborQuery.StringFilter]
    numeric_filters: _containers.RepeatedCompositeFieldContainer[NearestNeighborQuery.NumericFilter]
    per_crowding_attribute_neighbor_count: int
    parameters: NearestNeighborQuery.Parameters
    def __init__(self, entity_id: _Optional[str] = ..., embedding: _Optional[_Union[NearestNeighborQuery.Embedding, _Mapping]] = ..., neighbor_count: _Optional[int] = ..., string_filters: _Optional[_Iterable[_Union[NearestNeighborQuery.StringFilter, _Mapping]]] = ..., numeric_filters: _Optional[_Iterable[_Union[NearestNeighborQuery.NumericFilter, _Mapping]]] = ..., per_crowding_attribute_neighbor_count: _Optional[int] = ..., parameters: _Optional[_Union[NearestNeighborQuery.Parameters, _Mapping]] = ...) -> None: ...

class SearchNearestEntitiesRequest(_message.Message):
    __slots__ = ("feature_view", "query", "return_full_entity")
    FEATURE_VIEW_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RETURN_FULL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    feature_view: str
    query: NearestNeighborQuery
    return_full_entity: bool
    def __init__(self, feature_view: _Optional[str] = ..., query: _Optional[_Union[NearestNeighborQuery, _Mapping]] = ..., return_full_entity: bool = ...) -> None: ...

class NearestNeighbors(_message.Message):
    __slots__ = ("neighbors",)
    class Neighbor(_message.Message):
        __slots__ = ("entity_id", "distance", "entity_key_values")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        entity_id: str
        distance: float
        entity_key_values: FetchFeatureValuesResponse
        def __init__(self, entity_id: _Optional[str] = ..., distance: _Optional[float] = ..., entity_key_values: _Optional[_Union[FetchFeatureValuesResponse, _Mapping]] = ...) -> None: ...
    NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    neighbors: _containers.RepeatedCompositeFieldContainer[NearestNeighbors.Neighbor]
    def __init__(self, neighbors: _Optional[_Iterable[_Union[NearestNeighbors.Neighbor, _Mapping]]] = ...) -> None: ...

class SearchNearestEntitiesResponse(_message.Message):
    __slots__ = ("nearest_neighbors",)
    NEAREST_NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    nearest_neighbors: NearestNeighbors
    def __init__(self, nearest_neighbors: _Optional[_Union[NearestNeighbors, _Mapping]] = ...) -> None: ...
