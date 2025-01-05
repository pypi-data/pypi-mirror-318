"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1/web_security_scanner.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.websecurityscanner.v1 import crawled_url_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_crawled__url__pb2
from .....google.cloud.websecurityscanner.v1 import finding_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_finding__pb2
from .....google.cloud.websecurityscanner.v1 import finding_type_stats_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_finding__type__stats__pb2
from .....google.cloud.websecurityscanner.v1 import scan_config_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__config__pb2
from .....google.cloud.websecurityscanner.v1 import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__run__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/websecurityscanner/v1/web_security_scanner.proto\x12"google.cloud.websecurityscanner.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a4google/cloud/websecurityscanner/v1/crawled_url.proto\x1a0google/cloud/websecurityscanner/v1/finding.proto\x1a;google/cloud/websecurityscanner/v1/finding_type_stats.proto\x1a4google/cloud/websecurityscanner/v1/scan_config.proto\x1a1google/cloud/websecurityscanner/v1/scan_run.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"n\n\x17CreateScanConfigRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12C\n\x0bscan_config\x18\x02 \x01(\x0b2..google.cloud.websecurityscanner.v1.ScanConfig"\'\n\x17DeleteScanConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"$\n\x14GetScanConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"O\n\x16ListScanConfigsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\x8f\x01\n\x17UpdateScanConfigRequest\x12C\n\x0bscan_config\x18\x02 \x01(\x0b2..google.cloud.websecurityscanner.v1.ScanConfig\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"x\n\x17ListScanConfigsResponse\x12D\n\x0cscan_configs\x18\x01 \x03(\x0b2..google.cloud.websecurityscanner.v1.ScanConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"#\n\x13StartScanRunRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"!\n\x11GetScanRunRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"L\n\x13ListScanRunsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"o\n\x14ListScanRunsResponse\x12>\n\tscan_runs\x18\x01 \x03(\x0b2+.google.cloud.websecurityscanner.v1.ScanRun\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t""\n\x12StopScanRunRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"O\n\x16ListCrawledUrlsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"x\n\x17ListCrawledUrlsResponse\x12D\n\x0ccrawled_urls\x18\x01 \x03(\x0b2..google.cloud.websecurityscanner.v1.CrawledUrl\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11GetFindingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\\\n\x13ListFindingsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"n\n\x14ListFindingsResponse\x12=\n\x08findings\x18\x01 \x03(\x0b2+.google.cloud.websecurityscanner.v1.Finding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"-\n\x1bListFindingTypeStatsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t"p\n\x1cListFindingTypeStatsResponse\x12P\n\x12finding_type_stats\x18\x01 \x03(\x0b24.google.cloud.websecurityscanner.v1.FindingTypeStats2\xe9\x13\n\x12WebSecurityScanner\x12\xb9\x01\n\x10CreateScanConfig\x12;.google.cloud.websecurityscanner.v1.CreateScanConfigRequest\x1a..google.cloud.websecurityscanner.v1.ScanConfig"8\x82\xd3\xe4\x93\x022"#/v1/{parent=projects/*}/scanConfigs:\x0bscan_config\x12\x94\x01\n\x10DeleteScanConfig\x12;.google.cloud.websecurityscanner.v1.DeleteScanConfigRequest\x1a\x16.google.protobuf.Empty"+\x82\xd3\xe4\x93\x02%*#/v1/{name=projects/*/scanConfigs/*}\x12\xa6\x01\n\rGetScanConfig\x128.google.cloud.websecurityscanner.v1.GetScanConfigRequest\x1a..google.cloud.websecurityscanner.v1.ScanConfig"+\x82\xd3\xe4\x93\x02%\x12#/v1/{name=projects/*/scanConfigs/*}\x12\xb7\x01\n\x0fListScanConfigs\x12:.google.cloud.websecurityscanner.v1.ListScanConfigsRequest\x1a;.google.cloud.websecurityscanner.v1.ListScanConfigsResponse"+\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=projects/*}/scanConfigs\x12\xc5\x01\n\x10UpdateScanConfig\x12;.google.cloud.websecurityscanner.v1.UpdateScanConfigRequest\x1a..google.cloud.websecurityscanner.v1.ScanConfig"D\x82\xd3\xe4\x93\x02>2//v1/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config\x12\xaa\x01\n\x0cStartScanRun\x127.google.cloud.websecurityscanner.v1.StartScanRunRequest\x1a+.google.cloud.websecurityscanner.v1.ScanRun"4\x82\xd3\xe4\x93\x02.")/v1/{name=projects/*/scanConfigs/*}:start:\x01*\x12\xa8\x01\n\nGetScanRun\x125.google.cloud.websecurityscanner.v1.GetScanRunRequest\x1a+.google.cloud.websecurityscanner.v1.ScanRun"6\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/scanConfigs/*/scanRuns/*}\x12\xb9\x01\n\x0cListScanRuns\x127.google.cloud.websecurityscanner.v1.ListScanRunsRequest\x1a8.google.cloud.websecurityscanner.v1.ListScanRunsResponse"6\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/scanConfigs/*}/scanRuns\x12\xb2\x01\n\x0bStopScanRun\x126.google.cloud.websecurityscanner.v1.StopScanRunRequest\x1a+.google.cloud.websecurityscanner.v1.ScanRun">\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*\x12\xd0\x01\n\x0fListCrawledUrls\x12:.google.cloud.websecurityscanner.v1.ListCrawledUrlsRequest\x1a;.google.cloud.websecurityscanner.v1.ListCrawledUrlsResponse"D\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls\x12\xb3\x01\n\nGetFinding\x125.google.cloud.websecurityscanner.v1.GetFindingRequest\x1a+.google.cloud.websecurityscanner.v1.Finding"A\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}\x12\xc4\x01\n\x0cListFindings\x127.google.cloud.websecurityscanner.v1.ListFindingsRequest\x1a8.google.cloud.websecurityscanner.v1.ListFindingsResponse"A\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings\x12\xe4\x01\n\x14ListFindingTypeStats\x12?.google.cloud.websecurityscanner.v1.ListFindingTypeStatsRequest\x1a@.google.cloud.websecurityscanner.v1.ListFindingTypeStatsResponse"I\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats\x1aU\xcaA!websecurityscanner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8d\x02\n&com.google.cloud.websecurityscanner.v1B\x17WebSecurityScannerProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1.web_security_scanner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.websecurityscanner.v1B\x17WebSecurityScannerProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1'
    _globals['_WEBSECURITYSCANNER']._loaded_options = None
    _globals['_WEBSECURITYSCANNER']._serialized_options = b'\xcaA!websecurityscanner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['CreateScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['CreateScanConfig']._serialized_options = b'\x82\xd3\xe4\x93\x022"#/v1/{parent=projects/*}/scanConfigs:\x0bscan_config'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['DeleteScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['DeleteScanConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02%*#/v1/{name=projects/*/scanConfigs/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/v1/{name=projects/*/scanConfigs/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanConfigs']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanConfigs']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=projects/*}/scanConfigs'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['UpdateScanConfig']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['UpdateScanConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02>2//v1/{scan_config.name=projects/*/scanConfigs/*}:\x0bscan_config'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StartScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StartScanRun']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/v1/{name=projects/*/scanConfigs/*}:start:\x01*'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetScanRun']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/scanConfigs/*/scanRuns/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanRuns']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListScanRuns']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/scanConfigs/*}/scanRuns'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StopScanRun']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['StopScanRun']._serialized_options = b'\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/scanConfigs/*/scanRuns/*}:stop:\x01*'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListCrawledUrls']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListCrawledUrls']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetFinding']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['GetFinding']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindings']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindings']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings'
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindingTypeStats']._loaded_options = None
    _globals['_WEBSECURITYSCANNER'].methods_by_name['ListFindingTypeStats']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats'
    _globals['_CREATESCANCONFIGREQUEST']._serialized_start = 489
    _globals['_CREATESCANCONFIGREQUEST']._serialized_end = 599
    _globals['_DELETESCANCONFIGREQUEST']._serialized_start = 601
    _globals['_DELETESCANCONFIGREQUEST']._serialized_end = 640
    _globals['_GETSCANCONFIGREQUEST']._serialized_start = 642
    _globals['_GETSCANCONFIGREQUEST']._serialized_end = 678
    _globals['_LISTSCANCONFIGSREQUEST']._serialized_start = 680
    _globals['_LISTSCANCONFIGSREQUEST']._serialized_end = 759
    _globals['_UPDATESCANCONFIGREQUEST']._serialized_start = 762
    _globals['_UPDATESCANCONFIGREQUEST']._serialized_end = 905
    _globals['_LISTSCANCONFIGSRESPONSE']._serialized_start = 907
    _globals['_LISTSCANCONFIGSRESPONSE']._serialized_end = 1027
    _globals['_STARTSCANRUNREQUEST']._serialized_start = 1029
    _globals['_STARTSCANRUNREQUEST']._serialized_end = 1064
    _globals['_GETSCANRUNREQUEST']._serialized_start = 1066
    _globals['_GETSCANRUNREQUEST']._serialized_end = 1099
    _globals['_LISTSCANRUNSREQUEST']._serialized_start = 1101
    _globals['_LISTSCANRUNSREQUEST']._serialized_end = 1177
    _globals['_LISTSCANRUNSRESPONSE']._serialized_start = 1179
    _globals['_LISTSCANRUNSRESPONSE']._serialized_end = 1290
    _globals['_STOPSCANRUNREQUEST']._serialized_start = 1292
    _globals['_STOPSCANRUNREQUEST']._serialized_end = 1326
    _globals['_LISTCRAWLEDURLSREQUEST']._serialized_start = 1328
    _globals['_LISTCRAWLEDURLSREQUEST']._serialized_end = 1407
    _globals['_LISTCRAWLEDURLSRESPONSE']._serialized_start = 1409
    _globals['_LISTCRAWLEDURLSRESPONSE']._serialized_end = 1529
    _globals['_GETFINDINGREQUEST']._serialized_start = 1531
    _globals['_GETFINDINGREQUEST']._serialized_end = 1564
    _globals['_LISTFINDINGSREQUEST']._serialized_start = 1566
    _globals['_LISTFINDINGSREQUEST']._serialized_end = 1658
    _globals['_LISTFINDINGSRESPONSE']._serialized_start = 1660
    _globals['_LISTFINDINGSRESPONSE']._serialized_end = 1770
    _globals['_LISTFINDINGTYPESTATSREQUEST']._serialized_start = 1772
    _globals['_LISTFINDINGTYPESTATSREQUEST']._serialized_end = 1817
    _globals['_LISTFINDINGTYPESTATSRESPONSE']._serialized_start = 1819
    _globals['_LISTFINDINGTYPESTATSRESPONSE']._serialized_end = 1931
    _globals['_WEBSECURITYSCANNER']._serialized_start = 1934
    _globals['_WEBSECURITYSCANNER']._serialized_end = 4471