"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/google_channel_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/eventarc/v1/google_channel_config.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x02\n\x13GoogleChannelConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x0fcrypto_key_name\x18\x07 \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey:\x82\x01\xeaA\x7f\n+eventarc.googleapis.com/GoogleChannelConfig\x12;projects/{project}/locations/{location}/googleChannelConfig2\x13googleChannelConfigB\xc3\x02\n\x1ccom.google.cloud.eventarc.v1B\x18GoogleChannelConfigProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.google_channel_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x18GoogleChannelConfigProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}'
    _globals['_GOOGLECHANNELCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_GOOGLECHANNELCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLECHANNELCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_GOOGLECHANNELCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLECHANNELCONFIG'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_GOOGLECHANNELCONFIG'].fields_by_name['crypto_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_GOOGLECHANNELCONFIG']._loaded_options = None
    _globals['_GOOGLECHANNELCONFIG']._serialized_options = b'\xeaA\x7f\n+eventarc.googleapis.com/GoogleChannelConfig\x12;projects/{project}/locations/{location}/googleChannelConfig2\x13googleChannelConfig'
    _globals['_GOOGLECHANNELCONFIG']._serialized_start = 176
    _globals['_GOOGLECHANNELCONFIG']._serialized_end = 471