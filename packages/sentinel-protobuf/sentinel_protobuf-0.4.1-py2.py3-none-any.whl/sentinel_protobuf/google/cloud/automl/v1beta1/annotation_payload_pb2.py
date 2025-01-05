"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/annotation_payload.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_classification__pb2
from .....google.cloud.automl.v1beta1 import detection_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_detection__pb2
from .....google.cloud.automl.v1beta1 import tables_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2
from .....google.cloud.automl.v1beta1 import text_extraction_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__extraction__pb2
from .....google.cloud.automl.v1beta1 import text_sentiment_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__sentiment__pb2
from .....google.cloud.automl.v1beta1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/automl/v1beta1/annotation_payload.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a0google/cloud/automl/v1beta1/classification.proto\x1a+google/cloud/automl/v1beta1/detection.proto\x1a(google/cloud/automl/v1beta1/tables.proto\x1a1google/cloud/automl/v1beta1/text_extraction.proto\x1a0google/cloud/automl/v1beta1/text_sentiment.proto\x1a-google/cloud/automl/v1beta1/translation.proto"\xe6\x05\n\x11AnnotationPayload\x12I\n\x0btranslation\x18\x02 \x01(\x0b22.google.cloud.automl.v1beta1.TranslationAnnotationH\x00\x12O\n\x0eclassification\x18\x03 \x01(\x0b25.google.cloud.automl.v1beta1.ClassificationAnnotationH\x00\x12]\n\x16image_object_detection\x18\x04 \x01(\x0b2;.google.cloud.automl.v1beta1.ImageObjectDetectionAnnotationH\x00\x12Z\n\x14video_classification\x18\t \x01(\x0b2:.google.cloud.automl.v1beta1.VideoClassificationAnnotationH\x00\x12[\n\x15video_object_tracking\x18\x08 \x01(\x0b2:.google.cloud.automl.v1beta1.VideoObjectTrackingAnnotationH\x00\x12P\n\x0ftext_extraction\x18\x06 \x01(\x0b25.google.cloud.automl.v1beta1.TextExtractionAnnotationH\x00\x12N\n\x0etext_sentiment\x18\x07 \x01(\x0b24.google.cloud.automl.v1beta1.TextSentimentAnnotationH\x00\x12?\n\x06tables\x18\n \x01(\x0b2-.google.cloud.automl.v1beta1.TablesAnnotationH\x00\x12\x1a\n\x12annotation_spec_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x05 \x01(\tB\x08\n\x06detailB\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.annotation_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_ANNOTATIONPAYLOAD']._serialized_start = 371
    _globals['_ANNOTATIONPAYLOAD']._serialized_end = 1113