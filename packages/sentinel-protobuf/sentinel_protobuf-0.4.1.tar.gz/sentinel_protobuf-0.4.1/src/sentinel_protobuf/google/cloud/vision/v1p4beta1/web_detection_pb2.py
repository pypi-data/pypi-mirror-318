"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p4beta1/web_detection.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/vision/v1p4beta1/web_detection.proto\x12\x1dgoogle.cloud.vision.v1p4beta1"\x8c\x07\n\x0cWebDetection\x12K\n\x0cweb_entities\x18\x01 \x03(\x0b25.google.cloud.vision.v1p4beta1.WebDetection.WebEntity\x12R\n\x14full_matching_images\x18\x02 \x03(\x0b24.google.cloud.vision.v1p4beta1.WebDetection.WebImage\x12U\n\x17partial_matching_images\x18\x03 \x03(\x0b24.google.cloud.vision.v1p4beta1.WebDetection.WebImage\x12W\n\x1apages_with_matching_images\x18\x04 \x03(\x0b23.google.cloud.vision.v1p4beta1.WebDetection.WebPage\x12U\n\x17visually_similar_images\x18\x06 \x03(\x0b24.google.cloud.vision.v1p4beta1.WebDetection.WebImage\x12O\n\x11best_guess_labels\x18\x08 \x03(\x0b24.google.cloud.vision.v1p4beta1.WebDetection.WebLabel\x1aB\n\tWebEntity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x1a&\n\x08WebImage\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x1a\xe4\x01\n\x07WebPage\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x12\n\npage_title\x18\x03 \x01(\t\x12R\n\x14full_matching_images\x18\x04 \x03(\x0b24.google.cloud.vision.v1p4beta1.WebDetection.WebImage\x12U\n\x17partial_matching_images\x18\x05 \x03(\x0b24.google.cloud.vision.v1p4beta1.WebDetection.WebImage\x1a0\n\x08WebLabel\x12\r\n\x05label\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\tB}\n!com.google.cloud.vision.v1p4beta1B\x11WebDetectionProtoP\x01Z9cloud.google.com/go/vision/apiv1p4beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p4beta1.web_detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p4beta1B\x11WebDetectionProtoP\x01Z9cloud.google.com/go/vision/apiv1p4beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_WEBDETECTION']._serialized_start = 85
    _globals['_WEBDETECTION']._serialized_end = 993
    _globals['_WEBDETECTION_WEBENTITY']._serialized_start = 606
    _globals['_WEBDETECTION_WEBENTITY']._serialized_end = 672
    _globals['_WEBDETECTION_WEBIMAGE']._serialized_start = 674
    _globals['_WEBDETECTION_WEBIMAGE']._serialized_end = 712
    _globals['_WEBDETECTION_WEBPAGE']._serialized_start = 715
    _globals['_WEBDETECTION_WEBPAGE']._serialized_end = 943
    _globals['_WEBDETECTION_WEBLABEL']._serialized_start = 945
    _globals['_WEBDETECTION_WEBLABEL']._serialized_end = 993