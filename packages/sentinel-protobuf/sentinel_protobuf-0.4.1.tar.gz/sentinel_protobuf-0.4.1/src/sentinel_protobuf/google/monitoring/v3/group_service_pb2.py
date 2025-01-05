"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/group_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
from ....google.monitoring.v3 import group_pb2 as google_dot_monitoring_dot_v3_dot_group__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/monitoring/v3/group_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/api/monitored_resource.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/common.proto\x1a google/monitoring/v3/group.proto\x1a\x1bgoogle/protobuf/empty.proto"\xc8\x02\n\x11ListGroupsRequest\x125\n\x04name\x18\x07 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fmonitoring.googleapis.com/Group\x12A\n\x11children_of_group\x18\x02 \x01(\tB$\xfaA!\n\x1fmonitoring.googleapis.com/GroupH\x00\x12B\n\x12ancestors_of_group\x18\x03 \x01(\tB$\xfaA!\n\x1fmonitoring.googleapis.com/GroupH\x00\x12D\n\x14descendants_of_group\x18\x04 \x01(\tB$\xfaA!\n\x1fmonitoring.googleapis.com/GroupH\x00\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\tB\x08\n\x06filter"Y\n\x12ListGroupsResponse\x12*\n\x05group\x18\x01 \x03(\x0b2\x1b.google.monitoring.v3.Group\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\x0fGetGroupRequest\x125\n\x04name\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmonitoring.googleapis.com/Group"\x93\x01\n\x12CreateGroupRequest\x125\n\x04name\x18\x04 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fmonitoring.googleapis.com/Group\x12/\n\x05group\x18\x02 \x01(\x0b2\x1b.google.monitoring.v3.GroupB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\\\n\x12UpdateGroupRequest\x12/\n\x05group\x18\x02 \x01(\x0b2\x1b.google.monitoring.v3.GroupB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"^\n\x12DeleteGroupRequest\x125\n\x04name\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmonitoring.googleapis.com/Group\x12\x11\n\trecursive\x18\x04 \x01(\x08"\xbd\x01\n\x17ListGroupMembersRequest\x125\n\x04name\x18\x07 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmonitoring.googleapis.com/Group\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t\x124\n\x08interval\x18\x06 \x01(\x0b2".google.monitoring.v3.TimeInterval"w\n\x18ListGroupMembersResponse\x12.\n\x07members\x18\x01 \x03(\x0b2\x1d.google.api.MonitoredResource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\x98\x08\n\x0cGroupService\x12\x8c\x01\n\nListGroups\x12\'.google.monitoring.v3.ListGroupsRequest\x1a(.google.monitoring.v3.ListGroupsResponse"+\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v3/{name=projects/*}/groups\x12}\n\x08GetGroup\x12%.google.monitoring.v3.GetGroupRequest\x1a\x1b.google.monitoring.v3.Group"-\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v3/{name=projects/*/groups/*}\x12\x8e\x01\n\x0bCreateGroup\x12(.google.monitoring.v3.CreateGroupRequest\x1a\x1b.google.monitoring.v3.Group"8\xdaA\nname,group\x82\xd3\xe4\x93\x02%"\x1c/v3/{name=projects/*}/groups:\x05group\x12\x91\x01\n\x0bUpdateGroup\x12(.google.monitoring.v3.UpdateGroupRequest\x1a\x1b.google.monitoring.v3.Group";\xdaA\x05group\x82\xd3\xe4\x93\x02-\x1a$/v3/{group.name=projects/*/groups/*}:\x05group\x12~\n\x0bDeleteGroup\x12(.google.monitoring.v3.DeleteGroupRequest\x1a\x16.google.protobuf.Empty"-\xdaA\x04name\x82\xd3\xe4\x93\x02 *\x1e/v3/{name=projects/*/groups/*}\x12\xa8\x01\n\x10ListGroupMembers\x12-.google.monitoring.v3.ListGroupMembersRequest\x1a..google.monitoring.v3.ListGroupMembersResponse"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v3/{name=projects/*/groups/*}/members\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xcc\x01\n\x18com.google.monitoring.v3B\x11GroupServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x11GroupServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_LISTGROUPSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTGROUPSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fmonitoring.googleapis.com/Group'
    _globals['_LISTGROUPSREQUEST'].fields_by_name['children_of_group']._loaded_options = None
    _globals['_LISTGROUPSREQUEST'].fields_by_name['children_of_group']._serialized_options = b'\xfaA!\n\x1fmonitoring.googleapis.com/Group'
    _globals['_LISTGROUPSREQUEST'].fields_by_name['ancestors_of_group']._loaded_options = None
    _globals['_LISTGROUPSREQUEST'].fields_by_name['ancestors_of_group']._serialized_options = b'\xfaA!\n\x1fmonitoring.googleapis.com/Group'
    _globals['_LISTGROUPSREQUEST'].fields_by_name['descendants_of_group']._loaded_options = None
    _globals['_LISTGROUPSREQUEST'].fields_by_name['descendants_of_group']._serialized_options = b'\xfaA!\n\x1fmonitoring.googleapis.com/Group'
    _globals['_GETGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmonitoring.googleapis.com/Group'
    _globals['_CREATEGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CREATEGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fmonitoring.googleapis.com/Group'
    _globals['_CREATEGROUPREQUEST'].fields_by_name['group']._loaded_options = None
    _globals['_CREATEGROUPREQUEST'].fields_by_name['group']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGROUPREQUEST'].fields_by_name['group']._loaded_options = None
    _globals['_UPDATEGROUPREQUEST'].fields_by_name['group']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmonitoring.googleapis.com/Group'
    _globals['_LISTGROUPMEMBERSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTGROUPMEMBERSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmonitoring.googleapis.com/Group'
    _globals['_GROUPSERVICE']._loaded_options = None
    _globals['_GROUPSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_GROUPSERVICE'].methods_by_name['ListGroups']._loaded_options = None
    _globals['_GROUPSERVICE'].methods_by_name['ListGroups']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v3/{name=projects/*}/groups'
    _globals['_GROUPSERVICE'].methods_by_name['GetGroup']._loaded_options = None
    _globals['_GROUPSERVICE'].methods_by_name['GetGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v3/{name=projects/*/groups/*}'
    _globals['_GROUPSERVICE'].methods_by_name['CreateGroup']._loaded_options = None
    _globals['_GROUPSERVICE'].methods_by_name['CreateGroup']._serialized_options = b'\xdaA\nname,group\x82\xd3\xe4\x93\x02%"\x1c/v3/{name=projects/*}/groups:\x05group'
    _globals['_GROUPSERVICE'].methods_by_name['UpdateGroup']._loaded_options = None
    _globals['_GROUPSERVICE'].methods_by_name['UpdateGroup']._serialized_options = b'\xdaA\x05group\x82\xd3\xe4\x93\x02-\x1a$/v3/{group.name=projects/*/groups/*}:\x05group'
    _globals['_GROUPSERVICE'].methods_by_name['DeleteGroup']._loaded_options = None
    _globals['_GROUPSERVICE'].methods_by_name['DeleteGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 *\x1e/v3/{name=projects/*/groups/*}'
    _globals['_GROUPSERVICE'].methods_by_name['ListGroupMembers']._loaded_options = None
    _globals['_GROUPSERVICE'].methods_by_name['ListGroupMembers']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v3/{name=projects/*/groups/*}/members'
    _globals['_LISTGROUPSREQUEST']._serialized_start = 317
    _globals['_LISTGROUPSREQUEST']._serialized_end = 645
    _globals['_LISTGROUPSRESPONSE']._serialized_start = 647
    _globals['_LISTGROUPSRESPONSE']._serialized_end = 736
    _globals['_GETGROUPREQUEST']._serialized_start = 738
    _globals['_GETGROUPREQUEST']._serialized_end = 810
    _globals['_CREATEGROUPREQUEST']._serialized_start = 813
    _globals['_CREATEGROUPREQUEST']._serialized_end = 960
    _globals['_UPDATEGROUPREQUEST']._serialized_start = 962
    _globals['_UPDATEGROUPREQUEST']._serialized_end = 1054
    _globals['_DELETEGROUPREQUEST']._serialized_start = 1056
    _globals['_DELETEGROUPREQUEST']._serialized_end = 1150
    _globals['_LISTGROUPMEMBERSREQUEST']._serialized_start = 1153
    _globals['_LISTGROUPMEMBERSREQUEST']._serialized_end = 1342
    _globals['_LISTGROUPMEMBERSRESPONSE']._serialized_start = 1344
    _globals['_LISTGROUPMEMBERSRESPONSE']._serialized_end = 1463
    _globals['_GROUPSERVICE']._serialized_start = 1466
    _globals['_GROUPSERVICE']._serialized_end = 2514