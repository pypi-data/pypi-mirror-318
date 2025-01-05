from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1beta1 import data_stats_pb2 as _data_stats_pb2
from google.cloud.automl.v1beta1 import data_types_pb2 as _data_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ColumnSpec(_message.Message):
    __slots__ = ('name', 'data_type', 'display_name', 'data_stats', 'top_correlated_columns', 'etag')

    class CorrelatedColumn(_message.Message):
        __slots__ = ('column_spec_id', 'correlation_stats')
        COLUMN_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
        CORRELATION_STATS_FIELD_NUMBER: _ClassVar[int]
        column_spec_id: str
        correlation_stats: _data_stats_pb2.CorrelationStats

        def __init__(self, column_spec_id: _Optional[str]=..., correlation_stats: _Optional[_Union[_data_stats_pb2.CorrelationStats, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    TOP_CORRELATED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_type: _data_types_pb2.DataType
    display_name: str
    data_stats: _data_stats_pb2.DataStats
    top_correlated_columns: _containers.RepeatedCompositeFieldContainer[ColumnSpec.CorrelatedColumn]
    etag: str

    def __init__(self, name: _Optional[str]=..., data_type: _Optional[_Union[_data_types_pb2.DataType, _Mapping]]=..., display_name: _Optional[str]=..., data_stats: _Optional[_Union[_data_stats_pb2.DataStats, _Mapping]]=..., top_correlated_columns: _Optional[_Iterable[_Union[ColumnSpec.CorrelatedColumn, _Mapping]]]=..., etag: _Optional[str]=...) -> None:
        ...