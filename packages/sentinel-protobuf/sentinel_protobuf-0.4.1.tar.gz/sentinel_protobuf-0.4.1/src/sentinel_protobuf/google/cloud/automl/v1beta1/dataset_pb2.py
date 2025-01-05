"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1beta1 import image_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2
from .....google.cloud.automl.v1beta1 import tables_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2
from .....google.cloud.automl.v1beta1 import text_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2
from .....google.cloud.automl.v1beta1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2
from .....google.cloud.automl.v1beta1 import video_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_video__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/automl/v1beta1/dataset.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a\'google/cloud/automl/v1beta1/image.proto\x1a(google/cloud/automl/v1beta1/tables.proto\x1a&google/cloud/automl/v1beta1/text.proto\x1a-google/cloud/automl/v1beta1/translation.proto\x1a\'google/cloud/automl/v1beta1/video.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\t\n\x07Dataset\x12_\n\x1ctranslation_dataset_metadata\x18\x17 \x01(\x0b27.google.cloud.automl.v1beta1.TranslationDatasetMetadataH\x00\x12p\n%image_classification_dataset_metadata\x18\x18 \x01(\x0b2?.google.cloud.automl.v1beta1.ImageClassificationDatasetMetadataH\x00\x12n\n$text_classification_dataset_metadata\x18\x19 \x01(\x0b2>.google.cloud.automl.v1beta1.TextClassificationDatasetMetadataH\x00\x12s\n\'image_object_detection_dataset_metadata\x18\x1a \x01(\x0b2@.google.cloud.automl.v1beta1.ImageObjectDetectionDatasetMetadataH\x00\x12p\n%video_classification_dataset_metadata\x18\x1f \x01(\x0b2?.google.cloud.automl.v1beta1.VideoClassificationDatasetMetadataH\x00\x12q\n&video_object_tracking_dataset_metadata\x18\x1d \x01(\x0b2?.google.cloud.automl.v1beta1.VideoObjectTrackingDatasetMetadataH\x00\x12f\n text_extraction_dataset_metadata\x18\x1c \x01(\x0b2:.google.cloud.automl.v1beta1.TextExtractionDatasetMetadataH\x00\x12d\n\x1ftext_sentiment_dataset_metadata\x18\x1e \x01(\x0b29.google.cloud.automl.v1beta1.TextSentimentDatasetMetadataH\x00\x12U\n\x17tables_dataset_metadata\x18! \x01(\x0b22.google.cloud.automl.v1beta1.TablesDatasetMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x15\n\rexample_count\x18\x15 \x01(\x05\x12/\n\x0bcreate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04etag\x18\x11 \x01(\t:^\xeaA[\n\x1dautoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}B\x12\n\x10dataset_metadataB\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaA[\n\x1dautoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}'
    _globals['_DATASET']._serialized_start = 346
    _globals['_DATASET']._serialized_end = 1576