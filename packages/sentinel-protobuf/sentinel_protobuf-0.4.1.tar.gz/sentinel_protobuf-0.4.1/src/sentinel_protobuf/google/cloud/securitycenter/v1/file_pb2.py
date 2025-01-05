"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/file.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/securitycenter/v1/file.proto\x12\x1egoogle.cloud.securitycenter.v1"\xf0\x01\n\x04File\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x0e\n\x06sha256\x18\x03 \x01(\t\x12\x13\n\x0bhashed_size\x18\x04 \x01(\x03\x12\x18\n\x10partially_hashed\x18\x05 \x01(\x08\x12\x10\n\x08contents\x18\x06 \x01(\t\x12@\n\tdisk_path\x18\x07 \x01(\x0b2-.google.cloud.securitycenter.v1.File.DiskPath\x1a9\n\x08DiskPath\x12\x16\n\x0epartition_uuid\x18\x01 \x01(\t\x12\x15\n\rrelative_path\x18\x02 \x01(\tB\xe3\x01\n"com.google.cloud.securitycenter.v1B\tFileProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\tFileProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_FILE']._serialized_start = 78
    _globals['_FILE']._serialized_end = 318
    _globals['_FILE_DISKPATH']._serialized_start = 261
    _globals['_FILE_DISKPATH']._serialized_end = 318