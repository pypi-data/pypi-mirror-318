"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/cloudtrace/v2/tracing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.cloudtrace.v2 import trace_pb2 as google_dot_devtools_dot_cloudtrace_dot_v2_dot_trace__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/cloudtrace/v2/tracing.proto\x12\x1dgoogle.devtools.cloudtrace.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/devtools/cloudtrace/v2/trace.proto\x1a\x1bgoogle/protobuf/empty.proto"\x94\x01\n\x16BatchWriteSpansRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x127\n\x05spans\x18\x02 \x03(\x0b2#.google.devtools.cloudtrace.v2.SpanB\x03\xe0A\x022\xba\x03\n\x0cTraceService\x12\xa1\x01\n\x0fBatchWriteSpans\x125.google.devtools.cloudtrace.v2.BatchWriteSpansRequest\x1a\x16.google.protobuf.Empty"?\xdaA\nname,spans\x82\xd3\xe4\x93\x02,"\'/v2/{name=projects/*}/traces:batchWrite:\x01*\x12\x89\x01\n\nCreateSpan\x12#.google.devtools.cloudtrace.v2.Span\x1a#.google.devtools.cloudtrace.v2.Span"1\x82\xd3\xe4\x93\x02+"&/v2/{name=projects/*/traces/*/spans/*}:\x01*\x1az\xcaA\x19cloudtrace.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.appendB\xaf\x01\n!com.google.devtools.cloudtrace.v2B\x0cTracingProtoP\x01Z/cloud.google.com/go/trace/apiv2/tracepb;tracepb\xaa\x02\x15Google.Cloud.Trace.V2\xca\x02\x15Google\\Cloud\\Trace\\V2\xea\x02\x18Google::Cloud::Trace::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.cloudtrace.v2.tracing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.devtools.cloudtrace.v2B\x0cTracingProtoP\x01Z/cloud.google.com/go/trace/apiv2/tracepb;tracepb\xaa\x02\x15Google.Cloud.Trace.V2\xca\x02\x15Google\\Cloud\\Trace\\V2\xea\x02\x18Google::Cloud::Trace::V2'
    _globals['_BATCHWRITESPANSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_BATCHWRITESPANSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_BATCHWRITESPANSREQUEST'].fields_by_name['spans']._loaded_options = None
    _globals['_BATCHWRITESPANSREQUEST'].fields_by_name['spans']._serialized_options = b'\xe0A\x02'
    _globals['_TRACESERVICE']._loaded_options = None
    _globals['_TRACESERVICE']._serialized_options = b'\xcaA\x19cloudtrace.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append'
    _globals['_TRACESERVICE'].methods_by_name['BatchWriteSpans']._loaded_options = None
    _globals['_TRACESERVICE'].methods_by_name['BatchWriteSpans']._serialized_options = b'\xdaA\nname,spans\x82\xd3\xe4\x93\x02,"\'/v2/{name=projects/*}/traces:batchWrite:\x01*'
    _globals['_TRACESERVICE'].methods_by_name['CreateSpan']._loaded_options = None
    _globals['_TRACESERVICE'].methods_by_name['CreateSpan']._serialized_options = b'\x82\xd3\xe4\x93\x02+"&/v2/{name=projects/*/traces/*/spans/*}:\x01*'
    _globals['_BATCHWRITESPANSREQUEST']._serialized_start = 266
    _globals['_BATCHWRITESPANSREQUEST']._serialized_end = 414
    _globals['_TRACESERVICE']._serialized_start = 417
    _globals['_TRACESERVICE']._serialized_end = 859