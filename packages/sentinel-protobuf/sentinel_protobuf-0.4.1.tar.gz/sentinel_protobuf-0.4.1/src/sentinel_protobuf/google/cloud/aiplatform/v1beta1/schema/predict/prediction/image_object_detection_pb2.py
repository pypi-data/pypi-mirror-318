"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/predict/prediction/image_object_detection.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nVgoogle/cloud/aiplatform/v1beta1/schema/predict/prediction/image_object_detection.proto\x129google.cloud.aiplatform.v1beta1.schema.predict.prediction\x1a\x1cgoogle/protobuf/struct.proto"\x8b\x01\n$ImageObjectDetectionPredictionResult\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12\x15\n\rdisplay_names\x18\x02 \x03(\t\x12\x13\n\x0bconfidences\x18\x03 \x03(\x02\x12*\n\x06bboxes\x18\x04 \x03(\x0b2\x1a.google.protobuf.ListValueB\x85\x03\n=com.google.cloud.aiplatform.v1beta1.schema.predict.predictionB)ImageObjectDetectionPredictionResultProtoP\x01Z]cloud.google.com/go/aiplatform/apiv1beta1/schema/predict/prediction/predictionpb;predictionpb\xaa\x029Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction\xca\x029Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\Predict\\Prediction\xea\x02?Google::Cloud::AIPlatform::V1beta1::Schema::Predict::Predictionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.predict.prediction.image_object_detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n=com.google.cloud.aiplatform.v1beta1.schema.predict.predictionB)ImageObjectDetectionPredictionResultProtoP\x01Z]cloud.google.com/go/aiplatform/apiv1beta1/schema/predict/prediction/predictionpb;predictionpb\xaa\x029Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction\xca\x029Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\Predict\\Prediction\xea\x02?Google::Cloud::AIPlatform::V1beta1::Schema::Predict::Prediction'
    _globals['_IMAGEOBJECTDETECTIONPREDICTIONRESULT']._serialized_start = 180
    _globals['_IMAGEOBJECTDETECTIONPREDICTIONRESULT']._serialized_end = 319