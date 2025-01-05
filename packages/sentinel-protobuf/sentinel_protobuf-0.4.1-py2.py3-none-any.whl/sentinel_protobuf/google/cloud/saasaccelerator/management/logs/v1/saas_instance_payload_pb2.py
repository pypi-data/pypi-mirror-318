"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/saasaccelerator/management/logs/v1/saas_instance_payload.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/cloud/saasaccelerator/management/logs/v1/saas_instance_payload.proto\x12/google.cloud.saasaccelerator.management.logs.v1"\\\n\rInstanceEvent\x12\x0c\n\x04verb\x18\x01 \x01(\t\x12\r\n\x05stage\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x10\n\x08trace_id\x18\x04 \x01(\t\x12\x0f\n\x07node_id\x18\x05 \x01(\tB\x9a\x01\n3com.google.cloud.saasaccelerator.management.logs.v1B\x18SaasInstancePayloadProtoP\x01ZGcloud.google.com/go/saasaccelerator/management/logs/apiv1/logspb;logspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.saasaccelerator.management.logs.v1.saas_instance_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n3com.google.cloud.saasaccelerator.management.logs.v1B\x18SaasInstancePayloadProtoP\x01ZGcloud.google.com/go/saasaccelerator/management/logs/apiv1/logspb;logspb'
    _globals['_INSTANCEEVENT']._serialized_start = 128
    _globals['_INSTANCEEVENT']._serialized_end = 220