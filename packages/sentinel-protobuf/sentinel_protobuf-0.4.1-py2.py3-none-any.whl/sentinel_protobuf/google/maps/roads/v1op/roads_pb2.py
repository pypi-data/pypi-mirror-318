"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/roads/v1op/roads.proto')
_sym_db = _symbol_database.Default()
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/maps/roads/v1op/roads.proto\x12\x16google.maps.roads.v1op\x1a\x17google/api/client.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\x82\x01\n\x12SnapToRoadsRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x13\n\x0binterpolate\x18\x02 \x01(\x08\x12\x10\n\x08asset_id\x18\x03 \x01(\t\x127\n\x0btravel_mode\x18\x04 \x01(\x0e2".google.maps.roads.v1op.TravelMode"}\n\x0cSnappedPoint\x12%\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x124\n\x0eoriginal_index\x18\x02 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x10\n\x08place_id\x18\x03 \x01(\t"l\n\x13SnapToRoadsResponse\x12<\n\x0esnapped_points\x18\x01 \x03(\x0b2$.google.maps.roads.v1op.SnappedPoint\x12\x17\n\x0fwarning_message\x18\x02 \x01(\t"b\n\x17ListNearestRoadsRequest\x12\x0e\n\x06points\x18\x01 \x01(\t\x127\n\x0btravel_mode\x18\x02 \x01(\x0e2".google.maps.roads.v1op.TravelMode"X\n\x18ListNearestRoadsResponse\x12<\n\x0esnapped_points\x18\x01 \x03(\x0b2$.google.maps.roads.v1op.SnappedPoint*P\n\nTravelMode\x12\x1b\n\x17TRAVEL_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DRIVING\x10\x01\x12\x0b\n\x07CYCLING\x10\x02\x12\x0b\n\x07WALKING\x10\x032\x9b\x02\n\x0cRoadsService\x12o\n\x0bSnapToRoads\x12*.google.maps.roads.v1op.SnapToRoadsRequest\x1a+.google.maps.roads.v1op.SnapToRoadsResponse"\x07\xdaA\x04path\x12\x80\x01\n\x10ListNearestRoads\x12/.google.maps.roads.v1op.ListNearestRoadsRequest\x1a0.google.maps.roads.v1op.ListNearestRoadsResponse"\t\xdaA\x06points\x1a\x17\xcaA\x14roads.googleapis.comBb\n\x1acom.google.maps.roads.v1opB\nRoadsProtoP\x01Z6cloud.google.com/go/maps/roads/apiv1op/roadspb;roadspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.roads.v1op.roads_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.roads.v1opB\nRoadsProtoP\x01Z6cloud.google.com/go/maps/roads/apiv1op/roadspb;roadspb'
    _globals['_ROADSSERVICE']._loaded_options = None
    _globals['_ROADSSERVICE']._serialized_options = b'\xcaA\x14roads.googleapis.com'
    _globals['_ROADSSERVICE'].methods_by_name['SnapToRoads']._loaded_options = None
    _globals['_ROADSSERVICE'].methods_by_name['SnapToRoads']._serialized_options = b'\xdaA\x04path'
    _globals['_ROADSSERVICE'].methods_by_name['ListNearestRoads']._loaded_options = None
    _globals['_ROADSSERVICE'].methods_by_name['ListNearestRoads']._serialized_options = b'\xdaA\x06points'
    _globals['_TRAVELMODE']._serialized_start = 705
    _globals['_TRAVELMODE']._serialized_end = 785
    _globals['_SNAPTOROADSREQUEST']._serialized_start = 146
    _globals['_SNAPTOROADSREQUEST']._serialized_end = 276
    _globals['_SNAPPEDPOINT']._serialized_start = 278
    _globals['_SNAPPEDPOINT']._serialized_end = 403
    _globals['_SNAPTOROADSRESPONSE']._serialized_start = 405
    _globals['_SNAPTOROADSRESPONSE']._serialized_end = 513
    _globals['_LISTNEARESTROADSREQUEST']._serialized_start = 515
    _globals['_LISTNEARESTROADSREQUEST']._serialized_end = 613
    _globals['_LISTNEARESTROADSRESPONSE']._serialized_start = 615
    _globals['_LISTNEARESTROADSRESPONSE']._serialized_end = 703
    _globals['_ROADSSERVICE']._serialized_start = 788
    _globals['_ROADSSERVICE']._serialized_end = 1071