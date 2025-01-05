"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/text_sentiment.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_classification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/automl/v1beta1/text_sentiment.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a0google/cloud/automl/v1beta1/classification.proto",\n\x17TextSentimentAnnotation\x12\x11\n\tsentiment\x18\x01 \x01(\x05"\xc5\x02\n\x1eTextSentimentEvaluationMetrics\x12\x11\n\tprecision\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x10\n\x08f1_score\x18\x03 \x01(\x02\x12\x1b\n\x13mean_absolute_error\x18\x04 \x01(\x02\x12\x1a\n\x12mean_squared_error\x18\x05 \x01(\x02\x12\x14\n\x0clinear_kappa\x18\x06 \x01(\x02\x12\x17\n\x0fquadratic_kappa\x18\x07 \x01(\x02\x12f\n\x10confusion_matrix\x18\x08 \x01(\x0b2L.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix\x12\x1e\n\x12annotation_spec_id\x18\t \x03(\tB\x02\x18\x01B\xad\x01\n\x1fcom.google.cloud.automl.v1beta1B\x12TextSentimentProtoZ7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.text_sentiment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\x12TextSentimentProtoZ7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TEXTSENTIMENTEVALUATIONMETRICS'].fields_by_name['annotation_spec_id']._loaded_options = None
    _globals['_TEXTSENTIMENTEVALUATIONMETRICS'].fields_by_name['annotation_spec_id']._serialized_options = b'\x18\x01'
    _globals['_TEXTSENTIMENTANNOTATION']._serialized_start = 131
    _globals['_TEXTSENTIMENTANNOTATION']._serialized_end = 175
    _globals['_TEXTSENTIMENTEVALUATIONMETRICS']._serialized_start = 178
    _globals['_TEXTSENTIMENTEVALUATIONMETRICS']._serialized_end = 503