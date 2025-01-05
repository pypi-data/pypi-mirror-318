"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/gkebackup/v1/common.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"%\n\nNamespaces\x12\x17\n\nnamespaces\x18\x01 \x03(\tB\x03\xe0A\x01";\n\x0eNamespacedName\x12\x16\n\tnamespace\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x01"[\n\x0fNamespacedNames\x12H\n\x10namespaced_names\x18\x01 \x03(\x0b2).google.cloud.gkebackup.v1.NamespacedNameB\x03\xe0A\x01"Z\n\rEncryptionKey\x12I\n\x16gcp_kms_encryption_key\x18\x01 \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey"T\n\x0eVolumeTypeEnum"B\n\nVolumeType\x12\x1b\n\x17VOLUME_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13GCE_PERSISTENT_DISK\x10\x01B\xc2\x01\n\x1dcom.google.cloud.gkebackup.v1B\x0bCommonProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x0bCommonProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_NAMESPACES'].fields_by_name['namespaces']._loaded_options = None
    _globals['_NAMESPACES'].fields_by_name['namespaces']._serialized_options = b'\xe0A\x01'
    _globals['_NAMESPACEDNAME'].fields_by_name['namespace']._loaded_options = None
    _globals['_NAMESPACEDNAME'].fields_by_name['namespace']._serialized_options = b'\xe0A\x01'
    _globals['_NAMESPACEDNAME'].fields_by_name['name']._loaded_options = None
    _globals['_NAMESPACEDNAME'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_NAMESPACEDNAMES'].fields_by_name['namespaced_names']._loaded_options = None
    _globals['_NAMESPACEDNAMES'].fields_by_name['namespaced_names']._serialized_options = b'\xe0A\x01'
    _globals['_ENCRYPTIONKEY'].fields_by_name['gcp_kms_encryption_key']._loaded_options = None
    _globals['_ENCRYPTIONKEY'].fields_by_name['gcp_kms_encryption_key']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_NAMESPACES']._serialized_start = 129
    _globals['_NAMESPACES']._serialized_end = 166
    _globals['_NAMESPACEDNAME']._serialized_start = 168
    _globals['_NAMESPACEDNAME']._serialized_end = 227
    _globals['_NAMESPACEDNAMES']._serialized_start = 229
    _globals['_NAMESPACEDNAMES']._serialized_end = 320
    _globals['_ENCRYPTIONKEY']._serialized_start = 322
    _globals['_ENCRYPTIONKEY']._serialized_end = 412
    _globals['_VOLUMETYPEENUM']._serialized_start = 414
    _globals['_VOLUMETYPEENUM']._serialized_end = 498
    _globals['_VOLUMETYPEENUM_VOLUMETYPE']._serialized_start = 432
    _globals['_VOLUMETYPEENUM_VOLUMETYPE']._serialized_end = 498