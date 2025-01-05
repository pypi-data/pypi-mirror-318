"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/channel.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/eventarc/v1/channel.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcb\x04\n\x07Channel\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x1b\n\x0cpubsub_topic\x18\x08 \x01(\tB\x03\xe0A\x03H\x00\x12;\n\x05state\x18\t \x01(\x0e2\'.google.cloud.eventarc.v1.Channel.StateB\x03\xe0A\x03\x12\x1d\n\x10activation_token\x18\n \x01(\tB\x03\xe0A\x03\x12?\n\x0fcrypto_key_name\x18\x0b \x01(\tB&\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12\x1a\n\rsatisfies_pzs\x18\x0c \x01(\x08B\x03\xe0A\x03"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03:s\xeaAp\n\x1feventarc.googleapis.com/Channel\x12:projects/{project}/locations/{location}/channels/{channel}*\x08channels2\x07channelB\x0b\n\ttransportB\xbc\x01\n\x1ccom.google.cloud.eventarc.v1B\x0cChannelProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.channel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x0cChannelProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1'
    _globals['_CHANNEL'].fields_by_name['name']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNEL'].fields_by_name['uid']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['pubsub_topic']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['pubsub_topic']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['state']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['activation_token']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['activation_token']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['crypto_key_name']._serialized_options = b'\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_CHANNEL'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL']._loaded_options = None
    _globals['_CHANNEL']._serialized_options = b'\xeaAp\n\x1feventarc.googleapis.com/Channel\x12:projects/{project}/locations/{location}/channels/{channel}*\x08channels2\x07channel'
    _globals['_CHANNEL']._serialized_start = 162
    _globals['_CHANNEL']._serialized_end = 749
    _globals['_CHANNEL_STATE']._serialized_start = 550
    _globals['_CHANNEL_STATE']._serialized_end = 619