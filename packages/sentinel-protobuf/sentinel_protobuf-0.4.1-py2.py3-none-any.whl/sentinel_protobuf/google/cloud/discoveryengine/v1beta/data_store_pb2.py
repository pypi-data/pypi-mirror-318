"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/data_store.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_common__pb2
from .....google.cloud.discoveryengine.v1beta import document_processing_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_document__processing__config__pb2
from .....google.cloud.discoveryengine.v1beta import schema_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_schema__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/discoveryengine/v1beta/data_store.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/common.proto\x1aDgoogle/cloud/discoveryengine/v1beta/document_processing_config.proto\x1a0google/cloud/discoveryengine/v1beta/schema.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe0\r\n\tDataStore\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12U\n\x11industry_vertical\x18\x03 \x01(\x0e25.google.cloud.discoveryengine.v1beta.IndustryVerticalB\x03\xe0A\x05\x12I\n\x0esolution_types\x18\x05 \x03(\x0e21.google.cloud.discoveryengine.v1beta.SolutionType\x12\x1e\n\x11default_schema_id\x18\x07 \x01(\tB\x03\xe0A\x03\x12Y\n\x0econtent_config\x18\x06 \x01(\x0e2<.google.cloud.discoveryengine.v1beta.DataStore.ContentConfigB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\rlanguage_info\x18\x0e \x01(\x0b21.google.cloud.discoveryengine.v1beta.LanguageInfo\x12\x86\x01\n+natural_language_query_understanding_config\x18" \x01(\x0b2L.google.cloud.discoveryengine.v1beta.NaturalLanguageQueryUnderstandingConfigB\x03\xe0A\x01\x12a\n\x12billing_estimation\x18\x17 \x01(\x0b2@.google.cloud.discoveryengine.v1beta.DataStore.BillingEstimationB\x03\xe0A\x03\x12N\n\x10workspace_config\x18\x19 \x01(\x0b24.google.cloud.discoveryengine.v1beta.WorkspaceConfig\x12a\n\x1adocument_processing_config\x18\x1b \x01(\x0b2=.google.cloud.discoveryengine.v1beta.DocumentProcessingConfig\x12D\n\x0fstarting_schema\x18\x1c \x01(\x0b2+.google.cloud.discoveryengine.v1beta.Schema\x12m\n\x19serving_config_data_store\x18\x1e \x01(\x0b2E.google.cloud.discoveryengine.v1beta.DataStore.ServingConfigDataStoreB\x03\xe0A\x01\x1a\xae\x02\n\x11BillingEstimation\x12\x1c\n\x14structured_data_size\x18\x01 \x01(\x03\x12\x1e\n\x16unstructured_data_size\x18\x02 \x01(\x03\x12\x19\n\x11website_data_size\x18\x03 \x01(\x03\x12?\n\x1bstructured_data_update_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12A\n\x1dunstructured_data_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x18website_data_update_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a6\n\x16ServingConfigDataStore\x12\x1c\n\x14disabled_for_serving\x18\x01 \x01(\x08"\x7f\n\rContentConfig\x12\x1e\n\x1aCONTENT_CONFIG_UNSPECIFIED\x10\x00\x12\x0e\n\nNO_CONTENT\x10\x01\x12\x14\n\x10CONTENT_REQUIRED\x10\x02\x12\x12\n\x0ePUBLIC_WEBSITE\x10\x03\x12\x14\n\x10GOOGLE_WORKSPACE\x10\x04:\xc9\x01\xeaA\xc5\x01\n(discoveryengine.googleapis.com/DataStore\x12?projects/{project}/locations/{location}/dataStores/{data_store}\x12Xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}"x\n\x0cLanguageInfo\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12%\n\x18normalized_language_code\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08language\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06region\x18\x04 \x01(\tB\x03\xe0A\x03"\xc3\x01\n\'NaturalLanguageQueryUnderstandingConfig\x12_\n\x04mode\x18\x01 \x01(\x0e2Q.google.cloud.discoveryengine.v1beta.NaturalLanguageQueryUnderstandingConfig.Mode"7\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x0b\n\x07ENABLED\x10\x02"\xe6\x02\n\x0fWorkspaceConfig\x12G\n\x04type\x18\x01 \x01(\x0e29.google.cloud.discoveryengine.v1beta.WorkspaceConfig.Type\x12\x1a\n\x12dasher_customer_id\x18\x02 \x01(\t\x12(\n\x1bsuper_admin_service_account\x18\x04 \x01(\tB\x03\xe0A\x01\x12&\n\x19super_admin_email_address\x18\x05 \x01(\tB\x03\xe0A\x01"\x9b\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cGOOGLE_DRIVE\x10\x01\x12\x0f\n\x0bGOOGLE_MAIL\x10\x02\x12\x10\n\x0cGOOGLE_SITES\x10\x03\x12\x13\n\x0fGOOGLE_CALENDAR\x10\x04\x12\x0f\n\x0bGOOGLE_CHAT\x10\x05\x12\x11\n\rGOOGLE_GROUPS\x10\x06\x12\x0f\n\x0bGOOGLE_KEEP\x10\x07B\x95\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0eDataStoreProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.data_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0eDataStoreProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_DATASTORE'].fields_by_name['name']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_DATASTORE'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATASTORE'].fields_by_name['industry_vertical']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['industry_vertical']._serialized_options = b'\xe0A\x05'
    _globals['_DATASTORE'].fields_by_name['default_schema_id']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['default_schema_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['content_config']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['content_config']._serialized_options = b'\xe0A\x05'
    _globals['_DATASTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['natural_language_query_understanding_config']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['natural_language_query_understanding_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE'].fields_by_name['billing_estimation']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['billing_estimation']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['serving_config_data_store']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['serving_config_data_store']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE']._loaded_options = None
    _globals['_DATASTORE']._serialized_options = b'\xeaA\xc5\x01\n(discoveryengine.googleapis.com/DataStore\x12?projects/{project}/locations/{location}/dataStores/{data_store}\x12Xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}'
    _globals['_LANGUAGEINFO'].fields_by_name['normalized_language_code']._loaded_options = None
    _globals['_LANGUAGEINFO'].fields_by_name['normalized_language_code']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGEINFO'].fields_by_name['language']._loaded_options = None
    _globals['_LANGUAGEINFO'].fields_by_name['language']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGEINFO'].fields_by_name['region']._loaded_options = None
    _globals['_LANGUAGEINFO'].fields_by_name['region']._serialized_options = b'\xe0A\x03'
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_service_account']._loaded_options = None
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_service_account']._serialized_options = b'\xe0A\x01'
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_email_address']._loaded_options = None
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_email_address']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE']._serialized_start = 357
    _globals['_DATASTORE']._serialized_end = 2117
    _globals['_DATASTORE_BILLINGESTIMATION']._serialized_start = 1426
    _globals['_DATASTORE_BILLINGESTIMATION']._serialized_end = 1728
    _globals['_DATASTORE_SERVINGCONFIGDATASTORE']._serialized_start = 1730
    _globals['_DATASTORE_SERVINGCONFIGDATASTORE']._serialized_end = 1784
    _globals['_DATASTORE_CONTENTCONFIG']._serialized_start = 1786
    _globals['_DATASTORE_CONTENTCONFIG']._serialized_end = 1913
    _globals['_LANGUAGEINFO']._serialized_start = 2119
    _globals['_LANGUAGEINFO']._serialized_end = 2239
    _globals['_NATURALLANGUAGEQUERYUNDERSTANDINGCONFIG']._serialized_start = 2242
    _globals['_NATURALLANGUAGEQUERYUNDERSTANDINGCONFIG']._serialized_end = 2437
    _globals['_NATURALLANGUAGEQUERYUNDERSTANDINGCONFIG_MODE']._serialized_start = 2382
    _globals['_NATURALLANGUAGEQUERYUNDERSTANDINGCONFIG_MODE']._serialized_end = 2437
    _globals['_WORKSPACECONFIG']._serialized_start = 2440
    _globals['_WORKSPACECONFIG']._serialized_end = 2798
    _globals['_WORKSPACECONFIG_TYPE']._serialized_start = 2643
    _globals['_WORKSPACECONFIG_TYPE']._serialized_end = 2798