"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/document_schema.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/documentai/v1beta3/document_schema.proto\x12\x1fgoogle.cloud.documentai.v1beta3"\xac\x02\n\x0eSummaryOptions\x12F\n\x06length\x18\x01 \x01(\x0e26.google.cloud.documentai.v1beta3.SummaryOptions.Length\x12F\n\x06format\x18\x02 \x01(\x0e26.google.cloud.documentai.v1beta3.SummaryOptions.Format"L\n\x06Length\x12\x16\n\x12LENGTH_UNSPECIFIED\x10\x00\x12\t\n\x05BRIEF\x10\x01\x12\x0c\n\x08MODERATE\x10\x02\x12\x11\n\rCOMPREHENSIVE\x10\x03"<\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tPARAGRAPH\x10\x01\x12\x0b\n\x07BULLETS\x10\x02"c\n\x17FieldExtractionMetadata\x12H\n\x0fsummary_options\x18\x02 \x01(\x0b2/.google.cloud.documentai.v1beta3.SummaryOptions"\x81\x01\n\x10PropertyMetadata\x12\x10\n\x08inactive\x18\x03 \x01(\x08\x12[\n\x19field_extraction_metadata\x18\t \x01(\x0b28.google.cloud.documentai.v1beta3.FieldExtractionMetadata"&\n\x12EntityTypeMetadata\x12\x10\n\x08inactive\x18\x05 \x01(\x08"\xa1\t\n\x0eDocumentSchema\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12P\n\x0centity_types\x18\x03 \x03(\x0b2:.google.cloud.documentai.v1beta3.DocumentSchema.EntityType\x12J\n\x08metadata\x18\x04 \x01(\x0b28.google.cloud.documentai.v1beta3.DocumentSchema.Metadata\x1a\xae\x06\n\nEntityType\x12\\\n\x0benum_values\x18\x0e \x01(\x0b2E.google.cloud.documentai.v1beta3.DocumentSchema.EntityType.EnumValuesH\x00\x12\x14\n\x0cdisplay_name\x18\r \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x0f \x01(\t\x12\x12\n\nbase_types\x18\x02 \x03(\t\x12W\n\nproperties\x18\x06 \x03(\x0b2C.google.cloud.documentai.v1beta3.DocumentSchema.EntityType.Property\x12Q\n\x14entity_type_metadata\x18\x0b \x01(\x0b23.google.cloud.documentai.v1beta3.EntityTypeMetadata\x1a\x1c\n\nEnumValues\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a\x9a\x03\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12\x12\n\nvalue_type\x18\x02 \x01(\t\x12k\n\x0foccurrence_type\x18\x03 \x01(\x0e2R.google.cloud.documentai.v1beta3.DocumentSchema.EntityType.Property.OccurrenceType\x12L\n\x11property_metadata\x18\x05 \x01(\x0b21.google.cloud.documentai.v1beta3.PropertyMetadata"\x85\x01\n\x0eOccurrenceType\x12\x1f\n\x1bOCCURRENCE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rOPTIONAL_ONCE\x10\x01\x12\x15\n\x11OPTIONAL_MULTIPLE\x10\x02\x12\x11\n\rREQUIRED_ONCE\x10\x03\x12\x15\n\x11REQUIRED_MULTIPLE\x10\x04B\x0e\n\x0cvalue_source\x1a\x94\x01\n\x08Metadata\x12\x19\n\x11document_splitter\x18\x01 \x01(\x08\x12&\n\x1edocument_allow_multiple_labels\x18\x02 \x01(\x08\x12%\n\x1dprefixed_naming_on_properties\x18\x06 \x01(\x08\x12\x1e\n\x16skip_naming_validation\x18\x07 \x01(\x08B\xef\x01\n#com.google.cloud.documentai.v1beta3B\x18DocumentAiDocumentSchemaP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.document_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\x18DocumentAiDocumentSchemaP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3'
    _globals['_SUMMARYOPTIONS']._serialized_start = 91
    _globals['_SUMMARYOPTIONS']._serialized_end = 391
    _globals['_SUMMARYOPTIONS_LENGTH']._serialized_start = 253
    _globals['_SUMMARYOPTIONS_LENGTH']._serialized_end = 329
    _globals['_SUMMARYOPTIONS_FORMAT']._serialized_start = 331
    _globals['_SUMMARYOPTIONS_FORMAT']._serialized_end = 391
    _globals['_FIELDEXTRACTIONMETADATA']._serialized_start = 393
    _globals['_FIELDEXTRACTIONMETADATA']._serialized_end = 492
    _globals['_PROPERTYMETADATA']._serialized_start = 495
    _globals['_PROPERTYMETADATA']._serialized_end = 624
    _globals['_ENTITYTYPEMETADATA']._serialized_start = 626
    _globals['_ENTITYTYPEMETADATA']._serialized_end = 664
    _globals['_DOCUMENTSCHEMA']._serialized_start = 667
    _globals['_DOCUMENTSCHEMA']._serialized_end = 1852
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE']._serialized_start = 887
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE']._serialized_end = 1701
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_ENUMVALUES']._serialized_start = 1244
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_ENUMVALUES']._serialized_end = 1272
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY']._serialized_start = 1275
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY']._serialized_end = 1685
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY_OCCURRENCETYPE']._serialized_start = 1552
    _globals['_DOCUMENTSCHEMA_ENTITYTYPE_PROPERTY_OCCURRENCETYPE']._serialized_end = 1685
    _globals['_DOCUMENTSCHEMA_METADATA']._serialized_start = 1704
    _globals['_DOCUMENTSCHEMA_METADATA']._serialized_end = 1852