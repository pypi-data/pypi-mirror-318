"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/routing_summary.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/maps/places/v1/routing_summary.proto\x12\x15google.maps.places.v1\x1a\x1egoogle/protobuf/duration.proto"\xae\x01\n\x0eRoutingSummary\x127\n\x04legs\x18\x01 \x03(\x0b2).google.maps.places.v1.RoutingSummary.Leg\x12\x16\n\x0edirections_uri\x18\x02 \x01(\t\x1aK\n\x03Leg\x12+\n\x08duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x17\n\x0fdistance_meters\x18\x02 \x01(\x05B\xa4\x01\n\x19com.google.maps.places.v1B\x13RoutingSummaryProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.routing_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x13RoutingSummaryProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_ROUTINGSUMMARY']._serialized_start = 103
    _globals['_ROUTINGSUMMARY']._serialized_end = 277
    _globals['_ROUTINGSUMMARY_LEG']._serialized_start = 202
    _globals['_ROUTINGSUMMARY_LEG']._serialized_end = 277