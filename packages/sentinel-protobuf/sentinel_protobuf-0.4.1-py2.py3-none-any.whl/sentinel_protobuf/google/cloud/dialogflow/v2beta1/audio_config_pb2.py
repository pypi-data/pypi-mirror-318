"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/audio_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/v2beta1/audio_config.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto"9\n\rSpeechContext\x12\x14\n\x07phrases\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x12\n\x05boost\x18\x02 \x01(\x02B\x03\xe0A\x01"\x92\x01\n\x0eSpeechWordInfo\x12\x0c\n\x04word\x18\x03 \x01(\t\x12/\n\x0cstart_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12-\n\nend_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\nconfidence\x18\x04 \x01(\x02"{\n\rBargeInConfig\x127\n\x14no_barge_in_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x121\n\x0etotal_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xcc\x05\n\x10InputAudioConfig\x12K\n\x0eaudio_encoding\x18\x01 \x01(\x0e2..google.cloud.dialogflow.v2beta1.AudioEncodingB\x03\xe0A\x02\x12\x1e\n\x11sample_rate_hertz\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x10enable_word_info\x18\r \x01(\x08\x12\x18\n\x0cphrase_hints\x18\x04 \x03(\tB\x02\x18\x01\x12G\n\x0fspeech_contexts\x18\x0b \x03(\x0b2..google.cloud.dialogflow.v2beta1.SpeechContext\x12\r\n\x05model\x18\x07 \x01(\t\x12J\n\rmodel_variant\x18\n \x01(\x0e23.google.cloud.dialogflow.v2beta1.SpeechModelVariant\x12\x18\n\x10single_utterance\x18\x08 \x01(\x08\x12*\n"disable_no_speech_recognized_event\x18\x0e \x01(\x08\x12G\n\x0fbarge_in_config\x18\x0f \x01(\x0b2..google.cloud.dialogflow.v2beta1.BargeInConfig\x12$\n\x1cenable_automatic_punctuation\x18\x11 \x01(\x08\x12<\n\x19default_no_speech_timeout\x18\x12 \x01(\x0b2\x19.google.protobuf.Duration\x129\n\x0bphrase_sets\x18\x14 \x03(\tB$\xfaA!\n\x1fspeech.googleapis.com/PhraseSet\x12)\n!opt_out_conformer_model_migration\x18\x1a \x01(\x08"u\n\x14VoiceSelectionParams\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12J\n\x0bssml_gender\x18\x02 \x01(\x0e20.google.cloud.dialogflow.v2beta1.SsmlVoiceGenderB\x03\xe0A\x01"\xd1\x01\n\x16SynthesizeSpeechConfig\x12\x1a\n\rspeaking_rate\x18\x01 \x01(\x01B\x03\xe0A\x01\x12\x12\n\x05pitch\x18\x02 \x01(\x01B\x03\xe0A\x01\x12\x1b\n\x0evolume_gain_db\x18\x03 \x01(\x01B\x03\xe0A\x01\x12\x1f\n\x12effects_profile_id\x18\x05 \x03(\tB\x03\xe0A\x01\x12I\n\x05voice\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.VoiceSelectionParamsB\x03\xe0A\x01"\xdc\x01\n\x11OutputAudioConfig\x12Q\n\x0eaudio_encoding\x18\x01 \x01(\x0e24.google.cloud.dialogflow.v2beta1.OutputAudioEncodingB\x03\xe0A\x02\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12Y\n\x18synthesize_speech_config\x18\x03 \x01(\x0b27.google.cloud.dialogflow.v2beta1.SynthesizeSpeechConfig"Z\n\x13TelephonyDtmfEvents\x12C\n\x0bdtmf_events\x18\x01 \x03(\x0e2..google.cloud.dialogflow.v2beta1.TelephonyDtmf"\xec\x02\n\x12SpeechToTextConfig\x12Q\n\x14speech_model_variant\x18\x01 \x01(\x0e23.google.cloud.dialogflow.v2beta1.SpeechModelVariant\x12\r\n\x05model\x18\x02 \x01(\t\x129\n\x0bphrase_sets\x18\x04 \x03(\tB$\xfaA!\n\x1fspeech.googleapis.com/PhraseSet\x12F\n\x0eaudio_encoding\x18\x06 \x01(\x0e2..google.cloud.dialogflow.v2beta1.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x07 \x01(\x05\x12\x15\n\rlanguage_code\x18\x08 \x01(\t\x12\x18\n\x10enable_word_info\x18\t \x01(\x08\x12%\n\x1duse_timeout_based_endpointing\x18\x0b \x01(\x08*\x94\x02\n\rTelephonyDtmf\x12\x1e\n\x1aTELEPHONY_DTMF_UNSPECIFIED\x10\x00\x12\x0c\n\x08DTMF_ONE\x10\x01\x12\x0c\n\x08DTMF_TWO\x10\x02\x12\x0e\n\nDTMF_THREE\x10\x03\x12\r\n\tDTMF_FOUR\x10\x04\x12\r\n\tDTMF_FIVE\x10\x05\x12\x0c\n\x08DTMF_SIX\x10\x06\x12\x0e\n\nDTMF_SEVEN\x10\x07\x12\x0e\n\nDTMF_EIGHT\x10\x08\x12\r\n\tDTMF_NINE\x10\t\x12\r\n\tDTMF_ZERO\x10\n\x12\n\n\x06DTMF_A\x10\x0b\x12\n\n\x06DTMF_B\x10\x0c\x12\n\n\x06DTMF_C\x10\r\x12\n\n\x06DTMF_D\x10\x0e\x12\r\n\tDTMF_STAR\x10\x0f\x12\x0e\n\nDTMF_POUND\x10\x10*\x94\x02\n\rAudioEncoding\x12\x1e\n\x1aAUDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x1c\n\x18AUDIO_ENCODING_LINEAR_16\x10\x01\x12\x17\n\x13AUDIO_ENCODING_FLAC\x10\x02\x12\x18\n\x14AUDIO_ENCODING_MULAW\x10\x03\x12\x16\n\x12AUDIO_ENCODING_AMR\x10\x04\x12\x19\n\x15AUDIO_ENCODING_AMR_WB\x10\x05\x12\x1b\n\x17AUDIO_ENCODING_OGG_OPUS\x10\x06\x12)\n%AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE\x10\x07\x12\x17\n\x13AUDIO_ENCODING_ALAW\x10\x08*v\n\x12SpeechModelVariant\x12$\n SPEECH_MODEL_VARIANT_UNSPECIFIED\x10\x00\x12\x16\n\x12USE_BEST_AVAILABLE\x10\x01\x12\x10\n\x0cUSE_STANDARD\x10\x02\x12\x10\n\x0cUSE_ENHANCED\x10\x03*\x8d\x01\n\x0fSsmlVoiceGender\x12!\n\x1dSSML_VOICE_GENDER_UNSPECIFIED\x10\x00\x12\x1a\n\x16SSML_VOICE_GENDER_MALE\x10\x01\x12\x1c\n\x18SSML_VOICE_GENDER_FEMALE\x10\x02\x12\x1d\n\x19SSML_VOICE_GENDER_NEUTRAL\x10\x03*\x8c\x02\n\x13OutputAudioEncoding\x12%\n!OUTPUT_AUDIO_ENCODING_UNSPECIFIED\x10\x00\x12#\n\x1fOUTPUT_AUDIO_ENCODING_LINEAR_16\x10\x01\x12\x1d\n\x19OUTPUT_AUDIO_ENCODING_MP3\x10\x02\x12%\n!OUTPUT_AUDIO_ENCODING_MP3_64_KBPS\x10\x04\x12"\n\x1eOUTPUT_AUDIO_ENCODING_OGG_OPUS\x10\x03\x12\x1f\n\x1bOUTPUT_AUDIO_ENCODING_MULAW\x10\x05\x12\x1e\n\x1aOUTPUT_AUDIO_ENCODING_ALAW\x10\x06B\xe2\x02\n#com.google.cloud.dialogflow.v2beta1B\x10AudioConfigProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}\xeaAb\n\x1fspeech.googleapis.com/PhraseSet\x12?projects/{project}/locations/{location}/phraseSets/{phrase_set}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.audio_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x10AudioConfigProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}\xeaAb\n\x1fspeech.googleapis.com/PhraseSet\x12?projects/{project}/locations/{location}/phraseSets/{phrase_set}'
    _globals['_SPEECHCONTEXT'].fields_by_name['phrases']._loaded_options = None
    _globals['_SPEECHCONTEXT'].fields_by_name['phrases']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHCONTEXT'].fields_by_name['boost']._loaded_options = None
    _globals['_SPEECHCONTEXT'].fields_by_name['boost']._serialized_options = b'\xe0A\x01'
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['sample_rate_hertz']._loaded_options = None
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['sample_rate_hertz']._serialized_options = b'\xe0A\x02'
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['language_code']._loaded_options = None
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['phrase_hints']._loaded_options = None
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['phrase_hints']._serialized_options = b'\x18\x01'
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['phrase_sets']._loaded_options = None
    _globals['_INPUTAUDIOCONFIG'].fields_by_name['phrase_sets']._serialized_options = b'\xfaA!\n\x1fspeech.googleapis.com/PhraseSet'
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['name']._loaded_options = None
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['ssml_gender']._loaded_options = None
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['ssml_gender']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['speaking_rate']._loaded_options = None
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['speaking_rate']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['pitch']._loaded_options = None
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['pitch']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['volume_gain_db']._loaded_options = None
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['volume_gain_db']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['effects_profile_id']._loaded_options = None
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['effects_profile_id']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['voice']._loaded_options = None
    _globals['_SYNTHESIZESPEECHCONFIG'].fields_by_name['voice']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_OUTPUTAUDIOCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_SPEECHTOTEXTCONFIG'].fields_by_name['phrase_sets']._loaded_options = None
    _globals['_SPEECHTOTEXTCONFIG'].fields_by_name['phrase_sets']._serialized_options = b'\xfaA!\n\x1fspeech.googleapis.com/PhraseSet'
    _globals['_TELEPHONYDTMF']._serialized_start = 2245
    _globals['_TELEPHONYDTMF']._serialized_end = 2521
    _globals['_AUDIOENCODING']._serialized_start = 2524
    _globals['_AUDIOENCODING']._serialized_end = 2800
    _globals['_SPEECHMODELVARIANT']._serialized_start = 2802
    _globals['_SPEECHMODELVARIANT']._serialized_end = 2920
    _globals['_SSMLVOICEGENDER']._serialized_start = 2923
    _globals['_SSMLVOICEGENDER']._serialized_end = 3064
    _globals['_OUTPUTAUDIOENCODING']._serialized_start = 3067
    _globals['_OUTPUTAUDIOENCODING']._serialized_end = 3335
    _globals['_SPEECHCONTEXT']._serialized_start = 179
    _globals['_SPEECHCONTEXT']._serialized_end = 236
    _globals['_SPEECHWORDINFO']._serialized_start = 239
    _globals['_SPEECHWORDINFO']._serialized_end = 385
    _globals['_BARGEINCONFIG']._serialized_start = 387
    _globals['_BARGEINCONFIG']._serialized_end = 510
    _globals['_INPUTAUDIOCONFIG']._serialized_start = 513
    _globals['_INPUTAUDIOCONFIG']._serialized_end = 1229
    _globals['_VOICESELECTIONPARAMS']._serialized_start = 1231
    _globals['_VOICESELECTIONPARAMS']._serialized_end = 1348
    _globals['_SYNTHESIZESPEECHCONFIG']._serialized_start = 1351
    _globals['_SYNTHESIZESPEECHCONFIG']._serialized_end = 1560
    _globals['_OUTPUTAUDIOCONFIG']._serialized_start = 1563
    _globals['_OUTPUTAUDIOCONFIG']._serialized_end = 1783
    _globals['_TELEPHONYDTMFEVENTS']._serialized_start = 1785
    _globals['_TELEPHONYDTMFEVENTS']._serialized_end = 1875
    _globals['_SPEECHTOTEXTCONFIG']._serialized_start = 1878
    _globals['_SPEECHTOTEXTCONFIG']._serialized_end = 2242