"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/text_extraction.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import text_segment_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__segment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/automl/v1beta1/text_extraction.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a.google/cloud/automl/v1beta1/text_segment.proto"y\n\x18TextExtractionAnnotation\x12@\n\x0ctext_segment\x18\x03 \x01(\x0b2(.google.cloud.automl.v1beta1.TextSegmentH\x00\x12\r\n\x05score\x18\x01 \x01(\x02B\x0c\n\nannotation"\x97\x02\n\x1fTextExtractionEvaluationMetrics\x12\x0e\n\x06au_prc\x18\x01 \x01(\x02\x12w\n\x1aconfidence_metrics_entries\x18\x02 \x03(\x0b2S.google.cloud.automl.v1beta1.TextExtractionEvaluationMetrics.ConfidenceMetricsEntry\x1ak\n\x16ConfidenceMetricsEntry\x12\x1c\n\x14confidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x03 \x01(\x02\x12\x11\n\tprecision\x18\x04 \x01(\x02\x12\x10\n\x08f1_score\x18\x05 \x01(\x02B\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.text_extraction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TEXTEXTRACTIONANNOTATION']._serialized_start = 130
    _globals['_TEXTEXTRACTIONANNOTATION']._serialized_end = 251
    _globals['_TEXTEXTRACTIONEVALUATIONMETRICS']._serialized_start = 254
    _globals['_TEXTEXTRACTIONEVALUATIONMETRICS']._serialized_end = 533
    _globals['_TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY']._serialized_start = 426
    _globals['_TEXTEXTRACTIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY']._serialized_end = 533