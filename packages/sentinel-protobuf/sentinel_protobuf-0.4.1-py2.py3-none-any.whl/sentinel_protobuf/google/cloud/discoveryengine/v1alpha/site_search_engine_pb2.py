"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/site_search_engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/discoveryengine/v1alpha/site_search_engine.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\x02\n\x10SiteSearchEngine\x12\x0c\n\x04name\x18\x01 \x01(\t:\xf2\x01\xeaA\xee\x01\n/discoveryengine.googleapis.com/SiteSearchEngine\x12Pprojects/{project}/locations/{location}/dataStores/{data_store}/siteSearchEngine\x12iprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine"\xaf\t\n\nTargetSite\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12$\n\x14provided_uri_pattern\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x04\x12C\n\x04type\x18\x03 \x01(\x0e25.google.cloud.discoveryengine.v1alpha.TargetSite.Type\x12\x18\n\x0bexact_match\x18\x06 \x01(\x08B\x03\xe0A\x04\x12"\n\x15generated_uri_pattern\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0froot_domain_uri\x18\n \x01(\tB\x03\xe0A\x03\x12_\n\x16site_verification_info\x18\x07 \x01(\x0b2:.google.cloud.discoveryengine.v1alpha.SiteVerificationInfoB\x03\xe0A\x03\x12]\n\x0findexing_status\x18\x08 \x01(\x0e2?.google.cloud.discoveryengine.v1alpha.TargetSite.IndexingStatusB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12[\n\x0efailure_reason\x18\t \x01(\x0b2>.google.cloud.discoveryengine.v1alpha.TargetSite.FailureReasonB\x03\xe0A\x03\x1a\xae\x01\n\rFailureReason\x12d\n\rquota_failure\x18\x01 \x01(\x0b2K.google.cloud.discoveryengine.v1alpha.TargetSite.FailureReason.QuotaFailureH\x00\x1a,\n\x0cQuotaFailure\x12\x1c\n\x14total_required_quota\x18\x01 \x01(\x03B\t\n\x07failure"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INCLUDE\x10\x01\x12\x0b\n\x07EXCLUDE\x10\x02"g\n\x0eIndexingStatus\x12\x1f\n\x1bINDEXING_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\x0c\n\x08DELETING\x10\x04:\xa1\x02\xeaA\x9d\x02\n)discoveryengine.googleapis.com/TargetSite\x12jprojects/{project}/locations/{location}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}\x12\x83\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}"\xa8\x02\n\x14SiteVerificationInfo\x12q\n\x17site_verification_state\x18\x01 \x01(\x0e2P.google.cloud.discoveryengine.v1alpha.SiteVerificationInfo.SiteVerificationState\x12/\n\x0bverify_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"l\n\x15SiteVerificationState\x12\'\n#SITE_VERIFICATION_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08VERIFIED\x10\x01\x12\x0e\n\nUNVERIFIED\x10\x02\x12\x0c\n\x08EXEMPTED\x10\x03B\xa1\x02\n(com.google.cloud.discoveryengine.v1alphaB\x15SiteSearchEngineProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.site_search_engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x15SiteSearchEngineProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_SITESEARCHENGINE']._loaded_options = None
    _globals['_SITESEARCHENGINE']._serialized_options = b'\xeaA\xee\x01\n/discoveryengine.googleapis.com/SiteSearchEngine\x12Pprojects/{project}/locations/{location}/dataStores/{data_store}/siteSearchEngine\x12iprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine'
    _globals['_TARGETSITE'].fields_by_name['name']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE'].fields_by_name['provided_uri_pattern']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['provided_uri_pattern']._serialized_options = b'\xe0A\x02\xe0A\x04'
    _globals['_TARGETSITE'].fields_by_name['exact_match']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['exact_match']._serialized_options = b'\xe0A\x04'
    _globals['_TARGETSITE'].fields_by_name['generated_uri_pattern']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['generated_uri_pattern']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE'].fields_by_name['root_domain_uri']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['root_domain_uri']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE'].fields_by_name['site_verification_info']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['site_verification_info']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE'].fields_by_name['indexing_status']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['indexing_status']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE'].fields_by_name['update_time']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE'].fields_by_name['failure_reason']._loaded_options = None
    _globals['_TARGETSITE'].fields_by_name['failure_reason']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETSITE']._loaded_options = None
    _globals['_TARGETSITE']._serialized_options = b'\xeaA\x9d\x02\n)discoveryengine.googleapis.com/TargetSite\x12jprojects/{project}/locations/{location}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}\x12\x83\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}'
    _globals['_SITESEARCHENGINE']._serialized_start = 197
    _globals['_SITESEARCHENGINE']._serialized_end = 474
    _globals['_TARGETSITE']._serialized_start = 477
    _globals['_TARGETSITE']._serialized_end = 1676
    _globals['_TARGETSITE_FAILUREREASON']._serialized_start = 1049
    _globals['_TARGETSITE_FAILUREREASON']._serialized_end = 1223
    _globals['_TARGETSITE_FAILUREREASON_QUOTAFAILURE']._serialized_start = 1168
    _globals['_TARGETSITE_FAILUREREASON_QUOTAFAILURE']._serialized_end = 1212
    _globals['_TARGETSITE_TYPE']._serialized_start = 1225
    _globals['_TARGETSITE_TYPE']._serialized_end = 1279
    _globals['_TARGETSITE_INDEXINGSTATUS']._serialized_start = 1281
    _globals['_TARGETSITE_INDEXINGSTATUS']._serialized_end = 1384
    _globals['_SITEVERIFICATIONINFO']._serialized_start = 1679
    _globals['_SITEVERIFICATIONINFO']._serialized_end = 1975
    _globals['_SITEVERIFICATIONINFO_SITEVERIFICATIONSTATE']._serialized_start = 1867
    _globals['_SITEVERIFICATIONINFO_SITEVERIFICATIONSTATE']._serialized_end = 1975