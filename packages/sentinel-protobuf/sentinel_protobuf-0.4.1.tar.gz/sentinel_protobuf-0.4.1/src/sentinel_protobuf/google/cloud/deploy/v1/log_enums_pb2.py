"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/deploy/v1/log_enums.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/deploy/v1/log_enums.proto\x12\x16google.cloud.deploy.v1*\x96\x02\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12$\n TYPE_PUBSUB_NOTIFICATION_FAILURE\x10\x01\x12\x1e\n\x1aTYPE_RESOURCE_STATE_CHANGE\x10\x03\x12\x18\n\x14TYPE_PROCESS_ABORTED\x10\x04\x12\x1d\n\x19TYPE_RESTRICTION_VIOLATED\x10\x05\x12\x19\n\x15TYPE_RESOURCE_DELETED\x10\x06\x12\x17\n\x13TYPE_ROLLOUT_UPDATE\x10\x07\x12!\n\x1dTYPE_DEPLOY_POLICY_EVALUATION\x10\x08\x12"\n\x1aTYPE_RENDER_STATUES_CHANGE\x10\x02\x1a\x02\x08\x01Ba\n\x1acom.google.cloud.deploy.v1B\rLogEnumsProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.deploy.v1.log_enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.deploy.v1B\rLogEnumsProtoP\x01Z2cloud.google.com/go/deploy/apiv1/deploypb;deploypb'
    _globals['_TYPE'].values_by_name['TYPE_RENDER_STATUES_CHANGE']._loaded_options = None
    _globals['_TYPE'].values_by_name['TYPE_RENDER_STATUES_CHANGE']._serialized_options = b'\x08\x01'
    _globals['_TYPE']._serialized_start = 67
    _globals['_TYPE']._serialized_end = 345