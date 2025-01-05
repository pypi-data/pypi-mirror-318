"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/data_items.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1 import geometry_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2
from .....google.cloud.automl.v1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_io__pb2
from .....google.cloud.automl.v1 import text_segment_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_text__segment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/automl/v1/data_items.proto\x12\x16google.cloud.automl.v1\x1a%google/cloud/automl/v1/geometry.proto\x1a\x1fgoogle/cloud/automl/v1/io.proto\x1a)google/cloud/automl/v1/text_segment.proto"=\n\x05Image\x12\x15\n\x0bimage_bytes\x18\x01 \x01(\x0cH\x00\x12\x15\n\rthumbnail_uri\x18\x04 \x01(\tB\x06\n\x04data"F\n\x0bTextSnippet\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x13\n\x0bcontent_uri\x18\x04 \x01(\t"\xea\x01\n\x12DocumentDimensions\x12N\n\x04unit\x18\x01 \x01(\x0e2@.google.cloud.automl.v1.DocumentDimensions.DocumentDimensionUnit\x12\r\n\x05width\x18\x02 \x01(\x02\x12\x0e\n\x06height\x18\x03 \x01(\x02"e\n\x15DocumentDimensionUnit\x12\'\n#DOCUMENT_DIMENSION_UNIT_UNSPECIFIED\x10\x00\x12\x08\n\x04INCH\x10\x01\x12\x0e\n\nCENTIMETER\x10\x02\x12\t\n\x05POINT\x10\x03"\xd6\x05\n\x08Document\x12A\n\x0cinput_config\x18\x01 \x01(\x0b2+.google.cloud.automl.v1.DocumentInputConfig\x12:\n\rdocument_text\x18\x02 \x01(\x0b2#.google.cloud.automl.v1.TextSnippet\x127\n\x06layout\x18\x03 \x03(\x0b2\'.google.cloud.automl.v1.Document.Layout\x12G\n\x13document_dimensions\x18\x04 \x01(\x0b2*.google.cloud.automl.v1.DocumentDimensions\x12\x12\n\npage_count\x18\x05 \x01(\x05\x1a\xb4\x03\n\x06Layout\x129\n\x0ctext_segment\x18\x01 \x01(\x0b2#.google.cloud.automl.v1.TextSegment\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\x12;\n\rbounding_poly\x18\x03 \x01(\x0b2$.google.cloud.automl.v1.BoundingPoly\x12R\n\x11text_segment_type\x18\x04 \x01(\x0e27.google.cloud.automl.v1.Document.Layout.TextSegmentType"\xc8\x01\n\x0fTextSegmentType\x12!\n\x1dTEXT_SEGMENT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TOKEN\x10\x01\x12\r\n\tPARAGRAPH\x10\x02\x12\x0e\n\nFORM_FIELD\x10\x03\x12\x13\n\x0fFORM_FIELD_NAME\x10\x04\x12\x17\n\x13FORM_FIELD_CONTENTS\x10\x05\x12\t\n\x05TABLE\x10\x06\x12\x10\n\x0cTABLE_HEADER\x10\x07\x12\r\n\tTABLE_ROW\x10\x08\x12\x0e\n\nTABLE_CELL\x10\t"\xbe\x01\n\x0eExamplePayload\x12.\n\x05image\x18\x01 \x01(\x0b2\x1d.google.cloud.automl.v1.ImageH\x00\x12;\n\x0ctext_snippet\x18\x02 \x01(\x0b2#.google.cloud.automl.v1.TextSnippetH\x00\x124\n\x08document\x18\x04 \x01(\x0b2 .google.cloud.automl.v1.DocumentH\x00B\t\n\x07payloadB\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.data_items_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_IMAGE']._serialized_start = 182
    _globals['_IMAGE']._serialized_end = 243
    _globals['_TEXTSNIPPET']._serialized_start = 245
    _globals['_TEXTSNIPPET']._serialized_end = 315
    _globals['_DOCUMENTDIMENSIONS']._serialized_start = 318
    _globals['_DOCUMENTDIMENSIONS']._serialized_end = 552
    _globals['_DOCUMENTDIMENSIONS_DOCUMENTDIMENSIONUNIT']._serialized_start = 451
    _globals['_DOCUMENTDIMENSIONS_DOCUMENTDIMENSIONUNIT']._serialized_end = 552
    _globals['_DOCUMENT']._serialized_start = 555
    _globals['_DOCUMENT']._serialized_end = 1281
    _globals['_DOCUMENT_LAYOUT']._serialized_start = 845
    _globals['_DOCUMENT_LAYOUT']._serialized_end = 1281
    _globals['_DOCUMENT_LAYOUT_TEXTSEGMENTTYPE']._serialized_start = 1081
    _globals['_DOCUMENT_LAYOUT_TEXTSEGMENTTYPE']._serialized_end = 1281
    _globals['_EXAMPLEPAYLOAD']._serialized_start = 1284
    _globals['_EXAMPLEPAYLOAD']._serialized_end = 1474