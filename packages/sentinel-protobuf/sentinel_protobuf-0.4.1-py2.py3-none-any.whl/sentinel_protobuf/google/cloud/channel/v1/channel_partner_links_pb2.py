"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/channel_partner_links.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.channel.v1 import common_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/channel/v1/channel_partner_links.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/channel/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8f\x04\n\x12ChannelPartnerLink\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\'\n\x1areseller_cloud_identity_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\nlink_state\x18\x03 \x01(\x0e20.google.cloud.channel.v1.ChannelPartnerLinkStateB\x03\xe0A\x02\x12\x1c\n\x0finvite_link_uri\x18\x04 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\tpublic_id\x18\x07 \x01(\tB\x03\xe0A\x03\x12\\\n#channel_partner_cloud_identity_info\x18\x08 \x01(\x0b2*.google.cloud.channel.v1.CloudIdentityInfoB\x03\xe0A\x03:r\xeaAo\n.cloudchannel.googleapis.com/ChannelPartnerLink\x12=accounts/{account}/channelPartnerLinks/{channel_partner_link}*>\n\x16ChannelPartnerLinkView\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02*z\n\x17ChannelPartnerLinkState\x12*\n&CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INVITED\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0b\n\x07REVOKED\x10\x03\x12\r\n\tSUSPENDED\x10\x04Bp\n\x1bcom.google.cloud.channel.v1B\x18ChannelPartnerLinksProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.channel_partner_links_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x18ChannelPartnerLinksProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['name']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['reseller_cloud_identity_id']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['reseller_cloud_identity_id']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['link_state']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['link_state']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['invite_link_uri']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['invite_link_uri']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['update_time']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['public_id']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['public_id']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERLINK'].fields_by_name['channel_partner_cloud_identity_info']._loaded_options = None
    _globals['_CHANNELPARTNERLINK'].fields_by_name['channel_partner_cloud_identity_info']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERLINK']._loaded_options = None
    _globals['_CHANNELPARTNERLINK']._serialized_options = b'\xeaAo\n.cloudchannel.googleapis.com/ChannelPartnerLink\x12=accounts/{account}/channelPartnerLinks/{channel_partner_link}'
    _globals['_CHANNELPARTNERLINKVIEW']._serialized_start = 741
    _globals['_CHANNELPARTNERLINKVIEW']._serialized_end = 803
    _globals['_CHANNELPARTNERLINKSTATE']._serialized_start = 805
    _globals['_CHANNELPARTNERLINKSTATE']._serialized_end = 927
    _globals['_CHANNELPARTNERLINK']._serialized_start = 212
    _globals['_CHANNELPARTNERLINK']._serialized_end = 739