"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/document_schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/contentwarehouse/v1/document_schema.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaa\x03\n\x0eDocumentSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12R\n\x14property_definitions\x18\x03 \x03(\x0b24.google.cloud.contentwarehouse.v1.PropertyDefinition\x12\x1a\n\x12document_is_folder\x18\x04 \x01(\x08\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x07 \x01(\t:~\xeaA{\n.contentwarehouse.googleapis.com/DocumentSchema\x12Iprojects/{project}/locations/{location}/documentSchemas/{document_schema}"\xdd\t\n\x12PropertyDefinition\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x0c \x01(\t\x12\x15\n\ris_repeatable\x18\x02 \x01(\x08\x12\x15\n\ris_filterable\x18\x03 \x01(\x08\x12\x15\n\ris_searchable\x18\x04 \x01(\x08\x12\x13\n\x0bis_metadata\x18\x05 \x01(\x08\x12\x13\n\x0bis_required\x18\x0e \x01(\x08\x12f\n\x14retrieval_importance\x18\x12 \x01(\x0e2H.google.cloud.contentwarehouse.v1.PropertyDefinition.RetrievalImportance\x12T\n\x14integer_type_options\x18\x07 \x01(\x0b24.google.cloud.contentwarehouse.v1.IntegerTypeOptionsH\x00\x12P\n\x12float_type_options\x18\x08 \x01(\x0b22.google.cloud.contentwarehouse.v1.FloatTypeOptionsH\x00\x12N\n\x11text_type_options\x18\t \x01(\x0b21.google.cloud.contentwarehouse.v1.TextTypeOptionsH\x00\x12V\n\x15property_type_options\x18\n \x01(\x0b25.google.cloud.contentwarehouse.v1.PropertyTypeOptionsH\x00\x12N\n\x11enum_type_options\x18\x0b \x01(\x0b21.google.cloud.contentwarehouse.v1.EnumTypeOptionsH\x00\x12W\n\x16date_time_type_options\x18\r \x01(\x0b25.google.cloud.contentwarehouse.v1.DateTimeTypeOptionsH\x00\x12L\n\x10map_type_options\x18\x0f \x01(\x0b20.google.cloud.contentwarehouse.v1.MapTypeOptionsH\x00\x12X\n\x16timestamp_type_options\x18\x10 \x01(\x0b26.google.cloud.contentwarehouse.v1.TimestampTypeOptionsH\x00\x12Y\n\x0eschema_sources\x18\x13 \x03(\x0b2A.google.cloud.contentwarehouse.v1.PropertyDefinition.SchemaSource\x1a4\n\x0cSchemaSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eprocessor_type\x18\x02 \x01(\t"\x7f\n\x13RetrievalImportance\x12$\n RETRIEVAL_IMPORTANCE_UNSPECIFIED\x10\x00\x12\x0b\n\x07HIGHEST\x10\x01\x12\n\n\x06HIGHER\x10\x02\x12\x08\n\x04HIGH\x10\x03\x12\n\n\x06MEDIUM\x10\x04\x12\x07\n\x03LOW\x10\x05\x12\n\n\x06LOWEST\x10\x06B\x14\n\x12value_type_options"\x14\n\x12IntegerTypeOptions"\x12\n\x10FloatTypeOptions"\x11\n\x0fTextTypeOptions"\x15\n\x13DateTimeTypeOptions"\x10\n\x0eMapTypeOptions"\x16\n\x14TimestampTypeOptions"n\n\x13PropertyTypeOptions\x12W\n\x14property_definitions\x18\x01 \x03(\x0b24.google.cloud.contentwarehouse.v1.PropertyDefinitionB\x03\xe0A\x02"R\n\x0fEnumTypeOptions\x12\x1c\n\x0fpossible_values\x18\x01 \x03(\tB\x03\xe0A\x02\x12!\n\x19validation_check_disabled\x18\x02 \x01(\x08B\xfb\x01\n$com.google.cloud.contentwarehouse.v1B\x13DocumentSchemaProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.document_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x13DocumentSchemaProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_DOCUMENTSCHEMA'].fields_by_name['display_name']._loaded_options = None
    _globals['_DOCUMENTSCHEMA'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENTSCHEMA'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOCUMENTSCHEMA'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTSCHEMA'].fields_by_name['create_time']._loaded_options = None
    _globals['_DOCUMENTSCHEMA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTSCHEMA']._loaded_options = None
    _globals['_DOCUMENTSCHEMA']._serialized_options = b'\xeaA{\n.contentwarehouse.googleapis.com/DocumentSchema\x12Iprojects/{project}/locations/{location}/documentSchemas/{document_schema}'
    _globals['_PROPERTYDEFINITION'].fields_by_name['name']._loaded_options = None
    _globals['_PROPERTYDEFINITION'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_PROPERTYTYPEOPTIONS'].fields_by_name['property_definitions']._loaded_options = None
    _globals['_PROPERTYTYPEOPTIONS'].fields_by_name['property_definitions']._serialized_options = b'\xe0A\x02'
    _globals['_ENUMTYPEOPTIONS'].fields_by_name['possible_values']._loaded_options = None
    _globals['_ENUMTYPEOPTIONS'].fields_by_name['possible_values']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENTSCHEMA']._serialized_start = 186
    _globals['_DOCUMENTSCHEMA']._serialized_end = 612
    _globals['_PROPERTYDEFINITION']._serialized_start = 615
    _globals['_PROPERTYDEFINITION']._serialized_end = 1860
    _globals['_PROPERTYDEFINITION_SCHEMASOURCE']._serialized_start = 1657
    _globals['_PROPERTYDEFINITION_SCHEMASOURCE']._serialized_end = 1709
    _globals['_PROPERTYDEFINITION_RETRIEVALIMPORTANCE']._serialized_start = 1711
    _globals['_PROPERTYDEFINITION_RETRIEVALIMPORTANCE']._serialized_end = 1838
    _globals['_INTEGERTYPEOPTIONS']._serialized_start = 1862
    _globals['_INTEGERTYPEOPTIONS']._serialized_end = 1882
    _globals['_FLOATTYPEOPTIONS']._serialized_start = 1884
    _globals['_FLOATTYPEOPTIONS']._serialized_end = 1902
    _globals['_TEXTTYPEOPTIONS']._serialized_start = 1904
    _globals['_TEXTTYPEOPTIONS']._serialized_end = 1921
    _globals['_DATETIMETYPEOPTIONS']._serialized_start = 1923
    _globals['_DATETIMETYPEOPTIONS']._serialized_end = 1944
    _globals['_MAPTYPEOPTIONS']._serialized_start = 1946
    _globals['_MAPTYPEOPTIONS']._serialized_end = 1962
    _globals['_TIMESTAMPTYPEOPTIONS']._serialized_start = 1964
    _globals['_TIMESTAMPTYPEOPTIONS']._serialized_end = 1986
    _globals['_PROPERTYTYPEOPTIONS']._serialized_start = 1988
    _globals['_PROPERTYTYPEOPTIONS']._serialized_end = 2098
    _globals['_ENUMTYPEOPTIONS']._serialized_start = 2100
    _globals['_ENUMTYPEOPTIONS']._serialized_end = 2182