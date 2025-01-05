"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/addressvalidation/v1/geocode.proto')
_sym_db = _symbol_database.Default()
from .....google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/addressvalidation/v1/geocode.proto\x12 google.maps.addressvalidation.v1\x1a\x1egoogle/geo/type/viewport.proto\x1a\x18google/type/latlng.proto"\xde\x01\n\x07Geocode\x12%\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12=\n\tplus_code\x18\x02 \x01(\x0b2*.google.maps.addressvalidation.v1.PlusCode\x12)\n\x06bounds\x18\x04 \x01(\x0b2\x19.google.geo.type.Viewport\x12\x1b\n\x13feature_size_meters\x18\x05 \x01(\x02\x12\x10\n\x08place_id\x18\x06 \x01(\t\x12\x13\n\x0bplace_types\x18\x07 \x03(\t"6\n\x08PlusCode\x12\x13\n\x0bglobal_code\x18\x01 \x01(\t\x12\x15\n\rcompound_code\x18\x02 \x01(\tB\x89\x02\n$com.google.maps.addressvalidation.v1B\x0cGeocodeProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xf8\x01\x01\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.addressvalidation.v1.geocode_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.addressvalidation.v1B\x0cGeocodeProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xf8\x01\x01\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1'
    _globals['_GEOCODE']._serialized_start = 143
    _globals['_GEOCODE']._serialized_end = 365
    _globals['_PLUSCODE']._serialized_start = 367
    _globals['_PLUSCODE']._serialized_end = 421