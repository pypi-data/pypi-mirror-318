"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/document.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.documentai.v1 import document_pb2 as google_dot_cloud_dot_documentai_dot_v1_dot_document__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/contentwarehouse/v1/document.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/documentai/v1/document.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto"\x84\t\n\x08Document\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0creference_id\x18\x0b \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\r\n\x05title\x18\x12 \x01(\t\x12\x13\n\x0bdisplay_uri\x18\x11 \x01(\t\x12Q\n\x14document_schema_name\x18\x03 \x01(\tB3\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema\x12\x14\n\nplain_text\x18\x0f \x01(\tH\x00\x12A\n\x11cloud_ai_document\x18\x04 \x01(\x0b2$.google.cloud.documentai.v1.DocumentH\x00\x12"\n\x16structured_content_uri\x18\x10 \x01(\tB\x02\x18\x01\x12\x1b\n\x11raw_document_path\x18\x05 \x01(\tH\x01\x12\x1d\n\x13inline_raw_document\x18\x06 \x01(\x0cH\x01\x12>\n\nproperties\x18\x07 \x03(\x0b2*.google.cloud.contentwarehouse.v1.Property\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12U\n\x16raw_document_file_type\x18\n \x01(\x0e25.google.cloud.contentwarehouse.v1.RawDocumentFileType\x12\x19\n\rasync_enabled\x18\x0c \x01(\x08B\x02\x18\x01\x12K\n\x10content_category\x18\x14 \x01(\x0e21.google.cloud.contentwarehouse.v1.ContentCategory\x12$\n\x18text_extraction_disabled\x18\x13 \x01(\x08B\x02\x18\x01\x12\x1f\n\x17text_extraction_enabled\x18\x15 \x01(\x08\x12\x0f\n\x07creator\x18\r \x01(\t\x12\x0f\n\x07updater\x18\x0e \x01(\t\x129\n\x10disposition_time\x18\x16 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x17\n\nlegal_hold\x18\x17 \x01(\x08B\x03\xe0A\x03:\xba\x01\xeaA\xb6\x01\n(contentwarehouse.googleapis.com/Document\x12<projects/{project}/locations/{location}/documents/{document}\x12Lprojects/{project}/locations/{location}/documents/referenceId/{reference_id}B\x14\n\x12structured_contentB\x0e\n\x0craw_document"\x8e\x03\n\x11DocumentReference\x12G\n\rdocument_name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0f\n\x07snippet\x18\x03 \x01(\t\x12\x1a\n\x12document_is_folder\x18\x04 \x01(\x08\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12$\n\x1cdocument_is_retention_folder\x18\x08 \x01(\x08\x12%\n\x1ddocument_is_legal_hold_folder\x18\t \x01(\x08"\xed\x04\n\x08Property\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12H\n\x0einteger_values\x18\x02 \x01(\x0b2..google.cloud.contentwarehouse.v1.IntegerArrayH\x00\x12D\n\x0cfloat_values\x18\x03 \x01(\x0b2,.google.cloud.contentwarehouse.v1.FloatArrayH\x00\x12B\n\x0btext_values\x18\x04 \x01(\x0b2+.google.cloud.contentwarehouse.v1.TextArrayH\x00\x12B\n\x0benum_values\x18\x05 \x01(\x0b2+.google.cloud.contentwarehouse.v1.EnumArrayH\x00\x12J\n\x0fproperty_values\x18\x06 \x01(\x0b2/.google.cloud.contentwarehouse.v1.PropertyArrayH\x00\x12K\n\x10date_time_values\x18\x07 \x01(\x0b2/.google.cloud.contentwarehouse.v1.DateTimeArrayH\x00\x12E\n\x0cmap_property\x18\x08 \x01(\x0b2-.google.cloud.contentwarehouse.v1.MapPropertyH\x00\x12L\n\x10timestamp_values\x18\t \x01(\x0b20.google.cloud.contentwarehouse.v1.TimestampArrayH\x00B\x08\n\x06values"\x1e\n\x0cIntegerArray\x12\x0e\n\x06values\x18\x01 \x03(\x05"\x1c\n\nFloatArray\x12\x0e\n\x06values\x18\x01 \x03(\x02"\x1b\n\tTextArray\x12\x0e\n\x06values\x18\x01 \x03(\t"\x1b\n\tEnumArray\x12\x0e\n\x06values\x18\x01 \x03(\t"6\n\rDateTimeArray\x12%\n\x06values\x18\x01 \x03(\x0b2\x15.google.type.DateTime"R\n\x0eTimestampArray\x12@\n\x06values\x18\x01 \x03(\x0b20.google.cloud.contentwarehouse.v1.TimestampValue"f\n\x0eTimestampValue\x125\n\x0ftimestamp_value\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12\x14\n\ntext_value\x18\x02 \x01(\tH\x00B\x07\n\x05value"O\n\rPropertyArray\x12>\n\nproperties\x18\x01 \x03(\x0b2*.google.cloud.contentwarehouse.v1.Property"\xb0\x01\n\x0bMapProperty\x12I\n\x06fields\x18\x01 \x03(\x0b29.google.cloud.contentwarehouse.v1.MapProperty.FieldsEntry\x1aV\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.contentwarehouse.v1.Value:\x028\x01"\xad\x02\n\x05Value\x12\x15\n\x0bfloat_value\x18\x01 \x01(\x02H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12A\n\nenum_value\x18\x04 \x01(\x0b2+.google.cloud.contentwarehouse.v1.EnumValueH\x00\x12/\n\x0edatetime_value\x18\x05 \x01(\x0b2\x15.google.type.DateTimeH\x00\x12K\n\x0ftimestamp_value\x18\x06 \x01(\x0b20.google.cloud.contentwarehouse.v1.TimestampValueH\x00\x12\x17\n\rboolean_value\x18\x07 \x01(\x08H\x00B\x06\n\x04kind"\x1a\n\tEnumValue\x12\r\n\x05value\x18\x01 \x01(\t*\x82\x02\n\x13RawDocumentFileType\x12&\n"RAW_DOCUMENT_FILE_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aRAW_DOCUMENT_FILE_TYPE_PDF\x10\x01\x12\x1f\n\x1bRAW_DOCUMENT_FILE_TYPE_DOCX\x10\x02\x12\x1f\n\x1bRAW_DOCUMENT_FILE_TYPE_XLSX\x10\x03\x12\x1f\n\x1bRAW_DOCUMENT_FILE_TYPE_PPTX\x10\x04\x12\x1f\n\x1bRAW_DOCUMENT_FILE_TYPE_TEXT\x10\x05\x12\x1f\n\x1bRAW_DOCUMENT_FILE_TYPE_TIFF\x10\x06*\x87\x01\n\x0fContentCategory\x12 \n\x1cCONTENT_CATEGORY_UNSPECIFIED\x10\x00\x12\x1a\n\x16CONTENT_CATEGORY_IMAGE\x10\x01\x12\x1a\n\x16CONTENT_CATEGORY_AUDIO\x10\x02\x12\x1a\n\x16CONTENT_CATEGORY_VIDEO\x10\x03B\xf5\x01\n$com.google.cloud.contentwarehouse.v1B\rDocumentProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.document_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\rDocumentProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_DOCUMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['document_schema_name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['document_schema_name']._serialized_options = b'\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_DOCUMENT'].fields_by_name['structured_content_uri']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['structured_content_uri']._serialized_options = b'\x18\x01'
    _globals['_DOCUMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['async_enabled']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['async_enabled']._serialized_options = b'\x18\x01'
    _globals['_DOCUMENT'].fields_by_name['text_extraction_disabled']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['text_extraction_disabled']._serialized_options = b'\x18\x01'
    _globals['_DOCUMENT'].fields_by_name['disposition_time']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['disposition_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['legal_hold']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['legal_hold']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT']._loaded_options = None
    _globals['_DOCUMENT']._serialized_options = b'\xeaA\xb6\x01\n(contentwarehouse.googleapis.com/Document\x12<projects/{project}/locations/{location}/documents/{document}\x12Lprojects/{project}/locations/{location}/documents/referenceId/{reference_id}'
    _globals['_DOCUMENTREFERENCE'].fields_by_name['document_name']._loaded_options = None
    _globals['_DOCUMENTREFERENCE'].fields_by_name['document_name']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_DOCUMENTREFERENCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOCUMENTREFERENCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTREFERENCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DOCUMENTREFERENCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTREFERENCE'].fields_by_name['delete_time']._loaded_options = None
    _globals['_DOCUMENTREFERENCE'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROPERTY'].fields_by_name['name']._loaded_options = None
    _globals['_PROPERTY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MAPPROPERTY_FIELDSENTRY']._loaded_options = None
    _globals['_MAPPROPERTY_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_RAWDOCUMENTFILETYPE']._serialized_start = 3390
    _globals['_RAWDOCUMENTFILETYPE']._serialized_end = 3648
    _globals['_CONTENTCATEGORY']._serialized_start = 3651
    _globals['_CONTENTCATEGORY']._serialized_end = 3786
    _globals['_DOCUMENT']._serialized_start = 250
    _globals['_DOCUMENT']._serialized_end = 1406
    _globals['_DOCUMENTREFERENCE']._serialized_start = 1409
    _globals['_DOCUMENTREFERENCE']._serialized_end = 1807
    _globals['_PROPERTY']._serialized_start = 1810
    _globals['_PROPERTY']._serialized_end = 2431
    _globals['_INTEGERARRAY']._serialized_start = 2433
    _globals['_INTEGERARRAY']._serialized_end = 2463
    _globals['_FLOATARRAY']._serialized_start = 2465
    _globals['_FLOATARRAY']._serialized_end = 2493
    _globals['_TEXTARRAY']._serialized_start = 2495
    _globals['_TEXTARRAY']._serialized_end = 2522
    _globals['_ENUMARRAY']._serialized_start = 2524
    _globals['_ENUMARRAY']._serialized_end = 2551
    _globals['_DATETIMEARRAY']._serialized_start = 2553
    _globals['_DATETIMEARRAY']._serialized_end = 2607
    _globals['_TIMESTAMPARRAY']._serialized_start = 2609
    _globals['_TIMESTAMPARRAY']._serialized_end = 2691
    _globals['_TIMESTAMPVALUE']._serialized_start = 2693
    _globals['_TIMESTAMPVALUE']._serialized_end = 2795
    _globals['_PROPERTYARRAY']._serialized_start = 2797
    _globals['_PROPERTYARRAY']._serialized_end = 2876
    _globals['_MAPPROPERTY']._serialized_start = 2879
    _globals['_MAPPROPERTY']._serialized_end = 3055
    _globals['_MAPPROPERTY_FIELDSENTRY']._serialized_start = 2969
    _globals['_MAPPROPERTY_FIELDSENTRY']._serialized_end = 3055
    _globals['_VALUE']._serialized_start = 3058
    _globals['_VALUE']._serialized_end = 3359
    _globals['_ENUMVALUE']._serialized_start = 3361
    _globals['_ENUMVALUE']._serialized_end = 3387