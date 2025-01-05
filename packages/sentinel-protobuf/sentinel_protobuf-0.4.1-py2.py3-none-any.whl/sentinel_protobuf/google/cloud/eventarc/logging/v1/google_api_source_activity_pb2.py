"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/logging/v1/google_api_source_activity.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/eventarc/logging/v1/google_api_source_activity.proto\x12 google.cloud.eventarc.logging.v1\x1a\x1bgoogle/api/field_info.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xd1\x03\n\x17GoogleApiSourceActivity\x12\x1d\n\x0bmessage_uid\x18\x01 \x01(\tB\x08\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12]\n\nattributes\x18\x02 \x03(\x0b2I.google.cloud.eventarc.logging.v1.GoogleApiSourceActivity.AttributesEntry\x121\n\ractivity_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12X\n\tpublished\x18\x04 \x01(\x0b2C.google.cloud.eventarc.logging.v1.GoogleApiSourceActivity.PublishedH\x00\x1al\n\tPublished\x12\x13\n\x0bmessage_bus\x18\x01 \x01(\t\x12\x16\n\x0eevent_provider\x18\x02 \x01(\t\x12\x0f\n\x07details\x18\x03 \x01(\t\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\n\n\x08activityB\xfb\x01\n$com.google.cloud.eventarc.logging.v1B$GoogleApiEventPublishedActivityProtoP\x01Z>cloud.google.com/go/eventarc/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.Eventarc.Logging.V1\xca\x02 Google\\Cloud\\Eventarc\\Logging\\V1\xea\x02$Google::Cloud::Eventarc::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.logging.v1.google_api_source_activity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.eventarc.logging.v1B$GoogleApiEventPublishedActivityProtoP\x01Z>cloud.google.com/go/eventarc/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.Eventarc.Logging.V1\xca\x02 Google\\Cloud\\Eventarc\\Logging\\V1\xea\x02$Google::Cloud::Eventarc::Logging::V1'
    _globals['_GOOGLEAPISOURCEACTIVITY_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_GOOGLEAPISOURCEACTIVITY_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_GOOGLEAPISOURCEACTIVITY'].fields_by_name['message_uid']._loaded_options = None
    _globals['_GOOGLEAPISOURCEACTIVITY'].fields_by_name['message_uid']._serialized_options = b'\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GOOGLEAPISOURCEACTIVITY']._serialized_start = 191
    _globals['_GOOGLEAPISOURCEACTIVITY']._serialized_end = 656
    _globals['_GOOGLEAPISOURCEACTIVITY_PUBLISHED']._serialized_start = 485
    _globals['_GOOGLEAPISOURCEACTIVITY_PUBLISHED']._serialized_end = 593
    _globals['_GOOGLEAPISOURCEACTIVITY_ATTRIBUTESENTRY']._serialized_start = 595
    _globals['_GOOGLEAPISOURCEACTIVITY_ATTRIBUTESENTRY']._serialized_end = 644