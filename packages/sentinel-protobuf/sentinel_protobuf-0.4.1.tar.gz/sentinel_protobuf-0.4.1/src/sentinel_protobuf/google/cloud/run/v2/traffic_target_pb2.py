"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/run/v2/traffic_target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/run/v2/traffic_target.proto\x12\x13google.cloud.run.v2\x1a\x19google/api/resource.proto"\xa1\x01\n\rTrafficTarget\x12>\n\x04type\x18\x01 \x01(\x0e20.google.cloud.run.v2.TrafficTargetAllocationType\x122\n\x08revision\x18\x02 \x01(\tB \xfaA\x1d\n\x1brun.googleapis.com/Revision\x12\x0f\n\x07percent\x18\x03 \x01(\x05\x12\x0b\n\x03tag\x18\x04 \x01(\t"\xb4\x01\n\x13TrafficTargetStatus\x12>\n\x04type\x18\x01 \x01(\x0e20.google.cloud.run.v2.TrafficTargetAllocationType\x122\n\x08revision\x18\x02 \x01(\tB \xfaA\x1d\n\x1brun.googleapis.com/Revision\x12\x0f\n\x07percent\x18\x03 \x01(\x05\x12\x0b\n\x03tag\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x05 \x01(\t*\xa5\x01\n\x1bTrafficTargetAllocationType\x12.\n*TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED\x10\x00\x12)\n%TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST\x10\x01\x12+\n\'TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION\x10\x02BZ\n\x17com.google.cloud.run.v2B\x12TrafficTargetProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.run.v2.traffic_target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.run.v2B\x12TrafficTargetProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb'
    _globals['_TRAFFICTARGET'].fields_by_name['revision']._loaded_options = None
    _globals['_TRAFFICTARGET'].fields_by_name['revision']._serialized_options = b'\xfaA\x1d\n\x1brun.googleapis.com/Revision'
    _globals['_TRAFFICTARGETSTATUS'].fields_by_name['revision']._loaded_options = None
    _globals['_TRAFFICTARGETSTATUS'].fields_by_name['revision']._serialized_options = b'\xfaA\x1d\n\x1brun.googleapis.com/Revision'
    _globals['_TRAFFICTARGETALLOCATIONTYPE']._serialized_start = 440
    _globals['_TRAFFICTARGETALLOCATIONTYPE']._serialized_end = 605
    _globals['_TRAFFICTARGET']._serialized_start = 93
    _globals['_TRAFFICTARGET']._serialized_end = 254
    _globals['_TRAFFICTARGETSTATUS']._serialized_start = 257
    _globals['_TRAFFICTARGETSTATUS']._serialized_end = 437