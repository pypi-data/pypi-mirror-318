"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p2beta1/text_annotation.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.vision.v1p2beta1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1p2beta1_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/vision/v1p2beta1/text_annotation.proto\x12\x1dgoogle.cloud.vision.v1p2beta1\x1a,google/cloud/vision/v1p2beta1/geometry.proto"\xb2\x04\n\x0eTextAnnotation\x122\n\x05pages\x18\x01 \x03(\x0b2#.google.cloud.vision.v1p2beta1.Page\x12\x0c\n\x04text\x18\x02 \x01(\t\x1a=\n\x10DetectedLanguage\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x1a\xdc\x01\n\rDetectedBreak\x12S\n\x04type\x18\x01 \x01(\x0e2E.google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak.BreakType\x12\x11\n\tis_prefix\x18\x02 \x01(\x08"c\n\tBreakType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05SPACE\x10\x01\x12\x0e\n\nSURE_SPACE\x10\x02\x12\x12\n\x0eEOL_SURE_SPACE\x10\x03\x12\n\n\x06HYPHEN\x10\x04\x12\x0e\n\nLINE_BREAK\x10\x05\x1a\xbf\x01\n\x0cTextProperty\x12Z\n\x12detected_languages\x18\x01 \x03(\x0b2>.google.cloud.vision.v1p2beta1.TextAnnotation.DetectedLanguage\x12S\n\x0edetected_break\x18\x02 \x01(\x0b2;.google.cloud.vision.v1p2beta1.TextAnnotation.DetectedBreak"\xbd\x01\n\x04Page\x12L\n\x08property\x18\x01 \x01(\x0b2:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x124\n\x06blocks\x18\x04 \x03(\x0b2$.google.cloud.vision.v1p2beta1.Block\x12\x12\n\nconfidence\x18\x05 \x01(\x02"\x82\x03\n\x05Block\x12L\n\x08property\x18\x01 \x01(\x0b2:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12A\n\x0cbounding_box\x18\x02 \x01(\x0b2+.google.cloud.vision.v1p2beta1.BoundingPoly\x12<\n\nparagraphs\x18\x03 \x03(\x0b2(.google.cloud.vision.v1p2beta1.Paragraph\x12B\n\nblock_type\x18\x04 \x01(\x0e2..google.cloud.vision.v1p2beta1.Block.BlockType\x12\x12\n\nconfidence\x18\x05 \x01(\x02"R\n\tBlockType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05TABLE\x10\x02\x12\x0b\n\x07PICTURE\x10\x03\x12\t\n\x05RULER\x10\x04\x12\x0b\n\x07BARCODE\x10\x05"\xe4\x01\n\tParagraph\x12L\n\x08property\x18\x01 \x01(\x0b2:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12A\n\x0cbounding_box\x18\x02 \x01(\x0b2+.google.cloud.vision.v1p2beta1.BoundingPoly\x122\n\x05words\x18\x03 \x03(\x0b2#.google.cloud.vision.v1p2beta1.Word\x12\x12\n\nconfidence\x18\x04 \x01(\x02"\xe3\x01\n\x04Word\x12L\n\x08property\x18\x01 \x01(\x0b2:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12A\n\x0cbounding_box\x18\x02 \x01(\x0b2+.google.cloud.vision.v1p2beta1.BoundingPoly\x126\n\x07symbols\x18\x03 \x03(\x0b2%.google.cloud.vision.v1p2beta1.Symbol\x12\x12\n\nconfidence\x18\x04 \x01(\x02"\xbb\x01\n\x06Symbol\x12L\n\x08property\x18\x01 \x01(\x0b2:.google.cloud.vision.v1p2beta1.TextAnnotation.TextProperty\x12A\n\x0cbounding_box\x18\x02 \x01(\x0b2+.google.cloud.vision.v1p2beta1.BoundingPoly\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02Bx\n!com.google.cloud.vision.v1p2beta1B\x13TextAnnotationProtoP\x01Z9cloud.google.com/go/vision/apiv1p2beta1/visionpb;visionpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p2beta1.text_annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p2beta1B\x13TextAnnotationProtoP\x01Z9cloud.google.com/go/vision/apiv1p2beta1/visionpb;visionpb\xf8\x01\x01'
    _globals['_TEXTANNOTATION']._serialized_start = 133
    _globals['_TEXTANNOTATION']._serialized_end = 695
    _globals['_TEXTANNOTATION_DETECTEDLANGUAGE']._serialized_start = 217
    _globals['_TEXTANNOTATION_DETECTEDLANGUAGE']._serialized_end = 278
    _globals['_TEXTANNOTATION_DETECTEDBREAK']._serialized_start = 281
    _globals['_TEXTANNOTATION_DETECTEDBREAK']._serialized_end = 501
    _globals['_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE']._serialized_start = 402
    _globals['_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE']._serialized_end = 501
    _globals['_TEXTANNOTATION_TEXTPROPERTY']._serialized_start = 504
    _globals['_TEXTANNOTATION_TEXTPROPERTY']._serialized_end = 695
    _globals['_PAGE']._serialized_start = 698
    _globals['_PAGE']._serialized_end = 887
    _globals['_BLOCK']._serialized_start = 890
    _globals['_BLOCK']._serialized_end = 1276
    _globals['_BLOCK_BLOCKTYPE']._serialized_start = 1194
    _globals['_BLOCK_BLOCKTYPE']._serialized_end = 1276
    _globals['_PARAGRAPH']._serialized_start = 1279
    _globals['_PARAGRAPH']._serialized_end = 1507
    _globals['_WORD']._serialized_start = 1510
    _globals['_WORD']._serialized_end = 1737
    _globals['_SYMBOL']._serialized_start = 1740
    _globals['_SYMBOL']._serialized_end = 1927