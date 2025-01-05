"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"sentinel/subscription/v1/msg.proto\x12\x18sentinel.subscription.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"~\n\x12MsgAddQuotaRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0f\n\x07address\x18\x03 \x01(\t\x12=\n\x05bytes\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int",\n\x10MsgCancelRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04"l\n\x19MsgSubscribeToNodeRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0f\n\x07address\x18\x02 \x01(\t\x120\n\x07deposit\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"D\n\x19MsgSubscribeToPlanRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\r\n\x05denom\x18\x03 \x01(\t"\x81\x01\n\x15MsgUpdateQuotaRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0f\n\x07address\x18\x03 \x01(\t\x12=\n\x05bytes\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int"\x15\n\x13MsgAddQuotaResponse"\x13\n\x11MsgCancelResponse"\x1c\n\x1aMsgSubscribeToNodeResponse"\x1c\n\x1aMsgSubscribeToPlanResponse"\x18\n\x16MsgUpdateQuotaResponse2\xd5\x04\n\nMsgService\x12j\n\x0bMsgAddQuota\x12,.sentinel.subscription.v1.MsgAddQuotaRequest\x1a-.sentinel.subscription.v1.MsgAddQuotaResponse\x12d\n\tMsgCancel\x12*.sentinel.subscription.v1.MsgCancelRequest\x1a+.sentinel.subscription.v1.MsgCancelResponse\x12\x7f\n\x12MsgSubscribeToNode\x123.sentinel.subscription.v1.MsgSubscribeToNodeRequest\x1a4.sentinel.subscription.v1.MsgSubscribeToNodeResponse\x12\x7f\n\x12MsgSubscribeToPlan\x123.sentinel.subscription.v1.MsgSubscribeToPlanRequest\x1a4.sentinel.subscription.v1.MsgSubscribeToPlanResponse\x12s\n\x0eMsgUpdateQuota\x12/.sentinel.subscription.v1.MsgUpdateQuotaRequest\x1a0.sentinel.subscription.v1.MsgUpdateQuotaResponseBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGADDQUOTAREQUEST'].fields_by_name['bytes']._loaded_options = None
    _globals['_MSGADDQUOTAREQUEST'].fields_by_name['bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _globals['_MSGSUBSCRIBETONODEREQUEST'].fields_by_name['deposit']._loaded_options = None
    _globals['_MSGSUBSCRIBETONODEREQUEST'].fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGUPDATEQUOTAREQUEST'].fields_by_name['bytes']._loaded_options = None
    _globals['_MSGUPDATEQUOTAREQUEST'].fields_by_name['bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _globals['_MSGADDQUOTAREQUEST']._serialized_start = 118
    _globals['_MSGADDQUOTAREQUEST']._serialized_end = 244
    _globals['_MSGCANCELREQUEST']._serialized_start = 246
    _globals['_MSGCANCELREQUEST']._serialized_end = 290
    _globals['_MSGSUBSCRIBETONODEREQUEST']._serialized_start = 292
    _globals['_MSGSUBSCRIBETONODEREQUEST']._serialized_end = 400
    _globals['_MSGSUBSCRIBETOPLANREQUEST']._serialized_start = 402
    _globals['_MSGSUBSCRIBETOPLANREQUEST']._serialized_end = 470
    _globals['_MSGUPDATEQUOTAREQUEST']._serialized_start = 473
    _globals['_MSGUPDATEQUOTAREQUEST']._serialized_end = 602
    _globals['_MSGADDQUOTARESPONSE']._serialized_start = 604
    _globals['_MSGADDQUOTARESPONSE']._serialized_end = 625
    _globals['_MSGCANCELRESPONSE']._serialized_start = 627
    _globals['_MSGCANCELRESPONSE']._serialized_end = 646
    _globals['_MSGSUBSCRIBETONODERESPONSE']._serialized_start = 648
    _globals['_MSGSUBSCRIBETONODERESPONSE']._serialized_end = 676
    _globals['_MSGSUBSCRIBETOPLANRESPONSE']._serialized_start = 678
    _globals['_MSGSUBSCRIBETOPLANRESPONSE']._serialized_end = 706
    _globals['_MSGUPDATEQUOTARESPONSE']._serialized_start = 708
    _globals['_MSGUPDATEQUOTARESPONSE']._serialized_end = 732
    _globals['_MSGSERVICE']._serialized_start = 735
    _globals['_MSGSERVICE']._serialized_end = 1332