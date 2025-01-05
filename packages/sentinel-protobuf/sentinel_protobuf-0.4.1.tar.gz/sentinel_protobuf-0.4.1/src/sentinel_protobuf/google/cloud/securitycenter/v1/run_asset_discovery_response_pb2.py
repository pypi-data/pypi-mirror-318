"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/run_asset_discovery_response.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/securitycenter/v1/run_asset_discovery_response.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1egoogle/protobuf/duration.proto"\xe7\x01\n\x19RunAssetDiscoveryResponse\x12N\n\x05state\x18\x01 \x01(\x0e2?.google.cloud.securitycenter.v1.RunAssetDiscoveryResponse.State\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"M\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\x0e\n\nSUPERSEDED\x10\x02\x12\x0e\n\nTERMINATED\x10\x03B\xd8\x01\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.run_asset_discovery_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_RUNASSETDISCOVERYRESPONSE']._serialized_start = 134
    _globals['_RUNASSETDISCOVERYRESPONSE']._serialized_end = 365
    _globals['_RUNASSETDISCOVERYRESPONSE_STATE']._serialized_start = 288
    _globals['_RUNASSETDISCOVERYRESPONSE_STATE']._serialized_end = 365