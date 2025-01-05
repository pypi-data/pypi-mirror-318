"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v3/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.session.v2 import params_pb2 as sentinel_dot_session_dot_v2_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/session/v3/msg.proto\x12\x13sentinel.session.v3\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a sentinel/session/v2/params.proto";\n\x17MsgCancelSessionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\xf1\x01\n\x17MsgUpdateSessionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x125\n\x0edownload_bytes\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x123\n\x0cupload_bytes\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x125\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\tsignature\x18\x06 \x01(\x0c"Y\n\x16MsgUpdateParamsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x121\n\x06params\x18\x02 \x01(\x0b2\x1b.sentinel.session.v2.ParamsB\x04\xc8\xde\x1f\x00"\x1a\n\x18MsgCancelSessionResponse"\x1a\n\x18MsgUpdateSessionResponse"\x19\n\x17MsgUpdateParamsResponse2\xdc\x02\n\nMsgService\x12o\n\x10MsgCancelSession\x12,.sentinel.session.v3.MsgCancelSessionRequest\x1a-.sentinel.session.v3.MsgCancelSessionResponse\x12o\n\x10MsgUpdateSession\x12,.sentinel.session.v3.MsgUpdateSessionRequest\x1a-.sentinel.session.v3.MsgUpdateSessionResponse\x12l\n\x0fMsgUpdateParams\x12+.sentinel.session.v3.MsgUpdateParamsRequest\x1a,.sentinel.session.v3.MsgUpdateParamsResponseBAZ7github.com/sentinel-official/hub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v3.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGCANCELSESSIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGCANCELSESSIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['download_bytes']._loaded_options = None
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['download_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['upload_bytes']._loaded_options = None
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['upload_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['duration']._loaded_options = None
    _globals['_MSGUPDATESESSIONREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGCANCELSESSIONREQUEST']._serialized_start = 142
    _globals['_MSGCANCELSESSIONREQUEST']._serialized_end = 201
    _globals['_MSGUPDATESESSIONREQUEST']._serialized_start = 204
    _globals['_MSGUPDATESESSIONREQUEST']._serialized_end = 445
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 447
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 536
    _globals['_MSGCANCELSESSIONRESPONSE']._serialized_start = 538
    _globals['_MSGCANCELSESSIONRESPONSE']._serialized_end = 564
    _globals['_MSGUPDATESESSIONRESPONSE']._serialized_start = 566
    _globals['_MSGUPDATESESSIONRESPONSE']._serialized_end = 592
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 594
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 619
    _globals['_MSGSERVICE']._serialized_start = 622
    _globals['_MSGSERVICE']._serialized_end = 970