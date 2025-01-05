"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/text.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/monitoring/dashboard/v1/text.proto\x12\x1egoogle.monitoring.dashboard.v1"\xf8\n\n\x04Text\x12\x0f\n\x07content\x18\x01 \x01(\t\x12;\n\x06format\x18\x02 \x01(\x0e2+.google.monitoring.dashboard.v1.Text.Format\x12=\n\x05style\x18\x03 \x01(\x0b2..google.monitoring.dashboard.v1.Text.TextStyle\x1a\xa9\t\n\tTextStyle\x12\x18\n\x10background_color\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12`\n\x14horizontal_alignment\x18\x03 \x01(\x0e2B.google.monitoring.dashboard.v1.Text.TextStyle.HorizontalAlignment\x12\\\n\x12vertical_alignment\x18\x04 \x01(\x0e2@.google.monitoring.dashboard.v1.Text.TextStyle.VerticalAlignment\x12K\n\x07padding\x18\x05 \x01(\x0e2:.google.monitoring.dashboard.v1.Text.TextStyle.PaddingSize\x12J\n\tfont_size\x18\x06 \x01(\x0e27.google.monitoring.dashboard.v1.Text.TextStyle.FontSize\x12X\n\x10pointer_location\x18\x07 \x01(\x0e2>.google.monitoring.dashboard.v1.Text.TextStyle.PointerLocation"b\n\x13HorizontalAlignment\x12$\n HORIZONTAL_ALIGNMENT_UNSPECIFIED\x10\x00\x12\n\n\x06H_LEFT\x10\x01\x12\x0c\n\x08H_CENTER\x10\x02\x12\x0b\n\x07H_RIGHT\x10\x03"^\n\x11VerticalAlignment\x12"\n\x1eVERTICAL_ALIGNMENT_UNSPECIFIED\x10\x00\x12\t\n\x05V_TOP\x10\x01\x12\x0c\n\x08V_CENTER\x10\x02\x12\x0c\n\x08V_BOTTOM\x10\x03"y\n\x0bPaddingSize\x12\x1c\n\x18PADDING_SIZE_UNSPECIFIED\x10\x00\x12\x11\n\rP_EXTRA_SMALL\x10\x01\x12\x0b\n\x07P_SMALL\x10\x02\x12\x0c\n\x08P_MEDIUM\x10\x03\x12\x0b\n\x07P_LARGE\x10\x04\x12\x11\n\rP_EXTRA_LARGE\x10\x05"x\n\x08FontSize\x12\x19\n\x15FONT_SIZE_UNSPECIFIED\x10\x00\x12\x12\n\x0eFS_EXTRA_SMALL\x10\x01\x12\x0c\n\x08FS_SMALL\x10\x02\x12\r\n\tFS_MEDIUM\x10\x03\x12\x0c\n\x08FS_LARGE\x10\x04\x12\x12\n\x0eFS_EXTRA_LARGE\x10\x05"\x81\x02\n\x0fPointerLocation\x12 \n\x1cPOINTER_LOCATION_UNSPECIFIED\x10\x00\x12\n\n\x06PL_TOP\x10\x01\x12\x0c\n\x08PL_RIGHT\x10\x02\x12\r\n\tPL_BOTTOM\x10\x03\x12\x0b\n\x07PL_LEFT\x10\x04\x12\x0f\n\x0bPL_TOP_LEFT\x10\x05\x12\x10\n\x0cPL_TOP_RIGHT\x10\x06\x12\x10\n\x0cPL_RIGHT_TOP\x10\x07\x12\x13\n\x0fPL_RIGHT_BOTTOM\x10\x08\x12\x13\n\x0fPL_BOTTOM_RIGHT\x10\t\x12\x12\n\x0ePL_BOTTOM_LEFT\x10\n\x12\x12\n\x0ePL_LEFT_BOTTOM\x10\x0b\x12\x0f\n\x0bPL_LEFT_TOP\x10\x0c"7\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x12\x07\n\x03RAW\x10\x02B\xf2\x01\n"com.google.monitoring.dashboard.v1B\tTextProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.text_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\tTextProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_TEXT']._serialized_start = 78
    _globals['_TEXT']._serialized_end = 1478
    _globals['_TEXT_TEXTSTYLE']._serialized_start = 228
    _globals['_TEXT_TEXTSTYLE']._serialized_end = 1421
    _globals['_TEXT_TEXTSTYLE_HORIZONTALALIGNMENT']._serialized_start = 722
    _globals['_TEXT_TEXTSTYLE_HORIZONTALALIGNMENT']._serialized_end = 820
    _globals['_TEXT_TEXTSTYLE_VERTICALALIGNMENT']._serialized_start = 822
    _globals['_TEXT_TEXTSTYLE_VERTICALALIGNMENT']._serialized_end = 916
    _globals['_TEXT_TEXTSTYLE_PADDINGSIZE']._serialized_start = 918
    _globals['_TEXT_TEXTSTYLE_PADDINGSIZE']._serialized_end = 1039
    _globals['_TEXT_TEXTSTYLE_FONTSIZE']._serialized_start = 1041
    _globals['_TEXT_TEXTSTYLE_FONTSIZE']._serialized_end = 1161
    _globals['_TEXT_TEXTSTYLE_POINTERLOCATION']._serialized_start = 1164
    _globals['_TEXT_TEXTSTYLE_POINTERLOCATION']._serialized_end = 1421
    _globals['_TEXT_FORMAT']._serialized_start = 1423
    _globals['_TEXT_FORMAT']._serialized_end = 1478