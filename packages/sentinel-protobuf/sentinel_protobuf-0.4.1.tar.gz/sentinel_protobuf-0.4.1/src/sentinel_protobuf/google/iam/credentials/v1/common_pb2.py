"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/credentials/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/iam/credentials/v1/common.proto\x12\x19google.iam.credentials.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa9\x01\n\x1aGenerateAccessTokenRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount\x12\x11\n\tdelegates\x18\x02 \x03(\t\x12\x12\n\x05scope\x18\x04 \x03(\tB\x03\xe0A\x02\x12+\n\x08lifetime\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration"d\n\x1bGenerateAccessTokenResponse\x12\x14\n\x0caccess_token\x18\x01 \x01(\t\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"s\n\x0fSignBlobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount\x12\x11\n\tdelegates\x18\x03 \x03(\t\x12\x14\n\x07payload\x18\x05 \x01(\x0cB\x03\xe0A\x02"7\n\x10SignBlobResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x13\n\x0bsigned_blob\x18\x04 \x01(\x0c"r\n\x0eSignJwtRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount\x12\x11\n\tdelegates\x18\x03 \x03(\t\x12\x14\n\x07payload\x18\x05 \x01(\tB\x03\xe0A\x02"5\n\x0fSignJwtResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nsigned_jwt\x18\x02 \x01(\t"\x92\x01\n\x16GenerateIdTokenRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount\x12\x11\n\tdelegates\x18\x02 \x03(\t\x12\x15\n\x08audience\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rinclude_email\x18\x04 \x01(\x08"(\n\x17GenerateIdTokenResponse\x12\r\n\x05token\x18\x01 \x01(\tB\xac\x02\n#com.google.cloud.iam.credentials.v1B\x19IAMCredentialsCommonProtoP\x01ZEcloud.google.com/go/iam/credentials/apiv1/credentialspb;credentialspb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.Iam.Credentials.V1\xca\x02\x1fGoogle\\Cloud\\Iam\\Credentials\\V1\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.credentials.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.iam.credentials.v1B\x19IAMCredentialsCommonProtoP\x01ZEcloud.google.com/go/iam/credentials/apiv1/credentialspb;credentialspb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.Iam.Credentials.V1\xca\x02\x1fGoogle\\Cloud\\Iam\\Credentials\\V1\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}'
    _globals['_GENERATEACCESSTOKENREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEACCESSTOKENREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_GENERATEACCESSTOKENREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_GENERATEACCESSTOKENREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_SIGNBLOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SIGNBLOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_SIGNBLOBREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_SIGNBLOBREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_SIGNJWTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SIGNJWTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_SIGNJWTREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_SIGNJWTREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEIDTOKENREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEIDTOKENREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_GENERATEIDTOKENREQUEST'].fields_by_name['audience']._loaded_options = None
    _globals['_GENERATEIDTOKENREQUEST'].fields_by_name['audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEACCESSTOKENREQUEST']._serialized_start = 195
    _globals['_GENERATEACCESSTOKENREQUEST']._serialized_end = 364
    _globals['_GENERATEACCESSTOKENRESPONSE']._serialized_start = 366
    _globals['_GENERATEACCESSTOKENRESPONSE']._serialized_end = 466
    _globals['_SIGNBLOBREQUEST']._serialized_start = 468
    _globals['_SIGNBLOBREQUEST']._serialized_end = 583
    _globals['_SIGNBLOBRESPONSE']._serialized_start = 585
    _globals['_SIGNBLOBRESPONSE']._serialized_end = 640
    _globals['_SIGNJWTREQUEST']._serialized_start = 642
    _globals['_SIGNJWTREQUEST']._serialized_end = 756
    _globals['_SIGNJWTRESPONSE']._serialized_start = 758
    _globals['_SIGNJWTRESPONSE']._serialized_end = 811
    _globals['_GENERATEIDTOKENREQUEST']._serialized_start = 814
    _globals['_GENERATEIDTOKENREQUEST']._serialized_end = 960
    _globals['_GENERATEIDTOKENRESPONSE']._serialized_start = 962
    _globals['_GENERATEIDTOKENRESPONSE']._serialized_end = 1002