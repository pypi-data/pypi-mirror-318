"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/batch/v1/volume.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/batch/v1/volume.proto\x12\x15google.cloud.batch.v1"\xaa\x01\n\x06Volume\x12)\n\x03nfs\x18\x01 \x01(\x0b2\x1a.google.cloud.batch.v1.NFSH\x00\x12)\n\x03gcs\x18\x03 \x01(\x0b2\x1a.google.cloud.batch.v1.GCSH\x00\x12\x15\n\x0bdevice_name\x18\x06 \x01(\tH\x00\x12\x12\n\nmount_path\x18\x04 \x01(\t\x12\x15\n\rmount_options\x18\x05 \x03(\tB\x08\n\x06source"*\n\x03NFS\x12\x0e\n\x06server\x18\x01 \x01(\t\x12\x13\n\x0bremote_path\x18\x02 \x01(\t"\x1a\n\x03GCS\x12\x13\n\x0bremote_path\x18\x01 \x01(\tB\xac\x01\n\x19com.google.cloud.batch.v1B\x0bVolumeProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1.volume_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.batch.v1B\x0bVolumeProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1'
    _globals['_VOLUME']._serialized_start = 62
    _globals['_VOLUME']._serialized_end = 232
    _globals['_NFS']._serialized_start = 234
    _globals['_NFS']._serialized_end = 276
    _globals['_GCS']._serialized_start = 278
    _globals['_GCS']._serialized_end = 304