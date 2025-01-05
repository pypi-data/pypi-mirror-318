from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VpcFlowLogsConfig(_message.Message):
    __slots__ = ("name", "description", "state", "aggregation_interval", "flow_sampling", "metadata", "metadata_fields", "filter_expr", "interconnect_attachment", "vpn_tunnel", "labels", "create_time", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VpcFlowLogsConfig.State]
        ENABLED: _ClassVar[VpcFlowLogsConfig.State]
        DISABLED: _ClassVar[VpcFlowLogsConfig.State]
    STATE_UNSPECIFIED: VpcFlowLogsConfig.State
    ENABLED: VpcFlowLogsConfig.State
    DISABLED: VpcFlowLogsConfig.State
    class AggregationInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATION_INTERVAL_UNSPECIFIED: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
        INTERVAL_5_SEC: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
        INTERVAL_30_SEC: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
        INTERVAL_1_MIN: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
        INTERVAL_5_MIN: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
        INTERVAL_10_MIN: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
        INTERVAL_15_MIN: _ClassVar[VpcFlowLogsConfig.AggregationInterval]
    AGGREGATION_INTERVAL_UNSPECIFIED: VpcFlowLogsConfig.AggregationInterval
    INTERVAL_5_SEC: VpcFlowLogsConfig.AggregationInterval
    INTERVAL_30_SEC: VpcFlowLogsConfig.AggregationInterval
    INTERVAL_1_MIN: VpcFlowLogsConfig.AggregationInterval
    INTERVAL_5_MIN: VpcFlowLogsConfig.AggregationInterval
    INTERVAL_10_MIN: VpcFlowLogsConfig.AggregationInterval
    INTERVAL_15_MIN: VpcFlowLogsConfig.AggregationInterval
    class Metadata(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METADATA_UNSPECIFIED: _ClassVar[VpcFlowLogsConfig.Metadata]
        INCLUDE_ALL_METADATA: _ClassVar[VpcFlowLogsConfig.Metadata]
        EXCLUDE_ALL_METADATA: _ClassVar[VpcFlowLogsConfig.Metadata]
        CUSTOM_METADATA: _ClassVar[VpcFlowLogsConfig.Metadata]
    METADATA_UNSPECIFIED: VpcFlowLogsConfig.Metadata
    INCLUDE_ALL_METADATA: VpcFlowLogsConfig.Metadata
    EXCLUDE_ALL_METADATA: VpcFlowLogsConfig.Metadata
    CUSTOM_METADATA: VpcFlowLogsConfig.Metadata
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    FLOW_SAMPLING_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPR_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    VPN_TUNNEL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: VpcFlowLogsConfig.State
    aggregation_interval: VpcFlowLogsConfig.AggregationInterval
    flow_sampling: float
    metadata: VpcFlowLogsConfig.Metadata
    metadata_fields: _containers.RepeatedScalarFieldContainer[str]
    filter_expr: str
    interconnect_attachment: str
    vpn_tunnel: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., state: _Optional[_Union[VpcFlowLogsConfig.State, str]] = ..., aggregation_interval: _Optional[_Union[VpcFlowLogsConfig.AggregationInterval, str]] = ..., flow_sampling: _Optional[float] = ..., metadata: _Optional[_Union[VpcFlowLogsConfig.Metadata, str]] = ..., metadata_fields: _Optional[_Iterable[str]] = ..., filter_expr: _Optional[str] = ..., interconnect_attachment: _Optional[str] = ..., vpn_tunnel: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
