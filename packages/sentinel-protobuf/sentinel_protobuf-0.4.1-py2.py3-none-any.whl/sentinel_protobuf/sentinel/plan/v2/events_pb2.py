"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/plan/v2/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/plan/v2/events.proto\x12\x10sentinel.plan.v2\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"S\n\x0bEventCreate\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\x1f\n\x02id\x18\x02 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\x84\x01\n\rEventLinkNode\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\x86\x01\n\x0fEventUnlinkNode\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\x97\x01\n\x11EventUpdateStatus\x12<\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\xc5\x01\n\x17EventCreateSubscription\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x125\n\x10provider_address\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"provider_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"\x12-\n\x07plan_id\x18\x04 \x01(\x04B\x1c\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"B>Z4github.com/sentinel-official/hub/v12/x/plan/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v2.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTCREATE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTLINKNODE'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTLINKNODE'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTLINKNODE'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTLINKNODE'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTLINKNODE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTLINKNODE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUNLINKNODE'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUNLINKNODE'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUNLINKNODE'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTUNLINKNODE'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTUNLINKNODE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUNLINKNODE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['provider_address']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['provider_address']._serialized_options = b'\xf2\xde\x1f\x17yaml:"provider_address"'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"'
    _globals['_EVENTCREATE']._serialized_start = 105
    _globals['_EVENTCREATE']._serialized_end = 188
    _globals['_EVENTLINKNODE']._serialized_start = 191
    _globals['_EVENTLINKNODE']._serialized_end = 323
    _globals['_EVENTUNLINKNODE']._serialized_start = 326
    _globals['_EVENTUNLINKNODE']._serialized_end = 460
    _globals['_EVENTUPDATESTATUS']._serialized_start = 463
    _globals['_EVENTUPDATESTATUS']._serialized_end = 614
    _globals['_EVENTCREATESUBSCRIPTION']._serialized_start = 617
    _globals['_EVENTCREATESUBSCRIPTION']._serialized_end = 814