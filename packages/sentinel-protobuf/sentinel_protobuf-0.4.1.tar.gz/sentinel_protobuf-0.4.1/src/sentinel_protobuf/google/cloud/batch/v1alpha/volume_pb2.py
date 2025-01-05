"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/batch/v1alpha/volume.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/batch/v1alpha/volume.proto\x12\x1agoogle.cloud.batch.v1alpha"\xe6\x01\n\x06Volume\x12.\n\x03nfs\x18\x01 \x01(\x0b2\x1f.google.cloud.batch.v1alpha.NFSH\x00\x120\n\x02pd\x18\x02 \x01(\x0b2\x1e.google.cloud.batch.v1alpha.PDB\x02\x18\x01H\x00\x12.\n\x03gcs\x18\x03 \x01(\x0b2\x1f.google.cloud.batch.v1alpha.GCSH\x00\x12\x15\n\x0bdevice_name\x18\x06 \x01(\tH\x00\x12\x12\n\nmount_path\x18\x04 \x01(\t\x12\x15\n\rmount_options\x18\x05 \x03(\tB\x08\n\x06source"*\n\x03NFS\x12\x0e\n\x06server\x18\x01 \x01(\t\x12\x13\n\x0bremote_path\x18\x02 \x01(\t"8\n\x02PD\x12\x0c\n\x04disk\x18\x01 \x01(\t\x12\x0e\n\x06device\x18\x02 \x01(\t\x12\x14\n\x08existing\x18\x03 \x01(\x08B\x02\x18\x01"\x1a\n\x03GCS\x12\x13\n\x0bremote_path\x18\x01 \x01(\tB\xc5\x01\n\x1ecom.google.cloud.batch.v1alphaB\x0bVolumeProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1alpha.volume_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.batch.v1alphaB\x0bVolumeProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alpha'
    _globals['_VOLUME'].fields_by_name['pd']._loaded_options = None
    _globals['_VOLUME'].fields_by_name['pd']._serialized_options = b'\x18\x01'
    _globals['_PD'].fields_by_name['existing']._loaded_options = None
    _globals['_PD'].fields_by_name['existing']._serialized_options = b'\x18\x01'
    _globals['_VOLUME']._serialized_start = 72
    _globals['_VOLUME']._serialized_end = 302
    _globals['_NFS']._serialized_start = 304
    _globals['_NFS']._serialized_end = 346
    _globals['_PD']._serialized_start = 348
    _globals['_PD']._serialized_end = 404
    _globals['_GCS']._serialized_start = 406
    _globals['_GCS']._serialized_end = 432