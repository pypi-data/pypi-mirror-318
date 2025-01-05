"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_image_segmentation.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n]google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_image_segmentation.proto\x12=google.cloud.aiplatform.v1beta1.schema.trainingjob.definition"\xf9\x01\n\x17AutoMlImageSegmentation\x12l\n\x06inputs\x18\x01 \x01(\x0b2\\.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageSegmentationInputs\x12p\n\x08metadata\x18\x02 \x01(\x0b2^.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageSegmentationMetadata"\xce\x02\n\x1dAutoMlImageSegmentationInputs\x12z\n\nmodel_type\x18\x01 \x01(\x0e2f.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageSegmentationInputs.ModelType\x12\x1f\n\x17budget_milli_node_hours\x18\x02 \x01(\x03\x12\x15\n\rbase_model_id\x18\x03 \x01(\t"y\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15CLOUD_HIGH_ACCURACY_1\x10\x01\x12\x18\n\x14CLOUD_LOW_ACCURACY_1\x10\x02\x12\x1b\n\x17MOBILE_TF_LOW_LATENCY_1\x10\x03"\xbf\x02\n\x1fAutoMlImageSegmentationMetadata\x12\x1d\n\x15cost_milli_node_hours\x18\x01 \x01(\x03\x12\x93\x01\n\x16successful_stop_reason\x18\x02 \x01(\x0e2s.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageSegmentationMetadata.SuccessfulStopReason"g\n\x14SuccessfulStopReason\x12&\n"SUCCESSFUL_STOP_REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0eBUDGET_REACHED\x10\x01\x12\x13\n\x0fMODEL_CONVERGED\x10\x02B\x8c\x03\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1cAutoMLImageSegmentationProtoP\x01Zacloud.google.com/go/aiplatform/apiv1beta1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x02=Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition\xca\x02=Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\TrainingJob\\Definition\xea\x02CGoogle::Cloud::AIPlatform::V1beta1::Schema::TrainingJob::Definitionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automl_image_segmentation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1cAutoMLImageSegmentationProtoP\x01Zacloud.google.com/go/aiplatform/apiv1beta1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x02=Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition\xca\x02=Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\TrainingJob\\Definition\xea\x02CGoogle::Cloud::AIPlatform::V1beta1::Schema::TrainingJob::Definition'
    _globals['_AUTOMLIMAGESEGMENTATION']._serialized_start = 161
    _globals['_AUTOMLIMAGESEGMENTATION']._serialized_end = 410
    _globals['_AUTOMLIMAGESEGMENTATIONINPUTS']._serialized_start = 413
    _globals['_AUTOMLIMAGESEGMENTATIONINPUTS']._serialized_end = 747
    _globals['_AUTOMLIMAGESEGMENTATIONINPUTS_MODELTYPE']._serialized_start = 626
    _globals['_AUTOMLIMAGESEGMENTATIONINPUTS_MODELTYPE']._serialized_end = 747
    _globals['_AUTOMLIMAGESEGMENTATIONMETADATA']._serialized_start = 750
    _globals['_AUTOMLIMAGESEGMENTATIONMETADATA']._serialized_end = 1069
    _globals['_AUTOMLIMAGESEGMENTATIONMETADATA_SUCCESSFULSTOPREASON']._serialized_start = 966
    _globals['_AUTOMLIMAGESEGMENTATIONMETADATA_SUCCESSFULSTOPREASON']._serialized_end = 1069