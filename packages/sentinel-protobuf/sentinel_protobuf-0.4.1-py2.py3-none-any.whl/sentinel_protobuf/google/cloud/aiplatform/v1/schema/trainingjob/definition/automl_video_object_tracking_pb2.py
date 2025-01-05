"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_video_object_tracking.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n[google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_video_object_tracking.proto\x128google.cloud.aiplatform.v1.schema.trainingjob.definition"\x86\x01\n\x19AutoMlVideoObjectTracking\x12i\n\x06inputs\x18\x01 \x01(\x0b2Y.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoObjectTrackingInputs"\xe5\x02\n\x1fAutoMlVideoObjectTrackingInputs\x12w\n\nmodel_type\x18\x01 \x01(\x0e2c.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoObjectTrackingInputs.ModelType"\xc8\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05CLOUD\x10\x01\x12\x16\n\x12MOBILE_VERSATILE_1\x10\x02\x12\x1c\n\x18MOBILE_CORAL_VERSATILE_1\x10\x03\x12\x1e\n\x1aMOBILE_CORAL_LOW_LATENCY_1\x10\x04\x12\x1d\n\x19MOBILE_JETSON_VERSATILE_1\x10\x05\x12\x1f\n\x1bMOBILE_JETSON_LOW_LATENCY_1\x10\x06B\xf5\x02\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\x1eAutoMLVideoObjectTrackingProtoP\x01Z\\cloud.google.com/go/aiplatform/apiv1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definitionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_video_object_tracking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\x1eAutoMLVideoObjectTrackingProtoP\x01Z\\cloud.google.com/go/aiplatform/apiv1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition'
    _globals['_AUTOMLVIDEOOBJECTTRACKING']._serialized_start = 154
    _globals['_AUTOMLVIDEOOBJECTTRACKING']._serialized_end = 288
    _globals['_AUTOMLVIDEOOBJECTTRACKINGINPUTS']._serialized_start = 291
    _globals['_AUTOMLVIDEOOBJECTTRACKINGINPUTS']._serialized_end = 648
    _globals['_AUTOMLVIDEOOBJECTTRACKINGINPUTS_MODELTYPE']._serialized_start = 448
    _globals['_AUTOMLVIDEOOBJECTTRACKINGINPUTS_MODELTYPE']._serialized_end = 648