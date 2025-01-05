
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"sentinel/subscription/v2/msg.proto\x12\x18sentinel.subscription.v2\x1a\x14gogoproto/gogo.proto"u\n\x12MsgAllocateRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x0f\n\x07address\x18\x03 \x01(\t\x12,\n\x05bytes\x18\x04 \x01(\tB\x1d\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00"4\n\x10MsgCancelRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x15\n\x13MsgAllocateResponse"\x13\n\x11MsgCancelResponse2\xde\x01\n\nMsgService\x12j\n\x0bMsgAllocate\x12,.sentinel.subscription.v2.MsgAllocateRequest\x1a-.sentinel.subscription.v2.MsgAllocateResponse\x12d\n\tMsgCancel\x12*.sentinel.subscription.v2.MsgCancelRequest\x1a+.sentinel.subscription.v2.MsgCancelResponseBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v2\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v2.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v2\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGALLOCATEREQUEST.fields_by_name['id']._options = None
    _MSGALLOCATEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGALLOCATEREQUEST.fields_by_name['bytes']._options = None
    _MSGALLOCATEREQUEST.fields_by_name['bytes']._serialized_options = b'\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00'
    _MSGCANCELREQUEST.fields_by_name['id']._options = None
    _MSGCANCELREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGALLOCATEREQUEST._serialized_start = 86
    _MSGALLOCATEREQUEST._serialized_end = 203
    _MSGCANCELREQUEST._serialized_start = 205
    _MSGCANCELREQUEST._serialized_end = 257
    _MSGALLOCATERESPONSE._serialized_start = 259
    _MSGALLOCATERESPONSE._serialized_end = 280
    _MSGCANCELRESPONSE._serialized_start = 282
    _MSGCANCELRESPONSE._serialized_end = 301
    _MSGSERVICE._serialized_start = 304
    _MSGSERVICE._serialized_end = 526
