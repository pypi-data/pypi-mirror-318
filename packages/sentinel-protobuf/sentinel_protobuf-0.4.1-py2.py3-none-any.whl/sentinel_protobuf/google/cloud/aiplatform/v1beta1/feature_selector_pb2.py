"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/feature_selector.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/feature_selector.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto"\x1d\n\tIdMatcher\x12\x10\n\x03ids\x18\x01 \x03(\tB\x03\xe0A\x02"V\n\x0fFeatureSelector\x12C\n\nid_matcher\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.IdMatcherB\x03\xe0A\x02B\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14FeatureSelectorProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_selector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14FeatureSelectorProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_IDMATCHER'].fields_by_name['ids']._loaded_options = None
    _globals['_IDMATCHER'].fields_by_name['ids']._serialized_options = b'\xe0A\x02'
    _globals['_FEATURESELECTOR'].fields_by_name['id_matcher']._loaded_options = None
    _globals['_FEATURESELECTOR'].fields_by_name['id_matcher']._serialized_options = b'\xe0A\x02'
    _globals['_IDMATCHER']._serialized_start = 124
    _globals['_IDMATCHER']._serialized_end = 153
    _globals['_FEATURESELECTOR']._serialized_start = 155
    _globals['_FEATURESELECTOR']._serialized_end = 241