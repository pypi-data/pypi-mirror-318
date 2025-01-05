"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/delivery/v1/delivery_api.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.api import routing_pb2 as google_dot_api_dot_routing__pb2
from ......google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from ......google.maps.fleetengine.delivery.v1 import delivery_vehicles_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_delivery__vehicles__pb2
from ......google.maps.fleetengine.delivery.v1 import header_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_header__pb2
from ......google.maps.fleetengine.delivery.v1 import task_tracking_info_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_task__tracking__info__pb2
from ......google.maps.fleetengine.delivery.v1 import tasks_pb2 as google_dot_maps_dot_fleetengine_dot_delivery_dot_v1_dot_tasks__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/maps/fleetengine/delivery/v1/delivery_api.proto\x12\x1cmaps.fleetengine.delivery.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x18google/api/routing.proto\x1a\x1egoogle/geo/type/viewport.proto\x1a;google/maps/fleetengine/delivery/v1/delivery_vehicles.proto\x1a0google/maps/fleetengine/delivery/v1/header.proto\x1a<google/maps/fleetengine/delivery/v1/task_tracking_info.proto\x1a/google/maps/fleetengine/delivery/v1/tasks.proto\x1a google/protobuf/field_mask.proto"\xed\x01\n\x1cCreateDeliveryVehicleRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x12\x13\n\x06parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12 \n\x13delivery_vehicle_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12L\n\x10delivery_vehicle\x18\x05 \x01(\x0b2-.maps.fleetengine.delivery.v1.DeliveryVehicleB\x03\xe0A\x02"\xa7\x01\n\x19GetDeliveryVehicleRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x12@\n\x04name\x18\x03 \x01(\tB2\xe0A\x02\xfaA,\n*fleetengine.googleapis.com/DeliveryVehicle"\xa3\x02\n\x1bListDeliveryVehiclesRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x12B\n\x06parent\x18\x03 \x01(\tB2\xe0A\x02\xfaA,\x12*fleetengine.googleapis.com/DeliveryVehicle\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x06 \x01(\tB\x03\xe0A\x01\x120\n\x08viewport\x18\x07 \x01(\x0b2\x19.google.geo.type.ViewportB\x03\xe0A\x01"\x95\x01\n\x1cListDeliveryVehiclesResponse\x12H\n\x11delivery_vehicles\x18\x01 \x03(\x0b2-.maps.fleetengine.delivery.v1.DeliveryVehicle\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x03"\xec\x01\n\x1cUpdateDeliveryVehicleRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x12L\n\x10delivery_vehicle\x18\x03 \x01(\x0b2-.maps.fleetengine.delivery.v1.DeliveryVehicleB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xe4\x01\n\x17BatchCreateTasksRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x127\n\x06parent\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1ffleetengine.googleapis.com/Task\x12F\n\x08requests\x18\x04 \x03(\x0b2/.maps.fleetengine.delivery.v1.CreateTaskRequestB\x03\xe0A\x02"M\n\x18BatchCreateTasksResponse\x121\n\x05tasks\x18\x01 \x03(\x0b2".maps.fleetengine.delivery.v1.Task"\xbf\x01\n\x11CreateTaskRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x12\x13\n\x06parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07task_id\x18\x05 \x01(\tB\x03\xe0A\x02\x125\n\x04task\x18\x04 \x01(\x0b2".maps.fleetengine.delivery.v1.TaskB\x03\xe0A\x02"\x91\x01\n\x0eGetTaskRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x125\n\x04name\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1ffleetengine.googleapis.com/Task"\xca\x01\n\x11UpdateTaskRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x125\n\x04task\x18\x03 \x01(\x0b2".maps.fleetengine.delivery.v1.TaskB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xdb\x01\n\x10ListTasksRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x127\n\x06parent\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1ffleetengine.googleapis.com/Task\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x06 \x01(\tB\x03\xe0A\x01"s\n\x11ListTasksResponse\x121\n\x05tasks\x18\x01 \x03(\x0b2".maps.fleetengine.delivery.v1.Task\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x03"\xa9\x01\n\x1aGetTaskTrackingInfoRequest\x12H\n\x06header\x18\x01 \x01(\x0b23.maps.fleetengine.delivery.v1.DeliveryRequestHeaderB\x03\xe0A\x01\x12A\n\x04name\x18\x03 \x01(\tB3\xe0A\x02\xfaA-\n+fleetengine.googleapis.com/TaskTrackingInfo2\x8a\x13\n\x0fDeliveryService\x12\xa1\x02\n\x15CreateDeliveryVehicle\x12:.maps.fleetengine.delivery.v1.CreateDeliveryVehicleRequest\x1a-.maps.fleetengine.delivery.v1.DeliveryVehicle"\x9c\x01\xdaA+parent,delivery_vehicle,delivery_vehicle_id\x82\xd3\xe4\x93\x02=")/v1/{parent=providers/*}/deliveryVehicles:\x10delivery_vehicle\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xdf\x01\n\x12GetDeliveryVehicle\x127.maps.fleetengine.delivery.v1.GetDeliveryVehicleRequest\x1a-.maps.fleetengine.delivery.v1.DeliveryVehicle"a\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=providers/*/deliveryVehicles/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xb2\x02\n\x15UpdateDeliveryVehicle\x12:.maps.fleetengine.delivery.v1.UpdateDeliveryVehicleRequest\x1a-.maps.fleetengine.delivery.v1.DeliveryVehicle"\xad\x01\xdaA\x1cdelivery_vehicle,update_mask\x82\xd3\xe4\x93\x02N2:/v1/{delivery_vehicle.name=providers/*/deliveryVehicles/*}:\x10delivery_vehicle\x8a\xd3\xe4\x93\x024\x122\n\x15delivery_vehicle.name\x12\x19{provider_id=providers/*}\x12\xe3\x01\n\x10BatchCreateTasks\x125.maps.fleetengine.delivery.v1.BatchCreateTasksRequest\x1a6.maps.fleetengine.delivery.v1.BatchCreateTasksResponse"`\x82\xd3\xe4\x93\x02/"*/v1/{parent=providers/*}/tasks:batchCreate:\x01*\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xd0\x01\n\nCreateTask\x12/.maps.fleetengine.delivery.v1.CreateTaskRequest\x1a".maps.fleetengine.delivery.v1.Task"m\xdaA\x13parent,task,task_id\x82\xd3\xe4\x93\x02&"\x1e/v1/{parent=providers/*}/tasks:\x04task\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xb3\x01\n\x07GetTask\x12,.maps.fleetengine.delivery.v1.GetTaskRequest\x1a".maps.fleetengine.delivery.v1.Task"V\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=providers/*/tasks/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xd5\x01\n\nUpdateTask\x12/.maps.fleetengine.delivery.v1.UpdateTaskRequest\x1a".maps.fleetengine.delivery.v1.Task"r\xdaA\x10task,update_mask\x82\xd3\xe4\x93\x02+2#/v1/{task.name=providers/*/tasks/*}:\x04task\x8a\xd3\xe4\x93\x02(\x12&\n\ttask.name\x12\x19{provider_id=providers/*}\x12\xc8\x01\n\tListTasks\x12..maps.fleetengine.delivery.v1.ListTasksRequest\x1a/.maps.fleetengine.delivery.v1.ListTasksResponse"Z\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=providers/*}/tasks\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xe2\x01\n\x13GetTaskTrackingInfo\x128.maps.fleetengine.delivery.v1.GetTaskTrackingInfoRequest\x1a..maps.fleetengine.delivery.v1.TaskTrackingInfo"a\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=providers/*/taskTrackingInfo/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xf4\x01\n\x14ListDeliveryVehicles\x129.maps.fleetengine.delivery.v1.ListDeliveryVehiclesRequest\x1a:.maps.fleetengine.delivery.v1.ListDeliveryVehiclesResponse"e\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=providers/*}/deliveryVehicles\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x1aN\xcaA\x1afleetengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbe\x02\n\'com.google.maps.fleetengine.delivery.v1B\x0bDeliveryApiP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02\'Google::Maps::FleetEngine::Delivery::V1\xeaA;\n#fleetengine.googleapis.com/Provider\x12\x14providers/{provider}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.delivery.v1.delivery_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.fleetengine.delivery.v1B\x0bDeliveryApiP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02'Google::Maps::FleetEngine::Delivery::V1\xeaA;\n#fleetengine.googleapis.com/Provider\x12\x14providers/{provider}"
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['delivery_vehicle_id']._loaded_options = None
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['delivery_vehicle_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['delivery_vehicle']._loaded_options = None
    _globals['_CREATEDELIVERYVEHICLEREQUEST'].fields_by_name['delivery_vehicle']._serialized_options = b'\xe0A\x02'
    _globals['_GETDELIVERYVEHICLEREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_GETDELIVERYVEHICLEREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_GETDELIVERYVEHICLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDELIVERYVEHICLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*fleetengine.googleapis.com/DeliveryVehicle'
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*fleetengine.googleapis.com/DeliveryVehicle'
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['viewport']._loaded_options = None
    _globals['_LISTDELIVERYVEHICLESREQUEST'].fields_by_name['viewport']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDELIVERYVEHICLEREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_UPDATEDELIVERYVEHICLEREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDELIVERYVEHICLEREQUEST'].fields_by_name['delivery_vehicle']._loaded_options = None
    _globals['_UPDATEDELIVERYVEHICLEREQUEST'].fields_by_name['delivery_vehicle']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDELIVERYVEHICLEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDELIVERYVEHICLEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATETASKSREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_BATCHCREATETASKSREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHCREATETASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATETASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1ffleetengine.googleapis.com/Task'
    _globals['_BATCHCREATETASKSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATETASKSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETASKREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_CREATETASKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETASKREQUEST'].fields_by_name['task_id']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['task_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETASKREQUEST'].fields_by_name['task']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['task']._serialized_options = b'\xe0A\x02'
    _globals['_GETTASKREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_GETTASKREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_GETTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1ffleetengine.googleapis.com/Task'
    _globals['_UPDATETASKREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_UPDATETASKREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETASKREQUEST'].fields_by_name['task']._loaded_options = None
    _globals['_UPDATETASKREQUEST'].fields_by_name['task']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETASKREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETASKREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTASKSREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1ffleetengine.googleapis.com/Task'
    _globals['_LISTTASKSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTASKSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTASKSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETTASKTRACKINGINFOREQUEST'].fields_by_name['header']._loaded_options = None
    _globals['_GETTASKTRACKINGINFOREQUEST'].fields_by_name['header']._serialized_options = b'\xe0A\x01'
    _globals['_GETTASKTRACKINGINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTASKTRACKINGINFOREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+fleetengine.googleapis.com/TaskTrackingInfo'
    _globals['_DELIVERYSERVICE']._loaded_options = None
    _globals['_DELIVERYSERVICE']._serialized_options = b'\xcaA\x1afleetengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DELIVERYSERVICE'].methods_by_name['CreateDeliveryVehicle']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['CreateDeliveryVehicle']._serialized_options = b'\xdaA+parent,delivery_vehicle,delivery_vehicle_id\x82\xd3\xe4\x93\x02=")/v1/{parent=providers/*}/deliveryVehicles:\x10delivery_vehicle\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['GetDeliveryVehicle']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['GetDeliveryVehicle']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=providers/*/deliveryVehicles/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['UpdateDeliveryVehicle']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['UpdateDeliveryVehicle']._serialized_options = b'\xdaA\x1cdelivery_vehicle,update_mask\x82\xd3\xe4\x93\x02N2:/v1/{delivery_vehicle.name=providers/*/deliveryVehicles/*}:\x10delivery_vehicle\x8a\xd3\xe4\x93\x024\x122\n\x15delivery_vehicle.name\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['BatchCreateTasks']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['BatchCreateTasks']._serialized_options = b'\x82\xd3\xe4\x93\x02/"*/v1/{parent=providers/*}/tasks:batchCreate:\x01*\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['CreateTask']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['CreateTask']._serialized_options = b'\xdaA\x13parent,task,task_id\x82\xd3\xe4\x93\x02&"\x1e/v1/{parent=providers/*}/tasks:\x04task\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['GetTask']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['GetTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=providers/*/tasks/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['UpdateTask']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['UpdateTask']._serialized_options = b'\xdaA\x10task,update_mask\x82\xd3\xe4\x93\x02+2#/v1/{task.name=providers/*/tasks/*}:\x04task\x8a\xd3\xe4\x93\x02(\x12&\n\ttask.name\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['ListTasks']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['ListTasks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=providers/*}/tasks\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['GetTaskTrackingInfo']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['GetTaskTrackingInfo']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=providers/*/taskTrackingInfo/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_DELIVERYSERVICE'].methods_by_name['ListDeliveryVehicles']._loaded_options = None
    _globals['_DELIVERYSERVICE'].methods_by_name['ListDeliveryVehicles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=providers/*}/deliveryVehicles\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_CREATEDELIVERYVEHICLEREQUEST']._serialized_start = 518
    _globals['_CREATEDELIVERYVEHICLEREQUEST']._serialized_end = 755
    _globals['_GETDELIVERYVEHICLEREQUEST']._serialized_start = 758
    _globals['_GETDELIVERYVEHICLEREQUEST']._serialized_end = 925
    _globals['_LISTDELIVERYVEHICLESREQUEST']._serialized_start = 928
    _globals['_LISTDELIVERYVEHICLESREQUEST']._serialized_end = 1219
    _globals['_LISTDELIVERYVEHICLESRESPONSE']._serialized_start = 1222
    _globals['_LISTDELIVERYVEHICLESRESPONSE']._serialized_end = 1371
    _globals['_UPDATEDELIVERYVEHICLEREQUEST']._serialized_start = 1374
    _globals['_UPDATEDELIVERYVEHICLEREQUEST']._serialized_end = 1610
    _globals['_BATCHCREATETASKSREQUEST']._serialized_start = 1613
    _globals['_BATCHCREATETASKSREQUEST']._serialized_end = 1841
    _globals['_BATCHCREATETASKSRESPONSE']._serialized_start = 1843
    _globals['_BATCHCREATETASKSRESPONSE']._serialized_end = 1920
    _globals['_CREATETASKREQUEST']._serialized_start = 1923
    _globals['_CREATETASKREQUEST']._serialized_end = 2114
    _globals['_GETTASKREQUEST']._serialized_start = 2117
    _globals['_GETTASKREQUEST']._serialized_end = 2262
    _globals['_UPDATETASKREQUEST']._serialized_start = 2265
    _globals['_UPDATETASKREQUEST']._serialized_end = 2467
    _globals['_LISTTASKSREQUEST']._serialized_start = 2470
    _globals['_LISTTASKSREQUEST']._serialized_end = 2689
    _globals['_LISTTASKSRESPONSE']._serialized_start = 2691
    _globals['_LISTTASKSRESPONSE']._serialized_end = 2806
    _globals['_GETTASKTRACKINGINFOREQUEST']._serialized_start = 2809
    _globals['_GETTASKTRACKINGINFOREQUEST']._serialized_end = 2978
    _globals['_DELIVERYSERVICE']._serialized_start = 2981
    _globals['_DELIVERYSERVICE']._serialized_end = 5423