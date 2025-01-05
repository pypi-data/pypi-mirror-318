"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/run/v2/status.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/cloud/run/v2/status.proto\x12\x13google.cloud.run.v2";\n\x15RevisionScalingStatus\x12"\n\x1adesired_min_instance_count\x18\x01 \x01(\x05BS\n\x17com.google.cloud.run.v2B\x0bStatusProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.run.v2.status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.run.v2B\x0bStatusProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb'
    _globals['_REVISIONSCALINGSTATUS']._serialized_start = 57
    _globals['_REVISIONSCALINGSTATUS']._serialized_end = 116