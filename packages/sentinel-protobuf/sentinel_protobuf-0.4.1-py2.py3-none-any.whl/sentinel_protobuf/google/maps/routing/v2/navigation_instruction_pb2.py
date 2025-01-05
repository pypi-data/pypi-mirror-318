"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/navigation_instruction.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routing.v2 import maneuver_pb2 as google_dot_maps_dot_routing_dot_v2_dot_maneuver__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/maps/routing/v2/navigation_instruction.proto\x12\x16google.maps.routing.v2\x1a%google/maps/routing/v2/maneuver.proto"a\n\x15NavigationInstruction\x122\n\x08maneuver\x18\x01 \x01(\x0e2 .google.maps.routing.v2.Maneuver\x12\x14\n\x0cinstructions\x18\x02 \x01(\tB\xcc\x01\n\x1acom.google.maps.routing.v2B\x1aNavigationInstructionProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.navigation_instruction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x1aNavigationInstructionProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_NAVIGATIONINSTRUCTION']._serialized_start = 118
    _globals['_NAVIGATIONINSTRUCTION']._serialized_end = 215