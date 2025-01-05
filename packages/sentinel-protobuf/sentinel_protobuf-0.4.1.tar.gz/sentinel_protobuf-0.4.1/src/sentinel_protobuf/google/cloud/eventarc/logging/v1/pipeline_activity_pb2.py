"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/logging/v1/pipeline_activity.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/eventarc/logging/v1/pipeline_activity.proto\x12 google.cloud.eventarc.logging.v1\x1a\x1bgoogle/api/field_info.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x94\x0e\n\x10PipelineActivity\x12\x1d\n\x0bmessage_uid\x18\x01 \x01(\tB\x08\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12V\n\nattributes\x18\x02 \x03(\x0b2B.google.cloud.eventarc.logging.v1.PipelineActivity.AttributesEntry\x121\n\ractivity_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12^\n\x10message_received\x18\x04 \x01(\x0b2B.google.cloud.eventarc.logging.v1.PipelineActivity.MessageReceivedH\x00\x12d\n\x13message_transformed\x18\x05 \x01(\x0b2E.google.cloud.eventarc.logging.v1.PipelineActivity.MessageTransformedH\x00\x12`\n\x11message_converted\x18\x06 \x01(\x0b2C.google.cloud.eventarc.logging.v1.PipelineActivity.MessageConvertedH\x00\x12q\n\x1amessage_request_dispatched\x18\x07 \x01(\x0b2K.google.cloud.eventarc.logging.v1.PipelineActivity.MessageRequestDispatchedH\x00\x12o\n\x19message_response_received\x18\x08 \x01(\x0b2J.google.cloud.eventarc.logging.v1.PipelineActivity.MessageResponseReceivedH\x00\x1a\xa5\x01\n\x0fMessageReceived\x12\x0f\n\x07details\x18\x01 \x01(\t\x12^\n\x14input_payload_format\x18\x02 \x01(\x0e2@.google.cloud.eventarc.logging.v1.PipelineActivity.PayloadFormat\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x1aH\n\x12MessageTransformed\x12\x0f\n\x07details\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x1a\x87\x02\n\x10MessageConverted\x12\x0f\n\x07details\x18\x01 \x01(\t\x12^\n\x14input_payload_format\x18\x02 \x01(\x0e2@.google.cloud.eventarc.logging.v1.PipelineActivity.PayloadFormat\x12_\n\x15output_payload_format\x18\x03 \x01(\x0e2@.google.cloud.eventarc.logging.v1.PipelineActivity.PayloadFormat\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x1ac\n\x18MessageRequestDispatched\x12\x0f\n\x07details\x18\x01 \x01(\t\x12\x13\n\x0bdestination\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x1a\xd9\x02\n\x17MessageResponseReceived\x12\x0f\n\x07details\x18\x01 \x01(\t\x12l\n\x0cretry_status\x18\x02 \x01(\x0e2V.google.cloud.eventarc.logging.v1.PipelineActivity.MessageResponseReceived.RetryStatus\x12.\n\nretry_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1a\n\x12http_response_code\x18\x04 \x01(\x05\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.Status"P\n\x0bRetryStatus\x12\x1c\n\x18RETRY_STATUS_UNSPECIFIED\x10\x00\x12\x0e\n\nWILL_RETRY\x10\x01\x12\x13\n\x0fRETRY_EXHAUSTED\x10\x02\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"N\n\rPayloadFormat\x12\x1e\n\x1aPAYLOAD_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04JSON\x10\x01\x12\t\n\x05PROTO\x10\x02\x12\x08\n\x04AVRO\x10\x03B\n\n\x08activityB\xec\x01\n$com.google.cloud.eventarc.logging.v1B\x15PipelineActivityProtoP\x01Z>cloud.google.com/go/eventarc/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.Eventarc.Logging.V1\xca\x02 Google\\Cloud\\Eventarc\\Logging\\V1\xea\x02$Google::Cloud::Eventarc::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.logging.v1.pipeline_activity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.eventarc.logging.v1B\x15PipelineActivityProtoP\x01Z>cloud.google.com/go/eventarc/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.Eventarc.Logging.V1\xca\x02 Google\\Cloud\\Eventarc\\Logging\\V1\xea\x02$Google::Cloud::Eventarc::Logging::V1'
    _globals['_PIPELINEACTIVITY_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PIPELINEACTIVITY_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINEACTIVITY'].fields_by_name['message_uid']._loaded_options = None
    _globals['_PIPELINEACTIVITY'].fields_by_name['message_uid']._serialized_options = b'\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_PIPELINEACTIVITY']._serialized_start = 182
    _globals['_PIPELINEACTIVITY']._serialized_end = 1994
    _globals['_PIPELINEACTIVITY_MESSAGERECEIVED']._serialized_start = 897
    _globals['_PIPELINEACTIVITY_MESSAGERECEIVED']._serialized_end = 1062
    _globals['_PIPELINEACTIVITY_MESSAGETRANSFORMED']._serialized_start = 1064
    _globals['_PIPELINEACTIVITY_MESSAGETRANSFORMED']._serialized_end = 1136
    _globals['_PIPELINEACTIVITY_MESSAGECONVERTED']._serialized_start = 1139
    _globals['_PIPELINEACTIVITY_MESSAGECONVERTED']._serialized_end = 1402
    _globals['_PIPELINEACTIVITY_MESSAGEREQUESTDISPATCHED']._serialized_start = 1404
    _globals['_PIPELINEACTIVITY_MESSAGEREQUESTDISPATCHED']._serialized_end = 1503
    _globals['_PIPELINEACTIVITY_MESSAGERESPONSERECEIVED']._serialized_start = 1506
    _globals['_PIPELINEACTIVITY_MESSAGERESPONSERECEIVED']._serialized_end = 1851
    _globals['_PIPELINEACTIVITY_MESSAGERESPONSERECEIVED_RETRYSTATUS']._serialized_start = 1771
    _globals['_PIPELINEACTIVITY_MESSAGERESPONSERECEIVED_RETRYSTATUS']._serialized_end = 1851
    _globals['_PIPELINEACTIVITY_ATTRIBUTESENTRY']._serialized_start = 1853
    _globals['_PIPELINEACTIVITY_ATTRIBUTESENTRY']._serialized_end = 1902
    _globals['_PIPELINEACTIVITY_PAYLOADFORMAT']._serialized_start = 1904
    _globals['_PIPELINEACTIVITY_PAYLOADFORMAT']._serialized_end = 1982