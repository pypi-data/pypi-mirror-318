from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryVehicleLocationSensor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SENSOR: _ClassVar[DeliveryVehicleLocationSensor]
    GPS: _ClassVar[DeliveryVehicleLocationSensor]
    NETWORK: _ClassVar[DeliveryVehicleLocationSensor]
    PASSIVE: _ClassVar[DeliveryVehicleLocationSensor]
    ROAD_SNAPPED_LOCATION_PROVIDER: _ClassVar[DeliveryVehicleLocationSensor]
    CUSTOMER_SUPPLIED_LOCATION: _ClassVar[DeliveryVehicleLocationSensor]
    FLEET_ENGINE_LOCATION: _ClassVar[DeliveryVehicleLocationSensor]
    FUSED_LOCATION_PROVIDER: _ClassVar[DeliveryVehicleLocationSensor]
    CORE_LOCATION: _ClassVar[DeliveryVehicleLocationSensor]

class DeliveryVehicleNavigationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_NAVIGATION_STATUS: _ClassVar[DeliveryVehicleNavigationStatus]
    NO_GUIDANCE: _ClassVar[DeliveryVehicleNavigationStatus]
    ENROUTE_TO_DESTINATION: _ClassVar[DeliveryVehicleNavigationStatus]
    OFF_ROUTE: _ClassVar[DeliveryVehicleNavigationStatus]
    ARRIVED_AT_DESTINATION: _ClassVar[DeliveryVehicleNavigationStatus]
UNKNOWN_SENSOR: DeliveryVehicleLocationSensor
GPS: DeliveryVehicleLocationSensor
NETWORK: DeliveryVehicleLocationSensor
PASSIVE: DeliveryVehicleLocationSensor
ROAD_SNAPPED_LOCATION_PROVIDER: DeliveryVehicleLocationSensor
CUSTOMER_SUPPLIED_LOCATION: DeliveryVehicleLocationSensor
FLEET_ENGINE_LOCATION: DeliveryVehicleLocationSensor
FUSED_LOCATION_PROVIDER: DeliveryVehicleLocationSensor
CORE_LOCATION: DeliveryVehicleLocationSensor
UNKNOWN_NAVIGATION_STATUS: DeliveryVehicleNavigationStatus
NO_GUIDANCE: DeliveryVehicleNavigationStatus
ENROUTE_TO_DESTINATION: DeliveryVehicleNavigationStatus
OFF_ROUTE: DeliveryVehicleNavigationStatus
ARRIVED_AT_DESTINATION: DeliveryVehicleNavigationStatus

class DeliveryVehicleAttribute(_message.Message):
    __slots__ = ('key', 'value', 'string_value', 'bool_value', 'number_value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    string_value: str
    bool_value: bool
    number_value: float

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=..., string_value: _Optional[str]=..., bool_value: bool=..., number_value: _Optional[float]=...) -> None:
        ...

class DeliveryVehicleLocation(_message.Message):
    __slots__ = ('location', 'horizontal_accuracy', 'latlng_accuracy', 'heading', 'bearing_accuracy', 'heading_accuracy', 'altitude', 'vertical_accuracy', 'altitude_accuracy', 'speed_kmph', 'speed', 'speed_accuracy', 'update_time', 'server_time', 'location_sensor', 'is_road_snapped', 'is_gps_sensor_enabled', 'time_since_update', 'num_stale_updates', 'raw_location', 'raw_location_time', 'raw_location_sensor', 'raw_location_accuracy', 'supplemental_location', 'supplemental_location_time', 'supplemental_location_sensor', 'supplemental_location_accuracy', 'road_snapped')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    LATLNG_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    BEARING_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    HEADING_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    SPEED_KMPH_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    SPEED_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    IS_ROAD_SNAPPED_FIELD_NUMBER: _ClassVar[int]
    IS_GPS_SENSOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIME_SINCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    NUM_STALE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_TIME_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    RAW_LOCATION_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_LOCATION_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ROAD_SNAPPED_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    horizontal_accuracy: _wrappers_pb2.DoubleValue
    latlng_accuracy: _wrappers_pb2.DoubleValue
    heading: _wrappers_pb2.Int32Value
    bearing_accuracy: _wrappers_pb2.DoubleValue
    heading_accuracy: _wrappers_pb2.DoubleValue
    altitude: _wrappers_pb2.DoubleValue
    vertical_accuracy: _wrappers_pb2.DoubleValue
    altitude_accuracy: _wrappers_pb2.DoubleValue
    speed_kmph: _wrappers_pb2.Int32Value
    speed: _wrappers_pb2.DoubleValue
    speed_accuracy: _wrappers_pb2.DoubleValue
    update_time: _timestamp_pb2.Timestamp
    server_time: _timestamp_pb2.Timestamp
    location_sensor: DeliveryVehicleLocationSensor
    is_road_snapped: _wrappers_pb2.BoolValue
    is_gps_sensor_enabled: _wrappers_pb2.BoolValue
    time_since_update: _wrappers_pb2.Int32Value
    num_stale_updates: _wrappers_pb2.Int32Value
    raw_location: _latlng_pb2.LatLng
    raw_location_time: _timestamp_pb2.Timestamp
    raw_location_sensor: DeliveryVehicleLocationSensor
    raw_location_accuracy: _wrappers_pb2.DoubleValue
    supplemental_location: _latlng_pb2.LatLng
    supplemental_location_time: _timestamp_pb2.Timestamp
    supplemental_location_sensor: DeliveryVehicleLocationSensor
    supplemental_location_accuracy: _wrappers_pb2.DoubleValue
    road_snapped: bool

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., horizontal_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., latlng_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., heading: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., bearing_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., heading_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., altitude: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., vertical_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., altitude_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., speed_kmph: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., speed: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., speed_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., server_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., location_sensor: _Optional[_Union[DeliveryVehicleLocationSensor, str]]=..., is_road_snapped: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., is_gps_sensor_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., time_since_update: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., num_stale_updates: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., raw_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., raw_location_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., raw_location_sensor: _Optional[_Union[DeliveryVehicleLocationSensor, str]]=..., raw_location_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., supplemental_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., supplemental_location_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., supplemental_location_sensor: _Optional[_Union[DeliveryVehicleLocationSensor, str]]=..., supplemental_location_accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]]=..., road_snapped: bool=...) -> None:
        ...

class TimeWindow(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TaskAttribute(_message.Message):
    __slots__ = ('key', 'string_value', 'bool_value', 'number_value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    string_value: str
    bool_value: bool
    number_value: float

    def __init__(self, key: _Optional[str]=..., string_value: _Optional[str]=..., bool_value: bool=..., number_value: _Optional[float]=...) -> None:
        ...