"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/uptime.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ....google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/monitoring/v3/uptime.proto\x12\x14google.monitoring.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a#google/api/monitored_resource.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto"\xe6\x01\n\x0fInternalChecker\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x10\n\x08gcp_zone\x18\x04 \x01(\t\x12\x17\n\x0fpeer_project_id\x18\x06 \x01(\t\x12:\n\x05state\x18\x07 \x01(\x0e2+.google.monitoring.v3.InternalChecker.State"3\n\x05State\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02:\x02\x18\x01"\x9b\x02\n\x16SyntheticMonitorTarget\x12_\n\x11cloud_function_v2\x18\x01 \x01(\x0b2B.google.monitoring.v3.SyntheticMonitorTarget.CloudFunctionV2TargetH\x00\x1a\x95\x01\n\x15CloudFunctionV2Target\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&cloudfunctions.googleapis.com/Function\x12>\n\x12cloud_run_revision\x18\x02 \x01(\x0b2\x1d.google.api.MonitoredResourceB\x03\xe0A\x03B\x08\n\x06target"\xd6\x1e\n\x11UptimeCheckConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12;\n\x12monitored_resource\x18\x03 \x01(\x0b2\x1d.google.api.MonitoredResourceH\x00\x12O\n\x0eresource_group\x18\x04 \x01(\x0b25.google.monitoring.v3.UptimeCheckConfig.ResourceGroupH\x00\x12I\n\x11synthetic_monitor\x18\x15 \x01(\x0b2,.google.monitoring.v3.SyntheticMonitorTargetH\x00\x12G\n\nhttp_check\x18\x05 \x01(\x0b21.google.monitoring.v3.UptimeCheckConfig.HttpCheckH\x01\x12E\n\ttcp_check\x18\x06 \x01(\x0b20.google.monitoring.v3.UptimeCheckConfig.TcpCheckH\x01\x12)\n\x06period\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x12*\n\x07timeout\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12P\n\x10content_matchers\x18\t \x03(\x0b26.google.monitoring.v3.UptimeCheckConfig.ContentMatcher\x12I\n\x0cchecker_type\x18\x11 \x01(\x0e23.google.monitoring.v3.UptimeCheckConfig.CheckerType\x12A\n\x10selected_regions\x18\n \x03(\x0e2\'.google.monitoring.v3.UptimeCheckRegion\x12\x17\n\x0bis_internal\x18\x0f \x01(\x08B\x02\x18\x01\x12D\n\x11internal_checkers\x18\x0e \x03(\x0b2%.google.monitoring.v3.InternalCheckerB\x02\x18\x01\x12L\n\x0buser_labels\x18\x14 \x03(\x0b27.google.monitoring.v3.UptimeCheckConfig.UserLabelsEntry\x1aa\n\rResourceGroup\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12>\n\rresource_type\x18\x02 \x01(\x0e2\'.google.monitoring.v3.GroupResourceType\x1a!\n\nPingConfig\x12\x13\n\x0bpings_count\x18\x01 \x01(\x05\x1a\xf2\x0c\n\tHttpCheck\x12W\n\x0erequest_method\x18\x08 \x01(\x0e2?.google.monitoring.v3.UptimeCheckConfig.HttpCheck.RequestMethod\x12\x0f\n\x07use_ssl\x18\x01 \x01(\x08\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12X\n\tauth_info\x18\x04 \x01(\x0b2E.google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication\x12\x14\n\x0cmask_headers\x18\x05 \x01(\x08\x12O\n\x07headers\x18\x06 \x03(\x0b2>.google.monitoring.v3.UptimeCheckConfig.HttpCheck.HeadersEntry\x12S\n\x0ccontent_type\x18\t \x01(\x0e2=.google.monitoring.v3.UptimeCheckConfig.HttpCheck.ContentType\x12\x1b\n\x13custom_content_type\x18\r \x01(\t\x12\x14\n\x0cvalidate_ssl\x18\x07 \x01(\x08\x12\x0c\n\x04body\x18\n \x01(\x0c\x12l\n\x1eaccepted_response_status_codes\x18\x0b \x03(\x0b2D.google.monitoring.v3.UptimeCheckConfig.HttpCheck.ResponseStatusCode\x12G\n\x0bping_config\x18\x0c \x01(\x0b22.google.monitoring.v3.UptimeCheckConfig.PingConfig\x12t\n\x1cservice_agent_authentication\x18\x0e \x01(\x0b2L.google.monitoring.v3.UptimeCheckConfig.HttpCheck.ServiceAgentAuthenticationH\x00\x1a9\n\x13BasicAuthentication\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x1a\xdc\x02\n\x12ResponseStatusCode\x12\x16\n\x0cstatus_value\x18\x01 \x01(\x05H\x00\x12h\n\x0cstatus_class\x18\x02 \x01(\x0e2P.google.monitoring.v3.UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClassH\x00"\xb4\x01\n\x0bStatusClass\x12\x1c\n\x18STATUS_CLASS_UNSPECIFIED\x10\x00\x12\x14\n\x10STATUS_CLASS_1XX\x10d\x12\x15\n\x10STATUS_CLASS_2XX\x10\xc8\x01\x12\x15\n\x10STATUS_CLASS_3XX\x10\xac\x02\x12\x15\n\x10STATUS_CLASS_4XX\x10\x90\x03\x12\x15\n\x10STATUS_CLASS_5XX\x10\xf4\x03\x12\x15\n\x10STATUS_CLASS_ANY\x10\xe8\x07B\r\n\x0bstatus_code\x1a\xfc\x01\n\x1aServiceAgentAuthentication\x12y\n\x04type\x18\x01 \x01(\x0e2k.google.monitoring.v3.UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType"c\n\x1eServiceAgentAuthenticationType\x121\n-SERVICE_AGENT_AUTHENTICATION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nOIDC_TOKEN\x10\x01\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01":\n\rRequestMethod\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04POST\x10\x02"G\n\x0bContentType\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bURL_ENCODED\x10\x01\x12\x11\n\rUSER_PROVIDED\x10\x02B\r\n\x0bauth_method\x1aa\n\x08TcpCheck\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12G\n\x0bping_config\x18\x02 \x01(\x0b22.google.monitoring.v3.UptimeCheckConfig.PingConfig\x1a\xca\x05\n\x0eContentMatcher\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\\\n\x07matcher\x18\x02 \x01(\x0e2K.google.monitoring.v3.UptimeCheckConfig.ContentMatcher.ContentMatcherOption\x12c\n\x11json_path_matcher\x18\x03 \x01(\x0b2F.google.monitoring.v3.UptimeCheckConfig.ContentMatcher.JsonPathMatcherH\x00\x1a\xfd\x01\n\x0fJsonPathMatcher\x12\x11\n\tjson_path\x18\x01 \x01(\t\x12r\n\x0cjson_matcher\x18\x02 \x01(\x0e2\\.google.monitoring.v3.UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption"c\n\x15JsonPathMatcherOption\x12(\n$JSON_PATH_MATCHER_OPTION_UNSPECIFIED\x10\x00\x12\x0f\n\x0bEXACT_MATCH\x10\x01\x12\x0f\n\x0bREGEX_MATCH\x10\x02"\xc8\x01\n\x14ContentMatcherOption\x12&\n"CONTENT_MATCHER_OPTION_UNSPECIFIED\x10\x00\x12\x13\n\x0fCONTAINS_STRING\x10\x01\x12\x17\n\x13NOT_CONTAINS_STRING\x10\x02\x12\x11\n\rMATCHES_REGEX\x10\x03\x12\x15\n\x11NOT_MATCHES_REGEX\x10\x04\x12\x15\n\x11MATCHES_JSON_PATH\x10\x05\x12\x19\n\x15NOT_MATCHES_JSON_PATH\x10\x06B\x19\n\x17additional_matcher_info\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"U\n\x0bCheckerType\x12\x1c\n\x18CHECKER_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12STATIC_IP_CHECKERS\x10\x01\x12\x10\n\x0cVPC_CHECKERS\x10\x03:\xf3\x01\xeaA\xef\x01\n+monitoring.googleapis.com/UptimeCheckConfig\x12;projects/{project}/uptimeCheckConfigs/{uptime_check_config}\x12Eorganizations/{organization}/uptimeCheckConfigs/{uptime_check_config}\x129folders/{folder}/uptimeCheckConfigs/{uptime_check_config}\x12\x01*B\n\n\x08resourceB\x14\n\x12check_request_type"n\n\rUptimeCheckIp\x127\n\x06region\x18\x01 \x01(\x0e2\'.google.monitoring.v3.UptimeCheckRegion\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x12\n\nip_address\x18\x03 \x01(\t*\x95\x01\n\x11UptimeCheckRegion\x12\x16\n\x12REGION_UNSPECIFIED\x10\x00\x12\x07\n\x03USA\x10\x01\x12\n\n\x06EUROPE\x10\x02\x12\x11\n\rSOUTH_AMERICA\x10\x03\x12\x10\n\x0cASIA_PACIFIC\x10\x04\x12\x0e\n\nUSA_OREGON\x10\x05\x12\x0c\n\x08USA_IOWA\x10\x06\x12\x10\n\x0cUSA_VIRGINIA\x10\x07*[\n\x11GroupResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INSTANCE\x10\x01\x12\x19\n\x15AWS_ELB_LOAD_BALANCER\x10\x02B\xaf\x02\n\x18com.google.monitoring.v3B\x0bUptimeProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3\xeaAf\n&cloudfunctions.googleapis.com/Function\x12<projects/{project}/locations/{location}/functions/{function}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.uptime_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x0bUptimeProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3\xeaAf\n&cloudfunctions.googleapis.com/Function\x12<projects/{project}/locations/{location}/functions/{function}'
    _globals['_INTERNALCHECKER']._loaded_options = None
    _globals['_INTERNALCHECKER']._serialized_options = b'\x18\x01'
    _globals['_SYNTHETICMONITORTARGET_CLOUDFUNCTIONV2TARGET'].fields_by_name['name']._loaded_options = None
    _globals['_SYNTHETICMONITORTARGET_CLOUDFUNCTIONV2TARGET'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&cloudfunctions.googleapis.com/Function'
    _globals['_SYNTHETICMONITORTARGET_CLOUDFUNCTIONV2TARGET'].fields_by_name['cloud_run_revision']._loaded_options = None
    _globals['_SYNTHETICMONITORTARGET_CLOUDFUNCTIONV2TARGET'].fields_by_name['cloud_run_revision']._serialized_options = b'\xe0A\x03'
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY']._loaded_options = None
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_UPTIMECHECKCONFIG_USERLABELSENTRY']._loaded_options = None
    _globals['_UPTIMECHECKCONFIG_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_UPTIMECHECKCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_UPTIMECHECKCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_UPTIMECHECKCONFIG'].fields_by_name['is_internal']._loaded_options = None
    _globals['_UPTIMECHECKCONFIG'].fields_by_name['is_internal']._serialized_options = b'\x18\x01'
    _globals['_UPTIMECHECKCONFIG'].fields_by_name['internal_checkers']._loaded_options = None
    _globals['_UPTIMECHECKCONFIG'].fields_by_name['internal_checkers']._serialized_options = b'\x18\x01'
    _globals['_UPTIMECHECKCONFIG']._loaded_options = None
    _globals['_UPTIMECHECKCONFIG']._serialized_options = b'\xeaA\xef\x01\n+monitoring.googleapis.com/UptimeCheckConfig\x12;projects/{project}/uptimeCheckConfigs/{uptime_check_config}\x12Eorganizations/{organization}/uptimeCheckConfigs/{uptime_check_config}\x129folders/{folder}/uptimeCheckConfigs/{uptime_check_config}\x12\x01*'
    _globals['_UPTIMECHECKREGION']._serialized_start = 4778
    _globals['_UPTIMECHECKREGION']._serialized_end = 4927
    _globals['_GROUPRESOURCETYPE']._serialized_start = 4929
    _globals['_GROUPRESOURCETYPE']._serialized_end = 5020
    _globals['_INTERNALCHECKER']._serialized_start = 218
    _globals['_INTERNALCHECKER']._serialized_end = 448
    _globals['_INTERNALCHECKER_STATE']._serialized_start = 393
    _globals['_INTERNALCHECKER_STATE']._serialized_end = 444
    _globals['_SYNTHETICMONITORTARGET']._serialized_start = 451
    _globals['_SYNTHETICMONITORTARGET']._serialized_end = 734
    _globals['_SYNTHETICMONITORTARGET_CLOUDFUNCTIONV2TARGET']._serialized_start = 575
    _globals['_SYNTHETICMONITORTARGET_CLOUDFUNCTIONV2TARGET']._serialized_end = 724
    _globals['_UPTIMECHECKCONFIG']._serialized_start = 737
    _globals['_UPTIMECHECKCONFIG']._serialized_end = 4663
    _globals['_UPTIMECHECKCONFIG_RESOURCEGROUP']._serialized_start = 1644
    _globals['_UPTIMECHECKCONFIG_RESOURCEGROUP']._serialized_end = 1741
    _globals['_UPTIMECHECKCONFIG_PINGCONFIG']._serialized_start = 1743
    _globals['_UPTIMECHECKCONFIG_PINGCONFIG']._serialized_end = 1776
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK']._serialized_start = 1779
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK']._serialized_end = 3429
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION']._serialized_start = 2570
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION']._serialized_end = 2627
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_RESPONSESTATUSCODE']._serialized_start = 2630
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_RESPONSESTATUSCODE']._serialized_end = 2978
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_RESPONSESTATUSCODE_STATUSCLASS']._serialized_start = 2783
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_RESPONSESTATUSCODE_STATUSCLASS']._serialized_end = 2963
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_SERVICEAGENTAUTHENTICATION']._serialized_start = 2981
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_SERVICEAGENTAUTHENTICATION']._serialized_end = 3233
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_SERVICEAGENTAUTHENTICATION_SERVICEAGENTAUTHENTICATIONTYPE']._serialized_start = 3134
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_SERVICEAGENTAUTHENTICATION_SERVICEAGENTAUTHENTICATIONTYPE']._serialized_end = 3233
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY']._serialized_start = 3235
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY']._serialized_end = 3281
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_REQUESTMETHOD']._serialized_start = 3283
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_REQUESTMETHOD']._serialized_end = 3341
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_CONTENTTYPE']._serialized_start = 3343
    _globals['_UPTIMECHECKCONFIG_HTTPCHECK_CONTENTTYPE']._serialized_end = 3414
    _globals['_UPTIMECHECKCONFIG_TCPCHECK']._serialized_start = 3431
    _globals['_UPTIMECHECKCONFIG_TCPCHECK']._serialized_end = 3528
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER']._serialized_start = 3531
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER']._serialized_end = 4245
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER_JSONPATHMATCHER']._serialized_start = 3762
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER_JSONPATHMATCHER']._serialized_end = 4015
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER_JSONPATHMATCHER_JSONPATHMATCHEROPTION']._serialized_start = 3916
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER_JSONPATHMATCHER_JSONPATHMATCHEROPTION']._serialized_end = 4015
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER_CONTENTMATCHEROPTION']._serialized_start = 4018
    _globals['_UPTIMECHECKCONFIG_CONTENTMATCHER_CONTENTMATCHEROPTION']._serialized_end = 4218
    _globals['_UPTIMECHECKCONFIG_USERLABELSENTRY']._serialized_start = 4247
    _globals['_UPTIMECHECKCONFIG_USERLABELSENTRY']._serialized_end = 4296
    _globals['_UPTIMECHECKCONFIG_CHECKERTYPE']._serialized_start = 4298
    _globals['_UPTIMECHECKCONFIG_CHECKERTYPE']._serialized_end = 4383
    _globals['_UPTIMECHECKIP']._serialized_start = 4665
    _globals['_UPTIMECHECKIP']._serialized_end = 4775