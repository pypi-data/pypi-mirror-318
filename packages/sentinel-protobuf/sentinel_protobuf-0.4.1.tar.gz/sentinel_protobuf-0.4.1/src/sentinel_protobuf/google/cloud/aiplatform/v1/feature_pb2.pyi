from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import feature_monitoring_stats_pb2 as _feature_monitoring_stats_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Feature(_message.Message):
    __slots__ = ('name', 'description', 'value_type', 'create_time', 'update_time', 'labels', 'etag', 'disable_monitoring', 'monitoring_stats_anomalies', 'version_column_name', 'point_of_contact')

    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_TYPE_UNSPECIFIED: _ClassVar[Feature.ValueType]
        BOOL: _ClassVar[Feature.ValueType]
        BOOL_ARRAY: _ClassVar[Feature.ValueType]
        DOUBLE: _ClassVar[Feature.ValueType]
        DOUBLE_ARRAY: _ClassVar[Feature.ValueType]
        INT64: _ClassVar[Feature.ValueType]
        INT64_ARRAY: _ClassVar[Feature.ValueType]
        STRING: _ClassVar[Feature.ValueType]
        STRING_ARRAY: _ClassVar[Feature.ValueType]
        BYTES: _ClassVar[Feature.ValueType]
        STRUCT: _ClassVar[Feature.ValueType]
    VALUE_TYPE_UNSPECIFIED: Feature.ValueType
    BOOL: Feature.ValueType
    BOOL_ARRAY: Feature.ValueType
    DOUBLE: Feature.ValueType
    DOUBLE_ARRAY: Feature.ValueType
    INT64: Feature.ValueType
    INT64_ARRAY: Feature.ValueType
    STRING: Feature.ValueType
    STRING_ARRAY: Feature.ValueType
    BYTES: Feature.ValueType
    STRUCT: Feature.ValueType

    class MonitoringStatsAnomaly(_message.Message):
        __slots__ = ('objective', 'feature_stats_anomaly')

        class Objective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OBJECTIVE_UNSPECIFIED: _ClassVar[Feature.MonitoringStatsAnomaly.Objective]
            IMPORT_FEATURE_ANALYSIS: _ClassVar[Feature.MonitoringStatsAnomaly.Objective]
            SNAPSHOT_ANALYSIS: _ClassVar[Feature.MonitoringStatsAnomaly.Objective]
        OBJECTIVE_UNSPECIFIED: Feature.MonitoringStatsAnomaly.Objective
        IMPORT_FEATURE_ANALYSIS: Feature.MonitoringStatsAnomaly.Objective
        SNAPSHOT_ANALYSIS: Feature.MonitoringStatsAnomaly.Objective
        OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
        FEATURE_STATS_ANOMALY_FIELD_NUMBER: _ClassVar[int]
        objective: Feature.MonitoringStatsAnomaly.Objective
        feature_stats_anomaly: _feature_monitoring_stats_pb2.FeatureStatsAnomaly

        def __init__(self, objective: _Optional[_Union[Feature.MonitoringStatsAnomaly.Objective, str]]=..., feature_stats_anomaly: _Optional[_Union[_feature_monitoring_stats_pb2.FeatureStatsAnomaly, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MONITORING_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATS_ANOMALIES_FIELD_NUMBER: _ClassVar[int]
    VERSION_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_OF_CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    value_type: Feature.ValueType
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    etag: str
    disable_monitoring: bool
    monitoring_stats_anomalies: _containers.RepeatedCompositeFieldContainer[Feature.MonitoringStatsAnomaly]
    version_column_name: str
    point_of_contact: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., value_type: _Optional[_Union[Feature.ValueType, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., disable_monitoring: bool=..., monitoring_stats_anomalies: _Optional[_Iterable[_Union[Feature.MonitoringStatsAnomaly, _Mapping]]]=..., version_column_name: _Optional[str]=..., point_of_contact: _Optional[str]=...) -> None:
        ...