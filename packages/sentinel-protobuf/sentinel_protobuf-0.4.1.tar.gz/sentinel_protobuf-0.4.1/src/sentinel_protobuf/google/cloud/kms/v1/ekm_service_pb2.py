"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kms/v1/ekm_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/kms/v1/ekm_service.proto\x12\x13google.cloud.kms.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x01\n\x19ListEkmConnectionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x86\x01\n\x1aListEkmConnectionsResponse\x12;\n\x0fekm_connections\x18\x01 \x03(\x0b2".google.cloud.kms.v1.EkmConnection\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"V\n\x17GetEkmConnectionRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%cloudkms.googleapis.com/EkmConnection"\xb8\x01\n\x1aCreateEkmConnectionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x1e\n\x11ekm_connection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\x0eekm_connection\x18\x03 \x01(\x0b2".google.cloud.kms.v1.EkmConnectionB\x03\xe0A\x02"\x93\x01\n\x1aUpdateEkmConnectionRequest\x12?\n\x0eekm_connection\x18\x01 \x01(\x0b2".google.cloud.kms.v1.EkmConnectionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"N\n\x13GetEkmConfigRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudkms.googleapis.com/EkmConfig"\x87\x01\n\x16UpdateEkmConfigRequest\x127\n\nekm_config\x18\x01 \x01(\x0b2\x1e.google.cloud.kms.v1.EkmConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xbf\x02\n\x0bCertificate\x12\x14\n\x07raw_der\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x13\n\x06parsed\x18\x02 \x01(\x08B\x03\xe0A\x03\x12\x13\n\x06issuer\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07subject\x18\x04 \x01(\tB\x03\xe0A\x03\x12*\n\x1dsubject_alternative_dns_names\x18\x05 \x03(\tB\x03\xe0A\x03\x128\n\x0fnot_before_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x127\n\x0enot_after_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rserial_number\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12sha256_fingerprint\x18\t \x01(\tB\x03\xe0A\x03"\xe2\x05\n\rEkmConnection\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12R\n\x11service_resolvers\x18\x03 \x03(\x0b22.google.cloud.kms.v1.EkmConnection.ServiceResolverB\x03\xe0A\x01\x12\x11\n\x04etag\x18\x05 \x01(\tB\x03\xe0A\x01\x12V\n\x13key_management_mode\x18\x06 \x01(\x0e24.google.cloud.kms.v1.EkmConnection.KeyManagementModeB\x03\xe0A\x01\x12\x1e\n\x11crypto_space_path\x18\x07 \x01(\tB\x03\xe0A\x01\x1a\xde\x01\n\x0fServiceResolver\x12R\n\x19service_directory_service\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x1c\n\x0fendpoint_filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08hostname\x18\x03 \x01(\tB\x03\xe0A\x02\x12B\n\x13server_certificates\x18\x04 \x03(\x0b2 .google.cloud.kms.v1.CertificateB\x03\xe0A\x02"S\n\x11KeyManagementMode\x12#\n\x1fKEY_MANAGEMENT_MODE_UNSPECIFIED\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\r\n\tCLOUD_KMS\x10\x02:s\xeaAp\n%cloudkms.googleapis.com/EkmConnection\x12Gprojects/{project}/locations/{location}/ekmConnections/{ekm_connection}"\xc8\x01\n\tEkmConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12M\n\x16default_ekm_connection\x18\x02 \x01(\tB-\xe0A\x01\xfaA\'\n%cloudkms.googleapis.com/EkmConnection:Y\xeaAV\n!cloudkms.googleapis.com/EkmConfig\x121projects/{project}/locations/{location}/ekmConfig"X\n\x19VerifyConnectivityRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%cloudkms.googleapis.com/EkmConnection"\x1c\n\x1aVerifyConnectivityResponse2\xdc\x0b\n\nEkmService\x12\xba\x01\n\x12ListEkmConnections\x12..google.cloud.kms.v1.ListEkmConnectionsRequest\x1a/.google.cloud.kms.v1.ListEkmConnectionsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/ekmConnections\x12\xa7\x01\n\x10GetEkmConnection\x12,.google.cloud.kms.v1.GetEkmConnectionRequest\x1a".google.cloud.kms.v1.EkmConnection"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/ekmConnections/*}\x12\xe0\x01\n\x13CreateEkmConnection\x12/.google.cloud.kms.v1.CreateEkmConnectionRequest\x1a".google.cloud.kms.v1.EkmConnection"t\xdaA\'parent,ekm_connection_id,ekm_connection\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/ekmConnections:\x0eekm_connection\x12\xe2\x01\n\x13UpdateEkmConnection\x12/.google.cloud.kms.v1.UpdateEkmConnectionRequest\x1a".google.cloud.kms.v1.EkmConnection"v\xdaA\x1aekm_connection,update_mask\x82\xd3\xe4\x93\x02S2A/v1/{ekm_connection.name=projects/*/locations/*/ekmConnections/*}:\x0eekm_connection\x12\x94\x01\n\x0cGetEkmConfig\x12(.google.cloud.kms.v1.GetEkmConfigRequest\x1a\x1e.google.cloud.kms.v1.EkmConfig":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/ekmConfig}\x12\xc3\x01\n\x0fUpdateEkmConfig\x12+.google.cloud.kms.v1.UpdateEkmConfigRequest\x1a\x1e.google.cloud.kms.v1.EkmConfig"c\xdaA\x16ekm_config,update_mask\x82\xd3\xe4\x93\x02D26/v1/{ekm_config.name=projects/*/locations/*/ekmConfig}:\nekm_config\x12\xcb\x01\n\x12VerifyConnectivity\x12..google.cloud.kms.v1.VerifyConnectivityRequest\x1a/.google.cloud.kms.v1.VerifyConnectivityResponse"T\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1/{name=projects/*/locations/*/ekmConnections/*}:verifyConnectivity\x1at\xcaA\x17cloudkms.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudkmsB\x82\x02\n\x17com.google.cloud.kms.v1B\x0fEkmServiceProtoP\x01Z)cloud.google.com/go/kms/apiv1/kmspb;kmspb\xaa\x02\x13Google.Cloud.Kms.V1\xca\x02\x13Google\\Cloud\\Kms\\V1\xeaA|\n\'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kms.v1.ekm_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n\x17com.google.cloud.kms.v1B\x0fEkmServiceProtoP\x01Z)cloud.google.com/go/kms/apiv1/kmspb;kmspb\xaa\x02\x13Google.Cloud.Kms.V1\xca\x02\x13Google\\Cloud\\Kms\\V1\xeaA|\n'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}"
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTEKMCONNECTIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETEKMCONNECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEKMCONNECTIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%cloudkms.googleapis.com/EkmConnection"
    _globals['_CREATEEKMCONNECTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEKMCONNECTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEEKMCONNECTIONREQUEST'].fields_by_name['ekm_connection_id']._loaded_options = None
    _globals['_CREATEEKMCONNECTIONREQUEST'].fields_by_name['ekm_connection_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEEKMCONNECTIONREQUEST'].fields_by_name['ekm_connection']._loaded_options = None
    _globals['_CREATEEKMCONNECTIONREQUEST'].fields_by_name['ekm_connection']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEKMCONNECTIONREQUEST'].fields_by_name['ekm_connection']._loaded_options = None
    _globals['_UPDATEEKMCONNECTIONREQUEST'].fields_by_name['ekm_connection']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEKMCONNECTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEKMCONNECTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETEKMCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEKMCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudkms.googleapis.com/EkmConfig'
    _globals['_UPDATEEKMCONFIGREQUEST'].fields_by_name['ekm_config']._loaded_options = None
    _globals['_UPDATEEKMCONFIGREQUEST'].fields_by_name['ekm_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEKMCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEKMCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATE'].fields_by_name['raw_der']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['raw_der']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATE'].fields_by_name['parsed']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['parsed']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['issuer']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['issuer']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['subject']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['subject']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['subject_alternative_dns_names']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['subject_alternative_dns_names']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['not_before_time']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['not_before_time']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['not_after_time']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['not_after_time']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['serial_number']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['serial_number']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATE'].fields_by_name['sha256_fingerprint']._loaded_options = None
    _globals['_CERTIFICATE'].fields_by_name['sha256_fingerprint']._serialized_options = b'\xe0A\x03'
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['service_directory_service']._loaded_options = None
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['service_directory_service']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['endpoint_filter']._loaded_options = None
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['endpoint_filter']._serialized_options = b'\xe0A\x01'
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['hostname']._loaded_options = None
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['hostname']._serialized_options = b'\xe0A\x02'
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['server_certificates']._loaded_options = None
    _globals['_EKMCONNECTION_SERVICERESOLVER'].fields_by_name['server_certificates']._serialized_options = b'\xe0A\x02'
    _globals['_EKMCONNECTION'].fields_by_name['name']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EKMCONNECTION'].fields_by_name['create_time']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EKMCONNECTION'].fields_by_name['service_resolvers']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['service_resolvers']._serialized_options = b'\xe0A\x01'
    _globals['_EKMCONNECTION'].fields_by_name['etag']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_EKMCONNECTION'].fields_by_name['key_management_mode']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['key_management_mode']._serialized_options = b'\xe0A\x01'
    _globals['_EKMCONNECTION'].fields_by_name['crypto_space_path']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['crypto_space_path']._serialized_options = b'\xe0A\x01'
    _globals['_EKMCONNECTION']._loaded_options = None
    _globals['_EKMCONNECTION']._serialized_options = b'\xeaAp\n%cloudkms.googleapis.com/EkmConnection\x12Gprojects/{project}/locations/{location}/ekmConnections/{ekm_connection}'
    _globals['_EKMCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_EKMCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EKMCONFIG'].fields_by_name['default_ekm_connection']._loaded_options = None
    _globals['_EKMCONFIG'].fields_by_name['default_ekm_connection']._serialized_options = b"\xe0A\x01\xfaA'\n%cloudkms.googleapis.com/EkmConnection"
    _globals['_EKMCONFIG']._loaded_options = None
    _globals['_EKMCONFIG']._serialized_options = b'\xeaAV\n!cloudkms.googleapis.com/EkmConfig\x121projects/{project}/locations/{location}/ekmConfig'
    _globals['_VERIFYCONNECTIVITYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VERIFYCONNECTIVITYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%cloudkms.googleapis.com/EkmConnection"
    _globals['_EKMSERVICE']._loaded_options = None
    _globals['_EKMSERVICE']._serialized_options = b'\xcaA\x17cloudkms.googleapis.com\xd2AWhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloudkms'
    _globals['_EKMSERVICE'].methods_by_name['ListEkmConnections']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['ListEkmConnections']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/ekmConnections'
    _globals['_EKMSERVICE'].methods_by_name['GetEkmConnection']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['GetEkmConnection']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/ekmConnections/*}'
    _globals['_EKMSERVICE'].methods_by_name['CreateEkmConnection']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['CreateEkmConnection']._serialized_options = b'\xdaA\'parent,ekm_connection_id,ekm_connection\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/ekmConnections:\x0eekm_connection'
    _globals['_EKMSERVICE'].methods_by_name['UpdateEkmConnection']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['UpdateEkmConnection']._serialized_options = b'\xdaA\x1aekm_connection,update_mask\x82\xd3\xe4\x93\x02S2A/v1/{ekm_connection.name=projects/*/locations/*/ekmConnections/*}:\x0eekm_connection'
    _globals['_EKMSERVICE'].methods_by_name['GetEkmConfig']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['GetEkmConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/ekmConfig}'
    _globals['_EKMSERVICE'].methods_by_name['UpdateEkmConfig']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['UpdateEkmConfig']._serialized_options = b'\xdaA\x16ekm_config,update_mask\x82\xd3\xe4\x93\x02D26/v1/{ekm_config.name=projects/*/locations/*/ekmConfig}:\nekm_config'
    _globals['_EKMSERVICE'].methods_by_name['VerifyConnectivity']._loaded_options = None
    _globals['_EKMSERVICE'].methods_by_name['VerifyConnectivity']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1/{name=projects/*/locations/*/ekmConnections/*}:verifyConnectivity'
    _globals['_LISTEKMCONNECTIONSREQUEST']._serialized_start = 245
    _globals['_LISTEKMCONNECTIONSREQUEST']._serialized_end = 424
    _globals['_LISTEKMCONNECTIONSRESPONSE']._serialized_start = 427
    _globals['_LISTEKMCONNECTIONSRESPONSE']._serialized_end = 561
    _globals['_GETEKMCONNECTIONREQUEST']._serialized_start = 563
    _globals['_GETEKMCONNECTIONREQUEST']._serialized_end = 649
    _globals['_CREATEEKMCONNECTIONREQUEST']._serialized_start = 652
    _globals['_CREATEEKMCONNECTIONREQUEST']._serialized_end = 836
    _globals['_UPDATEEKMCONNECTIONREQUEST']._serialized_start = 839
    _globals['_UPDATEEKMCONNECTIONREQUEST']._serialized_end = 986
    _globals['_GETEKMCONFIGREQUEST']._serialized_start = 988
    _globals['_GETEKMCONFIGREQUEST']._serialized_end = 1066
    _globals['_UPDATEEKMCONFIGREQUEST']._serialized_start = 1069
    _globals['_UPDATEEKMCONFIGREQUEST']._serialized_end = 1204
    _globals['_CERTIFICATE']._serialized_start = 1207
    _globals['_CERTIFICATE']._serialized_end = 1526
    _globals['_EKMCONNECTION']._serialized_start = 1529
    _globals['_EKMCONNECTION']._serialized_end = 2267
    _globals['_EKMCONNECTION_SERVICERESOLVER']._serialized_start = 1843
    _globals['_EKMCONNECTION_SERVICERESOLVER']._serialized_end = 2065
    _globals['_EKMCONNECTION_KEYMANAGEMENTMODE']._serialized_start = 2067
    _globals['_EKMCONNECTION_KEYMANAGEMENTMODE']._serialized_end = 2150
    _globals['_EKMCONFIG']._serialized_start = 2270
    _globals['_EKMCONFIG']._serialized_end = 2470
    _globals['_VERIFYCONNECTIVITYREQUEST']._serialized_start = 2472
    _globals['_VERIFYCONNECTIVITYREQUEST']._serialized_end = 2560
    _globals['_VERIFYCONNECTIVITYRESPONSE']._serialized_start = 2562
    _globals['_VERIFYCONNECTIVITYRESPONSE']._serialized_end = 2590
    _globals['_EKMSERVICE']._serialized_start = 2593
    _globals['_EKMSERVICE']._serialized_end = 4093