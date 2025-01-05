"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/annotation_payload.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_classification__pb2
from .....google.cloud.automl.v1 import detection_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_detection__pb2
from .....google.cloud.automl.v1 import text_extraction_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_text__extraction__pb2
from .....google.cloud.automl.v1 import text_sentiment_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_text__sentiment__pb2
from .....google.cloud.automl.v1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_translation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/automl/v1/annotation_payload.proto\x12\x16google.cloud.automl.v1\x1a+google/cloud/automl/v1/classification.proto\x1a&google/cloud/automl/v1/detection.proto\x1a,google/cloud/automl/v1/text_extraction.proto\x1a+google/cloud/automl/v1/text_sentiment.proto\x1a(google/cloud/automl/v1/translation.proto"\xd3\x03\n\x11AnnotationPayload\x12D\n\x0btranslation\x18\x02 \x01(\x0b2-.google.cloud.automl.v1.TranslationAnnotationH\x00\x12J\n\x0eclassification\x18\x03 \x01(\x0b20.google.cloud.automl.v1.ClassificationAnnotationH\x00\x12X\n\x16image_object_detection\x18\x04 \x01(\x0b26.google.cloud.automl.v1.ImageObjectDetectionAnnotationH\x00\x12K\n\x0ftext_extraction\x18\x06 \x01(\x0b20.google.cloud.automl.v1.TextExtractionAnnotationH\x00\x12I\n\x0etext_sentiment\x18\x07 \x01(\x0b2/.google.cloud.automl.v1.TextSentimentAnnotationH\x00\x12\x1a\n\x12annotation_spec_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x05 \x01(\tB\x08\n\x06detailB\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.annotation_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_ANNOTATIONPAYLOAD']._serialized_start = 294
    _globals['_ANNOTATIONPAYLOAD']._serialized_end = 761