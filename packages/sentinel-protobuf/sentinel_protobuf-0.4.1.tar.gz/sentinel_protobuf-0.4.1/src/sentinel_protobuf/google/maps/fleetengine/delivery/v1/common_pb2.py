"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/delivery/v1/common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ......google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/maps/fleetengine/delivery/v1/common.proto\x12\x1cmaps.fleetengine.delivery.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xa0\x01\n\x18DeliveryVehicleAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0cnumber_value\x18\x05 \x01(\x01H\x00B"\n delivery_vehicle_attribute_value"\xf4\x0c\n\x17DeliveryVehicleLocation\x12%\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12=\n\x13horizontal_accuracy\x18\x08 \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x02\x18\x01\x125\n\x0flatlng_accuracy\x18\x16 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12,\n\x07heading\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12:\n\x10bearing_accuracy\x18\n \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x02\x18\x01\x126\n\x10heading_accuracy\x18\x17 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12.\n\x08altitude\x18\x05 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12;\n\x11vertical_accuracy\x18\t \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x02\x18\x01\x127\n\x11altitude_accuracy\x18\x18 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x123\n\nspeed_kmph\x18\x03 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x02\x18\x01\x12+\n\x05speed\x18\x06 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x124\n\x0espeed_accuracy\x18\x07 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x0bserver_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12T\n\x0flocation_sensor\x18\x0b \x01(\x0e2;.maps.fleetengine.delivery.v1.DeliveryVehicleLocationSensor\x123\n\x0fis_road_snapped\x18\x1b \x01(\x0b2\x1a.google.protobuf.BoolValue\x12>\n\x15is_gps_sensor_enabled\x18\x0c \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x04\x12;\n\x11time_since_update\x18\x0e \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x04\x12=\n\x11num_stale_updates\x18\x0f \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x05\x18\x01\xe0A\x04\x12)\n\x0craw_location\x18\x10 \x01(\x0b2\x13.google.type.LatLng\x125\n\x11raw_location_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12X\n\x13raw_location_sensor\x18\x1c \x01(\x0e2;.maps.fleetengine.delivery.v1.DeliveryVehicleLocationSensor\x12;\n\x15raw_location_accuracy\x18\x19 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x122\n\x15supplemental_location\x18\x12 \x01(\x0b2\x13.google.type.LatLng\x12>\n\x1asupplemental_location_time\x18\x13 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12a\n\x1csupplemental_location_sensor\x18\x14 \x01(\x0e2;.maps.fleetengine.delivery.v1.DeliveryVehicleLocationSensor\x12D\n\x1esupplemental_location_accuracy\x18\x15 \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12\x18\n\x0croad_snapped\x18\x1a \x01(\x08B\x02\x18\x01"t\n\nTimeWindow\x123\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"z\n\rTaskAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0cnumber_value\x18\x04 \x01(\x01H\x00B\x16\n\x14task_attribute_value*\xe6\x01\n\x1dDeliveryVehicleLocationSensor\x12\x12\n\x0eUNKNOWN_SENSOR\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\x0b\n\x07NETWORK\x10\x02\x12\x0b\n\x07PASSIVE\x10\x03\x12"\n\x1eROAD_SNAPPED_LOCATION_PROVIDER\x10\x04\x12\x1e\n\x1aCUSTOMER_SUPPLIED_LOCATION\x10\x05\x12\x19\n\x15FLEET_ENGINE_LOCATION\x10\x06\x12\x1b\n\x17FUSED_LOCATION_PROVIDER\x10d\x12\x12\n\rCORE_LOCATION\x10\xc8\x01*\x98\x01\n\x1fDeliveryVehicleNavigationStatus\x12\x1d\n\x19UNKNOWN_NAVIGATION_STATUS\x10\x00\x12\x0f\n\x0bNO_GUIDANCE\x10\x01\x12\x1a\n\x16ENROUTE_TO_DESTINATION\x10\x02\x12\r\n\tOFF_ROUTE\x10\x03\x12\x1a\n\x16ARRIVED_AT_DESTINATION\x10\x04B\xfb\x01\n\'com.google.maps.fleetengine.delivery.v1B\x06CommonP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02\'Google::Maps::FleetEngine::Delivery::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.delivery.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.fleetengine.delivery.v1B\x06CommonP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02'Google::Maps::FleetEngine::Delivery::V1"
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['horizontal_accuracy']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['horizontal_accuracy']._serialized_options = b'\x18\x01'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['bearing_accuracy']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['bearing_accuracy']._serialized_options = b'\x18\x01'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['vertical_accuracy']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['vertical_accuracy']._serialized_options = b'\x18\x01'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['speed_kmph']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['speed_kmph']._serialized_options = b'\x18\x01'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['server_time']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['server_time']._serialized_options = b'\xe0A\x03'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['is_gps_sensor_enabled']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['is_gps_sensor_enabled']._serialized_options = b'\xe0A\x04'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['time_since_update']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['time_since_update']._serialized_options = b'\xe0A\x04'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['num_stale_updates']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['num_stale_updates']._serialized_options = b'\x18\x01\xe0A\x04'
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['road_snapped']._loaded_options = None
    _globals['_DELIVERYVEHICLELOCATION'].fields_by_name['road_snapped']._serialized_options = b'\x18\x01'
    _globals['_TIMEWINDOW'].fields_by_name['start_time']._loaded_options = None
    _globals['_TIMEWINDOW'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_TIMEWINDOW'].fields_by_name['end_time']._loaded_options = None
    _globals['_TIMEWINDOW'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_DELIVERYVEHICLELOCATIONSENSOR']._serialized_start = 2267
    _globals['_DELIVERYVEHICLELOCATIONSENSOR']._serialized_end = 2497
    _globals['_DELIVERYVEHICLENAVIGATIONSTATUS']._serialized_start = 2500
    _globals['_DELIVERYVEHICLENAVIGATIONSTATUS']._serialized_end = 2652
    _globals['_DELIVERYVEHICLEATTRIBUTE']._serialized_start = 207
    _globals['_DELIVERYVEHICLEATTRIBUTE']._serialized_end = 367
    _globals['_DELIVERYVEHICLELOCATION']._serialized_start = 370
    _globals['_DELIVERYVEHICLELOCATION']._serialized_end = 2022
    _globals['_TIMEWINDOW']._serialized_start = 2024
    _globals['_TIMEWINDOW']._serialized_end = 2140
    _globals['_TASKATTRIBUTE']._serialized_start = 2142
    _globals['_TASKATTRIBUTE']._serialized_end = 2264