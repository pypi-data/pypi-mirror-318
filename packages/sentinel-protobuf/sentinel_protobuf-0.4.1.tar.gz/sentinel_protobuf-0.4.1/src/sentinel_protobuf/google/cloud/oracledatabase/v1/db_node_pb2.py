"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/db_node.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/oracledatabase/v1/db_node.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x82\x02\n\x06DbNode\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12I\n\nproperties\x18\x03 \x01(\x0b20.google.cloud.oracledatabase.v1.DbNodePropertiesB\x03\xe0A\x01:\x99\x01\xeaA\x95\x01\n$oracledatabase.googleapis.com/DbNode\x12\\projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}*\x07dbNodes2\x06dbNode"\xc0\x03\n\x10DbNodeProperties\x12\x11\n\x04ocid\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nocpu_count\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x16\n\x0ememory_size_gb\x18\x03 \x01(\x05\x12$\n\x17db_node_storage_size_gb\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x1b\n\x0edb_server_ocid\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08hostname\x18\x08 \x01(\tB\x03\xe0A\x01\x12J\n\x05state\x18\t \x01(\x0e26.google.cloud.oracledatabase.v1.DbNodeProperties.StateB\x03\xe0A\x03\x12\x1c\n\x14total_cpu_core_count\x18\n \x01(\x05"\xa3\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\r\n\tAVAILABLE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0c\n\x08STARTING\x10\x06\x12\x0f\n\x0bTERMINATING\x10\x07\x12\x0e\n\nTERMINATED\x10\x08\x12\n\n\x06FAILED\x10\tB\xe5\x01\n"com.google.cloud.oracledatabase.v1B\x0bDbNodeProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.db_node_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x0bDbNodeProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_DBNODE'].fields_by_name['name']._loaded_options = None
    _globals['_DBNODE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DBNODE'].fields_by_name['properties']._loaded_options = None
    _globals['_DBNODE'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_DBNODE']._loaded_options = None
    _globals['_DBNODE']._serialized_options = b'\xeaA\x95\x01\n$oracledatabase.googleapis.com/DbNode\x12\\projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}*\x07dbNodes2\x06dbNode'
    _globals['_DBNODEPROPERTIES'].fields_by_name['ocid']._loaded_options = None
    _globals['_DBNODEPROPERTIES'].fields_by_name['ocid']._serialized_options = b'\xe0A\x03'
    _globals['_DBNODEPROPERTIES'].fields_by_name['ocpu_count']._loaded_options = None
    _globals['_DBNODEPROPERTIES'].fields_by_name['ocpu_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBNODEPROPERTIES'].fields_by_name['db_node_storage_size_gb']._loaded_options = None
    _globals['_DBNODEPROPERTIES'].fields_by_name['db_node_storage_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBNODEPROPERTIES'].fields_by_name['db_server_ocid']._loaded_options = None
    _globals['_DBNODEPROPERTIES'].fields_by_name['db_server_ocid']._serialized_options = b'\xe0A\x01'
    _globals['_DBNODEPROPERTIES'].fields_by_name['hostname']._loaded_options = None
    _globals['_DBNODEPROPERTIES'].fields_by_name['hostname']._serialized_options = b'\xe0A\x01'
    _globals['_DBNODEPROPERTIES'].fields_by_name['state']._loaded_options = None
    _globals['_DBNODEPROPERTIES'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DBNODE']._serialized_start = 141
    _globals['_DBNODE']._serialized_end = 399
    _globals['_DBNODEPROPERTIES']._serialized_start = 402
    _globals['_DBNODEPROPERTIES']._serialized_end = 850
    _globals['_DBNODEPROPERTIES_STATE']._serialized_start = 687
    _globals['_DBNODEPROPERTIES_STATE']._serialized_end = 850