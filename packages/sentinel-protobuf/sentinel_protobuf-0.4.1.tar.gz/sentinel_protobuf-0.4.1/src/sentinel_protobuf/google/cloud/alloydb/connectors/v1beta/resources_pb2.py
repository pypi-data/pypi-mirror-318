"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/alloydb/connectors/v1beta/resources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/alloydb/connectors/v1beta/resources.proto\x12&google.cloud.alloydb.connectors.v1beta\x1a\x1fgoogle/api/field_behavior.proto"\xe9\x01\n\x17MetadataExchangeRequest\x12\x17\n\nuser_agent\x18\x01 \x01(\tB\x03\xe0A\x01\x12[\n\tauth_type\x18\x02 \x01(\x0e2H.google.cloud.alloydb.connectors.v1beta.MetadataExchangeRequest.AuthType\x12\x14\n\x0coauth2_token\x18\x03 \x01(\t"B\n\x08AuthType\x12\x19\n\x15AUTH_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tDB_NATIVE\x10\x01\x12\x0c\n\x08AUTO_IAM\x10\x02"\xd6\x01\n\x18MetadataExchangeResponse\x12d\n\rresponse_code\x18\x01 \x01(\x0e2M.google.cloud.alloydb.connectors.v1beta.MetadataExchangeResponse.ResponseCode\x12\x12\n\x05error\x18\x02 \x01(\tB\x03\xe0A\x01"@\n\x0cResponseCode\x12\x1d\n\x19RESPONSE_CODE_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05ERROR\x10\x02B\x89\x02\n*com.google.cloud.alloydb.connectors.v1betaB\x0eResourcesProtoP\x01ZJcloud.google.com/go/alloydb/connectors/apiv1beta/connectorspb;connectorspb\xaa\x02&Google.Cloud.AlloyDb.Connectors.V1Beta\xca\x02&Google\\Cloud\\AlloyDb\\Connectors\\V1beta\xea\x02*Google::Cloud::AlloyDb::Connectors::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.connectors.v1beta.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.alloydb.connectors.v1betaB\x0eResourcesProtoP\x01ZJcloud.google.com/go/alloydb/connectors/apiv1beta/connectorspb;connectorspb\xaa\x02&Google.Cloud.AlloyDb.Connectors.V1Beta\xca\x02&Google\\Cloud\\AlloyDb\\Connectors\\V1beta\xea\x02*Google::Cloud::AlloyDb::Connectors::V1beta'
    _globals['_METADATAEXCHANGEREQUEST'].fields_by_name['user_agent']._loaded_options = None
    _globals['_METADATAEXCHANGEREQUEST'].fields_by_name['user_agent']._serialized_options = b'\xe0A\x01'
    _globals['_METADATAEXCHANGERESPONSE'].fields_by_name['error']._loaded_options = None
    _globals['_METADATAEXCHANGERESPONSE'].fields_by_name['error']._serialized_options = b'\xe0A\x01'
    _globals['_METADATAEXCHANGEREQUEST']._serialized_start = 132
    _globals['_METADATAEXCHANGEREQUEST']._serialized_end = 365
    _globals['_METADATAEXCHANGEREQUEST_AUTHTYPE']._serialized_start = 299
    _globals['_METADATAEXCHANGEREQUEST_AUTHTYPE']._serialized_end = 365
    _globals['_METADATAEXCHANGERESPONSE']._serialized_start = 368
    _globals['_METADATAEXCHANGERESPONSE']._serialized_end = 582
    _globals['_METADATAEXCHANGERESPONSE_RESPONSECODE']._serialized_start = 518
    _globals['_METADATAEXCHANGERESPONSE_RESPONSECODE']._serialized_end = 582