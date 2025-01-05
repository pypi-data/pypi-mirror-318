"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/admin/database/v1/common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/spanner/admin/database/v1/common.proto\x12 google.spanner.admin.database.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x8b\x01\n\x11OperationProgress\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8f\x01\n\x10EncryptionConfig\x12<\n\x0ckms_key_name\x18\x02 \x01(\tB&\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12=\n\rkms_key_names\x18\x03 \x03(\tB&\xfaA#\n!cloudkms.googleapis.com/CryptoKey"\xc2\x02\n\x0eEncryptionInfo\x12S\n\x0fencryption_type\x18\x03 \x01(\x0e25.google.spanner.admin.database.v1.EncryptionInfo.TypeB\x03\xe0A\x03\x122\n\x11encryption_status\x18\x04 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12I\n\x0fkms_key_version\x18\x02 \x01(\tB0\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion"\\\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19GOOGLE_DEFAULT_ENCRYPTION\x10\x01\x12\x1f\n\x1bCUSTOMER_MANAGED_ENCRYPTION\x10\x02*\\\n\x0fDatabaseDialect\x12 \n\x1cDATABASE_DIALECT_UNSPECIFIED\x10\x00\x12\x17\n\x13GOOGLE_STANDARD_SQL\x10\x01\x12\x0e\n\nPOSTGRESQL\x10\x02B\xa2\x04\n$com.google.spanner.admin.database.v1B\x0bCommonProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}\xeaA\xa6\x01\n(cloudkms.googleapis.com/CryptoKeyVersion\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.admin.database.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.spanner.admin.database.v1B\x0bCommonProtoP\x01ZFcloud.google.com/go/spanner/admin/database/apiv1/databasepb;databasepb\xaa\x02&Google.Cloud.Spanner.Admin.Database.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Database\\V1\xea\x02+Google::Cloud::Spanner::Admin::Database::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}\xeaA\xa6\x01\n(cloudkms.googleapis.com/CryptoKeyVersion\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['kms_key_name']._serialized_options = b'\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['kms_key_names']._serialized_options = b'\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_type']._loaded_options = None
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_type']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_status']._loaded_options = None
    _globals['_ENCRYPTIONINFO'].fields_by_name['encryption_status']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONINFO'].fields_by_name['kms_key_version']._loaded_options = None
    _globals['_ENCRYPTIONINFO'].fields_by_name['kms_key_version']._serialized_options = b'\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion'
    _globals['_DATABASEDIALECT']._serialized_start = 814
    _globals['_DATABASEDIALECT']._serialized_end = 906
    _globals['_OPERATIONPROGRESS']._serialized_start = 202
    _globals['_OPERATIONPROGRESS']._serialized_end = 341
    _globals['_ENCRYPTIONCONFIG']._serialized_start = 344
    _globals['_ENCRYPTIONCONFIG']._serialized_end = 487
    _globals['_ENCRYPTIONINFO']._serialized_start = 490
    _globals['_ENCRYPTIONINFO']._serialized_end = 812
    _globals['_ENCRYPTIONINFO_TYPE']._serialized_start = 720
    _globals['_ENCRYPTIONINFO_TYPE']._serialized_end = 812