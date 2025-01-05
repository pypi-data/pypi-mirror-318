"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/image.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.automl.v1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_classification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/automl/v1/image.proto\x12\x16google.cloud.automl.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/cloud/automl/v1/classification.proto"r\n"ImageClassificationDatasetMetadata\x12L\n\x13classification_type\x18\x01 \x01(\x0e2*.google.cloud.automl.v1.ClassificationTypeB\x03\xe0A\x02"%\n#ImageObjectDetectionDatasetMetadata"\xf7\x01\n ImageClassificationModelMetadata\x12\x1a\n\rbase_model_id\x18\x01 \x01(\tB\x03\xe0A\x01\x12*\n\x1dtrain_budget_milli_node_hours\x18\x10 \x01(\x03B\x03\xe0A\x01\x12(\n\x1btrain_cost_milli_node_hours\x18\x11 \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bstop_reason\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x17\n\nmodel_type\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08node_qps\x18\r \x01(\x01B\x03\xe0A\x03\x12\x17\n\nnode_count\x18\x0e \x01(\x03B\x03\xe0A\x03"\xdc\x01\n!ImageObjectDetectionModelMetadata\x12\x17\n\nmodel_type\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x17\n\nnode_count\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x15\n\x08node_qps\x18\x04 \x01(\x01B\x03\xe0A\x03\x12\x18\n\x0bstop_reason\x18\x05 \x01(\tB\x03\xe0A\x03\x12*\n\x1dtrain_budget_milli_node_hours\x18\x06 \x01(\x03B\x03\xe0A\x01\x12(\n\x1btrain_cost_milli_node_hours\x18\x07 \x01(\x03B\x03\xe0A\x03"E\n*ImageClassificationModelDeploymentMetadata\x12\x17\n\nnode_count\x18\x01 \x01(\x03B\x03\xe0A\x04"F\n+ImageObjectDetectionModelDeploymentMetadata\x12\x17\n\nnode_count\x18\x01 \x01(\x03B\x03\xe0A\x04B\xac\x01\n\x1acom.google.cloud.automl.v1B\nImageProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1B\nImageProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_IMAGECLASSIFICATIONDATASETMETADATA'].fields_by_name['classification_type']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONDATASETMETADATA'].fields_by_name['classification_type']._serialized_options = b'\xe0A\x02'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['base_model_id']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['base_model_id']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['train_budget_milli_node_hours']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['train_budget_milli_node_hours']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['train_cost_milli_node_hours']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['train_cost_milli_node_hours']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['stop_reason']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['stop_reason']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['model_type']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['model_type']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['node_qps']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['node_qps']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['node_count']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELMETADATA'].fields_by_name['node_count']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['model_type']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['model_type']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['node_count']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['node_count']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['node_qps']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['node_qps']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['stop_reason']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['stop_reason']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['train_budget_milli_node_hours']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['train_budget_milli_node_hours']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['train_cost_milli_node_hours']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA'].fields_by_name['train_cost_milli_node_hours']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA'].fields_by_name['node_count']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA'].fields_by_name['node_count']._serialized_options = b'\xe0A\x04'
    _globals['_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA'].fields_by_name['node_count']._loaded_options = None
    _globals['_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA'].fields_by_name['node_count']._serialized_options = b'\xe0A\x04'
    _globals['_IMAGECLASSIFICATIONDATASETMETADATA']._serialized_start = 140
    _globals['_IMAGECLASSIFICATIONDATASETMETADATA']._serialized_end = 254
    _globals['_IMAGEOBJECTDETECTIONDATASETMETADATA']._serialized_start = 256
    _globals['_IMAGEOBJECTDETECTIONDATASETMETADATA']._serialized_end = 293
    _globals['_IMAGECLASSIFICATIONMODELMETADATA']._serialized_start = 296
    _globals['_IMAGECLASSIFICATIONMODELMETADATA']._serialized_end = 543
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA']._serialized_start = 546
    _globals['_IMAGEOBJECTDETECTIONMODELMETADATA']._serialized_end = 766
    _globals['_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA']._serialized_start = 768
    _globals['_IMAGECLASSIFICATIONMODELDEPLOYMENTMETADATA']._serialized_end = 837
    _globals['_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA']._serialized_start = 839
    _globals['_IMAGEOBJECTDETECTIONMODELDEPLOYMENTMETADATA']._serialized_end = 909