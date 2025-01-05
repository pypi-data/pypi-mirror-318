"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.session.v1 import proof_pb2 as sentinel_dot_session_dot_v1_dot_proof__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/session/v1/msg.proto\x12\x13sentinel.session.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fsentinel/session/v1/proof.proto"9\n\rMsgEndRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0e\n\x06rating\x18\x03 \x01(\x04"9\n\x0fMsgStartRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04node\x18\x03 \x01(\t"d\n\x10MsgUpdateRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12/\n\x05proof\x18\x02 \x01(\x0b2\x1a.sentinel.session.v1.ProofB\x04\xc8\xde\x1f\x00\x12\x11\n\tsignature\x18\x03 \x01(\x0c"\x10\n\x0eMsgEndResponse"\x12\n\x10MsgStartResponse"\x13\n\x11MsgUpdateResponse2\x94\x02\n\nMsgService\x12W\n\x08MsgStart\x12$.sentinel.session.v1.MsgStartRequest\x1a%.sentinel.session.v1.MsgStartResponse\x12Z\n\tMsgUpdate\x12%.sentinel.session.v1.MsgUpdateRequest\x1a&.sentinel.session.v1.MsgUpdateResponse\x12Q\n\x06MsgEnd\x12".sentinel.session.v1.MsgEndRequest\x1a#.sentinel.session.v1.MsgEndResponseBAZ7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGUPDATEREQUEST'].fields_by_name['proof']._loaded_options = None
    _globals['_MSGUPDATEREQUEST'].fields_by_name['proof']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGENDREQUEST']._serialized_start = 109
    _globals['_MSGENDREQUEST']._serialized_end = 166
    _globals['_MSGSTARTREQUEST']._serialized_start = 168
    _globals['_MSGSTARTREQUEST']._serialized_end = 225
    _globals['_MSGUPDATEREQUEST']._serialized_start = 227
    _globals['_MSGUPDATEREQUEST']._serialized_end = 327
    _globals['_MSGENDRESPONSE']._serialized_start = 329
    _globals['_MSGENDRESPONSE']._serialized_end = 345
    _globals['_MSGSTARTRESPONSE']._serialized_start = 347
    _globals['_MSGSTARTRESPONSE']._serialized_end = 365
    _globals['_MSGUPDATERESPONSE']._serialized_start = 367
    _globals['_MSGUPDATERESPONSE']._serialized_end = 386
    _globals['_MSGSERVICE']._serialized_start = 389
    _globals['_MSGSERVICE']._serialized_end = 665