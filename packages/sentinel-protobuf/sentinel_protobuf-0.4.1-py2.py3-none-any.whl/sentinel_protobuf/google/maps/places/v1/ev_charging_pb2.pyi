from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EVConnectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EV_CONNECTOR_TYPE_UNSPECIFIED: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_OTHER: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_J1772: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_TYPE_2: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_CHADEMO: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_CCS_COMBO_1: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_CCS_COMBO_2: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_TESLA: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T: _ClassVar[EVConnectorType]
    EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET: _ClassVar[EVConnectorType]
EV_CONNECTOR_TYPE_UNSPECIFIED: EVConnectorType
EV_CONNECTOR_TYPE_OTHER: EVConnectorType
EV_CONNECTOR_TYPE_J1772: EVConnectorType
EV_CONNECTOR_TYPE_TYPE_2: EVConnectorType
EV_CONNECTOR_TYPE_CHADEMO: EVConnectorType
EV_CONNECTOR_TYPE_CCS_COMBO_1: EVConnectorType
EV_CONNECTOR_TYPE_CCS_COMBO_2: EVConnectorType
EV_CONNECTOR_TYPE_TESLA: EVConnectorType
EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T: EVConnectorType
EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET: EVConnectorType

class EVChargeOptions(_message.Message):
    __slots__ = ("connector_count", "connector_aggregation")
    class ConnectorAggregation(_message.Message):
        __slots__ = ("type", "max_charge_rate_kw", "count", "available_count", "out_of_service_count", "availability_last_update_time")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        MAX_CHARGE_RATE_KW_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_SERVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        type: EVConnectorType
        max_charge_rate_kw: float
        count: int
        available_count: int
        out_of_service_count: int
        availability_last_update_time: _timestamp_pb2.Timestamp
        def __init__(self, type: _Optional[_Union[EVConnectorType, str]] = ..., max_charge_rate_kw: _Optional[float] = ..., count: _Optional[int] = ..., available_count: _Optional[int] = ..., out_of_service_count: _Optional[int] = ..., availability_last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    CONNECTOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    connector_count: int
    connector_aggregation: _containers.RepeatedCompositeFieldContainer[EVChargeOptions.ConnectorAggregation]
    def __init__(self, connector_count: _Optional[int] = ..., connector_aggregation: _Optional[_Iterable[_Union[EVChargeOptions.ConnectorAggregation, _Mapping]]] = ...) -> None: ...
