"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/logging/v1/enrollment_activity.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/eventarc/logging/v1/enrollment_activity.proto\x12 google.cloud.eventarc.logging.v1\x1a\x1bgoogle/api/field_info.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xaa\x03\n\x12EnrollmentActivity\x12\x1d\n\x0bmessage_uid\x18\x01 \x01(\tB\x08\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12X\n\nattributes\x18\x02 \x03(\x0b2D.google.cloud.eventarc.logging.v1.EnrollmentActivity.AttributesEntry\x121\n\ractivity_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12O\n\x07matched\x18\x04 \x01(\x0b2<.google.cloud.eventarc.logging.v1.EnrollmentActivity.MatchedH\x00\x1aX\n\x07Matched\x12\x0f\n\x07details\x18\x01 \x01(\t\x12\x19\n\x11event_destination\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\n\n\x08activityB\xee\x01\n$com.google.cloud.eventarc.logging.v1B\x17EnrollmentActivityProtoP\x01Z>cloud.google.com/go/eventarc/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.Eventarc.Logging.V1\xca\x02 Google\\Cloud\\Eventarc\\Logging\\V1\xea\x02$Google::Cloud::Eventarc::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.logging.v1.enrollment_activity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.eventarc.logging.v1B\x17EnrollmentActivityProtoP\x01Z>cloud.google.com/go/eventarc/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.Eventarc.Logging.V1\xca\x02 Google\\Cloud\\Eventarc\\Logging\\V1\xea\x02$Google::Cloud::Eventarc::Logging::V1'
    _globals['_ENROLLMENTACTIVITY_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_ENROLLMENTACTIVITY_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_ENROLLMENTACTIVITY'].fields_by_name['message_uid']._loaded_options = None
    _globals['_ENROLLMENTACTIVITY'].fields_by_name['message_uid']._serialized_options = b'\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_ENROLLMENTACTIVITY']._serialized_start = 184
    _globals['_ENROLLMENTACTIVITY']._serialized_end = 610
    _globals['_ENROLLMENTACTIVITY_MATCHED']._serialized_start = 459
    _globals['_ENROLLMENTACTIVITY_MATCHED']._serialized_end = 547
    _globals['_ENROLLMENTACTIVITY_ATTRIBUTESENTRY']._serialized_start = 549
    _globals['_ENROLLMENTACTIVITY_ATTRIBUTESENTRY']._serialized_end = 598