"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/geometry.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/maps/places/v1/geometry.proto\x12\x15google.maps.places.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x18google/type/latlng.proto"G\n\x06Circle\x12(\n\x06center\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12\x13\n\x06radius\x18\x02 \x01(\x01B\x03\xe0A\x02B\x9e\x01\n\x19com.google.maps.places.v1B\rGeometryProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.geometry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\rGeometryProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_CIRCLE'].fields_by_name['center']._loaded_options = None
    _globals['_CIRCLE'].fields_by_name['center']._serialized_options = b'\xe0A\x02'
    _globals['_CIRCLE'].fields_by_name['radius']._loaded_options = None
    _globals['_CIRCLE'].fields_by_name['radius']._serialized_options = b'\xe0A\x02'
    _globals['_CIRCLE']._serialized_start = 122
    _globals['_CIRCLE']._serialized_end = 193