"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/photo.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.places.v1 import attribution_pb2 as google_dot_maps_dot_places_dot_v1_dot_attribution__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/maps/places/v1/photo.proto\x12\x15google.maps.places.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/maps/places/v1/attribution.proto"\xd6\x01\n\x05Photo\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x10\n\x08width_px\x18\x02 \x01(\x05\x12\x11\n\theight_px\x18\x03 \x01(\x05\x12E\n\x13author_attributions\x18\x04 \x03(\x0b2(.google.maps.places.v1.AuthorAttribution:N\xeaAK\n\x1bplaces.googleapis.com/Photo\x12\x1dplaces/{place}/photos/{photo}*\x06photos2\x05photoB\x9b\x01\n\x19com.google.maps.places.v1B\nPhotoProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.photo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\nPhotoProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_PHOTO'].fields_by_name['name']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PHOTO']._loaded_options = None
    _globals['_PHOTO']._serialized_options = b'\xeaAK\n\x1bplaces.googleapis.com/Photo\x12\x1dplaces/{place}/photos/{photo}*\x06photos2\x05photo'
    _globals['_PHOTO']._serialized_start = 162
    _globals['_PHOTO']._serialized_end = 376