"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommender/v1/insight.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/recommender/v1/insight.proto\x12\x1bgoogle.cloud.recommender.v1\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\t\n\x07Insight\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x18\n\x10target_resources\x18\t \x03(\t\x12\x17\n\x0finsight_subtype\x18\n \x01(\t\x12(\n\x07content\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x125\n\x11last_refresh_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x125\n\x12observation_period\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12A\n\nstate_info\x18\x06 \x01(\x0b2-.google.cloud.recommender.v1.InsightStateInfo\x12?\n\x08category\x18\x07 \x01(\x0e2-.google.cloud.recommender.v1.Insight.Category\x12?\n\x08severity\x18\x0f \x01(\x0e2-.google.cloud.recommender.v1.Insight.Severity\x12\x0c\n\x04etag\x18\x0b \x01(\t\x12`\n\x1aassociated_recommendations\x18\x08 \x03(\x0b2<.google.cloud.recommender.v1.Insight.RecommendationReference\x1a1\n\x17RecommendationReference\x12\x16\n\x0erecommendation\x18\x01 \x01(\t"\x85\x01\n\x08Category\x12\x18\n\x14CATEGORY_UNSPECIFIED\x10\x00\x12\x08\n\x04COST\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0f\n\x0bPERFORMANCE\x10\x03\x12\x11\n\rMANAGEABILITY\x10\x04\x12\x12\n\x0eSUSTAINABILITY\x10\x05\x12\x0f\n\x0bRELIABILITY\x10\x06"Q\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03\x12\x0c\n\x08CRITICAL\x10\x04:\x9f\x03\xeaA\x9b\x03\n"recommender.googleapis.com/Insight\x12Vprojects/{project}/locations/{location}/insightTypes/{insight_type}/insights/{insight}\x12ebillingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}/insights/{insight}\x12Tfolders/{folder}/locations/{location}/insightTypes/{insight_type}/insights/{insight}\x12`organizations/{organization}/locations/{location}/insightTypes/{insight_type}/insights/{insight}"\xaf\x02\n\x10InsightStateInfo\x12B\n\x05state\x18\x01 \x01(\x0e23.google.cloud.recommender.v1.InsightStateInfo.State\x12X\n\x0estate_metadata\x18\x02 \x03(\x0b2@.google.cloud.recommender.v1.InsightStateInfo.StateMetadataEntry\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"G\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08ACCEPTED\x10\x02\x12\r\n\tDISMISSED\x10\x03B\xf0\x03\n\x1fcom.google.cloud.recommender.v1B\x0cInsightProtoP\x01ZAcloud.google.com/go/recommender/apiv1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02\x1bGoogle.Cloud.Recommender.V1\xeaA\xd3\x02\n&recommender.googleapis.com/InsightType\x12Cprojects/{project}/locations/{location}/insightTypes/{insight_type}\x12RbillingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}\x12Afolders/{folder}/locations/{location}/insightTypes/{insight_type}\x12Morganizations/{organization}/locations/{location}/insightTypes/{insight_type}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommender.v1.insight_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.recommender.v1B\x0cInsightProtoP\x01ZAcloud.google.com/go/recommender/apiv1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02\x1bGoogle.Cloud.Recommender.V1\xeaA\xd3\x02\n&recommender.googleapis.com/InsightType\x12Cprojects/{project}/locations/{location}/insightTypes/{insight_type}\x12RbillingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}\x12Afolders/{folder}/locations/{location}/insightTypes/{insight_type}\x12Morganizations/{organization}/locations/{location}/insightTypes/{insight_type}'
    _globals['_INSIGHT']._loaded_options = None
    _globals['_INSIGHT']._serialized_options = b'\xeaA\x9b\x03\n"recommender.googleapis.com/Insight\x12Vprojects/{project}/locations/{location}/insightTypes/{insight_type}/insights/{insight}\x12ebillingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}/insights/{insight}\x12Tfolders/{folder}/locations/{location}/insightTypes/{insight_type}/insights/{insight}\x12`organizations/{organization}/locations/{location}/insightTypes/{insight_type}/insights/{insight}'
    _globals['_INSIGHTSTATEINFO_STATEMETADATAENTRY']._loaded_options = None
    _globals['_INSIGHTSTATEINFO_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_INSIGHT']._serialized_start = 197
    _globals['_INSIGHT']._serialized_end = 1441
    _globals['_INSIGHT_RECOMMENDATIONREFERENCE']._serialized_start = 755
    _globals['_INSIGHT_RECOMMENDATIONREFERENCE']._serialized_end = 804
    _globals['_INSIGHT_CATEGORY']._serialized_start = 807
    _globals['_INSIGHT_CATEGORY']._serialized_end = 940
    _globals['_INSIGHT_SEVERITY']._serialized_start = 942
    _globals['_INSIGHT_SEVERITY']._serialized_end = 1023
    _globals['_INSIGHTSTATEINFO']._serialized_start = 1444
    _globals['_INSIGHTSTATEINFO']._serialized_end = 1747
    _globals['_INSIGHTSTATEINFO_STATEMETADATAENTRY']._serialized_start = 1622
    _globals['_INSIGHTSTATEINFO_STATEMETADATAENTRY']._serialized_end = 1674
    _globals['_INSIGHTSTATEINFO_STATE']._serialized_start = 1676
    _globals['_INSIGHTSTATEINFO_STATE']._serialized_end = 1747