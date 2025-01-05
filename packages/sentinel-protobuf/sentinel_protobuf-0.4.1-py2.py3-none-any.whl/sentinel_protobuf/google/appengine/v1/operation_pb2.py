"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/operation.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/appengine/v1/operation.proto\x12\x13google.appengine.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xb2\x02\n\x13OperationMetadataV1\x12\x0e\n\x06method\x18\x01 \x01(\t\x12/\n\x0binsert_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x0e\n\x06target\x18\x05 \x01(\t\x12\x19\n\x11ephemeral_message\x18\x06 \x01(\t\x12\x0f\n\x07warning\x18\x07 \x03(\t\x12O\n\x17create_version_metadata\x18\x08 \x01(\x0b2,.google.appengine.v1.CreateVersionMetadataV1H\x00B\x11\n\x0fmethod_metadata"1\n\x17CreateVersionMetadataV1\x12\x16\n\x0ecloud_build_id\x18\x01 \x01(\tB\xbf\x01\n\x17com.google.appengine.v1B\x0eOperationProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.operation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x0eOperationProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_OPERATIONMETADATAV1']._serialized_start = 94
    _globals['_OPERATIONMETADATAV1']._serialized_end = 400
    _globals['_CREATEVERSIONMETADATAV1']._serialized_start = 402
    _globals['_CREATEVERSIONMETADATAV1']._serialized_end = 451