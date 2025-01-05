"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/provider/v2/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/provider/v2/msg.proto\x12\x14sentinel.provider.v2\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"h\n\x12MsgRegisterRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"\x91\x01\n\x10MsgUpdateRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12)\n\x06status\x18\x06 \x01(\x0e2\x19.sentinel.types.v1.Status"\x15\n\x13MsgRegisterResponse"\x13\n\x11MsgUpdateResponse2\xce\x01\n\nMsgService\x12b\n\x0bMsgRegister\x12(.sentinel.provider.v2.MsgRegisterRequest\x1a).sentinel.provider.v2.MsgRegisterResponse\x12\\\n\tMsgUpdate\x12&.sentinel.provider.v2.MsgUpdateRequest\x1a\'.sentinel.provider.v2.MsgUpdateResponseBBZ8github.com/sentinel-official/hub/v12/x/provider/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v2.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/sentinel-official/hub/v12/x/provider/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGREGISTERREQUEST']._serialized_start = 110
    _globals['_MSGREGISTERREQUEST']._serialized_end = 214
    _globals['_MSGUPDATEREQUEST']._serialized_start = 217
    _globals['_MSGUPDATEREQUEST']._serialized_end = 362
    _globals['_MSGREGISTERRESPONSE']._serialized_start = 364
    _globals['_MSGREGISTERRESPONSE']._serialized_end = 385
    _globals['_MSGUPDATERESPONSE']._serialized_start = 387
    _globals['_MSGUPDATERESPONSE']._serialized_end = 406
    _globals['_MSGSERVICE']._serialized_start = 409
    _globals['_MSGSERVICE']._serialized_end = 615