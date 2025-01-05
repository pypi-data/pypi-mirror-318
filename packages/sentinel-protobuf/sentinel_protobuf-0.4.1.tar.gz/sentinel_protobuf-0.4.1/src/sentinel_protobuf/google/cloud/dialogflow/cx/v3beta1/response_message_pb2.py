"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/response_message.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import tool_call_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_tool__call__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/dialogflow/cx/v3beta1/response_message.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a2google/cloud/dialogflow/cx/v3beta1/tool_call.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa7\r\n\x0fResponseMessage\x12H\n\x04text\x18\x01 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.TextH\x00\x12*\n\x07payload\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12g\n\x14conversation_success\x18\t \x01(\x0b2G.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.ConversationSuccessH\x00\x12`\n\x11output_audio_text\x18\x08 \x01(\x0b2C.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.OutputAudioTextH\x00\x12b\n\x12live_agent_handoff\x18\n \x01(\x0b2D.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.LiveAgentHandoffH\x00\x12b\n\x0fend_interaction\x18\x0b \x01(\x0b2B.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.EndInteractionB\x03\xe0A\x03H\x00\x12S\n\nplay_audio\x18\x0c \x01(\x0b2=.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.PlayAudioH\x00\x12Z\n\x0bmixed_audio\x18\r \x01(\x0b2>.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.MixedAudioB\x03\xe0A\x03H\x00\x12l\n\x17telephony_transfer_call\x18\x12 \x01(\x0b2I.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.TelephonyTransferCallH\x00\x12d\n\x13knowledge_info_card\x18\x14 \x01(\x0b2E.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.KnowledgeInfoCardH\x00\x12A\n\ttool_call\x18\x16 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.ToolCallH\x00\x12\x0f\n\x07channel\x18\x13 \x01(\t\x1aC\n\x04Text\x12\x11\n\x04text\x18\x01 \x03(\tB\x03\xe0A\x02\x12(\n\x1ballow_playback_interruption\x18\x02 \x01(\x08B\x03\xe0A\x03\x1a=\n\x10LiveAgentHandoff\x12)\n\x08metadata\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct\x1a@\n\x13ConversationSuccess\x12)\n\x08metadata\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct\x1ae\n\x0fOutputAudioText\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x0e\n\x04ssml\x18\x02 \x01(\tH\x00\x12(\n\x1ballow_playback_interruption\x18\x03 \x01(\x08B\x03\xe0A\x03B\x08\n\x06source\x1a\x10\n\x0eEndInteraction\x1aM\n\tPlayAudio\x12\x16\n\taudio_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12(\n\x1ballow_playback_interruption\x18\x02 \x01(\x08B\x03\xe0A\x03\x1a\xc6\x01\n\nMixedAudio\x12X\n\x08segments\x18\x01 \x03(\x0b2F.google.cloud.dialogflow.cx.v3beta1.ResponseMessage.MixedAudio.Segment\x1a^\n\x07Segment\x12\x0f\n\x05audio\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x12(\n\x1ballow_playback_interruption\x18\x03 \x01(\x08B\x03\xe0A\x03B\t\n\x07content\x1a;\n\x15TelephonyTransferCall\x12\x16\n\x0cphone_number\x18\x01 \x01(\tH\x00B\n\n\x08endpoint\x1a\x13\n\x11KnowledgeInfoCardB\t\n\x07messageB\xce\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x14ResponseMessageProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.response_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x14ResponseMessageProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_RESPONSEMESSAGE_TEXT'].fields_by_name['text']._loaded_options = None
    _globals['_RESPONSEMESSAGE_TEXT'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_RESPONSEMESSAGE_TEXT'].fields_by_name['allow_playback_interruption']._loaded_options = None
    _globals['_RESPONSEMESSAGE_TEXT'].fields_by_name['allow_playback_interruption']._serialized_options = b'\xe0A\x03'
    _globals['_RESPONSEMESSAGE_OUTPUTAUDIOTEXT'].fields_by_name['allow_playback_interruption']._loaded_options = None
    _globals['_RESPONSEMESSAGE_OUTPUTAUDIOTEXT'].fields_by_name['allow_playback_interruption']._serialized_options = b'\xe0A\x03'
    _globals['_RESPONSEMESSAGE_PLAYAUDIO'].fields_by_name['audio_uri']._loaded_options = None
    _globals['_RESPONSEMESSAGE_PLAYAUDIO'].fields_by_name['audio_uri']._serialized_options = b'\xe0A\x02'
    _globals['_RESPONSEMESSAGE_PLAYAUDIO'].fields_by_name['allow_playback_interruption']._loaded_options = None
    _globals['_RESPONSEMESSAGE_PLAYAUDIO'].fields_by_name['allow_playback_interruption']._serialized_options = b'\xe0A\x03'
    _globals['_RESPONSEMESSAGE_MIXEDAUDIO_SEGMENT'].fields_by_name['allow_playback_interruption']._loaded_options = None
    _globals['_RESPONSEMESSAGE_MIXEDAUDIO_SEGMENT'].fields_by_name['allow_playback_interruption']._serialized_options = b'\xe0A\x03'
    _globals['_RESPONSEMESSAGE'].fields_by_name['end_interaction']._loaded_options = None
    _globals['_RESPONSEMESSAGE'].fields_by_name['end_interaction']._serialized_options = b'\xe0A\x03'
    _globals['_RESPONSEMESSAGE'].fields_by_name['mixed_audio']._loaded_options = None
    _globals['_RESPONSEMESSAGE'].fields_by_name['mixed_audio']._serialized_options = b'\xe0A\x03'
    _globals['_RESPONSEMESSAGE']._serialized_start = 213
    _globals['_RESPONSEMESSAGE']._serialized_end = 1916
    _globals['_RESPONSEMESSAGE_TEXT']._serialized_start = 1226
    _globals['_RESPONSEMESSAGE_TEXT']._serialized_end = 1293
    _globals['_RESPONSEMESSAGE_LIVEAGENTHANDOFF']._serialized_start = 1295
    _globals['_RESPONSEMESSAGE_LIVEAGENTHANDOFF']._serialized_end = 1356
    _globals['_RESPONSEMESSAGE_CONVERSATIONSUCCESS']._serialized_start = 1358
    _globals['_RESPONSEMESSAGE_CONVERSATIONSUCCESS']._serialized_end = 1422
    _globals['_RESPONSEMESSAGE_OUTPUTAUDIOTEXT']._serialized_start = 1424
    _globals['_RESPONSEMESSAGE_OUTPUTAUDIOTEXT']._serialized_end = 1525
    _globals['_RESPONSEMESSAGE_ENDINTERACTION']._serialized_start = 1527
    _globals['_RESPONSEMESSAGE_ENDINTERACTION']._serialized_end = 1543
    _globals['_RESPONSEMESSAGE_PLAYAUDIO']._serialized_start = 1545
    _globals['_RESPONSEMESSAGE_PLAYAUDIO']._serialized_end = 1622
    _globals['_RESPONSEMESSAGE_MIXEDAUDIO']._serialized_start = 1625
    _globals['_RESPONSEMESSAGE_MIXEDAUDIO']._serialized_end = 1823
    _globals['_RESPONSEMESSAGE_MIXEDAUDIO_SEGMENT']._serialized_start = 1729
    _globals['_RESPONSEMESSAGE_MIXEDAUDIO_SEGMENT']._serialized_end = 1823
    _globals['_RESPONSEMESSAGE_TELEPHONYTRANSFERCALL']._serialized_start = 1825
    _globals['_RESPONSEMESSAGE_TELEPHONYTRANSFERCALL']._serialized_end = 1884
    _globals['_RESPONSEMESSAGE_KNOWLEDGEINFOCARD']._serialized_start = 1886
    _globals['_RESPONSEMESSAGE_KNOWLEDGEINFOCARD']._serialized_end = 1905