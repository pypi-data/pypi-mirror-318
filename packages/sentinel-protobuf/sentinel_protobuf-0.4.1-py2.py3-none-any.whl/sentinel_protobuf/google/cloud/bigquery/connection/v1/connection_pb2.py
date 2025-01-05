"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/connection/v1/connection.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/bigquery/connection/v1/connection.proto\x12#google.cloud.bigquery.connection.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xba\x01\n\x17CreateConnectionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x1a\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12H\n\nconnection\x18\x03 \x01(\x0b2/.google.cloud.bigquery.connection.v1.ConnectionB\x03\xe0A\x02"Z\n\x14GetConnectionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection"\x7f\n\x16ListConnectionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x12\n\npage_token\x18\x03 \x01(\t"x\n\x17ListConnectionsResponse\x12\x17\n\x0fnext_page_token\x18\x01 \x01(\t\x12D\n\x0bconnections\x18\x02 \x03(\x0b2/.google.cloud.bigquery.connection.v1.Connection"\xdd\x01\n\x17UpdateConnectionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection\x12H\n\nconnection\x18\x02 \x01(\x0b2/.google.cloud.bigquery.connection.v1.ConnectionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"]\n\x17DeleteConnectionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection"\xda\x06\n\nConnection\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rfriendly_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12L\n\tcloud_sql\x18\x04 \x01(\x0b27.google.cloud.bigquery.connection.v1.CloudSqlPropertiesH\x00\x12A\n\x03aws\x18\x08 \x01(\x0b22.google.cloud.bigquery.connection.v1.AwsPropertiesH\x00\x12E\n\x05azure\x18\x0b \x01(\x0b24.google.cloud.bigquery.connection.v1.AzurePropertiesH\x00\x12T\n\rcloud_spanner\x18\x15 \x01(\x0b2;.google.cloud.bigquery.connection.v1.CloudSpannerPropertiesH\x00\x12V\n\x0ecloud_resource\x18\x16 \x01(\x0b2<.google.cloud.bigquery.connection.v1.CloudResourcePropertiesH\x00\x12E\n\x05spark\x18\x17 \x01(\x0b24.google.cloud.bigquery.connection.v1.SparkPropertiesH\x00\x12h\n\x15salesforce_data_cloud\x18\x18 \x01(\x0b2B.google.cloud.bigquery.connection.v1.SalesforceDataCloudPropertiesB\x03\xe0A\x01H\x00\x12\x1a\n\rcreation_time\x18\x05 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18\x06 \x01(\x03B\x03\xe0A\x03\x12\x1b\n\x0ehas_credential\x18\x07 \x01(\x08B\x03\xe0A\x03:s\xeaAp\n,bigqueryconnection.googleapis.com/Connection\x12@projects/{project}/locations/{location}/connections/{connection}B\x0c\n\nproperties"\xca\x02\n\x12CloudSqlProperties\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x10\n\x08database\x18\x02 \x01(\t\x12R\n\x04type\x18\x03 \x01(\x0e2D.google.cloud.bigquery.connection.v1.CloudSqlProperties.DatabaseType\x12P\n\ncredential\x18\x04 \x01(\x0b27.google.cloud.bigquery.connection.v1.CloudSqlCredentialB\x03\xe0A\x04\x12\x1f\n\x12service_account_id\x18\x05 \x01(\tB\x03\xe0A\x03"F\n\x0cDatabaseType\x12\x1d\n\x19DATABASE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSTGRES\x10\x01\x12\t\n\x05MYSQL\x10\x02"8\n\x12CloudSqlCredential\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t"\xb2\x01\n\x16CloudSpannerProperties\x12\x10\n\x08database\x18\x01 \x01(\t\x12\x17\n\x0fuse_parallelism\x18\x02 \x01(\x08\x12\x17\n\x0fmax_parallelism\x18\x05 \x01(\x05\x12 \n\x18use_serverless_analytics\x18\x03 \x01(\x08\x12\x16\n\x0euse_data_boost\x18\x06 \x01(\x08\x12\x1a\n\rdatabase_role\x18\x04 \x01(\tB\x03\xe0A\x01"\xcf\x01\n\rAwsProperties\x12Z\n\x12cross_account_role\x18\x02 \x01(\x0b28.google.cloud.bigquery.connection.v1.AwsCrossAccountRoleB\x02\x18\x01H\x00\x12I\n\x0baccess_role\x18\x03 \x01(\x0b22.google.cloud.bigquery.connection.v1.AwsAccessRoleH\x00B\x17\n\x15authentication_method"^\n\x13AwsCrossAccountRole\x12\x13\n\x0biam_role_id\x18\x01 \x01(\t\x12\x18\n\x0biam_user_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bexternal_id\x18\x03 \x01(\tB\x03\xe0A\x03"6\n\rAwsAccessRole\x12\x13\n\x0biam_role_id\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t"\xcd\x01\n\x0fAzureProperties\x12\x18\n\x0bapplication\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\tclient_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x16\n\tobject_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1a\n\x12customer_tenant_id\x18\x04 \x01(\t\x12\x14\n\x0credirect_uri\x18\x05 \x01(\t\x12\'\n\x1ffederated_application_client_id\x18\x06 \x01(\t\x12\x15\n\x08identity\x18\x07 \x01(\tB\x03\xe0A\x03":\n\x17CloudResourceProperties\x12\x1f\n\x12service_account_id\x18\x01 \x01(\tB\x03\xe0A\x03"]\n\x16MetastoreServiceConfig\x12C\n\x11metastore_service\x18\x01 \x01(\tB(\xe0A\x01\xfaA"\n metastore.googleapis.com/Service"]\n\x18SparkHistoryServerConfig\x12A\n\x10dataproc_cluster\x18\x01 \x01(\tB\'\xe0A\x01\xfaA!\n\x1fdataproc.googleapis.com/Cluster"\xff\x01\n\x0fSparkProperties\x12\x1f\n\x12service_account_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12b\n\x18metastore_service_config\x18\x03 \x01(\x0b2;.google.cloud.bigquery.connection.v1.MetastoreServiceConfigB\x03\xe0A\x01\x12g\n\x1bspark_history_server_config\x18\x04 \x01(\x0b2=.google.cloud.bigquery.connection.v1.SparkHistoryServerConfigB\x03\xe0A\x01"_\n\x1dSalesforceDataCloudProperties\x12\x14\n\x0cinstance_uri\x18\x01 \x01(\t\x12\x15\n\x08identity\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\ttenant_id\x18\x03 \x01(\t2\xcc\r\n\x11ConnectionService\x12\xe8\x01\n\x10CreateConnection\x12<.google.cloud.bigquery.connection.v1.CreateConnectionRequest\x1a/.google.cloud.bigquery.connection.v1.Connection"e\xdaA\x1fparent,connection,connection_id\x82\xd3\xe4\x93\x02="//v1/{parent=projects/*/locations/*}/connections:\nconnection\x12\xbb\x01\n\rGetConnection\x129.google.cloud.bigquery.connection.v1.GetConnectionRequest\x1a/.google.cloud.bigquery.connection.v1.Connection">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/connections/*}\x12\xce\x01\n\x0fListConnections\x12;.google.cloud.bigquery.connection.v1.ListConnectionsRequest\x1a<.google.cloud.bigquery.connection.v1.ListConnectionsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/connections\x12\xe4\x01\n\x10UpdateConnection\x12<.google.cloud.bigquery.connection.v1.UpdateConnectionRequest\x1a/.google.cloud.bigquery.connection.v1.Connection"a\xdaA\x1bname,connection,update_mask\x82\xd3\xe4\x93\x02=2//v1/{name=projects/*/locations/*/connections/*}:\nconnection\x12\xa8\x01\n\x10DeleteConnection\x12<.google.cloud.bigquery.connection.v1.DeleteConnectionRequest\x1a\x16.google.protobuf.Empty">\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/connections/*}\x12\xa9\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"^\xdaA\x10resource,options\x82\xd3\xe4\x93\x02E"@/v1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\x01*\x12\xa8\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"]\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02E"@/v1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\x01*\x12\xd3\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"h\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02K"F/v1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\x01*\x1a~\xcaA!bigqueryconnection.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xfd\x02\n\'com.google.cloud.bigquery.connection.v1P\x01ZGcloud.google.com/go/bigquery/connection/apiv1/connectionpb;connectionpb\xaa\x02#Google.Cloud.BigQuery.Connection.V1\xca\x02#Google\\Cloud\\BigQuery\\Connection\\V1\xeaAY\n\x1fdataproc.googleapis.com/Cluster\x126projects/{project}/regions/{region}/clusters/{cluster}\xeaA^\n metastore.googleapis.com/Service\x12:projects/{project}/locations/{location}/services/{service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.connection.v1.connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.bigquery.connection.v1P\x01ZGcloud.google.com/go/bigquery/connection/apiv1/connectionpb;connectionpb\xaa\x02#Google.Cloud.BigQuery.Connection.V1\xca\x02#Google\\Cloud\\BigQuery\\Connection\\V1\xeaAY\n\x1fdataproc.googleapis.com/Cluster\x126projects/{project}/regions/{region}/clusters/{cluster}\xeaA^\n metastore.googleapis.com/Service\x12:projects/{project}/locations/{location}/services/{service}"
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
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['connection']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['connection']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigqueryconnection.googleapis.com/Connection'
    _globals['_CONNECTION'].fields_by_name['salesforce_data_cloud']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['salesforce_data_cloud']._serialized_options = b'\xe0A\x01'
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
    _globals['_CLOUDSPANNERPROPERTIES'].fields_by_name['database_role']._loaded_options = None
    _globals['_CLOUDSPANNERPROPERTIES'].fields_by_name['database_role']._serialized_options = b'\xe0A\x01'
    _globals['_AWSPROPERTIES'].fields_by_name['cross_account_role']._loaded_options = None
    _globals['_AWSPROPERTIES'].fields_by_name['cross_account_role']._serialized_options = b'\x18\x01'
    _globals['_AWSCROSSACCOUNTROLE'].fields_by_name['iam_user_id']._loaded_options = None
    _globals['_AWSCROSSACCOUNTROLE'].fields_by_name['iam_user_id']._serialized_options = b'\xe0A\x03'
    _globals['_AWSCROSSACCOUNTROLE'].fields_by_name['external_id']._loaded_options = None
    _globals['_AWSCROSSACCOUNTROLE'].fields_by_name['external_id']._serialized_options = b'\xe0A\x03'
    _globals['_AZUREPROPERTIES'].fields_by_name['application']._loaded_options = None
    _globals['_AZUREPROPERTIES'].fields_by_name['application']._serialized_options = b'\xe0A\x03'
    _globals['_AZUREPROPERTIES'].fields_by_name['client_id']._loaded_options = None
    _globals['_AZUREPROPERTIES'].fields_by_name['client_id']._serialized_options = b'\xe0A\x03'
    _globals['_AZUREPROPERTIES'].fields_by_name['object_id']._loaded_options = None
    _globals['_AZUREPROPERTIES'].fields_by_name['object_id']._serialized_options = b'\xe0A\x03'
    _globals['_AZUREPROPERTIES'].fields_by_name['identity']._loaded_options = None
    _globals['_AZUREPROPERTIES'].fields_by_name['identity']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDRESOURCEPROPERTIES'].fields_by_name['service_account_id']._loaded_options = None
    _globals['_CLOUDRESOURCEPROPERTIES'].fields_by_name['service_account_id']._serialized_options = b'\xe0A\x03'
    _globals['_METASTORESERVICECONFIG'].fields_by_name['metastore_service']._loaded_options = None
    _globals['_METASTORESERVICECONFIG'].fields_by_name['metastore_service']._serialized_options = b'\xe0A\x01\xfaA"\n metastore.googleapis.com/Service'
    _globals['_SPARKHISTORYSERVERCONFIG'].fields_by_name['dataproc_cluster']._loaded_options = None
    _globals['_SPARKHISTORYSERVERCONFIG'].fields_by_name['dataproc_cluster']._serialized_options = b'\xe0A\x01\xfaA!\n\x1fdataproc.googleapis.com/Cluster'
    _globals['_SPARKPROPERTIES'].fields_by_name['service_account_id']._loaded_options = None
    _globals['_SPARKPROPERTIES'].fields_by_name['service_account_id']._serialized_options = b'\xe0A\x03'
    _globals['_SPARKPROPERTIES'].fields_by_name['metastore_service_config']._loaded_options = None
    _globals['_SPARKPROPERTIES'].fields_by_name['metastore_service_config']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKPROPERTIES'].fields_by_name['spark_history_server_config']._loaded_options = None
    _globals['_SPARKPROPERTIES'].fields_by_name['spark_history_server_config']._serialized_options = b'\xe0A\x01'
    _globals['_SALESFORCEDATACLOUDPROPERTIES'].fields_by_name['identity']._loaded_options = None
    _globals['_SALESFORCEDATACLOUDPROPERTIES'].fields_by_name['identity']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIONSERVICE']._loaded_options = None
    _globals['_CONNECTIONSERVICE']._serialized_options = b'\xcaA!bigqueryconnection.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONNECTIONSERVICE'].methods_by_name['CreateConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['CreateConnection']._serialized_options = b'\xdaA\x1fparent,connection,connection_id\x82\xd3\xe4\x93\x02="//v1/{parent=projects/*/locations/*}/connections:\nconnection'
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/connections/*}'
    _globals['_CONNECTIONSERVICE'].methods_by_name['ListConnections']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['ListConnections']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/connections'
    _globals['_CONNECTIONSERVICE'].methods_by_name['UpdateConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['UpdateConnection']._serialized_options = b'\xdaA\x1bname,connection,update_mask\x82\xd3\xe4\x93\x02=2//v1/{name=projects/*/locations/*/connections/*}:\nconnection'
    _globals['_CONNECTIONSERVICE'].methods_by_name['DeleteConnection']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['DeleteConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/connections/*}'
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x10resource,options\x82\xd3\xe4\x93\x02E"@/v1/{resource=projects/*/locations/*/connections/*}:getIamPolicy:\x01*'
    _globals['_CONNECTIONSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02E"@/v1/{resource=projects/*/locations/*/connections/*}:setIamPolicy:\x01*'
    _globals['_CONNECTIONSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02K"F/v1/{resource=projects/*/locations/*/connections/*}:testIamPermissions:\x01*'
    _globals['_CREATECONNECTIONREQUEST']._serialized_start = 332
    _globals['_CREATECONNECTIONREQUEST']._serialized_end = 518
    _globals['_GETCONNECTIONREQUEST']._serialized_start = 520
    _globals['_GETCONNECTIONREQUEST']._serialized_end = 610
    _globals['_LISTCONNECTIONSREQUEST']._serialized_start = 612
    _globals['_LISTCONNECTIONSREQUEST']._serialized_end = 739
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_start = 741
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_end = 861
    _globals['_UPDATECONNECTIONREQUEST']._serialized_start = 864
    _globals['_UPDATECONNECTIONREQUEST']._serialized_end = 1085
    _globals['_DELETECONNECTIONREQUEST']._serialized_start = 1087
    _globals['_DELETECONNECTIONREQUEST']._serialized_end = 1180
    _globals['_CONNECTION']._serialized_start = 1183
    _globals['_CONNECTION']._serialized_end = 2041
    _globals['_CLOUDSQLPROPERTIES']._serialized_start = 2044
    _globals['_CLOUDSQLPROPERTIES']._serialized_end = 2374
    _globals['_CLOUDSQLPROPERTIES_DATABASETYPE']._serialized_start = 2304
    _globals['_CLOUDSQLPROPERTIES_DATABASETYPE']._serialized_end = 2374
    _globals['_CLOUDSQLCREDENTIAL']._serialized_start = 2376
    _globals['_CLOUDSQLCREDENTIAL']._serialized_end = 2432
    _globals['_CLOUDSPANNERPROPERTIES']._serialized_start = 2435
    _globals['_CLOUDSPANNERPROPERTIES']._serialized_end = 2613
    _globals['_AWSPROPERTIES']._serialized_start = 2616
    _globals['_AWSPROPERTIES']._serialized_end = 2823
    _globals['_AWSCROSSACCOUNTROLE']._serialized_start = 2825
    _globals['_AWSCROSSACCOUNTROLE']._serialized_end = 2919
    _globals['_AWSACCESSROLE']._serialized_start = 2921
    _globals['_AWSACCESSROLE']._serialized_end = 2975
    _globals['_AZUREPROPERTIES']._serialized_start = 2978
    _globals['_AZUREPROPERTIES']._serialized_end = 3183
    _globals['_CLOUDRESOURCEPROPERTIES']._serialized_start = 3185
    _globals['_CLOUDRESOURCEPROPERTIES']._serialized_end = 3243
    _globals['_METASTORESERVICECONFIG']._serialized_start = 3245
    _globals['_METASTORESERVICECONFIG']._serialized_end = 3338
    _globals['_SPARKHISTORYSERVERCONFIG']._serialized_start = 3340
    _globals['_SPARKHISTORYSERVERCONFIG']._serialized_end = 3433
    _globals['_SPARKPROPERTIES']._serialized_start = 3436
    _globals['_SPARKPROPERTIES']._serialized_end = 3691
    _globals['_SALESFORCEDATACLOUDPROPERTIES']._serialized_start = 3693
    _globals['_SALESFORCEDATACLOUDPROPERTIES']._serialized_end = 3788
    _globals['_CONNECTIONSERVICE']._serialized_start = 3791
    _globals['_CONNECTIONSERVICE']._serialized_end = 5531