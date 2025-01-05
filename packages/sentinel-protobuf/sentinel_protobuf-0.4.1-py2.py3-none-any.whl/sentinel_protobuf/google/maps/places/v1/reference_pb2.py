"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/reference.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.places.v1 import review_pb2 as google_dot_maps_dot_places_dot_v1_dot_review__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/maps/places/v1/reference.proto\x12\x15google.maps.places.v1\x1a\x19google/api/resource.proto\x1a"google/maps/places/v1/review.proto"n\n\nReferences\x12.\n\x07reviews\x18\x01 \x03(\x0b2\x1d.google.maps.places.v1.Review\x120\n\x06places\x18\x02 \x03(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/PlaceB\x9f\x01\n\x19com.google.maps.places.v1B\x0eReferenceProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.reference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x0eReferenceProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_REFERENCES'].fields_by_name['places']._loaded_options = None
    _globals['_REFERENCES'].fields_by_name['places']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_REFERENCES']._serialized_start = 127
    _globals['_REFERENCES']._serialized_end = 237