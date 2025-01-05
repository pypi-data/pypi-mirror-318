
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.lease.v1 import params_pb2 as sentinel_dot_lease_dot_v1_dot_params__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsentinel/lease/v1/msg.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/lease/v1/params.proto\x1a\x1fsentinel/types/v1/renewal.proto"6\n\x12MsgEndLeaseRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"V\n\x14MsgRenewLeaseRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05hours\x18\x03 \x01(\x03\x12\r\n\x05denom\x18\x04 \x01(\t"\x9d\x01\n\x14MsgStartLeaseRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\r\n\x05hours\x18\x03 \x01(\x03\x12\r\n\x05denom\x18\x04 \x01(\t\x12C\n\x14renewal_price_policy\x18\x05 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy"~\n\x15MsgUpdateLeaseRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12C\n\x14renewal_price_policy\x18\x03 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy"W\n\x16MsgUpdateParamsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12/\n\x06params\x18\x02 \x01(\x0b2\x19.sentinel.lease.v1.ParamsB\x04\xc8\xde\x1f\x00"\x15\n\x13MsgEndLeaseResponse"\x17\n\x15MsgRenewLeaseResponse"+\n\x15MsgStartLeaseResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x18\n\x16MsgUpdateLeaseResponse"\x19\n\x17MsgUpdateParamsResponse2\x83\x04\n\nMsgService\x12\\\n\x0bMsgEndLease\x12%.sentinel.lease.v1.MsgEndLeaseRequest\x1a&.sentinel.lease.v1.MsgEndLeaseResponse\x12b\n\rMsgRenewLease\x12\'.sentinel.lease.v1.MsgRenewLeaseRequest\x1a(.sentinel.lease.v1.MsgRenewLeaseResponse\x12b\n\rMsgStartLease\x12\'.sentinel.lease.v1.MsgStartLeaseRequest\x1a(.sentinel.lease.v1.MsgStartLeaseResponse\x12e\n\x0eMsgUpdateLease\x12(.sentinel.lease.v1.MsgUpdateLeaseRequest\x1a).sentinel.lease.v1.MsgUpdateLeaseResponse\x12h\n\x0fMsgUpdateParams\x12).sentinel.lease.v1.MsgUpdateParamsRequest\x1a*.sentinel.lease.v1.MsgUpdateParamsResponseB?Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.msg_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _MSGENDLEASEREQUEST.fields_by_name['id']._options = None
    _MSGENDLEASEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGRENEWLEASEREQUEST.fields_by_name['id']._options = None
    _MSGRENEWLEASEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGUPDATELEASEREQUEST.fields_by_name['id']._options = None
    _MSGUPDATELEASEREQUEST.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGUPDATEPARAMSREQUEST.fields_by_name['params']._options = None
    _MSGUPDATEPARAMSREQUEST.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGSTARTLEASERESPONSE.fields_by_name['id']._options = None
    _MSGSTARTLEASERESPONSE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _MSGENDLEASEREQUEST._serialized_start = 137
    _MSGENDLEASEREQUEST._serialized_end = 191
    _MSGRENEWLEASEREQUEST._serialized_start = 193
    _MSGRENEWLEASEREQUEST._serialized_end = 279
    _MSGSTARTLEASEREQUEST._serialized_start = 282
    _MSGSTARTLEASEREQUEST._serialized_end = 439
    _MSGUPDATELEASEREQUEST._serialized_start = 441
    _MSGUPDATELEASEREQUEST._serialized_end = 567
    _MSGUPDATEPARAMSREQUEST._serialized_start = 569
    _MSGUPDATEPARAMSREQUEST._serialized_end = 656
    _MSGENDLEASERESPONSE._serialized_start = 658
    _MSGENDLEASERESPONSE._serialized_end = 679
    _MSGRENEWLEASERESPONSE._serialized_start = 681
    _MSGRENEWLEASERESPONSE._serialized_end = 704
    _MSGSTARTLEASERESPONSE._serialized_start = 706
    _MSGSTARTLEASERESPONSE._serialized_end = 749
    _MSGUPDATELEASERESPONSE._serialized_start = 751
    _MSGUPDATELEASERESPONSE._serialized_end = 775
    _MSGUPDATEPARAMSRESPONSE._serialized_start = 777
    _MSGUPDATEPARAMSRESPONSE._serialized_end = 802
    _MSGSERVICE._serialized_start = 805
    _MSGSERVICE._serialized_end = 1320
