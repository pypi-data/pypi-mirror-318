"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/mute_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/securitycenter/v2/mute_config.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x06\n\nMuteConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1f\n\x12most_recent_editor\x18\x06 \x01(\tB\x03\xe0A\x03\x12L\n\x04type\x18\x08 \x01(\x0e29.google.cloud.securitycenter.v2.MuteConfig.MuteConfigTypeB\x03\xe0A\x02\x124\n\x0bexpiry_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"K\n\x0eMuteConfigType\x12 \n\x1cMUTE_CONFIG_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STATIC\x10\x01\x12\x0b\n\x07DYNAMIC\x10\x02:\xaa\x03\xeaA\xa6\x03\n(securitycenter.googleapis.com/MuteConfig\x126organizations/{organization}/muteConfigs/{mute_config}\x12Korganizations/{organization}/locations/{location}/muteConfigs/{mute_config}\x12*folders/{folder}/muteConfigs/{mute_config}\x12?folders/{folder}/locations/{location}/muteConfigs/{mute_config}\x12,projects/{project}/muteConfigs/{mute_config}\x12Aprojects/{project}/locations/{location}/muteConfigs/{mute_config}*\x0bmuteConfigs2\nmuteConfigB\xe9\x01\n"com.google.cloud.securitycenter.v2B\x0fMuteConfigProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.mute_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0fMuteConfigProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_MUTECONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MUTECONFIG'].fields_by_name['filter']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_MUTECONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MUTECONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MUTECONFIG'].fields_by_name['most_recent_editor']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['most_recent_editor']._serialized_options = b'\xe0A\x03'
    _globals['_MUTECONFIG'].fields_by_name['type']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_MUTECONFIG'].fields_by_name['expiry_time']._loaded_options = None
    _globals['_MUTECONFIG'].fields_by_name['expiry_time']._serialized_options = b'\xe0A\x01'
    _globals['_MUTECONFIG']._loaded_options = None
    _globals['_MUTECONFIG']._serialized_options = b'\xeaA\xa6\x03\n(securitycenter.googleapis.com/MuteConfig\x126organizations/{organization}/muteConfigs/{mute_config}\x12Korganizations/{organization}/locations/{location}/muteConfigs/{mute_config}\x12*folders/{folder}/muteConfigs/{mute_config}\x12?folders/{folder}/locations/{location}/muteConfigs/{mute_config}\x12,projects/{project}/muteConfigs/{mute_config}\x12Aprojects/{project}/locations/{location}/muteConfigs/{mute_config}*\x0bmuteConfigs2\nmuteConfig'
    _globals['_MUTECONFIG']._serialized_start = 178
    _globals['_MUTECONFIG']._serialized_end = 1030
    _globals['_MUTECONFIG_MUTECONFIGTYPE']._serialized_start = 526
    _globals['_MUTECONFIG_MUTECONFIGTYPE']._serialized_end = 601