"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/site_search_engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import site_search_engine_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_site__search__engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/discoveryengine/v1beta/site_search_engine_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/discoveryengine/v1beta/site_search_engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"c\n\x1aGetSiteSearchEngineRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine"\xad\x01\n\x17CreateTargetSiteRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12I\n\x0btarget_site\x18\x02 \x01(\x0b2/.google.cloud.discoveryengine.v1beta.TargetSiteB\x03\xe0A\x02"|\n\x18CreateTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xbd\x01\n\x1dBatchCreateTargetSitesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12S\n\x08requests\x18\x02 \x03(\x0b2<.google.cloud.discoveryengine.v1beta.CreateTargetSiteRequestB\x03\xe0A\x02"W\n\x14GetTargetSiteRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/TargetSite"d\n\x17UpdateTargetSiteRequest\x12I\n\x0btarget_site\x18\x01 \x01(\x0b2/.google.cloud.discoveryengine.v1beta.TargetSiteB\x03\xe0A\x02"|\n\x18UpdateTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"Z\n\x17DeleteTargetSiteRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/TargetSite"|\n\x18DeleteTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x88\x01\n\x16ListTargetSitesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8d\x01\n\x17ListTargetSitesResponse\x12E\n\x0ctarget_sites\x18\x01 \x03(\x0b2/.google.cloud.discoveryengine.v1beta.TargetSite\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x81\x01\n\x1dBatchCreateTargetSiteMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"g\n\x1eBatchCreateTargetSitesResponse\x12E\n\x0ctarget_sites\x18\x01 \x03(\x0b2/.google.cloud.discoveryengine.v1beta.TargetSite"\xa3\x01\n\x14CreateSitemapRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12B\n\x07sitemap\x18\x02 \x01(\x0b2,.google.cloud.discoveryengine.v1beta.SitemapB\x03\xe0A\x02"T\n\x14DeleteSitemapRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Sitemap"\xca\x02\n\x14FetchSitemapsRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12W\n\x07matcher\x18\x02 \x01(\x0b2A.google.cloud.discoveryengine.v1beta.FetchSitemapsRequest.MatcherB\x03\xe0A\x01\x1a\x1b\n\x0bUrisMatcher\x12\x0c\n\x04uris\x18\x01 \x03(\t\x1as\n\x07Matcher\x12]\n\x0curis_matcher\x18\x01 \x01(\x0b2E.google.cloud.discoveryengine.v1beta.FetchSitemapsRequest.UrisMatcherH\x00B\t\n\x07matcher"y\n\x15CreateSitemapMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"y\n\x15DeleteSitemapMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xd0\x01\n\x15FetchSitemapsResponse\x12e\n\x11sitemaps_metadata\x18\x01 \x03(\x0b2J.google.cloud.discoveryengine.v1beta.FetchSitemapsResponse.SitemapMetadata\x1aP\n\x0fSitemapMetadata\x12=\n\x07sitemap\x18\x01 \x01(\x0b2,.google.cloud.discoveryengine.v1beta.Sitemap"v\n\x1fEnableAdvancedSiteSearchRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine""\n EnableAdvancedSiteSearchResponse"\x84\x01\n EnableAdvancedSiteSearchMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"w\n DisableAdvancedSiteSearchRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine"#\n!DisableAdvancedSiteSearchResponse"\x85\x01\n!DisableAdvancedSiteSearchMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x9a\x01\n\x12RecrawlUrisRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12\x11\n\x04uris\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x1c\n\x0fsite_credential\x18\x05 \x01(\tB\x03\xe0A\x01"\xf4\x03\n\x13RecrawlUrisResponse\x12]\n\x0ffailure_samples\x18\x01 \x03(\x0b2D.google.cloud.discoveryengine.v1beta.RecrawlUrisResponse.FailureInfo\x12\x13\n\x0bfailed_uris\x18\x02 \x03(\t\x1a\xe8\x02\n\x0bFailureInfo\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12k\n\x0ffailure_reasons\x18\x02 \x03(\x0b2R.google.cloud.discoveryengine.v1beta.RecrawlUrisResponse.FailureInfo.FailureReason\x1a\xde\x01\n\rFailureReason\x12r\n\x0bcorpus_type\x18\x01 \x01(\x0e2].google.cloud.discoveryengine.v1beta.RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType\x12\x15\n\rerror_message\x18\x02 \x01(\t"B\n\nCorpusType\x12\x1b\n\x17CORPUS_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DESKTOP\x10\x01\x12\n\n\x06MOBILE\x10\x02"\xe5\x02\n\x13RecrawlUrisMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0cinvalid_uris\x18\x03 \x03(\t\x12\x1a\n\x12invalid_uris_count\x18\x08 \x01(\x05\x12&\n\x1euris_not_matching_target_sites\x18\t \x03(\t\x12,\n$uris_not_matching_target_sites_count\x18\n \x01(\x05\x12\x18\n\x10valid_uris_count\x18\x04 \x01(\x05\x12\x15\n\rsuccess_count\x18\x05 \x01(\x05\x12\x15\n\rpending_count\x18\x06 \x01(\x05\x12\x1c\n\x14quota_exceeded_count\x18\x07 \x01(\x05"h\n\x1dBatchVerifyTargetSitesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine" \n\x1eBatchVerifyTargetSitesResponse"\x82\x01\n\x1eBatchVerifyTargetSitesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa2\x01\n$FetchDomainVerificationStatusRequest\x12S\n\x12site_search_engine\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x9b\x01\n%FetchDomainVerificationStatusResponse\x12E\n\x0ctarget_sites\x18\x01 \x03(\x0b2/.google.cloud.discoveryengine.v1beta.TargetSite\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xb00\n\x17SiteSearchEngineService\x12\xb8\x02\n\x13GetSiteSearchEngine\x12?.google.cloud.discoveryengine.v1beta.GetSiteSearchEngineRequest\x1a5.google.cloud.discoveryengine.v1beta.SiteSearchEngine"\xa8\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9a\x01\x12C/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine}ZS\x12Q/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}\x12\xcf\x03\n\x10CreateTargetSite\x12<.google.cloud.discoveryengine.v1beta.CreateTargetSiteRequest\x1a\x1d.google.longrunning.Operation"\xdd\x02\xcaAn\n.google.cloud.discoveryengine.v1beta.TargetSite\x12<google.cloud.discoveryengine.v1beta.CreateTargetSiteMetadata\xdaA\x12parent,target_site\x82\xd3\xe4\x93\x02\xd0\x01"Q/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_siteZn"_/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_site\x12\xe4\x03\n\x16BatchCreateTargetSites\x12B.google.cloud.discoveryengine.v1beta.BatchCreateTargetSitesRequest\x1a\x1d.google.longrunning.Operation"\xe6\x02\xcaA\x87\x01\nBgoogle.cloud.discoveryengine.v1beta.BatchCreateTargetSitesResponse\x12Agoogle.cloud.discoveryengine.v1beta.BatchCreateTargetSiteMetadata\x82\xd3\xe4\x93\x02\xd4\x01"]/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*Zp"k/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*\x12\xc2\x02\n\rGetTargetSite\x129.google.cloud.discoveryengine.v1beta.GetTargetSiteRequest\x1a/.google.cloud.discoveryengine.v1beta.TargetSite"\xc4\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xb6\x01\x12Q/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Za\x12_/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}\x12\xe0\x03\n\x10UpdateTargetSite\x12<.google.cloud.discoveryengine.v1beta.UpdateTargetSiteRequest\x1a\x1d.google.longrunning.Operation"\xee\x02\xcaAn\n.google.cloud.discoveryengine.v1beta.TargetSite\x12<google.cloud.discoveryengine.v1beta.UpdateTargetSiteMetadata\xdaA\x0btarget_site\x82\xd3\xe4\x93\x02\xe8\x012]/v1beta/{target_site.name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_siteZz2k/v1beta/{target_site.name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_site\x12\x8e\x03\n\x10DeleteTargetSite\x12<.google.cloud.discoveryengine.v1beta.DeleteTargetSiteRequest\x1a\x1d.google.longrunning.Operation"\x9c\x02\xcaAU\n\x15google.protobuf.Empty\x12<google.cloud.discoveryengine.v1beta.DeleteTargetSiteMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb6\x01*Q/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Za*_/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}\x12\xd5\x02\n\x0fListTargetSites\x12;.google.cloud.discoveryengine.v1beta.ListTargetSitesRequest\x1a<.google.cloud.discoveryengine.v1beta.ListTargetSitesResponse"\xc6\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb6\x01\x12Q/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSitesZa\x12_/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites\x12\xb1\x03\n\rCreateSitemap\x129.google.cloud.discoveryengine.v1beta.CreateSitemapRequest\x1a\x1d.google.longrunning.Operation"\xc5\x02\xcaAh\n+google.cloud.discoveryengine.v1beta.Sitemap\x129google.cloud.discoveryengine.v1beta.CreateSitemapMetadata\xdaA\x0eparent,sitemap\x82\xd3\xe4\x93\x02\xc2\x01"N/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/sitemaps:\x07sitemapZg"\\/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/sitemaps:\x07sitemap\x12\xff\x02\n\rDeleteSitemap\x129.google.cloud.discoveryengine.v1beta.DeleteSitemapRequest\x1a\x1d.google.longrunning.Operation"\x93\x02\xcaAR\n\x15google.protobuf.Empty\x129google.cloud.discoveryengine.v1beta.DeleteSitemapMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb0\x01*N/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/sitemaps/*}Z^*\\/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/sitemaps/*}\x12\xed\x01\n\rFetchSitemaps\x129.google.cloud.discoveryengine.v1beta.FetchSitemapsRequest\x1a:.google.cloud.discoveryengine.v1beta.FetchSitemapsResponse"e\xdaA\x06parent\x82\xd3\xe4\x93\x02V\x12T/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/sitemaps:fetch\x12\x87\x04\n\x18EnableAdvancedSiteSearch\x12D.google.cloud.discoveryengine.v1beta.EnableAdvancedSiteSearchRequest\x1a\x1d.google.longrunning.Operation"\x85\x03\xcaA\x8c\x01\nDgoogle.cloud.discoveryengine.v1beta.EnableAdvancedSiteSearchResponse\x12Dgoogle.cloud.discoveryengine.v1beta.EnableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xee\x01"j/v1beta/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*Z}"x/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*\x12\x8d\x04\n\x19DisableAdvancedSiteSearch\x12E.google.cloud.discoveryengine.v1beta.DisableAdvancedSiteSearchRequest\x1a\x1d.google.longrunning.Operation"\x89\x03\xcaA\x8e\x01\nEgoogle.cloud.discoveryengine.v1beta.DisableAdvancedSiteSearchResponse\x12Egoogle.cloud.discoveryengine.v1beta.DisableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xf0\x01"k/v1beta/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*Z~"y/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*\x12\xb8\x03\n\x0bRecrawlUris\x127.google.cloud.discoveryengine.v1beta.RecrawlUrisRequest\x1a\x1d.google.longrunning.Operation"\xd0\x02\xcaAr\n7google.cloud.discoveryengine.v1beta.RecrawlUrisResponse\x127google.cloud.discoveryengine.v1beta.RecrawlUrisMetadata\x82\xd3\xe4\x93\x02\xd4\x01"]/v1beta/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*Zp"k/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*\x12\xff\x02\n\x16BatchVerifyTargetSites\x12B.google.cloud.discoveryengine.v1beta.BatchVerifyTargetSitesRequest\x1a\x1d.google.longrunning.Operation"\x81\x02\xcaA\x88\x01\nBgoogle.cloud.discoveryengine.v1beta.BatchVerifyTargetSitesResponse\x12Bgoogle.cloud.discoveryengine.v1beta.BatchVerifyTargetSitesMetadata\x82\xd3\xe4\x93\x02o"j/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:batchVerifyTargetSites:\x01*\x12\xbe\x02\n\x1dFetchDomainVerificationStatus\x12I.google.cloud.discoveryengine.v1beta.FetchDomainVerificationStatusRequest\x1aJ.google.cloud.discoveryengine.v1beta.FetchDomainVerificationStatusResponse"\x85\x01\x82\xd3\xe4\x93\x02\x7f\x12}/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:fetchDomainVerificationStatus\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa3\x02\n\'com.google.cloud.discoveryengine.v1betaB\x1cSiteSearchEngineServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.site_search_engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x1cSiteSearchEngineServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_CREATESITEMAPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESITEMAPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_CREATESITEMAPREQUEST'].fields_by_name['sitemap']._loaded_options = None
    _globals['_CREATESITEMAPREQUEST'].fields_by_name['sitemap']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESITEMAPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESITEMAPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Sitemap'
    _globals['_FETCHSITEMAPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_FETCHSITEMAPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/discoveryengine.googleapis.com/SiteSearchEngine'
    _globals['_FETCHSITEMAPSREQUEST'].fields_by_name['matcher']._loaded_options = None
    _globals['_FETCHSITEMAPSREQUEST'].fields_by_name['matcher']._serialized_options = b'\xe0A\x01'
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
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetSiteSearchEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9a\x01\x12C/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine}ZS\x12Q/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['CreateTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['CreateTargetSite']._serialized_options = b'\xcaAn\n.google.cloud.discoveryengine.v1beta.TargetSite\x12<google.cloud.discoveryengine.v1beta.CreateTargetSiteMetadata\xdaA\x12parent,target_site\x82\xd3\xe4\x93\x02\xd0\x01"Q/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_siteZn"_/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:\x0btarget_site'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchCreateTargetSites']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchCreateTargetSites']._serialized_options = b'\xcaA\x87\x01\nBgoogle.cloud.discoveryengine.v1beta.BatchCreateTargetSitesResponse\x12Agoogle.cloud.discoveryengine.v1beta.BatchCreateTargetSiteMetadata\x82\xd3\xe4\x93\x02\xd4\x01"]/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*Zp"k/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites:batchCreate:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['GetTargetSite']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xb6\x01\x12Q/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Za\x12_/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['UpdateTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['UpdateTargetSite']._serialized_options = b'\xcaAn\n.google.cloud.discoveryengine.v1beta.TargetSite\x12<google.cloud.discoveryengine.v1beta.UpdateTargetSiteMetadata\xdaA\x0btarget_site\x82\xd3\xe4\x93\x02\xe8\x012]/v1beta/{target_site.name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_siteZz2k/v1beta/{target_site.name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}:\x0btarget_site'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DeleteTargetSite']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DeleteTargetSite']._serialized_options = b'\xcaAU\n\x15google.protobuf.Empty\x12<google.cloud.discoveryengine.v1beta.DeleteTargetSiteMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb6\x01*Q/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/targetSites/*}Za*_/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/targetSites/*}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['ListTargetSites']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['ListTargetSites']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb6\x01\x12Q/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/targetSitesZa\x12_/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/targetSites'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['CreateSitemap']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['CreateSitemap']._serialized_options = b'\xcaAh\n+google.cloud.discoveryengine.v1beta.Sitemap\x129google.cloud.discoveryengine.v1beta.CreateSitemapMetadata\xdaA\x0eparent,sitemap\x82\xd3\xe4\x93\x02\xc2\x01"N/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/sitemaps:\x07sitemapZg"\\/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}/sitemaps:\x07sitemap'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DeleteSitemap']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DeleteSitemap']._serialized_options = b'\xcaAR\n\x15google.protobuf.Empty\x129google.cloud.discoveryengine.v1beta.DeleteSitemapMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb0\x01*N/v1beta/{name=projects/*/locations/*/dataStores/*/siteSearchEngine/sitemaps/*}Z^*\\/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine/sitemaps/*}'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['FetchSitemaps']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['FetchSitemaps']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02V\x12T/v1beta/{parent=projects/*/locations/*/dataStores/*/siteSearchEngine}/sitemaps:fetch'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['EnableAdvancedSiteSearch']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['EnableAdvancedSiteSearch']._serialized_options = b'\xcaA\x8c\x01\nDgoogle.cloud.discoveryengine.v1beta.EnableAdvancedSiteSearchResponse\x12Dgoogle.cloud.discoveryengine.v1beta.EnableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xee\x01"j/v1beta/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*Z}"x/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:enableAdvancedSiteSearch:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DisableAdvancedSiteSearch']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['DisableAdvancedSiteSearch']._serialized_options = b'\xcaA\x8e\x01\nEgoogle.cloud.discoveryengine.v1beta.DisableAdvancedSiteSearchResponse\x12Egoogle.cloud.discoveryengine.v1beta.DisableAdvancedSiteSearchMetadata\x82\xd3\xe4\x93\x02\xf0\x01"k/v1beta/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*Z~"y/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:disableAdvancedSiteSearch:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['RecrawlUris']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['RecrawlUris']._serialized_options = b'\xcaAr\n7google.cloud.discoveryengine.v1beta.RecrawlUrisResponse\x127google.cloud.discoveryengine.v1beta.RecrawlUrisMetadata\x82\xd3\xe4\x93\x02\xd4\x01"]/v1beta/{site_search_engine=projects/*/locations/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*Zp"k/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:recrawlUris:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchVerifyTargetSites']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['BatchVerifyTargetSites']._serialized_options = b'\xcaA\x88\x01\nBgoogle.cloud.discoveryengine.v1beta.BatchVerifyTargetSitesResponse\x12Bgoogle.cloud.discoveryengine.v1beta.BatchVerifyTargetSitesMetadata\x82\xd3\xe4\x93\x02o"j/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:batchVerifyTargetSites:\x01*'
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['FetchDomainVerificationStatus']._loaded_options = None
    _globals['_SITESEARCHENGINESERVICE'].methods_by_name['FetchDomainVerificationStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x7f\x12}/v1beta/{site_search_engine=projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine}:fetchDomainVerificationStatus'
    _globals['_GETSITESEARCHENGINEREQUEST']._serialized_start = 385
    _globals['_GETSITESEARCHENGINEREQUEST']._serialized_end = 484
    _globals['_CREATETARGETSITEREQUEST']._serialized_start = 487
    _globals['_CREATETARGETSITEREQUEST']._serialized_end = 660
    _globals['_CREATETARGETSITEMETADATA']._serialized_start = 662
    _globals['_CREATETARGETSITEMETADATA']._serialized_end = 786
    _globals['_BATCHCREATETARGETSITESREQUEST']._serialized_start = 789
    _globals['_BATCHCREATETARGETSITESREQUEST']._serialized_end = 978
    _globals['_GETTARGETSITEREQUEST']._serialized_start = 980
    _globals['_GETTARGETSITEREQUEST']._serialized_end = 1067
    _globals['_UPDATETARGETSITEREQUEST']._serialized_start = 1069
    _globals['_UPDATETARGETSITEREQUEST']._serialized_end = 1169
    _globals['_UPDATETARGETSITEMETADATA']._serialized_start = 1171
    _globals['_UPDATETARGETSITEMETADATA']._serialized_end = 1295
    _globals['_DELETETARGETSITEREQUEST']._serialized_start = 1297
    _globals['_DELETETARGETSITEREQUEST']._serialized_end = 1387
    _globals['_DELETETARGETSITEMETADATA']._serialized_start = 1389
    _globals['_DELETETARGETSITEMETADATA']._serialized_end = 1513
    _globals['_LISTTARGETSITESREQUEST']._serialized_start = 1516
    _globals['_LISTTARGETSITESREQUEST']._serialized_end = 1652
    _globals['_LISTTARGETSITESRESPONSE']._serialized_start = 1655
    _globals['_LISTTARGETSITESRESPONSE']._serialized_end = 1796
    _globals['_BATCHCREATETARGETSITEMETADATA']._serialized_start = 1799
    _globals['_BATCHCREATETARGETSITEMETADATA']._serialized_end = 1928
    _globals['_BATCHCREATETARGETSITESRESPONSE']._serialized_start = 1930
    _globals['_BATCHCREATETARGETSITESRESPONSE']._serialized_end = 2033
    _globals['_CREATESITEMAPREQUEST']._serialized_start = 2036
    _globals['_CREATESITEMAPREQUEST']._serialized_end = 2199
    _globals['_DELETESITEMAPREQUEST']._serialized_start = 2201
    _globals['_DELETESITEMAPREQUEST']._serialized_end = 2285
    _globals['_FETCHSITEMAPSREQUEST']._serialized_start = 2288
    _globals['_FETCHSITEMAPSREQUEST']._serialized_end = 2618
    _globals['_FETCHSITEMAPSREQUEST_URISMATCHER']._serialized_start = 2474
    _globals['_FETCHSITEMAPSREQUEST_URISMATCHER']._serialized_end = 2501
    _globals['_FETCHSITEMAPSREQUEST_MATCHER']._serialized_start = 2503
    _globals['_FETCHSITEMAPSREQUEST_MATCHER']._serialized_end = 2618
    _globals['_CREATESITEMAPMETADATA']._serialized_start = 2620
    _globals['_CREATESITEMAPMETADATA']._serialized_end = 2741
    _globals['_DELETESITEMAPMETADATA']._serialized_start = 2743
    _globals['_DELETESITEMAPMETADATA']._serialized_end = 2864
    _globals['_FETCHSITEMAPSRESPONSE']._serialized_start = 2867
    _globals['_FETCHSITEMAPSRESPONSE']._serialized_end = 3075
    _globals['_FETCHSITEMAPSRESPONSE_SITEMAPMETADATA']._serialized_start = 2995
    _globals['_FETCHSITEMAPSRESPONSE_SITEMAPMETADATA']._serialized_end = 3075
    _globals['_ENABLEADVANCEDSITESEARCHREQUEST']._serialized_start = 3077
    _globals['_ENABLEADVANCEDSITESEARCHREQUEST']._serialized_end = 3195
    _globals['_ENABLEADVANCEDSITESEARCHRESPONSE']._serialized_start = 3197
    _globals['_ENABLEADVANCEDSITESEARCHRESPONSE']._serialized_end = 3231
    _globals['_ENABLEADVANCEDSITESEARCHMETADATA']._serialized_start = 3234
    _globals['_ENABLEADVANCEDSITESEARCHMETADATA']._serialized_end = 3366
    _globals['_DISABLEADVANCEDSITESEARCHREQUEST']._serialized_start = 3368
    _globals['_DISABLEADVANCEDSITESEARCHREQUEST']._serialized_end = 3487
    _globals['_DISABLEADVANCEDSITESEARCHRESPONSE']._serialized_start = 3489
    _globals['_DISABLEADVANCEDSITESEARCHRESPONSE']._serialized_end = 3524
    _globals['_DISABLEADVANCEDSITESEARCHMETADATA']._serialized_start = 3527
    _globals['_DISABLEADVANCEDSITESEARCHMETADATA']._serialized_end = 3660
    _globals['_RECRAWLURISREQUEST']._serialized_start = 3663
    _globals['_RECRAWLURISREQUEST']._serialized_end = 3817
    _globals['_RECRAWLURISRESPONSE']._serialized_start = 3820
    _globals['_RECRAWLURISRESPONSE']._serialized_end = 4320
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO']._serialized_start = 3960
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO']._serialized_end = 4320
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON']._serialized_start = 4098
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON']._serialized_end = 4320
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON_CORPUSTYPE']._serialized_start = 4254
    _globals['_RECRAWLURISRESPONSE_FAILUREINFO_FAILUREREASON_CORPUSTYPE']._serialized_end = 4320
    _globals['_RECRAWLURISMETADATA']._serialized_start = 4323
    _globals['_RECRAWLURISMETADATA']._serialized_end = 4680
    _globals['_BATCHVERIFYTARGETSITESREQUEST']._serialized_start = 4682
    _globals['_BATCHVERIFYTARGETSITESREQUEST']._serialized_end = 4786
    _globals['_BATCHVERIFYTARGETSITESRESPONSE']._serialized_start = 4788
    _globals['_BATCHVERIFYTARGETSITESRESPONSE']._serialized_end = 4820
    _globals['_BATCHVERIFYTARGETSITESMETADATA']._serialized_start = 4823
    _globals['_BATCHVERIFYTARGETSITESMETADATA']._serialized_end = 4953
    _globals['_FETCHDOMAINVERIFICATIONSTATUSREQUEST']._serialized_start = 4956
    _globals['_FETCHDOMAINVERIFICATIONSTATUSREQUEST']._serialized_end = 5118
    _globals['_FETCHDOMAINVERIFICATIONSTATUSRESPONSE']._serialized_start = 5121
    _globals['_FETCHDOMAINVERIFICATIONSTATUSRESPONSE']._serialized_end = 5276
    _globals['_SITESEARCHENGINESERVICE']._serialized_start = 5279
    _globals['_SITESEARCHENGINESERVICE']._serialized_end = 11471