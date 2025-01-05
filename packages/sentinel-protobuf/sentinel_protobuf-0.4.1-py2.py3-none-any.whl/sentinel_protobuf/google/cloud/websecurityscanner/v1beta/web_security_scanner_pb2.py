"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1beta/web_security_scanner.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1beta import crawled_url_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_crawled__url__pb2
from .....google.cloud.websecurityscanner.v1beta import finding_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_finding__pb2
from .....google.cloud.websecurityscanner.v1beta import finding_type_stats_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_finding__type__stats__pb2
from .....google.cloud.websecurityscanner.v1beta import scan_config_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__config__pb2
from .....google.cloud.websecurityscanner.v1beta import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/websecurityscanner/v1beta/web_security_scanner.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/websecurityscanner/v1beta/crawled_url.proto\x1a4google/cloud/websecurityscanner/v1beta/finding.proto\x1a?google/cloud/websecurityscanner/v1beta/finding_type_stats.proto\x1a8google/cloud/websecurityscanner/v1beta/scan_config.proto\x1a5google/cloud/websecurityscanner/v1beta/scan_run.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xac\x01\n\x17CreateScanConfigRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12L\n\x0bscan_config\x18\x02 \x01(\x0b22.google.cloud.websecurityscanner.v1beta.ScanConfigB\x03\xe0A\x02"]\n\x17DeleteScanConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig"Z\n\x14GetScanConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig"\x84\x01\n\x16ListScanConfigsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\x9d\x01\n\x17UpdateScanConfigRequest\x12L\n\x0bscan_config\x18\x02 \x01(\x0b22.google.cloud.websecurityscanner.v1beta.ScanConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"|\n\x17ListScanConfigsResponse\x12H\n\x0cscan_configs\x18\x01 \x03(\x0b22.google.cloud.websecurityscanner.v1beta.ScanConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Y\n\x13StartScanRunRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig"T\n\x11GetScanRunRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun"\x82\x01\n\x13ListScanRunsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"s\n\x14ListScanRunsResponse\x12B\n\tscan_runs\x18\x01 \x03(\x0b2/.google.cloud.websecurityscanner.v1beta.ScanRun\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x12StopScanRunRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun"\x82\x01\n\x16ListCrawledUrlsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"|\n\x17ListCrawledUrlsResponse\x12H\n\x0ccrawled_urls\x18\x01 \x03(\x0b22.google.cloud.websecurityscanner.v1beta.CrawledUrl\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x11GetFindingRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/Finding"\x94\x01\n\x13ListFindingsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"r\n\x14ListFindingsResponse\x12A\n\x08findings\x18\x01 \x03(\x0b2/.google.cloud.websecurityscanner.v1beta.Finding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x1bListFindingTypeStatsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun"t\n\x1cListFindingTypeStatsResponse\x12T\n\x12finding_type_stats\x18\x01 \x03(\x0b28.google.cloud.websecurityscanner.v1beta.FindingTypeStats2\x8e\x16\n\x12WebSecurityScanner\x12\xda\x01\n\x10CreateScanConfig\x12?.google.cloud.websecurityscanner.v1beta.CreateScanConfigRequest\x1a2.google.cloud.websecurityscanner.v1beta.ScanConfig"Q\xdaA\x12parent,scan_config\x82\xd3\xe4\x93\x026"\'/v1beta/{parent=projects/*}/scanConfigs:\x0bscan_config\x12\xa3\x01\n\x10DeleteScanConfig\x12?.google.cloud.websecurityscanner.v1beta.DeleteScanConfigRequest\x1a\x16.google.protobuf.Empty"6\xdaA\x04name\x82\xd3\xe4\x93\x02)*\'/v1beta/{name=projects/*/scanConfigs/*}\x12\xb9\x01\n\rGetScanConfig\x12<.google.cloud.websecurityscanner.v1beta.GetScanConfigRequest\x1a2.google.cloud.websecurityscanner.v1beta.ScanConfig"6\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12\'/v1beta/{name=projects/*/scanConfigs/*}\x12\xcc\x01\n\x0fListScanConfigs\x12>.google.cloud.websecurityscanner.v1beta.ListScanConfigsRequest\x1a?.google.cloud.websecurityscanner.v1beta.ListScanConfigsResponse"8\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12\'/v1beta/{parent=projects/*}/scanConfigs\x12\xeb\x01\n\x10UpdateScanConfig\x12?.google.cloud.websecurityscanner.v1beta.UpdateScanConfigRequest\x1a2.google.cloud.websecurityscanner.v1beta.ScanConfig"b\xdaA\x17scan_config,update_mask\x82\xd3\xe4\x93\x02B23/v1beta/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config\x12\xbd\x01\n\x0cStartScanRun\x12;.google.cloud.websecurityscanner.v1beta.StartScanRunRequest\x1a/.google.cloud.websecurityscanner.v1beta.ScanRun"?\xdaA\x04name\x82\xd3\xe4\x93\x022"-/v1beta/{name=projects/*/scanConfigs/*}:start:\x01*\x12\xbb\x01\n\nGetScanRun\x129.google.cloud.websecurityscanner.v1beta.GetScanRunRequest\x1a/.google.cloud.websecurityscanner.v1beta.ScanRun"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}\x12\xce\x01\n\x0cListScanRuns\x12;.google.cloud.websecurityscanner.v1beta.ListScanRunsRequest\x1a<.google.cloud.websecurityscanner.v1beta.ListScanRunsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta/{parent=projects/*/scanConfigs/*}/scanRuns\x12\xc5\x01\n\x0bStopScanRun\x12:.google.cloud.websecurityscanner.v1beta.StopScanRunRequest\x1a/.google.cloud.websecurityscanner.v1beta.ScanRun"I\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*\x12\xe5\x01\n\x0fListCrawledUrls\x12>.google.cloud.websecurityscanner.v1beta.ListCrawledUrlsRequest\x1a?.google.cloud.websecurityscanner.v1beta.ListCrawledUrlsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls\x12\xc6\x01\n\nGetFinding\x129.google.cloud.websecurityscanner.v1beta.GetFindingRequest\x1a/.google.cloud.websecurityscanner.v1beta.Finding"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}\x12\xe0\x01\n\x0cListFindings\x12;.google.cloud.websecurityscanner.v1beta.ListFindingsRequest\x1a<.google.cloud.websecurityscanner.v1beta.ListFindingsResponse"U\xdaA\rparent,filter\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings\x12\xf9\x01\n\x14ListFindingTypeStats\x12C.google.cloud.websecurityscanner.v1beta.ListFindingTypeStatsRequest\x1aD.google.cloud.websecurityscanner.v1beta.ListFindingTypeStatsResponse"V\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats\x1aU\xcaA!websecurityscanner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa1\x02\n*com.google.cloud.websecurityscanner.v1betaB\x17WebSecurityScannerProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1beta.web_security_scanner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\x17WebSecurityScannerProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1beta'
    _globals['_CREATESCANCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESCANCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATESCANCONFIGREQUEST'].fields_by_name['scan_config']._loaded_options = None
    _globals['_CREATESCANCONFIGREQUEST'].fields_by_name['scan_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESCANCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESCANCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig'
    _globals['_GETSCANCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSCANCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig'
    _globals['_LISTSCANCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSCANCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_UPDATESCANCONFIGREQUEST'].fields_by_name['scan_config']._loaded_options = None
    _globals['_UPDATESCANCONFIGREQUEST'].fields_by_name['scan_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESCANCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESCANCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_STARTSCANRUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTSCANRUNREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig'
    _globals['_GETSCANRUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSCANRUNREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun'
    _globals['_LISTSCANRUNSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSCANRUNSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig'
    _globals['_STOPSCANRUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPSCANRUNREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun'
    _globals['_LISTCRAWLEDURLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCRAWLEDURLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun'
    _globals['_GETFINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/Finding'
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun'
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_LISTFINDINGTYPESTATSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFINDINGTYPESTATSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun'
    _globals['_WEBSECURITYSCANNER']._loaded_options = None
    _globals['_WEBSECURITYSCANNER']._serialized_options = b'\xcaA!websecurityscanner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['CreateScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['CreateScanConfig']._serialized_options = b'\xdaA\x12parent,scan_config\x82\xd3\xe4\x93\x026"\'/v1beta/{parent=projects/*}/scanConfigs:\x0bscan_config'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['DeleteScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['DeleteScanConfig']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02)*'/v1beta/{name=projects/*/scanConfigs/*}"
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanConfig']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12'/v1beta/{name=projects/*/scanConfigs/*}"
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanConfigs']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanConfigs']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12'/v1beta/{parent=projects/*}/scanConfigs"
    _globals['_WEBSECURITYSCANNER'].methods_by_name['UpdateScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['UpdateScanConfig']._serialized_options = b'\xdaA\x17scan_config,update_mask\x82\xd3\xe4\x93\x02B23/v1beta/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StartScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StartScanRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022"-/v1beta/{name=projects/*/scanConfigs/*}:start:\x01*'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanRuns']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanRuns']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta/{parent=projects/*/scanConfigs/*}/scanRuns'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StopScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StopScanRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListCrawledUrls']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListCrawledUrls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetFinding']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetFinding']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindings']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindings']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindingTypeStats']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindingTypeStats']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats'
    _globals['_CREATESCANCONFIGREQUEST']._serialized_start = 578
    _globals['_CREATESCANCONFIGREQUEST']._serialized_end = 750
    _globals['_DELETESCANCONFIGREQUEST']._serialized_start = 752
    _globals['_DELETESCANCONFIGREQUEST']._serialized_end = 845
    _globals['_GETSCANCONFIGREQUEST']._serialized_start = 847
    _globals['_GETSCANCONFIGREQUEST']._serialized_end = 937
    _globals['_LISTSCANCONFIGSREQUEST']._serialized_start = 940
    _globals['_LISTSCANCONFIGSREQUEST']._serialized_end = 1072
    _globals['_UPDATESCANCONFIGREQUEST']._serialized_start = 1075
    _globals['_UPDATESCANCONFIGREQUEST']._serialized_end = 1232
    _globals['_LISTSCANCONFIGSRESPONSE']._serialized_start = 1234
    _globals['_LISTSCANCONFIGSRESPONSE']._serialized_end = 1358
    _globals['_STARTSCANRUNREQUEST']._serialized_start = 1360
    _globals['_STARTSCANRUNREQUEST']._serialized_end = 1449
    _globals['_GETSCANRUNREQUEST']._serialized_start = 1451
    _globals['_GETSCANRUNREQUEST']._serialized_end = 1535
    _globals['_LISTSCANRUNSREQUEST']._serialized_start = 1538
    _globals['_LISTSCANRUNSREQUEST']._serialized_end = 1668
    _globals['_LISTSCANRUNSRESPONSE']._serialized_start = 1670
    _globals['_LISTSCANRUNSRESPONSE']._serialized_end = 1785
    _globals['_STOPSCANRUNREQUEST']._serialized_start = 1787
    _globals['_STOPSCANRUNREQUEST']._serialized_end = 1872
    _globals['_LISTCRAWLEDURLSREQUEST']._serialized_start = 1875
    _globals['_LISTCRAWLEDURLSREQUEST']._serialized_end = 2005
    _globals['_LISTCRAWLEDURLSRESPONSE']._serialized_start = 2007
    _globals['_LISTCRAWLEDURLSRESPONSE']._serialized_end = 2131
    _globals['_GETFINDINGREQUEST']._serialized_start = 2133
    _globals['_GETFINDINGREQUEST']._serialized_end = 2217
    _globals['_LISTFINDINGSREQUEST']._serialized_start = 2220
    _globals['_LISTFINDINGSREQUEST']._serialized_end = 2368
    _globals['_LISTFINDINGSRESPONSE']._serialized_start = 2370
    _globals['_LISTFINDINGSRESPONSE']._serialized_end = 2484
    _globals['_LISTFINDINGTYPESTATSREQUEST']._serialized_start = 2486
    _globals['_LISTFINDINGTYPESTATSREQUEST']._serialized_end = 2582
    _globals['_LISTFINDINGTYPESTATSRESPONSE']._serialized_start = 2584
    _globals['_LISTFINDINGTYPESTATSRESPONSE']._serialized_end = 2700
    _globals['_WEBSECURITYSCANNER']._serialized_start = 2703
    _globals['_WEBSECURITYSCANNER']._serialized_end = 5533