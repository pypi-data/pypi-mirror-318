"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/shell/v1/cloudshell.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/shell/v1/cloudshell.proto\x12\x15google.cloud.shell.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x03\n\x0bEnvironment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0cdocker_image\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12<\n\x05state\x18\x04 \x01(\x0e2(.google.cloud.shell.v1.Environment.StateB\x03\xe0A\x03\x12\x15\n\x08web_host\x18\x0c \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cssh_username\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08ssh_host\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08ssh_port\x18\x07 \x01(\x05B\x03\xe0A\x03\x12\x18\n\x0bpublic_keys\x18\x08 \x03(\tB\x03\xe0A\x03"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUSPENDED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0c\n\x08DELETING\x10\x04:S\xeaAP\n%cloudshell.googleapis.com/Environment\x12\'users/{user}/environments/{environment}"T\n\x15GetEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%cloudshell.googleapis.com/Environment"\x1b\n\x19CreateEnvironmentMetadata"\x1b\n\x19DeleteEnvironmentMetadata"R\n\x17StartEnvironmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0caccess_token\x18\x02 \x01(\t\x12\x13\n\x0bpublic_keys\x18\x03 \x03(\t"\x84\x01\n\x1bAuthorizeEnvironmentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0caccess_token\x18\x02 \x01(\t\x12\x10\n\x08id_token\x18\x04 \x01(\t\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x1e\n\x1cAuthorizeEnvironmentResponse"\x1e\n\x1cAuthorizeEnvironmentMetadata"\xd2\x01\n\x18StartEnvironmentMetadata\x12D\n\x05state\x18\x01 \x01(\x0e25.google.cloud.shell.v1.StartEnvironmentMetadata.State"p\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x14\n\x10UNARCHIVING_DISK\x10\x02\x12\x1e\n\x1aAWAITING_COMPUTE_RESOURCES\x10\x04\x12\x0c\n\x08FINISHED\x10\x03"S\n\x18StartEnvironmentResponse\x127\n\x0benvironment\x18\x01 \x01(\x0b2".google.cloud.shell.v1.Environment"7\n\x13AddPublicKeyRequest\x12\x13\n\x0benvironment\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t"#\n\x14AddPublicKeyResponse\x12\x0b\n\x03key\x18\x01 \x01(\t"\x16\n\x14AddPublicKeyMetadata":\n\x16RemovePublicKeyRequest\x12\x13\n\x0benvironment\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t"\x19\n\x17RemovePublicKeyResponse"\x19\n\x17RemovePublicKeyMetadata"\x9e\x02\n\x16CloudShellErrorDetails\x12O\n\x04code\x18\x01 \x01(\x0e2A.google.cloud.shell.v1.CloudShellErrorDetails.CloudShellErrorCode"\xb2\x01\n\x13CloudShellErrorCode\x12&\n"CLOUD_SHELL_ERROR_CODE_UNSPECIFIED\x10\x00\x12\x15\n\x11IMAGE_UNAVAILABLE\x10\x01\x12\x18\n\x14CLOUD_SHELL_DISABLED\x10\x02\x12\x11\n\rTOS_VIOLATION\x10\x04\x12\x12\n\x0eQUOTA_EXCEEDED\x10\x05\x12\x1b\n\x17ENVIRONMENT_UNAVAILABLE\x10\x062\xd4\x08\n\x11CloudShellService\x12\x94\x01\n\x0eGetEnvironment\x12,.google.cloud.shell.v1.GetEnvironmentRequest\x1a".google.cloud.shell.v1.Environment"0\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=users/*/environments/*}\x12\xcc\x01\n\x10StartEnvironment\x12..google.cloud.shell.v1.StartEnvironmentRequest\x1a\x1d.google.longrunning.Operation"i\xcaA4\n\x18StartEnvironmentResponse\x12\x18StartEnvironmentMetadata\x82\xd3\xe4\x93\x02,"\'/v1/{name=users/*/environments/*}:start:\x01*\x12\xe0\x01\n\x14AuthorizeEnvironment\x122.google.cloud.shell.v1.AuthorizeEnvironmentRequest\x1a\x1d.google.longrunning.Operation"u\xcaA<\n\x1cAuthorizeEnvironmentResponse\x12\x1cAuthorizeEnvironmentMetadata\x82\xd3\xe4\x93\x020"+/v1/{name=users/*/environments/*}:authorize:\x01*\x12\xca\x01\n\x0cAddPublicKey\x12*.google.cloud.shell.v1.AddPublicKeyRequest\x1a\x1d.google.longrunning.Operation"o\xcaA,\n\x14AddPublicKeyResponse\x12\x14AddPublicKeyMetadata\x82\xd3\xe4\x93\x02:"5/v1/{environment=users/*/environments/*}:addPublicKey:\x01*\x12\xd9\x01\n\x0fRemovePublicKey\x12-.google.cloud.shell.v1.RemovePublicKeyRequest\x1a\x1d.google.longrunning.Operation"x\xcaA2\n\x17RemovePublicKeyResponse\x12\x17RemovePublicKeyMetadata\x82\xd3\xe4\x93\x02="8/v1/{environment=users/*/environments/*}:removePublicKey:\x01*\x1aM\xcaA\x19cloudshell.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB_\n\x19com.google.cloud.shell.v1B\x0fCloudShellProtoP\x01Z/cloud.google.com/go/shell/apiv1/shellpb;shellpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.shell.v1.cloudshell_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.shell.v1B\x0fCloudShellProtoP\x01Z/cloud.google.com/go/shell/apiv1/shellpb;shellpb'
    _globals['_ENVIRONMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ENVIRONMENT'].fields_by_name['id']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['docker_image']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['docker_image']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ENVIRONMENT'].fields_by_name['state']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['web_host']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['web_host']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['ssh_username']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['ssh_username']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['ssh_host']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['ssh_host']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['ssh_port']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['ssh_port']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['public_keys']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['public_keys']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT']._loaded_options = None
    _globals['_ENVIRONMENT']._serialized_options = b"\xeaAP\n%cloudshell.googleapis.com/Environment\x12'users/{user}/environments/{environment}"
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%cloudshell.googleapis.com/Environment"
    _globals['_CLOUDSHELLSERVICE']._loaded_options = None
    _globals['_CLOUDSHELLSERVICE']._serialized_options = b'\xcaA\x19cloudshell.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['GetEnvironment']._loaded_options = None
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['GetEnvironment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=users/*/environments/*}'
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['StartEnvironment']._loaded_options = None
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['StartEnvironment']._serialized_options = b'\xcaA4\n\x18StartEnvironmentResponse\x12\x18StartEnvironmentMetadata\x82\xd3\xe4\x93\x02,"\'/v1/{name=users/*/environments/*}:start:\x01*'
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['AuthorizeEnvironment']._loaded_options = None
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['AuthorizeEnvironment']._serialized_options = b'\xcaA<\n\x1cAuthorizeEnvironmentResponse\x12\x1cAuthorizeEnvironmentMetadata\x82\xd3\xe4\x93\x020"+/v1/{name=users/*/environments/*}:authorize:\x01*'
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['AddPublicKey']._loaded_options = None
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['AddPublicKey']._serialized_options = b'\xcaA,\n\x14AddPublicKeyResponse\x12\x14AddPublicKeyMetadata\x82\xd3\xe4\x93\x02:"5/v1/{environment=users/*/environments/*}:addPublicKey:\x01*'
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['RemovePublicKey']._loaded_options = None
    _globals['_CLOUDSHELLSERVICE'].methods_by_name['RemovePublicKey']._serialized_options = b'\xcaA2\n\x17RemovePublicKeyResponse\x12\x17RemovePublicKeyMetadata\x82\xd3\xe4\x93\x02="8/v1/{environment=users/*/environments/*}:removePublicKey:\x01*'
    _globals['_ENVIRONMENT']._serialized_start = 251
    _globals['_ENVIRONMENT']._serialized_end = 686
    _globals['_ENVIRONMENT_STATE']._serialized_start = 516
    _globals['_ENVIRONMENT_STATE']._serialized_end = 601
    _globals['_GETENVIRONMENTREQUEST']._serialized_start = 688
    _globals['_GETENVIRONMENTREQUEST']._serialized_end = 772
    _globals['_CREATEENVIRONMENTMETADATA']._serialized_start = 774
    _globals['_CREATEENVIRONMENTMETADATA']._serialized_end = 801
    _globals['_DELETEENVIRONMENTMETADATA']._serialized_start = 803
    _globals['_DELETEENVIRONMENTMETADATA']._serialized_end = 830
    _globals['_STARTENVIRONMENTREQUEST']._serialized_start = 832
    _globals['_STARTENVIRONMENTREQUEST']._serialized_end = 914
    _globals['_AUTHORIZEENVIRONMENTREQUEST']._serialized_start = 917
    _globals['_AUTHORIZEENVIRONMENTREQUEST']._serialized_end = 1049
    _globals['_AUTHORIZEENVIRONMENTRESPONSE']._serialized_start = 1051
    _globals['_AUTHORIZEENVIRONMENTRESPONSE']._serialized_end = 1081
    _globals['_AUTHORIZEENVIRONMENTMETADATA']._serialized_start = 1083
    _globals['_AUTHORIZEENVIRONMENTMETADATA']._serialized_end = 1113
    _globals['_STARTENVIRONMENTMETADATA']._serialized_start = 1116
    _globals['_STARTENVIRONMENTMETADATA']._serialized_end = 1326
    _globals['_STARTENVIRONMENTMETADATA_STATE']._serialized_start = 1214
    _globals['_STARTENVIRONMENTMETADATA_STATE']._serialized_end = 1326
    _globals['_STARTENVIRONMENTRESPONSE']._serialized_start = 1328
    _globals['_STARTENVIRONMENTRESPONSE']._serialized_end = 1411
    _globals['_ADDPUBLICKEYREQUEST']._serialized_start = 1413
    _globals['_ADDPUBLICKEYREQUEST']._serialized_end = 1468
    _globals['_ADDPUBLICKEYRESPONSE']._serialized_start = 1470
    _globals['_ADDPUBLICKEYRESPONSE']._serialized_end = 1505
    _globals['_ADDPUBLICKEYMETADATA']._serialized_start = 1507
    _globals['_ADDPUBLICKEYMETADATA']._serialized_end = 1529
    _globals['_REMOVEPUBLICKEYREQUEST']._serialized_start = 1531
    _globals['_REMOVEPUBLICKEYREQUEST']._serialized_end = 1589
    _globals['_REMOVEPUBLICKEYRESPONSE']._serialized_start = 1591
    _globals['_REMOVEPUBLICKEYRESPONSE']._serialized_end = 1616
    _globals['_REMOVEPUBLICKEYMETADATA']._serialized_start = 1618
    _globals['_REMOVEPUBLICKEYMETADATA']._serialized_end = 1643
    _globals['_CLOUDSHELLERRORDETAILS']._serialized_start = 1646
    _globals['_CLOUDSHELLERRORDETAILS']._serialized_end = 1932
    _globals['_CLOUDSHELLERRORDETAILS_CLOUDSHELLERRORCODE']._serialized_start = 1754
    _globals['_CLOUDSHELLERRORDETAILS_CLOUDSHELLERRORCODE']._serialized_end = 1932
    _globals['_CLOUDSHELLSERVICE']._serialized_start = 1935
    _globals['_CLOUDSHELLSERVICE']._serialized_end = 3043