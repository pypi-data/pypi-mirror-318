"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/fallback_info.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/maps/routing/v2/fallback_info.proto\x12\x16google.maps.routing.v2"\x89\x01\n\x0cFallbackInfo\x12A\n\x0crouting_mode\x18\x01 \x01(\x0e2+.google.maps.routing.v2.FallbackRoutingMode\x126\n\x06reason\x18\x02 \x01(\x0e2&.google.maps.routing.v2.FallbackReason*Y\n\x0eFallbackReason\x12\x1f\n\x1bFALLBACK_REASON_UNSPECIFIED\x10\x00\x12\x10\n\x0cSERVER_ERROR\x10\x01\x12\x14\n\x10LATENCY_EXCEEDED\x10\x02*v\n\x13FallbackRoutingMode\x12%\n!FALLBACK_ROUTING_MODE_UNSPECIFIED\x10\x00\x12\x1c\n\x18FALLBACK_TRAFFIC_UNAWARE\x10\x01\x12\x1a\n\x16FALLBACK_TRAFFIC_AWARE\x10\x02B\xc3\x01\n\x1acom.google.maps.routing.v2B\x11FallbackInfoProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.fallback_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x11FallbackInfoProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_FALLBACKREASON']._serialized_start = 210
    _globals['_FALLBACKREASON']._serialized_end = 299
    _globals['_FALLBACKROUTINGMODE']._serialized_start = 301
    _globals['_FALLBACKROUTINGMODE']._serialized_end = 419
    _globals['_FALLBACKINFO']._serialized_start = 71
    _globals['_FALLBACKINFO']._serialized_end = 208