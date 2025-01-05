"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1alpha/web_security_scanner.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1alpha import crawled_url_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_crawled__url__pb2
from .....google.cloud.websecurityscanner.v1alpha import finding_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__pb2
from .....google.cloud.websecurityscanner.v1alpha import finding_type_stats_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__type__stats__pb2
from .....google.cloud.websecurityscanner.v1alpha import scan_config_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_scan__config__pb2
from .....google.cloud.websecurityscanner.v1alpha import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_scan__run__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/websecurityscanner/v1alpha/web_security_scanner.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a9google/cloud/websecurityscanner/v1alpha/crawled_url.proto\x1a5google/cloud/websecurityscanner/v1alpha/finding.proto\x1a@google/cloud/websecurityscanner/v1alpha/finding_type_stats.proto\x1a9google/cloud/websecurityscanner/v1alpha/scan_config.proto\x1a6google/cloud/websecurityscanner/v1alpha/scan_run.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xad\x01\n\x17CreateScanConfigRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12M\n\x0bscan_config\x18\x02 \x01(\x0b23.google.cloud.websecurityscanner.v1alpha.ScanConfigB\x03\xe0A\x02"]\n\x17DeleteScanConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig"Z\n\x14GetScanConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig"\x84\x01\n\x16ListScanConfigsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\x9e\x01\n\x17UpdateScanConfigRequest\x12M\n\x0bscan_config\x18\x02 \x01(\x0b23.google.cloud.websecurityscanner.v1alpha.ScanConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"}\n\x17ListScanConfigsResponse\x12I\n\x0cscan_configs\x18\x01 \x03(\x0b23.google.cloud.websecurityscanner.v1alpha.ScanConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Y\n\x13StartScanRunRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig"T\n\x11GetScanRunRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun"\x82\x01\n\x13ListScanRunsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,websecurityscanner.googleapis.com/ScanConfig\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"t\n\x14ListScanRunsResponse\x12C\n\tscan_runs\x18\x01 \x03(\x0b20.google.cloud.websecurityscanner.v1alpha.ScanRun\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x12StopScanRunRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun"\x82\x01\n\x16ListCrawledUrlsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"}\n\x17ListCrawledUrlsResponse\x12I\n\x0ccrawled_urls\x18\x01 \x03(\x0b23.google.cloud.websecurityscanner.v1alpha.CrawledUrl\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x11GetFindingRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/Finding"\x94\x01\n\x13ListFindingsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"s\n\x14ListFindingsResponse\x12B\n\x08findings\x18\x01 \x03(\x0b20.google.cloud.websecurityscanner.v1alpha.Finding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x1bListFindingTypeStatsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)websecurityscanner.googleapis.com/ScanRun"u\n\x1cListFindingTypeStatsResponse\x12U\n\x12finding_type_stats\x18\x01 \x03(\x0b29.google.cloud.websecurityscanner.v1alpha.FindingTypeStats2\xb4\x16\n\x12WebSecurityScanner\x12\xdd\x01\n\x10CreateScanConfig\x12@.google.cloud.websecurityscanner.v1alpha.CreateScanConfigRequest\x1a3.google.cloud.websecurityscanner.v1alpha.ScanConfig"R\xdaA\x12parent,scan_config\x82\xd3\xe4\x93\x027"(/v1alpha/{parent=projects/*}/scanConfigs:\x0bscan_config\x12\xa5\x01\n\x10DeleteScanConfig\x12@.google.cloud.websecurityscanner.v1alpha.DeleteScanConfigRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1alpha/{name=projects/*/scanConfigs/*}\x12\xbc\x01\n\rGetScanConfig\x12=.google.cloud.websecurityscanner.v1alpha.GetScanConfigRequest\x1a3.google.cloud.websecurityscanner.v1alpha.ScanConfig"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1alpha/{name=projects/*/scanConfigs/*}\x12\xcf\x01\n\x0fListScanConfigs\x12?.google.cloud.websecurityscanner.v1alpha.ListScanConfigsRequest\x1a@.google.cloud.websecurityscanner.v1alpha.ListScanConfigsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1alpha/{parent=projects/*}/scanConfigs\x12\xee\x01\n\x10UpdateScanConfig\x12@.google.cloud.websecurityscanner.v1alpha.UpdateScanConfigRequest\x1a3.google.cloud.websecurityscanner.v1alpha.ScanConfig"c\xdaA\x17scan_config,update_mask\x82\xd3\xe4\x93\x02C24/v1alpha/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config\x12\xc0\x01\n\x0cStartScanRun\x12<.google.cloud.websecurityscanner.v1alpha.StartScanRunRequest\x1a0.google.cloud.websecurityscanner.v1alpha.ScanRun"@\xdaA\x04name\x82\xd3\xe4\x93\x023"./v1alpha/{name=projects/*/scanConfigs/*}:start:\x01*\x12\xbe\x01\n\nGetScanRun\x12:.google.cloud.websecurityscanner.v1alpha.GetScanRunRequest\x1a0.google.cloud.websecurityscanner.v1alpha.ScanRun"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1alpha/{name=projects/*/scanConfigs/*/scanRuns/*}\x12\xd1\x01\n\x0cListScanRuns\x12<.google.cloud.websecurityscanner.v1alpha.ListScanRunsRequest\x1a=.google.cloud.websecurityscanner.v1alpha.ListScanRunsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1alpha/{parent=projects/*/scanConfigs/*}/scanRuns\x12\xc8\x01\n\x0bStopScanRun\x12;.google.cloud.websecurityscanner.v1alpha.StopScanRunRequest\x1a0.google.cloud.websecurityscanner.v1alpha.ScanRun"J\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1alpha/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*\x12\xe8\x01\n\x0fListCrawledUrls\x12?.google.cloud.websecurityscanner.v1alpha.ListCrawledUrlsRequest\x1a@.google.cloud.websecurityscanner.v1alpha.ListCrawledUrlsResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1alpha/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls\x12\xc9\x01\n\nGetFinding\x12:.google.cloud.websecurityscanner.v1alpha.GetFindingRequest\x1a0.google.cloud.websecurityscanner.v1alpha.Finding"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}\x12\xe3\x01\n\x0cListFindings\x12<.google.cloud.websecurityscanner.v1alpha.ListFindingsRequest\x1a=.google.cloud.websecurityscanner.v1alpha.ListFindingsResponse"V\xdaA\rparent,filter\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings\x12\xfc\x01\n\x14ListFindingTypeStats\x12D.google.cloud.websecurityscanner.v1alpha.ListFindingTypeStatsRequest\x1aE.google.cloud.websecurityscanner.v1alpha.ListFindingTypeStatsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1alpha/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats\x1aU\xcaA!websecurityscanner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa5\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x17WebSecurityScannerProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1alpha.web_security_scanner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.cloud.websecurityscanner.v1alphaB\x17WebSecurityScannerProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpb'
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
    _globals['_WEBSECURITYSCANNER'].methods_by_name['CreateScanConfig']._serialized_options = b'\xdaA\x12parent,scan_config\x82\xd3\xe4\x93\x027"(/v1alpha/{parent=projects/*}/scanConfigs:\x0bscan_config'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['DeleteScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['DeleteScanConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1alpha/{name=projects/*/scanConfigs/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1alpha/{name=projects/*/scanConfigs/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanConfigs']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1alpha/{parent=projects/*}/scanConfigs'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['UpdateScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['UpdateScanConfig']._serialized_options = b'\xdaA\x17scan_config,update_mask\x82\xd3\xe4\x93\x02C24/v1alpha/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StartScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StartScanRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023"./v1alpha/{name=projects/*/scanConfigs/*}:start:\x01*'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1alpha/{name=projects/*/scanConfigs/*/scanRuns/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanRuns']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanRuns']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1alpha/{parent=projects/*/scanConfigs/*}/scanRuns'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StopScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StopScanRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1alpha/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListCrawledUrls']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListCrawledUrls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1alpha/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetFinding']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetFinding']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindings']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindings']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02@\x12>/v1alpha/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindingTypeStats']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindingTypeStats']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1alpha/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats'
    _globals['_CREATESCANCONFIGREQUEST']._serialized_start = 585
    _globals['_CREATESCANCONFIGREQUEST']._serialized_end = 758
    _globals['_DELETESCANCONFIGREQUEST']._serialized_start = 760
    _globals['_DELETESCANCONFIGREQUEST']._serialized_end = 853
    _globals['_GETSCANCONFIGREQUEST']._serialized_start = 855
    _globals['_GETSCANCONFIGREQUEST']._serialized_end = 945
    _globals['_LISTSCANCONFIGSREQUEST']._serialized_start = 948
    _globals['_LISTSCANCONFIGSREQUEST']._serialized_end = 1080
    _globals['_UPDATESCANCONFIGREQUEST']._serialized_start = 1083
    _globals['_UPDATESCANCONFIGREQUEST']._serialized_end = 1241
    _globals['_LISTSCANCONFIGSRESPONSE']._serialized_start = 1243
    _globals['_LISTSCANCONFIGSRESPONSE']._serialized_end = 1368
    _globals['_STARTSCANRUNREQUEST']._serialized_start = 1370
    _globals['_STARTSCANRUNREQUEST']._serialized_end = 1459
    _globals['_GETSCANRUNREQUEST']._serialized_start = 1461
    _globals['_GETSCANRUNREQUEST']._serialized_end = 1545
    _globals['_LISTSCANRUNSREQUEST']._serialized_start = 1548
    _globals['_LISTSCANRUNSREQUEST']._serialized_end = 1678
    _globals['_LISTSCANRUNSRESPONSE']._serialized_start = 1680
    _globals['_LISTSCANRUNSRESPONSE']._serialized_end = 1796
    _globals['_STOPSCANRUNREQUEST']._serialized_start = 1798
    _globals['_STOPSCANRUNREQUEST']._serialized_end = 1883
    _globals['_LISTCRAWLEDURLSREQUEST']._serialized_start = 1886
    _globals['_LISTCRAWLEDURLSREQUEST']._serialized_end = 2016
    _globals['_LISTCRAWLEDURLSRESPONSE']._serialized_start = 2018
    _globals['_LISTCRAWLEDURLSRESPONSE']._serialized_end = 2143
    _globals['_GETFINDINGREQUEST']._serialized_start = 2145
    _globals['_GETFINDINGREQUEST']._serialized_end = 2229
    _globals['_LISTFINDINGSREQUEST']._serialized_start = 2232
    _globals['_LISTFINDINGSREQUEST']._serialized_end = 2380
    _globals['_LISTFINDINGSRESPONSE']._serialized_start = 2382
    _globals['_LISTFINDINGSRESPONSE']._serialized_end = 2497
    _globals['_LISTFINDINGTYPESTATSREQUEST']._serialized_start = 2499
    _globals['_LISTFINDINGTYPESTATSREQUEST']._serialized_end = 2595
    _globals['_LISTFINDINGTYPESTATSRESPONSE']._serialized_start = 2597
    _globals['_LISTFINDINGTYPESTATSRESPONSE']._serialized_end = 2714
    _globals['_WEBSECURITYSCANNER']._serialized_start = 2717
    _globals['_WEBSECURITYSCANNER']._serialized_end = 5585