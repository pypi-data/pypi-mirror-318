"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1/document_schema.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/documentai/v1/document_schema.proto\x12\x1agoogle.cloud.documentai.v1"\xbd\x07\n\x0eDocumentSchema\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12K\n\x0centity_types\x18\x03 \x03(\x0b25.google.cloud.documentai.v1.DocumentSchema.EntityType\x12E\n\x08metadata\x18\x04 \x01(\x0b23.google.cloud.documentai.v1.DocumentSchema.Metadata\x1a\xd4\x04\n\nEntityType\x12W\n\x0benum_values\x18\x0e \x01(\x0b2@.google.cloud.documentai.v1.DocumentSchema.EntityType.EnumValuesH\x00\x12\x14\n\x0cdisplay_name\x18\r \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nbase_types\x18\x02 \x03(\t\x12R\n\nproperties\x18\x06 \x03(\x0b2>.google.cloud.documentai.v1.DocumentSchema.EntityType.Property\x1a\x1c\n\nEnumValues\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a\xb2\x02\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12\x12\n\nvalue_type\x18\x02 \x01(\t\x12f\n\x0foccurrence_type\x18\x03 \x01(\x0e2M.google.cloud.documentai.v1.DocumentSchema.EntityType.Property.OccurrenceType"\x85\x01\n\x0eOccurrenceType\x12\x1f\n\x1bOCCURRENCE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rOPTIONAL_ONCE\x10\x01\x12\x15\n\x11OPTIONAL_MULTIPLE\x10\x02\x12\x11\n\rREQUIRED_ONCE\x10\x03\x12\x15\n\x11REQUIRED_MULTIPLE\x10\x04B\x0e\n\x0cvalue_source\x1a\x94\x01\n\x08Metadata\x12\x19\n\x11document_splitter\x18\x01 \x01(\x08\x12&\n\x1edocument_allow_multiple_labels\x18\x02 \x01(\x08\x12%\n\x1dprefixed_naming_on_properties\x18\x06 \x01(\x08\x12\x1e\n\x16skip_naming_validation\x18\x07 \x01(\x08B\xd6\x01\n\x1ecom.google.cloud.documentai.v1B\x18DocumentAiDocumentSchemaP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1.document_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.documentai.v1B\x18DocumentAiDocumentSchemaP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1'
    _globals['_DOCUMENTSCHEMA']._serialized_start = 81
    _globals['_DOCUMENTSCHEMA']._serialized_end = 1038
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE']._serialized_start = 291
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE']._serialized_end = 887
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_ENUMVALUES']._serialized_start = 534
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_ENUMVALUES']._serialized_end = 562
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY']._serialized_start = 565
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY']._serialized_end = 871
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY_OCCURRENCETYPE']._serialized_start = 738
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY_OCCURRENCETYPE']._serialized_end = 871
    _globals['_DOCUMENTSCHEMA_METADATA']._serialized_start = 890
    _globals['_DOCUMENTSCHEMA_METADATA']._serialized_end = 1038