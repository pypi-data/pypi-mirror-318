from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureGroup(_message.Message):
    __slots__ = ('big_query', 'name', 'create_time', 'update_time', 'etag', 'labels', 'description', 'service_agent_type', 'service_account_email')

    class ServiceAgentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_AGENT_TYPE_UNSPECIFIED: _ClassVar[FeatureGroup.ServiceAgentType]
        SERVICE_AGENT_TYPE_PROJECT: _ClassVar[FeatureGroup.ServiceAgentType]
        SERVICE_AGENT_TYPE_FEATURE_GROUP: _ClassVar[FeatureGroup.ServiceAgentType]
    SERVICE_AGENT_TYPE_UNSPECIFIED: FeatureGroup.ServiceAgentType
    SERVICE_AGENT_TYPE_PROJECT: FeatureGroup.ServiceAgentType
    SERVICE_AGENT_TYPE_FEATURE_GROUP: FeatureGroup.ServiceAgentType

    class BigQuery(_message.Message):
        __slots__ = ('big_query_source', 'entity_id_columns', 'static_data_source', 'time_series', 'dense')

        class TimeSeries(_message.Message):
            __slots__ = ('timestamp_column',)
            TIMESTAMP_COLUMN_FIELD_NUMBER: _ClassVar[int]
            timestamp_column: str

            def __init__(self, timestamp_column: _Optional[str]=...) -> None:
                ...
        BIG_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_COLUMNS_FIELD_NUMBER: _ClassVar[int]
        STATIC_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
        TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
        DENSE_FIELD_NUMBER: _ClassVar[int]
        big_query_source: _io_pb2.BigQuerySource
        entity_id_columns: _containers.RepeatedScalarFieldContainer[str]
        static_data_source: bool
        time_series: FeatureGroup.BigQuery.TimeSeries
        dense: bool

        def __init__(self, big_query_source: _Optional[_Union[_io_pb2.BigQuerySource, _Mapping]]=..., entity_id_columns: _Optional[_Iterable[str]]=..., static_data_source: bool=..., time_series: _Optional[_Union[FeatureGroup.BigQuery.TimeSeries, _Mapping]]=..., dense: bool=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BIG_QUERY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    big_query: FeatureGroup.BigQuery
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]
    description: str
    service_agent_type: FeatureGroup.ServiceAgentType
    service_account_email: str

    def __init__(self, big_query: _Optional[_Union[FeatureGroup.BigQuery, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., service_agent_type: _Optional[_Union[FeatureGroup.ServiceAgentType, str]]=..., service_account_email: _Optional[str]=...) -> None:
        ...