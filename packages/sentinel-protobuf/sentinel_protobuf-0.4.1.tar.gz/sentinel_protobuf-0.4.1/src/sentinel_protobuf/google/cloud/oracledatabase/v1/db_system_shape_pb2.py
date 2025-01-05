"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/db_system_shape.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/oracledatabase/v1/db_system_shape.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc5\x04\n\rDbSystemShape\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x12\n\x05shape\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0emin_node_count\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x1b\n\x0emax_node_count\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x1e\n\x11min_storage_count\x18\x05 \x01(\x05B\x03\xe0A\x01\x12\x1e\n\x11max_storage_count\x18\x06 \x01(\x05B\x03\xe0A\x01\x12*\n\x1davailable_core_count_per_node\x18\x07 \x01(\x05B\x03\xe0A\x01\x12)\n\x1cavailable_memory_per_node_gb\x18\x08 \x01(\x05B\x03\xe0A\x01\x12&\n\x19available_data_storage_tb\x18\t \x01(\x05B\x03\xe0A\x01\x12$\n\x17min_core_count_per_node\x18\n \x01(\x05B\x03\xe0A\x01\x12#\n\x16min_memory_per_node_gb\x18\x0b \x01(\x05B\x03\xe0A\x01\x12,\n\x1fmin_db_node_storage_per_node_gb\x18\x0c \x01(\x05B\x03\xe0A\x01:\x9a\x01\xeaA\x96\x01\n+oracledatabase.googleapis.com/DbSystemShape\x12Hprojects/{project}/locations/{location}/dbSystemShapes/{db_system_shape}*\x0edbSystemShapes2\rdbSystemShapeB\xec\x01\n"com.google.cloud.oracledatabase.v1B\x12DbSystemShapeProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.db_system_shape_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x12DbSystemShapeProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['name']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['shape']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['shape']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_node_count']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_node_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['max_node_count']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['max_node_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_storage_count']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_storage_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['max_storage_count']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['max_storage_count']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['available_core_count_per_node']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['available_core_count_per_node']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['available_memory_per_node_gb']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['available_memory_per_node_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['available_data_storage_tb']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['available_data_storage_tb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_core_count_per_node']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_core_count_per_node']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_memory_per_node_gb']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_memory_per_node_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_db_node_storage_per_node_gb']._loaded_options = None
    _globals['_DBSYSTEMSHAPE'].fields_by_name['min_db_node_storage_per_node_gb']._serialized_options = b'\xe0A\x01'
    _globals['_DBSYSTEMSHAPE']._loaded_options = None
    _globals['_DBSYSTEMSHAPE']._serialized_options = b'\xeaA\x96\x01\n+oracledatabase.googleapis.com/DbSystemShape\x12Hprojects/{project}/locations/{location}/dbSystemShapes/{db_system_shape}*\x0edbSystemShapes2\rdbSystemShape'
    _globals['_DBSYSTEMSHAPE']._serialized_start = 149
    _globals['_DBSYSTEMSHAPE']._serialized_end = 730