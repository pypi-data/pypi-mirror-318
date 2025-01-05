"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/group.proto')
_sym_db = _symbol_database.Default()
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/monitoring/v3/group.proto\x12\x14google.monitoring.v3\x1a\x19google/api/resource.proto"\x80\x02\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bparent_name\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t\x12\x12\n\nis_cluster\x18\x06 \x01(\x08:\x99\x01\xeaA\x95\x01\n\x1fmonitoring.googleapis.com/Group\x12!projects/{project}/groups/{group}\x12+organizations/{organization}/groups/{group}\x12\x1ffolders/{folder}/groups/{group}\x12\x01*B\xc5\x01\n\x18com.google.monitoring.v3B\nGroupProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\nGroupProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_GROUP']._loaded_options = None
    _globals['_GROUP']._serialized_options = b'\xeaA\x95\x01\n\x1fmonitoring.googleapis.com/Group\x12!projects/{project}/groups/{group}\x12+organizations/{organization}/groups/{group}\x12\x1ffolders/{folder}/groups/{group}\x12\x01*'
    _globals['_GROUP']._serialized_start = 86
    _globals['_GROUP']._serialized_end = 342