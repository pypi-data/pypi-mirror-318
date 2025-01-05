
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.oracle.v1 import params_pb2 as sentinel_dot_oracle_dot_v1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csentinel/oracle/v1/msg.proto\x12\x12sentinel.oracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fsentinel/oracle/v1/params.proto"{\n\x15MsgCreateAssetRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x10\n\x08decimals\x18\x03 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x04 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x05 \x01(\t"4\n\x15MsgDeleteAssetRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"{\n\x15MsgUpdateAssetRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x10\n\x08decimals\x18\x03 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x04 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x05 \x01(\t"X\n\x16MsgUpdateParamsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x120\n\x06params\x18\x02 \x01(\x0b2\x1a.sentinel.oracle.v1.ParamsB\x04\xc8\xde\x1f\x00"\x18\n\x16MsgCreateAssetResponse"\x18\n\x16MsgDeleteAssetResponse"\x18\n\x16MsgUpdateAssetResponse"\x19\n\x17MsgUpdateParamsResponse2\xb3\x03\n\nMsgService\x12g\n\x0eMsgCreateAsset\x12).sentinel.oracle.v1.MsgCreateAssetRequest\x1a*.sentinel.oracle.v1.MsgCreateAssetResponse\x12g\n\x0eMsgDeleteAsset\x12).sentinel.oracle.v1.MsgDeleteAssetRequest\x1a*.sentinel.oracle.v1.MsgDeleteAssetResponse\x12g\n\x0eMsgUpdateAsset\x12).sentinel.oracle.v1.MsgUpdateAssetRequest\x1a*.sentinel.oracle.v1.MsgUpdateAssetResponse\x12j\n\x0fMsgUpdateParams\x12*.sentinel.oracle.v1.MsgUpdateParamsRequest\x1a+.sentinel.oracle.v1.MsgUpdateParamsResponseB@Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGUPDATEPARAMSREQUEST.fields_by_name['params']._options = None
    _MSGUPDATEPARAMSREQUEST.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEASSETREQUEST._serialized_start = 107
    _MSGCREATEASSETREQUEST._serialized_end = 230
    _MSGDELETEASSETREQUEST._serialized_start = 232
    _MSGDELETEASSETREQUEST._serialized_end = 284
    _MSGUPDATEASSETREQUEST._serialized_start = 286
    _MSGUPDATEASSETREQUEST._serialized_end = 409
    _MSGUPDATEPARAMSREQUEST._serialized_start = 411
    _MSGUPDATEPARAMSREQUEST._serialized_end = 499
    _MSGCREATEASSETRESPONSE._serialized_start = 501
    _MSGCREATEASSETRESPONSE._serialized_end = 525
    _MSGDELETEASSETRESPONSE._serialized_start = 527
    _MSGDELETEASSETRESPONSE._serialized_end = 551
    _MSGUPDATEASSETRESPONSE._serialized_start = 553
    _MSGUPDATEASSETRESPONSE._serialized_end = 577
    _MSGUPDATEPARAMSRESPONSE._serialized_start = 579
    _MSGUPDATEPARAMSRESPONSE._serialized_end = 604
    _MSGSERVICE._serialized_start = 607
    _MSGSERVICE._serialized_end = 1042
