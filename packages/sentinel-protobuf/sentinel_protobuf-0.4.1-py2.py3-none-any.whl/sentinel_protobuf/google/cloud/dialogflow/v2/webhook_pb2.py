"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/webhook.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.dialogflow.v2 import context_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_context__pb2
from .....google.cloud.dialogflow.v2 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2
from .....google.cloud.dialogflow.v2 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2
from .....google.cloud.dialogflow.v2 import session_entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_session__entity__type__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/v2/webhook.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a(google/cloud/dialogflow/v2/context.proto\x1a\'google/cloud/dialogflow/v2/intent.proto\x1a(google/cloud/dialogflow/v2/session.proto\x1a4google/cloud/dialogflow/v2/session_entity_type.proto\x1a\x1cgoogle/protobuf/struct.proto"\xd6\x01\n\x0eWebhookRequest\x12\x0f\n\x07session\x18\x04 \x01(\t\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12=\n\x0cquery_result\x18\x02 \x01(\x0b2\'.google.cloud.dialogflow.v2.QueryResult\x12_\n\x1eoriginal_detect_intent_request\x18\x03 \x01(\x0b27.google.cloud.dialogflow.v2.OriginalDetectIntentRequest"\x80\x03\n\x0fWebhookResponse\x12\x18\n\x10fulfillment_text\x18\x01 \x01(\t\x12H\n\x14fulfillment_messages\x18\x02 \x03(\x0b2*.google.cloud.dialogflow.v2.Intent.Message\x12\x0e\n\x06source\x18\x03 \x01(\t\x12(\n\x07payload\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12<\n\x0foutput_contexts\x18\x05 \x03(\x0b2#.google.cloud.dialogflow.v2.Context\x12D\n\x14followup_event_input\x18\x06 \x01(\x0b2&.google.cloud.dialogflow.v2.EventInput\x12K\n\x14session_entity_types\x18\n \x03(\x0b2-.google.cloud.dialogflow.v2.SessionEntityType"h\n\x1bOriginalDetectIntentRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07payload\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x92\x01\n\x1ecom.google.cloud.dialogflow.v2B\x0cWebhookProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.webhook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x0cWebhookProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_WEBHOOKREQUEST']._serialized_start = 282
    _globals['_WEBHOOKREQUEST']._serialized_end = 496
    _globals['_WEBHOOKRESPONSE']._serialized_start = 499
    _globals['_WEBHOOKRESPONSE']._serialized_end = 883
    _globals['_ORIGINALDETECTINTENTREQUEST']._serialized_start = 885
    _globals['_ORIGINALDETECTINTENTREQUEST']._serialized_end = 989