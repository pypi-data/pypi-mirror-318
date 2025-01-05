"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datastream/v1alpha1/datastream.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datastream.v1alpha1 import datastream_resources_pb2 as google_dot_cloud_dot_datastream_dot_v1alpha1_dot_datastream__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/datastream/v1alpha1/datastream.proto\x12 google.cloud.datastream.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a;google/cloud/datastream/v1alpha1/datastream_resources.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x03\n DiscoverConnectionProfileRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+datastream.googleapis.com/ConnectionProfile\x12R\n\x12connection_profile\x18\xc8\x01 \x01(\x0b23.google.cloud.datastream.v1alpha1.ConnectionProfileH\x00\x12"\n\x17connection_profile_name\x18\xc9\x01 \x01(\tH\x00\x12\x13\n\trecursive\x18\x03 \x01(\x08H\x01\x12\x19\n\x0frecursion_depth\x18\x04 \x01(\x05H\x01\x12E\n\x0coracle_rdbms\x18d \x01(\x0b2-.google.cloud.datastream.v1alpha1.OracleRdbmsH\x02\x12C\n\x0bmysql_rdbms\x18e \x01(\x0b2,.google.cloud.datastream.v1alpha1.MysqlRdbmsH\x02B\x08\n\x06targetB\x07\n\x05depthB\r\n\x0bdata_object"\xbe\x01\n!DiscoverConnectionProfileResponse\x12E\n\x0coracle_rdbms\x18d \x01(\x0b2-.google.cloud.datastream.v1alpha1.OracleRdbmsH\x00\x12C\n\x0bmysql_rdbms\x18e \x01(\x0b2,.google.cloud.datastream.v1alpha1.MysqlRdbmsH\x00B\r\n\x0bdata_object"w\n\x15FetchStaticIpsRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"E\n\x16FetchStaticIpsResponse\x12\x12\n\nstatic_ips\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"K\n\x12FetchErrorsRequest\x125\n\x06stream\x18\x01 \x01(\tB%\xfaA"\n datastream.googleapis.com/Stream"N\n\x13FetchErrorsResponse\x127\n\x06errors\x18\x01 \x03(\x0b2\'.google.cloud.datastream.v1alpha1.Error"\xad\x01\n\x1dListConnectionProfilesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+datastream.googleapis.com/ConnectionProfile\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\xa0\x01\n\x1eListConnectionProfilesResponse\x12P\n\x13connection_profiles\x18\x01 \x03(\x0b23.google.cloud.datastream.v1alpha1.ConnectionProfile\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"`\n\x1bGetConnectionProfileRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datastream.googleapis.com/ConnectionProfile"\xf8\x01\n\x1eCreateConnectionProfileRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+datastream.googleapis.com/ConnectionProfile\x12"\n\x15connection_profile_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12T\n\x12connection_profile\x18\x03 \x01(\x0b23.google.cloud.datastream.v1alpha1.ConnectionProfileB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xc5\x01\n\x1eUpdateConnectionProfileRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12T\n\x12connection_profile\x18\x02 \x01(\x0b23.google.cloud.datastream.v1alpha1.ConnectionProfileB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"|\n\x1eDeleteConnectionProfileRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datastream.googleapis.com/ConnectionProfile\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x97\x01\n\x12ListStreamsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 datastream.googleapis.com/Stream\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"~\n\x13ListStreamsResponse\x129\n\x07streams\x18\x01 \x03(\x0b2(.google.cloud.datastream.v1alpha1.Stream\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"J\n\x10GetStreamRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datastream.googleapis.com/Stream"\xef\x01\n\x13CreateStreamRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 datastream.googleapis.com/Stream\x12\x16\n\tstream_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x06stream\x18\x03 \x01(\x0b2(.google.cloud.datastream.v1alpha1.StreamB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x12\n\x05force\x18\x06 \x01(\x08B\x03\xe0A\x01"\xd3\x01\n\x13UpdateStreamRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12=\n\x06stream\x18\x02 \x01(\x0b2(.google.cloud.datastream.v1alpha1.StreamB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x12\n\x05force\x18\x05 \x01(\x08B\x03\xe0A\x01"f\n\x13DeleteStreamRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datastream.googleapis.com/Stream\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xd4\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03\x12R\n\x11validation_result\x18\x08 \x01(\x0b22.google.cloud.datastream.v1alpha1.ValidationResultB\x03\xe0A\x03"\xf8\x01\n\x1eCreatePrivateConnectionRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+datastream.googleapis.com/PrivateConnection\x12"\n\x15private_connection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12T\n\x12private_connection\x18\x03 \x01(\x0b23.google.cloud.datastream.v1alpha1.PrivateConnectionB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xad\x01\n\x1dListPrivateConnectionsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+datastream.googleapis.com/PrivateConnection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\xa0\x01\n\x1eListPrivateConnectionsResponse\x12P\n\x13private_connections\x18\x01 \x03(\x0b23.google.cloud.datastream.v1alpha1.PrivateConnection\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x90\x01\n\x1eDeletePrivateConnectionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datastream.googleapis.com/PrivateConnection\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05force\x18\x03 \x01(\x08B\x03\xe0A\x01"`\n\x1bGetPrivateConnectionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datastream.googleapis.com/PrivateConnection"\xba\x01\n\x12CreateRouteRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdatastream.googleapis.com/Route\x12\x15\n\x08route_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x05route\x18\x03 \x01(\x0b2\'.google.cloud.datastream.v1alpha1.RouteB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\x95\x01\n\x11ListRoutesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdatastream.googleapis.com/Route\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"{\n\x12ListRoutesResponse\x127\n\x06routes\x18\x01 \x03(\x0b2\'.google.cloud.datastream.v1alpha1.Route\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"d\n\x12DeleteRouteRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdatastream.googleapis.com/Route\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"H\n\x0fGetRouteRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdatastream.googleapis.com/Route2\x8a\'\n\nDatastream\x12\xea\x01\n\x16ListConnectionProfiles\x12?.google.cloud.datastream.v1alpha1.ListConnectionProfilesRequest\x1a@.google.cloud.datastream.v1alpha1.ListConnectionProfilesResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*}/connectionProfiles\x12\xd7\x01\n\x14GetConnectionProfile\x12=.google.cloud.datastream.v1alpha1.GetConnectionProfileRequest\x1a3.google.cloud.datastream.v1alpha1.ConnectionProfile"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/connectionProfiles/*}\x12\xb0\x02\n\x17CreateConnectionProfile\x12@.google.cloud.datastream.v1alpha1.CreateConnectionProfileRequest\x1a\x1d.google.longrunning.Operation"\xb3\x01\xcaA&\n\x11ConnectionProfile\x12\x11OperationMetadata\xdaA/parent,connection_profile,connection_profile_id\x82\xd3\xe4\x93\x02R"</v1alpha1/{parent=projects/*/locations/*}/connectionProfiles:\x12connection_profile\x12\xb2\x02\n\x17UpdateConnectionProfile\x12@.google.cloud.datastream.v1alpha1.UpdateConnectionProfileRequest\x1a\x1d.google.longrunning.Operation"\xb5\x01\xcaA&\n\x11ConnectionProfile\x12\x11OperationMetadata\xdaA\x1econnection_profile,update_mask\x82\xd3\xe4\x93\x02e2O/v1alpha1/{connection_profile.name=projects/*/locations/*/connectionProfiles/*}:\x12connection_profile\x12\xf4\x01\n\x17DeleteConnectionProfile\x12@.google.cloud.datastream.v1alpha1.DeleteConnectionProfileRequest\x1a\x1d.google.longrunning.Operation"x\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/connectionProfiles/*}\x12\xf6\x01\n\x19DiscoverConnectionProfile\x12B.google.cloud.datastream.v1alpha1.DiscoverConnectionProfileRequest\x1aC.google.cloud.datastream.v1alpha1.DiscoverConnectionProfileResponse"P\x82\xd3\xe4\x93\x02J"E/v1alpha1/{parent=projects/*/locations/*}/connectionProfiles:discover:\x01*\x12\xbe\x01\n\x0bListStreams\x124.google.cloud.datastream.v1alpha1.ListStreamsRequest\x1a5.google.cloud.datastream.v1alpha1.ListStreamsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1alpha1/{parent=projects/*/locations/*}/streams\x12\xab\x01\n\tGetStream\x122.google.cloud.datastream.v1alpha1.GetStreamRequest\x1a(.google.cloud.datastream.v1alpha1.Stream"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1alpha1/{name=projects/*/locations/*/streams/*}\x12\xdf\x01\n\x0cCreateStream\x125.google.cloud.datastream.v1alpha1.CreateStreamRequest\x1a\x1d.google.longrunning.Operation"y\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x17parent,stream,stream_id\x82\xd3\xe4\x93\x02;"1/v1alpha1/{parent=projects/*/locations/*}/streams:\x06stream\x12\xe1\x01\n\x0cUpdateStream\x125.google.cloud.datastream.v1alpha1.UpdateStreamRequest\x1a\x1d.google.longrunning.Operation"{\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x12stream,update_mask\x82\xd3\xe4\x93\x02B28/v1alpha1/{stream.name=projects/*/locations/*/streams/*}:\x06stream\x12\xd3\x01\n\x0cDeleteStream\x125.google.cloud.datastream.v1alpha1.DeleteStreamRequest\x1a\x1d.google.longrunning.Operation"m\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1alpha1/{name=projects/*/locations/*/streams/*}\x12\xd9\x01\n\x0bFetchErrors\x124.google.cloud.datastream.v1alpha1.FetchErrorsRequest\x1a\x1d.google.longrunning.Operation"u\xcaA(\n\x13FetchErrorsResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02D"?/v1alpha1/{stream=projects/*/locations/*/streams/*}:fetchErrors:\x01*\x12\xca\x01\n\x0eFetchStaticIps\x127.google.cloud.datastream.v1alpha1.FetchStaticIpsRequest\x1a8.google.cloud.datastream.v1alpha1.FetchStaticIpsResponse"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1alpha1/{name=projects/*/locations/*}:fetchStaticIps\x12\xb0\x02\n\x17CreatePrivateConnection\x12@.google.cloud.datastream.v1alpha1.CreatePrivateConnectionRequest\x1a\x1d.google.longrunning.Operation"\xb3\x01\xcaA&\n\x11PrivateConnection\x12\x11OperationMetadata\xdaA/parent,private_connection,private_connection_id\x82\xd3\xe4\x93\x02R"</v1alpha1/{parent=projects/*/locations/*}/privateConnections:\x12private_connection\x12\xd7\x01\n\x14GetPrivateConnection\x12=.google.cloud.datastream.v1alpha1.GetPrivateConnectionRequest\x1a3.google.cloud.datastream.v1alpha1.PrivateConnection"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/privateConnections/*}\x12\xea\x01\n\x16ListPrivateConnections\x12?.google.cloud.datastream.v1alpha1.ListPrivateConnectionsRequest\x1a@.google.cloud.datastream.v1alpha1.ListPrivateConnectionsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*}/privateConnections\x12\xf4\x01\n\x17DeletePrivateConnection\x12@.google.cloud.datastream.v1alpha1.DeletePrivateConnectionRequest\x1a\x1d.google.longrunning.Operation"x\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/privateConnections/*}\x12\xee\x01\n\x0bCreateRoute\x124.google.cloud.datastream.v1alpha1.CreateRouteRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA\x1a\n\x05Route\x12\x11OperationMetadata\xdaA\x15parent,route,route_id\x82\xd3\xe4\x93\x02N"E/v1alpha1/{parent=projects/*/locations/*/privateConnections/*}/routes:\x05route\x12\xbc\x01\n\x08GetRoute\x121.google.cloud.datastream.v1alpha1.GetRouteRequest\x1a\'.google.cloud.datastream.v1alpha1.Route"T\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1alpha1/{name=projects/*/locations/*/privateConnections/*/routes/*}\x12\xcf\x01\n\nListRoutes\x123.google.cloud.datastream.v1alpha1.ListRoutesRequest\x1a4.google.cloud.datastream.v1alpha1.ListRoutesResponse"V\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1alpha1/{parent=projects/*/locations/*/privateConnections/*}/routes\x12\xe6\x01\n\x0bDeleteRoute\x124.google.cloud.datastream.v1alpha1.DeleteRouteRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G*E/v1alpha1/{name=projects/*/locations/*/privateConnections/*/routes/*}\x1aM\xcaA\x19datastream.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf7\x01\n$com.google.cloud.datastream.v1alpha1B\x1bCloudDatastreamServiceProtoP\x01ZDcloud.google.com/go/datastream/apiv1alpha1/datastreampb;datastreampb\xaa\x02 Google.Cloud.Datastream.V1Alpha1\xca\x02 Google\\Cloud\\Datastream\\V1alpha1\xea\x02#Google::Cloud::Datastream::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datastream.v1alpha1.datastream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datastream.v1alpha1B\x1bCloudDatastreamServiceProtoP\x01ZDcloud.google.com/go/datastream/apiv1alpha1/datastreampb;datastreampb\xaa\x02 Google.Cloud.Datastream.V1Alpha1\xca\x02 Google\\Cloud\\Datastream\\V1alpha1\xea\x02#Google::Cloud::Datastream::V1alpha1'
    _globals['_DISCOVERCONNECTIONPROFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_DISCOVERCONNECTIONPROFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+datastream.googleapis.com/ConnectionProfile'
    _globals['_FETCHSTATICIPSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FETCHSTATICIPSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_FETCHERRORSREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_FETCHERRORSREQUEST'].fields_by_name['stream']._serialized_options = b'\xfaA"\n datastream.googleapis.com/Stream'
    _globals['_LISTCONNECTIONPROFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTIONPROFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+datastream.googleapis.com/ConnectionProfile'
    _globals['_GETCONNECTIONPROFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTIONPROFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datastream.googleapis.com/ConnectionProfile'
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+datastream.googleapis.com/ConnectionProfile'
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['connection_profile_id']._loaded_options = None
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['connection_profile_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['connection_profile']._loaded_options = None
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['connection_profile']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECONNECTIONPROFILEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECONNECTIONPROFILEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTIONPROFILEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECONNECTIONPROFILEREQUEST'].fields_by_name['connection_profile']._loaded_options = None
    _globals['_UPDATECONNECTIONPROFILEREQUEST'].fields_by_name['connection_profile']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIONPROFILEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATECONNECTIONPROFILEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECONNECTIONPROFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTIONPROFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datastream.googleapis.com/ConnectionProfile'
    _globals['_DELETECONNECTIONPROFILEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECONNECTIONPROFILEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSTREAMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSTREAMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 datastream.googleapis.com/Stream'
    _globals['_GETSTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datastream.googleapis.com/Stream'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 datastream.googleapis.com/Stream'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream_id']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['stream']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESTREAMREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_CREATESTREAMREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['stream']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_UPDATESTREAMREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datastream.googleapis.com/Stream'
    _globals['_DELETESTREAMREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETESTREAMREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['validation_result']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['validation_result']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+datastream.googleapis.com/PrivateConnection'
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['private_connection_id']._loaded_options = None
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['private_connection_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['private_connection']._loaded_options = None
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['private_connection']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEPRIVATECONNECTIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATECONNECTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRIVATECONNECTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+datastream.googleapis.com/PrivateConnection'
    _globals['_DELETEPRIVATECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRIVATECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datastream.googleapis.com/PrivateConnection'
    _globals['_DELETEPRIVATECONNECTIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEPRIVATECONNECTIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPRIVATECONNECTIONREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEPRIVATECONNECTIONREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_GETPRIVATECONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRIVATECONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datastream.googleapis.com/PrivateConnection'
    _globals['_CREATEROUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEROUTEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdatastream.googleapis.com/Route'
    _globals['_CREATEROUTEREQUEST'].fields_by_name['route_id']._loaded_options = None
    _globals['_CREATEROUTEREQUEST'].fields_by_name['route_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROUTEREQUEST'].fields_by_name['route']._loaded_options = None
    _globals['_CREATEROUTEREQUEST'].fields_by_name['route']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROUTEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEROUTEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROUTESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTROUTESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdatastream.googleapis.com/Route'
    _globals['_DELETEROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdatastream.googleapis.com/Route'
    _globals['_DELETEROUTEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEROUTEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdatastream.googleapis.com/Route'
    _globals['_DATASTREAM']._loaded_options = None
    _globals['_DATASTREAM']._serialized_options = b'\xcaA\x19datastream.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATASTREAM'].methods_by_name['ListConnectionProfiles']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['ListConnectionProfiles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*}/connectionProfiles'
    _globals['_DATASTREAM'].methods_by_name['GetConnectionProfile']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['GetConnectionProfile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/connectionProfiles/*}'
    _globals['_DATASTREAM'].methods_by_name['CreateConnectionProfile']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['CreateConnectionProfile']._serialized_options = b'\xcaA&\n\x11ConnectionProfile\x12\x11OperationMetadata\xdaA/parent,connection_profile,connection_profile_id\x82\xd3\xe4\x93\x02R"</v1alpha1/{parent=projects/*/locations/*}/connectionProfiles:\x12connection_profile'
    _globals['_DATASTREAM'].methods_by_name['UpdateConnectionProfile']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['UpdateConnectionProfile']._serialized_options = b'\xcaA&\n\x11ConnectionProfile\x12\x11OperationMetadata\xdaA\x1econnection_profile,update_mask\x82\xd3\xe4\x93\x02e2O/v1alpha1/{connection_profile.name=projects/*/locations/*/connectionProfiles/*}:\x12connection_profile'
    _globals['_DATASTREAM'].methods_by_name['DeleteConnectionProfile']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['DeleteConnectionProfile']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/connectionProfiles/*}'
    _globals['_DATASTREAM'].methods_by_name['DiscoverConnectionProfile']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['DiscoverConnectionProfile']._serialized_options = b'\x82\xd3\xe4\x93\x02J"E/v1alpha1/{parent=projects/*/locations/*}/connectionProfiles:discover:\x01*'
    _globals['_DATASTREAM'].methods_by_name['ListStreams']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['ListStreams']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1alpha1/{parent=projects/*/locations/*}/streams'
    _globals['_DATASTREAM'].methods_by_name['GetStream']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['GetStream']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1alpha1/{name=projects/*/locations/*/streams/*}'
    _globals['_DATASTREAM'].methods_by_name['CreateStream']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['CreateStream']._serialized_options = b'\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x17parent,stream,stream_id\x82\xd3\xe4\x93\x02;"1/v1alpha1/{parent=projects/*/locations/*}/streams:\x06stream'
    _globals['_DATASTREAM'].methods_by_name['UpdateStream']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['UpdateStream']._serialized_options = b'\xcaA\x1b\n\x06Stream\x12\x11OperationMetadata\xdaA\x12stream,update_mask\x82\xd3\xe4\x93\x02B28/v1alpha1/{stream.name=projects/*/locations/*/streams/*}:\x06stream'
    _globals['_DATASTREAM'].methods_by_name['DeleteStream']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['DeleteStream']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1alpha1/{name=projects/*/locations/*/streams/*}'
    _globals['_DATASTREAM'].methods_by_name['FetchErrors']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['FetchErrors']._serialized_options = b'\xcaA(\n\x13FetchErrorsResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02D"?/v1alpha1/{stream=projects/*/locations/*/streams/*}:fetchErrors:\x01*'
    _globals['_DATASTREAM'].methods_by_name['FetchStaticIps']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['FetchStaticIps']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1alpha1/{name=projects/*/locations/*}:fetchStaticIps'
    _globals['_DATASTREAM'].methods_by_name['CreatePrivateConnection']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['CreatePrivateConnection']._serialized_options = b'\xcaA&\n\x11PrivateConnection\x12\x11OperationMetadata\xdaA/parent,private_connection,private_connection_id\x82\xd3\xe4\x93\x02R"</v1alpha1/{parent=projects/*/locations/*}/privateConnections:\x12private_connection'
    _globals['_DATASTREAM'].methods_by_name['GetPrivateConnection']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['GetPrivateConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{name=projects/*/locations/*/privateConnections/*}'
    _globals['_DATASTREAM'].methods_by_name['ListPrivateConnections']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['ListPrivateConnections']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1alpha1/{parent=projects/*/locations/*}/privateConnections'
    _globals['_DATASTREAM'].methods_by_name['DeletePrivateConnection']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['DeletePrivateConnection']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1alpha1/{name=projects/*/locations/*/privateConnections/*}'
    _globals['_DATASTREAM'].methods_by_name['CreateRoute']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['CreateRoute']._serialized_options = b'\xcaA\x1a\n\x05Route\x12\x11OperationMetadata\xdaA\x15parent,route,route_id\x82\xd3\xe4\x93\x02N"E/v1alpha1/{parent=projects/*/locations/*/privateConnections/*}/routes:\x05route'
    _globals['_DATASTREAM'].methods_by_name['GetRoute']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['GetRoute']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1alpha1/{name=projects/*/locations/*/privateConnections/*/routes/*}'
    _globals['_DATASTREAM'].methods_by_name['ListRoutes']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['ListRoutes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1alpha1/{parent=projects/*/locations/*/privateConnections/*}/routes'
    _globals['_DATASTREAM'].methods_by_name['DeleteRoute']._loaded_options = None
    _globals['_DATASTREAM'].methods_by_name['DeleteRoute']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G*E/v1alpha1/{name=projects/*/locations/*/privateConnections/*/routes/*}'
    _globals['_DISCOVERCONNECTIONPROFILEREQUEST']._serialized_start = 368
    _globals['_DISCOVERCONNECTIONPROFILEREQUEST']._serialized_end = 813
    _globals['_DISCOVERCONNECTIONPROFILERESPONSE']._serialized_start = 816
    _globals['_DISCOVERCONNECTIONPROFILERESPONSE']._serialized_end = 1006
    _globals['_FETCHSTATICIPSREQUEST']._serialized_start = 1008
    _globals['_FETCHSTATICIPSREQUEST']._serialized_end = 1127
    _globals['_FETCHSTATICIPSRESPONSE']._serialized_start = 1129
    _globals['_FETCHSTATICIPSRESPONSE']._serialized_end = 1198
    _globals['_FETCHERRORSREQUEST']._serialized_start = 1200
    _globals['_FETCHERRORSREQUEST']._serialized_end = 1275
    _globals['_FETCHERRORSRESPONSE']._serialized_start = 1277
    _globals['_FETCHERRORSRESPONSE']._serialized_end = 1355
    _globals['_LISTCONNECTIONPROFILESREQUEST']._serialized_start = 1358
    _globals['_LISTCONNECTIONPROFILESREQUEST']._serialized_end = 1531
    _globals['_LISTCONNECTIONPROFILESRESPONSE']._serialized_start = 1534
    _globals['_LISTCONNECTIONPROFILESRESPONSE']._serialized_end = 1694
    _globals['_GETCONNECTIONPROFILEREQUEST']._serialized_start = 1696
    _globals['_GETCONNECTIONPROFILEREQUEST']._serialized_end = 1792
    _globals['_CREATECONNECTIONPROFILEREQUEST']._serialized_start = 1795
    _globals['_CREATECONNECTIONPROFILEREQUEST']._serialized_end = 2043
    _globals['_UPDATECONNECTIONPROFILEREQUEST']._serialized_start = 2046
    _globals['_UPDATECONNECTIONPROFILEREQUEST']._serialized_end = 2243
    _globals['_DELETECONNECTIONPROFILEREQUEST']._serialized_start = 2245
    _globals['_DELETECONNECTIONPROFILEREQUEST']._serialized_end = 2369
    _globals['_LISTSTREAMSREQUEST']._serialized_start = 2372
    _globals['_LISTSTREAMSREQUEST']._serialized_end = 2523
    _globals['_LISTSTREAMSRESPONSE']._serialized_start = 2525
    _globals['_LISTSTREAMSRESPONSE']._serialized_end = 2651
    _globals['_GETSTREAMREQUEST']._serialized_start = 2653
    _globals['_GETSTREAMREQUEST']._serialized_end = 2727
    _globals['_CREATESTREAMREQUEST']._serialized_start = 2730
    _globals['_CREATESTREAMREQUEST']._serialized_end = 2969
    _globals['_UPDATESTREAMREQUEST']._serialized_start = 2972
    _globals['_UPDATESTREAMREQUEST']._serialized_end = 3183
    _globals['_DELETESTREAMREQUEST']._serialized_start = 3185
    _globals['_DELETESTREAMREQUEST']._serialized_end = 3287
    _globals['_OPERATIONMETADATA']._serialized_start = 3290
    _globals['_OPERATIONMETADATA']._serialized_end = 3630
    _globals['_CREATEPRIVATECONNECTIONREQUEST']._serialized_start = 3633
    _globals['_CREATEPRIVATECONNECTIONREQUEST']._serialized_end = 3881
    _globals['_LISTPRIVATECONNECTIONSREQUEST']._serialized_start = 3884
    _globals['_LISTPRIVATECONNECTIONSREQUEST']._serialized_end = 4057
    _globals['_LISTPRIVATECONNECTIONSRESPONSE']._serialized_start = 4060
    _globals['_LISTPRIVATECONNECTIONSRESPONSE']._serialized_end = 4220
    _globals['_DELETEPRIVATECONNECTIONREQUEST']._serialized_start = 4223
    _globals['_DELETEPRIVATECONNECTIONREQUEST']._serialized_end = 4367
    _globals['_GETPRIVATECONNECTIONREQUEST']._serialized_start = 4369
    _globals['_GETPRIVATECONNECTIONREQUEST']._serialized_end = 4465
    _globals['_CREATEROUTEREQUEST']._serialized_start = 4468
    _globals['_CREATEROUTEREQUEST']._serialized_end = 4654
    _globals['_LISTROUTESREQUEST']._serialized_start = 4657
    _globals['_LISTROUTESREQUEST']._serialized_end = 4806
    _globals['_LISTROUTESRESPONSE']._serialized_start = 4808
    _globals['_LISTROUTESRESPONSE']._serialized_end = 4931
    _globals['_DELETEROUTEREQUEST']._serialized_start = 4933
    _globals['_DELETEROUTEREQUEST']._serialized_end = 5033
    _globals['_GETROUTEREQUEST']._serialized_start = 5035
    _globals['_GETROUTEREQUEST']._serialized_end = 5107
    _globals['_DATASTREAM']._serialized_start = 5110
    _globals['_DATASTREAM']._serialized_end = 10112