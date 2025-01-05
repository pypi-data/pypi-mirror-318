"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/delivery/v1/delivery_vehicles.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.maps.fleetengine.delivery.v1 import common_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ......google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/maps/fleetengine/delivery/v1/delivery_vehicles.proto\x12\x1cmaps.fleetengine.delivery.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/maps/fleetengine/delivery/v1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xf1\x06\n\x0fDeliveryVehicle\x12\x0c\n\x04name\x18\x01 \x01(\t\x12L\n\rlast_location\x18\x02 \x01(\x0b25.maps.fleetengine.delivery.v1.DeliveryVehicleLocation\x12X\n\x11navigation_status\x18\x03 \x01(\x0e2=.maps.fleetengine.delivery.v1.DeliveryVehicleNavigationStatus\x12\x1d\n\x15current_route_segment\x18\x04 \x01(\x0c\x12<\n\x1fcurrent_route_segment_end_point\x18\x05 \x01(\x0b2\x13.google.type.LatLng\x12>\n\x19remaining_distance_meters\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int32Value\x125\n\x12remaining_duration\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x12_\n"remaining_vehicle_journey_segments\x18\x08 \x03(\x0b23.maps.fleetengine.delivery.v1.VehicleJourneySegment\x12J\n\nattributes\x18\t \x03(\x0b26.maps.fleetengine.delivery.v1.DeliveryVehicleAttribute\x12O\n\x04type\x18\n \x01(\x0e2A.maps.fleetengine.delivery.v1.DeliveryVehicle.DeliveryVehicleType"t\n\x13DeliveryVehicleType\x12%\n!DELIVERY_VEHICLE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04AUTO\x10\x01\x12\x0f\n\x0bTWO_WHEELER\x10\x02\x12\x0b\n\x07BICYCLE\x10\x03\x12\x0e\n\nPEDESTRIAN\x10\x04:`\xeaA]\n*fleetengine.googleapis.com/DeliveryVehicle\x12/providers/{provider}/deliveryVehicles/{vehicle}"2\n\x0cLocationInfo\x12"\n\x05point\x18\x01 \x01(\x0b2\x13.google.type.LatLng"\xf5\x01\n\x15VehicleJourneySegment\x127\n\x04stop\x18\x01 \x01(\x0b2).maps.fleetengine.delivery.v1.VehicleStop\x12A\n\x17driving_distance_meters\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x03\x128\n\x10driving_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12&\n\x04path\x18\x05 \x03(\x0b2\x13.google.type.LatLngB\x03\xe0A\x03"\xbe\x03\n\x0bVehicleStop\x12I\n\x10planned_location\x18\x01 \x01(\x0b2*.maps.fleetengine.delivery.v1.LocationInfoB\x03\xe0A\x02\x12A\n\x05tasks\x18\x02 \x03(\x0b22.maps.fleetengine.delivery.v1.VehicleStop.TaskInfo\x12>\n\x05state\x18\x03 \x01(\x0e2/.maps.fleetengine.delivery.v1.VehicleStop.State\x1a\x9d\x01\n\x08TaskInfo\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x125\n\rtask_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12I\n\x12target_time_window\x18\x03 \x01(\x0b2(.maps.fleetengine.delivery.v1.TimeWindowB\x03\xe0A\x03"A\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x0b\n\x07ENROUTE\x10\x02\x12\x0b\n\x07ARRIVED\x10\x03B\x85\x02\n\'com.google.maps.fleetengine.delivery.v1B\x10DeliveryVehiclesP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02\'Google::Maps::FleetEngine::Delivery::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.delivery.v1.delivery_vehicles_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.fleetengine.delivery.v1B\x10DeliveryVehiclesP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02'Google::Maps::FleetEngine::Delivery::V1"
    _globals['_DELIVERYVEHICLE']._loaded_options = None
    _globals['_DELIVERYVEHICLE']._serialized_options = b'\xeaA]\n*fleetengine.googleapis.com/DeliveryVehicle\x12/providers/{provider}/deliveryVehicles/{vehicle}'
    _globals['_VEHICLEJOURNEYSEGMENT'].fields_by_name['driving_distance_meters']._loaded_options = None
    _globals['_VEHICLEJOURNEYSEGMENT'].fields_by_name['driving_distance_meters']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLEJOURNEYSEGMENT'].fields_by_name['driving_duration']._loaded_options = None
    _globals['_VEHICLEJOURNEYSEGMENT'].fields_by_name['driving_duration']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLEJOURNEYSEGMENT'].fields_by_name['path']._loaded_options = None
    _globals['_VEHICLEJOURNEYSEGMENT'].fields_by_name['path']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLESTOP_TASKINFO'].fields_by_name['task_duration']._loaded_options = None
    _globals['_VEHICLESTOP_TASKINFO'].fields_by_name['task_duration']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLESTOP_TASKINFO'].fields_by_name['target_time_window']._loaded_options = None
    _globals['_VEHICLESTOP_TASKINFO'].fields_by_name['target_time_window']._serialized_options = b'\xe0A\x03'
    _globals['_VEHICLESTOP'].fields_by_name['planned_location']._loaded_options = None
    _globals['_VEHICLESTOP'].fields_by_name['planned_location']._serialized_options = b'\xe0A\x02'
    _globals['_DELIVERYVEHICLE']._serialized_start = 294
    _globals['_DELIVERYVEHICLE']._serialized_end = 1175
    _globals['_DELIVERYVEHICLE_DELIVERYVEHICLETYPE']._serialized_start = 961
    _globals['_DELIVERYVEHICLE_DELIVERYVEHICLETYPE']._serialized_end = 1077
    _globals['_LOCATIONINFO']._serialized_start = 1177
    _globals['_LOCATIONINFO']._serialized_end = 1227
    _globals['_VEHICLEJOURNEYSEGMENT']._serialized_start = 1230
    _globals['_VEHICLEJOURNEYSEGMENT']._serialized_end = 1475
    _globals['_VEHICLESTOP']._serialized_start = 1478
    _globals['_VEHICLESTOP']._serialized_end = 1924
    _globals['_VEHICLESTOP_TASKINFO']._serialized_start = 1700
    _globals['_VEHICLESTOP_TASKINFO']._serialized_end = 1857
    _globals['_VEHICLESTOP_STATE']._serialized_start = 1859
    _globals['_VEHICLESTOP_STATE']._serialized_end = 1924