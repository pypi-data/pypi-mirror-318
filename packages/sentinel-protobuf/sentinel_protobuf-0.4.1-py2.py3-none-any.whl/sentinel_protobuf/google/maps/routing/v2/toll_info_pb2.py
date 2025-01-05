"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/toll_info.proto')
_sym_db = _symbol_database.Default()
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/maps/routing/v2/toll_info.proto\x12\x16google.maps.routing.v2\x1a\x17google/type/money.proto"7\n\x08TollInfo\x12+\n\x0festimated_price\x18\x01 \x03(\x0b2\x12.google.type.MoneyB\xc2\x01\n\x1acom.google.maps.routing.v2B\rTollInfoProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xf8\x01\x01\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.toll_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\rTollInfoProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xf8\x01\x01\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_TOLLINFO']._serialized_start = 91
    _globals['_TOLLINFO']._serialized_end = 146