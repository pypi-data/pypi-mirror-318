"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/connection.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.connectors.v1 import authconfig_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_authconfig__pb2
from .....google.cloud.connectors.v1 import common_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_common__pb2
from .....google.cloud.connectors.v1 import destination_config_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_destination__config__pb2
from .....google.cloud.connectors.v1 import ssl_config_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_ssl__config__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/connectors/v1/connection.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/connectors/v1/authconfig.proto\x1a\'google/cloud/connectors/v1/common.proto\x1a3google/cloud/connectors/v1/destination_config.proto\x1a+google/cloud/connectors/v1/ssl_config.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x08\n\nConnection\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x06labels\x18\x04 \x03(\x0b22.google.cloud.connectors.v1.Connection.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12M\n\x11connector_version\x18\x06 \x01(\tB2\xe0A\x02\xfaA,\n*connectors.googleapis.com/ConnectorVersion\x12A\n\x06status\x18\x07 \x01(\x0b2,.google.cloud.connectors.v1.ConnectionStatusB\x03\xe0A\x03\x12I\n\x10config_variables\x18\x08 \x03(\x0b2*.google.cloud.connectors.v1.ConfigVariableB\x03\xe0A\x01\x12@\n\x0bauth_config\x18\t \x01(\x0b2&.google.cloud.connectors.v1.AuthConfigB\x03\xe0A\x01\x12@\n\x0block_config\x18\n \x01(\x0b2&.google.cloud.connectors.v1.LockConfigB\x03\xe0A\x01\x12O\n\x13destination_configs\x18\x12 \x03(\x0b2-.google.cloud.connectors.v1.DestinationConfigB\x03\xe0A\x01\x12\x1b\n\x0eimage_location\x18\x0b \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fservice_account\x18\x0c \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11service_directory\x18\r \x01(\tB\x03\xe0A\x03\x12!\n\x14envoy_image_location\x18\x0f \x01(\tB\x03\xe0A\x03\x12\x16\n\tsuspended\x18\x11 \x01(\x08B\x03\xe0A\x01\x12@\n\x0bnode_config\x18\x13 \x01(\x0b2&.google.cloud.connectors.v1.NodeConfigB\x03\xe0A\x01\x12>\n\nssl_config\x18\x15 \x01(\x0b2%.google.cloud.connectors.v1.SslConfigB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:k\xeaAh\n$connectors.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}"<\n\nNodeConfig\x12\x16\n\x0emin_node_count\x18\x01 \x01(\x05\x12\x16\n\x0emax_node_count\x18\x02 \x01(\x05"\xea\x03\n\x18ConnectionSchemaMetadata\x12\x15\n\x08entities\x18\x01 \x03(\tB\x03\xe0A\x03\x12\x14\n\x07actions\x18\x02 \x03(\tB\x03\xe0A\x03\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0crefresh_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12N\n\x05state\x18\x06 \x01(\x0e2:.google.cloud.connectors.v1.ConnectionSchemaMetadata.StateB\x03\xe0A\x03";\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nREFRESHING\x10\x01\x12\x0b\n\x07UPDATED\x10\x02:\x93\x01\xeaA\x8f\x01\n2connectors.googleapis.com/ConnectionSchemaMetadata\x12Yprojects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata"\xf2\x02\n\x13RuntimeEntitySchema\x12\x13\n\x06entity\x18\x01 \x01(\tB\x03\xe0A\x03\x12J\n\x06fields\x18\x02 \x03(\x0b25.google.cloud.connectors.v1.RuntimeEntitySchema.FieldB\x03\xe0A\x03\x1a\xf9\x01\n\x05Field\x12\r\n\x05field\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x127\n\tdata_type\x18\x03 \x01(\x0e2$.google.cloud.connectors.v1.DataType\x12\x0b\n\x03key\x18\x04 \x01(\x08\x12\x10\n\x08readonly\x18\x05 \x01(\x08\x12\x10\n\x08nullable\x18\x06 \x01(\x08\x12-\n\rdefault_value\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x123\n\x12additional_details\x18\x08 \x01(\x0b2\x17.google.protobuf.Struct"\x8b\x04\n\x13RuntimeActionSchema\x12\x13\n\x06action\x18\x01 \x01(\tB\x03\xe0A\x03\x12]\n\x10input_parameters\x18\x02 \x03(\x0b2>.google.cloud.connectors.v1.RuntimeActionSchema.InputParameterB\x03\xe0A\x03\x12\\\n\x0fresult_metadata\x18\x03 \x03(\x0b2>.google.cloud.connectors.v1.RuntimeActionSchema.ResultMetadataB\x03\xe0A\x03\x1a\xb2\x01\n\x0eInputParameter\x12\x11\n\tparameter\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x127\n\tdata_type\x18\x03 \x01(\x0e2$.google.cloud.connectors.v1.DataType\x12\x10\n\x08nullable\x18\x04 \x01(\x08\x12-\n\rdefault_value\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x1am\n\x0eResultMetadata\x12\r\n\x05field\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x127\n\tdata_type\x18\x03 \x01(\x0e2$.google.cloud.connectors.v1.DataType",\n\nLockConfig\x12\x0e\n\x06locked\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\t"\xd9\x01\n\x16ListConnectionsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$connectors.googleapis.com/Connection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x128\n\x04view\x18\x06 \x01(\x0e2*.google.cloud.connectors.v1.ConnectionView"\x84\x01\n\x17ListConnectionsResponse\x12;\n\x0bconnections\x18\x01 \x03(\x0b2&.google.cloud.connectors.v1.Connection\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x8c\x01\n\x14GetConnectionRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection\x128\n\x04view\x18\x02 \x01(\x0e2*.google.cloud.connectors.v1.ConnectionView"\xb4\x01\n\x17CreateConnectionRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$connectors.googleapis.com/Connection\x12\x1a\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\nconnection\x18\x03 \x01(\x0b2&.google.cloud.connectors.v1.ConnectionB\x03\xe0A\x02"\x90\x01\n\x17UpdateConnectionRequest\x12?\n\nconnection\x18\x01 \x01(\x0b2&.google.cloud.connectors.v1.ConnectionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x17DeleteConnectionRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection"n\n"GetConnectionSchemaMetadataRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2connectors.googleapis.com/ConnectionSchemaMetadata"r\n&RefreshConnectionSchemaMetadataRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2connectors.googleapis.com/ConnectionSchemaMetadata"\x9b\x01\n\x1fListRuntimeEntitySchemasRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x02"\x8c\x01\n ListRuntimeEntitySchemasResponse\x12O\n\x16runtime_entity_schemas\x18\x01 \x03(\x0b2/.google.cloud.connectors.v1.RuntimeEntitySchema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9b\x01\n\x1fListRuntimeActionSchemasRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x02"\x8c\x01\n ListRuntimeActionSchemasResponse\x12O\n\x16runtime_action_schemas\x18\x01 \x03(\x0b2/.google.cloud.connectors.v1.RuntimeActionSchema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x86\x02\n\x10ConnectionStatus\x12A\n\x05state\x18\x01 \x01(\x0e22.google.cloud.connectors.v1.ConnectionStatus.State\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t"\x89\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08INACTIVE\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x0c\n\x08UPDATING\x10\x05\x12\t\n\x05ERROR\x10\x06\x12\x1a\n\x16AUTHORIZATION_REQUIRED\x10\x07*\xae\x08\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\rDATA_TYPE_INT\x10\x01\x1a\x02\x08\x01\x12\x16\n\x12DATA_TYPE_SMALLINT\x10\x02\x12\x14\n\x10DATA_TYPE_DOUBLE\x10\x03\x12\x12\n\x0eDATA_TYPE_DATE\x10\x04\x12\x1a\n\x12DATA_TYPE_DATETIME\x10\x05\x1a\x02\x08\x01\x12\x12\n\x0eDATA_TYPE_TIME\x10\x06\x12\x18\n\x10DATA_TYPE_STRING\x10\x07\x1a\x02\x08\x01\x12\x16\n\x0eDATA_TYPE_LONG\x10\x08\x1a\x02\x08\x01\x12\x15\n\x11DATA_TYPE_BOOLEAN\x10\t\x12\x15\n\x11DATA_TYPE_DECIMAL\x10\n\x12\x16\n\x0eDATA_TYPE_UUID\x10\x0b\x1a\x02\x08\x01\x12\x12\n\x0eDATA_TYPE_BLOB\x10\x0c\x12\x11\n\rDATA_TYPE_BIT\x10\r\x12\x15\n\x11DATA_TYPE_TINYINT\x10\x0e\x12\x15\n\x11DATA_TYPE_INTEGER\x10\x0f\x12\x14\n\x10DATA_TYPE_BIGINT\x10\x10\x12\x13\n\x0fDATA_TYPE_FLOAT\x10\x11\x12\x12\n\x0eDATA_TYPE_REAL\x10\x12\x12\x15\n\x11DATA_TYPE_NUMERIC\x10\x13\x12\x12\n\x0eDATA_TYPE_CHAR\x10\x14\x12\x15\n\x11DATA_TYPE_VARCHAR\x10\x15\x12\x19\n\x15DATA_TYPE_LONGVARCHAR\x10\x16\x12\x17\n\x13DATA_TYPE_TIMESTAMP\x10\x17\x12\x13\n\x0fDATA_TYPE_NCHAR\x10\x18\x12\x16\n\x12DATA_TYPE_NVARCHAR\x10\x19\x12\x1a\n\x16DATA_TYPE_LONGNVARCHAR\x10\x1a\x12\x12\n\x0eDATA_TYPE_NULL\x10\x1b\x12\x13\n\x0fDATA_TYPE_OTHER\x10\x1c\x12\x19\n\x15DATA_TYPE_JAVA_OBJECT\x10\x1d\x12\x16\n\x12DATA_TYPE_DISTINCT\x10\x1e\x12\x14\n\x10DATA_TYPE_STRUCT\x10\x1f\x12\x13\n\x0fDATA_TYPE_ARRAY\x10 \x12\x12\n\x0eDATA_TYPE_CLOB\x10!\x12\x11\n\rDATA_TYPE_REF\x10"\x12\x16\n\x12DATA_TYPE_DATALINK\x10#\x12\x13\n\x0fDATA_TYPE_ROWID\x10$\x12\x14\n\x10DATA_TYPE_BINARY\x10%\x12\x17\n\x13DATA_TYPE_VARBINARY\x10&\x12\x1b\n\x17DATA_TYPE_LONGVARBINARY\x10\'\x12\x13\n\x0fDATA_TYPE_NCLOB\x10(\x12\x14\n\x10DATA_TYPE_SQLXML\x10)\x12\x18\n\x14DATA_TYPE_REF_CURSOR\x10*\x12 \n\x1cDATA_TYPE_TIME_WITH_TIMEZONE\x10+\x12%\n!DATA_TYPE_TIMESTAMP_WITH_TIMEZONE\x10,*F\n\x0eConnectionView\x12\x1f\n\x1bCONNECTION_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02Bs\n\x1ecom.google.cloud.connectors.v1B\x0fConnectionProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x0fConnectionProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_INT']._loaded_options = None
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_INT']._serialized_options = b'\x08\x01'
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_DATETIME']._loaded_options = None
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_DATETIME']._serialized_options = b'\x08\x01'
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_STRING']._loaded_options = None
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_STRING']._serialized_options = b'\x08\x01'
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_LONG']._loaded_options = None
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_LONG']._serialized_options = b'\x08\x01'
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_UUID']._loaded_options = None
    _globals['_DATATYPE'].values_by_name['DATA_TYPE_UUID']._serialized_options = b'\x08\x01'
    _globals['_CONNECTION_LABELSENTRY']._loaded_options = None
    _globals['_CONNECTION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONNECTION'].fields_by_name['name']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['labels']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['description']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['connector_version']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['connector_version']._serialized_options = b'\xe0A\x02\xfaA,\n*connectors.googleapis.com/ConnectorVersion'
    _globals['_CONNECTION'].fields_by_name['status']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['config_variables']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['config_variables']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['auth_config']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['auth_config']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['lock_config']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['lock_config']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['destination_configs']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['destination_configs']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['image_location']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['image_location']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['service_account']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['service_directory']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['service_directory']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['envoy_image_location']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['envoy_image_location']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['suspended']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['suspended']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['node_config']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['node_config']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION'].fields_by_name['ssl_config']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['ssl_config']._serialized_options = b'\xe0A\x01'
    _globals['_CONNECTION']._loaded_options = None
    _globals['_CONNECTION']._serialized_options = b'\xeaAh\n$connectors.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}'
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['entities']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['entities']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['actions']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['actions']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['refresh_time']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['refresh_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['state']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSCHEMAMETADATA']._loaded_options = None
    _globals['_CONNECTIONSCHEMAMETADATA']._serialized_options = b'\xeaA\x8f\x01\n2connectors.googleapis.com/ConnectionSchemaMetadata\x12Yprojects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata'
    _globals['_RUNTIMEENTITYSCHEMA'].fields_by_name['entity']._loaded_options = None
    _globals['_RUNTIMEENTITYSCHEMA'].fields_by_name['entity']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMEENTITYSCHEMA'].fields_by_name['fields']._loaded_options = None
    _globals['_RUNTIMEENTITYSCHEMA'].fields_by_name['fields']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMEACTIONSCHEMA'].fields_by_name['action']._loaded_options = None
    _globals['_RUNTIMEACTIONSCHEMA'].fields_by_name['action']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMEACTIONSCHEMA'].fields_by_name['input_parameters']._loaded_options = None
    _globals['_RUNTIMEACTIONSCHEMA'].fields_by_name['input_parameters']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMEACTIONSCHEMA'].fields_by_name['result_metadata']._loaded_options = None
    _globals['_RUNTIMEACTIONSCHEMA'].fields_by_name['result_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$connectors.googleapis.com/Connection'
    _globals['_GETCONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection'
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$connectors.googleapis.com/Connection'
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection_id']._loaded_options = None
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection']._loaded_options = None
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['connection']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['connection']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection'
    _globals['_GETCONNECTIONSCHEMAMETADATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTIONSCHEMAMETADATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2connectors.googleapis.com/ConnectionSchemaMetadata'
    _globals['_REFRESHCONNECTIONSCHEMAMETADATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REFRESHCONNECTIONSCHEMAMETADATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2connectors.googleapis.com/ConnectionSchemaMetadata'
    _globals['_LISTRUNTIMEENTITYSCHEMASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRUNTIMEENTITYSCHEMASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection'
    _globals['_LISTRUNTIMEENTITYSCHEMASREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTRUNTIMEENTITYSCHEMASREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_LISTRUNTIMEACTIONSCHEMASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRUNTIMEACTIONSCHEMASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$connectors.googleapis.com/Connection'
    _globals['_LISTRUNTIMEACTIONSCHEMASREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTRUNTIMEACTIONSCHEMASREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_DATATYPE']._serialized_start = 5038
    _globals['_DATATYPE']._serialized_end = 6108
    _globals['_CONNECTIONVIEW']._serialized_start = 6110
    _globals['_CONNECTIONVIEW']._serialized_end = 6180
    _globals['_CONNECTION']._serialized_start = 417
    _globals['_CONNECTION']._serialized_end = 1525
    _globals['_CONNECTION_LABELSENTRY']._serialized_start = 1371
    _globals['_CONNECTION_LABELSENTRY']._serialized_end = 1416
    _globals['_NODECONFIG']._serialized_start = 1527
    _globals['_NODECONFIG']._serialized_end = 1587
    _globals['_CONNECTIONSCHEMAMETADATA']._serialized_start = 1590
    _globals['_CONNECTIONSCHEMAMETADATA']._serialized_end = 2080
    _globals['_CONNECTIONSCHEMAMETADATA_STATE']._serialized_start = 1871
    _globals['_CONNECTIONSCHEMAMETADATA_STATE']._serialized_end = 1930
    _globals['_RUNTIMEENTITYSCHEMA']._serialized_start = 2083
    _globals['_RUNTIMEENTITYSCHEMA']._serialized_end = 2453
    _globals['_RUNTIMEENTITYSCHEMA_FIELD']._serialized_start = 2204
    _globals['_RUNTIMEENTITYSCHEMA_FIELD']._serialized_end = 2453
    _globals['_RUNTIMEACTIONSCHEMA']._serialized_start = 2456
    _globals['_RUNTIMEACTIONSCHEMA']._serialized_end = 2979
    _globals['_RUNTIMEACTIONSCHEMA_INPUTPARAMETER']._serialized_start = 2690
    _globals['_RUNTIMEACTIONSCHEMA_INPUTPARAMETER']._serialized_end = 2868
    _globals['_RUNTIMEACTIONSCHEMA_RESULTMETADATA']._serialized_start = 2870
    _globals['_RUNTIMEACTIONSCHEMA_RESULTMETADATA']._serialized_end = 2979
    _globals['_LOCKCONFIG']._serialized_start = 2981
    _globals['_LOCKCONFIG']._serialized_end = 3025
    _globals['_LISTCONNECTIONSREQUEST']._serialized_start = 3028
    _globals['_LISTCONNECTIONSREQUEST']._serialized_end = 3245
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_start = 3248
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_end = 3380
    _globals['_GETCONNECTIONREQUEST']._serialized_start = 3383
    _globals['_GETCONNECTIONREQUEST']._serialized_end = 3523
    _globals['_CREATECONNECTIONREQUEST']._serialized_start = 3526
    _globals['_CREATECONNECTIONREQUEST']._serialized_end = 3706
    _globals['_UPDATECONNECTIONREQUEST']._serialized_start = 3709
    _globals['_UPDATECONNECTIONREQUEST']._serialized_end = 3853
    _globals['_DELETECONNECTIONREQUEST']._serialized_start = 3855
    _globals['_DELETECONNECTIONREQUEST']._serialized_end = 3940
    _globals['_GETCONNECTIONSCHEMAMETADATAREQUEST']._serialized_start = 3942
    _globals['_GETCONNECTIONSCHEMAMETADATAREQUEST']._serialized_end = 4052
    _globals['_REFRESHCONNECTIONSCHEMAMETADATAREQUEST']._serialized_start = 4054
    _globals['_REFRESHCONNECTIONSCHEMAMETADATAREQUEST']._serialized_end = 4168
    _globals['_LISTRUNTIMEENTITYSCHEMASREQUEST']._serialized_start = 4171
    _globals['_LISTRUNTIMEENTITYSCHEMASREQUEST']._serialized_end = 4326
    _globals['_LISTRUNTIMEENTITYSCHEMASRESPONSE']._serialized_start = 4329
    _globals['_LISTRUNTIMEENTITYSCHEMASRESPONSE']._serialized_end = 4469
    _globals['_LISTRUNTIMEACTIONSCHEMASREQUEST']._serialized_start = 4472
    _globals['_LISTRUNTIMEACTIONSCHEMASREQUEST']._serialized_end = 4627
    _globals['_LISTRUNTIMEACTIONSCHEMASRESPONSE']._serialized_start = 4630
    _globals['_LISTRUNTIMEACTIONSCHEMASRESPONSE']._serialized_end = 4770
    _globals['_CONNECTIONSTATUS']._serialized_start = 4773
    _globals['_CONNECTIONSTATUS']._serialized_end = 5035
    _globals['_CONNECTIONSTATUS_STATE']._serialized_start = 4898
    _globals['_CONNECTIONSTATUS_STATE']._serialized_end = 5035