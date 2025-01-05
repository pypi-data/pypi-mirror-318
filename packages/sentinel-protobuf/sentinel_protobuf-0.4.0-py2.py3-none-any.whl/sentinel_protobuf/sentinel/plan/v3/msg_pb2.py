
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/plan/v3/msg.proto\x12\x10sentinel.plan.v3\x1a\x14gogoproto/gogo.proto\x1a\x1dsentinel/types/v1/price.proto\x1a\x1fsentinel/types/v1/renewal.proto\x1a\x1esentinel/types/v1/status.proto"\x87\x01\n\x14MsgCreatePlanRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x11\n\tgigabytes\x18\x02 \x01(\x03\x12\r\n\x05hours\x18\x03 \x01(\x03\x12.\n\x06prices\x18\x04 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12\x0f\n\x07private\x18\x05 \x01(\x08"L\n\x12MsgLinkNodeRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"N\n\x14MsgUnlinkNodeRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"i\n\x1aMsgUpdatePlanStatusRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12)\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.Status"\xa4\x01\n\x16MsgStartSessionRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05denom\x18\x03 \x01(\t\x12C\n\x14renewal_price_policy\x18\x04 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy\x12\x14\n\x0cnode_address\x18\x05 \x01(\t"+\n\x15MsgCreatePlanResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x15\n\x13MsgLinkNodeResponse"\x17\n\x15MsgUnlinkNodeResponse"\x1d\n\x1bMsgUpdatePlanStatusResponse"-\n\x17MsgStartSessionResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID2\x88\x04\n\nMsgService\x12`\n\rMsgCreatePlan\x12&.sentinel.plan.v3.MsgCreatePlanRequest\x1a\'.sentinel.plan.v3.MsgCreatePlanResponse\x12Z\n\x0bMsgLinkNode\x12$.sentinel.plan.v3.MsgLinkNodeRequest\x1a%.sentinel.plan.v3.MsgLinkNodeResponse\x12`\n\rMsgUnlinkNode\x12&.sentinel.plan.v3.MsgUnlinkNodeRequest\x1a\'.sentinel.plan.v3.MsgUnlinkNodeResponse\x12r\n\x13MsgUpdatePlanStatus\x12,.sentinel.plan.v3.MsgUpdatePlanStatusRequest\x1a-.sentinel.plan.v3.MsgUpdatePlanStatusResponse\x12f\n\x0fMsgStartSession\x12(.sentinel.plan.v3.MsgStartSessionRequest\x1a).sentinel.plan.v3.MsgStartSessionResponseB>Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v3.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGCREATEPLANREQUEST.fields_by_name['prices']._options = None
    _MSGCREATEPLANREQUEST.fields_by_name['prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGLINKNODEREQUEST.fields_by_name['id']._options = None
    _MSGLINKNODEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGUNLINKNODEREQUEST.fields_by_name['id']._options = None
    _MSGUNLINKNODEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGUPDATEPLANSTATUSREQUEST.fields_by_name['id']._options = None
    _MSGUPDATEPLANSTATUSREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGSTARTSESSIONREQUEST.fields_by_name['id']._options = None
    _MSGSTARTSESSIONREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGCREATEPLANRESPONSE.fields_by_name['id']._options = None
    _MSGCREATEPLANRESPONSE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGSTARTSESSIONRESPONSE.fields_by_name['id']._options = None
    _MSGSTARTSESSIONRESPONSE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGCREATEPLANREQUEST._serialized_start = 167
    _MSGCREATEPLANREQUEST._serialized_end = 302
    _MSGLINKNODEREQUEST._serialized_start = 304
    _MSGLINKNODEREQUEST._serialized_end = 380
    _MSGUNLINKNODEREQUEST._serialized_start = 382
    _MSGUNLINKNODEREQUEST._serialized_end = 460
    _MSGUPDATEPLANSTATUSREQUEST._serialized_start = 462
    _MSGUPDATEPLANSTATUSREQUEST._serialized_end = 567
    _MSGSTARTSESSIONREQUEST._serialized_start = 570
    _MSGSTARTSESSIONREQUEST._serialized_end = 734
    _MSGCREATEPLANRESPONSE._serialized_start = 736
    _MSGCREATEPLANRESPONSE._serialized_end = 779
    _MSGLINKNODERESPONSE._serialized_start = 781
    _MSGLINKNODERESPONSE._serialized_end = 802
    _MSGUNLINKNODERESPONSE._serialized_start = 804
    _MSGUNLINKNODERESPONSE._serialized_end = 827
    _MSGUPDATEPLANSTATUSRESPONSE._serialized_start = 829
    _MSGUPDATEPLANSTATUSRESPONSE._serialized_end = 858
    _MSGSTARTSESSIONRESPONSE._serialized_start = 860
    _MSGSTARTSESSIONRESPONSE._serialized_end = 905
    _MSGSERVICE._serialized_start = 908
    _MSGSERVICE._serialized_end = 1428
