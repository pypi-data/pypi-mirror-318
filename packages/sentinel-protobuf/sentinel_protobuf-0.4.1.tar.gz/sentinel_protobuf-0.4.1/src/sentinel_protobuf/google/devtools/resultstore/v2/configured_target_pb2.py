"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/configured_target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from .....google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/resultstore/v2/configured_target.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto\x1a)google/devtools/resultstore/v2/file.proto\x1a\x1egoogle/protobuf/duration.proto"\xfa\x04\n\x10ConfiguredTarget\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x02id\x18\x02 \x01(\x0b23.google.devtools.resultstore.v2.ConfiguredTarget.Id\x12K\n\x11status_attributes\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.StatusAttributes\x126\n\x06timing\x18\x04 \x01(\x0b2&.google.devtools.resultstore.v2.Timing\x12Q\n\x0ftest_attributes\x18\x06 \x01(\x0b28.google.devtools.resultstore.v2.ConfiguredTestAttributes\x12<\n\nproperties\x18\x07 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x123\n\x05files\x18\x08 \x03(\x0b2$.google.devtools.resultstore.v2.File\x1aH\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x11\n\ttarget_id\x18\x02 \x01(\t\x12\x18\n\x10configuration_id\x18\x03 \x01(\t:\x81\x01\xeaA~\n+resultstore.googleapis.com/ConfiguredTarget\x12Oinvocations/{invocation}/targets/{target}/configuredTargets/{configured_target}"\x83\x01\n\x18ConfiguredTestAttributes\x12\x17\n\x0ftotal_run_count\x18\x02 \x01(\x05\x12\x19\n\x11total_shard_count\x18\x03 \x01(\x05\x123\n\x10timeout_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x88\x01\n"com.google.devtools.resultstore.v2B\x15ConfiguredTargetProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.configured_target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x15ConfiguredTargetProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_CONFIGUREDTARGET']._loaded_options = None
    _globals['_CONFIGUREDTARGET']._serialized_options = b'\xeaA~\n+resultstore.googleapis.com/ConfiguredTarget\x12Oinvocations/{invocation}/targets/{target}/configuredTargets/{configured_target}'
    _globals['_CONFIGUREDTARGET']._serialized_start = 238
    _globals['_CONFIGUREDTARGET']._serialized_end = 872
    _globals['_CONFIGUREDTARGET_ID']._serialized_start = 668
    _globals['_CONFIGUREDTARGET_ID']._serialized_end = 740
    _globals['_CONFIGUREDTESTATTRIBUTES']._serialized_start = 875
    _globals['_CONFIGUREDTESTATTRIBUTES']._serialized_end = 1006