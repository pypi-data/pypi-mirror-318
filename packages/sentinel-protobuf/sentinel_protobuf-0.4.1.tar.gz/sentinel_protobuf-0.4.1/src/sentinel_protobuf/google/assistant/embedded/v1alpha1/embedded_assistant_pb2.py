"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/assistant/embedded/v1alpha1/embedded_assistant.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/assistant/embedded/v1alpha1/embedded_assistant.proto\x12"google.assistant.embedded.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/rpc/status.proto"\xf5\x01\n\x0eConverseConfig\x12J\n\x0faudio_in_config\x18\x01 \x01(\x0b21.google.assistant.embedded.v1alpha1.AudioInConfig\x12L\n\x10audio_out_config\x18\x02 \x01(\x0b22.google.assistant.embedded.v1alpha1.AudioOutConfig\x12I\n\x0econverse_state\x18\x03 \x01(\x0b21.google.assistant.embedded.v1alpha1.ConverseState"\xb6\x01\n\rAudioInConfig\x12L\n\x08encoding\x18\x01 \x01(\x0e2:.google.assistant.embedded.v1alpha1.AudioInConfig.Encoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05"<\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x08\n\x04FLAC\x10\x02"\xe3\x01\n\x0eAudioOutConfig\x12M\n\x08encoding\x18\x01 \x01(\x0e2;.google.assistant.embedded.v1alpha1.AudioOutConfig.Encoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x19\n\x11volume_percentage\x18\x03 \x01(\x05"L\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x0f\n\x0bOPUS_IN_OGG\x10\x03"+\n\rConverseState\x12\x1a\n\x12conversation_state\x18\x01 \x01(\x0c"\x1e\n\x08AudioOut\x12\x12\n\naudio_data\x18\x01 \x01(\x0c"\xbd\x02\n\x0eConverseResult\x12\x1b\n\x13spoken_request_text\x18\x01 \x01(\t\x12\x1c\n\x14spoken_response_text\x18\x02 \x01(\t\x12\x1a\n\x12conversation_state\x18\x03 \x01(\x0c\x12Z\n\x0fmicrophone_mode\x18\x04 \x01(\x0e2A.google.assistant.embedded.v1alpha1.ConverseResult.MicrophoneMode\x12\x19\n\x11volume_percentage\x18\x05 \x01(\x05"]\n\x0eMicrophoneMode\x12\x1f\n\x1bMICROPHONE_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10CLOSE_MICROPHONE\x10\x01\x12\x14\n\x10DIALOG_FOLLOW_ON\x10\x02"\x7f\n\x0fConverseRequest\x12D\n\x06config\x18\x01 \x01(\x0b22.google.assistant.embedded.v1alpha1.ConverseConfigH\x00\x12\x12\n\x08audio_in\x18\x02 \x01(\x0cH\x00B\x12\n\x10converse_request"\xea\x02\n\x10ConverseResponse\x12#\n\x05error\x18\x01 \x01(\x0b2\x12.google.rpc.StatusH\x00\x12T\n\nevent_type\x18\x02 \x01(\x0e2>.google.assistant.embedded.v1alpha1.ConverseResponse.EventTypeH\x00\x12A\n\taudio_out\x18\x03 \x01(\x0b2,.google.assistant.embedded.v1alpha1.AudioOutH\x00\x12D\n\x06result\x18\x05 \x01(\x0b22.google.assistant.embedded.v1alpha1.ConverseResultH\x00"=\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10END_OF_UTTERANCE\x10\x01B\x13\n\x11converse_response2\x8e\x01\n\x11EmbeddedAssistant\x12y\n\x08Converse\x123.google.assistant.embedded.v1alpha1.ConverseRequest\x1a4.google.assistant.embedded.v1alpha1.ConverseResponse(\x010\x01B\x86\x01\n&com.google.assistant.embedded.v1alpha1B\x0eAssistantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/assistant/embedded/v1alpha1;embeddedb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.assistant.embedded.v1alpha1.embedded_assistant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.assistant.embedded.v1alpha1B\x0eAssistantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/assistant/embedded/v1alpha1;embedded'
    _globals['_CONVERSECONFIG']._serialized_start = 155
    _globals['_CONVERSECONFIG']._serialized_end = 400
    _globals['_AUDIOINCONFIG']._serialized_start = 403
    _globals['_AUDIOINCONFIG']._serialized_end = 585
    _globals['_AUDIOINCONFIG_ENCODING']._serialized_start = 525
    _globals['_AUDIOINCONFIG_ENCODING']._serialized_end = 585
    _globals['_AUDIOOUTCONFIG']._serialized_start = 588
    _globals['_AUDIOOUTCONFIG']._serialized_end = 815
    _globals['_AUDIOOUTCONFIG_ENCODING']._serialized_start = 739
    _globals['_AUDIOOUTCONFIG_ENCODING']._serialized_end = 815
    _globals['_CONVERSESTATE']._serialized_start = 817
    _globals['_CONVERSESTATE']._serialized_end = 860
    _globals['_AUDIOOUT']._serialized_start = 862
    _globals['_AUDIOOUT']._serialized_end = 892
    _globals['_CONVERSERESULT']._serialized_start = 895
    _globals['_CONVERSERESULT']._serialized_end = 1212
    _globals['_CONVERSERESULT_MICROPHONEMODE']._serialized_start = 1119
    _globals['_CONVERSERESULT_MICROPHONEMODE']._serialized_end = 1212
    _globals['_CONVERSEREQUEST']._serialized_start = 1214
    _globals['_CONVERSEREQUEST']._serialized_end = 1341
    _globals['_CONVERSERESPONSE']._serialized_start = 1344
    _globals['_CONVERSERESPONSE']._serialized_end = 1706
    _globals['_CONVERSERESPONSE_EVENTTYPE']._serialized_start = 1624
    _globals['_CONVERSERESPONSE_EVENTTYPE']._serialized_end = 1685
    _globals['_EMBEDDEDASSISTANT']._serialized_start = 1709
    _globals['_EMBEDDEDASSISTANT']._serialized_end = 1851