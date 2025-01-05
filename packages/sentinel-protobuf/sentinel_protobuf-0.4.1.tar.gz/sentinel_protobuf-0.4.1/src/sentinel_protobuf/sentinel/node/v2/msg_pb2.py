"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v2/msg.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/node/v2/msg.proto\x12\x10sentinel.node.v2\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"\x8f\x02\n\x12MsgRegisterRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12d\n\x0fgigabyte_prices\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12b\n\rhourly_prices\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"\x94\x02\n\x17MsgUpdateDetailsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12d\n\x0fgigabyte_prices\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12b\n\rhourly_prices\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"Q\n\x16MsgUpdateStatusRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status"j\n\x13MsgSubscribeRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x11\n\tgigabytes\x18\x03 \x01(\x03\x12\r\n\x05hours\x18\x04 \x01(\x03\x12\r\n\x05denom\x18\x05 \x01(\t"\x15\n\x13MsgRegisterResponse"\x1a\n\x18MsgUpdateDetailsResponse"\x19\n\x17MsgUpdateStatusResponse"\x16\n\x14MsgSubscribeResponse2\x9a\x03\n\nMsgService\x12Z\n\x0bMsgRegister\x12$.sentinel.node.v2.MsgRegisterRequest\x1a%.sentinel.node.v2.MsgRegisterResponse\x12i\n\x10MsgUpdateDetails\x12).sentinel.node.v2.MsgUpdateDetailsRequest\x1a*.sentinel.node.v2.MsgUpdateDetailsResponse\x12f\n\x0fMsgUpdateStatus\x12(.sentinel.node.v2.MsgUpdateStatusRequest\x1a).sentinel.node.v2.MsgUpdateStatusResponse\x12]\n\x0cMsgSubscribe\x12%.sentinel.node.v2.MsgSubscribeRequest\x1a&.sentinel.node.v2.MsgSubscribeResponseB>Z4github.com/sentinel-official/hub/v12/x/node/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v2.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGREGISTERREQUEST'].fields_by_name['gigabyte_prices']._loaded_options = None
    _globals['_MSGREGISTERREQUEST'].fields_by_name['gigabyte_prices']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGREGISTERREQUEST'].fields_by_name['hourly_prices']._loaded_options = None
    _globals['_MSGREGISTERREQUEST'].fields_by_name['hourly_prices']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGREGISTERREQUEST'].fields_by_name['remote_url']._loaded_options = None
    _globals['_MSGREGISTERREQUEST'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_MSGUPDATEDETAILSREQUEST'].fields_by_name['gigabyte_prices']._loaded_options = None
    _globals['_MSGUPDATEDETAILSREQUEST'].fields_by_name['gigabyte_prices']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGUPDATEDETAILSREQUEST'].fields_by_name['hourly_prices']._loaded_options = None
    _globals['_MSGUPDATEDETAILSREQUEST'].fields_by_name['hourly_prices']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGUPDATEDETAILSREQUEST'].fields_by_name['remote_url']._loaded_options = None
    _globals['_MSGUPDATEDETAILSREQUEST'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_MSGREGISTERREQUEST']._serialized_start = 135
    _globals['_MSGREGISTERREQUEST']._serialized_end = 406
    _globals['_MSGUPDATEDETAILSREQUEST']._serialized_start = 409
    _globals['_MSGUPDATEDETAILSREQUEST']._serialized_end = 685
    _globals['_MSGUPDATESTATUSREQUEST']._serialized_start = 687
    _globals['_MSGUPDATESTATUSREQUEST']._serialized_end = 768
    _globals['_MSGSUBSCRIBEREQUEST']._serialized_start = 770
    _globals['_MSGSUBSCRIBEREQUEST']._serialized_end = 876
    _globals['_MSGREGISTERRESPONSE']._serialized_start = 878
    _globals['_MSGREGISTERRESPONSE']._serialized_end = 899
    _globals['_MSGUPDATEDETAILSRESPONSE']._serialized_start = 901
    _globals['_MSGUPDATEDETAILSRESPONSE']._serialized_end = 927
    _globals['_MSGUPDATESTATUSRESPONSE']._serialized_start = 929
    _globals['_MSGUPDATESTATUSRESPONSE']._serialized_end = 954
    _globals['_MSGSUBSCRIBERESPONSE']._serialized_start = 956
    _globals['_MSGSUBSCRIBERESPONSE']._serialized_end = 978
    _globals['_MSGSERVICE']._serialized_start = 981
    _globals['_MSGSERVICE']._serialized_end = 1391