"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/channel_connection.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/eventarc/v1/channel_connection.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x03\n\x11ChannelConnection\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x128\n\x07channel\x18\x05 \x01(\tB\'\xe0A\x02\xfaA!\n\x1feventarc.googleapis.com/Channel\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1d\n\x10activation_token\x18\x08 \x01(\tB\x03\xe0A\x04:\xa7\x01\xeaA\xa3\x01\n)eventarc.googleapis.com/ChannelConnection\x12Oprojects/{project}/locations/{location}/channelConnections/{channel_connection}*\x12channelConnections2\x11channelConnectionB\xc6\x01\n\x1ccom.google.cloud.eventarc.v1B\x16ChannelConnectionProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.channel_connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x16ChannelConnectionProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1'
    _globals['_CHANNELCONNECTION'].fields_by_name['name']._loaded_options = None
    _globals['_CHANNELCONNECTION'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELCONNECTION'].fields_by_name['uid']._loaded_options = None
    _globals['_CHANNELCONNECTION'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELCONNECTION'].fields_by_name['channel']._loaded_options = None
    _globals['_CHANNELCONNECTION'].fields_by_name['channel']._serialized_options = b'\xe0A\x02\xfaA!\n\x1feventarc.googleapis.com/Channel'
    _globals['_CHANNELCONNECTION'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHANNELCONNECTION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELCONNECTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CHANNELCONNECTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELCONNECTION'].fields_by_name['activation_token']._loaded_options = None
    _globals['_CHANNELCONNECTION'].fields_by_name['activation_token']._serialized_options = b'\xe0A\x04'
    _globals['_CHANNELCONNECTION']._loaded_options = None
    _globals['_CHANNELCONNECTION']._serialized_options = b'\xeaA\xa3\x01\n)eventarc.googleapis.com/ChannelConnection\x12Oprojects/{project}/locations/{location}/channelConnections/{channel_connection}*\x12channelConnections2\x11channelConnection'
    _globals['_CHANNELCONNECTION']._serialized_start = 173
    _globals['_CHANNELCONNECTION']._serialized_end = 596