"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/connection.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/securitycenter/v1/connection.proto\x12\x1egoogle.cloud.securitycenter.v1"\x81\x02\n\nConnection\x12\x16\n\x0edestination_ip\x18\x01 \x01(\t\x12\x18\n\x10destination_port\x18\x02 \x01(\x05\x12\x11\n\tsource_ip\x18\x03 \x01(\t\x12\x13\n\x0bsource_port\x18\x04 \x01(\x05\x12E\n\x08protocol\x18\x05 \x01(\x0e23.google.cloud.securitycenter.v1.Connection.Protocol"R\n\x08Protocol\x12\x18\n\x14PROTOCOL_UNSPECIFIED\x10\x00\x12\x08\n\x04ICMP\x10\x01\x12\x07\n\x03TCP\x10\x06\x12\x07\n\x03UDP\x10\x11\x12\x07\n\x03GRE\x10/\x12\x07\n\x03ESP\x102B\xe9\x01\n"com.google.cloud.securitycenter.v1B\x0fConnectionProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x0fConnectionProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_CONNECTION']._serialized_start = 84
    _globals['_CONNECTION']._serialized_end = 341
    _globals['_CONNECTION_PROTOCOL']._serialized_start = 259
    _globals['_CONNECTION_PROTOCOL']._serialized_end = 341