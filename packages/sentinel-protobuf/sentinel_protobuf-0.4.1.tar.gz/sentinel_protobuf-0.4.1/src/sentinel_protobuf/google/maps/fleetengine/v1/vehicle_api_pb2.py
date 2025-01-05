"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/v1/vehicle_api.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.api import routing_pb2 as google_dot_api_dot_routing__pb2
from .....google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from .....google.maps.fleetengine.v1 import fleetengine_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_fleetengine__pb2
from .....google.maps.fleetengine.v1 import header_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_header__pb2
from .....google.maps.fleetengine.v1 import vehicles_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_vehicles__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/maps/fleetengine/v1/vehicle_api.proto\x12\x13maps.fleetengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x18google/api/routing.proto\x1a\x1egoogle/geo/type/viewport.proto\x1a,google/maps/fleetengine/v1/fleetengine.proto\x1a\'google/maps/fleetengine/v1/header.proto\x1a)google/maps/fleetengine/v1/vehicles.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xac\x01\n\x14CreateVehicleRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x13\n\x06parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\nvehicle_id\x18\x04 \x01(\tB\x03\xe0A\x02\x122\n\x07vehicle\x18\x05 \x01(\x0b2\x1c.maps.fleetengine.v1.VehicleB\x03\xe0A\x02"\xfb\x01\n\x11GetVehicleRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x128\n\x04name\x18\x03 \x01(\tB*\xe0A\x02\xfaA$\n"fleetengine.googleapis.com/Vehicle\x12A\n\x1dcurrent_route_segment_version\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x125\n\x11waypoints_version\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xc7\x01\n\x14UpdateVehicleRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x122\n\x07vehicle\x18\x04 \x01(\x0b2\x1c.maps.fleetengine.v1.VehicleB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xa7\x01\n\x1eUpdateVehicleAttributesRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12>\n\nattributes\x18\x04 \x03(\x0b2%.maps.fleetengine.v1.VehicleAttributeB\x03\xe0A\x02"a\n\x1fUpdateVehicleAttributesResponse\x12>\n\nattributes\x18\x01 \x03(\x0b2%.maps.fleetengine.v1.VehicleAttributeB\x03\xe0A\x02"\xc6\t\n\x15SearchVehiclesRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x13\n\x06parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12@\n\x0cpickup_point\x18\x04 \x01(\x0b2%.maps.fleetengine.v1.TerminalLocationB\x03\xe0A\x02\x12<\n\rdropoff_point\x18\x05 \x01(\x0b2%.maps.fleetengine.v1.TerminalLocation\x12!\n\x14pickup_radius_meters\x18\x06 \x01(\x05B\x03\xe0A\x02\x12\x12\n\x05count\x18\x07 \x01(\x05B\x03\xe0A\x02\x12\x1d\n\x10minimum_capacity\x18\x08 \x01(\x05B\x03\xe0A\x02\x126\n\ntrip_types\x18\t \x03(\x0e2\x1d.maps.fleetengine.v1.TripTypeB\x03\xe0A\x02\x124\n\x11maximum_staleness\x18\n \x01(\x0b2\x19.google.protobuf.Duration\x12D\n\rvehicle_types\x18\x0e \x03(\x0b2(.maps.fleetengine.v1.Vehicle.VehicleTypeB\x03\xe0A\x02\x12B\n\x13required_attributes\x18\x0c \x03(\x0b2%.maps.fleetengine.v1.VehicleAttribute\x12M\n\x1arequired_one_of_attributes\x18\x0f \x03(\x0b2).maps.fleetengine.v1.VehicleAttributeList\x12Q\n\x1erequired_one_of_attribute_sets\x18\x14 \x03(\x0b2).maps.fleetengine.v1.VehicleAttributeList\x12S\n\x08order_by\x18\r \x01(\x0e2<.maps.fleetengine.v1.SearchVehiclesRequest.VehicleMatchOrderB\x03\xe0A\x02\x12\x1c\n\x14include_back_to_back\x18\x12 \x01(\x08\x12\x0f\n\x07trip_id\x18\x13 \x01(\t\x12]\n\x15current_trips_present\x18\x15 \x01(\x0e2>.maps.fleetengine.v1.SearchVehiclesRequest.CurrentTripsPresent\x12\x13\n\x06filter\x18\x16 \x01(\tB\x03\xe0A\x01"\xaa\x01\n\x11VehicleMatchOrder\x12\x1f\n\x1bUNKNOWN_VEHICLE_MATCH_ORDER\x10\x00\x12\x14\n\x10PICKUP_POINT_ETA\x10\x01\x12\x19\n\x15PICKUP_POINT_DISTANCE\x10\x02\x12\x15\n\x11DROPOFF_POINT_ETA\x10\x03\x12"\n\x1ePICKUP_POINT_STRAIGHT_DISTANCE\x10\x04\x12\x08\n\x04COST\x10\x05"O\n\x13CurrentTripsPresent\x12%\n!CURRENT_TRIPS_PRESENT_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x07\n\x03ANY\x10\x02"L\n\x16SearchVehiclesResponse\x122\n\x07matches\x18\x01 \x03(\x0b2!.maps.fleetengine.v1.VehicleMatch"\xfe\x04\n\x13ListVehiclesRequest\x122\n\x06header\x18\x0c \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x125\n\x10minimum_capacity\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int32Value\x121\n\ntrip_types\x18\x07 \x03(\x0e2\x1d.maps.fleetengine.v1.TripType\x124\n\x11maximum_staleness\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12W\n\x17vehicle_type_categories\x18\t \x03(\x0e21.maps.fleetengine.v1.Vehicle.VehicleType.CategoryB\x03\xe0A\x02\x12\x1b\n\x13required_attributes\x18\n \x03(\t\x12"\n\x1arequired_one_of_attributes\x18\r \x03(\t\x12&\n\x1erequired_one_of_attribute_sets\x18\x0f \x03(\t\x128\n\rvehicle_state\x18\x0b \x01(\x0e2!.maps.fleetengine.v1.VehicleState\x12\x14\n\x0con_trip_only\x18\x0e \x01(\x08\x12\x13\n\x06filter\x18\x10 \x01(\tB\x03\xe0A\x01\x120\n\x08viewport\x18\x11 \x01(\x0b2\x19.google.geo.type.ViewportB\x03\xe0A\x01"x\n\x14ListVehiclesResponse\x12.\n\x08vehicles\x18\x01 \x03(\x0b2\x1c.maps.fleetengine.v1.Vehicle\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x17\n\ntotal_size\x18\x03 \x01(\x03B\x03\xe0A\x02"Y\n\x08Waypoint\x12$\n\x07lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12\'\n\x03eta\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xfe\x06\n\x0cVehicleMatch\x122\n\x07vehicle\x18\x01 \x01(\x0b2\x1c.maps.fleetengine.v1.VehicleB\x03\xe0A\x02\x126\n\x12vehicle_pickup_eta\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12C\n\x1evehicle_pickup_distance_meters\x18\x03 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12V\n,vehicle_pickup_straight_line_distance_meters\x18\x0b \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x02\x127\n\x13vehicle_dropoff_eta\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12N\n)vehicle_pickup_to_dropoff_distance_meters\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int32Value\x125\n\ttrip_type\x18\x06 \x01(\x0e2\x1d.maps.fleetengine.v1.TripTypeB\x03\xe0A\x02\x12>\n\x17vehicle_trips_waypoints\x18\x07 \x03(\x0b2\x1d.maps.fleetengine.v1.Waypoint\x12N\n\x12vehicle_match_type\x18\x08 \x01(\x0e22.maps.fleetengine.v1.VehicleMatch.VehicleMatchType\x12Z\n\x14requested_ordered_by\x18\t \x01(\x0e2<.maps.fleetengine.v1.SearchVehiclesRequest.VehicleMatchOrder\x12P\n\nordered_by\x18\n \x01(\x0e2<.maps.fleetengine.v1.SearchVehiclesRequest.VehicleMatchOrder"g\n\x10VehicleMatchType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tEXCLUSIVE\x10\x01\x12\x10\n\x0cBACK_TO_BACK\x10\x02\x12\x0b\n\x07CARPOOL\x10\x03\x12\x18\n\x14CARPOOL_BACK_TO_BACK\x10\x04"Q\n\x14VehicleAttributeList\x129\n\nattributes\x18\x01 \x03(\x0b2%.maps.fleetengine.v1.VehicleAttribute2\xf2\t\n\x0eVehicleService\x12\xb7\x01\n\rCreateVehicle\x12).maps.fleetengine.v1.CreateVehicleRequest\x1a\x1c.maps.fleetengine.v1.Vehicle"]\x82\xd3\xe4\x93\x02,"!/v1/{parent=providers/*}/vehicles:\x07vehicle\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xa6\x01\n\nGetVehicle\x12&.maps.fleetengine.v1.GetVehicleRequest\x1a\x1c.maps.fleetengine.v1.Vehicle"R\x82\xd3\xe4\x93\x02#\x12!/v1/{name=providers/*/vehicles/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xb5\x01\n\rUpdateVehicle\x12).maps.fleetengine.v1.UpdateVehicleRequest\x1a\x1c.maps.fleetengine.v1.Vehicle"[\x82\xd3\xe4\x93\x02,\x1a!/v1/{name=providers/*/vehicles/*}:\x07vehicle\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xec\x01\n\x17UpdateVehicleAttributes\x123.maps.fleetengine.v1.UpdateVehicleAttributesRequest\x1a4.maps.fleetengine.v1.UpdateVehicleAttributesResponse"f\x82\xd3\xe4\x93\x027"2/v1/{name=providers/*/vehicles/*}:updateAttributes:\x01*\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xb9\x01\n\x0cListVehicles\x12(.maps.fleetengine.v1.ListVehiclesRequest\x1a).maps.fleetengine.v1.ListVehiclesResponse"T\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=providers/*}/vehicles\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xc9\x01\n\x0eSearchVehicles\x12*.maps.fleetengine.v1.SearchVehiclesRequest\x1a+.maps.fleetengine.v1.SearchVehiclesResponse"^\x82\xd3\xe4\x93\x02-"(/v1/{parent=providers/*}/vehicles:search:\x01*\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x1aN\xcaA\x1afleetengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd6\x01\n\x1ecom.google.maps.fleetengine.v1B\nVehicleApiP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.v1.vehicle_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.fleetengine.v1B\nVehicleApiP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1'
    _globals['_CREATEVEHICLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEVEHICLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEVEHICLEREQUEST'].fields_by_name['vehicle_id']._loaded_options = None
    _globals['_CREATEVEHICLEREQUEST'].fields_by_name['vehicle_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEVEHICLEREQUEST'].fields_by_name['vehicle']._loaded_options = None
    _globals['_CREATEVEHICLEREQUEST'].fields_by_name['vehicle']._serialized_options = b'\xe0A\x02'
    _globals['_GETVEHICLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVEHICLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"fleetengine.googleapis.com/Vehicle'
    _globals['_UPDATEVEHICLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEVEHICLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVEHICLEREQUEST'].fields_by_name['vehicle']._loaded_options = None
    _globals['_UPDATEVEHICLEREQUEST'].fields_by_name['vehicle']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVEHICLEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEVEHICLEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVEHICLEATTRIBUTESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEVEHICLEATTRIBUTESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVEHICLEATTRIBUTESREQUEST'].fields_by_name['attributes']._loaded_options = None
    _globals['_UPDATEVEHICLEATTRIBUTESREQUEST'].fields_by_name['attributes']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVEHICLEATTRIBUTESRESPONSE'].fields_by_name['attributes']._loaded_options = None
    _globals['_UPDATEVEHICLEATTRIBUTESRESPONSE'].fields_by_name['attributes']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['pickup_point']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['pickup_point']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['pickup_radius_meters']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['pickup_radius_meters']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['count']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['count']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['minimum_capacity']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['minimum_capacity']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['trip_types']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['trip_types']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['vehicle_types']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['vehicle_types']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_SEARCHVEHICLESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['vehicle_type_categories']._loaded_options = None
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['vehicle_type_categories']._serialized_options = b'\xe0A\x02'
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['viewport']._loaded_options = None
    _globals['_LISTVEHICLESREQUEST'].fields_by_name['viewport']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVEHICLESRESPONSE'].fields_by_name['total_size']._loaded_options = None
    _globals['_LISTVEHICLESRESPONSE'].fields_by_name['total_size']._serialized_options = b'\xe0A\x02'
    _globals['_VEHICLEMATCH'].fields_by_name['vehicle']._loaded_options = None
    _globals['_VEHICLEMATCH'].fields_by_name['vehicle']._serialized_options = b'\xe0A\x02'
    _globals['_VEHICLEMATCH'].fields_by_name['vehicle_pickup_straight_line_distance_meters']._loaded_options = None
    _globals['_VEHICLEMATCH'].fields_by_name['vehicle_pickup_straight_line_distance_meters']._serialized_options = b'\xe0A\x02'
    _globals['_VEHICLEMATCH'].fields_by_name['trip_type']._loaded_options = None
    _globals['_VEHICLEMATCH'].fields_by_name['trip_type']._serialized_options = b'\xe0A\x02'
    _globals['_VEHICLESERVICE']._loaded_options = None
    _globals['_VEHICLESERVICE']._serialized_options = b'\xcaA\x1afleetengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VEHICLESERVICE'].methods_by_name['CreateVehicle']._loaded_options = None
    _globals['_VEHICLESERVICE'].methods_by_name['CreateVehicle']._serialized_options = b'\x82\xd3\xe4\x93\x02,"!/v1/{parent=providers/*}/vehicles:\x07vehicle\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_VEHICLESERVICE'].methods_by_name['GetVehicle']._loaded_options = None
    _globals['_VEHICLESERVICE'].methods_by_name['GetVehicle']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/v1/{name=providers/*/vehicles/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_VEHICLESERVICE'].methods_by_name['UpdateVehicle']._loaded_options = None
    _globals['_VEHICLESERVICE'].methods_by_name['UpdateVehicle']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a!/v1/{name=providers/*/vehicles/*}:\x07vehicle\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_VEHICLESERVICE'].methods_by_name['UpdateVehicleAttributes']._loaded_options = None
    _globals['_VEHICLESERVICE'].methods_by_name['UpdateVehicleAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x027"2/v1/{name=providers/*/vehicles/*}:updateAttributes:\x01*\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_VEHICLESERVICE'].methods_by_name['ListVehicles']._loaded_options = None
    _globals['_VEHICLESERVICE'].methods_by_name['ListVehicles']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=providers/*}/vehicles\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_VEHICLESERVICE'].methods_by_name['SearchVehicles']._loaded_options = None
    _globals['_VEHICLESERVICE'].methods_by_name['SearchVehicles']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/v1/{parent=providers/*}/vehicles:search:\x01*\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_CREATEVEHICLEREQUEST']._serialized_start = 530
    _globals['_CREATEVEHICLEREQUEST']._serialized_end = 702
    _globals['_GETVEHICLEREQUEST']._serialized_start = 705
    _globals['_GETVEHICLEREQUEST']._serialized_end = 956
    _globals['_UPDATEVEHICLEREQUEST']._serialized_start = 959
    _globals['_UPDATEVEHICLEREQUEST']._serialized_end = 1158
    _globals['_UPDATEVEHICLEATTRIBUTESREQUEST']._serialized_start = 1161
    _globals['_UPDATEVEHICLEATTRIBUTESREQUEST']._serialized_end = 1328
    _globals['_UPDATEVEHICLEATTRIBUTESRESPONSE']._serialized_start = 1330
    _globals['_UPDATEVEHICLEATTRIBUTESRESPONSE']._serialized_end = 1427
    _globals['_SEARCHVEHICLESREQUEST']._serialized_start = 1430
    _globals['_SEARCHVEHICLESREQUEST']._serialized_end = 2652
    _globals['_SEARCHVEHICLESREQUEST_VEHICLEMATCHORDER']._serialized_start = 2401
    _globals['_SEARCHVEHICLESREQUEST_VEHICLEMATCHORDER']._serialized_end = 2571
    _globals['_SEARCHVEHICLESREQUEST_CURRENTTRIPSPRESENT']._serialized_start = 2573
    _globals['_SEARCHVEHICLESREQUEST_CURRENTTRIPSPRESENT']._serialized_end = 2652
    _globals['_SEARCHVEHICLESRESPONSE']._serialized_start = 2654
    _globals['_SEARCHVEHICLESRESPONSE']._serialized_end = 2730
    _globals['_LISTVEHICLESREQUEST']._serialized_start = 2733
    _globals['_LISTVEHICLESREQUEST']._serialized_end = 3371
    _globals['_LISTVEHICLESRESPONSE']._serialized_start = 3373
    _globals['_LISTVEHICLESRESPONSE']._serialized_end = 3493
    _globals['_WAYPOINT']._serialized_start = 3495
    _globals['_WAYPOINT']._serialized_end = 3584
    _globals['_VEHICLEMATCH']._serialized_start = 3587
    _globals['_VEHICLEMATCH']._serialized_end = 4481
    _globals['_VEHICLEMATCH_VEHICLEMATCHTYPE']._serialized_start = 4378
    _globals['_VEHICLEMATCH_VEHICLEMATCHTYPE']._serialized_end = 4481
    _globals['_VEHICLEATTRIBUTELIST']._serialized_start = 4483
    _globals['_VEHICLEATTRIBUTELIST']._serialized_end = 4564
    _globals['_VEHICLESERVICE']._serialized_start = 4567
    _globals['_VEHICLESERVICE']._serialized_end = 5833