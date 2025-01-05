"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/completion_stats.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1/completion_stats.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto"\x98\x01\n\x0fCompletionStats\x12\x1d\n\x10successful_count\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cfailed_count\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x1d\n\x10incomplete_count\x18\x03 \x01(\x03B\x03\xe0A\x03\x12,\n\x1fsuccessful_forecast_point_count\x18\x05 \x01(\x03B\x03\xe0A\x03B\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14CompletionStatsProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.completion_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14CompletionStatsProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_COMPLETIONSTATS'].fields_by_name['successful_count']._loaded_options = None
    _globals['_COMPLETIONSTATS'].fields_by_name['successful_count']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONSTATS'].fields_by_name['failed_count']._loaded_options = None
    _globals['_COMPLETIONSTATS'].fields_by_name['failed_count']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONSTATS'].fields_by_name['incomplete_count']._loaded_options = None
    _globals['_COMPLETIONSTATS'].fields_by_name['incomplete_count']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONSTATS'].fields_by_name['successful_forecast_point_count']._loaded_options = None
    _globals['_COMPLETIONSTATS'].fields_by_name['successful_forecast_point_count']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONSTATS']._serialized_start = 115
    _globals['_COMPLETIONSTATS']._serialized_end = 267