from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import index_pb2 as _index_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FindNeighborsRequest(_message.Message):
    __slots__ = ('index_endpoint', 'deployed_index_id', 'queries', 'return_full_datapoint')

    class Query(_message.Message):
        __slots__ = ('rrf', 'datapoint', 'neighbor_count', 'per_crowding_attribute_neighbor_count', 'approximate_neighbor_count', 'fraction_leaf_nodes_to_search_override')

        class RRF(_message.Message):
            __slots__ = ('alpha',)
            ALPHA_FIELD_NUMBER: _ClassVar[int]
            alpha: float

            def __init__(self, alpha: _Optional[float]=...) -> None:
                ...
        RRF_FIELD_NUMBER: _ClassVar[int]
        DATAPOINT_FIELD_NUMBER: _ClassVar[int]
        NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
        PER_CROWDING_ATTRIBUTE_NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
        APPROXIMATE_NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRACTION_LEAF_NODES_TO_SEARCH_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        rrf: FindNeighborsRequest.Query.RRF
        datapoint: _index_pb2.IndexDatapoint
        neighbor_count: int
        per_crowding_attribute_neighbor_count: int
        approximate_neighbor_count: int
        fraction_leaf_nodes_to_search_override: float

        def __init__(self, rrf: _Optional[_Union[FindNeighborsRequest.Query.RRF, _Mapping]]=..., datapoint: _Optional[_Union[_index_pb2.IndexDatapoint, _Mapping]]=..., neighbor_count: _Optional[int]=..., per_crowding_attribute_neighbor_count: _Optional[int]=..., approximate_neighbor_count: _Optional[int]=..., fraction_leaf_nodes_to_search_override: _Optional[float]=...) -> None:
            ...
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    RETURN_FULL_DATAPOINT_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index_id: str
    queries: _containers.RepeatedCompositeFieldContainer[FindNeighborsRequest.Query]
    return_full_datapoint: bool

    def __init__(self, index_endpoint: _Optional[str]=..., deployed_index_id: _Optional[str]=..., queries: _Optional[_Iterable[_Union[FindNeighborsRequest.Query, _Mapping]]]=..., return_full_datapoint: bool=...) -> None:
        ...

class FindNeighborsResponse(_message.Message):
    __slots__ = ('nearest_neighbors',)

    class Neighbor(_message.Message):
        __slots__ = ('datapoint', 'distance', 'sparse_distance')
        DATAPOINT_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        SPARSE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        datapoint: _index_pb2.IndexDatapoint
        distance: float
        sparse_distance: float

        def __init__(self, datapoint: _Optional[_Union[_index_pb2.IndexDatapoint, _Mapping]]=..., distance: _Optional[float]=..., sparse_distance: _Optional[float]=...) -> None:
            ...

    class NearestNeighbors(_message.Message):
        __slots__ = ('id', 'neighbors')
        ID_FIELD_NUMBER: _ClassVar[int]
        NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
        id: str
        neighbors: _containers.RepeatedCompositeFieldContainer[FindNeighborsResponse.Neighbor]

        def __init__(self, id: _Optional[str]=..., neighbors: _Optional[_Iterable[_Union[FindNeighborsResponse.Neighbor, _Mapping]]]=...) -> None:
            ...
    NEAREST_NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    nearest_neighbors: _containers.RepeatedCompositeFieldContainer[FindNeighborsResponse.NearestNeighbors]

    def __init__(self, nearest_neighbors: _Optional[_Iterable[_Union[FindNeighborsResponse.NearestNeighbors, _Mapping]]]=...) -> None:
        ...

class ReadIndexDatapointsRequest(_message.Message):
    __slots__ = ('index_endpoint', 'deployed_index_id', 'ids')
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index_id: str
    ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, index_endpoint: _Optional[str]=..., deployed_index_id: _Optional[str]=..., ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class ReadIndexDatapointsResponse(_message.Message):
    __slots__ = ('datapoints',)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    datapoints: _containers.RepeatedCompositeFieldContainer[_index_pb2.IndexDatapoint]

    def __init__(self, datapoints: _Optional[_Iterable[_Union[_index_pb2.IndexDatapoint, _Mapping]]]=...) -> None:
        ...