"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/text.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_classification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/cloud/automl/v1/text.proto\x12\x16google.cloud.automl.v1\x1a+google/cloud/automl/v1/classification.proto"l\n!TextClassificationDatasetMetadata\x12G\n\x13classification_type\x18\x01 \x01(\x0e2*.google.cloud.automl.v1.ClassificationType"j\n\x1fTextClassificationModelMetadata\x12G\n\x13classification_type\x18\x03 \x01(\x0e2*.google.cloud.automl.v1.ClassificationType"\x1f\n\x1dTextExtractionDatasetMetadata"\x1d\n\x1bTextExtractionModelMetadata"5\n\x1cTextSentimentDatasetMetadata\x12\x15\n\rsentiment_max\x18\x01 \x01(\x05"\x1c\n\x1aTextSentimentModelMetadataB\xab\x01\n\x1acom.google.cloud.automl.v1B\tTextProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.text_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1B\tTextProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_TEXTCLASSIFICATIONDATASETMETADATA']._serialized_start = 106
    _globals['_TEXTCLASSIFICATIONDATASETMETADATA']._serialized_end = 214
    _globals['_TEXTCLASSIFICATIONMODELMETADATA']._serialized_start = 216
    _globals['_TEXTCLASSIFICATIONMODELMETADATA']._serialized_end = 322
    _globals['_TEXTEXTRACTIONDATASETMETADATA']._serialized_start = 324
    _globals['_TEXTEXTRACTIONDATASETMETADATA']._serialized_end = 355
    _globals['_TEXTEXTRACTIONMODELMETADATA']._serialized_start = 357
    _globals['_TEXTEXTRACTIONMODELMETADATA']._serialized_end = 386
    _globals['_TEXTSENTIMENTDATASETMETADATA']._serialized_start = 388
    _globals['_TEXTSENTIMENTDATASETMETADATA']._serialized_end = 441
    _globals['_TEXTSENTIMENTMODELMETADATA']._serialized_start = 443
    _globals['_TEXTSENTIMENTMODELMETADATA']._serialized_end = 471