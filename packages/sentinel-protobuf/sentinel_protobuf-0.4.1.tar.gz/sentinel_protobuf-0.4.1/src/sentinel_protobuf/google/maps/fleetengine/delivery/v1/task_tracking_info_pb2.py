"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/delivery/v1/task_tracking_info.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.maps.fleetengine.delivery.v1 import common_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_common__pb2
from ......google.maps.fleetengine.delivery.v1 import delivery_vehicles_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_delivery__vehicles__pb2
from ......google.maps.fleetengine.delivery.v1 import tasks_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_tasks__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ......google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/maps/fleetengine/delivery/v1/task_tracking_info.proto\x12\x1cmaps.fleetengine.delivery.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/maps/fleetengine/delivery/v1/common.proto\x1a;google/maps/fleetengine/delivery/v1/delivery_vehicles.proto\x1a/google/maps/fleetengine/delivery/v1/tasks.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xae\x07\n\x10TaskTrackingInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0btracking_id\x18\x02 \x01(\tB\x03\xe0A\x05\x12O\n\x10vehicle_location\x18\x03 \x01(\x0b25.maps.fleetengine.delivery.v1.DeliveryVehicleLocation\x122\n\x15route_polyline_points\x18\x04 \x03(\x0b2\x13.google.type.LatLng\x129\n\x14remaining_stop_count\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12F\n!remaining_driving_distance_meters\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12:\n\x16estimated_arrival_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x1eestimated_task_completion_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x05state\x18\x0b \x01(\x0e2(.maps.fleetengine.delivery.v1.Task.State\x12D\n\x0ctask_outcome\x18\t \x01(\x0e2..maps.fleetengine.delivery.v1.Task.TaskOutcome\x125\n\x11task_outcome_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x10planned_location\x18\n \x01(\x0b2*.maps.fleetengine.delivery.v1.LocationInfoB\x03\xe0A\x05\x12D\n\x12target_time_window\x18\r \x01(\x0b2(.maps.fleetengine.delivery.v1.TimeWindow\x12?\n\nattributes\x18\x0e \x03(\x0b2+.maps.fleetengine.delivery.v1.TaskAttribute:b\xeaA_\n+fleetengine.googleapis.com/TaskTrackingInfo\x120providers/{provider}/taskTrackingInfo/{tracking}B\x8a\x02\n\'com.google.maps.fleetengine.delivery.v1B\x15TaskTrackingInfoProtoP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02\'Google::Maps::FleetEngine::Delivery::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.delivery.v1.task_tracking_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.fleetengine.delivery.v1B\x15TaskTrackingInfoProtoP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02'Google::Maps::FleetEngine::Delivery::V1"
    _globals['_TASKTRACKINGINFO'].fields_by_name['tracking_id']._loaded_options = None
    _globals['_TASKTRACKINGINFO'].fields_by_name['tracking_id']._serialized_options = b'\xe0A\x05'
    _globals['_TASKTRACKINGINFO'].fields_by_name['planned_location']._loaded_options = None
    _globals['_TASKTRACKINGINFO'].fields_by_name['planned_location']._serialized_options = b'\xe0A\x05'
    _globals['_TASKTRACKINGINFO']._loaded_options = None
    _globals['_TASKTRACKINGINFO']._serialized_options = b'\xeaA_\n+fleetengine.googleapis.com/TaskTrackingInfo\x120providers/{provider}/taskTrackingInfo/{tracking}'
    _globals['_TASKTRACKINGINFO']._serialized_start = 406
    _globals['_TASKTRACKINGINFO']._serialized_end = 1348