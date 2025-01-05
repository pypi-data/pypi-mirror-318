"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/review.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.places.v1 import attribution_pb2 as google_dot_maps_dot_places_dot_v1_dot_attribution__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/maps/places/v1/review.proto\x12\x15google.maps.places.v1\x1a\x19google/api/resource.proto\x1a\'google/maps/places/v1/attribution.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/type/localized_text.proto"\xfb\x02\n\x06Review\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n!relative_publish_time_description\x18\x02 \x01(\t\x12(\n\x04text\x18\t \x01(\x0b2\x1a.google.type.LocalizedText\x121\n\roriginal_text\x18\x0c \x01(\x0b2\x1a.google.type.LocalizedText\x12\x0e\n\x06rating\x18\x07 \x01(\x01\x12D\n\x12author_attribution\x18\r \x01(\x0b2(.google.maps.places.v1.AuthorAttribution\x120\n\x0cpublish_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.Timestamp:S\xeaAP\n\x1cplaces.googleapis.com/Review\x12\x1fplaces/{place}/reviews/{review}*\x07reviews2\x06reviewB\x9c\x01\n\x19com.google.maps.places.v1B\x0bReviewProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.review_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x0bReviewProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_REVIEW']._loaded_options = None
    _globals['_REVIEW']._serialized_options = b'\xeaAP\n\x1cplaces.googleapis.com/Review\x12\x1fplaces/{place}/reviews/{review}*\x07reviews2\x06review'
    _globals['_REVIEW']._serialized_start = 197
    _globals['_REVIEW']._serialized_end = 576