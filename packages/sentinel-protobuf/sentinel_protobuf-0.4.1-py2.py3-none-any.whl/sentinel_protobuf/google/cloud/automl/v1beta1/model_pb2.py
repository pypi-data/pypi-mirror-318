"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1beta1 import image_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2
from .....google.cloud.automl.v1beta1 import tables_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2
from .....google.cloud.automl.v1beta1 import text_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__pb2
from .....google.cloud.automl.v1beta1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2
from .....google.cloud.automl.v1beta1 import video_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_video__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/automl/v1beta1/model.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a\'google/cloud/automl/v1beta1/image.proto\x1a(google/cloud/automl/v1beta1/tables.proto\x1a&google/cloud/automl/v1beta1/text.proto\x1a-google/cloud/automl/v1beta1/translation.proto\x1a\'google/cloud/automl/v1beta1/video.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcc\n\n\x05Model\x12[\n\x1atranslation_model_metadata\x18\x0f \x01(\x0b25.google.cloud.automl.v1beta1.TranslationModelMetadataH\x00\x12l\n#image_classification_model_metadata\x18\r \x01(\x0b2=.google.cloud.automl.v1beta1.ImageClassificationModelMetadataH\x00\x12j\n"text_classification_model_metadata\x18\x0e \x01(\x0b2<.google.cloud.automl.v1beta1.TextClassificationModelMetadataH\x00\x12o\n%image_object_detection_model_metadata\x18\x14 \x01(\x0b2>.google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadataH\x00\x12l\n#video_classification_model_metadata\x18\x17 \x01(\x0b2=.google.cloud.automl.v1beta1.VideoClassificationModelMetadataH\x00\x12m\n$video_object_tracking_model_metadata\x18\x15 \x01(\x0b2=.google.cloud.automl.v1beta1.VideoObjectTrackingModelMetadataH\x00\x12b\n\x1etext_extraction_model_metadata\x18\x13 \x01(\x0b28.google.cloud.automl.v1beta1.TextExtractionModelMetadataH\x00\x12Q\n\x15tables_model_metadata\x18\x18 \x01(\x0b20.google.cloud.automl.v1beta1.TablesModelMetadataH\x00\x12`\n\x1dtext_sentiment_model_metadata\x18\x16 \x01(\x0b27.google.cloud.automl.v1beta1.TextSentimentModelMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12L\n\x10deployment_state\x18\x08 \x01(\x0e22.google.cloud.automl.v1beta1.Model.DeploymentState"Q\n\x0fDeploymentState\x12 \n\x1cDEPLOYMENT_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DEPLOYED\x10\x01\x12\x0e\n\nUNDEPLOYED\x10\x02:X\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}B\x10\n\x0emodel_metadataB\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b'\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}'
    _globals['_MODEL']._serialized_start = 344
    _globals['_MODEL']._serialized_end = 1700
    _globals['_MODEL_DEPLOYMENTSTATE']._serialized_start = 1511
    _globals['_MODEL_DEPLOYMENTSTATE']._serialized_end = 1592