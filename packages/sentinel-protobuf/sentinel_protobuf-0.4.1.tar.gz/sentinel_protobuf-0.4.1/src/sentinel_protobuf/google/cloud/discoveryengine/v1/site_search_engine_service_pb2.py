"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/site_search_engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import site_search_engine_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_site__search__engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/discoveryengine/v1/site_search_engine_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/discoveryengine/v1/site_search_engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"c\n\x1aGetSiteSearchEngineRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine"\xa9\x01\n\x17CreateTargetSiteRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12E\n\x0btarget_site\x18\x02 \x01(\x0b2+.google.cloud.discoveryengine.v1.TargetSiteB\x03\xe0A\x02"|\n\x18CreateTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xb9\x01\n\x1dBatchCreateTargetSitesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12O\n\x08requests\x18\x02 \x03(\x0b28.google.cloud.discoveryengine.v1.CreateTargetSiteRequestB\x03\xe0A\x02"W\n\x14GetTargetSiteRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/TargetSite"`\n\x17UpdateTargetSiteRequest\x12E\n\x0btarget_site\x18\x01 \x01(\x0b2+.google.cloud.discoveryengine.v1.TargetSiteB\x03\xe0A\x02"|\n\x18UpdateTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"Z\n\x17DeleteTargetSiteRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/TargetSite"|\n\x18DeleteTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x88\x01\n\x16ListTargetSitesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x89\x01\n\x17ListTargetSitesResponse\x12A\n\x0ctarget_sites\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1.TargetSite\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x81\x01\n\x1dBatchCreateTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"c\n\x1eBatchCreateTargetSitesResponse\x12A\n\x0ctarget_sites\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1.TargetSite"v\n\x1fEnableAdvancedSiteSearchRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine""\n EnableAdvancedSiteSearchResponse"\x84\x01\n EnableAdvancedSiteSearchMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"w\n DisableAdvancedSiteSearchRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine"#\n!DisableAdvancedSiteSearchResponse"\x85\x01\n!DisableAdvancedSiteSearchMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x9a\x01\n\x12RecrawlUrisRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12\x11\n\x04uris\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x1c\n\x0fsite_credential\x18\x05 \x01(\tB\x03\xe0A\x01"\xe8\x03\n\x13RecrawlUrisResponse\x12Y\n\x0ffailure_samples\x18\x01 \x03(\x0b2@.google.cloud.discoveryengine.v1.RecrawlUrisResponse.FailureInfo\x12\x13\n\x0bfailed_uris\x18\x02 \x03(\t\x1a\xe0\x02\n\x0bFailureInfo\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12g\n\x0ffailure_reasons\x18\x02 \x03(\x0b2N.google.cloud.discoveryengine.v1.RecrawlUrisResponse.FailureInfo.FailureReason\x1a\xda\x01\n\rFailureReason\x12n\n\x0bcorpus_type\x18\x01 \x01(\x0e2Y.google.cloud.discoveryengine.v1.RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType\x12\x15\n\rerror_message\x18\x02 \x01(\t"B\n\nCorpusType\x12\x1b\n\x17CORPUS_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DESKTOP\x10\x01\x12\n\n\x06MOBILE\x10\x02"\xf3\x01\n\x13RecrawlUrisMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0cinvalid_uris\x18\x03 \x03(\t\x12\x18\n\x10valid_uris_count\x18\x04 \x01(\x05\x12\x15\n\rsuccess_count\x18\x05 \x01(\x05\x12\x15\n\rpending_count\x18\x06 \x01(\x05\x12\x1c\n\x14quota_exceeded_count\x18\x07 \x01(\x05"h\n\x1dBatchVerifyTargetSitesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine" \n\x1eBatchVerifyTargetSitesResponse"\x82\x01\n\x1eBatchVerifyTargetSitesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa2\x01\n$FetchDomainVerificationStatusRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x97\x01\n%FetchDomainVerificationStatusResponse\x12A\n\x0ctarget_sites\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1.TargetSite\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xb5&\n\x17SiteSearchEngineService\x12\xa8\x02\n\x13GetSiteSearchEngine\x12;.google.cloud.discoveryengine.v1.GetSiteSearchEngineRequest\x1a1.google.cloud.discoveryengine.v1.SiteSearchEngine"\xa0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01\x12?/v1/{name=projects/*/locations/*/dataStores/*/siteSearchEngine}ZO\x12M/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}\x12\xbb\x03\n\x10CreateTargetSite\x128.google.cloud.discoveryengine.v1.CreateTargetSiteRequest\x1a\x1d.google.longrunning.Operation"\xcd\x02\xcaAf\n*google.cloud.discoveryengine.v1.TargetSite\x128google.cloud.discoveryengine.v1.CreateTargetSiteMetadata\xdaA\x12parent,target_site\x82\xd3\xe4\x93\x02\xc8\x01"M/v1/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_siteZj"[/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_site\x12\xcf\x03\n\x16BatchCreateTargetSites\x12>.google.cloud.discoveryengine.v1.BatchCreateTargetSitesRequest\x1a\x1d.google.longrunning.Operation"\xd5\x02\xcaA\x7f\n>google.cloud.discoveryengine.v1.BatchCreateTargetSitesResponse\x12=google.cloud.discoveryengine.v1.BatchCreateTargetSiteMetadata\x82\xd3\xe4\x93\x02\xcc\x01"Y/v1/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*Zl"g/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*\x12\xb2\x02\n\rGetTargetSite\x125.google.cloud.discoveryengine.v1.GetTargetSiteRequest\x1a+.google.cloud.discoveryengine.v1.TargetSite"\xbc\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xae\x01\x12M/v1/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Z]\x12[/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}\x12\xcc\x03\n\x10UpdateTargetSite\x128.google.cloud.discoveryengine.v1.UpdateTargetSiteRequest\x1a\x1d.google.longrunning.Operation"\xde\x02\xcaAf\n*google.cloud.discoveryengine.v1.TargetSite\x128google.cloud.discoveryengine.v1.UpdateTargetSiteMetadata\xdaA\x0btarget_site\x82\xd3\xe4\x93\x02\xe0\x012Y/v1/{target_site.name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_siteZv2g/v1/{target_site.name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_site\x12\xfe\x02\n\x10DeleteTargetSite\x128.google.cloud.discoveryengine.v1.DeleteTargetSiteRequest\x1a\x1d.google.longrunning.Operation"\x90\x02\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1.DeleteTargetSiteMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xae\x01*M/v1/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Z]*[/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}\x12\xc5\x02\n\x0fListTargetSites\x127.google.cloud.discoveryengine.v1.ListTargetSitesRequest\x1a8.google.cloud.discoveryengine.v1.ListTargetSitesResponse"\xbe\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xae\x01\x12M/v1/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSitesZ]\x12[/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites\x12\xf3\x03\n\x18EnableAdvancedSiteSearch\x12@.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchRequest\x1a\x1d.google.longrunning.Operation"\xf5\x02\xcaA\x84\x01\n@google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchResponse\x12@google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xe6\x01"f/v1/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*Zy"t/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*\x12\xf9\x03\n\x19DisableAdvancedSiteSearch\x12A.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchRequest\x1a\x1d.google.longrunning.Operation"\xf9\x02\xcaA\x86\x01\nAgoogle.cloud.discoveryengine.v1.DisableAdvancedSiteSearchResponse\x12Agoogle.cloud.discoveryengine.v1.DisableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xe8\x01"g/v1/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*Zz"u/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*\x12\xa4\x03\n\x0bRecrawlUris\x123.google.cloud.discoveryengine.v1.RecrawlUrisRequest\x1a\x1d.google.longrunning.Operation"\xc0\x02\xcaAj\n3google.cloud.discoveryengine.v1.RecrawlUrisResponse\x123google.cloud.discoveryengine.v1.RecrawlUrisMetadata\x82\xd3\xe4\x93\x02\xcc\x01"Y/v1/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*Zl"g/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*\x12\xef\x02\n\x16BatchVerifyTargetSites\x12>.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesRequest\x1a\x1d.google.longrunning.Operation"\xf5\x01\xcaA\x80\x01\n>google.cloud.discoveryengine.v1.BatchVerifyTargetSitesResponse\x12>google.cloud.discoveryengine.v1.BatchVerifyTargetSitesMetadata\x82\xd3\xe4\x93\x02k"f/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:batchVerifyTargetSites:\x01*\x12\xb2\x02\n\x1dFetchDomainVerificationStatus\x12E.google.cloud.discoveryengine.v1.FetchDomainVerificationStatusRequest\x1aF.google.cloud.discoveryengine.v1.FetchDomainVerificationStatusResponse"\x81\x01\x82\xd3\xe4\x93\x02{\x12y/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:fetchDomainVerificationStatus\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8f\x02\n#com.google.cloud.discoveryengine.v1B\x1cSiteSearchEngineServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.site_search_engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x1cSiteSearchEngineServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_GETSITESEARCHENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSITESEARCHENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_CREATETARGETSITEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETARGETSITEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_CREATETARGETSITEREQUEST'].fields_by_name['target_site']._loaded_options = None
    _globals['_CREATETARGETSITEREQUEST'].fields_by_name['target_site']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATETARGETSITESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATETARGETSITESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_BATCHCREATETARGETSITESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATETARGETSITESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_GETTARGETSITEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTARGETSITEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/TargetSite'
    _globals['_UPDATETARGETSITEREQUEST'].fields_by_name['target_site']._loaded_options = None
    _globals['_UPDATETARGETSITEREQUEST'].fields_by_name['target_site']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETARGETSITEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETARGETSITEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/TargetSite'
    _globals['_LISTTARGETSITESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTARGETSITESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_ENABLEADVANCEDSITESEARCHREQUEST'].fields_by_name['site_search_engine']._loaded_options = None
    _globals['_ENABLEADVANCEDSITESEARCHREQUEST'].fields_by_name['site_search_engine']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_DISABLEADVANCEDSITESEARCHREQUEST'].fields_by_name['site_search_engine']._loaded_options = None
    _globals['_DISABLEADVANCEDSITESEARCHREQUEST'].fields_by_name['site_search_engine']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_RECRAWLURISREQUEST'].fields_by_name['site_search_engine']._loaded_options = None
    _globals['_RECRAWLURISREQUEST'].fields_by_name['site_search_engine']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_RECRAWLURISREQUEST'].fields_by_name['uris']._loaded_options = None
    _globals['_RECRAWLURISREQUEST'].fields_by_name['uris']._serialized_options = b'\xe0A\x02'
    _globals['_RECRAWLURISREQUEST'].fields_by_name['site_credential']._loaded_options = None
    _globals['_RECRAWLURISREQUEST'].fields_by_name['site_credential']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHVERIFYTARGETSITESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHVERIFYTARGETSITESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_FETCHDOMAINVERIFICATIONSTATUSREQUEST'].fields_by_name['site_search_engine']._loaded_options = None
    _globals['_FETCHDOMAINVERIFICATIONSTATUSREQUEST'].fields_by_name['site_search_engine']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_SITESEARCHENGINESERVICE']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetSiteSearchEngine']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetSiteSearchEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01\x12?/v1/{name=projects/*/locations/*/dataStores/*/siteSearchEngine}ZO\x12M/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['CreateTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['CreateTargetSite']._serialized_options = b'\xcaAf\n*google.cloud.discoveryengine.v1.TargetSite\x128google.cloud.discoveryengine.v1.CreateTargetSiteMetadata\xdaA\x12parent,target_site\x82\xd3\xe4\x93\x02\xc8\x01"M/v1/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_siteZj"[/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_site'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchCreateTargetSites']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchCreateTargetSites']._serialized_options = b'\xcaA\x7f\n>google.cloud.discoveryengine.v1.BatchCreateTargetSitesResponse\x12=google.cloud.discoveryengine.v1.BatchCreateTargetSiteMetadata\x82\xd3\xe4\x93\x02\xcc\x01"Y/v1/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*Zl"g/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetTargetSite']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xae\x01\x12M/v1/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Z]\x12[/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['UpdateTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['UpdateTargetSite']._serialized_options = b'\xcaAf\n*google.cloud.discoveryengine.v1.TargetSite\x128google.cloud.discoveryengine.v1.UpdateTargetSiteMetadata\xdaA\x0btarget_site\x82\xd3\xe4\x93\x02\xe0\x012Y/v1/{target_site.name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_siteZv2g/v1/{target_site.name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_site'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DeleteTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DeleteTargetSite']._serialized_options = b'\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1.DeleteTargetSiteMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xae\x01*M/v1/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Z]*[/v1/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['ListTargetSites']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['ListTargetSites']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xae\x01\x12M/v1/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSitesZ]\x12[/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['EnableAdvancedSiteSearch']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['EnableAdvancedSiteSearch']._serialized_options = b'\xcaA\x84\x01\n@google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchResponse\x12@google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xe6\x01"f/v1/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*Zy"t/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DisableAdvancedSiteSearch']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DisableAdvancedSiteSearch']._serialized_options = b'\xcaA\x86\x01\nAgoogle.cloud.discoveryengine.v1.DisableAdvancedSiteSearchResponse\x12Agoogle.cloud.discoveryengine.v1.DisableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xe8\x01"g/v1/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*Zz"u/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['RecrawlUris']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['RecrawlUris']._serialized_options = b'\xcaAj\n3google.cloud.discoveryengine.v1.RecrawlUrisResponse\x123google.cloud.discoveryengine.v1.RecrawlUrisMetadata\x82\xd3\xe4\x93\x02\xcc\x01"Y/v1/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*Zl"g/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchVerifyTargetSites']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchVerifyTargetSites']._serialized_options = b'\xcaA\x80\x01\n>google.cloud.discoveryengine.v1.BatchVerifyTargetSitesResponse\x12>google.cloud.discoveryengine.v1.BatchVerifyTargetSitesMetadata\x82\xd3\xe4\x93\x02k"f/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:batchVerifyTargetSites:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['FetchDomainVerificationStatus']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['FetchDomainVerificationStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02{\x12y/v1/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:fetchDomainVerificationStatus'
    _globals['_GETSITESEARCHENGINEREQUEST']._serialized_start = 373
    _globals['_GETSITESEARCHENGINEREQUEST']._serialized_end = 472
    _globals['_CREATETARGETSITEREQUEST']._serialized_start = 475
    _globals['_CREATETARGETSITEREQUEST']._serialized_end = 644
    _globals['_CREATETARGETSITEMETADATA']._serialized_start = 646
    _globals['_CREATETARGETSITEMETADATA']._serialized_end = 770
    _globals['_BATCHCREATETARGETSITESREQUEST']._serialized_start = 773
    _globals['_BATCHCREATETARGETSITESREQUEST']._serialized_end = 958
    _globals['_GETTARGETSITEREQUEST']._serialized_start = 960
    _globals['_GETTARGETSITEREQUEST']._serialized_end = 1047
    _globals['_UPDATETARGETSITEREQUEST']._serialized_start = 1049
    _globals['_UPDATETARGETSITEREQUEST']._serialized_end = 1145
    _globals['_UPDATETARGETSITEMETADATA']._serialized_start = 1147
    _globals['_UPDATETARGETSITEMETADATA']._serialized_end = 1271
    _globals['_DELETETARGETSITEREQUEST']._serialized_start = 1273
    _globals['_DELETETARGETSITEREQUEST']._serialized_end = 1363
    _globals['_DELETETARGETSITEMETADATA']._serialized_start = 1365
    _globals['_DELETETARGETSITEMETADATA']._serialized_end = 1489
    _globals['_LISTTARGETSITESREQUEST']._serialized_start = 1492
    _globals['_LISTTARGETSITESREQUEST']._serialized_end = 1628
    _globals['_LISTTARGETSITESRESPONSE']._serialized_start = 1631
    _globals['_LISTTARGETSITESRESPONSE']._serialized_end = 1768
    _globals['_BATCHCREATETARGETSITEMETADATA']._serialized_start = 1771
    _globals['_BATCHCREATETARGETSITEMETADATA']._serialized_end = 1900
    _globals['_BATCHCREATETARGETSITESRESPONSE']._serialized_start = 1902
    _globals['_BATCHCREATETARGETSITESRESPONSE']._serialized_end = 2001
    _globals['_ENABLEADVANCEDSITESEARCHREQUEST']._serialized_start = 2003
    _globals['_ENABLEADVANCEDSITESEARCHREQUEST']._serialized_end = 2121
    _globals['_ENABLEADVANCEDSITESEARCHRESPONSE']._serialized_start = 2123
    _globals['_ENABLEADVANCEDSITESEARCHRESPONSE']._serialized_end = 2157
    _globals['_ENABLEADVANCEDSITESEARCHMETADATA']._serialized_start = 2160
    _globals['_ENABLEADVANCEDSITESEARCHMETADATA']._serialized_end = 2292
    _globals['_DISABLEADVANCEDSITESEARCHREQUEST']._serialized_start = 2294
    _globals['_DISABLEADVANCEDSITESEARCHREQUEST']._serialized_end = 2413
    _globals['_DISABLEADVANCEDSITESEARCHRESPONSE']._serialized_start = 2415
    _globals['_DISABLEADVANCEDSITESEARCHRESPONSE']._serialized_end = 2450
    _globals['_DISABLEADVANCEDSITESEARCHMETADATA']._serialized_start = 2453
    _globals['_DISABLEADVANCEDSITESEARCHMETADATA']._serialized_end = 2586
    _globals['_RECRAWLURISREQUEST']._serialized_start = 2589
    _globals['_RECRAWLURISREQUEST']._serialized_end = 2743
    _globals['_RECRAWLURISRESPONSE']._serialized_start = 2746
    _globals['_RECRAWLURISRESPONSE']._serialized_end = 3234
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO']._serialized_start = 2882
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO']._serialized_end = 3234
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON']._serialized_start = 3016
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON']._serialized_end = 3234
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON_CORPUSTYPE']._serialized_start = 3168
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON_CORPUSTYPE']._serialized_end = 3234
    _globals['_RECRAWLURISMETADATA']._serialized_start = 3237
    _globals['_RECRAWLURISMETADATA']._serialized_end = 3480
    _globals['_BATCHVERIFYTARGETSITESREQUEST']._serialized_start = 3482
    _globals['_BATCHVERIFYTARGETSITESREQUEST']._serialized_end = 3586
    _globals['_BATCHVERIFYTARGETSITESRESPONSE']._serialized_start = 3588
    _globals['_BATCHVERIFYTARGETSITESRESPONSE']._serialized_end = 3620
    _globals['_BATCHVERIFYTARGETSITESMETADATA']._serialized_start = 3623
    _globals['_BATCHVERIFYTARGETSITESMETADATA']._serialized_end = 3753
    _globals['_FETCHDOMAINVERIFICATIONSTATUSREQUEST']._serialized_start = 3756
    _globals['_FETCHDOMAINVERIFICATIONSTATUSREQUEST']._serialized_end = 3918
    _globals['_FETCHDOMAINVERIFICATIONSTATUSRESPONSE']._serialized_start = 3921
    _globals['_FETCHDOMAINVERIFICATIONSTATUSRESPONSE']._serialized_end = 4072
    _globals['_SITESEARCHENGINESERVICE']._serialized_start = 4075
    _globals['_SITESEARCHENGINESERVICE']._serialized_end = 8992