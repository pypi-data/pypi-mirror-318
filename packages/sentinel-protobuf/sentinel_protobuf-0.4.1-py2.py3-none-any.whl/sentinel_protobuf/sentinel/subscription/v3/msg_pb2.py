"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v3/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.subscription.v2 import params_pb2 as sentinel_dot_subscription_dot_v2_dot_params__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"sentinel/subscription/v3/msg.proto\x12\x18sentinel.subscription.v3\x1a\x14gogoproto/gogo.proto\x1a%sentinel/subscription/v2/params.proto\x1a\x1fsentinel/types/v1/renewal.proto"@\n\x1cMsgCancelSubscriptionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"N\n\x1bMsgRenewSubscriptionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05denom\x18\x03 \x01(\t"\x82\x01\n\x1bMsgShareSubscriptionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12,\n\x05bytes\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int"\x93\x01\n\x1bMsgStartSubscriptionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05denom\x18\x03 \x01(\t\x12C\n\x14renewal_price_policy\x18\x04 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy"\x85\x01\n\x1cMsgUpdateSubscriptionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12C\n\x14renewal_price_policy\x18\x03 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy"P\n\x16MsgStartSessionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"^\n\x16MsgUpdateParamsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x126\n\x06params\x18\x02 \x01(\x0b2 .sentinel.subscription.v2.ParamsB\x04\xc8\xde\x1f\x00"\x1f\n\x1dMsgCancelSubscriptionResponse"\x1e\n\x1cMsgRenewSubscriptionResponse"\x1e\n\x1cMsgShareSubscriptionResponse"2\n\x1cMsgStartSubscriptionResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x1f\n\x1dMsgUpdateSubscriptionResponse"-\n\x17MsgStartSessionResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x19\n\x17MsgUpdateParamsResponse2\xaa\x07\n\nMsgService\x12\x88\x01\n\x15MsgCancelSubscription\x126.sentinel.subscription.v3.MsgCancelSubscriptionRequest\x1a7.sentinel.subscription.v3.MsgCancelSubscriptionResponse\x12\x85\x01\n\x14MsgRenewSubscription\x125.sentinel.subscription.v3.MsgRenewSubscriptionRequest\x1a6.sentinel.subscription.v3.MsgRenewSubscriptionResponse\x12\x85\x01\n\x14MsgShareSubscription\x125.sentinel.subscription.v3.MsgShareSubscriptionRequest\x1a6.sentinel.subscription.v3.MsgShareSubscriptionResponse\x12\x85\x01\n\x14MsgStartSubscription\x125.sentinel.subscription.v3.MsgStartSubscriptionRequest\x1a6.sentinel.subscription.v3.MsgStartSubscriptionResponse\x12\x88\x01\n\x15MsgUpdateSubscription\x126.sentinel.subscription.v3.MsgUpdateSubscriptionRequest\x1a7.sentinel.subscription.v3.MsgUpdateSubscriptionResponse\x12v\n\x0fMsgStartSession\x120.sentinel.subscription.v3.MsgStartSessionRequest\x1a1.sentinel.subscription.v3.MsgStartSessionResponse\x12v\n\x0fMsgUpdateParams\x120.sentinel.subscription.v3.MsgUpdateParamsRequest\x1a1.sentinel.subscription.v3.MsgUpdateParamsResponseBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v3.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGCANCELSUBSCRIPTIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGCANCELSUBSCRIPTIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGRENEWSUBSCRIPTIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGRENEWSUBSCRIPTIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSHARESUBSCRIPTIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSHARESUBSCRIPTIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSHARESUBSCRIPTIONREQUEST'].fields_by_name['bytes']._loaded_options = None
    _globals['_MSGSHARESUBSCRIPTIONREQUEST'].fields_by_name['bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_MSGSTARTSUBSCRIPTIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSUBSCRIPTIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATESUBSCRIPTIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUPDATESUBSCRIPTIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSTARTSESSIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSESSIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGSTARTSUBSCRIPTIONRESPONSE'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSUBSCRIPTIONRESPONSE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSTARTSESSIONRESPONSE'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSESSIONRESPONSE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGCANCELSUBSCRIPTIONREQUEST']._serialized_start = 158
    _globals['_MSGCANCELSUBSCRIPTIONREQUEST']._serialized_end = 222
    _globals['_MSGRENEWSUBSCRIPTIONREQUEST']._serialized_start = 224
    _globals['_MSGRENEWSUBSCRIPTIONREQUEST']._serialized_end = 302
    _globals['_MSGSHARESUBSCRIPTIONREQUEST']._serialized_start = 305
    _globals['_MSGSHARESUBSCRIPTIONREQUEST']._serialized_end = 435
    _globals['_MSGSTARTSUBSCRIPTIONREQUEST']._serialized_start = 438
    _globals['_MSGSTARTSUBSCRIPTIONREQUEST']._serialized_end = 585
    _globals['_MSGUPDATESUBSCRIPTIONREQUEST']._serialized_start = 588
    _globals['_MSGUPDATESUBSCRIPTIONREQUEST']._serialized_end = 721
    _globals['_MSGSTARTSESSIONREQUEST']._serialized_start = 723
    _globals['_MSGSTARTSESSIONREQUEST']._serialized_end = 803
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 805
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 899
    _globals['_MSGCANCELSUBSCRIPTIONRESPONSE']._serialized_start = 901
    _globals['_MSGCANCELSUBSCRIPTIONRESPONSE']._serialized_end = 932
    _globals['_MSGRENEWSUBSCRIPTIONRESPONSE']._serialized_start = 934
    _globals['_MSGRENEWSUBSCRIPTIONRESPONSE']._serialized_end = 964
    _globals['_MSGSHARESUBSCRIPTIONRESPONSE']._serialized_start = 966
    _globals['_MSGSHARESUBSCRIPTIONRESPONSE']._serialized_end = 996
    _globals['_MSGSTARTSUBSCRIPTIONRESPONSE']._serialized_start = 998
    _globals['_MSGSTARTSUBSCRIPTIONRESPONSE']._serialized_end = 1048
    _globals['_MSGUPDATESUBSCRIPTIONRESPONSE']._serialized_start = 1050
    _globals['_MSGUPDATESUBSCRIPTIONRESPONSE']._serialized_end = 1081
    _globals['_MSGSTARTSESSIONRESPONSE']._serialized_start = 1083
    _globals['_MSGSTARTSESSIONRESPONSE']._serialized_end = 1128
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 1130
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 1155
    _globals['_MSGSERVICE']._serialized_start = 1158
    _globals['_MSGSERVICE']._serialized_end = 2096