"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v2/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/node/v2/events.proto\x12\x10sentinel.node.v2\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"\x8e\x01\n\x17EventCreateSubscription\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""4\n\rEventRegister\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address""\xc2\x01\n\x12EventUpdateDetails\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x123\n\x0fgigabyte_prices\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"gigabyte_prices"\x12/\n\rhourly_prices\x18\x03 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"hourly_prices"\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"v\n\x11EventUpdateStatus\x12<\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"B>Z4github.com/sentinel-official/hub/v12/x/node/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v2.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTCREATESUBSCRIPTION'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTREGISTER'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTREGISTER'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['gigabyte_prices']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['gigabyte_prices']._serialized_options = b'\xf2\xde\x1f\x16yaml:"gigabyte_prices"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['hourly_prices']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['hourly_prices']._serialized_options = b'\xf2\xde\x1f\x14yaml:"hourly_prices"'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['remote_url']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTCREATESUBSCRIPTION']._serialized_start = 106
    _globals['_EVENTCREATESUBSCRIPTION']._serialized_end = 248
    _globals['_EVENTREGISTER']._serialized_start = 250
    _globals['_EVENTREGISTER']._serialized_end = 302
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 305
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 499
    _globals['_EVENTUPDATESTATUS']._serialized_start = 501
    _globals['_EVENTUPDATESTATUS']._serialized_end = 619