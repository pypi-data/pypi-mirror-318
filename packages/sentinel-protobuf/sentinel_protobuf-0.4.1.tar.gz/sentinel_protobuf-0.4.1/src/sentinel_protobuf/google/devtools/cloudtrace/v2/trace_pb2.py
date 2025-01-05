"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/cloudtrace/v2/trace.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/devtools/cloudtrace/v2/trace.proto\x12\x1dgoogle.devtools.cloudtrace.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\xf1\x11\n\x04Span\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07span_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\x0eparent_span_id\x18\x03 \x01(\t\x12K\n\x0cdisplay_name\x18\x04 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableStringB\x03\xe0A\x02\x123\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x121\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12B\n\nattributes\x18\x07 \x01(\x0b2..google.devtools.cloudtrace.v2.Span.Attributes\x12>\n\x0bstack_trace\x18\x08 \x01(\x0b2).google.devtools.cloudtrace.v2.StackTrace\x12C\n\x0btime_events\x18\t \x01(\x0b2..google.devtools.cloudtrace.v2.Span.TimeEvents\x128\n\x05links\x18\n \x01(\x0b2).google.devtools.cloudtrace.v2.Span.Links\x12\'\n\x06status\x18\x0b \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x01\x12D\n\x1bsame_process_as_parent_span\x18\x0c \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12:\n\x10child_span_count\x18\r \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x01\x12D\n\tspan_kind\x18\x0e \x01(\x0e2,.google.devtools.cloudtrace.v2.Span.SpanKindB\x03\xe0A\x01\x1a\xeb\x01\n\nAttributes\x12W\n\rattribute_map\x18\x01 \x03(\x0b2@.google.devtools.cloudtrace.v2.Span.Attributes.AttributeMapEntry\x12 \n\x18dropped_attributes_count\x18\x02 \x01(\x05\x1ab\n\x11AttributeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.devtools.cloudtrace.v2.AttributeValue:\x028\x01\x1a\xdf\x04\n\tTimeEvent\x12(\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12N\n\nannotation\x18\x02 \x01(\x0b28.google.devtools.cloudtrace.v2.Span.TimeEvent.AnnotationH\x00\x12S\n\rmessage_event\x18\x03 \x01(\x0b2:.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEventH\x00\x1a\x97\x01\n\nAnnotation\x12E\n\x0bdescription\x18\x01 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString\x12B\n\nattributes\x18\x02 \x01(\x0b2..google.devtools.cloudtrace.v2.Span.Attributes\x1a\xdf\x01\n\x0cMessageEvent\x12M\n\x04type\x18\x01 \x01(\x0e2?.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEvent.Type\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x1f\n\x17uncompressed_size_bytes\x18\x03 \x01(\x03\x12\x1d\n\x15compressed_size_bytes\x18\x04 \x01(\x03"4\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04SENT\x10\x01\x12\x0c\n\x08RECEIVED\x10\x02B\x07\n\x05value\x1a\x98\x01\n\nTimeEvents\x12A\n\ntime_event\x18\x01 \x03(\x0b2-.google.devtools.cloudtrace.v2.Span.TimeEvent\x12!\n\x19dropped_annotations_count\x18\x02 \x01(\x05\x12$\n\x1cdropped_message_events_count\x18\x03 \x01(\x05\x1a\xf7\x01\n\x04Link\x12\x10\n\x08trace_id\x18\x01 \x01(\t\x12\x0f\n\x07span_id\x18\x02 \x01(\t\x12;\n\x04type\x18\x03 \x01(\x0e2-.google.devtools.cloudtrace.v2.Span.Link.Type\x12B\n\nattributes\x18\x04 \x01(\x0b2..google.devtools.cloudtrace.v2.Span.Attributes"K\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11CHILD_LINKED_SPAN\x10\x01\x12\x16\n\x12PARENT_LINKED_SPAN\x10\x02\x1a\\\n\x05Links\x126\n\x04link\x18\x01 \x03(\x0b2(.google.devtools.cloudtrace.v2.Span.Link\x12\x1b\n\x13dropped_links_count\x18\x02 \x01(\x05"g\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x0c\n\x08INTERNAL\x10\x01\x12\n\n\x06SERVER\x10\x02\x12\n\n\x06CLIENT\x10\x03\x12\x0c\n\x08PRODUCER\x10\x04\x12\x0c\n\x08CONSUMER\x10\x05:S\xeaAP\n\x1ecloudtrace.googleapis.com/Span\x12.projects/{project}/traces/{trace}/spans/{span}"\x8e\x01\n\x0eAttributeValue\x12H\n\x0cstring_value\x18\x01 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableStringH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00B\x07\n\x05value"\x89\x05\n\nStackTrace\x12K\n\x0cstack_frames\x18\x01 \x01(\x0b25.google.devtools.cloudtrace.v2.StackTrace.StackFrames\x12\x1b\n\x13stack_trace_hash_id\x18\x02 \x01(\x03\x1a\x9e\x03\n\nStackFrame\x12G\n\rfunction_name\x18\x01 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString\x12P\n\x16original_function_name\x18\x02 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString\x12C\n\tfile_name\x18\x03 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString\x12\x13\n\x0bline_number\x18\x04 \x01(\x03\x12\x15\n\rcolumn_number\x18\x05 \x01(\x03\x12:\n\x0bload_module\x18\x06 \x01(\x0b2%.google.devtools.cloudtrace.v2.Module\x12H\n\x0esource_version\x18\x07 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString\x1ap\n\x0bStackFrames\x12C\n\x05frame\x18\x01 \x03(\x0b24.google.devtools.cloudtrace.v2.StackTrace.StackFrame\x12\x1c\n\x14dropped_frames_count\x18\x02 \x01(\x05"\x8e\x01\n\x06Module\x12@\n\x06module\x18\x01 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString\x12B\n\x08build_id\x18\x02 \x01(\x0b20.google.devtools.cloudtrace.v2.TruncatableString"@\n\x11TruncatableString\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1c\n\x14truncated_byte_count\x18\x02 \x01(\x05B\xad\x01\n!com.google.devtools.cloudtrace.v2B\nTraceProtoP\x01Z/cloud.google.com/go/trace/apiv2/tracepb;tracepb\xaa\x02\x15Google.Cloud.Trace.V2\xca\x02\x15Google\\Cloud\\Trace\\V2\xea\x02\x18Google::Cloud::Trace::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.cloudtrace.v2.trace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.devtools.cloudtrace.v2B\nTraceProtoP\x01Z/cloud.google.com/go/trace/apiv2/tracepb;tracepb\xaa\x02\x15Google.Cloud.Trace.V2\xca\x02\x15Google\\Cloud\\Trace\\V2\xea\x02\x18Google::Cloud::Trace::V2'
    _globals['_SPAN_ATTRIBUTES_ATTRIBUTEMAPENTRY']._loaded_options = None
    _globals['_SPAN_ATTRIBUTES_ATTRIBUTEMAPENTRY']._serialized_options = b'8\x01'
    _globals['_SPAN'].fields_by_name['name']._loaded_options = None
    _globals['_SPAN'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SPAN'].fields_by_name['span_id']._loaded_options = None
    _globals['_SPAN'].fields_by_name['span_id']._serialized_options = b'\xe0A\x02'
    _globals['_SPAN'].fields_by_name['display_name']._loaded_options = None
    _globals['_SPAN'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SPAN'].fields_by_name['start_time']._loaded_options = None
    _globals['_SPAN'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_SPAN'].fields_by_name['end_time']._loaded_options = None
    _globals['_SPAN'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_SPAN'].fields_by_name['status']._loaded_options = None
    _globals['_SPAN'].fields_by_name['status']._serialized_options = b'\xe0A\x01'
    _globals['_SPAN'].fields_by_name['same_process_as_parent_span']._loaded_options = None
    _globals['_SPAN'].fields_by_name['same_process_as_parent_span']._serialized_options = b'\xe0A\x01'
    _globals['_SPAN'].fields_by_name['child_span_count']._loaded_options = None
    _globals['_SPAN'].fields_by_name['child_span_count']._serialized_options = b'\xe0A\x01'
    _globals['_SPAN'].fields_by_name['span_kind']._loaded_options = None
    _globals['_SPAN'].fields_by_name['span_kind']._serialized_options = b'\xe0A\x01'
    _globals['_SPAN']._loaded_options = None
    _globals['_SPAN']._serialized_options = b'\xeaAP\n\x1ecloudtrace.googleapis.com/Span\x12.projects/{project}/traces/{trace}/spans/{span}'
    _globals['_SPAN']._serialized_start = 227
    _globals['_SPAN']._serialized_end = 2516
    _globals['_SPAN_ATTRIBUTES']._serialized_start = 982
    _globals['_SPAN_ATTRIBUTES']._serialized_end = 1217
    _globals['_SPAN_ATTRIBUTES_ATTRIBUTEMAPENTRY']._serialized_start = 1119
    _globals['_SPAN_ATTRIBUTES_ATTRIBUTEMAPENTRY']._serialized_end = 1217
    _globals['_SPAN_TIMEEVENT']._serialized_start = 1220
    _globals['_SPAN_TIMEEVENT']._serialized_end = 1827
    _globals['_SPAN_TIMEEVENT_ANNOTATION']._serialized_start = 1441
    _globals['_SPAN_TIMEEVENT_ANNOTATION']._serialized_end = 1592
    _globals['_SPAN_TIMEEVENT_MESSAGEEVENT']._serialized_start = 1595
    _globals['_SPAN_TIMEEVENT_MESSAGEEVENT']._serialized_end = 1818
    _globals['_SPAN_TIMEEVENT_MESSAGEEVENT_TYPE']._serialized_start = 1766
    _globals['_SPAN_TIMEEVENT_MESSAGEEVENT_TYPE']._serialized_end = 1818
    _globals['_SPAN_TIMEEVENTS']._serialized_start = 1830
    _globals['_SPAN_TIMEEVENTS']._serialized_end = 1982
    _globals['_SPAN_LINK']._serialized_start = 1985
    _globals['_SPAN_LINK']._serialized_end = 2232
    _globals['_SPAN_LINK_TYPE']._serialized_start = 2157
    _globals['_SPAN_LINK_TYPE']._serialized_end = 2232
    _globals['_SPAN_LINKS']._serialized_start = 2234
    _globals['_SPAN_LINKS']._serialized_end = 2326
    _globals['_SPAN_SPANKIND']._serialized_start = 2328
    _globals['_SPAN_SPANKIND']._serialized_end = 2431
    _globals['_ATTRIBUTEVALUE']._serialized_start = 2519
    _globals['_ATTRIBUTEVALUE']._serialized_end = 2661
    _globals['_STACKTRACE']._serialized_start = 2664
    _globals['_STACKTRACE']._serialized_end = 3313
    _globals['_STACKTRACE_STACKFRAME']._serialized_start = 2785
    _globals['_STACKTRACE_STACKFRAME']._serialized_end = 3199
    _globals['_STACKTRACE_STACKFRAMES']._serialized_start = 3201
    _globals['_STACKTRACE_STACKFRAMES']._serialized_end = 3313
    _globals['_MODULE']._serialized_start = 3316
    _globals['_MODULE']._serialized_end = 3458
    _globals['_TRUNCATABLESTRING']._serialized_start = 3460
    _globals['_TRUNCATABLESTRING']._serialized_end = 3524