"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/memcache/v1/cloud_memcache.proto')
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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/memcache/v1/cloud_memcache.proto\x12\x18google.cloud.memcache.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto"\xcc\r\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12>\n\x06labels\x18\x03 \x03(\x0b2..google.cloud.memcache.v1.Instance.LabelsEntry\x12\x1a\n\x12authorized_network\x18\x04 \x01(\t\x12\r\n\x05zones\x18\x05 \x03(\t\x12\x17\n\nnode_count\x18\x06 \x01(\x05B\x03\xe0A\x02\x12G\n\x0bnode_config\x18\x07 \x01(\x0b2-.google.cloud.memcache.v1.Instance.NodeConfigB\x03\xe0A\x02\x12C\n\x10memcache_version\x18\t \x01(\x0e2).google.cloud.memcache.v1.MemcacheVersion\x12@\n\nparameters\x18\x0b \x01(\x0b2,.google.cloud.memcache.v1.MemcacheParameters\x12D\n\x0ememcache_nodes\x18\x0c \x03(\x0b2\'.google.cloud.memcache.v1.Instance.NodeB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x05state\x18\x0f \x01(\x0e2(.google.cloud.memcache.v1.Instance.StateB\x03\xe0A\x03\x12"\n\x15memcache_full_version\x18\x12 \x01(\tB\x03\xe0A\x03\x12M\n\x11instance_messages\x18\x13 \x03(\x0b22.google.cloud.memcache.v1.Instance.InstanceMessage\x12\x1f\n\x12discovery_endpoint\x18\x14 \x01(\tB\x03\xe0A\x03\x12G\n\x12maintenance_policy\x18\x15 \x01(\x0b2+.google.cloud.memcache.v1.MaintenancePolicy\x12P\n\x14maintenance_schedule\x18\x16 \x01(\x0b2-.google.cloud.memcache.v1.MaintenanceScheduleB\x03\xe0A\x03\x1aA\n\nNodeConfig\x12\x16\n\tcpu_count\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x1b\n\x0ememory_size_mb\x18\x02 \x01(\x05B\x03\xe0A\x02\x1a\xaf\x02\n\x04Node\x12\x14\n\x07node_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04zone\x18\x02 \x01(\tB\x03\xe0A\x03\x12A\n\x05state\x18\x03 \x01(\x0e2-.google.cloud.memcache.v1.Instance.Node.StateB\x03\xe0A\x03\x12\x11\n\x04host\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04port\x18\x05 \x01(\x05B\x03\xe0A\x03\x12@\n\nparameters\x18\x06 \x01(\x0b2,.google.cloud.memcache.v1.MemcacheParameters"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x1a\xa9\x01\n\x0fInstanceMessage\x12E\n\x04code\x18\x01 \x01(\x0e27.google.cloud.memcache.v1.Instance.InstanceMessage.Code\x12\x0f\n\x07message\x18\x02 \x01(\t">\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12 \n\x1cZONE_DISTRIBUTION_UNBALANCED\x10\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"o\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x1a\n\x16PERFORMING_MAINTENANCE\x10\x05:c\xeaA`\n memcache.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}"\xef\x01\n\x11MaintenancePolicy\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12Y\n\x19weekly_maintenance_window\x18\x04 \x03(\x0b21.google.cloud.memcache.v1.WeeklyMaintenanceWindowB\x03\xe0A\x02"\xa6\x01\n\x17WeeklyMaintenanceWindow\x12(\n\x03day\x18\x01 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02\x12/\n\nstart_time\x18\x02 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x02\x120\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02"\xbe\x01\n\x13MaintenanceSchedule\x123\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x16schedule_deadline_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\xe2\x02\n\x1cRescheduleMaintenanceRequest\x12:\n\x08instance\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x12c\n\x0freschedule_type\x18\x02 \x01(\x0e2E.google.cloud.memcache.v1.RescheduleMaintenanceRequest.RescheduleTypeB\x03\xe0A\x02\x121\n\rschedule_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"n\n\x0eRescheduleType\x12\x1f\n\x1bRESCHEDULE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tIMMEDIATE\x10\x01\x12\x19\n\x15NEXT_AVAILABLE_WINDOW\x10\x02\x12\x11\n\rSPECIFIC_TIME\x10\x03"\x9a\x01\n\x14ListInstancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"|\n\x15ListInstancesResponse\x125\n\tinstances\x18\x01 \x03(\x0b2".google.cloud.memcache.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x12GetInstanceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance"\xa7\x01\n\x15CreateInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x08instance\x18\x03 \x01(\x0b2".google.cloud.memcache.v1.InstanceB\x03\xe0A\x02"\x88\x01\n\x15UpdateInstanceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x129\n\x08instance\x18\x02 \x01(\x0b2".google.cloud.memcache.v1.InstanceB\x03\xe0A\x02"O\n\x15DeleteInstanceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance"u\n\x16ApplyParametersRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x12\x10\n\x08node_ids\x18\x02 \x03(\t\x12\x11\n\tapply_all\x18\x03 \x01(\x08"\xc9\x01\n\x17UpdateParametersRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12@\n\nparameters\x18\x03 \x01(\x0b2,.google.cloud.memcache.v1.MemcacheParameters"\x9e\x01\n\x12MemcacheParameters\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12H\n\x06params\x18\x03 \x03(\x0b28.google.cloud.memcache.v1.MemcacheParameters.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xf9\x01\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rstatus_detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10cancel_requested\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"\xcf\x01\n\x10LocationMetadata\x12\\\n\x0favailable_zones\x18\x01 \x03(\x0b2>.google.cloud.memcache.v1.LocationMetadata.AvailableZonesEntryB\x03\xe0A\x03\x1a]\n\x13AvailableZonesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.cloud.memcache.v1.ZoneMetadata:\x028\x01"\x0e\n\x0cZoneMetadata*E\n\x0fMemcacheVersion\x12 \n\x1cMEMCACHE_VERSION_UNSPECIFIED\x10\x00\x12\x10\n\x0cMEMCACHE_1_5\x10\x012\xc5\x10\n\rCloudMemcache\x12\xb0\x01\n\rListInstances\x12..google.cloud.memcache.v1.ListInstancesRequest\x1a/.google.cloud.memcache.v1.ListInstancesResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances\x12\x9d\x01\n\x0bGetInstance\x12,.google.cloud.memcache.v1.GetInstanceRequest\x1a".google.cloud.memcache.v1.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x12\x92\x02\n\x0eCreateInstance\x12/.google.cloud.memcache.v1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"\xaf\x01\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance\x12\x94\x02\n\x0eUpdateInstance\x12/.google.cloud.memcache.v1.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation"\xb1\x01\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance\x12\xa0\x02\n\x10UpdateParameters\x121.google.cloud.memcache.v1.UpdateParametersRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x1bname,update_mask,parameters\x82\xd3\xe4\x93\x02C2>/v1/{name=projects/*/locations/*/instances/*}:updateParameters:\x01*\x12\xe5\x01\n\x0eDeleteInstance\x12/.google.cloud.memcache.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaAC\n\x15google.protobuf.Empty\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}\x12\x99\x02\n\x0fApplyParameters\x120.google.cloud.memcache.v1.ApplyParametersRequest\x1a\x1d.google.longrunning.Operation"\xb4\x01\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x17name,node_ids,apply_all\x82\xd3\xe4\x93\x02B"=/v1/{name=projects/*/locations/*/instances/*}:applyParameters:\x01*\x12\xc0\x02\n\x15RescheduleMaintenance\x126.google.cloud.memcache.v1.RescheduleMaintenanceRequest\x1a\x1d.google.longrunning.Operation"\xcf\x01\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA(instance, reschedule_type, schedule_time\x82\xd3\xe4\x93\x02L"G/v1/{instance=projects/*/locations/*/instances/*}:rescheduleMaintenance:\x01*\x1aK\xcaA\x17memcache.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBn\n\x1ccom.google.cloud.memcache.v1B\x12CloudMemcacheProtoP\x01Z8cloud.google.com/go/memcache/apiv1/memcachepb;memcachepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.memcache.v1.cloud_memcache_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.memcache.v1B\x12CloudMemcacheProtoP\x01Z8cloud.google.com/go/memcache/apiv1/memcachepb;memcachepb'
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
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['reschedule_type']._loaded_options = None
    _globals['_RESCHEDULEMAINTENANCEREQUEST'].fields_by_name['reschedule_type']._serialized_options = b'\xe0A\x02'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_APPLYPARAMETERSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_APPLYPARAMETERSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n memcache.googleapis.com/Instance'
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPARAMETERSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
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
    _globals['_CLOUDMEMCACHE'].methods_by_name['ListInstances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances'
    _globals['_CLOUDMEMCACHE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_CLOUDMEMCACHE'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['CreateInstance']._serialized_options = b'\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateInstance']._serialized_options = b'\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance'
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateParameters']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['UpdateParameters']._serialized_options = b'\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x1bname,update_mask,parameters\x82\xd3\xe4\x93\x02C2>/v1/{name=projects/*/locations/*/instances/*}:updateParameters:\x01*'
    _globals['_CLOUDMEMCACHE'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaAC\n\x15google.protobuf.Empty\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_CLOUDMEMCACHE'].methods_by_name['ApplyParameters']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['ApplyParameters']._serialized_options = b'\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA\x17name,node_ids,apply_all\x82\xd3\xe4\x93\x02B"=/v1/{name=projects/*/locations/*/instances/*}:applyParameters:\x01*'
    _globals['_CLOUDMEMCACHE'].methods_by_name['RescheduleMaintenance']._loaded_options = None
    _globals['_CLOUDMEMCACHE'].methods_by_name['RescheduleMaintenance']._serialized_options = b'\xcaAO\n!google.cloud.memcache.v1.Instance\x12*google.cloud.memcache.v1.OperationMetadata\xdaA(instance, reschedule_type, schedule_time\x82\xd3\xe4\x93\x02L"G/v1/{instance=projects/*/locations/*/instances/*}:rescheduleMaintenance:\x01*'
    _globals['_MEMCACHEVERSION']._serialized_start = 4801
    _globals['_MEMCACHEVERSION']._serialized_end = 4870
    _globals['_INSTANCE']._serialized_start = 385
    _globals['_INSTANCE']._serialized_end = 2125
    _globals['_INSTANCE_NODECONFIG']._serialized_start = 1321
    _globals['_INSTANCE_NODECONFIG']._serialized_end = 1386
    _globals['_INSTANCE_NODE']._serialized_start = 1389
    _globals['_INSTANCE_NODE']._serialized_end = 1692
    _globals['_INSTANCE_NODE_STATE']._serialized_start = 1609
    _globals['_INSTANCE_NODE_STATE']._serialized_end = 1692
    _globals['_INSTANCE_INSTANCEMESSAGE']._serialized_start = 1695
    _globals['_INSTANCE_INSTANCEMESSAGE']._serialized_end = 1864
    _globals['_INSTANCE_INSTANCEMESSAGE_CODE']._serialized_start = 1802
    _globals['_INSTANCE_INSTANCEMESSAGE_CODE']._serialized_end = 1864
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 1866
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 1911
    _globals['_INSTANCE_STATE']._serialized_start = 1913
    _globals['_INSTANCE_STATE']._serialized_end = 2024
    _globals['_MAINTENANCEPOLICY']._serialized_start = 2128
    _globals['_MAINTENANCEPOLICY']._serialized_end = 2367
    _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_start = 2370
    _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_end = 2536
    _globals['_MAINTENANCESCHEDULE']._serialized_start = 2539
    _globals['_MAINTENANCESCHEDULE']._serialized_end = 2729
    _globals['_RESCHEDULEMAINTENANCEREQUEST']._serialized_start = 2732
    _globals['_RESCHEDULEMAINTENANCEREQUEST']._serialized_end = 3086
    _globals['_RESCHEDULEMAINTENANCEREQUEST_RESCHEDULETYPE']._serialized_start = 2976
    _globals['_RESCHEDULEMAINTENANCEREQUEST_RESCHEDULETYPE']._serialized_end = 3086
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 3089
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 3243
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 3245
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 3369
    _globals['_GETINSTANCEREQUEST']._serialized_start = 3371
    _globals['_GETINSTANCEREQUEST']._serialized_end = 3447
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 3450
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 3617
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 3620
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 3756
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 3758
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 3837
    _globals['_APPLYPARAMETERSREQUEST']._serialized_start = 3839
    _globals['_APPLYPARAMETERSREQUEST']._serialized_end = 3956
    _globals['_UPDATEPARAMETERSREQUEST']._serialized_start = 3959
    _globals['_UPDATEPARAMETERSREQUEST']._serialized_end = 4160
    _globals['_MEMCACHEPARAMETERS']._serialized_start = 4163
    _globals['_MEMCACHEPARAMETERS']._serialized_end = 4321
    _globals['_MEMCACHEPARAMETERS_PARAMSENTRY']._serialized_start = 4276
    _globals['_MEMCACHEPARAMETERS_PARAMSENTRY']._serialized_end = 4321
    _globals['_OPERATIONMETADATA']._serialized_start = 4324
    _globals['_OPERATIONMETADATA']._serialized_end = 4573
    _globals['_LOCATIONMETADATA']._serialized_start = 4576
    _globals['_LOCATIONMETADATA']._serialized_end = 4783
    _globals['_LOCATIONMETADATA_AVAILABLEZONESENTRY']._serialized_start = 4690
    _globals['_LOCATIONMETADATA_AVAILABLEZONESENTRY']._serialized_end = 4783
    _globals['_ZONEMETADATA']._serialized_start = 4785
    _globals['_ZONEMETADATA']._serialized_end = 4799
    _globals['_CLOUDMEMCACHE']._serialized_start = 4873
    _globals['_CLOUDMEMCACHE']._serialized_end = 6990