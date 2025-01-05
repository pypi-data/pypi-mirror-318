"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/cloudtrace/v1/trace.proto')
_sym_db = _symbol_database.Default()
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/devtools/cloudtrace/v1/trace.proto\x12\x1dgoogle.devtools.cloudtrace.v1\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"f\n\x05Trace\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08trace_id\x18\x02 \x01(\t\x127\n\x05spans\x18\x03 \x03(\x0b2(.google.devtools.cloudtrace.v1.TraceSpan">\n\x06Traces\x124\n\x06traces\x18\x01 \x03(\x0b2$.google.devtools.cloudtrace.v1.Trace"\xa2\x03\n\tTraceSpan\x12\x0f\n\x07span_id\x18\x01 \x01(\x06\x12?\n\x04kind\x18\x02 \x01(\x0e21.google.devtools.cloudtrace.v1.TraceSpan.SpanKind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1b\n\x0eparent_span_id\x18\x06 \x01(\x06B\x03\xe0A\x01\x12D\n\x06labels\x18\x07 \x03(\x0b24.google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"E\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x0e\n\nRPC_SERVER\x10\x01\x12\x0e\n\nRPC_CLIENT\x10\x02"\x80\x03\n\x11ListTracesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x04view\x18\x02 \x01(\x0e29.google.devtools.cloudtrace.v1.ListTracesRequest.ViewTypeB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x12\n\npage_token\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x06filter\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x08 \x01(\tB\x03\xe0A\x01"N\n\x08ViewType\x12\x19\n\x15VIEW_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MINIMAL\x10\x01\x12\x0c\n\x08ROOTSPAN\x10\x02\x12\x0c\n\x08COMPLETE\x10\x03"c\n\x12ListTracesResponse\x124\n\x06traces\x18\x01 \x03(\x0b2$.google.devtools.cloudtrace.v1.Trace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"A\n\x0fGetTraceRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08trace_id\x18\x02 \x01(\tB\x03\xe0A\x02"i\n\x12PatchTracesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12:\n\x06traces\x18\x02 \x01(\x0b2%.google.devtools.cloudtrace.v1.TracesB\x03\xe0A\x022\xb5\x05\n\x0cTraceService\x12\xa8\x01\n\nListTraces\x120.google.devtools.cloudtrace.v1.ListTracesRequest\x1a1.google.devtools.cloudtrace.v1.ListTracesResponse"5\xdaA\nproject_id\x82\xd3\xe4\x93\x02"\x12 /v1/projects/{project_id}/traces\x12\xab\x01\n\x08GetTrace\x12..google.devtools.cloudtrace.v1.GetTraceRequest\x1a$.google.devtools.cloudtrace.v1.Trace"I\xdaA\x13project_id,trace_id\x82\xd3\xe4\x93\x02-\x12+/v1/projects/{project_id}/traces/{trace_id}\x12\x9e\x01\n\x0bPatchTraces\x121.google.devtools.cloudtrace.v1.PatchTracesRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x11project_id,traces\x82\xd3\xe4\x93\x02*2 /v1/projects/{project_id}/traces:\x06traces\x1a\xaa\x01\xcaA\x19cloudtrace.googleapis.com\xd2A\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/trace.readonlyB\xad\x01\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\x01Z/cloud.google.com/go/trace/apiv1/tracepb;tracepb\xaa\x02\x15Google.Cloud.Trace.V1\xca\x02\x15Google\\Cloud\\Trace\\V1\xea\x02\x18Google::Cloud::Trace::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.cloudtrace.v1.trace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\x01Z/cloud.google.com/go/trace/apiv1/tracepb;tracepb\xaa\x02\x15Google.Cloud.Trace.V1\xca\x02\x15Google\\Cloud\\Trace\\V1\xea\x02\x18Google::Cloud::Trace::V1'
    _globals['_TRACESPAN_LABELSENTRY']._loaded_options = None
    _globals['_TRACESPAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TRACESPAN'].fields_by_name['parent_span_id']._loaded_options = None
    _globals['_TRACESPAN'].fields_by_name['parent_span_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTRACESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTTRACESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTRACESREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTTRACESREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTRACESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTRACESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTRACESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTRACESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTRACESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTTRACESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETTRACEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETTRACEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRACEREQUEST'].fields_by_name['trace_id']._loaded_options = None
    _globals['_GETTRACEREQUEST'].fields_by_name['trace_id']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHTRACESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_PATCHTRACESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHTRACESREQUEST'].fields_by_name['traces']._loaded_options = None
    _globals['_PATCHTRACESREQUEST'].fields_by_name['traces']._serialized_options = b'\xe0A\x02'
    _globals['_TRACESERVICE']._loaded_options = None
    _globals['_TRACESERVICE']._serialized_options = b'\xcaA\x19cloudtrace.googleapis.com\xd2A\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/trace.readonly'
    _globals['_TRACESERVICE'].methods_by_name['ListTraces']._loaded_options = None
    _globals['_TRACESERVICE'].methods_by_name['ListTraces']._serialized_options = b'\xdaA\nproject_id\x82\xd3\xe4\x93\x02"\x12 /v1/projects/{project_id}/traces'
    _globals['_TRACESERVICE'].methods_by_name['GetTrace']._loaded_options = None
    _globals['_TRACESERVICE'].methods_by_name['GetTrace']._serialized_options = b'\xdaA\x13project_id,trace_id\x82\xd3\xe4\x93\x02-\x12+/v1/projects/{project_id}/traces/{trace_id}'
    _globals['_TRACESERVICE'].methods_by_name['PatchTraces']._loaded_options = None
    _globals['_TRACESERVICE'].methods_by_name['PatchTraces']._serialized_options = b'\xdaA\x11project_id,traces\x82\xd3\xe4\x93\x02*2 /v1/projects/{project_id}/traces:\x06traces'
    _globals['_TRACE']._serialized_start = 226
    _globals['_TRACE']._serialized_end = 328
    _globals['_TRACES']._serialized_start = 330
    _globals['_TRACES']._serialized_end = 392
    _globals['_TRACESPAN']._serialized_start = 395
    _globals['_TRACESPAN']._serialized_end = 813
    _globals['_TRACESPAN_LABELSENTRY']._serialized_start = 697
    _globals['_TRACESPAN_LABELSENTRY']._serialized_end = 742
    _globals['_TRACESPAN_SPANKIND']._serialized_start = 744
    _globals['_TRACESPAN_SPANKIND']._serialized_end = 813
    _globals['_LISTTRACESREQUEST']._serialized_start = 816
    _globals['_LISTTRACESREQUEST']._serialized_end = 1200
    _globals['_LISTTRACESREQUEST_VIEWTYPE']._serialized_start = 1122
    _globals['_LISTTRACESREQUEST_VIEWTYPE']._serialized_end = 1200
    _globals['_LISTTRACESRESPONSE']._serialized_start = 1202
    _globals['_LISTTRACESRESPONSE']._serialized_end = 1301
    _globals['_GETTRACEREQUEST']._serialized_start = 1303
    _globals['_GETTRACEREQUEST']._serialized_end = 1368
    _globals['_PATCHTRACESREQUEST']._serialized_start = 1370
    _globals['_PATCHTRACESREQUEST']._serialized_end = 1475
    _globals['_TRACESERVICE']._serialized_start = 1478
    _globals['_TRACESERVICE']._serialized_end = 2171