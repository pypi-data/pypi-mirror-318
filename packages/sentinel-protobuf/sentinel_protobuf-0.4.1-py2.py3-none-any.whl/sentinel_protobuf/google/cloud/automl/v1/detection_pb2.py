"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/detection.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1 import geometry_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/automl/v1/detection.proto\x12\x16google.cloud.automl.v1\x1a%google/cloud/automl/v1/geometry.proto"k\n\x1eImageObjectDetectionAnnotation\x12:\n\x0cbounding_box\x18\x01 \x01(\x0b2$.google.cloud.automl.v1.BoundingPoly\x12\r\n\x05score\x18\x02 \x01(\x02"\xa9\x02\n\x17BoundingBoxMetricsEntry\x12\x15\n\riou_threshold\x18\x01 \x01(\x02\x12\x1e\n\x16mean_average_precision\x18\x02 \x01(\x02\x12j\n\x1aconfidence_metrics_entries\x18\x03 \x03(\x0b2F.google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry\x1ak\n\x16ConfidenceMetricsEntry\x12\x1c\n\x14confidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08f1_score\x18\x04 \x01(\x02"\xd1\x01\n%ImageObjectDetectionEvaluationMetrics\x12$\n\x1cevaluated_bounding_box_count\x18\x01 \x01(\x05\x12U\n\x1cbounding_box_metrics_entries\x18\x02 \x03(\x0b2/.google.cloud.automl.v1.BoundingBoxMetricsEntry\x12+\n#bounding_box_mean_average_precision\x18\x03 \x01(\x02B\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_IMAGEOBJECTDETECTIONANNOTATION']._serialized_start = 105
    _globals['_IMAGEOBJECTDETECTIONANNOTATION']._serialized_end = 212
    _globals['_BOUNDINGBOXMETRICSENTRY']._serialized_start = 215
    _globals['_BOUNDINGBOXMETRICSENTRY']._serialized_end = 512
    _globals['_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY']._serialized_start = 405
    _globals['_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY']._serialized_end = 512
    _globals['_IMAGEOBJECTDETECTIONEVALUATIONMETRICS']._serialized_start = 515
    _globals['_IMAGEOBJECTDETECTIONEVALUATIONMETRICS']._serialized_end = 724