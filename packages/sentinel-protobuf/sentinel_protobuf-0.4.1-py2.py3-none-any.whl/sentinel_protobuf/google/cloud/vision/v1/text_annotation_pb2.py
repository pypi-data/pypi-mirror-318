"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1/text_annotation.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.vision.v1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/vision/v1/text_annotation.proto\x12\x16google.cloud.vision.v1\x1a%google/cloud/vision/v1/geometry.proto"\x96\x04\n\x0eTextAnnotation\x12+\n\x05pages\x18\x01 \x03(\x0b2\x1c.google.cloud.vision.v1.Page\x12\x0c\n\x04text\x18\x02 \x01(\t\x1a=\n\x10DetectedLanguage\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x1a\xd5\x01\n\rDetectedBreak\x12L\n\x04type\x18\x01 \x01(\x0e2>.google.cloud.vision.v1.TextAnnotation.DetectedBreak.BreakType\x12\x11\n\tis_prefix\x18\x02 \x01(\x08"c\n\tBreakType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05SPACE\x10\x01\x12\x0e\n\nSURE_SPACE\x10\x02\x12\x12\n\x0eEOL_SURE_SPACE\x10\x03\x12\n\n\x06HYPHEN\x10\x04\x12\x0e\n\nLINE_BREAK\x10\x05\x1a\xb1\x01\n\x0cTextProperty\x12S\n\x12detected_languages\x18\x01 \x03(\x0b27.google.cloud.vision.v1.TextAnnotation.DetectedLanguage\x12L\n\x0edetected_break\x18\x02 \x01(\x0b24.google.cloud.vision.v1.TextAnnotation.DetectedBreak"\xaf\x01\n\x04Page\x12E\n\x08property\x18\x01 \x01(\x0b23.google.cloud.vision.v1.TextAnnotation.TextProperty\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12-\n\x06blocks\x18\x04 \x03(\x0b2\x1d.google.cloud.vision.v1.Block\x12\x12\n\nconfidence\x18\x05 \x01(\x02"\xe6\x02\n\x05Block\x12E\n\x08property\x18\x01 \x01(\x0b23.google.cloud.vision.v1.TextAnnotation.TextProperty\x12:\n\x0cbounding_box\x18\x02 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x125\n\nparagraphs\x18\x03 \x03(\x0b2!.google.cloud.vision.v1.Paragraph\x12;\n\nblock_type\x18\x04 \x01(\x0e2\'.google.cloud.vision.v1.Block.BlockType\x12\x12\n\nconfidence\x18\x05 \x01(\x02"R\n\tBlockType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05TABLE\x10\x02\x12\x0b\n\x07PICTURE\x10\x03\x12\t\n\x05RULER\x10\x04\x12\x0b\n\x07BARCODE\x10\x05"\xcf\x01\n\tParagraph\x12E\n\x08property\x18\x01 \x01(\x0b23.google.cloud.vision.v1.TextAnnotation.TextProperty\x12:\n\x0cbounding_box\x18\x02 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x12+\n\x05words\x18\x03 \x03(\x0b2\x1c.google.cloud.vision.v1.Word\x12\x12\n\nconfidence\x18\x04 \x01(\x02"\xce\x01\n\x04Word\x12E\n\x08property\x18\x01 \x01(\x0b23.google.cloud.vision.v1.TextAnnotation.TextProperty\x12:\n\x0cbounding_box\x18\x02 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x12/\n\x07symbols\x18\x03 \x03(\x0b2\x1e.google.cloud.vision.v1.Symbol\x12\x12\n\nconfidence\x18\x04 \x01(\x02"\xad\x01\n\x06Symbol\x12E\n\x08property\x18\x01 \x01(\x0b23.google.cloud.vision.v1.TextAnnotation.TextProperty\x12:\n\x0cbounding_box\x18\x02 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02Bt\n\x1acom.google.cloud.vision.v1B\x13TextAnnotationProtoP\x01Z5cloud.google.com/go/vision/v2/apiv1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1.text_annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.vision.v1B\x13TextAnnotationProtoP\x01Z5cloud.google.com/go/vision/v2/apiv1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_TEXTANNOTATION']._serialized_start = 112
    _globals['_TEXTANNOTATION']._serialized_end = 646
    _globals['_TEXTANNOTATION_DETECTEDLANGUAGE']._serialized_start = 189
    _globals['_TEXTANNOTATION_DETECTEDLANGUAGE']._serialized_end = 250
    _globals['_TEXTANNOTATION_DETECTEDBREAK']._serialized_start = 253
    _globals['_TEXTANNOTATION_DETECTEDBREAK']._serialized_end = 466
    _globals['_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE']._serialized_start = 367
    _globals['_TEXTANNOTATION_DETECTEDBREAK_BREAKTYPE']._serialized_end = 466
    _globals['_TEXTANNOTATION_TEXTPROPERTY']._serialized_start = 469
    _globals['_TEXTANNOTATION_TEXTPROPERTY']._serialized_end = 646
    _globals['_PAGE']._serialized_start = 649
    _globals['_PAGE']._serialized_end = 824
    _globals['_BLOCK']._serialized_start = 827
    _globals['_BLOCK']._serialized_end = 1185
    _globals['_BLOCK_BLOCKTYPE']._serialized_start = 1103
    _globals['_BLOCK_BLOCKTYPE']._serialized_end = 1185
    _globals['_PARAGRAPH']._serialized_start = 1188
    _globals['_PARAGRAPH']._serialized_end = 1395
    _globals['_WORD']._serialized_start = 1398
    _globals['_WORD']._serialized_end = 1604
    _globals['_SYMBOL']._serialized_start = 1607
    _globals['_SYMBOL']._serialized_end = 1780