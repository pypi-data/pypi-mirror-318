"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/connection/v1beta1/connection.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/bigquery/connection/v1beta1/connection.proto\x12(google.cloud.bigquery.connection.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbf\x01\n\x17CreateConnectionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x1a\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12M\n\nconnection\x18\x03 \x01(\x0b24.google.cloud.bigquery.connection.v1beta1.ConnectionB\x03\xe0A\x02"Z\n\x14GetConnectionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection"\x9f\x01\n\x16ListConnectionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x126\n\x0bmax_results\x18\x02 \x01(\x0b2\x1c.google.protobuf.UInt32ValueB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x03 \x01(\t"}\n\x17ListConnectionsResponse\x12\x17\n\x0fnext_page_token\x18\x01 \x01(\t\x12I\n\x0bconnections\x18\x02 \x03(\x0b24.google.cloud.bigquery.connection.v1beta1.Connection"\xe2\x01\n\x17UpdateConnectionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection\x12M\n\nconnection\x18\x02 \x01(\x0b24.google.cloud.bigquery.connection.v1beta1.ConnectionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x8f\x01\n!UpdateConnectionCredentialRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12W\n\ncredential\x18\x02 \x01(\x0b2>.google.cloud.bigquery.connection.v1beta1.ConnectionCredentialB\x03\xe0A\x02"]\n\x17DeleteConnectionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection"\xf6\x02\n\nConnection\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rfriendly_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12Q\n\tcloud_sql\x18\x04 \x01(\x0b2<.google.cloud.bigquery.connection.v1beta1.CloudSqlPropertiesH\x00\x12\x1a\n\rcreation_time\x18\x05 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18\x06 \x01(\x03B\x03\xe0A\x03\x12\x1b\n\x0ehas_credential\x18\x07 \x01(\x08B\x03\xe0A\x03:s\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}B\x0c\n\nproperties"w\n\x14ConnectionCredential\x12Q\n\tcloud_sql\x18\x01 \x01(\x0b2<.google.cloud.bigquery.connection.v1beta1.CloudSqlCredentialH\x00B\x0c\n\ncredential"\xd4\x02\n\x12CloudSqlProperties\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x10\n\x08database\x18\x02 \x01(\t\x12W\n\x04type\x18\x03 \x01(\x0e2I.google.cloud.bigquery.connection.v1beta1.CloudSqlProperties.DatabaseType\x12U\n\ncredential\x18\x04 \x01(\x0b2<.google.cloud.bigquery.connection.v1beta1.CloudSqlCredentialB\x03\xe0A\x04\x12\x1f\n\x12service_account_id\x18\x05 \x01(\tB\x03\xe0A\x03"F\n\x0cDatabaseType\x12\x1d\n\x19DATABASE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\t\n\x05MYSQL\x10\x02"8\n\x12CloudSqlCredential\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t2\x98\x10\n\x11ConnectionService\x12\xf7\x01\n\x10CreateConnection\x12A.google.cloud.bigquery.connection.v1beta1.CreateConnectionRequest\x1a4.google.cloud.bigquery.connection.v1beta1.Connection"j\xdaA\x1fparent,connection,connection_id\x82\xd3\xe4\x93\x02B"4/v1beta1/{parent=projects/*/locations/*}/connections:\nconnection\x12\xca\x01\n\rGetConnection\x12>.google.cloud.bigquery.connection.v1beta1.GetConnectionRequest\x1a4.google.cloud.bigquery.connection.v1beta1.Connection"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1beta1/{name=projects/*/locations/*/connections/*}\x12\xe9\x01\n\x0fListConnections\x12@.google.cloud.bigquery.connection.v1beta1.ListConnectionsRequest\x1aA.google.cloud.bigquery.connection.v1beta1.ListConnectionsResponse"Q\xdaA\x12parent,max_results\x82\xd3\xe4\x93\x026\x124/v1beta1/{parent=projects/*/locations/*}/connections\x12\xf3\x01\n\x10UpdateConnection\x12A.google.cloud.bigquery.connection.v1beta1.UpdateConnectionRequest\x1a4.google.cloud.bigquery.connection.v1beta1.Connection"f\xdaA\x1bname,connection,update_mask\x82\xd3\xe4\x93\x02B24/v1beta1/{name=projects/*/locations/*/connections/*}:\nconnection\x12\xe8\x01\n\x1aUpdateConnectionCredential\x12K.google.cloud.bigquery.connection.v1beta1.UpdateConnectionCredentialRequest\x1a\x16.google.protobuf.Empty"e\xdaA\x0fname,credential\x82\xd3\xe4\x93\x02M2?/v1beta1/{name=projects/*/locations/*/connections/*/credential}:\ncredential\x12\xb2\x01\n\x10DeleteConnection\x12A.google.cloud.bigquery.connection.v1beta1.DeleteConnectionRequest\x1a\x16.google.protobuf.Empty"C\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1beta1/{name=projects/*/locations/*/connections/*}\x12\xae\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"c\xdaA\x10resource,options\x82\xd3\xe4\x93\x02J"E/v1beta1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\x01*\x12\xad\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"b\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02J"E/v1beta1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\x01*\x12\xd8\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"m\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02P"K/v1beta1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\x01*\x1a~\xcaA!bigqueryconnection.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xe3\x01\n,com.google.cloud.bigquery.connection.v1beta1B\x0fConnectionProtoZLcloud.google.com/go/bigquery/connection/apiv1beta1/connectionpb;connectionpb\xaa\x02(Google.Cloud.BigQuery.Connection.V1Beta1\xca\x02(Google\\Cloud\\BigQuery\\Connection\\V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.connection.v1beta1.connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.bigquery.connection.v1beta1B\x0fConnectionProtoZLcloud.google.com/go/bigquery/connection/apiv1beta1/connectionpb;connectionpb\xaa\x02(Google.Cloud.BigQuery.Connection.V1Beta1\xca\x02(Google\\Cloud\\BigQuery\\Connection\\V1beta1'
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection_id']._loaded_options = None
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection']._loaded_options = None
    _globals['_CREATECONNECTIONREQUEST'].fields_by_name['connection']._serialized_options = b'\xe0A\x02'
    _globals['_GETCONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['max_results']._loaded_options = None
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['max_results']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['connection']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['connection']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONCREDENTIALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATECONNECTIONCREDENTIALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONCREDENTIALREQUEST'].fields_by_name['credential']._loaded_options = None
    _globals['_UPDATECONNECTIONCREDENTIALREQUEST'].fields_by_name['credential']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_CONNECTION'].fields_by_name['creation_time']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['has_credential']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['has_credential']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION']._loaded_options = None
    _globals['_CONNECTION']._serialized_options = b'\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}'
    _globals['_CLOUDSQLPROPERTIES'].fields_by_name['credential']._loaded_options = None
    _globals['_CLOUDSQLPROPERTIES'].fields_by_name['credential']._serialized_options = b'\xe0A\x04'
    _globals['_CLOUDSQLPROPERTIES'].fields_by_name['service_account_id']._loaded_options = None
    _globals['_CLOUDSQLPROPERTIES'].fields_by_name['service_account_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSERVICE']._loaded_options = None
    _globals['_CONNECTIONSERVICE']._serialized_options = b'\xcaA!bigqueryconnection.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONNECTIONSERVICE'].methods_by_name['CreateConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['CreateConnection']._serialized_options = b'\xdaA\x1fparent,connection,connection_id\x82\xd3\xe4\x93\x02B"4/v1beta1/{parent=projects/*/locations/*}/connections:\nconnection'
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1beta1/{name=projects/*/locations/*/connections/*}'
    _globals['_CONNECTIONSERVICE'].methods_by_name['ListConnections']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['ListConnections']._serialized_options = b'\xdaA\x12parent,max_results\x82\xd3\xe4\x93\x026\x124/v1beta1/{parent=projects/*/locations/*}/connections'
    _globals['_CONNECTIONSERVICE'].methods_by_name['UpdateConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['UpdateConnection']._serialized_options = b'\xdaA\x1bname,connection,update_mask\x82\xd3\xe4\x93\x02B24/v1beta1/{name=projects/*/locations/*/connections/*}:\nconnection'
    _globals['_CONNECTIONSERVICE'].methods_by_name['UpdateConnectionCredential']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['UpdateConnectionCredential']._serialized_options = b'\xdaA\x0fname,credential\x82\xd3\xe4\x93\x02M2?/v1beta1/{name=projects/*/locations/*/connections/*/credential}:\ncredential'
    _globals['_CONNECTIONSERVICE'].methods_by_name['DeleteConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['DeleteConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1beta1/{name=projects/*/locations/*/connections/*}'
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x10resource,options\x82\xd3\xe4\x93\x02J"E/v1beta1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\x01*'
    _globals['_CONNECTIONSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02J"E/v1beta1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\x01*'
    _globals['_CONNECTIONSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02P"K/v1beta1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\x01*'
    _globals['_CREATECONNECTIONREQUEST']._serialized_start = 374
    _globals['_CREATECONNECTIONREQUEST']._serialized_end = 565
    _globals['_GETCONNECTIONREQUEST']._serialized_start = 567
    _globals['_GETCONNECTIONREQUEST']._serialized_end = 657
    _globals['_LISTCONNECTIONSREQUEST']._serialized_start = 660
    _globals['_LISTCONNECTIONSREQUEST']._serialized_end = 819
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_start = 821
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_end = 946
    _globals['_UPDATECONNECTIONREQUEST']._serialized_start = 949
    _globals['_UPDATECONNECTIONREQUEST']._serialized_end = 1175
    _globals['_UPDATECONNECTIONCREDENTIALREQUEST']._serialized_start = 1178
    _globals['_UPDATECONNECTIONCREDENTIALREQUEST']._serialized_end = 1321
    _globals['_DELETECONNECTIONREQUEST']._serialized_start = 1323
    _globals['_DELETECONNECTIONREQUEST']._serialized_end = 1416
    _globals['_CONNECTION']._serialized_start = 1419
    _globals['_CONNECTION']._serialized_end = 1793
    _globals['_CONNECTIONCREDENTIAL']._serialized_start = 1795
    _globals['_CONNECTIONCREDENTIAL']._serialized_end = 1914
    _globals['_CLOUDSQLPROPERTIES']._serialized_start = 1917
    _globals['_CLOUDSQLPROPERTIES']._serialized_end = 2257
    _globals['_CLOUDSQLPROPERTIES_DATABASETYPE']._serialized_start = 2187
    _globals['_CLOUDSQLPROPERTIES_DATABASETYPE']._serialized_end = 2257
    _globals['_CLOUDSQLCREDENTIAL']._serialized_start = 2259
    _globals['_CLOUDSQLCREDENTIAL']._serialized_end = 2315
    _globals['_CONNECTIONSERVICE']._serialized_start = 2318
    _globals['_CONNECTIONSERVICE']._serialized_end = 4390