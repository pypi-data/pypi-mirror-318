"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/location_metadata.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/oracledatabase/v1/location_metadata.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto"1\n\x10LocationMetadata\x12\x1d\n\x10gcp_oracle_zones\x18\x02 \x03(\tB\x03\xe0A\x03B\xef\x01\n"com.google.cloud.oracledatabase.v1B\x15LocationMetadataProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.location_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x15LocationMetadataProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_LOCATIONMETADATA'].fields_by_name['gcp_oracle_zones']._loaded_options = None
    _globals['_LOCATIONMETADATA'].fields_by_name['gcp_oracle_zones']._serialized_options = b'\xe0A\x03'
    _globals['_LOCATIONMETADATA']._serialized_start = 123
    _globals['_LOCATIONMETADATA']._serialized_end = 172