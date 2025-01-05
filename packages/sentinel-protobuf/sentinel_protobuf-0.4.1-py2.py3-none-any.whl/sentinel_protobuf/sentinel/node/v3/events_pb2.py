"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/node/v3/events.proto\x12\x10sentinel.node.v3\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"v\n\x0bEventCreate\x12\x14\n\x0cnode_address\x18\x01 \x01(\t\x12\x17\n\x0fgigabyte_prices\x18\x02 \x01(\t\x12\x15\n\rhourly_prices\x18\x03 \x01(\t\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"r\n\x08EventPay\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\x0f\n\x07payment\x18\x04 \x01(\t\x12\x16\n\x0estaking_reward\x18\x05 \x01(\t"F\n\x0bEventRefund\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x0e\n\x06amount\x18\x03 \x01(\t"}\n\x12EventUpdateDetails\x12\x14\n\x0cnode_address\x18\x01 \x01(\t\x12\x17\n\x0fgigabyte_prices\x18\x02 \x01(\t\x12\x15\n\rhourly_prices\x18\x03 \x01(\t\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"T\n\x11EventUpdateStatus\x12\x14\n\x0cnode_address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status"\x8c\x01\n\x12EventCreateSession\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\x12\x15\n\rmax_gigabytes\x18\x05 \x01(\x03\x12\x11\n\tmax_hours\x18\x06 \x01(\x03B>Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE'].fields_by_name['remote_url']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_EVENTPAY'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTREFUND'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['remote_url']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_EVENTCREATESESSION'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTCREATESESSION'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTCREATE']._serialized_start = 105
    _globals['_EVENTCREATE']._serialized_end = 223
    _globals['_EVENTPAY']._serialized_start = 225
    _globals['_EVENTPAY']._serialized_end = 339
    _globals['_EVENTREFUND']._serialized_start = 341
    _globals['_EVENTREFUND']._serialized_end = 411
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 413
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 538
    _globals['_EVENTUPDATESTATUS']._serialized_start = 540
    _globals['_EVENTUPDATESTATUS']._serialized_end = 624
    _globals['_EVENTCREATESESSION']._serialized_start = 627
    _globals['_EVENTCREATESESSION']._serialized_end = 767