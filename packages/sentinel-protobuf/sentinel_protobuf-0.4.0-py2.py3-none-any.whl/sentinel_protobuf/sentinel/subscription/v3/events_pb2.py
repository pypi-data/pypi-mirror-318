
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sentinel/subscription/v3/events.proto\x12\x18sentinel.subscription.v3\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"g\n\rEventAllocate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x15\n\rgranted_bytes\x18\x03 \x01(\t\x12\x16\n\x0eutilised_bytes\x18\x04 \x01(\t"x\n\x0bEventCreate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x14\n\x0cprov_address\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\t"\x80\x01\n\x12EventCreateSession\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12+\n\x0fsubscription_id\x18\x04 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID"\x8f\x01\n\x08EventPay\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x14\n\x0cprov_address\x18\x04 \x01(\t\x12\x0f\n\x07payment\x18\x05 \x01(\t\x12\x16\n\x0estaking_reward\x18\x06 \x01(\t"w\n\nEventRenew\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x14\n\x0cprov_address\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\t"\xc4\x01\n\x0bEventUpdate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x1c\n\x14renewal_price_policy\x18\x04 \x01(\t\x12)\n\x06status\x18\x05 \x01(\x0e2\x19.sentinel.types.v1.Status\x12\x13\n\x0binactive_at\x18\x06 \x01(\t\x12\x11\n\tstatus_at\x18\x07 \x01(\tBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v3.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTALLOCATE.fields_by_name['id']._options = None
    _EVENTALLOCATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTCREATE.fields_by_name['id']._options = None
    _EVENTCREATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTCREATE.fields_by_name['plan_id']._options = None
    _EVENTCREATE.fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _EVENTCREATESESSION.fields_by_name['id']._options = None
    _EVENTCREATESESSION.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTCREATESESSION.fields_by_name['subscription_id']._options = None
    _EVENTCREATESESSION.fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _EVENTPAY.fields_by_name['id']._options = None
    _EVENTPAY.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTPAY.fields_by_name['plan_id']._options = None
    _EVENTPAY.fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _EVENTRENEW.fields_by_name['id']._options = None
    _EVENTRENEW.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTRENEW.fields_by_name['plan_id']._options = None
    _EVENTRENEW.fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _EVENTUPDATE.fields_by_name['id']._options = None
    _EVENTUPDATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTUPDATE.fields_by_name['plan_id']._options = None
    _EVENTUPDATE.fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _EVENTALLOCATE._serialized_start = 121
    _EVENTALLOCATE._serialized_end = 224
    _EVENTCREATE._serialized_start = 226
    _EVENTCREATE._serialized_end = 346
    _EVENTCREATESESSION._serialized_start = 349
    _EVENTCREATESESSION._serialized_end = 477
    _EVENTPAY._serialized_start = 480
    _EVENTPAY._serialized_end = 623
    _EVENTRENEW._serialized_start = 625
    _EVENTRENEW._serialized_end = 744
    _EVENTUPDATE._serialized_start = 747
    _EVENTUPDATE._serialized_end = 943
