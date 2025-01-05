"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/content_block.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.places.v1 import reference_pb2 as google_dot_maps_dot_places_dot_v1_dot_reference__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/maps/places/v1/content_block.proto\x12\x15google.maps.places.v1\x1a%google/maps/places/v1/reference.proto\x1a google/type/localized_text.proto"\x81\x01\n\x0cContentBlock\x12\r\n\x05topic\x18\x01 \x01(\t\x12+\n\x07content\x18\x02 \x01(\x0b2\x1a.google.type.LocalizedText\x125\n\nreferences\x18\x03 \x01(\x0b2!.google.maps.places.v1.ReferencesB\xa2\x01\n\x19com.google.maps.places.v1B\x11ContentBlockProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.content_block_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x11ContentBlockProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_CONTENTBLOCK']._serialized_start = 142
    _globals['_CONTENTBLOCK']._serialized_end = 271