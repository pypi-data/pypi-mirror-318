"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/vm_cluster.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/oracledatabase/v1/vm_cluster.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto"\xd6\x05\n\x0eCloudVmCluster\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12`\n\x16exadata_infrastructure\x18\x02 \x01(\tB@\xe0A\x02\xfaA:\n8oracledatabase.googleapis.com/CloudExadataInfrastructure\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fgcp_oracle_zone\x18\x0c \x01(\tB\x03\xe0A\x03\x12Q\n\nproperties\x18\x06 \x01(\x0b28.google.cloud.oracledatabase.v1.CloudVmClusterPropertiesB\x03\xe0A\x01\x12O\n\x06labels\x18\x07 \x03(\x0b2:.google.cloud.oracledatabase.v1.CloudVmCluster.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04cidr\x18\t \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12backup_subnet_cidr\x18\n \x01(\tB\x03\xe0A\x02\x127\n\x07network\x18\x0b \x01(\tB&\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x9f\x01\xeaA\x9b\x01\n,oracledatabase.googleapis.com/CloudVmCluster\x12Jprojects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}*\x0fcloudVmClusters2\x0ecloudVmCluster"\x9c\x0c\n\x18CloudVmClusterProperties\x12\x11\n\x04ocid\x18\x01 \x01(\tB\x03\xe0A\x03\x12_\n\x0clicense_type\x18\x02 \x01(\x0e2D.google.cloud.oracledatabase.v1.CloudVmClusterProperties.LicenseTypeB\x03\xe0A\x02\x12\x17\n\ngi_version\x18\x03 \x01(\tB\x03\xe0A\x01\x12-\n\ttime_zone\x18\x04 \x01(\x0b2\x15.google.type.TimeZoneB\x03\xe0A\x01\x12\x1c\n\x0fssh_public_keys\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x17\n\nnode_count\x18\x06 \x01(\x05B\x03\xe0A\x01\x12\x12\n\x05shape\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x17\n\nocpu_count\x18\x08 \x01(\x02B\x03\xe0A\x01\x12\x1b\n\x0ememory_size_gb\x18\t \x01(\x05B\x03\xe0A\x01\x12$\n\x17db_node_storage_size_gb\x18\n \x01(\x05B\x03\xe0A\x01\x12\x1c\n\x0fstorage_size_gb\x18\x0b \x01(\x05B\x03\xe0A\x03\x12!\n\x14data_storage_size_tb\x18\x0c \x01(\x01B\x03\xe0A\x01\x12e\n\x0fdisk_redundancy\x18\r \x01(\x0e2G.google.cloud.oracledatabase.v1.CloudVmClusterProperties.DiskRedundancyB\x03\xe0A\x01\x12%\n\x18sparse_diskgroup_enabled\x18\x0e \x01(\x08B\x03\xe0A\x01\x12!\n\x14local_backup_enabled\x18\x0f \x01(\x08B\x03\xe0A\x01\x12\x1c\n\x0fhostname_prefix\x18\x10 \x01(\tB\x03\xe0A\x01\x12g\n#diagnostics_data_collection_options\x18\x13 \x01(\x0b25.google.cloud.oracledatabase.v1.DataCollectionOptionsB\x03\xe0A\x01\x12R\n\x05state\x18\x14 \x01(\x0e2>.google.cloud.oracledatabase.v1.CloudVmClusterProperties.StateB\x03\xe0A\x03\x12#\n\x16scan_listener_port_tcp\x18\x15 \x01(\x05B\x03\xe0A\x03\x12\'\n\x1ascan_listener_port_tcp_ssl\x18\x16 \x01(\x05B\x03\xe0A\x03\x12\x13\n\x06domain\x18\x17 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08scan_dns\x18\x18 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08hostname\x18\x19 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0ecpu_core_count\x18\x1a \x01(\x05B\x03\xe0A\x02\x12\x1b\n\x0esystem_version\x18\x1b \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bscan_ip_ids\x18\x1c \x03(\tB\x03\xe0A\x03\x12\x1f\n\x12scan_dns_record_id\x18\x1d \x01(\tB\x03\xe0A\x03\x12\x14\n\x07oci_url\x18\x1e \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fdb_server_ocids\x18\x1f \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0ecompartment_id\x18  \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fdns_listener_ip\x18# \x01(\tB\x03\xe0A\x03\x12\x19\n\x0ccluster_name\x18$ \x01(\tB\x03\xe0A\x01"]\n\x0bLicenseType\x12\x1c\n\x18LICENSE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10LICENSE_INCLUDED\x10\x01\x12\x1a\n\x16BRING_YOUR_OWN_LICENSE\x10\x02"G\n\x0eDiskRedundancy\x12\x1f\n\x1bDISK_REDUNDANCY_UNSPECIFIED\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\n\n\x06NORMAL\x10\x02"\x97\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\r\n\tAVAILABLE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0f\n\x0bTERMINATING\x10\x04\x12\x0e\n\nTERMINATED\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\x1b\n\x17MAINTENANCE_IN_PROGRESS\x10\x07"\x8c\x01\n\x15DataCollectionOptions\x12\'\n\x1adiagnostics_events_enabled\x18\x01 \x01(\x08B\x03\xe0A\x01\x12&\n\x19health_monitoring_enabled\x18\x02 \x01(\x08B\x03\xe0A\x01\x12"\n\x15incident_logs_enabled\x18\x03 \x01(\x08B\x03\xe0A\x01B\xed\x01\n"com.google.cloud.oracledatabase.v1B\x13CloudVmClusterProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.vm_cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x13CloudVmClusterProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_CLOUDVMCLUSTER_LABELSENTRY']._loaded_options = None
    _globals['_CLOUDVMCLUSTER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['name']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['exadata_infrastructure']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['exadata_infrastructure']._serialized_options = b'\xe0A\x02\xfaA:\n8oracledatabase.googleapis.com/CloudExadataInfrastructure'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['display_name']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['gcp_oracle_zone']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['gcp_oracle_zone']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['properties']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['labels']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['cidr']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['cidr']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['backup_subnet_cidr']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['backup_subnet_cidr']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDVMCLUSTER'].fields_by_name['network']._loaded_options = None
    _globals['_CLOUDVMCLUSTER'].fields_by_name['network']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_CLOUDVMCLUSTER']._loaded_options = None
    _globals['_CLOUDVMCLUSTER']._serialized_options = b'\xeaA\x9b\x01\n,oracledatabase.googleapis.com/CloudVmCluster\x12Jprojects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}*\x0fcloudVmClusters2\x0ecloudVmCluster'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['ocid']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['ocid']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['license_type']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['license_type']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['gi_version']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['gi_version']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['time_zone']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['ssh_public_keys']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['ssh_public_keys']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['node_count']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['node_count']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['shape']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['shape']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['ocpu_count']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['ocpu_count']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['memory_size_gb']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['memory_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['db_node_storage_size_gb']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['db_node_storage_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['storage_size_gb']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['storage_size_gb']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['data_storage_size_tb']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['data_storage_size_tb']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['disk_redundancy']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['disk_redundancy']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['sparse_diskgroup_enabled']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['sparse_diskgroup_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['local_backup_enabled']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['local_backup_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['hostname_prefix']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['hostname_prefix']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['diagnostics_data_collection_options']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['diagnostics_data_collection_options']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['state']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_listener_port_tcp']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_listener_port_tcp']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_listener_port_tcp_ssl']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_listener_port_tcp_ssl']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['domain']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['domain']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_dns']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_dns']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['hostname']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['hostname']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['cpu_core_count']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['cpu_core_count']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['system_version']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['system_version']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_ip_ids']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_ip_ids']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_dns_record_id']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['scan_dns_record_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['oci_url']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['oci_url']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['db_server_ocids']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['db_server_ocids']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['compartment_id']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['compartment_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['dns_listener_ip']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['dns_listener_ip']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['cluster_name']._loaded_options = None
    _globals['_CLOUDVMCLUSTERPROPERTIES'].fields_by_name['cluster_name']._serialized_options = b'\xe0A\x01'
    _globals['_DATACOLLECTIONOPTIONS'].fields_by_name['diagnostics_events_enabled']._loaded_options = None
    _globals['_DATACOLLECTIONOPTIONS'].fields_by_name['diagnostics_events_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_DATACOLLECTIONOPTIONS'].fields_by_name['health_monitoring_enabled']._loaded_options = None
    _globals['_DATACOLLECTIONOPTIONS'].fields_by_name['health_monitoring_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_DATACOLLECTIONOPTIONS'].fields_by_name['incident_logs_enabled']._loaded_options = None
    _globals['_DATACOLLECTIONOPTIONS'].fields_by_name['incident_logs_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDVMCLUSTER']._serialized_start = 205
    _globals['_CLOUDVMCLUSTER']._serialized_end = 931
    _globals['_CLOUDVMCLUSTER_LABELSENTRY']._serialized_start = 724
    _globals['_CLOUDVMCLUSTER_LABELSENTRY']._serialized_end = 769
    _globals['_CLOUDVMCLUSTERPROPERTIES']._serialized_start = 934
    _globals['_CLOUDVMCLUSTERPROPERTIES']._serialized_end = 2498
    _globals['_CLOUDVMCLUSTERPROPERTIES_LICENSETYPE']._serialized_start = 2178
    _globals['_CLOUDVMCLUSTERPROPERTIES_LICENSETYPE']._serialized_end = 2271
    _globals['_CLOUDVMCLUSTERPROPERTIES_DISKREDUNDANCY']._serialized_start = 2273
    _globals['_CLOUDVMCLUSTERPROPERTIES_DISKREDUNDANCY']._serialized_end = 2344
    _globals['_CLOUDVMCLUSTERPROPERTIES_STATE']._serialized_start = 2347
    _globals['_CLOUDVMCLUSTERPROPERTIES_STATE']._serialized_end = 2498
    _globals['_DATACOLLECTIONOPTIONS']._serialized_start = 2501
    _globals['_DATACOLLECTIONOPTIONS']._serialized_end = 2641