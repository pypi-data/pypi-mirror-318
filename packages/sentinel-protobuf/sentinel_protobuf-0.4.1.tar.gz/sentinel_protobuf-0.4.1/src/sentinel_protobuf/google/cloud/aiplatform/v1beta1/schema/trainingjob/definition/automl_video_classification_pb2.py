"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_video_classification.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n_google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_video_classification.proto\x12=google.cloud.aiplatform.v1beta1.schema.trainingjob.definition"\x8b\x01\n\x19AutoMlVideoClassification\x12n\n\x06inputs\x18\x01 \x01(\x0b2^.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlVideoClassificationInputs"\x8a\x02\n\x1fAutoMlVideoClassificationInputs\x12|\n\nmodel_type\x18\x01 \x01(\x0e2h.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlVideoClassificationInputs.ModelType"i\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05CLOUD\x10\x01\x12\x16\n\x12MOBILE_VERSATILE_1\x10\x02\x12\x1d\n\x19MOBILE_JETSON_VERSATILE_1\x10\x03B\x8e\x03\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1eAutoMLVideoClassificationProtoP\x01Zacloud.google.com/go/aiplatform/apiv1beta1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x02=Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition\xca\x02=Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\TrainingJob\\Definition\xea\x02CGoogle::Cloud::AIPlatform::V1beta1::Schema::TrainingJob::Definitionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automl_video_classification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1eAutoMLVideoClassificationProtoP\x01Zacloud.google.com/go/aiplatform/apiv1beta1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x02=Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition\xca\x02=Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\TrainingJob\\Definition\xea\x02CGoogle::Cloud::AIPlatform::V1beta1::Schema::TrainingJob::Definition'
    _globals['_AUTOMLVIDEOCLASSIFICATION']._serialized_start = 163
    _globals['_AUTOMLVIDEOCLASSIFICATION']._serialized_end = 302
    _globals['_AUTOMLVIDEOCLASSIFICATIONINPUTS']._serialized_start = 305
    _globals['_AUTOMLVIDEOCLASSIFICATIONINPUTS']._serialized_end = 571
    _globals['_AUTOMLVIDEOCLASSIFICATIONINPUTS_MODELTYPE']._serialized_start = 466
    _globals['_AUTOMLVIDEOCLASSIFICATIONINPUTS_MODELTYPE']._serialized_end = 571