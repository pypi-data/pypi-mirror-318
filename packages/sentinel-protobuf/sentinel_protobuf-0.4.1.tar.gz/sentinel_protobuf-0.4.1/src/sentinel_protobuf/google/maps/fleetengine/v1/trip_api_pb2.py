"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/v1/trip_api.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.api import routing_pb2 as google_dot_api_dot_routing__pb2
from .....google.maps.fleetengine.v1 import fleetengine_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_fleetengine__pb2
from .....google.maps.fleetengine.v1 import header_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_header__pb2
from .....google.maps.fleetengine.v1 import trips_pb2 as google_dot_maps_dot_fleetengine_dot_v1_dot_trips__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/maps/fleetengine/v1/trip_api.proto\x12\x13maps.fleetengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x18google/api/routing.proto\x1a,google/maps/fleetengine/v1/fleetengine.proto\x1a\'google/maps/fleetengine/v1/header.proto\x1a&google/maps/fleetengine/v1/trips.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc4\x01\n\x11CreateTripRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x127\n\x06parent\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1ffleetengine.googleapis.com/Trip\x12\x14\n\x07trip_id\x18\x05 \x01(\tB\x03\xe0A\x02\x12,\n\x04trip\x18\x04 \x01(\x0b2\x19.maps.fleetengine.v1.TripB\x03\xe0A\x02"\x82\x04\n\x0eGetTripRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x125\n\x04name\x18\x03 \x01(\tB\'\xe0A\x02\xfaA!\n\x1ffleetengine.googleapis.com/Trip\x12+\n\x04view\x18\x0b \x01(\x0e2\x1d.maps.fleetengine.v1.TripView\x12A\n\x1dcurrent_route_segment_version\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12?\n\x1bremaining_waypoints_version\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x11route_format_type\x18\x08 \x01(\x0e2\'.maps.fleetengine.v1.PolylineFormatType\x12I\n%current_route_segment_traffic_version\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n!remaining_waypoints_route_version\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp"\xcd\x02\n\x19ReportBillableTripRequest\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0ccountry_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12@\n\x08platform\x18\x05 \x01(\x0e2..maps.fleetengine.v1.BillingPlatformIdentifier\x12\x13\n\x0brelated_ids\x18\x06 \x03(\t\x12R\n\rsolution_type\x18\x07 \x01(\x0e2;.maps.fleetengine.v1.ReportBillableTripRequest.SolutionType"W\n\x0cSolutionType\x12\x1d\n\x19SOLUTION_TYPE_UNSPECIFIED\x10\x00\x12(\n$ON_DEMAND_RIDESHARING_AND_DELIVERIES\x10\x01"\xbe\x01\n\x11UpdateTripRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12,\n\x04trip\x18\x04 \x01(\x0b2\x19.maps.fleetengine.v1.TripB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xe9\x01\n\x12SearchTripsRequest\x122\n\x06header\x18\x01 \x01(\x0b2".maps.fleetengine.v1.RequestHeader\x12\x13\n\x06parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nvehicle_id\x18\x04 \x01(\t\x12\x19\n\x11active_trips_only\x18\x05 \x01(\x08\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t\x124\n\x11minimum_staleness\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration"X\n\x13SearchTripsResponse\x12(\n\x05trips\x18\x01 \x03(\x0b2\x19.maps.fleetengine.v1.Trip\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd0\x07\n\x0bTripService\x12\xa8\x01\n\nCreateTrip\x12&.maps.fleetengine.v1.CreateTripRequest\x1a\x19.maps.fleetengine.v1.Trip"W\x82\xd3\xe4\x93\x02&"\x1e/v1/{parent=providers/*}/trips:\x04trip\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\x9a\x01\n\x07GetTrip\x12#.maps.fleetengine.v1.GetTripRequest\x1a\x19.maps.fleetengine.v1.Trip"O\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=providers/*/trips/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xbf\x01\n\x12ReportBillableTrip\x12..maps.fleetengine.v1.ReportBillableTripRequest\x1a\x16.google.protobuf.Empty"a\x82\xd3\xe4\x93\x022"-/v1/{name=providers/*/billableTrips/*}:report:\x01*\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x12\xbd\x01\n\x0bSearchTrips\x12\'.maps.fleetengine.v1.SearchTripsRequest\x1a(.maps.fleetengine.v1.SearchTripsResponse"[\x82\xd3\xe4\x93\x02*"%/v1/{parent=providers/*}/trips:search:\x01*\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}\x12\xa6\x01\n\nUpdateTrip\x12&.maps.fleetengine.v1.UpdateTripRequest\x1a\x19.maps.fleetengine.v1.Trip"U\x82\xd3\xe4\x93\x02&\x1a\x1e/v1/{name=providers/*/trips/*}:\x04trip\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}\x1aN\xcaA\x1afleetengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd3\x01\n\x1ecom.google.maps.fleetengine.v1B\x07TripApiP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.v1.trip_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.maps.fleetengine.v1B\x07TripApiP\x01ZFcloud.google.com/go/maps/fleetengine/apiv1/fleetenginepb;fleetenginepb\xa2\x02\x03CFE\xaa\x02\x1aGoogle.Maps.FleetEngine.V1\xca\x02\x1aGoogle\\Maps\\FleetEngine\\V1\xea\x02\x1dGoogle::Maps::FleetEngine::V1'
    _globals['_CREATETRIPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETRIPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1ffleetengine.googleapis.com/Trip'
    _globals['_CREATETRIPREQUEST'].fields_by_name['trip_id']._loaded_options = None
    _globals['_CREATETRIPREQUEST'].fields_by_name['trip_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETRIPREQUEST'].fields_by_name['trip']._loaded_options = None
    _globals['_CREATETRIPREQUEST'].fields_by_name['trip']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1ffleetengine.googleapis.com/Trip'
    _globals['_REPORTBILLABLETRIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REPORTBILLABLETRIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTBILLABLETRIPREQUEST'].fields_by_name['country_code']._loaded_options = None
    _globals['_REPORTBILLABLETRIPREQUEST'].fields_by_name['country_code']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATETRIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRIPREQUEST'].fields_by_name['trip']._loaded_options = None
    _globals['_UPDATETRIPREQUEST'].fields_by_name['trip']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRIPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETRIPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHTRIPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHTRIPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_TRIPSERVICE']._loaded_options = None
    _globals['_TRIPSERVICE']._serialized_options = b'\xcaA\x1afleetengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TRIPSERVICE'].methods_by_name['CreateTrip']._loaded_options = None
    _globals['_TRIPSERVICE'].methods_by_name['CreateTrip']._serialized_options = b'\x82\xd3\xe4\x93\x02&"\x1e/v1/{parent=providers/*}/trips:\x04trip\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_TRIPSERVICE'].methods_by_name['GetTrip']._loaded_options = None
    _globals['_TRIPSERVICE'].methods_by_name['GetTrip']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=providers/*/trips/*}\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_TRIPSERVICE'].methods_by_name['ReportBillableTrip']._loaded_options = None
    _globals['_TRIPSERVICE'].methods_by_name['ReportBillableTrip']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/v1/{name=providers/*/billableTrips/*}:report:\x01*\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_TRIPSERVICE'].methods_by_name['SearchTrips']._loaded_options = None
    _globals['_TRIPSERVICE'].methods_by_name['SearchTrips']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v1/{parent=providers/*}/trips:search:\x01*\x8a\xd3\xe4\x93\x02%\x12#\n\x06parent\x12\x19{provider_id=providers/*}'
    _globals['_TRIPSERVICE'].methods_by_name['UpdateTrip']._loaded_options = None
    _globals['_TRIPSERVICE'].methods_by_name['UpdateTrip']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x1a\x1e/v1/{name=providers/*/trips/*}:\x04trip\x8a\xd3\xe4\x93\x02#\x12!\n\x04name\x12\x19{provider_id=providers/*}'
    _globals['_CREATETRIPREQUEST']._serialized_start = 463
    _globals['_CREATETRIPREQUEST']._serialized_end = 659
    _globals['_GETTRIPREQUEST']._serialized_start = 662
    _globals['_GETTRIPREQUEST']._serialized_end = 1176
    _globals['_REPORTBILLABLETRIPREQUEST']._serialized_start = 1179
    _globals['_REPORTBILLABLETRIPREQUEST']._serialized_end = 1512
    _globals['_REPORTBILLABLETRIPREQUEST_SOLUTIONTYPE']._serialized_start = 1425
    _globals['_REPORTBILLABLETRIPREQUEST_SOLUTIONTYPE']._serialized_end = 1512
    _globals['_UPDATETRIPREQUEST']._serialized_start = 1515
    _globals['_UPDATETRIPREQUEST']._serialized_end = 1705
    _globals['_SEARCHTRIPSREQUEST']._serialized_start = 1708
    _globals['_SEARCHTRIPSREQUEST']._serialized_end = 1941
    _globals['_SEARCHTRIPSRESPONSE']._serialized_start = 1943
    _globals['_SEARCHTRIPSRESPONSE']._serialized_end = 2031
    _globals['_TRIPSERVICE']._serialized_start = 2034
    _globals['_TRIPSERVICE']._serialized_end = 3010