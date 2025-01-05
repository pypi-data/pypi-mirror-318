"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_image_object_detection.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nagoogle/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_image_object_detection.proto\x12=google.cloud.aiplatform.v1beta1.schema.trainingjob.definition"\x82\x02\n\x1aAutoMlImageObjectDetection\x12o\n\x06inputs\x18\x01 \x01(\x0b2_.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs\x12s\n\x08metadata\x18\x02 \x01(\x0b2a.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageObjectDetectionMetadata"\x97\x03\n AutoMlImageObjectDetectionInputs\x12}\n\nmodel_type\x18\x01 \x01(\x0e2i.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs.ModelType\x12\x1f\n\x17budget_milli_node_hours\x18\x02 \x01(\x03\x12\x1e\n\x16disable_early_stopping\x18\x03 \x01(\x08"\xb2\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15CLOUD_HIGH_ACCURACY_1\x10\x01\x12\x17\n\x13CLOUD_LOW_LATENCY_1\x10\x02\x12\x1b\n\x17MOBILE_TF_LOW_LATENCY_1\x10\x03\x12\x19\n\x15MOBILE_TF_VERSATILE_1\x10\x04\x12\x1d\n\x19MOBILE_TF_HIGH_ACCURACY_1\x10\x05"\xc5\x02\n"AutoMlImageObjectDetectionMetadata\x12\x1d\n\x15cost_milli_node_hours\x18\x01 \x01(\x03\x12\x96\x01\n\x16successful_stop_reason\x18\x02 \x01(\x0e2v.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlImageObjectDetectionMetadata.SuccessfulStopReason"g\n\x14SuccessfulStopReason\x12&\n"SUCCESSFUL_STOP_REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0eBUDGET_REACHED\x10\x01\x12\x13\n\x0fMODEL_CONVERGED\x10\x02B\x8f\x03\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1fAutoMLImageObjectDetectionProtoP\x01Zacloud.google.com/go/aiplatform/apiv1beta1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x02=Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition\xca\x02=Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\TrainingJob\\Definition\xea\x02CGoogle::Cloud::AIPlatform::V1beta1::Schema::TrainingJob::Definitionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automl_image_object_detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1fAutoMLImageObjectDetectionProtoP\x01Zacloud.google.com/go/aiplatform/apiv1beta1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x02=Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition\xca\x02=Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\TrainingJob\\Definition\xea\x02CGoogle::Cloud::AIPlatform::V1beta1::Schema::TrainingJob::Definition'
    _globals['_AUTOMLIMAGEOBJECTDETECTION']._serialized_start = 165
    _globals['_AUTOMLIMAGEOBJECTDETECTION']._serialized_end = 423
    _globals['_AUTOMLIMAGEOBJECTDETECTIONINPUTS']._serialized_start = 426
    _globals['_AUTOMLIMAGEOBJECTDETECTIONINPUTS']._serialized_end = 833
    _globals['_AUTOMLIMAGEOBJECTDETECTIONINPUTS_MODELTYPE']._serialized_start = 655
    _globals['_AUTOMLIMAGEOBJECTDETECTIONINPUTS_MODELTYPE']._serialized_end = 833
    _globals['_AUTOMLIMAGEOBJECTDETECTIONMETADATA']._serialized_start = 836
    _globals['_AUTOMLIMAGEOBJECTDETECTIONMETADATA']._serialized_end = 1161
    _globals['_AUTOMLIMAGEOBJECTDETECTIONMETADATA_SUCCESSFULSTOPREASON']._serialized_start = 1058
    _globals['_AUTOMLIMAGEOBJECTDETECTIONMETADATA_SUCCESSFULSTOPREASON']._serialized_end = 1161