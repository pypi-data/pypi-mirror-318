"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/delivery/v1/tasks.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.maps.fleetengine.delivery.v1 import common_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_common__pb2
from ......google.maps.fleetengine.delivery.v1 import delivery_vehicles_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_delivery__vehicles__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/maps/fleetengine/delivery/v1/tasks.proto\x12\x1cmaps.fleetengine.delivery.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/maps/fleetengine/delivery/v1/common.proto\x1a;google/maps/fleetengine/delivery/v1/delivery_vehicles.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x0c\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x04type\x18\x02 \x01(\x0e2\'.maps.fleetengine.delivery.v1.Task.TypeB\x06\xe0A\x02\xe0A\x05\x12<\n\x05state\x18\x03 \x01(\x0e2(.maps.fleetengine.delivery.v1.Task.StateB\x03\xe0A\x02\x12D\n\x0ctask_outcome\x18\t \x01(\x0e2..maps.fleetengine.delivery.v1.Task.TaskOutcome\x125\n\x11task_outcome_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x15task_outcome_location\x18\x0b \x01(\x0b2*.maps.fleetengine.delivery.v1.LocationInfo\x12b\n\x1ctask_outcome_location_source\x18\x0c \x01(\x0e2<.maps.fleetengine.delivery.v1.Task.TaskOutcomeLocationSource\x12\x18\n\x0btracking_id\x18\x04 \x01(\tB\x03\xe0A\x05\x12 \n\x13delivery_vehicle_id\x18\x05 \x01(\tB\x03\xe0A\x03\x12I\n\x10planned_location\x18\x06 \x01(\x0b2*.maps.fleetengine.delivery.v1.LocationInfoB\x03\xe0A\x05\x128\n\rtask_duration\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x06\xe0A\x02\xe0A\x05\x12D\n\x12target_time_window\x18\x0e \x01(\x0b2(.maps.fleetengine.delivery.v1.TimeWindow\x12X\n\x14journey_sharing_info\x18\x08 \x01(\x0b25.maps.fleetengine.delivery.v1.Task.JourneySharingInfoB\x03\xe0A\x03\x12W\n\x19task_tracking_view_config\x18\r \x01(\x0b24.maps.fleetengine.delivery.v1.TaskTrackingViewConfig\x12?\n\nattributes\x18\x0f \x03(\x0b2+.maps.fleetengine.delivery.v1.TaskAttribute\x1a\xe4\x01\n\x12JourneySharingInfo\x12_\n"remaining_vehicle_journey_segments\x18\x01 \x03(\x0b23.maps.fleetengine.delivery.v1.VehicleJourneySegment\x12L\n\rlast_location\x18\x02 \x01(\x0b25.maps.fleetengine.delivery.v1.DeliveryVehicleLocation\x12\x1f\n\x17last_location_snappable\x18\x03 \x01(\x08"[\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06PICKUP\x10\x01\x12\x0c\n\x08DELIVERY\x10\x02\x12\x12\n\x0eSCHEDULED_STOP\x10\x03\x12\x0f\n\x0bUNAVAILABLE\x10\x04"4\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\n\n\x06CLOSED\x10\x02"F\n\x0bTaskOutcome\x12\x1c\n\x18TASK_OUTCOME_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02"r\n\x19TaskOutcomeLocationSource\x12,\n(TASK_OUTCOME_LOCATION_SOURCE_UNSPECIFIED\x10\x00\x12\x0c\n\x08PROVIDER\x10\x02\x12\x19\n\x15LAST_VEHICLE_LOCATION\x10\x03:G\xeaAD\n\x1ffleetengine.googleapis.com/Task\x12!providers/{provider}/tasks/{task}"\xcb\x07\n\x16TaskTrackingViewConfig\x12o\n route_polyline_points_visibility\x18\x01 \x01(\x0b2E.maps.fleetengine.delivery.v1.TaskTrackingViewConfig.VisibilityOption\x12p\n!estimated_arrival_time_visibility\x18\x02 \x01(\x0b2E.maps.fleetengine.delivery.v1.TaskTrackingViewConfig.VisibilityOption\x12x\n)estimated_task_completion_time_visibility\x18\x03 \x01(\x0b2E.maps.fleetengine.delivery.v1.TaskTrackingViewConfig.VisibilityOption\x12t\n%remaining_driving_distance_visibility\x18\x04 \x01(\x0b2E.maps.fleetengine.delivery.v1.TaskTrackingViewConfig.VisibilityOption\x12n\n\x1fremaining_stop_count_visibility\x18\x05 \x01(\x0b2E.maps.fleetengine.delivery.v1.TaskTrackingViewConfig.VisibilityOption\x12j\n\x1bvehicle_location_visibility\x18\x06 \x01(\x0b2E.maps.fleetengine.delivery.v1.TaskTrackingViewConfig.VisibilityOption\x1a\x81\x02\n\x10VisibilityOption\x12(\n\x1eremaining_stop_count_threshold\x18\x01 \x01(\x05H\x00\x12T\n/duration_until_estimated_arrival_time_threshold\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x125\n+remaining_driving_distance_meters_threshold\x18\x03 \x01(\x05H\x00\x12\x10\n\x06always\x18\x04 \x01(\x08H\x00\x12\x0f\n\x05never\x18\x05 \x01(\x08H\x00B\x13\n\x11visibility_optionB\xfa\x01\n\'com.google.maps.fleetengine.delivery.v1B\x05TasksP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02\'Google::Maps::FleetEngine::Delivery::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.delivery.v1.tasks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.fleetengine.delivery.v1B\x05TasksP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02'Google::Maps::FleetEngine::Delivery::V1"
    _globals['_TASK'].fields_by_name['type']._loaded_options = None
    _globals['_TASK'].fields_by_name['type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_TASK'].fields_by_name['state']._loaded_options = None
    _globals['_TASK'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_TASK'].fields_by_name['tracking_id']._loaded_options = None
    _globals['_TASK'].fields_by_name['tracking_id']._serialized_options = b'\xe0A\x05'
    _globals['_TASK'].fields_by_name['delivery_vehicle_id']._loaded_options = None
    _globals['_TASK'].fields_by_name['delivery_vehicle_id']._serialized_options = b'\xe0A\x03'
    _globals['_TASK'].fields_by_name['planned_location']._loaded_options = None
    _globals['_TASK'].fields_by_name['planned_location']._serialized_options = b'\xe0A\x05'
    _globals['_TASK'].fields_by_name['task_duration']._loaded_options = None
    _globals['_TASK'].fields_by_name['task_duration']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_TASK'].fields_by_name['journey_sharing_info']._loaded_options = None
    _globals['_TASK'].fields_by_name['journey_sharing_info']._serialized_options = b'\xe0A\x03'
    _globals['_TASK']._loaded_options = None
    _globals['_TASK']._serialized_options = b'\xeaAD\n\x1ffleetengine.googleapis.com/Task\x12!providers/{provider}/tasks/{task}'
    _globals['_TASK']._serialized_start = 318
    _globals['_TASK']._serialized_end = 1909
    _globals['_TASK_JOURNEYSHARINGINFO']._serialized_start = 1273
    _globals['_TASK_JOURNEYSHARINGINFO']._serialized_end = 1501
    _globals['_TASK_TYPE']._serialized_start = 1503
    _globals['_TASK_TYPE']._serialized_end = 1594
    _globals['_TASK_STATE']._serialized_start = 1596
    _globals['_TASK_STATE']._serialized_end = 1648
    _globals['_TASK_TASKOUTCOME']._serialized_start = 1650
    _globals['_TASK_TASKOUTCOME']._serialized_end = 1720
    _globals['_TASK_TASKOUTCOMELOCATIONSOURCE']._serialized_start = 1722
    _globals['_TASK_TASKOUTCOMELOCATIONSOURCE']._serialized_end = 1836
    _globals['_TASKTRACKINGVIEWCONFIG']._serialized_start = 1912
    _globals['_TASKTRACKINGVIEWCONFIG']._serialized_end = 2883
    _globals['_TASKTRACKINGVIEWCONFIG_VISIBILITYOPTION']._serialized_start = 2626
    _globals['_TASKTRACKINGVIEWCONFIG_VISIBILITYOPTION']._serialized_end = 2883