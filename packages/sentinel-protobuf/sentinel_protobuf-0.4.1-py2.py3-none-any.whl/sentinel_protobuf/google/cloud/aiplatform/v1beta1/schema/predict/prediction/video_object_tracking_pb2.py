"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/predict/prediction/video_object_tracking.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nUgoogle/cloud/aiplatform/v1beta1/schema/predict/prediction/video_object_tracking.proto\x129google.cloud.aiplatform.v1beta1.schema.predict.prediction\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xc4\x04\n#VideoObjectTrackingPredictionResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x125\n\x12time_segment_start\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x123\n\x10time_segment_end\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12/\n\nconfidence\x18\x05 \x01(\x0b2\x1b.google.protobuf.FloatValue\x12t\n\x06frames\x18\x06 \x03(\x0b2d.google.cloud.aiplatform.v1beta1.schema.predict.prediction.VideoObjectTrackingPredictionResult.Frame\x1a\xe7\x01\n\x05Frame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12*\n\x05x_min\x18\x02 \x01(\x0b2\x1b.google.protobuf.FloatValue\x12*\n\x05x_max\x18\x03 \x01(\x0b2\x1b.google.protobuf.FloatValue\x12*\n\x05y_min\x18\x04 \x01(\x0b2\x1b.google.protobuf.FloatValue\x12*\n\x05y_max\x18\x05 \x01(\x0b2\x1b.google.protobuf.FloatValueB\x84\x03\n=com.google.cloud.aiplatform.v1beta1.schema.predict.predictionB(VideoObjectTrackingPredictionResultProtoP\x01Z]cloud.google.com/go/aiplatform/apiv1beta1/schema/predict/prediction/predictionpb;predictionpb\xaa\x029Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction\xca\x029Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\Predict\\Prediction\xea\x02?Google::Cloud::AIPlatform::V1beta1::Schema::Predict::Predictionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.predict.prediction.video_object_tracking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n=com.google.cloud.aiplatform.v1beta1.schema.predict.predictionB(VideoObjectTrackingPredictionResultProtoP\x01Z]cloud.google.com/go/aiplatform/apiv1beta1/schema/predict/prediction/predictionpb;predictionpb\xaa\x029Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction\xca\x029Google\\Cloud\\AIPlatform\\V1beta1\\Schema\\Predict\\Prediction\xea\x02?Google::Cloud::AIPlatform::V1beta1::Schema::Predict::Prediction'
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT']._serialized_start = 213
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT']._serialized_end = 793
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_FRAME']._serialized_start = 562
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_FRAME']._serialized_end = 793