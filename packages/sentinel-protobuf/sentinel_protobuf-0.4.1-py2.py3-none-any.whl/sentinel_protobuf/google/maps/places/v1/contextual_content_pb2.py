"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/contextual_content.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.places.v1 import photo_pb2 as google_dot_maps_dot_places_dot_v1_dot_photo__pb2
from .....google.maps.places.v1 import review_pb2 as google_dot_maps_dot_places_dot_v1_dot_review__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/places/v1/contextual_content.proto\x12\x15google.maps.places.v1\x1a!google/maps/places/v1/photo.proto\x1a"google/maps/places/v1/review.proto"\x84\x08\n\x11ContextualContent\x12.\n\x07reviews\x18\x01 \x03(\x0b2\x1d.google.maps.places.v1.Review\x12,\n\x06photos\x18\x02 \x03(\x0b2\x1c.google.maps.places.v1.Photo\x12N\n\x0ejustifications\x18\x03 \x03(\x0b26.google.maps.places.v1.ContextualContent.Justification\x1a\xc0\x06\n\rJustification\x12j\n\x14review_justification\x18\x01 \x01(\x0b2J.google.maps.places.v1.ContextualContent.Justification.ReviewJustificationH\x00\x12\x9c\x01\n.business_availability_attributes_justification\x18\x02 \x01(\x0b2b.google.maps.places.v1.ContextualContent.Justification.BusinessAvailabilityAttributesJustificationH\x00\x1a\xaf\x03\n\x13ReviewJustification\x12t\n\x10highlighted_text\x18\x01 \x01(\x0b2Z.google.maps.places.v1.ContextualContent.Justification.ReviewJustification.HighlightedText\x12-\n\x06review\x18\x02 \x01(\x0b2\x1d.google.maps.places.v1.Review\x1a\xf2\x01\n\x0fHighlightedText\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x90\x01\n\x17highlighted_text_ranges\x18\x02 \x03(\x0b2o.google.maps.places.v1.ContextualContent.Justification.ReviewJustification.HighlightedText.HighlightedTextRange\x1a>\n\x14HighlightedTextRange\x12\x13\n\x0bstart_index\x18\x01 \x01(\x05\x12\x11\n\tend_index\x18\x02 \x01(\x05\x1aa\n+BusinessAvailabilityAttributesJustification\x12\x0f\n\x07takeout\x18\x01 \x01(\x08\x12\x10\n\x08delivery\x18\x02 \x01(\x08\x12\x0f\n\x07dine_in\x18\x03 \x01(\x08B\x0f\n\rjustificationB\xa7\x01\n\x19com.google.maps.places.v1B\x16ContextualContentProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.contextual_content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x16ContextualContentProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_CONTEXTUALCONTENT']._serialized_start = 145
    _globals['_CONTEXTUALCONTENT']._serialized_end = 1173
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION']._serialized_start = 341
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION']._serialized_end = 1173
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_REVIEWJUSTIFICATION']._serialized_start = 626
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_REVIEWJUSTIFICATION']._serialized_end = 1057
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_REVIEWJUSTIFICATION_HIGHLIGHTEDTEXT']._serialized_start = 815
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_REVIEWJUSTIFICATION_HIGHLIGHTEDTEXT']._serialized_end = 1057
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_REVIEWJUSTIFICATION_HIGHLIGHTEDTEXT_HIGHLIGHTEDTEXTRANGE']._serialized_start = 995
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_REVIEWJUSTIFICATION_HIGHLIGHTEDTEXT_HIGHLIGHTEDTEXTRANGE']._serialized_end = 1057
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_BUSINESSAVAILABILITYATTRIBUTESJUSTIFICATION']._serialized_start = 1059
    _globals['_CONTEXTUALCONTENT_JUSTIFICATION_BUSINESSAVAILABILITYATTRIBUTESJUSTIFICATION']._serialized_end = 1156