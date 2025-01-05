"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/recommendationengine/v1beta1/common.proto\x12)google.cloud.recommendationengine.v1beta1"\x96\x04\n\nFeatureMap\x12l\n\x14categorical_features\x18\x01 \x03(\x0b2N.google.cloud.recommendationengine.v1beta1.FeatureMap.CategoricalFeaturesEntry\x12h\n\x12numerical_features\x18\x02 \x03(\x0b2L.google.cloud.recommendationengine.v1beta1.FeatureMap.NumericalFeaturesEntry\x1a\x1b\n\nStringList\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1a\n\tFloatList\x12\r\n\x05value\x18\x01 \x03(\x02\x1a|\n\x18CategoricalFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12O\n\x05value\x18\x02 \x01(\x0b2@.google.cloud.recommendationengine.v1beta1.FeatureMap.StringList:\x028\x01\x1ay\n\x16NumericalFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b2?.google.cloud.recommendationengine.v1beta1.FeatureMap.FloatList:\x028\x01B\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_FEATUREMAP_CATEGORICALFEATURESENTRY']._loaded_options = None
    _globals['_FEATUREMAP_CATEGORICALFEATURESENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREMAP_NUMERICALFEATURESENTRY']._loaded_options = None
    _globals['_FEATUREMAP_NUMERICALFEATURESENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREMAP']._serialized_start = 102
    _globals['_FEATUREMAP']._serialized_end = 636
    _globals['_FEATUREMAP_STRINGLIST']._serialized_start = 332
    _globals['_FEATUREMAP_STRINGLIST']._serialized_end = 359
    _globals['_FEATUREMAP_FLOATLIST']._serialized_start = 361
    _globals['_FEATUREMAP_FLOATLIST']._serialized_end = 387
    _globals['_FEATUREMAP_CATEGORICALFEATURESENTRY']._serialized_start = 389
    _globals['_FEATUREMAP_CATEGORICALFEATURESENTRY']._serialized_end = 513
    _globals['_FEATUREMAP_NUMERICALFEATURESENTRY']._serialized_start = 515
    _globals['_FEATUREMAP_NUMERICALFEATURESENTRY']._serialized_end = 636