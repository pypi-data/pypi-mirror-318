"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/classification.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/automl/v1/classification.proto\x12\x16google.cloud.automl.v1")\n\x18ClassificationAnnotation\x12\r\n\x05score\x18\x01 \x01(\x02"\x81\x07\n\x1fClassificationEvaluationMetrics\x12\x0e\n\x06au_prc\x18\x01 \x01(\x02\x12\x0e\n\x06au_roc\x18\x06 \x01(\x02\x12\x10\n\x08log_loss\x18\x07 \x01(\x02\x12p\n\x18confidence_metrics_entry\x18\x03 \x03(\x0b2N.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry\x12a\n\x10confusion_matrix\x18\x04 \x01(\x0b2G.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix\x12\x1a\n\x12annotation_spec_id\x18\x05 \x03(\t\x1a\xfc\x02\n\x16ConfidenceMetricsEntry\x12\x1c\n\x14confidence_threshold\x18\x01 \x01(\x02\x12\x1a\n\x12position_threshold\x18\x0e \x01(\x05\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x1b\n\x13false_positive_rate\x18\x08 \x01(\x02\x12\x10\n\x08f1_score\x18\x04 \x01(\x02\x12\x12\n\nrecall_at1\x18\x05 \x01(\x02\x12\x15\n\rprecision_at1\x18\x06 \x01(\x02\x12\x1f\n\x17false_positive_rate_at1\x18\t \x01(\x02\x12\x14\n\x0cf1_score_at1\x18\x07 \x01(\x02\x12\x1b\n\x13true_positive_count\x18\n \x01(\x03\x12\x1c\n\x14false_positive_count\x18\x0b \x01(\x03\x12\x1c\n\x14false_negative_count\x18\x0c \x01(\x03\x12\x1b\n\x13true_negative_count\x18\r \x01(\x03\x1a\xbb\x01\n\x0fConfusionMatrix\x12\x1a\n\x12annotation_spec_id\x18\x01 \x03(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x03(\t\x12X\n\x03row\x18\x02 \x03(\x0b2K.google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix.Row\x1a\x1c\n\x03Row\x12\x15\n\rexample_count\x18\x01 \x03(\x05*Y\n\x12ClassificationType\x12#\n\x1fCLASSIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nMULTICLASS\x10\x01\x12\x0e\n\nMULTILABEL\x10\x02B\xb5\x01\n\x1acom.google.cloud.automl.v1B\x13ClassificationProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.classification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1B\x13ClassificationProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_CLASSIFICATIONTYPE']._serialized_start = 1014
    _globals['_CLASSIFICATIONTYPE']._serialized_end = 1103
    _globals['_CLASSIFICATIONANNOTATION']._serialized_start = 71
    _globals['_CLASSIFICATIONANNOTATION']._serialized_end = 112
    _globals['_CLASSIFICATIONEVALUATIONMETRICS']._serialized_start = 115
    _globals['_CLASSIFICATIONEVALUATIONMETRICS']._serialized_end = 1012
    _globals['_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY']._serialized_start = 442
    _globals['_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY']._serialized_end = 822
    _globals['_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX']._serialized_start = 825
    _globals['_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX']._serialized_end = 1012
    _globals['_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW']._serialized_start = 984
    _globals['_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW']._serialized_end = 1012