"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/speech/v1p1beta1/resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/speech/v1p1beta1/resource.proto\x12\x1dgoogle.cloud.speech.v1p1beta1\x1a\x19google/api/resource.proto"\x83\x02\n\x0bCustomClass\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fcustom_class_id\x18\x02 \x01(\t\x12C\n\x05items\x18\x03 \x03(\x0b24.google.cloud.speech.v1p1beta1.CustomClass.ClassItem\x1a\x1a\n\tClassItem\x12\r\n\x05value\x18\x01 \x01(\t:l\xeaAi\n!speech.googleapis.com/CustomClass\x12Dprojects/{project}/locations/{location}/customClasses/{custom_class}"\xf9\x01\n\tPhraseSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x07phrases\x18\x02 \x03(\x0b2/.google.cloud.speech.v1p1beta1.PhraseSet.Phrase\x12\r\n\x05boost\x18\x04 \x01(\x02\x1a&\n\x06Phrase\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05boost\x18\x02 \x01(\x02:e\xeaAb\n\x1fspeech.googleapis.com/PhraseSet\x12?projects/{project}/locations/{location}/phraseSets/{phrase_set}"\xd2\x02\n\x10SpeechAdaptation\x12=\n\x0bphrase_sets\x18\x01 \x03(\x0b2(.google.cloud.speech.v1p1beta1.PhraseSet\x12C\n\x15phrase_set_references\x18\x02 \x03(\tB$\xfaA!\n\x1fspeech.googleapis.com/PhraseSet\x12B\n\x0ecustom_classes\x18\x03 \x03(\x0b2*.google.cloud.speech.v1p1beta1.CustomClass\x12Q\n\x0cabnf_grammar\x18\x04 \x01(\x0b2;.google.cloud.speech.v1p1beta1.SpeechAdaptation.ABNFGrammar\x1a#\n\x0bABNFGrammar\x12\x14\n\x0cabnf_strings\x18\x01 \x03(\t"\xaa\x01\n\x17TranscriptNormalization\x12M\n\x07entries\x18\x01 \x03(\x0b2<.google.cloud.speech.v1p1beta1.TranscriptNormalization.Entry\x1a@\n\x05Entry\x12\x0e\n\x06search\x18\x01 \x01(\t\x12\x0f\n\x07replace\x18\x02 \x01(\t\x12\x16\n\x0ecase_sensitive\x18\x03 \x01(\x08B~\n!com.google.cloud.speech.v1p1beta1B\x13SpeechResourceProtoP\x01Z9cloud.google.com/go/speech/apiv1p1beta1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.speech.v1p1beta1.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.speech.v1p1beta1B\x13SpeechResourceProtoP\x01Z9cloud.google.com/go/speech/apiv1p1beta1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCS'
    _globals['_CUSTOMCLASS']._loaded_options = None
    _globals['_CUSTOMCLASS']._serialized_options = b'\xeaAi\n!speech.googleapis.com/CustomClass\x12Dprojects/{project}/locations/{location}/customClasses/{custom_class}'
    _globals['_PHRASESET']._loaded_options = None
    _globals['_PHRASESET']._serialized_options = b'\xeaAb\n\x1fspeech.googleapis.com/PhraseSet\x12?projects/{project}/locations/{location}/phraseSets/{phrase_set}'
    _globals['_SPEECHADAPTATION'].fields_by_name['phrase_set_references']._loaded_options = None
    _globals['_SPEECHADAPTATION'].fields_by_name['phrase_set_references']._serialized_options = b'\xfaA!\n\x1fspeech.googleapis.com/PhraseSet'
    _globals['_CUSTOMCLASS']._serialized_start = 107
    _globals['_CUSTOMCLASS']._serialized_end = 366
    _globals['_CUSTOMCLASS_CLASSITEM']._serialized_start = 230
    _globals['_CUSTOMCLASS_CLASSITEM']._serialized_end = 256
    _globals['_PHRASESET']._serialized_start = 369
    _globals['_PHRASESET']._serialized_end = 618
    _globals['_PHRASESET_PHRASE']._serialized_start = 477
    _globals['_PHRASESET_PHRASE']._serialized_end = 515
    _globals['_SPEECHADAPTATION']._serialized_start = 621
    _globals['_SPEECHADAPTATION']._serialized_end = 959
    _globals['_SPEECHADAPTATION_ABNFGRAMMAR']._serialized_start = 924
    _globals['_SPEECHADAPTATION_ABNFGRAMMAR']._serialized_end = 959
    _globals['_TRANSCRIPTNORMALIZATION']._serialized_start = 962
    _globals['_TRANSCRIPTNORMALIZATION']._serialized_end = 1132
    _globals['_TRANSCRIPTNORMALIZATION_ENTRY']._serialized_start = 1068
    _globals['_TRANSCRIPTNORMALIZATION_ENTRY']._serialized_end = 1132