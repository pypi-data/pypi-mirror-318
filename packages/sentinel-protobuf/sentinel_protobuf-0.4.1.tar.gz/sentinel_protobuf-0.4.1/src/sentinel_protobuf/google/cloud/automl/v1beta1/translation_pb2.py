"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/translation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.automl.v1beta1 import data_items_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/automl/v1beta1/translation.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/automl/v1beta1/data_items.proto"b\n\x1aTranslationDatasetMetadata\x12!\n\x14source_language_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14target_language_code\x18\x02 \x01(\tB\x03\xe0A\x02"K\n\x1cTranslationEvaluationMetrics\x12\x12\n\nbleu_score\x18\x01 \x01(\x01\x12\x17\n\x0fbase_bleu_score\x18\x02 \x01(\x01"j\n\x18TranslationModelMetadata\x12\x12\n\nbase_model\x18\x01 \x01(\t\x12\x1c\n\x14source_language_code\x18\x02 \x01(\t\x12\x1c\n\x14target_language_code\x18\x03 \x01(\t"]\n\x15TranslationAnnotation\x12D\n\x12translated_content\x18\x01 \x01(\x0b2(.google.cloud.automl.v1beta1.TextSnippetB\xad\x01\n\x1fcom.google.cloud.automl.v1beta1B\x10TranslationProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.translation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\x10TranslationProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['source_language_code']._loaded_options = None
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['source_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['target_language_code']._loaded_options = None
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['target_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATIONDATASETMETADATA']._serialized_start = 157
    _globals['_TRANSLATIONDATASETMETADATA']._serialized_end = 255
    _globals['_TRANSLATIONEVALUATIONMETRICS']._serialized_start = 257
    _globals['_TRANSLATIONEVALUATIONMETRICS']._serialized_end = 332
    _globals['_TRANSLATIONMODELMETADATA']._serialized_start = 334
    _globals['_TRANSLATIONMODELMETADATA']._serialized_end = 440
    _globals['_TRANSLATIONANNOTATION']._serialized_start = 442
    _globals['_TRANSLATIONANNOTATION']._serialized_end = 535