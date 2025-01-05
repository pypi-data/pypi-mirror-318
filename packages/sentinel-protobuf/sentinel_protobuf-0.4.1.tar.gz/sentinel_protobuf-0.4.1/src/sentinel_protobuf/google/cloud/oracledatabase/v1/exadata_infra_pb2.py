"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/exadata_infra.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.oracledatabase.v1 import common_pb2 as google_dot_cloud_dot_oracledatabase_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from .....google.type import month_pb2 as google_dot_type_dot_month__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/oracledatabase/v1/exadata_infra.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/oracledatabase/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x17google/type/month.proto"\x84\x05\n\x1aCloudExadataInfrastructure\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fgcp_oracle_zone\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eentitlement_id\x18\x04 \x01(\tB\x03\xe0A\x03\x12]\n\nproperties\x18\x05 \x01(\x0b2D.google.cloud.oracledatabase.v1.CloudExadataInfrastructurePropertiesB\x03\xe0A\x01\x12[\n\x06labels\x18\x06 \x03(\x0b2F.google.cloud.oracledatabase.v1.CloudExadataInfrastructure.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xdb\x01\xeaA\xd7\x01\n8oracledatabase.googleapis.com/CloudExadataInfrastructure\x12bprojects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}*\x1bcloudExadataInfrastructures2\x1acloudExadataInfrastructure"\xa6\n\n$CloudExadataInfrastructureProperties\x12\x11\n\x04ocid\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rcompute_count\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1a\n\rstorage_count\x18\x03 \x01(\x05B\x03\xe0A\x01\x12"\n\x15total_storage_size_gb\x18\x04 \x01(\x05B\x03\xe0A\x01\x12&\n\x19available_storage_size_gb\x18\x05 \x01(\x05B\x03\xe0A\x03\x12R\n\x12maintenance_window\x18\x06 \x01(\x0b21.google.cloud.oracledatabase.v1.MaintenanceWindowB\x03\xe0A\x01\x12^\n\x05state\x18\x07 \x01(\x0e2J.google.cloud.oracledatabase.v1.CloudExadataInfrastructureProperties.StateB\x03\xe0A\x03\x12\x12\n\x05shape\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07oci_url\x18\t \x01(\tB\x03\xe0A\x03\x12\x16\n\tcpu_count\x18\n \x01(\x05B\x03\xe0A\x03\x12\x1a\n\rmax_cpu_count\x18\x0b \x01(\x05B\x03\xe0A\x03\x12\x1b\n\x0ememory_size_gb\x18\x0c \x01(\x05B\x03\xe0A\x03\x12\x1a\n\rmax_memory_gb\x18\r \x01(\x05B\x03\xe0A\x03\x12$\n\x17db_node_storage_size_gb\x18\x0e \x01(\x05B\x03\xe0A\x03\x12(\n\x1bmax_db_node_storage_size_gb\x18\x0f \x01(\x05B\x03\xe0A\x03\x12!\n\x14data_storage_size_tb\x18\x10 \x01(\x01B\x03\xe0A\x03\x12 \n\x13max_data_storage_tb\x18\x11 \x01(\x01B\x03\xe0A\x03\x12$\n\x17activated_storage_count\x18\x12 \x01(\x05B\x03\xe0A\x03\x12%\n\x18additional_storage_count\x18\x13 \x01(\x05B\x03\xe0A\x03\x12\x1e\n\x11db_server_version\x18\x14 \x01(\tB\x03\xe0A\x03\x12#\n\x16storage_server_version\x18\x15 \x01(\tB\x03\xe0A\x03\x12$\n\x17next_maintenance_run_id\x18\x16 \x01(\tB\x03\xe0A\x03\x12B\n\x19next_maintenance_run_time\x18\x17 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n"next_security_maintenance_run_time\x18\x18 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12O\n\x11customer_contacts\x18\x19 \x03(\x0b2/.google.cloud.oracledatabase.v1.CustomerContactB\x03\xe0A\x01\x12+\n\x1emonthly_storage_server_version\x18\x1a \x01(\tB\x03\xe0A\x03\x12&\n\x19monthly_db_server_version\x18\x1b \x01(\tB\x03\xe0A\x03"\x97\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\r\n\tAVAILABLE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0f\n\x0bTERMINATING\x10\x04\x12\x0e\n\nTERMINATED\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\x1b\n\x17MAINTENANCE_IN_PROGRESS\x10\x07"\xa5\x05\n\x11MaintenanceWindow\x12f\n\npreference\x18\x01 \x01(\x0e2M.google.cloud.oracledatabase.v1.MaintenanceWindow.MaintenanceWindowPreferenceB\x03\xe0A\x01\x12\'\n\x06months\x18\x02 \x03(\x0e2\x12.google.type.MonthB\x03\xe0A\x01\x12\x1b\n\x0eweeks_of_month\x18\x03 \x03(\x05B\x03\xe0A\x01\x121\n\x0cdays_of_week\x18\x04 \x03(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x01\x12\x19\n\x0chours_of_day\x18\x05 \x03(\x05B\x03\xe0A\x01\x12\x1b\n\x0elead_time_week\x18\x06 \x01(\x05B\x03\xe0A\x01\x12Z\n\rpatching_mode\x18\x07 \x01(\x0e2>.google.cloud.oracledatabase.v1.MaintenanceWindow.PatchingModeB\x03\xe0A\x01\x12\'\n\x1acustom_action_timeout_mins\x18\x08 \x01(\x05B\x03\xe0A\x01\x12-\n is_custom_action_timeout_enabled\x18\t \x01(\x08B\x03\xe0A\x01"v\n\x1bMaintenanceWindowPreference\x12-\n)MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED\x10\x00\x12\x15\n\x11CUSTOM_PREFERENCE\x10\x01\x12\x11\n\rNO_PREFERENCE\x10\x02"K\n\x0cPatchingMode\x12\x1d\n\x19PATCHING_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ROLLING\x10\x01\x12\x0f\n\x0bNON_ROLLING\x10\x02B\xf9\x01\n"com.google.cloud.oracledatabase.v1B\x1fCloudExadataInfrastructureProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.exadata_infra_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x1fCloudExadataInfrastructureProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_CLOUDEXADATAINFRASTRUCTURE_LABELSENTRY']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['name']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['display_name']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['gcp_oracle_zone']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['gcp_oracle_zone']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['entitlement_id']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['entitlement_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['properties']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['labels']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTURE']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTURE']._serialized_options = b'\xeaA\xd7\x01\n8oracledatabase.googleapis.com/CloudExadataInfrastructure\x12bprojects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}*\x1bcloudExadataInfrastructures2\x1acloudExadataInfrastructure'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['ocid']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['ocid']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['compute_count']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['compute_count']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['storage_count']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['storage_count']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['total_storage_size_gb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['total_storage_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['available_storage_size_gb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['available_storage_size_gb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['maintenance_window']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['maintenance_window']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['state']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['shape']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['shape']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['oci_url']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['oci_url']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['cpu_count']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['cpu_count']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_cpu_count']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_cpu_count']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['memory_size_gb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['memory_size_gb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_memory_gb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_memory_gb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['db_node_storage_size_gb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['db_node_storage_size_gb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_db_node_storage_size_gb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_db_node_storage_size_gb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['data_storage_size_tb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['data_storage_size_tb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_data_storage_tb']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['max_data_storage_tb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['activated_storage_count']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['activated_storage_count']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['additional_storage_count']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['additional_storage_count']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['db_server_version']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['db_server_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['storage_server_version']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['storage_server_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['next_maintenance_run_id']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['next_maintenance_run_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['next_maintenance_run_time']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['next_maintenance_run_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['next_security_maintenance_run_time']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['next_security_maintenance_run_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['customer_contacts']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['customer_contacts']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['monthly_storage_server_version']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['monthly_storage_server_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['monthly_db_server_version']._loaded_options = None
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES'].fields_by_name['monthly_db_server_version']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['preference']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['preference']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['months']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['months']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['weeks_of_month']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['weeks_of_month']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['days_of_week']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['days_of_week']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['hours_of_day']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['hours_of_day']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['lead_time_week']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['lead_time_week']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['patching_mode']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['patching_mode']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['custom_action_timeout_mins']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['custom_action_timeout_mins']._serialized_options = b'\xe0A\x01'
    _globals['_MAINTENANCEWINDOW'].fields_by_name['is_custom_action_timeout_enabled']._loaded_options = None
    _globals['_MAINTENANCEWINDOW'].fields_by_name['is_custom_action_timeout_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDEXADATAINFRASTRUCTURE']._serialized_start = 279
    _globals['_CLOUDEXADATAINFRASTRUCTURE']._serialized_end = 923
    _globals['_CLOUDEXADATAINFRASTRUCTURE_LABELSENTRY']._serialized_start = 656
    _globals['_CLOUDEXADATAINFRASTRUCTURE_LABELSENTRY']._serialized_end = 701
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES']._serialized_start = 926
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES']._serialized_end = 2244
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES_STATE']._serialized_start = 2093
    _globals['_CLOUDEXADATAINFRASTRUCTUREPROPERTIES_STATE']._serialized_end = 2244
    _globals['_MAINTENANCEWINDOW']._serialized_start = 2247
    _globals['_MAINTENANCEWINDOW']._serialized_end = 2924
    _globals['_MAINTENANCEWINDOW_MAINTENANCEWINDOWPREFERENCE']._serialized_start = 2729
    _globals['_MAINTENANCEWINDOW_MAINTENANCEWINDOWPREFERENCE']._serialized_end = 2847
    _globals['_MAINTENANCEWINDOW_PATCHINGMODE']._serialized_start = 2849
    _globals['_MAINTENANCEWINDOW_PATCHINGMODE']._serialized_end = 2924