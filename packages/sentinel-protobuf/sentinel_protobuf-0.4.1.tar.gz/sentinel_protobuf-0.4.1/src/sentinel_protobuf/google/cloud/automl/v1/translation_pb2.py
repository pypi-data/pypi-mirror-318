"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/translation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.automl.v1 import data_items_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_data__items__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/automl/v1/translation.proto\x12\x16google.cloud.automl.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\'google/cloud/automl/v1/data_items.proto"b\n\x1aTranslationDatasetMetadata\x12!\n\x14source_language_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14target_language_code\x18\x02 \x01(\tB\x03\xe0A\x02"K\n\x1cTranslationEvaluationMetrics\x12\x12\n\nbleu_score\x18\x01 \x01(\x01\x12\x17\n\x0fbase_bleu_score\x18\x02 \x01(\x01"j\n\x18TranslationModelMetadata\x12\x12\n\nbase_model\x18\x01 \x01(\t\x12\x1c\n\x14source_language_code\x18\x02 \x01(\t\x12\x1c\n\x14target_language_code\x18\x03 \x01(\t"X\n\x15TranslationAnnotation\x12?\n\x12translated_content\x18\x01 \x01(\x0b2#.google.cloud.automl.v1.TextSnippetB\xb2\x01\n\x1acom.google.cloud.automl.v1B\x10TranslationProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.translation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1B\x10TranslationProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['source_language_code']._loaded_options = None
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['source_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['target_language_code']._loaded_options = None
    _globals['_TRANSLATIONDATASETMETADATA'].fields_by_name['target_language_code']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSLATIONDATASETMETADATA']._serialized_start = 142
    _globals['_TRANSLATIONDATASETMETADATA']._serialized_end = 240
    _globals['_TRANSLATIONEVALUATIONMETRICS']._serialized_start = 242
    _globals['_TRANSLATIONEVALUATIONMETRICS']._serialized_end = 317
    _globals['_TRANSLATIONMODELMETADATA']._serialized_start = 319
    _globals['_TRANSLATIONMODELMETADATA']._serialized_end = 425
    _globals['_TRANSLATIONANNOTATION']._serialized_start = 427
    _globals['_TRANSLATIONANNOTATION']._serialized_end = 515