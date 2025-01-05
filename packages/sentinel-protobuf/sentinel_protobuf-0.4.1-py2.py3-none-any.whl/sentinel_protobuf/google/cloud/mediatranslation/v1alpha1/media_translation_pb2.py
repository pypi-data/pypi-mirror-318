"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/mediatranslation/v1alpha1/media_translation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/mediatranslation/v1alpha1/media_translation.proto\x12&google.cloud.mediatranslation.v1alpha1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto"\xde\x01\n\x15TranslateSpeechConfig\x12\x1b\n\x0eaudio_encoding\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14source_language_code\x18\x02 \x01(\tB\x03\xe0A\x02\x12!\n\x14target_language_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12.\n!alternative_source_language_codes\x18\x06 \x03(\tB\x03\xe0A\x01\x12\x1e\n\x11sample_rate_hertz\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x12\n\x05model\x18\x05 \x01(\tB\x03\xe0A\x01"\xf6\x01\n\x1eStreamingTranslateSpeechConfig\x12X\n\x0caudio_config\x18\x01 \x01(\x0b2=.google.cloud.mediatranslation.v1alpha1.TranslateSpeechConfigB\x03\xe0A\x02\x12\x1d\n\x10single_utterance\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x16\n\tstability\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10translation_mode\x18\x04 \x01(\tB\x03\xe0A\x01\x12$\n\x17disable_interim_results\x18\x05 \x01(\x08B\x03\xe0A\x01"\xb3\x01\n\x1fStreamingTranslateSpeechRequest\x12b\n\x10streaming_config\x18\x01 \x01(\x0b2F.google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00B\x13\n\x11streaming_request"\xf1\x03\n\x1eStreamingTranslateSpeechResult\x12}\n\x17text_translation_result\x18\x01 \x01(\x0b2\\.google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechResult.TextTranslationResult\x12\x7f\n\x18audio_translation_result\x18\x02 \x01(\x0b2].google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechResult.AudioTranslationResult\x12\x1f\n\x12recognition_result\x18\x03 \x01(\tB\x03\xe0A\x03\x12*\n\x1ddetected_source_language_code\x18\x04 \x01(\tB\x03\xe0A\x03\x1aH\n\x15TextTranslationResult\x12\x18\n\x0btranslation\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08is_final\x18\x02 \x01(\x08B\x03\xe0A\x03\x1a8\n\x16AudioTranslationResult\x12\x1e\n\x11audio_translation\x18\x01 \x01(\x0cB\x03\xe0A\x03"\xf4\x02\n StreamingTranslateSpeechResponse\x12&\n\x05error\x18\x01 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12[\n\x06result\x18\x02 \x01(\x0b2F.google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechResultB\x03\xe0A\x03\x12x\n\x11speech_event_type\x18\x03 \x01(\x0e2X.google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechResponse.SpeechEventTypeB\x03\xe0A\x03"Q\n\x0fSpeechEventType\x12!\n\x1dSPEECH_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17END_OF_SINGLE_UTTERANCE\x10\x012\xa5\x02\n\x18SpeechTranslationService\x12\xb3\x01\n\x18StreamingTranslateSpeech\x12G.google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechRequest\x1aH.google.cloud.mediatranslation.v1alpha1.StreamingTranslateSpeechResponse"\x00(\x010\x01\x1aS\xcaA\x1fmediatranslation.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x87\x01\n*com.google.cloud.mediatranslation.v1alpha1ZVcloud.google.com/go/mediatranslation/apiv1alpha1/mediatranslationpb;mediatranslationpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.mediatranslation.v1alpha1.media_translation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.mediatranslation.v1alpha1ZVcloud.google.com/go/mediatranslation/apiv1alpha1/mediatranslationpb;mediatranslationpb\xf8\x01\x01'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['source_language_code']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['source_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['target_language_code']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['target_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['alternative_source_language_codes']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['alternative_source_language_codes']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['sample_rate_hertz']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['sample_rate_hertz']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['model']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['model']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['audio_config']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['audio_config']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['single_utterance']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['single_utterance']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['stability']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['stability']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['translation_mode']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['translation_mode']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['disable_interim_results']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['disable_interim_results']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['translation']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['translation']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['is_final']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['is_final']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESULT_AUDIOTRANSLATIONRESULT'].fields_by_name['audio_translation']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT_AUDIOTRANSLATIONRESULT'].fields_by_name['audio_translation']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESULT'].fields_by_name['recognition_result']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT'].fields_by_name['recognition_result']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESULT'].fields_by_name['detected_source_language_code']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT'].fields_by_name['detected_source_language_code']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['error']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['result']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['result']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['speech_event_type']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['speech_event_type']._serialized_options = b'\xe0A\x03'
    _globals['_SPEECHTRANSLATIONSERVICE']._loaded_options = None
    _globals['_SPEECHTRANSLATIONSERVICE']._serialized_options = b'\xcaA\x1fmediatranslation.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TRANSLATESPEECHCONFIG']._serialized_start = 190
    _globals['_TRANSLATESPEECHCONFIG']._serialized_end = 412
    _globals['_STREAMINGTRANSLATESPEECHCONFIG']._serialized_start = 415
    _globals['_STREAMINGTRANSLATESPEECHCONFIG']._serialized_end = 661
    _globals['_STREAMINGTRANSLATESPEECHREQUEST']._serialized_start = 664
    _globals['_STREAMINGTRANSLATESPEECHREQUEST']._serialized_end = 843
    _globals['_STREAMINGTRANSLATESPEECHRESULT']._serialized_start = 846
    _globals['_STREAMINGTRANSLATESPEECHRESULT']._serialized_end = 1343
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT']._serialized_start = 1213
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT']._serialized_end = 1285
    _globals['_STREAMINGTRANSLATESPEECHRESULT_AUDIOTRANSLATIONRESULT']._serialized_start = 1287
    _globals['_STREAMINGTRANSLATESPEECHRESULT_AUDIOTRANSLATIONRESULT']._serialized_end = 1343
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE']._serialized_start = 1346
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE']._serialized_end = 1718
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE_SPEECHEVENTTYPE']._serialized_start = 1637
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE_SPEECHEVENTTYPE']._serialized_end = 1718
    _globals['_SPEECHTRANSLATIONSERVICE']._serialized_start = 1721
    _globals['_SPEECHTRANSLATIONSERVICE']._serialized_end = 2014