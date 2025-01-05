"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/io_format.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.aiplatform.v1beta1.schema import annotation_spec_color_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_schema_dot_annotation__spec__color__pb2
from ......google.cloud.aiplatform.v1beta1.schema import geometry_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_schema_dot_geometry__pb2
from ......google.cloud.aiplatform.v1beta1.schema.predict.instance import text_sentiment_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_schema_dot_predict_dot_instance_dot_text__sentiment__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/schema/io_format.proto\x12&google.cloud.aiplatform.v1beta1.schema\x1aBgoogle/cloud/aiplatform/v1beta1/schema/annotation_spec_color.proto\x1a5google/cloud/aiplatform/v1beta1/schema/geometry.proto\x1aLgoogle/cloud/aiplatform/v1beta1/schema/predict/instance/text_sentiment.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x15google/rpc/code.proto\x1a\x1cgoogle/api/annotations.proto"\x8e\x02\n\x10PredictionResult\x12+\n\x08instance\x18\x01 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12\r\n\x03key\x18\x02 \x01(\tH\x00\x12*\n\nprediction\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12M\n\x05error\x18\x04 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.schema.PredictionResult.Error\x1a:\n\x05Error\x12 \n\x06status\x18\x01 \x01(\x0e2\x10.google.rpc.Code\x12\x0f\n\x07message\x18\x02 \x01(\tB\x07\n\x05inputB\x80\x02\n*com.google.cloud.aiplatform.v1beta1.schemaB\rIoFormatProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schemab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.io_format_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.aiplatform.v1beta1.schemaB\rIoFormatProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schema'
    _globals['_PREDICTIONRESULT']._serialized_start = 415
    _globals['_PREDICTIONRESULT']._serialized_end = 685
    _globals['_PREDICTIONRESULT_ERROR']._serialized_start = 618
    _globals['_PREDICTIONRESULT_ERROR']._serialized_end = 676