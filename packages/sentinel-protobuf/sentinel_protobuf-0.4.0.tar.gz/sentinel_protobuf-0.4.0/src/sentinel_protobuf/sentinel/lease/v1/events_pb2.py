
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/lease/v1/events.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto"\x8d\x01\n\x0bEventCreate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x11\n\tmax_hours\x18\x04 \x01(\x03\x12\r\n\x05price\x18\x05 \x01(\t\x12\x1c\n\x14renewal_price_policy\x18\x06 \x01(\t"J\n\x08EventEnd\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t"s\n\x08EventPay\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x0f\n\x07payment\x18\x04 \x01(\t\x12\x16\n\x0estaking_reward\x18\x05 \x01(\t"G\n\x0bEventRefund\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x0e\n\x06amount\x18\x03 \x01(\t"n\n\nEventRenew\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x11\n\tmax_hours\x18\x04 \x01(\x03\x12\r\n\x05price\x18\x05 \x01(\t"\x8d\x01\n\x0bEventUpdate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\r\n\x05hours\x18\x04 \x01(\x03\x12\x1c\n\x14renewal_price_policy\x18\x05 \x01(\t\x12\x11\n\tpayout_at\x18\x06 \x01(\tB?Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTCREATE.fields_by_name['id']._options = None
    _EVENTCREATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTEND.fields_by_name['id']._options = None
    _EVENTEND.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTPAY.fields_by_name['id']._options = None
    _EVENTPAY.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTREFUND.fields_by_name['id']._options = None
    _EVENTREFUND.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTRENEW.fields_by_name['id']._options = None
    _EVENTRENEW.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTUPDATE.fields_by_name['id']._options = None
    _EVENTUPDATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTCREATE._serialized_start = 76
    _EVENTCREATE._serialized_end = 217
    _EVENTEND._serialized_start = 219
    _EVENTEND._serialized_end = 293
    _EVENTPAY._serialized_start = 295
    _EVENTPAY._serialized_end = 410
    _EVENTREFUND._serialized_start = 412
    _EVENTREFUND._serialized_end = 483
    _EVENTRENEW._serialized_start = 485
    _EVENTRENEW._serialized_end = 595
    _EVENTUPDATE._serialized_start = 598
    _EVENTUPDATE._serialized_end = 739
