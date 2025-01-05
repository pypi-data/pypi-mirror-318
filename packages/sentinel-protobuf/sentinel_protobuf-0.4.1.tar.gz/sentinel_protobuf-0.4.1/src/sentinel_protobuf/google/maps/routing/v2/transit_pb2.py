"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/routing/v2/transit.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.routing.v2 import location_pb2 as google_dot_maps_dot_routing_dot_v2_dot_location__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/maps/routing/v2/transit.proto\x12\x16google.maps.routing.v2\x1a%google/maps/routing/v2/location.proto\x1a google/type/localized_text.proto"@\n\rTransitAgency\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cphone_number\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t"\xe3\x01\n\x0bTransitLine\x127\n\x08agencies\x18\x01 \x03(\x0b2%.google.maps.routing.v2.TransitAgency\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\r\n\x05color\x18\x04 \x01(\t\x12\x10\n\x08icon_uri\x18\x05 \x01(\t\x12\x12\n\nname_short\x18\x06 \x01(\t\x12\x12\n\ntext_color\x18\x07 \x01(\t\x127\n\x07vehicle\x18\x08 \x01(\x0b2&.google.maps.routing.v2.TransitVehicle"O\n\x0bTransitStop\x12\x0c\n\x04name\x18\x01 \x01(\t\x122\n\x08location\x18\x02 \x01(\x0b2 .google.maps.routing.v2.Location"\xfd\x03\n\x0eTransitVehicle\x12(\n\x04name\x18\x01 \x01(\x0b2\x1a.google.type.LocalizedText\x12G\n\x04type\x18\x02 \x01(\x0e29.google.maps.routing.v2.TransitVehicle.TransitVehicleType\x12\x10\n\x08icon_uri\x18\x03 \x01(\t\x12\x16\n\x0elocal_icon_uri\x18\x04 \x01(\t"\xcd\x02\n\x12TransitVehicleType\x12$\n TRANSIT_VEHICLE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03BUS\x10\x01\x12\r\n\tCABLE_CAR\x10\x02\x12\x12\n\x0eCOMMUTER_TRAIN\x10\x03\x12\t\n\x05FERRY\x10\x04\x12\r\n\tFUNICULAR\x10\x05\x12\x10\n\x0cGONDOLA_LIFT\x10\x06\x12\x0e\n\nHEAVY_RAIL\x10\x07\x12\x14\n\x10HIGH_SPEED_TRAIN\x10\x08\x12\x11\n\rINTERCITY_BUS\x10\t\x12\x17\n\x13LONG_DISTANCE_TRAIN\x10\n\x12\x0e\n\nMETRO_RAIL\x10\x0b\x12\x0c\n\x08MONORAIL\x10\x0c\x12\t\n\x05OTHER\x10\r\x12\x08\n\x04RAIL\x10\x0e\x12\x0e\n\nSHARE_TAXI\x10\x0f\x12\n\n\x06SUBWAY\x10\x10\x12\x08\n\x04TRAM\x10\x11\x12\x0e\n\nTROLLEYBUS\x10\x12B\xbe\x01\n\x1acom.google.maps.routing.v2B\x0cTransitProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.transit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x0cTransitProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_TRANSITAGENCY']._serialized_start = 137
    _globals['_TRANSITAGENCY']._serialized_end = 201
    _globals['_TRANSITLINE']._serialized_start = 204
    _globals['_TRANSITLINE']._serialized_end = 431
    _globals['_TRANSITSTOP']._serialized_start = 433
    _globals['_TRANSITSTOP']._serialized_end = 512
    _globals['_TRANSITVEHICLE']._serialized_start = 515
    _globals['_TRANSITVEHICLE']._serialized_end = 1024
    _globals['_TRANSITVEHICLE_TRANSITVEHICLETYPE']._serialized_start = 691
    _globals['_TRANSITVEHICLE_TRANSITVEHICLETYPE']._serialized_end = 1024