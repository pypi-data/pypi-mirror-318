"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/text.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_classification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/automl/v1beta1/text.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a0google/cloud/automl/v1beta1/classification.proto"q\n!TextClassificationDatasetMetadata\x12L\n\x13classification_type\x18\x01 \x01(\x0e2/.google.cloud.automl.v1beta1.ClassificationType"o\n\x1fTextClassificationModelMetadata\x12L\n\x13classification_type\x18\x03 \x01(\x0e2/.google.cloud.automl.v1beta1.ClassificationType"\x1f\n\x1dTextExtractionDatasetMetadata"1\n\x1bTextExtractionModelMetadata\x12\x12\n\nmodel_hint\x18\x03 \x01(\t"5\n\x1cTextSentimentDatasetMetadata\x12\x15\n\rsentiment_max\x18\x01 \x01(\x05"\x1c\n\x1aTextSentimentModelMetadataB\xa6\x01\n\x1fcom.google.cloud.automl.v1beta1B\tTextProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.text_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\tTextProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TEXTCLASSIFICATIONDATASETMETADATA']._serialized_start = 121
    _globals['_TEXTCLASSIFICATIONDATASETMETADATA']._serialized_end = 234
    _globals['_TEXTCLASSIFICATIONMODELMETADATA']._serialized_start = 236
    _globals['_TEXTCLASSIFICATIONMODELMETADATA']._serialized_end = 347
    _globals['_TEXTEXTRACTIONDATASETMETADATA']._serialized_start = 349
    _globals['_TEXTEXTRACTIONDATASETMETADATA']._serialized_end = 380
    _globals['_TEXTEXTRACTIONMODELMETADATA']._serialized_start = 382
    _globals['_TEXTEXTRACTIONMODELMETADATA']._serialized_end = 431
    _globals['_TEXTSENTIMENTDATASETMETADATA']._serialized_start = 433
    _globals['_TEXTSENTIMENTDATASETMETADATA']._serialized_end = 486
    _globals['_TEXTSENTIMENTMODELMETADATA']._serialized_start = 488
    _globals['_TEXTSENTIMENTMODELMETADATA']._serialized_end = 516