"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/transit_preferences.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/maps/routing/v2/transit_preferences.proto\x12\x16google.maps.routing.v2"\xb4\x03\n\x12TransitPreferences\x12Z\n\x14allowed_travel_modes\x18\x01 \x03(\x0e2<.google.maps.routing.v2.TransitPreferences.TransitTravelMode\x12_\n\x12routing_preference\x18\x02 \x01(\x0e2C.google.maps.routing.v2.TransitPreferences.TransitRoutingPreference"r\n\x11TransitTravelMode\x12#\n\x1fTRANSIT_TRAVEL_MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03BUS\x10\x01\x12\n\n\x06SUBWAY\x10\x02\x12\t\n\x05TRAIN\x10\x03\x12\x0e\n\nLIGHT_RAIL\x10\x04\x12\x08\n\x04RAIL\x10\x05"m\n\x18TransitRoutingPreference\x12*\n&TRANSIT_ROUTING_PREFERENCE_UNSPECIFIED\x10\x00\x12\x10\n\x0cLESS_WALKING\x10\x01\x12\x13\n\x0fFEWER_TRANSFERS\x10\x02B\xc9\x01\n\x1acom.google.maps.routing.v2B\x17TransitPreferencesProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.transit_preferences_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x17TransitPreferencesProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_TRANSITPREFERENCES']._serialized_start = 77
    _globals['_TRANSITPREFERENCES']._serialized_end = 513
    _globals['_TRANSITPREFERENCES_TRANSITTRAVELMODE']._serialized_start = 288
    _globals['_TRANSITPREFERENCES_TRANSITTRAVELMODE']._serialized_end = 402
    _globals['_TRANSITPREFERENCES_TRANSITROUTINGPREFERENCE']._serialized_start = 404
    _globals['_TRANSITPREFERENCES_TRANSITROUTINGPREFERENCE']._serialized_end = 513