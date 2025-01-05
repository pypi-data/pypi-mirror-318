"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/db_server.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/oracledatabase/v1/db_server.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc3\x02\n\x08DbServer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12K\n\nproperties\x18\x03 \x01(\x0b22.google.cloud.oracledatabase.v1.DbServerPropertiesB\x03\xe0A\x01:\xbb\x01\xeaA\xb7\x01\n&oracledatabase.googleapis.com/DbServer\x12xprojects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}/dbServers/{db_server}*\tdbServers2\x08dbServer"\xd3\x03\n\x12DbServerProperties\x12\x11\n\x04ocid\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nocpu_count\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1b\n\x0emax_ocpu_count\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x1b\n\x0ememory_size_gb\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12max_memory_size_gb\x18\x05 \x01(\x05B\x03\xe0A\x01\x12$\n\x17db_node_storage_size_gb\x18\x06 \x01(\x05B\x03\xe0A\x01\x12(\n\x1bmax_db_node_storage_size_gb\x18\x07 \x01(\x05B\x03\xe0A\x01\x12\x15\n\x08vm_count\x18\x08 \x01(\x05B\x03\xe0A\x01\x12L\n\x05state\x18\t \x01(\x0e28.google.cloud.oracledatabase.v1.DbServerProperties.StateB\x03\xe0A\x03\x12\x18\n\x0bdb_node_ids\x18\n \x03(\tB\x03\xe0A\x03"g\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\r\n\tAVAILABLE\x10\x02\x12\x0f\n\x0bUNAVAILABLE\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x0b\n\x07DELETED\x10\x05B\xe7\x01\n"com.google.cloud.oracledatabase.v1B\rDbServerProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.db_server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\rDbServerProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_DBSERVER'].fields_by_name['name']._loaded_options = None
    _globals['_DBSERVER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DBSERVER'].fields_by_name['display_name']._loaded_options = None
    _globals['_DBSERVER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVER'].fields_by_name['properties']._loaded_options = None
    _globals['_DBSERVER'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVER']._loaded_options = None
    _globals['_DBSERVER']._serialized_options = b'\xeaA\xb7\x01\n&oracledatabase.googleapis.com/DbServer\x12xprojects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}/dbServers/{db_server}*\tdbServers2\x08dbServer'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['ocid']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['ocid']._serialized_options = b'\xe0A\x03'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['ocpu_count']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['ocpu_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['max_ocpu_count']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['max_ocpu_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['memory_size_gb']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['memory_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['max_memory_size_gb']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['max_memory_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['db_node_storage_size_gb']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['db_node_storage_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['max_db_node_storage_size_gb']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['max_db_node_storage_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['vm_count']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['vm_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['state']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DBSERVERPROPERTIES'].fields_by_name['db_node_ids']._loaded_options = None
    _globals['_DBSERVERPROPERTIES'].fields_by_name['db_node_ids']._serialized_options = b'\xe0A\x03'
    _globals['_DBSERVER']._serialized_start = 143
    _globals['_DBSERVER']._serialized_end = 466
    _globals['_DBSERVERPROPERTIES']._serialized_start = 469
    _globals['_DBSERVERPROPERTIES']._serialized_end = 936
    _globals['_DBSERVERPROPERTIES_STATE']._serialized_start = 833
    _globals['_DBSERVERPROPERTIES_STATE']._serialized_end = 936