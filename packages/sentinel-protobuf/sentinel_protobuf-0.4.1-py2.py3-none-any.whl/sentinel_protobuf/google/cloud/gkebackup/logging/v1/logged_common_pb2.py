"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/logging/v1/logged_common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/gkebackup/logging/v1/logged_common.proto\x12!google.cloud.gkebackup.logging.v1" \n\nNamespaces\x12\x12\n\nnamespaces\x18\x01 \x03(\t"1\n\x0eNamespacedName\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"^\n\x0fNamespacedNames\x12K\n\x10namespaced_names\x18\x01 \x03(\x0b21.google.cloud.gkebackup.logging.v1.NamespacedName"/\n\rEncryptionKey\x12\x1e\n\x16gcp_kms_encryption_key\x18\x01 \x01(\tB\xe9\x01\n!google.cloud.gkebackup.logging.v1B\x11LoggedCommonProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logged_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.gkebackup.logging.v1B\x11LoggedCommonProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_NAMESPACES']._serialized_start = 92
    _globals['_NAMESPACES']._serialized_end = 124
    _globals['_NAMESPACEDNAME']._serialized_start = 126
    _globals['_NAMESPACEDNAME']._serialized_end = 175
    _globals['_NAMESPACEDNAMES']._serialized_start = 177
    _globals['_NAMESPACEDNAMES']._serialized_end = 271
    _globals['_ENCRYPTIONKEY']._serialized_start = 273
    _globals['_ENCRYPTIONKEY']._serialized_end = 320