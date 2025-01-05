
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/provider/v1/msg.proto\x12\x14sentinel.provider.v1\x1a\x14gogoproto/gogo.proto"h\n\x12MsgRegisterRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"f\n\x10MsgUpdateRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"\x15\n\x13MsgRegisterResponse"\x13\n\x11MsgUpdateResponse2\xce\x01\n\nMsgService\x12b\n\x0bMsgRegister\x12(.sentinel.provider.v1.MsgRegisterRequest\x1a).sentinel.provider.v1.MsgRegisterResponse\x12\\\n\tMsgUpdate\x12&.sentinel.provider.v1.MsgUpdateRequest\x1a\'.sentinel.provider.v1.MsgUpdateResponseBBZ8github.com/sentinel-official/hub/v12/x/provider/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v1.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/sentinel-official/hub/v12/x/provider/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGREGISTERREQUEST._serialized_start = 78
    _MSGREGISTERREQUEST._serialized_end = 182
    _MSGUPDATEREQUEST._serialized_start = 184
    _MSGUPDATEREQUEST._serialized_end = 286
    _MSGREGISTERRESPONSE._serialized_start = 288
    _MSGREGISTERRESPONSE._serialized_end = 309
    _MSGUPDATERESPONSE._serialized_start = 311
    _MSGUPDATERESPONSE._serialized_end = 330
    _MSGSERVICE._serialized_start = 333
    _MSGSERVICE._serialized_end = 539
