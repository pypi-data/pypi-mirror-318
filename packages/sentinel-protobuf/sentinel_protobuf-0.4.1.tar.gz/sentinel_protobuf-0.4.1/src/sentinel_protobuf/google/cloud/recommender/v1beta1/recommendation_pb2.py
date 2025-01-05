"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommender/v1beta1/recommendation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/recommender/v1beta1/recommendation.proto\x12 google.cloud.recommender.v1beta1\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\xc0\t\n\x0eRecommendation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x1b\n\x13recommender_subtype\x18\x0c \x01(\t\x125\n\x11last_refresh_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\x0eprimary_impact\x18\x05 \x01(\x0b2(.google.cloud.recommender.v1beta1.Impact\x12C\n\x11additional_impact\x18\x06 \x03(\x0b2(.google.cloud.recommender.v1beta1.Impact\x12K\n\x08priority\x18\x11 \x01(\x0e29.google.cloud.recommender.v1beta1.Recommendation.Priority\x12H\n\x07content\x18\x07 \x01(\x0b27.google.cloud.recommender.v1beta1.RecommendationContent\x12M\n\nstate_info\x18\n \x01(\x0b29.google.cloud.recommender.v1beta1.RecommendationStateInfo\x12\x0c\n\x04etag\x18\x0b \x01(\t\x12^\n\x13associated_insights\x18\x0e \x03(\x0b2A.google.cloud.recommender.v1beta1.Recommendation.InsightReference\x12\x14\n\x0cxor_group_id\x18\x12 \x01(\t\x1a#\n\x10InsightReference\x12\x0f\n\x07insight\x18\x01 \x01(\t"D\n\x08Priority\x12\x18\n\x14PRIORITY_UNSPECIFIED\x10\x00\x12\x06\n\x02P4\x10\x01\x12\x06\n\x02P3\x10\x02\x12\x06\n\x02P2\x10\x03\x12\x06\n\x02P1\x10\x04:\xda\x03\xeaA\xd6\x03\n)recommender.googleapis.com/Recommendation\x12cprojects/{project}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}\x12rbillingAccounts/{billing_account}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}\x12afolders/{folder}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}\x12morganizations/{organization}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}"\x8e\x01\n\x15RecommendationContent\x12J\n\x10operation_groups\x18\x02 \x03(\x0b20.google.cloud.recommender.v1beta1.OperationGroup\x12)\n\x08overview\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct"Q\n\x0eOperationGroup\x12?\n\noperations\x18\x01 \x03(\x0b2+.google.cloud.recommender.v1beta1.Operation"\xeb\x04\n\tOperation\x12\x0e\n\x06action\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x17\n\x0fsource_resource\x18\x05 \x01(\t\x12\x13\n\x0bsource_path\x18\x06 \x01(\t\x12\'\n\x05value\x18\x07 \x01(\x0b2\x16.google.protobuf.ValueH\x00\x12G\n\rvalue_matcher\x18\n \x01(\x0b2..google.cloud.recommender.v1beta1.ValueMatcherH\x00\x12R\n\x0cpath_filters\x18\x08 \x03(\x0b2<.google.cloud.recommender.v1beta1.Operation.PathFiltersEntry\x12_\n\x13path_value_matchers\x18\x0b \x03(\x0b2B.google.cloud.recommender.v1beta1.Operation.PathValueMatchersEntry\x1aJ\n\x10PathFiltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1ah\n\x16PathValueMatchersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.cloud.recommender.v1beta1.ValueMatcher:\x028\x01B\x0c\n\npath_value":\n\x0cValueMatcher\x12\x19\n\x0fmatches_pattern\x18\x01 \x01(\tH\x00B\x0f\n\rmatch_variant"_\n\x0eCostProjection\x12 \n\x04cost\x18\x01 \x01(\x0b2\x12.google.type.Money\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration">\n\x12SecurityProjection\x12(\n\x07details\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct"Y\n\x18SustainabilityProjection\x12\x10\n\x08kg_c_o2e\x18\x01 \x01(\x01\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xd4\x03\n\x06Impact\x12C\n\x08category\x18\x01 \x01(\x0e21.google.cloud.recommender.v1beta1.Impact.Category\x12K\n\x0fcost_projection\x18d \x01(\x0b20.google.cloud.recommender.v1beta1.CostProjectionH\x00\x12S\n\x13security_projection\x18e \x01(\x0b24.google.cloud.recommender.v1beta1.SecurityProjectionH\x00\x12_\n\x19sustainability_projection\x18f \x01(\x0b2:.google.cloud.recommender.v1beta1.SustainabilityProjectionH\x00"t\n\x08Category\x12\x18\n\x14CATEGORY_UNSPECIFIED\x10\x00\x12\x08\n\x04COST\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0f\n\x0bPERFORMANCE\x10\x03\x12\x11\n\rMANAGEABILITY\x10\x04\x12\x12\n\x0eSUSTAINABILITY\x10\x05B\x0c\n\nprojection"\xe8\x02\n\x17RecommendationStateInfo\x12N\n\x05state\x18\x01 \x01(\x0e2?.google.cloud.recommender.v1beta1.RecommendationStateInfo.State\x12d\n\x0estate_metadata\x18\x02 \x03(\x0b2L.google.cloud.recommender.v1beta1.RecommendationStateInfo.StateMetadataEntry\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"a\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07CLAIMED\x10\x06\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\r\n\tDISMISSED\x10\x05"\x91\x03\n\x0fRecommenderType\x12\x0c\n\x04name\x18\x01 \x01(\t:\xef\x02\xeaA\xeb\x02\n&recommender.googleapis.com/Recommender\x12Bprojects/{project}/locations/{location}/recommenders/{recommender}\x12QbillingAccounts/{billing_account}/locations/{location}/recommenders/{recommender}\x12@folders/{folder}/locations/{location}/recommenders/{recommender}\x12Lorganizations/{organization}/locations/{location}/recommenders/{recommender}\x12\x1arecommenders/{recommender}B\x9a\x01\n$com.google.cloud.recommender.v1beta1P\x01ZFcloud.google.com/go/recommender/apiv1beta1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02 Google.Cloud.Recommender.V1Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommender.v1beta1.recommendation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.recommender.v1beta1P\x01ZFcloud.google.com/go/recommender/apiv1beta1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02 Google.Cloud.Recommender.V1Beta1'
    _globals['_RECOMMENDATION']._loaded_options = None
    _globals['_RECOMMENDATION']._serialized_options = b'\xeaA\xd6\x03\n)recommender.googleapis.com/Recommendation\x12cprojects/{project}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}\x12rbillingAccounts/{billing_account}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}\x12afolders/{folder}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}\x12morganizations/{organization}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}'
    _globals['_OPERATION_PATHFILTERSENTRY']._loaded_options = None
    _globals['_OPERATION_PATHFILTERSENTRY']._serialized_options = b'8\x01'
    _globals['_OPERATION_PATHVALUEMATCHERSENTRY']._loaded_options = None
    _globals['_OPERATION_PATHVALUEMATCHERSENTRY']._serialized_options = b'8\x01'
    _globals['_RECOMMENDATIONSTATEINFO_STATEMETADATAENTRY']._loaded_options = None
    _globals['_RECOMMENDATIONSTATEINFO_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_RECOMMENDERTYPE']._loaded_options = None
    _globals['_RECOMMENDERTYPE']._serialized_options = b'\xeaA\xeb\x02\n&recommender.googleapis.com/Recommender\x12Bprojects/{project}/locations/{location}/recommenders/{recommender}\x12QbillingAccounts/{billing_account}/locations/{location}/recommenders/{recommender}\x12@folders/{folder}/locations/{location}/recommenders/{recommender}\x12Lorganizations/{organization}/locations/{location}/recommenders/{recommender}\x12\x1arecommenders/{recommender}'
    _globals['_RECOMMENDATION']._serialized_start = 239
    _globals['_RECOMMENDATION']._serialized_end = 1455
    _globals['_RECOMMENDATION_INSIGHTREFERENCE']._serialized_start = 873
    _globals['_RECOMMENDATION_INSIGHTREFERENCE']._serialized_end = 908
    _globals['_RECOMMENDATION_PRIORITY']._serialized_start = 910
    _globals['_RECOMMENDATION_PRIORITY']._serialized_end = 978
    _globals['_RECOMMENDATIONCONTENT']._serialized_start = 1458
    _globals['_RECOMMENDATIONCONTENT']._serialized_end = 1600
    _globals['_OPERATIONGROUP']._serialized_start = 1602
    _globals['_OPERATIONGROUP']._serialized_end = 1683
    _globals['_OPERATION']._serialized_start = 1686
    _globals['_OPERATION']._serialized_end = 2305
    _globals['_OPERATION_PATHFILTERSENTRY']._serialized_start = 2111
    _globals['_OPERATION_PATHFILTERSENTRY']._serialized_end = 2185
    _globals['_OPERATION_PATHVALUEMATCHERSENTRY']._serialized_start = 2187
    _globals['_OPERATION_PATHVALUEMATCHERSENTRY']._serialized_end = 2291
    _globals['_VALUEMATCHER']._serialized_start = 2307
    _globals['_VALUEMATCHER']._serialized_end = 2365
    _globals['_COSTPROJECTION']._serialized_start = 2367
    _globals['_COSTPROJECTION']._serialized_end = 2462
    _globals['_SECURITYPROJECTION']._serialized_start = 2464
    _globals['_SECURITYPROJECTION']._serialized_end = 2526
    _globals['_SUSTAINABILITYPROJECTION']._serialized_start = 2528
    _globals['_SUSTAINABILITYPROJECTION']._serialized_end = 2617
    _globals['_IMPACT']._serialized_start = 2620
    _globals['_IMPACT']._serialized_end = 3088
    _globals['_IMPACT_CATEGORY']._serialized_start = 2958
    _globals['_IMPACT_CATEGORY']._serialized_end = 3074
    _globals['_RECOMMENDATIONSTATEINFO']._serialized_start = 3091
    _globals['_RECOMMENDATIONSTATEINFO']._serialized_end = 3451
    _globals['_RECOMMENDATIONSTATEINFO_STATEMETADATAENTRY']._serialized_start = 3300
    _globals['_RECOMMENDATIONSTATEINFO_STATEMETADATAENTRY']._serialized_end = 3352
    _globals['_RECOMMENDATIONSTATEINFO_STATE']._serialized_start = 3354
    _globals['_RECOMMENDATIONSTATEINFO_STATE']._serialized_end = 3451
    _globals['_RECOMMENDERTYPE']._serialized_start = 3454
    _globals['_RECOMMENDERTYPE']._serialized_end = 3855