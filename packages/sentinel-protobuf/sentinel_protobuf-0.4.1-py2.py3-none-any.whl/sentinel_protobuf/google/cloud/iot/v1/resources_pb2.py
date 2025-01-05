"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/iot/v1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/iot/v1/resources.proto\x12\x13google.cloud.iot.v1\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xb0\x07\n\x06Device\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06num_id\x18\x03 \x01(\x04\x12:\n\x0bcredentials\x18\x0c \x03(\x0b2%.google.cloud.iot.v1.DeviceCredential\x127\n\x13last_heartbeat_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0flast_event_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0flast_state_time\x18\x14 \x01(\x0b2\x1a.google.protobuf.Timestamp\x128\n\x14last_config_ack_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.Timestamp\x129\n\x15last_config_send_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0f\n\x07blocked\x18\x13 \x01(\x08\x123\n\x0flast_error_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12-\n\x11last_error_status\x18\x0b \x01(\x0b2\x12.google.rpc.Status\x121\n\x06config\x18\r \x01(\x0b2!.google.cloud.iot.v1.DeviceConfig\x12/\n\x05state\x18\x10 \x01(\x0b2 .google.cloud.iot.v1.DeviceState\x120\n\tlog_level\x18\x15 \x01(\x0e2\x1d.google.cloud.iot.v1.LogLevel\x12;\n\x08metadata\x18\x11 \x03(\x0b2).google.cloud.iot.v1.Device.MetadataEntry\x12:\n\x0egateway_config\x18\x18 \x01(\x0b2".google.cloud.iot.v1.GatewayConfig\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:s\xeaAp\n\x1ecloudiot.googleapis.com/Device\x12Nprojects/{project}/locations/{location}/registries/{registry}/devices/{device}"\xee\x01\n\rGatewayConfig\x126\n\x0cgateway_type\x18\x01 \x01(\x0e2 .google.cloud.iot.v1.GatewayType\x12C\n\x13gateway_auth_method\x18\x02 \x01(\x0e2&.google.cloud.iot.v1.GatewayAuthMethod\x12 \n\x18last_accessed_gateway_id\x18\x03 \x01(\t\x12>\n\x1alast_accessed_gateway_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8f\x04\n\x0eDeviceRegistry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12P\n\x1aevent_notification_configs\x18\n \x03(\x0b2,.google.cloud.iot.v1.EventNotificationConfig\x12O\n\x19state_notification_config\x18\x07 \x01(\x0b2,.google.cloud.iot.v1.StateNotificationConfig\x124\n\x0bmqtt_config\x18\x04 \x01(\x0b2\x1f.google.cloud.iot.v1.MqttConfig\x124\n\x0bhttp_config\x18\t \x01(\x0b2\x1f.google.cloud.iot.v1.HttpConfig\x120\n\tlog_level\x18\x0b \x01(\x0e2\x1d.google.cloud.iot.v1.LogLevel\x12<\n\x0bcredentials\x18\x08 \x03(\x0b2\'.google.cloud.iot.v1.RegistryCredential:d\xeaAa\n cloudiot.googleapis.com/Registry\x12=projects/{project}/locations/{location}/registries/{registry}"H\n\nMqttConfig\x12:\n\x12mqtt_enabled_state\x18\x01 \x01(\x0e2\x1e.google.cloud.iot.v1.MqttState"H\n\nHttpConfig\x12:\n\x12http_enabled_state\x18\x01 \x01(\x0e2\x1e.google.cloud.iot.v1.HttpState"O\n\x17EventNotificationConfig\x12\x19\n\x11subfolder_matches\x18\x02 \x01(\t\x12\x19\n\x11pubsub_topic_name\x18\x01 \x01(\t"4\n\x17StateNotificationConfig\x12\x19\n\x11pubsub_topic_name\x18\x01 \x01(\t"o\n\x12RegistryCredential\x12K\n\x16public_key_certificate\x18\x01 \x01(\x0b2).google.cloud.iot.v1.PublicKeyCertificateH\x00B\x0c\n\ncredential"\xd0\x01\n\x16X509CertificateDetails\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bexpiry_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1b\n\x13signature_algorithm\x18\x05 \x01(\t\x12\x17\n\x0fpublic_key_type\x18\x06 \x01(\t"\xaf\x01\n\x14PublicKeyCertificate\x12?\n\x06format\x18\x01 \x01(\x0e2/.google.cloud.iot.v1.PublicKeyCertificateFormat\x12\x13\n\x0bcertificate\x18\x02 \x01(\t\x12A\n\x0cx509_details\x18\x03 \x01(\x0b2+.google.cloud.iot.v1.X509CertificateDetails"\x95\x01\n\x10DeviceCredential\x12>\n\npublic_key\x18\x02 \x01(\x0b2(.google.cloud.iot.v1.PublicKeyCredentialH\x00\x123\n\x0fexpiration_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x0c\n\ncredential"X\n\x13PublicKeyCredential\x124\n\x06format\x18\x01 \x01(\x0e2$.google.cloud.iot.v1.PublicKeyFormat\x12\x0b\n\x03key\x18\x02 \x01(\t"\xa0\x01\n\x0cDeviceConfig\x12\x0f\n\x07version\x18\x01 \x01(\x03\x125\n\x11cloud_update_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0fdevice_ack_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0bbinary_data\x18\x04 \x01(\x0c"S\n\x0bDeviceState\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0bbinary_data\x18\x02 \x01(\x0c*L\n\tMqttState\x12\x1a\n\x16MQTT_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cMQTT_ENABLED\x10\x01\x12\x11\n\rMQTT_DISABLED\x10\x02*L\n\tHttpState\x12\x1a\n\x16HTTP_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cHTTP_ENABLED\x10\x01\x12\x11\n\rHTTP_DISABLED\x10\x02*O\n\x08LogLevel\x12\x19\n\x15LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\n\x12\t\n\x05ERROR\x10\x14\x12\x08\n\x04INFO\x10\x1e\x12\t\n\x05DEBUG\x10(*I\n\x0bGatewayType\x12\x1c\n\x18GATEWAY_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07GATEWAY\x10\x01\x12\x0f\n\x0bNON_GATEWAY\x10\x02*\x91\x01\n\x11GatewayAuthMethod\x12#\n\x1fGATEWAY_AUTH_METHOD_UNSPECIFIED\x10\x00\x12\x14\n\x10ASSOCIATION_ONLY\x10\x01\x12\x1a\n\x16DEVICE_AUTH_TOKEN_ONLY\x10\x02\x12%\n!ASSOCIATION_AND_DEVICE_AUTH_TOKEN\x10\x03*e\n\x1aPublicKeyCertificateFormat\x12-\n)UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT\x10\x00\x12\x18\n\x14X509_CERTIFICATE_PEM\x10\x01*v\n\x0fPublicKeyFormat\x12!\n\x1dUNSPECIFIED_PUBLIC_KEY_FORMAT\x10\x00\x12\x0b\n\x07RSA_PEM\x10\x03\x12\x10\n\x0cRSA_X509_PEM\x10\x01\x12\r\n\tES256_PEM\x10\x02\x12\x12\n\x0eES256_X509_PEM\x10\x04BY\n\x17com.google.cloud.iot.v1B\x0eResourcesProtoP\x01Z)cloud.google.com/go/iot/apiv1/iotpb;iotpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.iot.v1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.iot.v1B\x0eResourcesProtoP\x01Z)cloud.google.com/go/iot/apiv1/iotpb;iotpb\xf8\x01\x01'
    _globals['_DEVICE_METADATAENTRY']._loaded_options = None
    _globals['_DEVICE_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_DEVICE']._loaded_options = None
    _globals['_DEVICE']._serialized_options = b'\xeaAp\n\x1ecloudiot.googleapis.com/Device\x12Nprojects/{project}/locations/{location}/registries/{registry}/devices/{device}'
    _globals['_DEVICEREGISTRY']._loaded_options = None
    _globals['_DEVICEREGISTRY']._serialized_options = b'\xeaAa\n cloudiot.googleapis.com/Registry\x12=projects/{project}/locations/{location}/registries/{registry}'
    _globals['_MQTTSTATE']._serialized_start = 3138
    _globals['_MQTTSTATE']._serialized_end = 3214
    _globals['_HTTPSTATE']._serialized_start = 3216
    _globals['_HTTPSTATE']._serialized_end = 3292
    _globals['_LOGLEVEL']._serialized_start = 3294
    _globals['_LOGLEVEL']._serialized_end = 3373
    _globals['_GATEWAYTYPE']._serialized_start = 3375
    _globals['_GATEWAYTYPE']._serialized_end = 3448
    _globals['_GATEWAYAUTHMETHOD']._serialized_start = 3451
    _globals['_GATEWAYAUTHMETHOD']._serialized_end = 3596
    _globals['_PUBLICKEYCERTIFICATEFORMAT']._serialized_start = 3598
    _globals['_PUBLICKEYCERTIFICATEFORMAT']._serialized_end = 3699
    _globals['_PUBLICKEYFORMAT']._serialized_start = 3701
    _globals['_PUBLICKEYFORMAT']._serialized_end = 3819
    _globals['_DEVICE']._serialized_start = 146
    _globals['_DEVICE']._serialized_end = 1090
    _globals['_DEVICE_METADATAENTRY']._serialized_start = 926
    _globals['_DEVICE_METADATAENTRY']._serialized_end = 973
    _globals['_GATEWAYCONFIG']._serialized_start = 1093
    _globals['_GATEWAYCONFIG']._serialized_end = 1331
    _globals['_DEVICEREGISTRY']._serialized_start = 1334
    _globals['_DEVICEREGISTRY']._serialized_end = 1861
    _globals['_MQTTCONFIG']._serialized_start = 1863
    _globals['_MQTTCONFIG']._serialized_end = 1935
    _globals['_HTTPCONFIG']._serialized_start = 1937
    _globals['_HTTPCONFIG']._serialized_end = 2009
    _globals['_EVENTNOTIFICATIONCONFIG']._serialized_start = 2011
    _globals['_EVENTNOTIFICATIONCONFIG']._serialized_end = 2090
    _globals['_STATENOTIFICATIONCONFIG']._serialized_start = 2092
    _globals['_STATENOTIFICATIONCONFIG']._serialized_end = 2144
    _globals['_REGISTRYCREDENTIAL']._serialized_start = 2146
    _globals['_REGISTRYCREDENTIAL']._serialized_end = 2257
    _globals['_X509CERTIFICATEDETAILS']._serialized_start = 2260
    _globals['_X509CERTIFICATEDETAILS']._serialized_end = 2468
    _globals['_PUBLICKEYCERTIFICATE']._serialized_start = 2471
    _globals['_PUBLICKEYCERTIFICATE']._serialized_end = 2646
    _globals['_DEVICECREDENTIAL']._serialized_start = 2649
    _globals['_DEVICECREDENTIAL']._serialized_end = 2798
    _globals['_PUBLICKEYCREDENTIAL']._serialized_start = 2800
    _globals['_PUBLICKEYCREDENTIAL']._serialized_end = 2888
    _globals['_DEVICECONFIG']._serialized_start = 2891
    _globals['_DEVICECONFIG']._serialized_end = 3051
    _globals['_DEVICESTATE']._serialized_start = 3053
    _globals['_DEVICESTATE']._serialized_end = 3136