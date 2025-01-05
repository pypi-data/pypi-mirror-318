"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1 import image_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_image__pb2
from .....google.cloud.automl.v1 import text_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_text__pb2
from .....google.cloud.automl.v1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_translation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/automl/v1/dataset.proto\x12\x16google.cloud.automl.v1\x1a\x19google/api/resource.proto\x1a"google/cloud/automl/v1/image.proto\x1a!google/cloud/automl/v1/text.proto\x1a(google/cloud/automl/v1/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe0\x07\n\x07Dataset\x12Z\n\x1ctranslation_dataset_metadata\x18\x17 \x01(\x0b22.google.cloud.automl.v1.TranslationDatasetMetadataH\x00\x12k\n%image_classification_dataset_metadata\x18\x18 \x01(\x0b2:.google.cloud.automl.v1.ImageClassificationDatasetMetadataH\x00\x12i\n$text_classification_dataset_metadata\x18\x19 \x01(\x0b29.google.cloud.automl.v1.TextClassificationDatasetMetadataH\x00\x12n\n\'image_object_detection_dataset_metadata\x18\x1a \x01(\x0b2;.google.cloud.automl.v1.ImageObjectDetectionDatasetMetadataH\x00\x12a\n text_extraction_dataset_metadata\x18\x1c \x01(\x0b25.google.cloud.automl.v1.TextExtractionDatasetMetadataH\x00\x12_\n\x1ftext_sentiment_dataset_metadata\x18\x1e \x01(\x0b24.google.cloud.automl.v1.TextSentimentDatasetMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x15\n\rexample_count\x18\x15 \x01(\x05\x12/\n\x0bcreate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04etag\x18\x11 \x01(\t\x12;\n\x06labels\x18\' \x03(\x0b2+.google.cloud.automl.v1.Dataset.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:^\xeaA[\n\x1dautoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}B\x12\n\x10dataset_metadataB\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_DATASET_LABELSENTRY']._loaded_options = None
    _globals['_DATASET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaA[\n\x1dautoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}'
    _globals['_DATASET']._serialized_start = 238
    _globals['_DATASET']._serialized_end = 1230
    _globals['_DATASET_LABELSENTRY']._serialized_start = 1069
    _globals['_DATASET_LABELSENTRY']._serialized_end = 1114