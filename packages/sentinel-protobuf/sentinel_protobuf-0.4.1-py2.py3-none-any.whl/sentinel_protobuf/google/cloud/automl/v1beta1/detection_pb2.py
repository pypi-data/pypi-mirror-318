"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/detection.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import geometry_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_geometry__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/automl/v1beta1/detection.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a*google/cloud/automl/v1beta1/geometry.proto\x1a\x1egoogle/protobuf/duration.proto"p\n\x1eImageObjectDetectionAnnotation\x12?\n\x0cbounding_box\x18\x01 \x01(\x0b2).google.cloud.automl.v1beta1.BoundingPoly\x12\r\n\x05score\x18\x02 \x01(\x02"\xb4\x01\n\x1dVideoObjectTrackingAnnotation\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12?\n\x0cbounding_box\x18\x03 \x01(\x0b2).google.cloud.automl.v1beta1.BoundingPoly\x12\r\n\x05score\x18\x04 \x01(\x02"\xae\x02\n\x17BoundingBoxMetricsEntry\x12\x15\n\riou_threshold\x18\x01 \x01(\x02\x12\x1e\n\x16mean_average_precision\x18\x02 \x01(\x02\x12o\n\x1aconfidence_metrics_entries\x18\x03 \x03(\x0b2K.google.cloud.automl.v1beta1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry\x1ak\n\x16ConfidenceMetricsEntry\x12\x1c\n\x14confidence_threshold\x18\x01 \x01(\x02\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x10\n\x08f1_score\x18\x04 \x01(\x02"\xd6\x01\n%ImageObjectDetectionEvaluationMetrics\x12$\n\x1cevaluated_bounding_box_count\x18\x01 \x01(\x05\x12Z\n\x1cbounding_box_metrics_entries\x18\x02 \x03(\x0b24.google.cloud.automl.v1beta1.BoundingBoxMetricsEntry\x12+\n#bounding_box_mean_average_precision\x18\x03 \x01(\x02"\xf4\x01\n$VideoObjectTrackingEvaluationMetrics\x12\x1d\n\x15evaluated_frame_count\x18\x01 \x01(\x05\x12$\n\x1cevaluated_bounding_box_count\x18\x02 \x01(\x05\x12Z\n\x1cbounding_box_metrics_entries\x18\x04 \x03(\x0b24.google.cloud.automl.v1beta1.BoundingBoxMetricsEntry\x12+\n#bounding_box_mean_average_precision\x18\x06 \x01(\x02B\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_IMAGEOBJECTDETECTIONANNOTATION']._serialized_start = 152
    _globals['_IMAGEOBJECTDETECTIONANNOTATION']._serialized_end = 264
    _globals['_VIDEOOBJECTTRACKINGANNOTATION']._serialized_start = 267
    _globals['_VIDEOOBJECTTRACKINGANNOTATION']._serialized_end = 447
    _globals['_BOUNDINGBOXMETRICSENTRY']._serialized_start = 450
    _globals['_BOUNDINGBOXMETRICSENTRY']._serialized_end = 752
    _globals['_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY']._serialized_start = 645
    _globals['_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY']._serialized_end = 752
    _globals['_IMAGEOBJECTDETECTIONEVALUATIONMETRICS']._serialized_start = 755
    _globals['_IMAGEOBJECTDETECTIONEVALUATIONMETRICS']._serialized_end = 969
    _globals['_VIDEOOBJECTTRACKINGEVALUATIONMETRICS']._serialized_start = 972
    _globals['_VIDEOOBJECTTRACKINGEVALUATIONMETRICS']._serialized_end = 1216