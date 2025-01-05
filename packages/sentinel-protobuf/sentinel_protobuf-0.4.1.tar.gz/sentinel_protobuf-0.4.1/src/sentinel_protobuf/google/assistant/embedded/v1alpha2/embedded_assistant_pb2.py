"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/assistant/embedded/v1alpha2/embedded_assistant.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/assistant/embedded/v1alpha2/embedded_assistant.proto\x12"google.assistant.embedded.v1alpha2\x1a\x1cgoogle/api/annotations.proto\x1a\x18google/type/latlng.proto"o\n\rAssistRequest\x12B\n\x06config\x18\x01 \x01(\x0b20.google.assistant.embedded.v1alpha2.AssistConfigH\x00\x12\x12\n\x08audio_in\x18\x02 \x01(\x0cH\x00B\x06\n\x04type"\xd4\x04\n\x0eAssistResponse\x12P\n\nevent_type\x18\x01 \x01(\x0e2<.google.assistant.embedded.v1alpha2.AssistResponse.EventType\x12?\n\taudio_out\x18\x03 \x01(\x0b2,.google.assistant.embedded.v1alpha2.AudioOut\x12A\n\nscreen_out\x18\x04 \x01(\x0b2-.google.assistant.embedded.v1alpha2.ScreenOut\x12G\n\rdevice_action\x18\x06 \x01(\x0b20.google.assistant.embedded.v1alpha2.DeviceAction\x12S\n\x0espeech_results\x18\x02 \x03(\x0b2;.google.assistant.embedded.v1alpha2.SpeechRecognitionResult\x12L\n\x10dialog_state_out\x18\x05 \x01(\x0b22.google.assistant.embedded.v1alpha2.DialogStateOut\x12A\n\ndebug_info\x18\x08 \x01(\x0b2-.google.assistant.embedded.v1alpha2.DebugInfo"=\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10END_OF_UTTERANCE\x10\x01"0\n\tDebugInfo\x12#\n\x1baog_agent_to_assistant_json\x18\x01 \x01(\t"\xf4\x03\n\x0cAssistConfig\x12L\n\x0faudio_in_config\x18\x01 \x01(\x0b21.google.assistant.embedded.v1alpha2.AudioInConfigH\x00\x12\x14\n\ntext_query\x18\x06 \x01(\tH\x00\x12L\n\x10audio_out_config\x18\x02 \x01(\x0b22.google.assistant.embedded.v1alpha2.AudioOutConfig\x12N\n\x11screen_out_config\x18\x08 \x01(\x0b23.google.assistant.embedded.v1alpha2.ScreenOutConfig\x12J\n\x0fdialog_state_in\x18\x03 \x01(\x0b21.google.assistant.embedded.v1alpha2.DialogStateIn\x12G\n\rdevice_config\x18\x04 \x01(\x0b20.google.assistant.embedded.v1alpha2.DeviceConfig\x12E\n\x0cdebug_config\x18\x05 \x01(\x0b2/.google.assistant.embedded.v1alpha2.DebugConfigB\x06\n\x04type"\xb6\x01\n\rAudioInConfig\x12L\n\x08encoding\x18\x01 \x01(\x0e2:.google.assistant.embedded.v1alpha2.AudioInConfig.Encoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05"<\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x08\n\x04FLAC\x10\x02"\xe3\x01\n\x0eAudioOutConfig\x12M\n\x08encoding\x18\x01 \x01(\x0e2;.google.assistant.embedded.v1alpha2.AudioOutConfig.Encoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x19\n\x11volume_percentage\x18\x03 \x01(\x05"L\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x0f\n\x0bOPUS_IN_OGG\x10\x03"\xa7\x01\n\x0fScreenOutConfig\x12S\n\x0bscreen_mode\x18\x01 \x01(\x0e2>.google.assistant.embedded.v1alpha2.ScreenOutConfig.ScreenMode"?\n\nScreenMode\x12\x1b\n\x17SCREEN_MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07PLAYING\x10\x03"\xac\x01\n\rDialogStateIn\x12\x1a\n\x12conversation_state\x18\x01 \x01(\x0c\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12K\n\x0fdevice_location\x18\x05 \x01(\x0b22.google.assistant.embedded.v1alpha2.DeviceLocation\x12\x1b\n\x13is_new_conversation\x18\x07 \x01(\x08":\n\x0cDeviceConfig\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x17\n\x0fdevice_model_id\x18\x03 \x01(\t"\x1e\n\x08AudioOut\x12\x12\n\naudio_data\x18\x01 \x01(\x0c"\x8b\x01\n\tScreenOut\x12D\n\x06format\x18\x01 \x01(\x0e24.google.assistant.embedded.v1alpha2.ScreenOut.Format\x12\x0c\n\x04data\x18\x02 \x01(\x0c"*\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04HTML\x10\x01"+\n\x0cDeviceAction\x12\x1b\n\x13device_request_json\x18\x01 \x01(\t"@\n\x17SpeechRecognitionResult\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x11\n\tstability\x18\x02 \x01(\x02"\xa5\x02\n\x0eDialogStateOut\x12!\n\x19supplemental_display_text\x18\x01 \x01(\t\x12\x1a\n\x12conversation_state\x18\x02 \x01(\x0c\x12Z\n\x0fmicrophone_mode\x18\x03 \x01(\x0e2A.google.assistant.embedded.v1alpha2.DialogStateOut.MicrophoneMode\x12\x19\n\x11volume_percentage\x18\x04 \x01(\x05"]\n\x0eMicrophoneMode\x12\x1f\n\x1bMICROPHONE_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10CLOSE_MICROPHONE\x10\x01\x12\x14\n\x10DIALOG_FOLLOW_ON\x10\x02"(\n\x0bDebugConfig\x12\x19\n\x11return_debug_info\x18\x06 \x01(\x08"D\n\x0eDeviceLocation\x12*\n\x0bcoordinates\x18\x01 \x01(\x0b2\x13.google.type.LatLngH\x00B\x06\n\x04type2\x88\x01\n\x11EmbeddedAssistant\x12s\n\x06Assist\x121.google.assistant.embedded.v1alpha2.AssistRequest\x1a2.google.assistant.embedded.v1alpha2.AssistResponse(\x010\x01B\x8f\x01\n&com.google.assistant.embedded.v1alpha2B\x0eAssistantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/assistant/embedded/v1alpha2;embedded\xa2\x02\x06ASTSDKb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.assistant.embedded.v1alpha2.embedded_assistant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.assistant.embedded.v1alpha2B\x0eAssistantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/assistant/embedded/v1alpha2;embedded\xa2\x02\x06ASTSDK'
    _globals['_ASSISTREQUEST']._serialized_start = 155
    _globals['_ASSISTREQUEST']._serialized_end = 266
    _globals['_ASSISTRESPONSE']._serialized_start = 269
    _globals['_ASSISTRESPONSE']._serialized_end = 865
    _globals['_ASSISTRESPONSE_EVENTTYPE']._serialized_start = 804
    _globals['_ASSISTRESPONSE_EVENTTYPE']._serialized_end = 865
    _globals['_DEBUGINFO']._serialized_start = 867
    _globals['_DEBUGINFO']._serialized_end = 915
    _globals['_ASSISTCONFIG']._serialized_start = 918
    _globals['_ASSISTCONFIG']._serialized_end = 1418
    _globals['_AUDIOINCONFIG']._serialized_start = 1421
    _globals['_AUDIOINCONFIG']._serialized_end = 1603
    _globals['_AUDIOINCONFIG_ENCODING']._serialized_start = 1543
    _globals['_AUDIOINCONFIG_ENCODING']._serialized_end = 1603
    _globals['_AUDIOOUTCONFIG']._serialized_start = 1606
    _globals['_AUDIOOUTCONFIG']._serialized_end = 1833
    _globals['_AUDIOOUTCONFIG_ENCODING']._serialized_start = 1757
    _globals['_AUDIOOUTCONFIG_ENCODING']._serialized_end = 1833
    _globals['_SCREENOUTCONFIG']._serialized_start = 1836
    _globals['_SCREENOUTCONFIG']._serialized_end = 2003
    _globals['_SCREENOUTCONFIG_SCREENMODE']._serialized_start = 1940
    _globals['_SCREENOUTCONFIG_SCREENMODE']._serialized_end = 2003
    _globals['_DIALOGSTATEIN']._serialized_start = 2006
    _globals['_DIALOGSTATEIN']._serialized_end = 2178
    _globals['_DEVICECONFIG']._serialized_start = 2180
    _globals['_DEVICECONFIG']._serialized_end = 2238
    _globals['_AUDIOOUT']._serialized_start = 2240
    _globals['_AUDIOOUT']._serialized_end = 2270
    _globals['_SCREENOUT']._serialized_start = 2273
    _globals['_SCREENOUT']._serialized_end = 2412
    _globals['_SCREENOUT_FORMAT']._serialized_start = 2370
    _globals['_SCREENOUT_FORMAT']._serialized_end = 2412
    _globals['_DEVICEACTION']._serialized_start = 2414
    _globals['_DEVICEACTION']._serialized_end = 2457
    _globals['_SPEECHRECOGNITIONRESULT']._serialized_start = 2459
    _globals['_SPEECHRECOGNITIONRESULT']._serialized_end = 2523
    _globals['_DIALOGSTATEOUT']._serialized_start = 2526
    _globals['_DIALOGSTATEOUT']._serialized_end = 2819
    _globals['_DIALOGSTATEOUT_MICROPHONEMODE']._serialized_start = 2726
    _globals['_DIALOGSTATEOUT_MICROPHONEMODE']._serialized_end = 2819
    _globals['_DEBUGCONFIG']._serialized_start = 2821
    _globals['_DEBUGCONFIG']._serialized_end = 2861
    _globals['_DEVICELOCATION']._serialized_start = 2863
    _globals['_DEVICELOCATION']._serialized_end = 2931
    _globals['_EMBEDDEDASSISTANT']._serialized_start = 2934
    _globals['_EMBEDDEDASSISTANT']._serialized_end = 3070