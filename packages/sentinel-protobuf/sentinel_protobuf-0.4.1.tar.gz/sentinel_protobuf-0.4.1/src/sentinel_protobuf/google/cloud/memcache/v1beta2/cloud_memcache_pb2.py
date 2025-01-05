"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/memcache/v1beta2/cloud_memcache.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from .....google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/memcache/v1beta2/cloud_memcache.proto\x12\x1dgoogle.cloud.memcache.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto"\xc6\x0e\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12C\n\x06labels\x18\x03 \x03(\x0b23.google.cloud.memcache.v1beta2.Instance.LabelsEntry\x12\x1a\n\x12authorized_network\x18\x04 \x01(\t\x12\r\n\x05zones\x18\x05 \x03(\t\x12\x17\n\nnode_count\x18\x06 \x01(\x05B\x03\xe0A\x02\x12L\n\x0bnode_config\x18\x07 \x01(\x0b22.google.cloud.memcache.v1beta2.Instance.NodeConfigB\x03\xe0A\x02\x12H\n\x10memcache_version\x18\t \x01(\x0e2..google.cloud.memcache.v1beta2.MemcacheVersion\x12E\n\nparameters\x18\x0b \x01(\x0b21.google.cloud.memcache.v1beta2.MemcacheParameters\x12I\n\x0ememcache_nodes\x18\x0c \x03(\x0b2,.google.cloud.memcache.v1beta2.Instance.NodeB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x05state\x18\x0f \x01(\x0e2-.google.cloud.memcache.v1beta2.Instance.StateB\x03\xe0A\x03\x12"\n\x15memcache_full_version\x18\x12 \x01(\tB\x03\xe0A\x03\x12R\n\x11instance_messages\x18\x13 \x03(\x0b27.google.cloud.memcache.v1beta2.Instance.InstanceMessage\x12\x1f\n\x12discovery_endpoint\x18\x14 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10update_available\x18\x15 \x01(\x08B\x03\xe0A\x03\x12L\n\x12maintenance_policy\x18\x16 \x01(\x0b20.google.cloud.memcache.v1beta2.MaintenancePolicy\x12U\n\x14maintenance_schedule\x18\x17 \x01(\x0b22.google.cloud.memcache.v1beta2.MaintenanceScheduleB\x03\xe0A\x03\x1aA\n\nNodeConfig\x12\x16\n\tcpu_count\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x1b\n\x0ememory_size_mb\x18\x02 \x01(\x05B\x03\xe0A\x02\x1a\xd8\x02\n\x04Node\x12\x14\n\x07node_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04zone\x18\x02 \x01(\tB\x03\xe0A\x03\x12F\n\x05state\x18\x03 \x01(\x0e22.google.cloud.memcache.v1beta2.Instance.Node.StateB\x03\xe0A\x03\x12\x11\n\x04host\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04port\x18\x05 \x01(\x05B\x03\xe0A\x03\x12E\n\nparameters\x18\x06 \x01(\x0b21.google.cloud.memcache.v1beta2.MemcacheParameters\x12\x1d\n\x10update_available\x18\x07 \x01(\x08B\x03\xe0A\x03"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x1a\xae\x01\n\x0fInstanceMessage\x12J\n\x04code\x18\x01 \x01(\x0e2<.google.cloud.memcache.v1beta2.Instance.InstanceMessage.Code\x12\x0f\n\x07message\x18\x02 \x01(\t">\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12 \n\x1cZONE_DISTRIBUTION_UNBALANCED\x10\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"o\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x1a\n\x16PERFORMING_MAINTENANCE\x10\x05:c\xeaA`\n memcache.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}"\xf4\x01\n\x11MaintenancePolicy\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12^\n\x19weekly_maintenance_window\x18\x04 \x03(\x0b26.google.cloud.memcache.v1beta2.WeeklyMaintenanceWindowB\x03\xe0A\x02"\xa6\x01\n\x17WeeklyMaintenanceWindow\x12(\n\x03day\x18\x01 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02\x12/\n\nstart_time\x18\x02 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x02\x120\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02"\xbe\x01\n\x13MaintenanceSchedule\x123\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x16schedule_deadline_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x9a\x01\n\x14ListInstancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x81\x01\n\x15ListInstancesResponse\x12:\n\tresources\x18\x01 \x03(\x0b2\'.google.cloud.memcache.v1beta2.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x12GetInstanceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance"\xac\x01\n\x15CreateInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x08resource\x18\x03 \x01(\x0b2\'.google.cloud.memcache.v1beta2.InstanceB\x03\xe0A\x02"\x8d\x01\n\x15UpdateInstanceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\x08resource\x18\x02 \x01(\x0b2\'.google.cloud.memcache.v1beta2.InstanceB\x03\xe0A\x02"O\n\x15DeleteInstanceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance"\xe7\x02\n\x1cRescheduleMaintenanceRequest\x12:\n\x08instance\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x12h\n\x0freschedule_type\x18\x02 \x01(\x0e2J.google.cloud.memcache.v1beta2.RescheduleMaintenanceRequest.RescheduleTypeB\x03\xe0A\x02\x121\n\rschedule_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"n\n\x0eRescheduleType\x12\x1f\n\x1bRESCHEDULE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tIMMEDIATE\x10\x01\x12\x19\n\x15NEXT_AVAILABLE_WINDOW\x10\x02\x12\x11\n\rSPECIFIC_TIME\x10\x03"u\n\x16ApplyParametersRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x12\x10\n\x08node_ids\x18\x02 \x03(\t\x12\x11\n\tapply_all\x18\x03 \x01(\x08"\xce\x01\n\x17UpdateParametersRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12E\n\nparameters\x18\x03 \x01(\x0b21.google.cloud.memcache.v1beta2.MemcacheParameters"}\n\x1aApplySoftwareUpdateRequest\x12:\n\x08instance\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x12\x10\n\x08node_ids\x18\x02 \x03(\t\x12\x11\n\tapply_all\x18\x03 \x01(\x08"\xa3\x01\n\x12MemcacheParameters\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12M\n\x06params\x18\x03 \x03(\x0b2=.google.cloud.memcache.v1beta2.MemcacheParameters.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xf9\x01\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rstatus_detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10cancel_requested\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"\xd9\x01\n\x10LocationMetadata\x12a\n\x0favailable_zones\x18\x01 \x03(\x0b2C.google.cloud.memcache.v1beta2.LocationMetadata.AvailableZonesEntryB\x03\xe0A\x03\x1ab\n\x13AvailableZonesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.memcache.v1beta2.ZoneMetadata:\x028\x01"\x0e\n\x0cZoneMetadata*E\n\x0fMemcacheVersion\x12 \n\x1cMEMCACHE_VERSION_UNSPECIFIED\x10\x00\x12\x10\n\x0cMEMCACHE_1_5\x10\x012\x9a\x14\n\rCloudMemcache\x12\xbf\x01\n\rListInstances\x123.google.cloud.memcache.v1beta2.ListInstancesRequest\x1a4.google.cloud.memcache.v1beta2.ListInstancesResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta2/{parent=projects/*/locations/*}/instances\x12\xac\x01\n\x0bGetInstance\x121.google.cloud.memcache.v1beta2.GetInstanceRequest\x1a\'.google.cloud.memcache.v1beta2.Instance"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta2/{name=projects/*/locations/*/instances/*}\x12\xa6\x02\n\x0eCreateInstance\x124.google.cloud.memcache.v1beta2.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"\xbe\x01\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x1bparent,instance_id,resource\x82\xd3\xe4\x93\x02>"2/v1beta2/{parent=projects/*/locations/*}/instances:\x08resource\x12\xa8\x02\n\x0eUpdateInstance\x124.google.cloud.memcache.v1beta2.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation"\xc0\x01\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x14update_mask,resource\x82\xd3\xe4\x93\x02G2;/v1beta2/{resource.name=projects/*/locations/*/instances/*}:\x08resource\x12\xb4\x02\n\x10UpdateParameters\x126.google.cloud.memcache.v1beta2.UpdateParametersRequest\x1a\x1d.google.longrunning.Operation"\xc8\x01\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x1bname,update_mask,parameters\x82\xd3\xe4\x93\x02H2C/v1beta2/{name=projects/*/locations/*/instances/*}:updateParameters:\x01*\x12\xf4\x01\n\x0eDeleteInstance\x124.google.cloud.memcache.v1beta2.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaAH\n\x15google.protobuf.Empty\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta2/{name=projects/*/locations/*/instances/*}\x12\xad\x02\n\x0fApplyParameters\x125.google.cloud.memcache.v1beta2.ApplyParametersRequest\x1a\x1d.google.longrunning.Operation"\xc3\x01\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x17name,node_ids,apply_all\x82\xd3\xe4\x93\x02G"B/v1beta2/{name=projects/*/locations/*/instances/*}:applyParameters:\x01*\x12\xc1\x02\n\x13ApplySoftwareUpdate\x129.google.cloud.memcache.v1beta2.ApplySoftwareUpdateRequest\x1a\x1d.google.longrunning.Operation"\xcf\x01\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x1binstance,node_ids,apply_all\x82\xd3\xe4\x93\x02O"J/v1beta2/{instance=projects/*/locations/*/instances/*}:applySoftwareUpdate:\x01*\x12\xd4\x02\n\x15RescheduleMaintenance\x12;.google.cloud.memcache.v1beta2.RescheduleMaintenanceRequest\x1a\x1d.google.longrunning.Operation"\xde\x01\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA(instance, reschedule_type, schedule_time\x82\xd3\xe4\x93\x02Q"L/v1beta2/{instance=projects/*/locations/*/instances/*}:rescheduleMaintenance:\x01*\x1aK\xcaA\x17memcache.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBx\n!com.google.cloud.memcache.v1beta2B\x12CloudMemcacheProtoP\x01Z=cloud.google.com/go/memcache/apiv1beta2/memcachepb;memcachepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.memcache.v1beta2.cloud_memcache_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.memcache.v1beta2B\x12CloudMemcacheProtoP\x01Z=cloud.google.com/go/memcache/apiv1beta2/memcachepb;memcachepb'
    _globals['_INSTANCE_NODECONFIG'].fields_by_name['cpu_count']._loaded_options = None
    _globals['_INSTANCE_NODECONFIG'].fields_by_name['cpu_count']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE_NODECONFIG'].fields_by_name['memory_size_mb']._loaded_options = None
    _globals['_INSTANCE_NODECONFIG'].fields_by_name['memory_size_mb']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE_NODE'].fields_by_name['node_id']._loaded_options = None
    _globals['_INSTANCE_NODE'].fields_by_name['node_id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_NODE'].fields_by_name['zone']._loaded_options = None
    _globals['_INSTANCE_NODE'].fields_by_name['zone']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_NODE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE_NODE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_NODE'].fields_by_name['host']._loaded_options = None
    _globals['_INSTANCE_NODE'].fields_by_name['host']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_NODE'].fields_by_name['port']._loaded_options = None
    _globals['_INSTANCE_NODE'].fields_by_name['port']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_NODE'].fields_by_name['update_available']._loaded_options = None
    _globals['_INSTANCE_NODE'].fields_by_name['update_available']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['node_count']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['node_count']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['node_config']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['node_config']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['memcache_nodes']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['memcache_nodes']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['memcache_full_version']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['memcache_full_version']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['discovery_endpoint']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['discovery_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_available']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_available']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['maintenance_schedule']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['maintenance_schedule']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaA`\n memcache.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}'
    _globals['_MAINTENANCEPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_MAINTENANCEPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCEPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_MAINTENANCEPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCEPOLICY'].fields_by_name['weekly_maintenance_window']._loaded_options = None
    _globals['_MAINTENANCEPOLICY'].fields_by_name['weekly_maintenance_window']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKLYMAINTENANCEWINDOW'].fields_by_name['day']._loaded_options = None
    _globals['_WEEKLYMAINTENANCEWINDOW'].fields_by_name['day']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKLYMAINTENANCEWINDOW'].fields_by_name['start_time']._loaded_options = None
    _globals['_WEEKLYMAINTENANCEWINDOW'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKLYMAINTENANCEWINDOW'].fields_by_name['duration']._loaded_options = None
    _globals['_WEEKLYMAINTENANCEWINDOW'].fields_by_name['duration']._serialized_options = b'\xe0A\x02'
    _globals['_MAINTENANCESCHEDULE'].fields_by_name['start_time']._loaded_options = None
    _globals['_MAINTENANCESCHEDULE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESCHEDULE'].fields_by_name['end_time']._loaded_options = None
    _globals['_MAINTENANCESCHEDULE'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESCHEDULE'].fields_by_name['schedule_deadline_time']._loaded_options = None
    _globals['_MAINTENANCESCHEDULE'].fields_by_name['schedule_deadline_time']._serialized_options = b'\xe0A\x03'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['reschedule_type']._loaded_options = None
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['reschedule_type']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYPARAMETERSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_APPLYPARAMETERSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYSOFTWAREUPDATEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_APPLYSOFTWAREUPDATEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_MEMCACHEPARAMETERS_PARAMSENTRY']._loaded_options = None
    _globals['_MEMCACHEPARAMETERS_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_MEMCACHEPARAMETERS'].fields_by_name['id']._loaded_options = None
    _globals['_MEMCACHEPARAMETERS'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_detail']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_detail']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['cancel_requested']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['cancel_requested']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_LOCATIONMETADATA_AVAILABLEZONESENTRY']._loaded_options = None
    _globals['_LOCATIONMETADATA_AVAILABLEZONESENTRY']._serialized_options = b'8\x01'
    _globals['_LOCATIONMETADATA'].fields_by_name['available_zones']._loaded_options = None
    _globals['_LOCATIONMETADATA'].fields_by_name['available_zones']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDMEMCACHE']._loaded_options = None
    _globals['_CLOUDMEMCACHE']._serialized_options = b'\xcaA\x17memcache.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDMEMCACHE'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['ListInstances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta2/{parent=projects/*/locations/*}/instances'
    _globals['_CLOUDMEMCACHE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta2/{name=projects/*/locations/*/instances/*}'
    _globals['_CLOUDMEMCACHE'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['CreateInstance']._serialized_options = b'\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x1bparent,instance_id,resource\x82\xd3\xe4\x93\x02>"2/v1beta2/{parent=projects/*/locations/*}/instances:\x08resource'
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateInstance']._serialized_options = b'\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x14update_mask,resource\x82\xd3\xe4\x93\x02G2;/v1beta2/{resource.name=projects/*/locations/*/instances/*}:\x08resource'
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateParameters']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateParameters']._serialized_options = b'\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x1bname,update_mask,parameters\x82\xd3\xe4\x93\x02H2C/v1beta2/{name=projects/*/locations/*/instances/*}:updateParameters:\x01*'
    _globals['_CLOUDMEMCACHE'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaAH\n\x15google.protobuf.Empty\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta2/{name=projects/*/locations/*/instances/*}'
    _globals['_CLOUDMEMCACHE'].methods_by_name['ApplyParameters']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['ApplyParameters']._serialized_options = b'\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x17name,node_ids,apply_all\x82\xd3\xe4\x93\x02G"B/v1beta2/{name=projects/*/locations/*/instances/*}:applyParameters:\x01*'
    _globals['_CLOUDMEMCACHE'].methods_by_name['ApplySoftwareUpdate']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['ApplySoftwareUpdate']._serialized_options = b'\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA\x1binstance,node_ids,apply_all\x82\xd3\xe4\x93\x02O"J/v1beta2/{instance=projects/*/locations/*/instances/*}:applySoftwareUpdate:\x01*'
    _globals['_CLOUDMEMCACHE'].methods_by_name['RescheduleMaintenance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['RescheduleMaintenance']._serialized_options = b'\xcaAY\n&google.cloud.memcache.v1beta2.Instance\x12/google.cloud.memcache.v1beta2.OperationMetadata\xdaA(instance, reschedule_type, schedule_time\x82\xd3\xe4\x93\x02Q"L/v1beta2/{instance=projects/*/locations/*/instances/*}:rescheduleMaintenance:\x01*'
    _globals['_MEMCACHEVERSION']._serialized_start = 5106
    _globals['_MEMCACHEVERSION']._serialized_end = 5175
    _globals['_INSTANCE']._serialized_start = 395
    _globals['_INSTANCE']._serialized_end = 2257
    _globals['_INSTANCE_NODECONFIG']._serialized_start = 1407
    _globals['_INSTANCE_NODECONFIG']._serialized_end = 1472
    _globals['_INSTANCE_NODE']._serialized_start = 1475
    _globals['_INSTANCE_NODE']._serialized_end = 1819
    _globals['_INSTANCE_NODE_STATE']._serialized_start = 1736
    _globals['_INSTANCE_NODE_STATE']._serialized_end = 1819
    _globals['_INSTANCE_INSTANCEMESSAGE']._serialized_start = 1822
    _globals['_INSTANCE_INSTANCEMESSAGE']._serialized_end = 1996
    _globals['_INSTANCE_INSTANCEMESSAGE_CODE']._serialized_start = 1934
    _globals['_INSTANCE_INSTANCEMESSAGE_CODE']._serialized_end = 1996
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 1998
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 2043
    _globals['_INSTANCE_STATE']._serialized_start = 2045
    _globals['_INSTANCE_STATE']._serialized_end = 2156
    _globals['_MAINTENANCEPOLICY']._serialized_start = 2260
    _globals['_MAINTENANCEPOLICY']._serialized_end = 2504
    _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_start = 2507
    _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_end = 2673
    _globals['_MAINTENANCESCHEDULE']._serialized_start = 2676
    _globals['_MAINTENANCESCHEDULE']._serialized_end = 2866
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 2869
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 3023
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 3026
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 3155
    _globals['_GETINSTANCEREQUEST']._serialized_start = 3157
    _globals['_GETINSTANCEREQUEST']._serialized_end = 3233
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 3236
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 3408
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 3411
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 3552
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 3554
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 3633
    _globals['_RESCHEDULEMAINTENANCEREQUEST']._serialized_start = 3636
    _globals['_RESCHEDULEMAINTENANCEREQUEST']._serialized_end = 3995
    _globals['_RESCHEDULEMAINTENANCEREQUEST_RESCHEDULETYPE']._serialized_start = 3885
    _globals['_RESCHEDULEMAINTENANCEREQUEST_RESCHEDULETYPE']._serialized_end = 3995
    _globals['_APPLYPARAMETERSREQUEST']._serialized_start = 3997
    _globals['_APPLYPARAMETERSREQUEST']._serialized_end = 4114
    _globals['_UPDATEPARAMETERSREQUEST']._serialized_start = 4117
    _globals['_UPDATEPARAMETERSREQUEST']._serialized_end = 4323
    _globals['_APPLYSOFTWAREUPDATEREQUEST']._serialized_start = 4325
    _globals['_APPLYSOFTWAREUPDATEREQUEST']._serialized_end = 4450
    _globals['_MEMCACHEPARAMETERS']._serialized_start = 4453
    _globals['_MEMCACHEPARAMETERS']._serialized_end = 4616
    _globals['_MEMCACHEPARAMETERS_PARAMSENTRY']._serialized_start = 4571
    _globals['_MEMCACHEPARAMETERS_PARAMSENTRY']._serialized_end = 4616
    _globals['_OPERATIONMETADATA']._serialized_start = 4619
    _globals['_OPERATIONMETADATA']._serialized_end = 4868
    _globals['_LOCATIONMETADATA']._serialized_start = 4871
    _globals['_LOCATIONMETADATA']._serialized_end = 5088
    _globals['_LOCATIONMETADATA_AVAILABLEZONESENTRY']._serialized_start = 4990
    _globals['_LOCATIONMETADATA_AVAILABLEZONESENTRY']._serialized_end = 5088
    _globals['_ZONEMETADATA']._serialized_start = 5090
    _globals['_ZONEMETADATA']._serialized_end = 5104
    _globals['_CLOUDMEMCACHE']._serialized_start = 5178
    _globals['_CLOUDMEMCACHE']._serialized_end = 7764