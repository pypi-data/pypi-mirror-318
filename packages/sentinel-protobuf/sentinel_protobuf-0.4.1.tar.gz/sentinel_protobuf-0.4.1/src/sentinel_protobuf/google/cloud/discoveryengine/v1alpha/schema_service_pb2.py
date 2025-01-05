"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/schema_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import schema_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_schema__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/discoveryengine/v1alpha/schema_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/discoveryengine/v1alpha/schema.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"O\n\x10GetSchemaRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Schema"}\n\x12ListSchemasRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"m\n\x13ListSchemasResponse\x12=\n\x07schemas\x18\x01 \x03(\x0b2,.google.cloud.discoveryengine.v1alpha.Schema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb2\x01\n\x13CreateSchemaRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12A\n\x06schema\x18\x02 \x01(\x0b2,.google.cloud.discoveryengine.v1alpha.SchemaB\x03\xe0A\x02\x12\x16\n\tschema_id\x18\x03 \x01(\tB\x03\xe0A\x02"o\n\x13UpdateSchemaRequest\x12A\n\x06schema\x18\x01 \x01(\x0b2,.google.cloud.discoveryengine.v1alpha.SchemaB\x03\xe0A\x02\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"R\n\x13DeleteSchemaRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Schema"x\n\x14CreateSchemaMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"x\n\x14UpdateSchemaMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"x\n\x14DeleteSchemaMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp2\x9f\x0e\n\rSchemaService\x12\x90\x02\n\tGetSchema\x126.google.cloud.discoveryengine.v1alpha.GetSchemaRequest\x1a,.google.cloud.discoveryengine.v1alpha.Schema"\x9c\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01\x12=/v1alpha/{name=projects/*/locations/*/dataStores/*/schemas/*}ZM\x12K/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}\x12\xa3\x02\n\x0bListSchemas\x128.google.cloud.discoveryengine.v1alpha.ListSchemasRequest\x1a9.google.cloud.discoveryengine.v1alpha.ListSchemasResponse"\x9e\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8e\x01\x12=/v1alpha/{parent=projects/*/locations/*/dataStores/*}/schemasZM\x12K/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas\x12\x95\x03\n\x0cCreateSchema\x129.google.cloud.discoveryengine.v1alpha.CreateSchemaRequest\x1a\x1d.google.longrunning.Operation"\xaa\x02\xcaAh\n+google.cloud.discoveryengine.v1alpha.Schema\x129google.cloud.discoveryengine.v1alpha.CreateSchemaMetadata\xdaA\x17parent,schema,schema_id\x82\xd3\xe4\x93\x02\x9e\x01"=/v1alpha/{parent=projects/*/locations/*/dataStores/*}/schemas:\x06schemaZU"K/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas:\x06schema\x12\x89\x03\n\x0cUpdateSchema\x129.google.cloud.discoveryengine.v1alpha.UpdateSchemaRequest\x1a\x1d.google.longrunning.Operation"\x9e\x02\xcaAh\n+google.cloud.discoveryengine.v1alpha.Schema\x129google.cloud.discoveryengine.v1alpha.UpdateSchemaMetadata\x82\xd3\xe4\x93\x02\xac\x012D/v1alpha/{schema.name=projects/*/locations/*/dataStores/*/schemas/*}:\x06schemaZ\\2R/v1alpha/{schema.name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}:\x06schema\x12\xdc\x02\n\x0cDeleteSchema\x129.google.cloud.discoveryengine.v1alpha.DeleteSchemaRequest\x1a\x1d.google.longrunning.Operation"\xf1\x01\xcaAR\n\x15google.protobuf.Empty\x129google.cloud.discoveryengine.v1alpha.DeleteSchemaMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01*=/v1alpha/{name=projects/*/locations/*/dataStores/*/schemas/*}ZM*K/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9e\x02\n(com.google.cloud.discoveryengine.v1alphaB\x12SchemaServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.schema_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x12SchemaServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_GETSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Schema"
    _globals['_LISTSCHEMASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSCHEMASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema_id']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_UPDATESCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESCHEMAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Schema"
    _globals['_SCHEMASERVICE']._loaded_options = None
    _globals['_SCHEMASERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SCHEMASERVICE'].methods_by_name['GetSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['GetSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01\x12=/v1alpha/{name=projects/*/locations/*/dataStores/*/schemas/*}ZM\x12K/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}'
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemas']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemas']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8e\x01\x12=/v1alpha/{parent=projects/*/locations/*/dataStores/*}/schemasZM\x12K/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas'
    _globals['_SCHEMASERVICE'].methods_by_name['CreateSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['CreateSchema']._serialized_options = b'\xcaAh\n+google.cloud.discoveryengine.v1alpha.Schema\x129google.cloud.discoveryengine.v1alpha.CreateSchemaMetadata\xdaA\x17parent,schema,schema_id\x82\xd3\xe4\x93\x02\x9e\x01"=/v1alpha/{parent=projects/*/locations/*/dataStores/*}/schemas:\x06schemaZU"K/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas:\x06schema'
    _globals['_SCHEMASERVICE'].methods_by_name['UpdateSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['UpdateSchema']._serialized_options = b'\xcaAh\n+google.cloud.discoveryengine.v1alpha.Schema\x129google.cloud.discoveryengine.v1alpha.UpdateSchemaMetadata\x82\xd3\xe4\x93\x02\xac\x012D/v1alpha/{schema.name=projects/*/locations/*/dataStores/*/schemas/*}:\x06schemaZ\\2R/v1alpha/{schema.name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}:\x06schema'
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchema']._serialized_options = b'\xcaAR\n\x15google.protobuf.Empty\x129google.cloud.discoveryengine.v1alpha.DeleteSchemaMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x8e\x01*=/v1alpha/{name=projects/*/locations/*/dataStores/*/schemas/*}ZM*K/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}'
    _globals['_GETSCHEMAREQUEST']._serialized_start = 364
    _globals['_GETSCHEMAREQUEST']._serialized_end = 443
    _globals['_LISTSCHEMASREQUEST']._serialized_start = 445
    _globals['_LISTSCHEMASREQUEST']._serialized_end = 570
    _globals['_LISTSCHEMASRESPONSE']._serialized_start = 572
    _globals['_LISTSCHEMASRESPONSE']._serialized_end = 681
    _globals['_CREATESCHEMAREQUEST']._serialized_start = 684
    _globals['_CREATESCHEMAREQUEST']._serialized_end = 862
    _globals['_UPDATESCHEMAREQUEST']._serialized_start = 864
    _globals['_UPDATESCHEMAREQUEST']._serialized_end = 975
    _globals['_DELETESCHEMAREQUEST']._serialized_start = 977
    _globals['_DELETESCHEMAREQUEST']._serialized_end = 1059
    _globals['_CREATESCHEMAMETADATA']._serialized_start = 1061
    _globals['_CREATESCHEMAMETADATA']._serialized_end = 1181
    _globals['_UPDATESCHEMAMETADATA']._serialized_start = 1183
    _globals['_UPDATESCHEMAMETADATA']._serialized_end = 1303
    _globals['_DELETESCHEMAMETADATA']._serialized_start = 1305
    _globals['_DELETESCHEMAMETADATA']._serialized_end = 1425
    _globals['_SCHEMASERVICE']._serialized_start = 1428
    _globals['_SCHEMASERVICE']._serialized_end = 3251