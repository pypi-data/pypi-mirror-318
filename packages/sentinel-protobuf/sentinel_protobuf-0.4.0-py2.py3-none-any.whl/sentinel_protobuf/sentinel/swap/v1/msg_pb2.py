
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/swap/v1/msg.proto\x12\x10sentinel.swap.v1\x1a\x14gogoproto/gogo.proto"p\n\x0eMsgSwapRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0f\n\x07tx_hash\x18\x02 \x01(\x0c\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12-\n\x06amount\x18\x04 \x01(\tB\x1d\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00"\x11\n\x0fMsgSwapResponse2\\\n\nMsgService\x12N\n\x07MsgSwap\x12 .sentinel.swap.v1.MsgSwapRequest\x1a!.sentinel.swap.v1.MsgSwapResponseB>Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.swap.v1.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGSWAPREQUEST.fields_by_name['amount']._options = None
    _MSGSWAPREQUEST.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00'
    _MSGSWAPREQUEST._serialized_start = 70
    _MSGSWAPREQUEST._serialized_end = 182
    _MSGSWAPRESPONSE._serialized_start = 184
    _MSGSWAPRESPONSE._serialized_end = 201
    _MSGSERVICE._serialized_start = 203
    _MSGSERVICE._serialized_end = 295
