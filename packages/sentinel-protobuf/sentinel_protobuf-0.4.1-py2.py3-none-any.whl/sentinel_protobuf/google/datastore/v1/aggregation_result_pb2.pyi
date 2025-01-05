from google.datastore.v1 import entity_pb2 as _entity_pb2
from google.datastore.v1 import query_pb2 as _query_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AggregationResult(_message.Message):
    __slots__ = ('aggregate_properties',)

    class AggregatePropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _entity_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_entity_pb2.Value, _Mapping]]=...) -> None:
            ...
    AGGREGATE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    aggregate_properties: _containers.MessageMap[str, _entity_pb2.Value]

    def __init__(self, aggregate_properties: _Optional[_Mapping[str, _entity_pb2.Value]]=...) -> None:
        ...

class AggregationResultBatch(_message.Message):
    __slots__ = ('aggregation_results', 'more_results', 'read_time')
    AGGREGATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MORE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    aggregation_results: _containers.RepeatedCompositeFieldContainer[AggregationResult]
    more_results: _query_pb2.QueryResultBatch.MoreResultsType
    read_time: _timestamp_pb2.Timestamp

    def __init__(self, aggregation_results: _Optional[_Iterable[_Union[AggregationResult, _Mapping]]]=..., more_results: _Optional[_Union[_query_pb2.QueryResultBatch.MoreResultsType, str]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...