"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/discoveryengine/v1alpha/schema.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa8\x03\n\x06Schema\x120\n\rstruct_schema\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12\x15\n\x0bjson_schema\x18\x03 \x01(\tH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12M\n\rfield_configs\x18\x04 \x03(\x0b21.google.cloud.discoveryengine.v1alpha.FieldConfigB\x03\xe0A\x03:\xe8\x01\xeaA\xe4\x01\n%discoveryengine.googleapis.com/Schema\x12Pprojects/{project}/locations/{location}/dataStores/{data_store}/schemas/{schema}\x12iprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}B\x08\n\x06schema"\xad\x0e\n\x0bFieldConfig\x12\x17\n\nfield_path\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\nfield_type\x18\x02 \x01(\x0e2;.google.cloud.discoveryengine.v1alpha.FieldConfig.FieldTypeB\x03\xe0A\x03\x12[\n\x10indexable_option\x18\x03 \x01(\x0e2A.google.cloud.discoveryengine.v1alpha.FieldConfig.IndexableOption\x12j\n\x18dynamic_facetable_option\x18\x04 \x01(\x0e2H.google.cloud.discoveryengine.v1alpha.FieldConfig.DynamicFacetableOption\x12]\n\x11searchable_option\x18\x05 \x01(\x0e2B.google.cloud.discoveryengine.v1alpha.FieldConfig.SearchableOption\x12_\n\x12retrievable_option\x18\x06 \x01(\x0e2C.google.cloud.discoveryengine.v1alpha.FieldConfig.RetrievableOption\x12_\n\x12completable_option\x18\x08 \x01(\x0e2C.google.cloud.discoveryengine.v1alpha.FieldConfig.CompletableOption\x12b\n\x16recs_filterable_option\x18\t \x01(\x0e2B.google.cloud.discoveryengine.v1alpha.FieldConfig.FilterableOption\x12\x1e\n\x11key_property_type\x18\x07 \x01(\tB\x03\xe0A\x03\x12y\n!advanced_site_search_data_sources\x18\n \x03(\x0e2N.google.cloud.discoveryengine.v1alpha.FieldConfig.AdvancedSiteSearchDataSource\x12\x18\n\x10schema_org_paths\x18\x0b \x03(\t"\x84\x01\n\tFieldType\x12\x1a\n\x16FIELD_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06OBJECT\x10\x01\x12\n\n\x06STRING\x10\x02\x12\n\n\x06NUMBER\x10\x03\x12\x0b\n\x07INTEGER\x10\x04\x12\x0b\n\x07BOOLEAN\x10\x05\x12\x0f\n\x0bGEOLOCATION\x10\x06\x12\x0c\n\x08DATETIME\x10\x07"b\n\x0fIndexableOption\x12 \n\x1cINDEXABLE_OPTION_UNSPECIFIED\x10\x00\x12\x15\n\x11INDEXABLE_ENABLED\x10\x01\x12\x16\n\x12INDEXABLE_DISABLED\x10\x02"\x81\x01\n\x16DynamicFacetableOption\x12(\n$DYNAMIC_FACETABLE_OPTION_UNSPECIFIED\x10\x00\x12\x1d\n\x19DYNAMIC_FACETABLE_ENABLED\x10\x01\x12\x1e\n\x1aDYNAMIC_FACETABLE_DISABLED\x10\x02"f\n\x10SearchableOption\x12!\n\x1dSEARCHABLE_OPTION_UNSPECIFIED\x10\x00\x12\x16\n\x12SEARCHABLE_ENABLED\x10\x01\x12\x17\n\x13SEARCHABLE_DISABLED\x10\x02"j\n\x11RetrievableOption\x12"\n\x1eRETRIEVABLE_OPTION_UNSPECIFIED\x10\x00\x12\x17\n\x13RETRIEVABLE_ENABLED\x10\x01\x12\x18\n\x14RETRIEVABLE_DISABLED\x10\x02"j\n\x11CompletableOption\x12"\n\x1eCOMPLETABLE_OPTION_UNSPECIFIED\x10\x00\x12\x17\n\x13COMPLETABLE_ENABLED\x10\x01\x12\x18\n\x14COMPLETABLE_DISABLED\x10\x02"f\n\x10FilterableOption\x12!\n\x1dFILTERABLE_OPTION_UNSPECIFIED\x10\x00\x12\x16\n\x12FILTERABLE_ENABLED\x10\x01\x12\x17\n\x13FILTERABLE_DISABLED\x10\x02"\x94\x01\n\x1cAdvancedSiteSearchDataSource\x120\n,ADVANCED_SITE_SEARCH_DATA_SOURCE_UNSPECIFIED\x10\x00\x12\x0c\n\x08METATAGS\x10\x01\x12\x0b\n\x07PAGEMAP\x10\x02\x12\x17\n\x13URI_PATTERN_MAPPING\x10\x03\x12\x0e\n\nSCHEMA_ORG\x10\x04B\x97\x02\n(com.google.cloud.discoveryengine.v1alphaB\x0bSchemaProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0bSchemaProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_SCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SCHEMA'].fields_by_name['field_configs']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['field_configs']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEMA']._loaded_options = None
    _globals['_SCHEMA']._serialized_options = b'\xeaA\xe4\x01\n%discoveryengine.googleapis.com/Schema\x12Pprojects/{project}/locations/{location}/dataStores/{data_store}/schemas/{schema}\x12iprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}'
    _globals['_FIELDCONFIG'].fields_by_name['field_path']._loaded_options = None
    _globals['_FIELDCONFIG'].fields_by_name['field_path']._serialized_options = b'\xe0A\x02'
    _globals['_FIELDCONFIG'].fields_by_name['field_type']._loaded_options = None
    _globals['_FIELDCONFIG'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_FIELDCONFIG'].fields_by_name['key_property_type']._loaded_options = None
    _globals['_FIELDCONFIG'].fields_by_name['key_property_type']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEMA']._serialized_start = 182
    _globals['_SCHEMA']._serialized_end = 606
    _globals['_FIELDCONFIG']._serialized_start = 609
    _globals['_FIELDCONFIG']._serialized_end = 2446
    _globals['_FIELDCONFIG_FIELDTYPE']._serialized_start = 1507
    _globals['_FIELDCONFIG_FIELDTYPE']._serialized_end = 1639
    _globals['_FIELDCONFIG_INDEXABLEOPTION']._serialized_start = 1641
    _globals['_FIELDCONFIG_INDEXABLEOPTION']._serialized_end = 1739
    _globals['_FIELDCONFIG_DYNAMICFACETABLEOPTION']._serialized_start = 1742
    _globals['_FIELDCONFIG_DYNAMICFACETABLEOPTION']._serialized_end = 1871
    _globals['_FIELDCONFIG_SEARCHABLEOPTION']._serialized_start = 1873
    _globals['_FIELDCONFIG_SEARCHABLEOPTION']._serialized_end = 1975
    _globals['_FIELDCONFIG_RETRIEVABLEOPTION']._serialized_start = 1977
    _globals['_FIELDCONFIG_RETRIEVABLEOPTION']._serialized_end = 2083
    _globals['_FIELDCONFIG_COMPLETABLEOPTION']._serialized_start = 2085
    _globals['_FIELDCONFIG_COMPLETABLEOPTION']._serialized_end = 2191
    _globals['_FIELDCONFIG_FILTERABLEOPTION']._serialized_start = 2193
    _globals['_FIELDCONFIG_FILTERABLEOPTION']._serialized_end = 2295
    _globals['_FIELDCONFIG_ADVANCEDSITESEARCHDATASOURCE']._serialized_start = 2298
    _globals['_FIELDCONFIG_ADVANCEDSITESEARCHDATASOURCE']._serialized_end = 2446