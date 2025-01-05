"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/mediatranslation/v1beta1/media_translation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/mediatranslation/v1beta1/media_translation.proto\x12%google.cloud.mediatranslation.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto"\xae\x01\n\x15TranslateSpeechConfig\x12\x1b\n\x0eaudio_encoding\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14source_language_code\x18\x02 \x01(\tB\x03\xe0A\x02\x12!\n\x14target_language_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11sample_rate_hertz\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x12\n\x05model\x18\x05 \x01(\tB\x03\xe0A\x01"\x98\x01\n\x1eStreamingTranslateSpeechConfig\x12W\n\x0caudio_config\x18\x01 \x01(\x0b2<.google.cloud.mediatranslation.v1beta1.TranslateSpeechConfigB\x03\xe0A\x02\x12\x1d\n\x10single_utterance\x18\x02 \x01(\x08B\x03\xe0A\x01"\xb2\x01\n\x1fStreamingTranslateSpeechRequest\x12a\n\x10streaming_config\x18\x01 \x01(\x0b2E.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00B\x13\n\x11streaming_request"\xf4\x01\n\x1eStreamingTranslateSpeechResult\x12~\n\x17text_translation_result\x18\x01 \x01(\x0b2[.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResult.TextTranslationResultH\x00\x1aH\n\x15TextTranslationResult\x12\x18\n\x0btranslation\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08is_final\x18\x02 \x01(\x08B\x03\xe0A\x03B\x08\n\x06result"\xf2\x02\n StreamingTranslateSpeechResponse\x12&\n\x05error\x18\x01 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12Z\n\x06result\x18\x02 \x01(\x0b2E.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResultB\x03\xe0A\x03\x12w\n\x11speech_event_type\x18\x03 \x01(\x0e2W.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse.SpeechEventTypeB\x03\xe0A\x03"Q\n\x0fSpeechEventType\x12!\n\x1dSPEECH_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17END_OF_SINGLE_UTTERANCE\x10\x012\xa3\x02\n\x18SpeechTranslationService\x12\xb1\x01\n\x18StreamingTranslateSpeech\x12F.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechRequest\x1aG.google.cloud.mediatranslation.v1beta1.StreamingTranslateSpeechResponse"\x00(\x010\x01\x1aS\xcaA\x1fmediatranslation.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x99\x02\n)com.google.cloud.mediatranslation.v1beta1B\x15MediaTranslationProtoP\x01ZUcloud.google.com/go/mediatranslation/apiv1beta1/mediatranslationpb;mediatranslationpb\xf8\x01\x01\xaa\x02%Google.Cloud.MediaTranslation.V1Beta1\xca\x02%Google\\Cloud\\MediaTranslation\\V1beta1\xea\x02(Google::Cloud::MediaTranslation::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.mediatranslation.v1beta1.media_translation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.mediatranslation.v1beta1B\x15MediaTranslationProtoP\x01ZUcloud.google.com/go/mediatranslation/apiv1beta1/mediatranslationpb;mediatranslationpb\xf8\x01\x01\xaa\x02%Google.Cloud.MediaTranslation.V1Beta1\xca\x02%Google\\Cloud\\MediaTranslation\\V1beta1\xea\x02(Google::Cloud::MediaTranslation::V1beta1'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['source_language_code']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['source_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['target_language_code']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['target_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['sample_rate_hertz']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['sample_rate_hertz']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['model']._loaded_options = None
    _globals['_TRANSLATESPEECHCONFIG'].fields_by_name['model']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['audio_config']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['audio_config']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['single_utterance']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHCONFIG'].fields_by_name['single_utterance']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['translation']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['translation']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['is_final']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT'].fields_by_name['is_final']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['error']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['result']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['result']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['speech_event_type']._loaded_options = None
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE'].fields_by_name['speech_event_type']._serialized_options = b'\xe0A\x03'
    _globals['_SPEECHTRANSLATIONSERVICE']._loaded_options = None
    _globals['_SPEECHTRANSLATIONSERVICE']._serialized_options = b'\xcaA\x1fmediatranslation.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TRANSLATESPEECHCONFIG']._serialized_start = 188
    _globals['_TRANSLATESPEECHCONFIG']._serialized_end = 362
    _globals['_STREAMINGTRANSLATESPEECHCONFIG']._serialized_start = 365
    _globals['_STREAMINGTRANSLATESPEECHCONFIG']._serialized_end = 517
    _globals['_STREAMINGTRANSLATESPEECHREQUEST']._serialized_start = 520
    _globals['_STREAMINGTRANSLATESPEECHREQUEST']._serialized_end = 698
    _globals['_STREAMINGTRANSLATESPEECHRESULT']._serialized_start = 701
    _globals['_STREAMINGTRANSLATESPEECHRESULT']._serialized_end = 945
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT']._serialized_start = 863
    _globals['_STREAMINGTRANSLATESPEECHRESULT_TEXTTRANSLATIONRESULT']._serialized_end = 935
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE']._serialized_start = 948
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE']._serialized_end = 1318
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE_SPEECHEVENTTYPE']._serialized_start = 1237
    _globals['_STREAMINGTRANSLATESPEECHRESPONSE_SPEECHEVENTTYPE']._serialized_end = 1318
    _globals['_SPEECHTRANSLATIONSERVICE']._serialized_start = 1321
    _globals['_SPEECHTRANSLATIONSERVICE']._serialized_end = 1612