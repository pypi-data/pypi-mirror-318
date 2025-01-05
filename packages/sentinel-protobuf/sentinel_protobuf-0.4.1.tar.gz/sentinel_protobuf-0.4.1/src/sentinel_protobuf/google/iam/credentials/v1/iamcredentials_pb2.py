"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/credentials/v1/iamcredentials.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.iam.credentials.v1 import common_pb2 as google_dot_iam_dot_credentials_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/iam/credentials/v1/iamcredentials.proto\x12\x19google.iam.credentials.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a&google/iam/credentials/v1/common.proto2\xad\x07\n\x0eIAMCredentials\x12\xec\x01\n\x13GenerateAccessToken\x125.google.iam.credentials.v1.GenerateAccessTokenRequest\x1a6.google.iam.credentials.v1.GenerateAccessTokenResponse"f\xdaA\x1dname,delegates,scope,lifetime\x82\xd3\xe4\x93\x02@";/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken:\x01*\x12\xe4\x01\n\x0fGenerateIdToken\x121.google.iam.credentials.v1.GenerateIdTokenRequest\x1a2.google.iam.credentials.v1.GenerateIdTokenResponse"j\xdaA%name,delegates,audience,include_email\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/serviceAccounts/*}:generateIdToken:\x01*\x12\xb9\x01\n\x08SignBlob\x12*.google.iam.credentials.v1.SignBlobRequest\x1a+.google.iam.credentials.v1.SignBlobResponse"T\xdaA\x16name,delegates,payload\x82\xd3\xe4\x93\x025"0/v1/{name=projects/*/serviceAccounts/*}:signBlob:\x01*\x12\xb5\x01\n\x07SignJwt\x12).google.iam.credentials.v1.SignJwtRequest\x1a*.google.iam.credentials.v1.SignJwtResponse"S\xdaA\x16name,delegates,payload\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/serviceAccounts/*}:signJwt:\x01*\x1aQ\xcaA\x1diamcredentials.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xca\x01\n#com.google.cloud.iam.credentials.v1B\x13IAMCredentialsProtoP\x01ZEcloud.google.com/go/iam/credentials/apiv1/credentialspb;credentialspb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.Iam.Credentials.V1\xca\x02\x1fGoogle\\Cloud\\Iam\\Credentials\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.credentials.v1.iamcredentials_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.iam.credentials.v1B\x13IAMCredentialsProtoP\x01ZEcloud.google.com/go/iam/credentials/apiv1/credentialspb;credentialspb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.Iam.Credentials.V1\xca\x02\x1fGoogle\\Cloud\\Iam\\Credentials\\V1'
    _globals['_IAMCREDENTIALS']._loaded_options = None
    _globals['_IAMCREDENTIALS']._serialized_options = b'\xcaA\x1diamcredentials.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_IAMCREDENTIALS'].methods_by_name['GenerateAccessToken']._loaded_options = None
    _globals['_IAMCREDENTIALS'].methods_by_name['GenerateAccessToken']._serialized_options = b'\xdaA\x1dname,delegates,scope,lifetime\x82\xd3\xe4\x93\x02@";/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken:\x01*'
    _globals['_IAMCREDENTIALS'].methods_by_name['GenerateIdToken']._loaded_options = None
    _globals['_IAMCREDENTIALS'].methods_by_name['GenerateIdToken']._serialized_options = b'\xdaA%name,delegates,audience,include_email\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/serviceAccounts/*}:generateIdToken:\x01*'
    _globals['_IAMCREDENTIALS'].methods_by_name['SignBlob']._loaded_options = None
    _globals['_IAMCREDENTIALS'].methods_by_name['SignBlob']._serialized_options = b'\xdaA\x16name,delegates,payload\x82\xd3\xe4\x93\x025"0/v1/{name=projects/*/serviceAccounts/*}:signBlob:\x01*'
    _globals['_IAMCREDENTIALS'].methods_by_name['SignJwt']._loaded_options = None
    _globals['_IAMCREDENTIALS'].methods_by_name['SignJwt']._serialized_options = b'\xdaA\x16name,delegates,payload\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/serviceAccounts/*}:signJwt:\x01*'
    _globals['_IAMCREDENTIALS']._serialized_start = 173
    _globals['_IAMCREDENTIALS']._serialized_end = 1114