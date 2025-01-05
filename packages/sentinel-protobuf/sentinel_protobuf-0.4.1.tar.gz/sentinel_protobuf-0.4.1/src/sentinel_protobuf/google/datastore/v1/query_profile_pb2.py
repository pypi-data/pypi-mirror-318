"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1/query_profile.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/datastore/v1/query_profile.proto\x12\x13google.datastore.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"&\n\x0eExplainOptions\x12\x14\n\x07analyze\x18\x01 \x01(\x08B\x03\xe0A\x01"\x86\x01\n\x0eExplainMetrics\x126\n\x0cplan_summary\x18\x01 \x01(\x0b2 .google.datastore.v1.PlanSummary\x12<\n\x0fexecution_stats\x18\x02 \x01(\x0b2#.google.datastore.v1.ExecutionStats"<\n\x0bPlanSummary\x12-\n\x0cindexes_used\x18\x01 \x03(\x0b2\x17.google.protobuf.Struct"\xa8\x01\n\x0eExecutionStats\x12\x18\n\x10results_returned\x18\x01 \x01(\x03\x125\n\x12execution_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12\x17\n\x0fread_operations\x18\x04 \x01(\x03\x12,\n\x0bdebug_stats\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB\xc2\x01\n\x17com.google.datastore.v1B\x11QueryProfileProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1.query_profile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.datastore.v1B\x11QueryProfileProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1'
    _globals['_EXPLAINOPTIONS'].fields_by_name['analyze']._loaded_options = None
    _globals['_EXPLAINOPTIONS'].fields_by_name['analyze']._serialized_options = b'\xe0A\x01'
    _globals['_EXPLAINOPTIONS']._serialized_start = 159
    _globals['_EXPLAINOPTIONS']._serialized_end = 197
    _globals['_EXPLAINMETRICS']._serialized_start = 200
    _globals['_EXPLAINMETRICS']._serialized_end = 334
    _globals['_PLANSUMMARY']._serialized_start = 336
    _globals['_PLANSUMMARY']._serialized_end = 396
    _globals['_EXECUTIONSTATS']._serialized_start = 399
    _globals['_EXECUTIONSTATS']._serialized_end = 567