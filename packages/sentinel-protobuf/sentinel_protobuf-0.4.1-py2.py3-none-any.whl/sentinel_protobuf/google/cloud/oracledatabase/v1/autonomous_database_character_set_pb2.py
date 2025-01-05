"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/autonomous_database_character_set.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/cloud/oracledatabase/v1/autonomous_database_character_set.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x88\x04\n\x1eAutonomousDatabaseCharacterSet\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12p\n\x12character_set_type\x18\x02 \x01(\x0e2O.google.cloud.oracledatabase.v1.AutonomousDatabaseCharacterSet.CharacterSetTypeB\x03\xe0A\x03\x12\x1a\n\rcharacter_set\x18\x03 \x01(\tB\x03\xe0A\x03"R\n\x10CharacterSetType\x12"\n\x1eCHARACTER_SET_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DATABASE\x10\x01\x12\x0c\n\x08NATIONAL\x10\x02:\xf0\x01\xeaA\xec\x01\n<oracledatabase.googleapis.com/AutonomousDatabaseCharacterSet\x12kprojects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}*\x1fautonomousDatabaseCharacterSets2\x1eautonomousDatabaseCharacterSetB\xfd\x01\n"com.google.cloud.oracledatabase.v1B#AutonomousDatabaseCharacterSetProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.autonomous_database_character_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B#AutonomousDatabaseCharacterSetProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_AUTONOMOUSDATABASECHARACTERSET'].fields_by_name['name']._loaded_options = None
    _globals['_AUTONOMOUSDATABASECHARACTERSET'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTONOMOUSDATABASECHARACTERSET'].fields_by_name['character_set_type']._loaded_options = None
    _globals['_AUTONOMOUSDATABASECHARACTERSET'].fields_by_name['character_set_type']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASECHARACTERSET'].fields_by_name['character_set']._loaded_options = None
    _globals['_AUTONOMOUSDATABASECHARACTERSET'].fields_by_name['character_set']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASECHARACTERSET']._loaded_options = None
    _globals['_AUTONOMOUSDATABASECHARACTERSET']._serialized_options = b'\xeaA\xec\x01\n<oracledatabase.googleapis.com/AutonomousDatabaseCharacterSet\x12kprojects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}*\x1fautonomousDatabaseCharacterSets2\x1eautonomousDatabaseCharacterSet'
    _globals['_AUTONOMOUSDATABASECHARACTERSET']._serialized_start = 167
    _globals['_AUTONOMOUSDATABASECHARACTERSET']._serialized_end = 687
    _globals['_AUTONOMOUSDATABASECHARACTERSET_CHARACTERSETTYPE']._serialized_start = 362
    _globals['_AUTONOMOUSDATABASECHARACTERSET_CHARACTERSETTYPE']._serialized_end = 444