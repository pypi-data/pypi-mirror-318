"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/uptime_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import uptime_pb2 as google_dot_monitoring_dot_v3_dot_uptime__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/monitoring/v3/uptime_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/uptime.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9b\x01\n\x1dListUptimeCheckConfigsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+monitoring.googleapis.com/UptimeCheckConfig\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"\x94\x01\n\x1eListUptimeCheckConfigsResponse\x12E\n\x14uptime_check_configs\x18\x01 \x03(\x0b2\'.google.monitoring.v3.UptimeCheckConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"`\n\x1bGetUptimeCheckConfigRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+monitoring.googleapis.com/UptimeCheckConfig"\xb0\x01\n\x1eCreateUptimeCheckConfigRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+monitoring.googleapis.com/UptimeCheckConfig\x12I\n\x13uptime_check_config\x18\x02 \x01(\x0b2\'.google.monitoring.v3.UptimeCheckConfigB\x03\xe0A\x02"\x9c\x01\n\x1eUpdateUptimeCheckConfigRequest\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12I\n\x13uptime_check_config\x18\x03 \x01(\x0b2\'.google.monitoring.v3.UptimeCheckConfigB\x03\xe0A\x02"c\n\x1eDeleteUptimeCheckConfigRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+monitoring.googleapis.com/UptimeCheckConfig"B\n\x19ListUptimeCheckIpsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"t\n\x1aListUptimeCheckIpsResponse\x12=\n\x10uptime_check_ips\x18\x01 \x03(\x0b2#.google.monitoring.v3.UptimeCheckIp\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbd\n\n\x12UptimeCheckService\x12\xc0\x01\n\x16ListUptimeCheckConfigs\x123.google.monitoring.v3.ListUptimeCheckConfigsRequest\x1a4.google.monitoring.v3.ListUptimeCheckConfigsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v3/{parent=projects/*}/uptimeCheckConfigs\x12\xad\x01\n\x14GetUptimeCheckConfig\x121.google.monitoring.v3.GetUptimeCheckConfigRequest\x1a\'.google.monitoring.v3.UptimeCheckConfig"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*/uptimeCheckConfigs/*}\x12\xde\x01\n\x17CreateUptimeCheckConfig\x124.google.monitoring.v3.CreateUptimeCheckConfigRequest\x1a\'.google.monitoring.v3.UptimeCheckConfig"d\xdaA\x1aparent,uptime_check_config\x82\xd3\xe4\x93\x02A"*/v3/{parent=projects/*}/uptimeCheckConfigs:\x13uptime_check_config\x12\xeb\x01\n\x17UpdateUptimeCheckConfig\x124.google.monitoring.v3.UpdateUptimeCheckConfigRequest\x1a\'.google.monitoring.v3.UptimeCheckConfig"q\xdaA\x13uptime_check_config\x82\xd3\xe4\x93\x02U2>/v3/{uptime_check_config.name=projects/*/uptimeCheckConfigs/*}:\x13uptime_check_config\x12\xa2\x01\n\x17DeleteUptimeCheckConfig\x124.google.monitoring.v3.DeleteUptimeCheckConfigRequest\x1a\x16.google.protobuf.Empty"9\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v3/{name=projects/*/uptimeCheckConfigs/*}\x12\x93\x01\n\x12ListUptimeCheckIps\x12/.google.monitoring.v3.ListUptimeCheckIpsRequest\x1a0.google.monitoring.v3.ListUptimeCheckIpsResponse"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v3/uptimeCheckIps\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xcd\x01\n\x18com.google.monitoring.v3B\x12UptimeServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.uptime_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x12UptimeServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_LISTUPTIMECHECKCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTUPTIMECHECKCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+monitoring.googleapis.com/UptimeCheckConfig'
    _globals['_GETUPTIMECHECKCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETUPTIMECHECKCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+monitoring.googleapis.com/UptimeCheckConfig'
    _globals['_CREATEUPTIMECHECKCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEUPTIMECHECKCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+monitoring.googleapis.com/UptimeCheckConfig'
    _globals['_CREATEUPTIMECHECKCONFIGREQUEST'].fields_by_name['uptime_check_config']._loaded_options = None
    _globals['_CREATEUPTIMECHECKCONFIGREQUEST'].fields_by_name['uptime_check_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEUPTIMECHECKCONFIGREQUEST'].fields_by_name['uptime_check_config']._loaded_options = None
    _globals['_UPDATEUPTIMECHECKCONFIGREQUEST'].fields_by_name['uptime_check_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEUPTIMECHECKCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEUPTIMECHECKCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+monitoring.googleapis.com/UptimeCheckConfig'
    _globals['_UPTIMECHECKSERVICE']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['ListUptimeCheckConfigs']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['ListUptimeCheckConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v3/{parent=projects/*}/uptimeCheckConfigs'
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['GetUptimeCheckConfig']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['GetUptimeCheckConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*/uptimeCheckConfigs/*}'
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['CreateUptimeCheckConfig']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['CreateUptimeCheckConfig']._serialized_options = b'\xdaA\x1aparent,uptime_check_config\x82\xd3\xe4\x93\x02A"*/v3/{parent=projects/*}/uptimeCheckConfigs:\x13uptime_check_config'
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['UpdateUptimeCheckConfig']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['UpdateUptimeCheckConfig']._serialized_options = b'\xdaA\x13uptime_check_config\x82\xd3\xe4\x93\x02U2>/v3/{uptime_check_config.name=projects/*/uptimeCheckConfigs/*}:\x13uptime_check_config'
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['DeleteUptimeCheckConfig']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['DeleteUptimeCheckConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v3/{name=projects/*/uptimeCheckConfigs/*}'
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['ListUptimeCheckIps']._loaded_options = None
    _globals['_UPTIMECHECKSERVICE'].methods_by_name['ListUptimeCheckIps']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14\x12\x12/v3/uptimeCheckIps'
    _globals['_LISTUPTIMECHECKCONFIGSREQUEST']._serialized_start = 281
    _globals['_LISTUPTIMECHECKCONFIGSREQUEST']._serialized_end = 436
    _globals['_LISTUPTIMECHECKCONFIGSRESPONSE']._serialized_start = 439
    _globals['_LISTUPTIMECHECKCONFIGSRESPONSE']._serialized_end = 587
    _globals['_GETUPTIMECHECKCONFIGREQUEST']._serialized_start = 589
    _globals['_GETUPTIMECHECKCONFIGREQUEST']._serialized_end = 685
    _globals['_CREATEUPTIMECHECKCONFIGREQUEST']._serialized_start = 688
    _globals['_CREATEUPTIMECHECKCONFIGREQUEST']._serialized_end = 864
    _globals['_UPDATEUPTIMECHECKCONFIGREQUEST']._serialized_start = 867
    _globals['_UPDATEUPTIMECHECKCONFIGREQUEST']._serialized_end = 1023
    _globals['_DELETEUPTIMECHECKCONFIGREQUEST']._serialized_start = 1025
    _globals['_DELETEUPTIMECHECKCONFIGREQUEST']._serialized_end = 1124
    _globals['_LISTUPTIMECHECKIPSREQUEST']._serialized_start = 1126
    _globals['_LISTUPTIMECHECKIPSREQUEST']._serialized_end = 1192
    _globals['_LISTUPTIMECHECKIPSRESPONSE']._serialized_start = 1194
    _globals['_LISTUPTIMECHECKIPSRESPONSE']._serialized_end = 1310
    _globals['_UPTIMECHECKSERVICE']._serialized_start = 1313
    _globals['_UPTIMECHECKSERVICE']._serialized_end = 2654