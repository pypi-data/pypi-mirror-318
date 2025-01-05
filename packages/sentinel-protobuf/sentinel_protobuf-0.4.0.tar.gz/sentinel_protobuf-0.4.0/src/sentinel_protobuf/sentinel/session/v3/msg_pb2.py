
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.session.v2 import params_pb2 as sentinel_dot_session_dot_v2_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/session/v3/msg.proto\x12\x13sentinel.session.v3\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a sentinel/session/v2/params.proto";\n\x17MsgCancelSessionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\xf1\x01\n\x17MsgUpdateSessionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x125\n\x0edownload_bytes\x18\x03 \x01(\tB\x1d\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00\x123\n\x0cupload_bytes\x18\x04 \x01(\tB\x1d\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00\x125\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\tsignature\x18\x06 \x01(\x0c"Y\n\x16MsgUpdateParamsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x121\n\x06params\x18\x02 \x01(\x0b2\x1b.sentinel.session.v2.ParamsB\x04\xc8\xde\x1f\x00"\x1a\n\x18MsgCancelSessionResponse"\x1a\n\x18MsgUpdateSessionResponse"\x19\n\x17MsgUpdateParamsResponse2\xdc\x02\n\nMsgService\x12o\n\x10MsgCancelSession\x12,.sentinel.session.v3.MsgCancelSessionRequest\x1a-.sentinel.session.v3.MsgCancelSessionResponse\x12o\n\x10MsgUpdateSession\x12,.sentinel.session.v3.MsgUpdateSessionRequest\x1a-.sentinel.session.v3.MsgUpdateSessionResponse\x12l\n\x0fMsgUpdateParams\x12+.sentinel.session.v3.MsgUpdateParamsRequest\x1a,.sentinel.session.v3.MsgUpdateParamsResponseBAZ7github.com/sentinel-official/hub/v12/x/session/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v3.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGCANCELSESSIONREQUEST.fields_by_name['id']._options = None
    _MSGCANCELSESSIONREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGUPDATESESSIONREQUEST.fields_by_name['id']._options = None
    _MSGUPDATESESSIONREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGUPDATESESSIONREQUEST.fields_by_name['download_bytes']._options = None
    _MSGUPDATESESSIONREQUEST.fields_by_name['download_bytes']._serialized_options = b'\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00'
    _MSGUPDATESESSIONREQUEST.fields_by_name['upload_bytes']._options = None
    _MSGUPDATESESSIONREQUEST.fields_by_name['upload_bytes']._serialized_options = b'\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00'
    _MSGUPDATESESSIONREQUEST.fields_by_name['duration']._options = None
    _MSGUPDATESESSIONREQUEST.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _MSGUPDATEPARAMSREQUEST.fields_by_name['params']._options = None
    _MSGUPDATEPARAMSREQUEST.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCANCELSESSIONREQUEST._serialized_start = 142
    _MSGCANCELSESSIONREQUEST._serialized_end = 201
    _MSGUPDATESESSIONREQUEST._serialized_start = 204
    _MSGUPDATESESSIONREQUEST._serialized_end = 445
    _MSGUPDATEPARAMSREQUEST._serialized_start = 447
    _MSGUPDATEPARAMSREQUEST._serialized_end = 536
    _MSGCANCELSESSIONRESPONSE._serialized_start = 538
    _MSGCANCELSESSIONRESPONSE._serialized_end = 564
    _MSGUPDATESESSIONRESPONSE._serialized_start = 566
    _MSGUPDATESESSIONRESPONSE._serialized_end = 592
    _MSGUPDATEPARAMSRESPONSE._serialized_start = 594
    _MSGUPDATEPARAMSRESPONSE._serialized_end = 619
    _MSGSERVICE._serialized_start = 622
    _MSGSERVICE._serialized_end = 970
