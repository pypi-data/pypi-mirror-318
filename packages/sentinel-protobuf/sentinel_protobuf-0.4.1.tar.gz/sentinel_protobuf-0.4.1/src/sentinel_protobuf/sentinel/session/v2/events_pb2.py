"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v2/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/session/v2/events.proto\x12\x13sentinel.session.v2\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"\xf7\x01\n\nEventStart\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"\x12-\n\x07plan_id\x18\x04 \x01(\x04B\x1c\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"\x12E\n\x0fsubscription_id\x18\x05 \x01(\x04B,\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id""\xff\x01\n\x12EventUpdateDetails\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"\x12-\n\x07plan_id\x18\x04 \x01(\x04B\x1c\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"\x12E\n\x0fsubscription_id\x18\x05 \x01(\x04B,\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id""\xbc\x02\n\x11EventUpdateStatus\x12<\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x03 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x04 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"\x12-\n\x07plan_id\x18\x05 \x01(\x04B\x1c\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"\x12E\n\x0fsubscription_id\x18\x06 \x01(\x04B,\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id"BAZ7github.com/sentinel-official/hub/v12/x/session/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v2.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTSTART'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTSTART'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTSTART'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTSTART'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"'
    _globals['_EVENTSTART'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id"'
    _globals['_EVENTSTART']._serialized_start = 112
    _globals['_EVENTSTART']._serialized_end = 359
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 362
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 617
    _globals['_EVENTUPDATESTATUS']._serialized_start = 620
    _globals['_EVENTUPDATESTATUS']._serialized_end = 936