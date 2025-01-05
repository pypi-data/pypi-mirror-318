"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/evaluation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datalabeling.v1beta1 import annotation_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_annotation__pb2
from .....google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_annotation__spec__set__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/datalabeling/v1beta1/evaluation.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x19google/api/resource.proto\x1a2google/cloud/datalabeling/v1beta1/annotation.proto\x1a;google/cloud/datalabeling/v1beta1/annotation_spec_set.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf6\x03\n\nEvaluation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12C\n\x06config\x18\x02 \x01(\x0b23.google.cloud.datalabeling.v1beta1.EvaluationConfig\x12;\n\x17evaluation_job_run_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12P\n\x12evaluation_metrics\x18\x05 \x01(\x0b24.google.cloud.datalabeling.v1beta1.EvaluationMetrics\x12J\n\x0fannotation_type\x18\x06 \x01(\x0e21.google.cloud.datalabeling.v1beta1.AnnotationType\x12\x1c\n\x14evaluated_item_count\x18\x07 \x01(\x03:k\xeaAh\n&datalabeling.googleapis.com/Evaluation\x12>projects/{project}/datasets/{dataset}/evaluations/{evaluation}"\x91\x01\n\x10EvaluationConfig\x12j\n\x1fbounding_box_evaluation_options\x18\x01 \x01(\x0b2?.google.cloud.datalabeling.v1beta1.BoundingBoxEvaluationOptionsH\x00B\x11\n\x0fvertical_option"5\n\x1cBoundingBoxEvaluationOptions\x12\x15\n\riou_threshold\x18\x01 \x01(\x02"\xd9\x01\n\x11EvaluationMetrics\x12Z\n\x16classification_metrics\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.ClassificationMetricsH\x00\x12]\n\x18object_detection_metrics\x18\x02 \x01(\x0b29.google.cloud.datalabeling.v1beta1.ObjectDetectionMetricsH\x00B\t\n\x07metrics"\xa3\x01\n\x15ClassificationMetrics\x12<\n\x08pr_curve\x18\x01 \x01(\x0b2*.google.cloud.datalabeling.v1beta1.PrCurve\x12L\n\x10confusion_matrix\x18\x02 \x01(\x0b22.google.cloud.datalabeling.v1beta1.ConfusionMatrix"V\n\x16ObjectDetectionMetrics\x12<\n\x08pr_curve\x18\x01 \x01(\x0b2*.google.cloud.datalabeling.v1beta1.PrCurve"\xe6\x03\n\x07PrCurve\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12\x18\n\x10area_under_curve\x18\x02 \x01(\x02\x12e\n\x1aconfidence_metrics_entries\x18\x03 \x03(\x0b2A.google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry\x12\x1e\n\x16mean_average_precision\x18\x04 \x01(\x02\x1a\xed\x01\n\x16ConfidenceMetricsEntry\x12\x1c\n\x14confidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08f1_score\x18\x04 \x01(\x02\x12\x12\n\nrecall_at1\x18\x05 \x01(\x02\x12\x15\n\rprecision_at1\x18\x06 \x01(\x02\x12\x14\n\x0cf1_score_at1\x18\x07 \x01(\x02\x12\x12\n\nrecall_at5\x18\x08 \x01(\x02\x12\x15\n\rprecision_at5\x18\t \x01(\x02\x12\x14\n\x0cf1_score_at5\x18\n \x01(\x02"\xfc\x02\n\x0fConfusionMatrix\x12C\n\x03row\x18\x01 \x03(\x0b26.google.cloud.datalabeling.v1beta1.ConfusionMatrix.Row\x1av\n\x14ConfusionMatrixEntry\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12\x12\n\nitem_count\x18\x02 \x01(\x05\x1a\xab\x01\n\x03Row\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12X\n\x07entries\x18\x02 \x03(\x0b2G.google.cloud.datalabeling.v1beta1.ConfusionMatrix.ConfusionMatrixEntryB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_EVALUATION']._loaded_options = None
    _globals['_EVALUATION']._serialized_options = b'\xeaAh\n&datalabeling.googleapis.com/Evaluation\x12>projects/{project}/datasets/{dataset}/evaluations/{evaluation}'
    _globals['_EVALUATION']._serialized_start = 263
    _globals['_EVALUATION']._serialized_end = 765
    _globals['_EVALUATIONCONFIG']._serialized_start = 768
    _globals['_EVALUATIONCONFIG']._serialized_end = 913
    _globals['_BOUNDINGBOXEVALUATIONOPTIONS']._serialized_start = 915
    _globals['_BOUNDINGBOXEVALUATIONOPTIONS']._serialized_end = 968
    _globals['_EVALUATIONMETRICS']._serialized_start = 971
    _globals['_EVALUATIONMETRICS']._serialized_end = 1188
    _globals['_CLASSIFICATIONMETRICS']._serialized_start = 1191
    _globals['_CLASSIFICATIONMETRICS']._serialized_end = 1354
    _globals['_OBJECTDETECTIONMETRICS']._serialized_start = 1356
    _globals['_OBJECTDETECTIONMETRICS']._serialized_end = 1442
    _globals['_PRCURVE']._serialized_start = 1445
    _globals['_PRCURVE']._serialized_end = 1931
    _globals['_PRCURVE_CONFIDENCEMETRICSENTRY']._serialized_start = 1694
    _globals['_PRCURVE_CONFIDENCEMETRICSENTRY']._serialized_end = 1931
    _globals['_CONFUSIONMATRIX']._serialized_start = 1934
    _globals['_CONFUSIONMATRIX']._serialized_end = 2314
    _globals['_CONFUSIONMATRIX_CONFUSIONMATRIXENTRY']._serialized_start = 2022
    _globals['_CONFUSIONMATRIX_CONFUSIONMATRIXENTRY']._serialized_end = 2140
    _globals['_CONFUSIONMATRIX_ROW']._serialized_start = 2143
    _globals['_CONFUSIONMATRIX_ROW']._serialized_end = 2314