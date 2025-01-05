"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/audio_config.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dialogflow/cx/v3/audio_config.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto"\x92\x01\n\x0eSpeechWordInfo\x12\x0c\n\x04word\x18\x03 \x01(\t\x12/\n\x0cstart_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12-\n\nend_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\nconfidence\x18\x04 \x01(\x02"{\n\rBargeInConfig\x127\n\x14no_barge_in_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x121\n\x0etotal_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\x8d\x03\n\x10InputAudioConfig\x12I\n\x0eaudio_encoding\x18\x01 \x01(\x0e2,.google.cloud.dialogflow.cx.v3.AudioEncodingB\x03\xe0A\x02\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x18\n\x10enable_word_info\x18\r \x01(\x08\x12\x14\n\x0cphrase_hints\x18\x04 \x03(\t\x12\r\n\x05model\x18\x07 \x01(\t\x12H\n\rmodel_variant\x18\n \x01(\x0e21.google.cloud.dialogflow.cx.v3.SpeechModelVariant\x12\x18\n\x10single_utterance\x18\x08 \x01(\x08\x12E\n\x0fbarge_in_config\x18\x0f \x01(\x0b2,.google.cloud.dialogflow.cx.v3.BargeInConfig\x12)\n!opt_out_conformer_model_migration\x18\x1a \x01(\x08"i\n\x14VoiceSelectionParams\x12\x0c\n\x04name\x18\x01 \x01(\t\x12C\n\x0bssml_gender\x18\x02 \x01(\x0e2..google.cloud.dialogflow.cx.v3.SsmlVoiceGender"\xb6\x01\n\x16SynthesizeSpeechConfig\x12\x15\n\rspeaking_rate\x18\x01 \x01(\x01\x12\r\n\x05pitch\x18\x02 \x01(\x01\x12\x16\n\x0evolume_gain_db\x18\x03 \x01(\x01\x12\x1a\n\x12effects_profile_id\x18\x05 \x03(\t\x12B\n\x05voice\x18\x04 \x01(\x0b23.google.cloud.dialogflow.cx.v3.VoiceSelectionParams"\xd8\x01\n\x11OutputAudioConfig\x12O\n\x0eaudio_encoding\x18\x01 \x01(\x0e22.google.cloud.dialogflow.cx.v3.OutputAudioEncodingB\x03\xe0A\x02\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12W\n\x18synthesize_speech_config\x18\x03 \x01(\x0b25.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig"\x82\x02\n\x14TextToSpeechSettings\x12s\n\x19synthesize_speech_configs\x18\x01 \x03(\x0b2P.google.cloud.dialogflow.cx.v3.TextToSpeechSettings.SynthesizeSpeechConfigsEntry\x1au\n\x1cSynthesizeSpeechConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12D\n\x05value\x18\x02 \x01(\x0b25.google.cloud.dialogflow.cx.v3.SynthesizeSpeechConfig:\x028\x01*\x94\x02\n\rAudioEncoding\x12\x1e\n\x1aAUDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x1c\n\x18AUDIO_ENCODING_LINEAR_16\x10\x01\x12\x17\n\x13AUDIO_ENCODING_FLAC\x10\x02\x12\x18\n\x14AUDIO_ENCODING_MULAW\x10\x03\x12\x16\n\x12AUDIO_ENCODING_AMR\x10\x04\x12\x19\n\x15AUDIO_ENCODING_AMR_WB\x10\x05\x12\x1b\n\x17AUDIO_ENCODING_OGG_OPUS\x10\x06\x12)\n%AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE\x10\x07\x12\x17\n\x13AUDIO_ENCODING_ALAW\x10\x08*v\n\x12SpeechModelVariant\x12$\n SPEECH_MODEL_VARIANT_UNSPECIFIED\x10\x00\x12\x16\n\x12USE_BEST_AVAILABLE\x10\x01\x12\x10\n\x0cUSE_STANDARD\x10\x02\x12\x10\n\x0cUSE_ENHANCED\x10\x03*\x8d\x01\n\x0fSsmlVoiceGender\x12!\n\x1dSSML_VOICE_GENDER_UNSPECIFIED\x10\x00\x12\x1a\n\x16SSML_VOICE_GENDER_MALE\x10\x01\x12\x1c\n\x18SSML_VOICE_GENDER_FEMALE\x10\x02\x12\x1d\n\x19SSML_VOICE_GENDER_NEUTRAL\x10\x03*\x8c\x02\n\x13OutputAudioEncoding\x12%\n!OUTPUT_AUDIO_ENCODING_UNSPECIFIED\x10\x00\x12#\n\x1fOUTPUT_AUDIO_ENCODING_LINEAR_16\x10\x01\x12\x1d\n\x19OUTPUT_AUDIO_ENCODING_MP3\x10\x02\x12%\n!OUTPUT_AUDIO_ENCODING_MP3_64_KBPS\x10\x04\x12"\n\x1eOUTPUT_AUDIO_ENCODING_OGG_OPUS\x10\x03\x12\x1f\n\x1bOUTPUT_AUDIO_ENCODING_MULAW\x10\x05\x12\x1e\n\x1aOUTPUT_AUDIO_ENCODING_ALAW\x10\x06B\x8e\x02\n!com.google.cloud.dialogflow.cx.v3B\x10AudioConfigProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.audio_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x10AudioConfigProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}'
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_OUTPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._loaded_options = None
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_options = b'8\x01'
    _globals['_AUDIOENCODING']._serialized_start = 1622
    _globals['_AUDIOENCODING']._serialized_end = 1898
    _globals['_SPEECHMODELVARIANT']._serialized_start = 1900
    _globals['_SPEECHMODELVARIANT']._serialized_end = 2018
    _globals['_SSMLVOICEGENDER']._serialized_start = 2021
    _globals['_SSMLVOICEGENDER']._serialized_end = 2162
    _globals['_OUTPUTAUDIOENCODING']._serialized_start = 2165
    _globals['_OUTPUTAUDIOENCODING']._serialized_end = 2433
    _globals['_SPEECHWORDINFO']._serialized_start = 176
    _globals['_SPEECHWORDINFO']._serialized_end = 322
    _globals['_BARGEINCONFIG']._serialized_start = 324
    _globals['_BARGEINCONFIG']._serialized_end = 447
    _globals['_INPUTAUDIOCONFIG']._serialized_start = 450
    _globals['_INPUTAUDIOCONFIG']._serialized_end = 847
    _globals['_VOICESELECTIONPARAMS']._serialized_start = 849
    _globals['_VOICESELECTIONPARAMS']._serialized_end = 954
    _globals['_SYNTHESIZESPEECHCONFIG']._serialized_start = 957
    _globals['_SYNTHESIZESPEECHCONFIG']._serialized_end = 1139
    _globals['_OUTPUTAUDIOCONFIG']._serialized_start = 1142
    _globals['_OUTPUTAUDIOCONFIG']._serialized_end = 1358
    _globals['_TEXTTOSPEECHSETTINGS']._serialized_start = 1361
    _globals['_TEXTTOSPEECHSETTINGS']._serialized_end = 1619
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_start = 1502
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_end = 1619