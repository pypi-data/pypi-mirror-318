"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/evaluation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/documentai/v1beta3/evaluation.proto\x12\x1fgoogle.cloud.documentai.v1beta3\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8d\x02\n\x13EvaluationReference\x12\x11\n\toperation\x18\x01 \x01(\t\x12=\n\nevaluation\x18\x02 \x01(\tB)\xfaA&\n$documentai.googleapis.com/Evaluation\x12N\n\x11aggregate_metrics\x18\x04 \x01(\x0b23.google.cloud.documentai.v1beta3.Evaluation.Metrics\x12T\n\x17aggregate_metrics_exact\x18\x05 \x01(\x0b23.google.cloud.documentai.v1beta3.Evaluation.Metrics"\x8d\x0e\n\nEvaluation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12O\n\x11document_counters\x18\x05 \x01(\x0b24.google.cloud.documentai.v1beta3.Evaluation.Counters\x12`\n\x14all_entities_metrics\x18\x03 \x01(\x0b2B.google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetrics\x12V\n\x0eentity_metrics\x18\x04 \x03(\x0b2>.google.cloud.documentai.v1beta3.Evaluation.EntityMetricsEntry\x12\x14\n\x0ckms_key_name\x18\x06 \x01(\t\x12\x1c\n\x14kms_key_version_name\x18\x07 \x01(\t\x1a\x8d\x01\n\x08Counters\x12\x1d\n\x15input_documents_count\x18\x01 \x01(\x05\x12\x1f\n\x17invalid_documents_count\x18\x02 \x01(\x05\x12\x1e\n\x16failed_documents_count\x18\x03 \x01(\x05\x12!\n\x19evaluated_documents_count\x18\x04 \x01(\x05\x1a\xcd\x02\n\x07Metrics\x12\x11\n\tprecision\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x10\n\x08f1_score\x18\x03 \x01(\x02\x12#\n\x1bpredicted_occurrences_count\x18\x04 \x01(\x05\x12&\n\x1eground_truth_occurrences_count\x18\x05 \x01(\x05\x12 \n\x18predicted_document_count\x18\n \x01(\x05\x12#\n\x1bground_truth_document_count\x18\x0b \x01(\x05\x12\x1c\n\x14true_positives_count\x18\x06 \x01(\x05\x12\x1d\n\x15false_positives_count\x18\x07 \x01(\x05\x12\x1d\n\x15false_negatives_count\x18\x08 \x01(\x05\x12\x1d\n\x15total_documents_count\x18\t \x01(\x05\x1ax\n\x16ConfidenceLevelMetrics\x12\x18\n\x10confidence_level\x18\x01 \x01(\x02\x12D\n\x07metrics\x18\x02 \x01(\x0b23.google.cloud.documentai.v1beta3.Evaluation.Metrics\x1a\x80\x04\n\x16MultiConfidenceMetrics\x12d\n\x18confidence_level_metrics\x18\x01 \x03(\x0b2B.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics\x12j\n\x1econfidence_level_metrics_exact\x18\x04 \x03(\x0b2B.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics\x12\r\n\x05auprc\x18\x02 \x01(\x02\x12#\n\x1bestimated_calibration_error\x18\x03 \x01(\x02\x12\x13\n\x0bauprc_exact\x18\x05 \x01(\x02\x12)\n!estimated_calibration_error_exact\x18\x06 \x01(\x02\x12d\n\x0cmetrics_type\x18\x07 \x01(\x0e2N.google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetrics.MetricsType":\n\x0bMetricsType\x12\x1c\n\x18METRICS_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tAGGREGATE\x10\x01\x1ax\n\x12EntityMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b2B.google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetrics:\x028\x01:\xa9\x01\xeaA\xa5\x01\n$documentai.googleapis.com/Evaluation\x12}projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}/evaluations/{evaluation}B\xeb\x01\n#com.google.cloud.documentai.v1beta3B\x14DocumentAiEvaluationP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\x14DocumentAiEvaluationP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3'
    _globals['_EVALUATIONREFERENCE'].fields_by_name['evaluation']._loaded_options = None
    _globals['_EVALUATIONREFERENCE'].fields_by_name['evaluation']._serialized_options = b'\xfaA&\n$documentai.googleapis.com/Evaluation'
    _globals['_EVALUATION_ENTITYMETRICSENTRY']._loaded_options = None
    _globals['_EVALUATION_ENTITYMETRICSENTRY']._serialized_options = b'8\x01'
    _globals['_EVALUATION']._loaded_options = None
    _globals['_EVALUATION']._serialized_options = b'\xeaA\xa5\x01\n$documentai.googleapis.com/Evaluation\x12}projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}/evaluations/{evaluation}'
    _globals['_EVALUATIONREFERENCE']._serialized_start = 146
    _globals['_EVALUATIONREFERENCE']._serialized_end = 415
    _globals['_EVALUATION']._serialized_start = 418
    _globals['_EVALUATION']._serialized_end = 2223
    _globals['_EVALUATION_COUNTERS']._serialized_start = 815
    _globals['_EVALUATION_COUNTERS']._serialized_end = 956
    _globals['_EVALUATION_METRICS']._serialized_start = 959
    _globals['_EVALUATION_METRICS']._serialized_end = 1292
    _globals['_EVALUATION_CONFIDENCELEVELMETRICS']._serialized_start = 1294
    _globals['_EVALUATION_CONFIDENCELEVELMETRICS']._serialized_end = 1414
    _globals['_EVALUATION_MULTICONFIDENCEMETRICS']._serialized_start = 1417
    _globals['_EVALUATION_MULTICONFIDENCEMETRICS']._serialized_end = 1929
    _globals['_EVALUATION_MULTICONFIDENCEMETRICS_METRICSTYPE']._serialized_start = 1871
    _globals['_EVALUATION_MULTICONFIDENCEMETRICS_METRICSTYPE']._serialized_end = 1929
    _globals['_EVALUATION_ENTITYMETRICSENTRY']._serialized_start = 1931
    _globals['_EVALUATION_ENTITYMETRICSENTRY']._serialized_end = 2051