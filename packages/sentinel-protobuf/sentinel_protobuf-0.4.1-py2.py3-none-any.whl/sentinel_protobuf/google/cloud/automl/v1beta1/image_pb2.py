"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/image.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import annotation_spec_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__spec__pb2
from .....google.cloud.automl.v1beta1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_classification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/automl/v1beta1/image.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a1google/cloud/automl/v1beta1/annotation_spec.proto\x1a0google/cloud/automl/v1beta1/classification.proto"r\n"ImageClassificationDatasetMetadata\x12L\n\x13classification_type\x18\x01 \x01(\x0e2/.google.cloud.automl.v1beta1.ClassificationType"%\n#ImageObjectDetectionDatasetMetadata"\xb2\x01\n ImageClassificationModelMetadata\x12\x15\n\rbase_model_id\x18\x01 \x01(\t\x12\x14\n\x0ctrain_budget\x18\x02 \x01(\x03\x12\x12\n\ntrain_cost\x18\x03 \x01(\x03\x12\x13\n\x0bstop_reason\x18\x05 \x01(\t\x12\x12\n\nmodel_type\x18\x07 \x01(\t\x12\x10\n\x08node_qps\x18\r \x01(\x01\x12\x12\n\nnode_count\x18\x0e \x01(\x03"\xbe\x01\n!ImageObjectDetectionModelMetadata\x12\x12\n\nmodel_type\x18\x01 \x01(\t\x12\x12\n\nnode_count\x18\x03 \x01(\x03\x12\x10\n\x08node_qps\x18\x04 \x01(\x01\x12\x13\n\x0bstop_reason\x18\x05 \x01(\t\x12%\n\x1dtrain_budget_milli_node_hours\x18\x06 \x01(\x03\x12#\n\x1btrain_cost_milli_node_hours\x18\x07 \x01(\x03"@\n*ImageClassificationModelDeploymentMetadata\x12\x12\n\nnode_count\x18\x01 \x01(\x03"A\n+ImageObjectDetectionModelDeploymentMetadata\x12\x12\n\nnode_count\x18\x01 \x01(\x03B\xa7\x01\n\x1fcom.google.cloud.automl.v1beta1B\nImageProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\nImageProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_IMAGECLASSIFICATIONDATASETMETADATA']._serialized_start = 173
    _globals['_IMAGECLASSIFICATIONDATASETMETADATA']._serialized_end = 287
    _globals['_IMAGEOBJECTDETECTIONDATASETMETADATA']._serialized_start = 289
    _globals['_IMAGEOBJECTDETECTIONDATASETMETADATA']._serialized_end = 326
    _globals['_IMAGECLASSIFICATIONMODELMETADATA']._serialized_start = 329
    _globals['_IMAGECLASSIFICATIONMODELMETADATA']._serialized_end = 507
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA']._serialized_start = 510
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA']._serialized_end = 700
    _globals['_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA']._serialized_start = 702
    _globals['_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA']._serialized_end = 766
    _globals['_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA']._serialized_start = 768
    _globals['_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA']._serialized_end = 833