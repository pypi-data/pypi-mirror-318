"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/operations.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/channel/v1/operations.proto\x12\x17google.cloud.channel.v1"\xb6\x03\n\x11OperationMetadata\x12P\n\x0eoperation_type\x18\x01 \x01(\x0e28.google.cloud.channel.v1.OperationMetadata.OperationType"\xce\x02\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12CREATE_ENTITLEMENT\x10\x01\x12\x1b\n\x17CHANGE_RENEWAL_SETTINGS\x10\x03\x12\x16\n\x12START_PAID_SERVICE\x10\x05\x12\x18\n\x14ACTIVATE_ENTITLEMENT\x10\x07\x12\x17\n\x13SUSPEND_ENTITLEMENT\x10\x08\x12\x16\n\x12CANCEL_ENTITLEMENT\x10\t\x12\x19\n\x15TRANSFER_ENTITLEMENTS\x10\n\x12#\n\x1fTRANSFER_ENTITLEMENTS_TO_GOOGLE\x10\x0b\x12\x10\n\x0cCHANGE_OFFER\x10\x0e\x12\x15\n\x11CHANGE_PARAMETERS\x10\x0f\x12\x1c\n\x18PROVISION_CLOUD_IDENTITY\x10\x10Bg\n\x1bcom.google.cloud.channel.v1B\x0fOperationsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x0fOperationsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_OPERATIONMETADATA']._serialized_start = 70
    _globals['_OPERATIONMETADATA']._serialized_end = 508
    _globals['_OPERATIONMETADATA_OPERATIONTYPE']._serialized_start = 174
    _globals['_OPERATIONMETADATA_OPERATIONTYPE']._serialized_end = 508