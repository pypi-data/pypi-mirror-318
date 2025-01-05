"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/theme_customization.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/actions/sdk/v2/theme_customization.proto\x12\x15google.actions.sdk.v2"\xc9\x02\n\x12ThemeCustomization\x12\x18\n\x10background_color\x18\x01 \x01(\t\x12\x15\n\rprimary_color\x18\x02 \x01(\t\x12\x13\n\x0bfont_family\x18\x03 \x01(\t\x12V\n\x12image_corner_style\x18\x04 \x01(\x0e2:.google.actions.sdk.v2.ThemeCustomization.ImageCornerStyle\x12"\n\x1alandscape_background_image\x18\x05 \x01(\t\x12!\n\x19portrait_background_image\x18\x06 \x01(\t"N\n\x10ImageCornerStyle\x12"\n\x1eIMAGE_CORNER_STYLE_UNSPECIFIED\x10\x00\x12\n\n\x06CURVED\x10\x01\x12\n\n\x06ANGLED\x10\x02Bp\n\x19com.google.actions.sdk.v2B\x17ThemeCustomizationProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.theme_customization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x17ThemeCustomizationProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_THEMECUSTOMIZATION']._serialized_start = 75
    _globals['_THEMECUSTOMIZATION']._serialized_end = 404
    _globals['_THEMECUSTOMIZATION_IMAGECORNERSTYLE']._serialized_start = 326
    _globals['_THEMECUSTOMIZATION_IMAGECORNERSTYLE']._serialized_end = 404