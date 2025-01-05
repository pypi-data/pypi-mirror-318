"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_video_action_recognition.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n^google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_video_action_recognition.proto\x128google.cloud.aiplatform.v1.schema.trainingjob.definition"\x8c\x01\n\x1cAutoMlVideoActionRecognition\x12l\n\x06inputs\x18\x01 \x01(\x0b2\\.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoActionRecognitionInputs"\xaa\x02\n"AutoMlVideoActionRecognitionInputs\x12z\n\nmodel_type\x18\x01 \x01(\x0e2f.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoActionRecognitionInputs.ModelType"\x87\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05CLOUD\x10\x01\x12\x16\n\x12MOBILE_VERSATILE_1\x10\x02\x12\x1d\n\x19MOBILE_JETSON_VERSATILE_1\x10\x03\x12\x1c\n\x18MOBILE_CORAL_VERSATILE_1\x10\x04B\xf8\x02\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB!AutoMLVideoActionRecognitionProtoP\x01Z\\cloud.google.com/go/aiplatform/apiv1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definitionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_video_action_recognition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB!AutoMLVideoActionRecognitionProtoP\x01Z\\cloud.google.com/go/aiplatform/apiv1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition'
    _globals['_AUTOMLVIDEOACTIONRECOGNITION']._serialized_start = 157
    _globals['_AUTOMLVIDEOACTIONRECOGNITION']._serialized_end = 297
    _globals['_AUTOMLVIDEOACTIONRECOGNITIONINPUTS']._serialized_start = 300
    _globals['_AUTOMLVIDEOACTIONRECOGNITIONINPUTS']._serialized_end = 598
    _globals['_AUTOMLVIDEOACTIONRECOGNITIONINPUTS_MODELTYPE']._serialized_start = 463
    _globals['_AUTOMLVIDEOACTIONRECOGNITIONINPUTS_MODELTYPE']._serialized_end = 598